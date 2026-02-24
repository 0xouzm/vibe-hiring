"""DNA score query routes — retrieve candidate and company profiles."""

import json

from fastapi import APIRouter, Depends, HTTPException, status

import aiosqlite

from src.core.deps import get_db
from src.models.dna_score import DNAScoreResponse, DimensionScores

router = APIRouter()


@router.get("/candidate/{candidate_id}", response_model=DNAScoreResponse)
async def get_candidate_score(
    candidate_id: str,
    db: aiosqlite.Connection = Depends(get_db),
):
    """Retrieve a candidate's Career DNA score profile."""
    cursor = await db.execute(
        """
        SELECT entity_type, entity_id, scores, consistency
        FROM dna_scores
        WHERE entity_type = 'candidate' AND entity_id = ?
        """,
        (candidate_id,),
    )
    row = await cursor.fetchone()

    if not row:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Candidate score not found",
        )

    return DNAScoreResponse(
        entity_type=row["entity_type"],
        entity_id=row["entity_id"],
        scores=DimensionScores.model_validate_json(row["scores"]),
        consistency=row["consistency"],
    )


@router.get("/company/{company_id}", response_model=DNAScoreResponse)
async def get_company_score(
    company_id: str,
    db: aiosqlite.Connection = Depends(get_db),
):
    """Retrieve a company's aggregated DNA score profile."""
    cursor = await db.execute(
        """
        SELECT entity_type, entity_id, scores, consistency
        FROM dna_scores
        WHERE entity_type = 'company' AND entity_id = ?
        """,
        (company_id,),
    )
    row = await cursor.fetchone()

    if not row:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company score not found",
        )

    return DNAScoreResponse(
        entity_type=row["entity_type"],
        entity_id=row["entity_id"],
        scores=DimensionScores.model_validate_json(row["scores"]),
        consistency=row["consistency"],
    )
