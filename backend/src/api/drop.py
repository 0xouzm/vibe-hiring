"""Drop routes — weekly curated match delivery for candidates and companies."""

import json

from fastapi import APIRouter, Depends, HTTPException, status

import aiosqlite

from src.core.deps import get_db, get_current_user_id
from src.models.dna_score import DimensionScores
from src.models.match import (
    CompanyDropResponse,
    CompanyMatchResponse,
    DropResponse,
    MatchResponse,
    MatchStatus,
)
from src.services.drop import (
    generate_candidate_drop,
    generate_company_drop,
    get_current_drop,
)

router = APIRouter()


def _build_match_response(match_data: dict) -> MatchResponse:
    """Convert a raw match dict into a MatchResponse."""
    dim_scores = match_data["dimension_scores"]
    if isinstance(dim_scores, str):
        dim_scores = json.loads(dim_scores)

    return MatchResponse(
        id=match_data["id"],
        candidate_id=match_data["candidate_id"],
        company_id=match_data["company_id"],
        company_name=match_data.get("company_name", ""),
        role_id=match_data.get("role_id"),
        role_title=match_data.get("role_title"),
        score=match_data["score"],
        dimension_scores=DimensionScores.model_validate(dim_scores),
        report=match_data.get("report"),
        status=MatchStatus(match_data["status"]),
        candidate_action=match_data.get("candidate_action"),
        company_action=match_data.get("company_action"),
    )


def _build_company_match(match_data: dict) -> CompanyMatchResponse:
    """Convert a raw match dict into a CompanyMatchResponse."""
    dim_scores = match_data["dimension_scores"]
    if isinstance(dim_scores, str):
        dim_scores = json.loads(dim_scores)

    return CompanyMatchResponse(
        id=match_data["id"],
        candidate_id=match_data["candidate_id"],
        candidate_name=match_data.get("candidate_name", ""),
        company_id=match_data["company_id"],
        role_id=match_data.get("role_id"),
        role_title=match_data.get("role_title"),
        score=match_data["score"],
        dimension_scores=DimensionScores.model_validate(dim_scores),
        report=match_data.get("report"),
        status=MatchStatus(match_data["status"]),
        candidate_action=match_data.get("candidate_action"),
        company_action=match_data.get("company_action"),
    )


async def _enrich_candidate_matches(
    db: aiosqlite.Connection, matches: list[dict],
) -> list[dict]:
    """Add company_name and role_title to each match."""
    for match in matches:
        cursor = await db.execute(
            "SELECT name FROM companies WHERE id = ?",
            (match["company_id"],),
        )
        row = await cursor.fetchone()
        match["company_name"] = row["name"] if row else "Unknown"

        if match.get("role_id"):
            cursor = await db.execute(
                "SELECT title FROM roles WHERE id = ?",
                (match["role_id"],),
            )
            row = await cursor.fetchone()
            match["role_title"] = row["title"] if row else None
    return matches


async def _enrich_company_matches(
    db: aiosqlite.Connection, matches: list[dict],
) -> list[dict]:
    """Add candidate_name and role_title to each match."""
    for match in matches:
        cursor = await db.execute(
            "SELECT name FROM users WHERE id = ?",
            (match["candidate_id"],),
        )
        row = await cursor.fetchone()
        match["candidate_name"] = row["name"] if row else "Unknown"

        if match.get("role_id"):
            cursor = await db.execute(
                "SELECT title FROM roles WHERE id = ?",
                (match["role_id"],),
            )
            row = await cursor.fetchone()
            match["role_title"] = row["title"] if row else None
    return matches


@router.get("/drops/current", response_model=DropResponse)
async def candidate_current_drop(
    user_id: str = Depends(get_current_user_id),
    db: aiosqlite.Connection = Depends(get_db),
):
    """Get the current week's drop for the authenticated candidate."""
    cursor = await db.execute(
        "SELECT role FROM users WHERE id = ?", (user_id,)
    )
    user_row = await cursor.fetchone()
    if not user_row or user_row["role"] != "candidate":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only candidates can receive candidate drops",
        )

    drop_data = await get_current_drop(db, user_id, "candidate")

    if not drop_data:
        try:
            await generate_candidate_drop(db, user_id)
        except ValueError as exc:
            raise HTTPException(status_code=404, detail=str(exc))
        drop_data = await get_current_drop(db, user_id, "candidate")

    if not drop_data:
        raise HTTPException(status_code=404, detail="No matches available")

    enriched = await _enrich_candidate_matches(db, drop_data["matches"])
    return DropResponse(
        id=drop_data["id"],
        week=drop_data["week"],
        matches=[_build_match_response(m) for m in enriched],
        revealed_at=drop_data.get("revealed_at"),
    )


@router.get("/drops/company/current", response_model=CompanyDropResponse)
async def company_current_drop(
    user_id: str = Depends(get_current_user_id),
    db: aiosqlite.Connection = Depends(get_db),
):
    """Get the current week's drop for the authenticated HR user's company."""
    cursor = await db.execute(
        "SELECT role, company_id FROM users WHERE id = ?", (user_id,)
    )
    user_row = await cursor.fetchone()
    if not user_row or user_row["role"] != "hr" or not user_row["company_id"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only HR users can view company drops",
        )

    company_id = user_row["company_id"]
    drop_data = await get_current_drop(db, company_id, "company")

    if not drop_data:
        try:
            await generate_company_drop(db, company_id)
        except ValueError as exc:
            raise HTTPException(status_code=404, detail=str(exc))
        drop_data = await get_current_drop(db, company_id, "company")

    if not drop_data:
        raise HTTPException(status_code=404, detail="No matches available")

    enriched = await _enrich_company_matches(db, drop_data["matches"])
    return CompanyDropResponse(
        id=drop_data["id"],
        week=drop_data["week"],
        matches=[_build_company_match(m) for m in enriched],
        revealed_at=drop_data.get("revealed_at"),
    )
