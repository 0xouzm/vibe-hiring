"""Role management routes — CRUD for open positions."""

import json
import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status

import aiosqlite

from src.core.deps import get_db, get_current_user_id
from src.models.role import RoleCreate, RoleResponse, RoleUpdate, SalaryRange

router = APIRouter()


def _row_to_response(row: aiosqlite.Row, company_name: str = "") -> RoleResponse:
    """Convert a database row to a RoleResponse."""
    salary = json.loads(row["salary_range"]) if row["salary_range"] else None
    return RoleResponse(
        id=row["id"],
        company_id=row["company_id"],
        company_name=company_name,
        title=row["title"],
        level=row["level"],
        skills=json.loads(row["skills"]) if row["skills"] else [],
        nice_to_have=json.loads(row["nice_to_have"]) if row["nice_to_have"] else [],
        salary_range=SalaryRange(**salary) if salary else None,
        location=row["location"],
        remote_policy=row["remote_policy"],
        description=row["description"],
        is_active=bool(row["is_active"]),
        created_at=row["created_at"],
    )


async def _get_user_company(db: aiosqlite.Connection, user_id: str) -> str:
    """Get the company_id for an HR user, raise 403 if not HR."""
    cursor = await db.execute(
        "SELECT role, company_id FROM users WHERE id = ?", (user_id,)
    )
    row = await cursor.fetchone()
    if not row or row["role"] != "hr" or not row["company_id"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only HR users can manage roles",
        )
    return row["company_id"]


@router.post("", response_model=RoleResponse, status_code=201)
async def create_role(
    body: RoleCreate,
    user_id: str = Depends(get_current_user_id),
    db: aiosqlite.Connection = Depends(get_db),
):
    """Create a new open role for the user's company."""
    company_id = await _get_user_company(db, user_id)

    role_id = str(uuid.uuid4())
    now = datetime.now(tz=timezone.utc).isoformat()

    await db.execute(
        """
        INSERT INTO roles (id, company_id, title, level, skills, nice_to_have,
                          salary_range, location, remote_policy, description, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            role_id,
            company_id,
            body.title,
            body.level,
            json.dumps(body.skills),
            json.dumps(body.nice_to_have),
            json.dumps(body.salary_range.model_dump()) if body.salary_range else None,
            body.location,
            body.remote_policy,
            body.description,
            now,
        ),
    )
    await db.commit()

    # Fetch company name
    cursor = await db.execute(
        "SELECT name FROM companies WHERE id = ?", (company_id,)
    )
    comp = await cursor.fetchone()

    cursor = await db.execute("SELECT * FROM roles WHERE id = ?", (role_id,))
    row = await cursor.fetchone()
    return _row_to_response(row, comp["name"] if comp else "")


@router.get("", response_model=list[RoleResponse])
async def list_roles(
    company_id: str | None = None,
    db: aiosqlite.Connection = Depends(get_db),
):
    """List roles, optionally filtered by company."""
    if company_id:
        cursor = await db.execute(
            """SELECT r.*, c.name as company_name FROM roles r
               JOIN companies c ON c.id = r.company_id
               WHERE r.company_id = ? AND r.is_active = 1
               ORDER BY r.created_at DESC""",
            (company_id,),
        )
    else:
        cursor = await db.execute(
            """SELECT r.*, c.name as company_name FROM roles r
               JOIN companies c ON c.id = r.company_id
               WHERE r.is_active = 1
               ORDER BY r.created_at DESC""",
        )

    rows = await cursor.fetchall()
    return [_row_to_response(r, r["company_name"]) for r in rows]


@router.get("/{role_id}", response_model=RoleResponse)
async def get_role(
    role_id: str,
    db: aiosqlite.Connection = Depends(get_db),
):
    """Get a single role by ID."""
    cursor = await db.execute(
        """SELECT r.*, c.name as company_name FROM roles r
           JOIN companies c ON c.id = r.company_id
           WHERE r.id = ?""",
        (role_id,),
    )
    row = await cursor.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Role not found")
    return _row_to_response(row, row["company_name"])


@router.put("/{role_id}", response_model=RoleResponse)
async def update_role(
    role_id: str,
    body: RoleUpdate,
    user_id: str = Depends(get_current_user_id),
    db: aiosqlite.Connection = Depends(get_db),
):
    """Update an existing role."""
    company_id = await _get_user_company(db, user_id)

    # Verify role belongs to company
    cursor = await db.execute(
        "SELECT company_id FROM roles WHERE id = ?", (role_id,)
    )
    row = await cursor.fetchone()
    if not row or row["company_id"] != company_id:
        raise HTTPException(status_code=404, detail="Role not found")

    updates: list[str] = []
    values: list = []
    for field, col in [
        ("title", "title"), ("level", "level"),
        ("location", "location"), ("remote_policy", "remote_policy"),
        ("description", "description"),
    ]:
        val = getattr(body, field)
        if val is not None:
            updates.append(f"{col} = ?")
            values.append(val)

    if body.skills is not None:
        updates.append("skills = ?")
        values.append(json.dumps(body.skills))
    if body.nice_to_have is not None:
        updates.append("nice_to_have = ?")
        values.append(json.dumps(body.nice_to_have))
    if body.salary_range is not None:
        updates.append("salary_range = ?")
        values.append(json.dumps(body.salary_range.model_dump()))
    if body.is_active is not None:
        updates.append("is_active = ?")
        values.append(int(body.is_active))

    if updates:
        values.append(role_id)
        await db.execute(
            f"UPDATE roles SET {', '.join(updates)} WHERE id = ?", values
        )
        await db.commit()

    return await get_role(role_id, db)


@router.delete("/{role_id}", status_code=204)
async def deactivate_role(
    role_id: str,
    user_id: str = Depends(get_current_user_id),
    db: aiosqlite.Connection = Depends(get_db),
):
    """Soft-delete a role by setting is_active = 0."""
    company_id = await _get_user_company(db, user_id)

    cursor = await db.execute(
        "SELECT company_id FROM roles WHERE id = ?", (role_id,)
    )
    row = await cursor.fetchone()
    if not row or row["company_id"] != company_id:
        raise HTTPException(status_code=404, detail="Role not found")

    await db.execute("UPDATE roles SET is_active = 0 WHERE id = ?", (role_id,))
    await db.commit()
