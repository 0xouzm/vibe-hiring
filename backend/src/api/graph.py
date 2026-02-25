"""Knowledge graph and matching pipeline visualization routes."""

import json

from fastapi import APIRouter, Depends, HTTPException

import aiosqlite

from src.core.deps import get_db
from src.models.dna_score import DimensionScores
from src.services.graph_service import build_candidate_graph, build_match_graph

router = APIRouter()


@router.get("/candidate/{candidate_id}")
async def get_candidate_graph(
    candidate_id: str,
    db: aiosqlite.Connection = Depends(get_db),
):
    """Get knowledge graph data for a candidate."""
    graph = await build_candidate_graph(db, candidate_id)
    if not graph["nodes"]:
        raise HTTPException(status_code=404, detail="Candidate not found")
    return graph


@router.get("/match/{match_id}")
async def get_match_graph(
    match_id: str,
    db: aiosqlite.Connection = Depends(get_db),
):
    """Get merged knowledge graph for a match (candidate + company)."""
    graph = await build_match_graph(db, match_id)
    if not graph["nodes"]:
        raise HTTPException(status_code=404, detail="Match not found")
    return graph


@router.get("/pipeline/{match_id}")
async def get_matching_pipeline(
    match_id: str,
    db: aiosqlite.Connection = Depends(get_db),
):
    """Get matching pipeline visualization data for a specific match.

    Returns L1 filter stats, L2 dimension comparison, and score breakdown.
    """
    cursor = await db.execute(
        """SELECT m.*, c.name as company_name, u.name as candidate_name
           FROM matches m
           JOIN companies c ON c.id = m.company_id
           JOIN users u ON u.id = m.candidate_id
           WHERE m.id = ?""",
        (match_id,),
    )
    match = await cursor.fetchone()
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")

    # Get candidate and company DNA scores
    c_cursor = await db.execute(
        "SELECT scores, consistency FROM dna_scores "
        "WHERE entity_id = ? AND entity_type = 'candidate'",
        (match["candidate_id"],),
    )
    c_dna = await c_cursor.fetchone()

    j_cursor = await db.execute(
        "SELECT scores FROM dna_scores WHERE entity_id = ? AND entity_type = 'company'",
        (match["company_id"],),
    )
    j_dna = await j_cursor.fetchone()

    # Count total candidates for funnel
    total_cursor = await db.execute(
        "SELECT COUNT(*) as cnt FROM users WHERE role = 'candidate'"
    )
    total_row = await total_cursor.fetchone()
    total_candidates = total_row["cnt"]

    # Count candidates that matched this company's role
    matched_cursor = await db.execute(
        "SELECT COUNT(*) as cnt FROM matches WHERE role_id = ?",
        (match["role_id"],),
    )
    matched_row = await matched_cursor.fetchone()
    matched_count = matched_row["cnt"]

    candidate_scores = json.loads(c_dna["scores"]) if c_dna else {}
    company_scores = json.loads(j_dna["scores"]) if j_dna else {}
    dimension_scores = (
        json.loads(match["dimension_scores"]) if match["dimension_scores"] else {}
    )
    consistency = c_dna["consistency"] if c_dna else 0.85

    return {
        "match_id": match_id,
        "candidate_name": match["candidate_name"],
        "company_name": match["company_name"],
        "overall_score": match["score"],
        "funnel": {
            "total_candidates": total_candidates,
            "l1_passed": matched_count,
            "l2_top": 3,  # Top 3 in weekly drop
        },
        "dimensions": {
            "candidate": candidate_scores,
            "company": company_scores,
            "compatibility": dimension_scores,
        },
        "formula": {
            "consistency": consistency,
            "raw_average": round(
                sum(dimension_scores.values()) / max(len(dimension_scores), 1),
                2,
            ),
            "final_score": match["score"],
        },
    }
