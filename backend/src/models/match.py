"""Matching and weekly-drop related Pydantic models."""

from enum import Enum
from typing import Literal

from pydantic import BaseModel

from .dna_score import DimensionScores


class MatchStatus(str, Enum):
    """Lifecycle status of a single match."""

    pending = "pending"
    accepted = "accepted"
    passed = "passed"


class MatchResponse(BaseModel):
    """Public representation of a candidate ↔ company match."""

    id: str
    candidate_id: str
    company_id: str
    company_name: str
    score: float
    dimension_scores: DimensionScores
    report: str | None = None
    status: MatchStatus


class MatchActionRequest(BaseModel):
    """Request body when a candidate acts on a match."""

    action: Literal["accept", "pass"]


class CompanyMatchResponse(BaseModel):
    """Match seen from the company side — includes anonymized candidate info."""

    id: str
    candidate_id: str
    candidate_name: str
    company_id: str
    score: float
    dimension_scores: DimensionScores
    report: str | None = None
    status: MatchStatus


class DropResponse(BaseModel):
    """A weekly drop containing one or more matches for a candidate."""

    id: str
    week: str
    matches: list[MatchResponse]
    revealed_at: str | None = None
