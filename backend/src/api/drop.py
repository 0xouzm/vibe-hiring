"""Drop routes — weekly curated match delivery."""

import json

from fastapi import APIRouter, Depends, HTTPException, status

import aiosqlite

from src.core.deps import get_db, get_current_user_id
from src.models.dna_score import DimensionScores
from src.models.match import DropResponse, MatchResponse, MatchStatus
from src.services.drop import generate_drop, get_current_drop

router = APIRouter()


def _build_match_response(match_data: dict) -> MatchResponse:
    """Convert a raw match dict from the drop service into a MatchResponse."""
    dim_scores = match_data["dimension_scores"]
    if isinstance(dim_scores, str):
        dim_scores = json.loads(dim_scores)

    return MatchResponse(
        id=match_data["id"],
        candidate_id=match_data["candidate_id"],
        company_id=match_data["company_id"],
        company_name=match_data.get("company_name", ""),
        score=match_data["score"],
        dimension_scores=DimensionScores.model_validate(dim_scores),
        report=match_data.get("report"),
        status=MatchStatus(match_data["status"]),
    )


async def _enrich_matches_with_company_names(
    db: aiosqlite.Connection,
    matches: list[dict],
) -> list[dict]:
    """Add company_name to each match dict."""
    for match in matches:
        cursor = await db.execute(
            "SELECT name FROM companies WHERE id = ?",
            (match["company_id"],),
        )
        row = await cursor.fetchone()
        match["company_name"] = row["name"] if row else "Unknown"
    return matches


@router.get("/drops/current", response_model=DropResponse)
async def current_drop(
    user_id: str = Depends(get_current_user_id),
    db: aiosqlite.Connection = Depends(get_db),
):
    """Get the current week's drop for the authenticated candidate.

    If no drop exists yet, auto-generates one from pending matches.
    """
    # Verify user is a candidate
    cursor = await db.execute(
        "SELECT role FROM users WHERE id = ?", (user_id,)
    )
    user_row = await cursor.fetchone()
    if not user_row or user_row["role"] != "candidate":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only candidates can receive drops",
        )

    # Try to fetch existing drop
    drop_data = await get_current_drop(db, user_id)

    # Auto-generate if none exists
    if not drop_data:
        try:
            await generate_drop(db, user_id)
        except ValueError as exc:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(exc),
            )
        drop_data = await get_current_drop(db, user_id)

    if not drop_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No matches available for drop",
        )

    # Enrich matches with company names
    enriched = await _enrich_matches_with_company_names(db, drop_data["matches"])
    match_responses = [_build_match_response(m) for m in enriched]

    return DropResponse(
        id=drop_data["id"],
        week=drop_data["week"],
        matches=match_responses,
        revealed_at=drop_data.get("revealed_at"),
    )
