"""Matching and weekly-drop related Pydantic models."""

from enum import Enum
from typing import Literal

from pydantic import BaseModel

from .dna_score import DimensionScores


class MatchStatus(str, Enum):
    """Lifecycle status of a single match (dual-action model)."""

    pending = "pending"
    candidate_accepted = "candidate_accepted"
    company_accepted = "company_accepted"
    mutual = "mutual"
    passed = "passed"
    # Legacy compatibility
    accepted = "accepted"


class MatchResponse(BaseModel):
    """Public representation of a candidate <-> role match."""

    id: str
    candidate_id: str
    company_id: str
    company_name: str
    role_id: str | None = None
    role_title: str | None = None
    score: float
    dimension_scores: DimensionScores
    report: str | None = None
    status: MatchStatus
    candidate_action: str | None = None
    company_action: str | None = None


class MatchActionRequest(BaseModel):
    """Request body when either side acts on a match."""

    action: Literal["accept", "pass"]


class CompanyMatchResponse(BaseModel):
    """Match seen from the company side — includes candidate info."""

    id: str
    candidate_id: str
    candidate_name: str
    company_id: str
    role_id: str | None = None
    role_title: str | None = None
    score: float
    dimension_scores: DimensionScores
    report: str | None = None
    status: MatchStatus
    candidate_action: str | None = None
    company_action: str | None = None


class DropResponse(BaseModel):
    """A weekly drop containing one or more matches."""

    id: str
    week: str
    matches: list[MatchResponse]
    revealed_at: str | None = None


class CompanyDropResponse(BaseModel):
    """A weekly drop for a company — grouped by role."""

    id: str
    week: str
    matches: list[CompanyMatchResponse]
    revealed_at: str | None = None
