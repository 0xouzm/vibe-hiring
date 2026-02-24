"""Answer submission routes — Career DNA and Company DNA."""

import json
import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import TypeAdapter

import aiosqlite

from src.core.deps import get_db, get_current_user_id
from src.models.questionnaire import Answer, SubmitAnswersRequest
from src.models.dna_score import DNAScoreResponse, DimensionScores
from src.services.scoring import calculate_career_dna
from src.services.company_scoring import calculate_company_dna
from src.services.aggregation import aggregate_company_scores
from src.services.cas import calculate_cas

_answer_list_adapter = TypeAdapter(list[Answer])

router = APIRouter()


def _scores_to_json(scores: DimensionScores) -> str:
    """Serialize DimensionScores to a JSON string for DB storage."""
    return scores.model_dump_json()


async def _save_dna_score(
    db: aiosqlite.Connection,
    entity_type: str,
    entity_id: str,
    scores: DimensionScores,
    consistency: float,
) -> None:
    """Upsert a DNA score record — replace if the entity already has one."""
    now = datetime.now(tz=timezone.utc).isoformat()

    # Delete existing score for this entity to keep only the latest
    await db.execute(
        "DELETE FROM dna_scores WHERE entity_type = ? AND entity_id = ?",
        (entity_type, entity_id),
    )
    await db.execute(
        """
        INSERT INTO dna_scores (id, entity_type, entity_id, scores, consistency, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (str(uuid.uuid4()), entity_type, entity_id, _scores_to_json(scores), consistency, now),
    )


async def _update_company_aggregate(
    db: aiosqlite.Connection,
    company_id: str,
) -> None:
    """Re-aggregate company DNA from all respondents and update CAS."""
    # Fetch all individual company_answers for this company
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
        return

    # Re-score each respondent and collect for aggregation
    hr_scores: list[DimensionScores] = []
    employee_scores: list[DimensionScores] = []
    scores_with_roles: list[tuple[DimensionScores, str]] = []

    for row in rows:
        raw_answers = json.loads(row["answers"])
        answers = _answer_list_adapter.validate_python(raw_answers)
        individual_scores = calculate_company_dna(answers)

        role = row["role"]
        scores_with_roles.append((individual_scores, role))
        if role == "hr":
            hr_scores.append(individual_scores)
        else:
            employee_scores.append(individual_scores)

    # Aggregate
    aggregated = aggregate_company_scores(scores_with_roles)

    # CAS
    cas_result = calculate_cas(hr_scores, employee_scores)

    # Save aggregated company score (consistency = CAS / 100)
    await _save_dna_score(db, "company", company_id, aggregated, cas_result.score / 100.0)
    await db.commit()


@router.post("/career-dna", response_model=DNAScoreResponse)
async def submit_career_dna(
    body: SubmitAnswersRequest,
    user_id: str = Depends(get_current_user_id),
    db: aiosqlite.Connection = Depends(get_db),
):
    """Submit Career DNA answers and receive computed scores."""
    # Calculate scores
    scores, consistency = calculate_career_dna(body.answers)

    now = datetime.now(tz=timezone.utc).isoformat()

    # Save raw answers
    answers_json = json.dumps([a.model_dump() for a in body.answers])
    await db.execute(
        """
        INSERT INTO career_answers (id, user_id, answers, created_at)
        VALUES (?, ?, ?, ?)
        """,
        (str(uuid.uuid4()), user_id, answers_json, now),
    )

    # Save DNA score
    await _save_dna_score(db, "candidate", user_id, scores, consistency)
    await db.commit()

    return DNAScoreResponse(
        entity_type="candidate",
        entity_id=user_id,
        scores=scores,
        consistency=consistency,
    )


@router.post("/company-dna", response_model=DNAScoreResponse)
async def submit_company_dna(
    body: SubmitAnswersRequest,
    user_id: str = Depends(get_current_user_id),
    db: aiosqlite.Connection = Depends(get_db),
):
    """Submit Company DNA answers and receive computed scores."""
    # Verify user is HR and has a company
    cursor = await db.execute(
        "SELECT role, company_id FROM users WHERE id = ?", (user_id,)
    )
    user_row = await cursor.fetchone()

    if not user_row or user_row["role"] != "hr":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only HR users can submit Company DNA answers",
        )

    company_id = user_row["company_id"]
    if not company_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User is not associated with a company",
        )

    # Calculate individual scores
    individual_scores = calculate_company_dna(body.answers)

    now = datetime.now(tz=timezone.utc).isoformat()

    # Save raw answers
    answers_json = json.dumps([a.model_dump() for a in body.answers])
    await db.execute(
        """
        INSERT INTO company_answers (id, user_id, company_id, answers, created_at)
        VALUES (?, ?, ?, ?, ?)
        """,
        (str(uuid.uuid4()), user_id, company_id, answers_json, now),
    )
    await db.commit()

    # Re-aggregate company scores (handles CAS too)
    await _update_company_aggregate(db, company_id)

    # Fetch updated company score for response
    cursor = await db.execute(
        "SELECT scores, consistency FROM dna_scores WHERE entity_type = 'company' AND entity_id = ?",
        (company_id,),
    )
    score_row = await cursor.fetchone()

    if score_row:
        aggregated = DimensionScores.model_validate_json(score_row["scores"])
        return DNAScoreResponse(
            entity_type="company",
            entity_id=company_id,
            scores=aggregated,
            consistency=score_row["consistency"],
        )

    # Fallback: return individual scores
    return DNAScoreResponse(
        entity_type="company",
        entity_id=company_id,
        scores=individual_scores,
        consistency=1.0,
    )
