"""Matching routes — run matching, query matches, accept/pass."""

import json
import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status

import aiosqlite

from src.core.deps import get_db, get_current_user_id
from src.models.dna_score import DimensionScores
from src.models.match import (
    CompanyMatchResponse,
    MatchActionRequest,
    MatchResponse,
    MatchStatus,
)
from src.services.drop import compute_match_status
from src.services.matching import run_matching
from src.services.report import generate_simple_report

router = APIRouter()


async def _fetch_candidates(db: aiosqlite.Connection) -> list[dict]:
    """Fetch all candidates with DNA scores and profile info."""
    cursor = await db.execute(
        """
        SELECT u.id, u.name, ds.scores, ds.consistency,
               p.skills, p.location, p.remote_preference
        FROM users u
        JOIN dna_scores ds ON ds.entity_id = u.id AND ds.entity_type = 'candidate'
        LEFT JOIN user_profiles p ON p.user_id = u.id
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
            "skills": json.loads(r["skills"]) if r["skills"] else None,
            "location": r["location"],
        }
        for r in rows
    ]


async def _fetch_roles(db: aiosqlite.Connection) -> list[dict]:
    """Fetch all active roles with their company DNA scores."""
    cursor = await db.execute(
        """
        SELECT r.id as role_id, r.company_id, r.title, r.skills,
               r.location, r.remote_policy,
               c.name as company_name, ds.scores
        FROM roles r
        JOIN companies c ON c.id = r.company_id
        JOIN dna_scores ds ON ds.entity_id = r.company_id
                          AND ds.entity_type = 'company'
        WHERE r.is_active = 1
        """,
    )
    rows = await cursor.fetchall()
    return [
        {
            "role_id": r["role_id"],
            "company_id": r["company_id"],
            "company_name": r["company_name"],
            "title": r["title"],
            "skills": json.loads(r["skills"]) if r["skills"] else None,
            "location": r["location"],
            "remote_policy": r["remote_policy"],
            "scores": DimensionScores.model_validate_json(r["scores"]),
        }
        for r in rows
    ]


@router.post("/run")
async def run_matching_endpoint(
    db: aiosqlite.Connection = Depends(get_db),
):
    """Manually trigger matching for all eligible candidate-role pairs."""
    candidates = await _fetch_candidates(db)
    roles = await _fetch_roles(db)

    if not candidates or not roles:
        return {"matches_created": 0, "message": "Not enough data to match"}

    now = datetime.now(tz=timezone.utc)
    week_label = now.strftime("%Y-W%W")
    count = 0

    for cand in candidates:
        for role in roles:
            # Skip if match already exists this week
            cursor = await db.execute(
                "SELECT id FROM matches "
                "WHERE candidate_id = ? AND role_id = ? AND drop_week = ?",
                (cand["id"], role["role_id"], week_label),
            )
            if await cursor.fetchone():
                continue

            result = run_matching(
                candidate_id=cand["id"],
                candidate_scores=cand["scores"],
                candidate_consistency=cand["consistency"],
                company_id=role["company_id"],
                company_scores=role["scores"],
                role_id=role["role_id"],
                candidate_skills=cand.get("skills"),
                role_skills=role.get("skills"),
                candidate_location=cand.get("location"),
                role_location=role.get("location"),
                role_remote_policy=role.get("remote_policy"),
                l1_total=len(candidates),
            )

            if not result.passed_l1:
                continue

            dim_dict = result.dimension_scores.model_dump()
            report = generate_simple_report(
                candidate_name=cand["name"],
                company_name=role["company_name"],
                match_score=result.score,
                dimension_scores=dim_dict,
                candidate_dna=cand["scores"],
                company_dna=role["scores"],
                consistency=cand["consistency"],
            )

            match_id = str(uuid.uuid4())
            await db.execute(
                """
                INSERT INTO matches
                    (id, candidate_id, company_id, role_id, score,
                     dimension_scores, report, status, drop_week, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, 'pending', ?, ?)
                """,
                (
                    match_id, cand["id"], role["company_id"],
                    role["role_id"], result.score,
                    json.dumps(dim_dict), report,
                    week_label, now.isoformat(),
                ),
            )
            count += 1

    await db.commit()
    return {"matches_created": count}


async def _build_match_response(
    db: aiosqlite.Connection, row: aiosqlite.Row,
) -> MatchResponse:
    """Build a MatchResponse with company name and role title."""
    # Get company name
    cursor = await db.execute(
        "SELECT name FROM companies WHERE id = ?", (row["company_id"],)
    )
    comp = await cursor.fetchone()

    # Get role title
    role_title = None
    if row["role_id"]:
        cursor = await db.execute(
            "SELECT title FROM roles WHERE id = ?", (row["role_id"],)
        )
        role_row = await cursor.fetchone()
        role_title = role_row["title"] if role_row else None

    return MatchResponse(
        id=row["id"],
        candidate_id=row["candidate_id"],
        company_id=row["company_id"],
        company_name=comp["name"] if comp else "Unknown",
        role_id=row["role_id"],
        role_title=role_title,
        score=row["score"],
        dimension_scores=DimensionScores.model_validate(
            json.loads(row["dimension_scores"]),
        ),
        report=row["report"],
        status=MatchStatus(row["status"]),
        candidate_action=row["candidate_action"],
        company_action=row["company_action"],
    )


@router.get("/results/{match_id}", response_model=MatchResponse)
async def get_match(
    match_id: str,
    db: aiosqlite.Connection = Depends(get_db),
):
    """Retrieve a single match with its compatibility report."""
    cursor = await db.execute(
        "SELECT * FROM matches WHERE id = ?", (match_id,)
    )
    row = await cursor.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Match not found")
    return await _build_match_response(db, row)


@router.post("/results/{match_id}/candidate-action", response_model=MatchResponse)
async def candidate_action(
    match_id: str,
    body: MatchActionRequest,
    user_id: str = Depends(get_current_user_id),
    db: aiosqlite.Connection = Depends(get_db),
):
    """Candidate accepts or passes on a match."""
    cursor = await db.execute(
        "SELECT * FROM matches WHERE id = ?", (match_id,)
    )
    row = await cursor.fetchone()

    if not row:
        raise HTTPException(status_code=404, detail="Match not found")
    if row["candidate_id"] != user_id:
        raise HTTPException(status_code=403, detail="Not your match")
    if row["candidate_action"]:
        raise HTTPException(status_code=409, detail="Already acted on this match")

    action_value = "accept" if body.action == "accept" else "pass"
    new_status = compute_match_status(action_value, row["company_action"])

    await db.execute(
        "UPDATE matches SET candidate_action = ?, status = ? WHERE id = ?",
        (action_value, new_status, match_id),
    )
    await db.commit()
    return await get_match(match_id, db)


@router.post("/results/{match_id}/company-action", response_model=MatchResponse)
async def company_action(
    match_id: str,
    body: MatchActionRequest,
    user_id: str = Depends(get_current_user_id),
    db: aiosqlite.Connection = Depends(get_db),
):
    """Company accepts or passes on a candidate match."""
    # Verify user is HR and match belongs to their company
    cursor = await db.execute(
        "SELECT company_id FROM users WHERE id = ? AND role = 'hr'",
        (user_id,),
    )
    user_row = await cursor.fetchone()
    if not user_row:
        raise HTTPException(status_code=403, detail="Only HR can take company actions")

    cursor = await db.execute(
        "SELECT * FROM matches WHERE id = ?", (match_id,)
    )
    row = await cursor.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Match not found")
    if row["company_id"] != user_row["company_id"]:
        raise HTTPException(status_code=403, detail="Not your company's match")
    if row["company_action"]:
        raise HTTPException(status_code=409, detail="Already acted on this match")

    action_value = "accept" if body.action == "accept" else "pass"
    new_status = compute_match_status(row["candidate_action"], action_value)

    await db.execute(
        "UPDATE matches SET company_action = ?, status = ? WHERE id = ?",
        (action_value, new_status, match_id),
    )
    await db.commit()
    return await get_match(match_id, db)


# Legacy endpoint for backward compatibility
@router.post("/results/{match_id}/action", response_model=MatchResponse)
async def match_action(
    match_id: str,
    body: MatchActionRequest,
    user_id: str = Depends(get_current_user_id),
    db: aiosqlite.Connection = Depends(get_db),
):
    """Accept or pass on a match (legacy — delegates to candidate-action)."""
    return await candidate_action(match_id, body, user_id, db)
