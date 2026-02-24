"""DNA scoring models — the 8-dimension Career / Company DNA profile."""

from pydantic import BaseModel


DIMENSIONS: list[str] = [
    "pace",
    "collab",
    "decision",
    "expression",
    "unc",
    "growth",
    "motiv",
    "execution",
]
"""Canonical order of the eight Career DNA / Company DNA dimensions."""


class DimensionScores(BaseModel):
    """Scores for each of the eight DNA dimensions (0–100 scale)."""

    pace: float
    collab: float
    decision: float
    expression: float
    unc: float
    growth: float
    motiv: float
    execution: float


class DNAScoreResponse(BaseModel):
    """API response carrying a computed DNA profile."""

    entity_type: str  # "candidate" | "company"
    entity_id: str
    scores: DimensionScores
    consistency: float
