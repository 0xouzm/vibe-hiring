"""Matching routes — run matching, query matches, accept/pass."""

import json
import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status

import aiosqlite

from src.core.deps import get_db, get_current_user_id
from src.models.dna_score import DimensionScores
from src.models.match import MatchActionRequest, MatchResponse, MatchStatus
from src.services.matching import run_matching
from src.services.report import generate_simple_report

router = APIRouter()


async def _fetch_candidates(db: aiosqlite.Connection) -> list[dict]:
    """Fetch all candidates with DNA scores."""
    cursor = await db.execute(
        """
        SELECT u.id, u.name, ds.scores, ds.consistency
        FROM users u
        JOIN dna_scores ds ON ds.entity_id = u.id AND ds.entity_type = 'candidate'
        WHERE u.role = 'candidate'
        """,
    )
    rows = await cursor.fetchall()
    return [
        {
            "id": r["id"],
            "name": r["name"],
            "scores": DimensionScores.model_validate_json(r["scores"]),
            "consistency": r["consistency"],
        }
        for r in rows
    ]


async def _fetch_companies(db: aiosqlite.Connection) -> list[dict]:
    """Fetch all companies with aggregated DNA scores."""
    cursor = await db.execute(
        """
        SELECT c.id, c.name, ds.scores
        FROM companies c
        JOIN dna_scores ds ON ds.entity_id = c.id AND ds.entity_type = 'company'
        """,
    )
    rows = await cursor.fetchall()
    return [
        {
            "id": r["id"],
            "name": r["name"],
            "scores": DimensionScores.model_validate_json(r["scores"]),
        }
        for r in rows
    ]


@router.post("/run")
async def run_matching_endpoint(
    db: aiosqlite.Connection = Depends(get_db),
):
    """Manually trigger matching for all eligible candidate-company pairs."""
    candidates = await _fetch_candidates(db)
    companies = await _fetch_companies(db)

    if not candidates or not companies:
        return {"matches_created": 0, "message": "Not enough data to match"}

    now = datetime.now(tz=timezone.utc)
    week_label = now.strftime("%Y-W%W")
    count = 0

    for cand in candidates:
        for comp in companies:
            # Skip if match already exists for this pair this week
            cursor = await db.execute(
                """
                SELECT id FROM matches
                WHERE candidate_id = ? AND company_id = ? AND drop_week = ?
                """,
                (cand["id"], comp["id"], week_label),
            )
            if await cursor.fetchone():
                continue

            result = run_matching(
                candidate_id=cand["id"],
                candidate_scores=cand["scores"],
                candidate_consistency=cand["consistency"],
                company_id=comp["id"],
                company_scores=comp["scores"],
            )

            if not result.passed_l1:
                continue

            # Generate report
            dim_scores_dict = result.dimension_scores.model_dump()
            report = generate_simple_report(
                candidate_name=cand["name"],
                company_name=comp["name"],
                match_score=result.score,
                dimension_scores=dim_scores_dict,
                candidate_dna=cand["scores"],
                company_dna=comp["scores"],
                consistency=cand["consistency"],
            )

            match_id = str(uuid.uuid4())
            await db.execute(
                """
                INSERT INTO matches
                    (id, candidate_id, company_id, score, dimension_scores,
                     report, status, drop_week, created_at)
                VALUES (?, ?, ?, ?, ?, ?, 'pending', ?, ?)
                """,
                (
                    match_id,
                    cand["id"],
                    comp["id"],
                    result.score,
                    json.dumps(dim_scores_dict),
                    report,
                    week_label,
                    now.isoformat(),
                ),
            )
            count += 1

    await db.commit()
    return {"matches_created": count}


@router.get("/results/{match_id}", response_model=MatchResponse)
async def get_match(
    match_id: str,
    db: aiosqlite.Connection = Depends(get_db),
):
    """Retrieve a single match with its compatibility report."""
    cursor = await db.execute(
        """
        SELECT m.id, m.candidate_id, m.company_id, m.score,
               m.dimension_scores, m.report, m.status, c.name as company_name
        FROM matches m
        JOIN companies c ON c.id = m.company_id
        WHERE m.id = ?
        """,
        (match_id,),
    )
    row = await cursor.fetchone()

    if not row:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Match not found",
        )

    return MatchResponse(
        id=row["id"],
        candidate_id=row["candidate_id"],
        company_id=row["company_id"],
        company_name=row["company_name"],
        score=row["score"],
        dimension_scores=DimensionScores.model_validate(
            json.loads(row["dimension_scores"]),
        ),
        report=row["report"],
        status=MatchStatus(row["status"]),
    )


@router.post("/results/{match_id}/action", response_model=MatchResponse)
async def match_action(
    match_id: str,
    body: MatchActionRequest,
    user_id: str = Depends(get_current_user_id),
    db: aiosqlite.Connection = Depends(get_db),
):
    """Accept or pass on a match."""
    # Verify match exists and belongs to the user
    cursor = await db.execute(
        """
        SELECT m.id, m.candidate_id, m.status
        FROM matches m
        WHERE m.id = ?
        """,
        (match_id,),
    )
    row = await cursor.fetchone()

    if not row:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Match not found",
        )
    if row["candidate_id"] != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="This match does not belong to you",
        )
    if row["status"] != "pending":
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Match already {row['status']}",
        )

    new_status = "accepted" if body.action == "accept" else "passed"
    await db.execute(
        "UPDATE matches SET status = ? WHERE id = ?",
        (new_status, match_id),
    )
    await db.commit()

    # Return updated match
    return await get_match(match_id, db)
