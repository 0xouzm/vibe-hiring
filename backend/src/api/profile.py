"""User profile routes — view and update candidate profiles."""

import json
import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException

import aiosqlite

from src.core.deps import get_db, get_current_user_id
from src.models.profile import ProfileResponse, ProfileUpdate

router = APIRouter()


def _row_to_response(row: aiosqlite.Row) -> ProfileResponse:
    """Convert a database row to a ProfileResponse."""
    return ProfileResponse(
        id=row["id"],
        user_id=row["user_id"],
        title=row["title"],
        years_experience=row["years_experience"],
        skills=json.loads(row["skills"]) if row["skills"] else [],
        education=json.loads(row["education"]) if row["education"] else [],
        bio=row["bio"],
        resume_text=row["resume_text"],
        chat_summary=row["chat_summary"],
        location=row["location"],
        remote_preference=row["remote_preference"],
        salary_expectation=(
            json.loads(row["salary_expectation"]) if row["salary_expectation"] else None
        ),
        created_at=row["created_at"],
        updated_at=row["updated_at"],
    )


@router.get("/{user_id}", response_model=ProfileResponse)
async def get_profile(
    user_id: str,
    db: aiosqlite.Connection = Depends(get_db),
):
    """Get a user's profile."""
    cursor = await db.execute(
        "SELECT * FROM user_profiles WHERE user_id = ?", (user_id,)
    )
    row = await cursor.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Profile not found")
    return _row_to_response(row)


@router.put("", response_model=ProfileResponse)
async def update_profile(
    body: ProfileUpdate,
    user_id: str = Depends(get_current_user_id),
    db: aiosqlite.Connection = Depends(get_db),
):
    """Update the authenticated user's profile (upsert)."""
    now = datetime.now(tz=timezone.utc).isoformat()

    # Check if profile exists
    cursor = await db.execute(
        "SELECT id FROM user_profiles WHERE user_id = ?", (user_id,)
    )
    existing = await cursor.fetchone()

    if existing:
        updates: list[str] = []
        values: list = []

        for field, col in [
            ("title", "title"), ("bio", "bio"),
            ("location", "location"), ("remote_preference", "remote_preference"),
        ]:
            val = getattr(body, field)
            if val is not None:
                updates.append(f"{col} = ?")
                values.append(val)

        if body.years_experience is not None:
            updates.append("years_experience = ?")
            values.append(body.years_experience)
        if body.skills is not None:
            updates.append("skills = ?")
            values.append(json.dumps(body.skills))
        if body.education is not None:
            updates.append("education = ?")
            values.append(json.dumps(body.education))
        if body.salary_expectation is not None:
            updates.append("salary_expectation = ?")
            values.append(json.dumps(body.salary_expectation))

        updates.append("updated_at = ?")
        values.append(now)
        values.append(user_id)

        await db.execute(
            f"UPDATE user_profiles SET {', '.join(updates)} WHERE user_id = ?",
            values,
        )
    else:
        profile_id = str(uuid.uuid4())
        await db.execute(
            """
            INSERT INTO user_profiles
                (id, user_id, title, years_experience, skills, education,
                 bio, location, remote_preference, salary_expectation,
                 created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                profile_id, user_id,
                body.title, body.years_experience,
                json.dumps(body.skills) if body.skills else None,
                json.dumps(body.education) if body.education else None,
                body.bio, body.location, body.remote_preference,
                json.dumps(body.salary_expectation) if body.salary_expectation else None,
                now, now,
            ),
        )

    await db.commit()
    return await get_profile(user_id, db)
