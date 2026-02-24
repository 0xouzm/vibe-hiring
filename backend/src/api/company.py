"""Company management routes — create, invite employees, query CAS."""

import json
import uuid
from datetime import datetime, timezone

import bcrypt as _bcrypt
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import TypeAdapter

import aiosqlite

from src.core.deps import get_db, get_current_user_id
from src.models.company import (
    CASResponse,
    CompanyCreate,
    CompanyResponse,
    InviteRequest,
)
from src.models.dna_score import DimensionScores
from src.models.match import CompanyMatchResponse, MatchStatus
from src.models.questionnaire import Answer
from src.services.company_scoring import calculate_company_dna
from src.services.cas import calculate_cas

router = APIRouter()

_answer_list_adapter = TypeAdapter(list[Answer])


@router.post("/", response_model=CompanyResponse)
async def create_company(
    body: CompanyCreate,
    user_id: str = Depends(get_current_user_id),
    db: aiosqlite.Connection = Depends(get_db),
):
    """Create a new company profile (HR only)."""
    # Verify role
    cursor = await db.execute(
        "SELECT role, company_id FROM users WHERE id = ?", (user_id,)
    )
    user_row = await cursor.fetchone()

    if not user_row or user_row["role"] != "hr":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only HR users can create companies",
        )
    if user_row["company_id"]:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already belongs to a company",
        )

    company_id = str(uuid.uuid4())
    now = datetime.now(tz=timezone.utc).isoformat()

    await db.execute(
        """
        INSERT INTO companies (id, name, industry, size, created_at)
        VALUES (?, ?, ?, ?, ?)
        """,
        (company_id, body.name, body.industry, body.size, now),
    )

    # Link user to company
    await db.execute(
        "UPDATE users SET company_id = ? WHERE id = ?",
        (company_id, user_id),
    )
    await db.commit()

    return CompanyResponse(
        id=company_id,
        name=body.name,
        industry=body.industry,
        size=body.size,
    )


@router.post("/{company_id}/invite", response_model=dict)
async def invite_employee(
    company_id: str,
    body: InviteRequest,
    user_id: str = Depends(get_current_user_id),
    db: aiosqlite.Connection = Depends(get_db),
):
    """Invite an employee to fill the Company DNA survey.

    Demo simplification: creates a user account directly (no email).
    """
    # Verify caller is HR for this company
    cursor = await db.execute(
        "SELECT role, company_id FROM users WHERE id = ?", (user_id,)
    )
    user_row = await cursor.fetchone()

    if not user_row or user_row["role"] != "hr" or user_row["company_id"] != company_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only HR of this company can invite employees",
        )

    # Check if email already exists
    cursor = await db.execute(
        "SELECT id FROM users WHERE email = ?", (body.email,)
    )
    if await cursor.fetchone():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered",
        )

    # Create employee account with a default password
    new_user_id = str(uuid.uuid4())
    now = datetime.now(tz=timezone.utc).isoformat()
    default_password = _bcrypt.hashpw(b"welcome123", _bcrypt.gensalt()).decode()

    await db.execute(
        """
        INSERT INTO users (id, email, name, role, password_hash, company_id, created_at)
        VALUES (?, ?, ?, 'hr', ?, ?, ?)
        """,
        (new_user_id, body.email, body.name, default_password, company_id, now),
    )
    await db.commit()

    return {
        "user_id": new_user_id,
        "email": body.email,
        "message": "Employee account created. Default password: welcome123",
    }


@router.get("/{company_id}", response_model=CompanyResponse)
async def get_company(
    company_id: str,
    db: aiosqlite.Connection = Depends(get_db),
):
    """Retrieve a company's public profile."""
    cursor = await db.execute(
        "SELECT * FROM companies WHERE id = ?", (company_id,)
    )
    row = await cursor.fetchone()

    if not row:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found",
        )

    return CompanyResponse(
        id=row["id"],
        name=row["name"],
        industry=row["industry"],
        size=row["size"],
    )


@router.get("/{company_id}/cas", response_model=CASResponse)
async def get_cas(
    company_id: str,
    db: aiosqlite.Connection = Depends(get_db),
):
    """Retrieve the Culture Authenticity Score for a company."""
    # Verify company exists
    cursor = await db.execute(
        "SELECT id FROM companies WHERE id = ?", (company_id,)
    )
    if not await cursor.fetchone():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found",
        )

    # Re-derive CAS from company_answers
    cursor = await db.execute(
        """
        SELECT ca.answers, u.role
        FROM company_answers ca
        JOIN users u ON u.id = ca.user_id
        WHERE ca.company_id = ?
        """,
        (company_id,),
    )
    rows = await cursor.fetchall()

    if not rows:
        return CASResponse(
            company_id=company_id,
            score=0.0,
            tier="none",
            internal_consistency=1.0,
            hr_employee_alignment=1.0,
        )

    hr_scores: list[DimensionScores] = []
    employee_scores: list[DimensionScores] = []

    for row in rows:
        answers = _answer_list_adapter.validate_python(json.loads(row["answers"]))
        individual = calculate_company_dna(answers)
        if row["role"] == "hr":
            hr_scores.append(individual)
        else:
            employee_scores.append(individual)

    cas_result = calculate_cas(hr_scores, employee_scores)

    return CASResponse(
        company_id=company_id,
        score=cas_result.score,
        tier=cas_result.tier,
        internal_consistency=cas_result.internal_consistency,
        hr_employee_alignment=cas_result.hr_employee_alignment,
    )


@router.get(
    "/{company_id}/matches", response_model=list[CompanyMatchResponse]
)
async def get_company_matches(
    company_id: str,
    user_id: str = Depends(get_current_user_id),
    db: aiosqlite.Connection = Depends(get_db),
):
    """Retrieve all matches for a company, ordered by score descending."""
    # Verify caller is HR for this company
    cursor = await db.execute(
        "SELECT role, company_id FROM users WHERE id = ?", (user_id,)
    )
    user_row = await cursor.fetchone()

    if (
        not user_row
        or user_row["role"] != "hr"
        or user_row["company_id"] != company_id
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only HR of this company can view matches",
        )

    cursor = await db.execute(
        """
        SELECT m.id, m.candidate_id, m.company_id, m.score,
               m.dimension_scores, m.report, m.status, u.name as candidate_name
        FROM matches m
        JOIN users u ON u.id = m.candidate_id
        WHERE m.company_id = ?
        ORDER BY m.score DESC
        """,
        (company_id,),
    )
    rows = await cursor.fetchall()

    return [
        CompanyMatchResponse(
            id=row["id"],
            candidate_id=row["candidate_id"],
            candidate_name=row["candidate_name"],
            company_id=row["company_id"],
            score=row["score"],
            dimension_scores=DimensionScores.model_validate(
                json.loads(row["dimension_scores"]),
            ),
            report=row["report"],
            status=MatchStatus(row["status"]),
        )
        for row in rows
    ]
