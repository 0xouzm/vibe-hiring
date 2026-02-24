"""Questionnaire-related Pydantic models.

Covers question definitions and the three answer formats
(choice / ranking / budget) used in Career DNA & Company DNA.
"""

from enum import Enum
from typing import Annotated, Literal, Union

from pydantic import BaseModel, Field


# ── Question definitions ─────────────────────────────────────────────


class QuestionType(str, Enum):
    """Supported question formats."""

    choice = "choice"
    ranking = "ranking"
    budget = "budget"


class QuestionOption(BaseModel):
    """A single selectable option within a question."""

    key: str
    text: str


class Question(BaseModel):
    """Full question payload sent to the client."""

    id: str
    title: str
    scenario: str
    type: QuestionType
    options: list[QuestionOption]
    dimensions: list[str]


# ── Answer payloads ──────────────────────────────────────────────────


class ChoiceAnswer(BaseModel):
    """Answer for a single-select choice question."""

    type: Literal["choice"] = "choice"
    question_id: str
    selected_key: str


class RankingAnswer(BaseModel):
    """Answer for a drag-to-rank question.

    ``ranking`` is an ordered list of option keys (most preferred first).
    """

    type: Literal["ranking"] = "ranking"
    question_id: str
    ranking: list[str]


class BudgetAnswer(BaseModel):
    """Answer for a 100-point budget-allocation question.

    ``allocations`` maps option keys to their assigned percentage.
    """

    type: Literal["budget"] = "budget"
    question_id: str
    allocations: dict[str, int]


Answer = Annotated[
    Union[ChoiceAnswer, RankingAnswer, BudgetAnswer],
    Field(discriminator="type"),
]
"""Discriminated union over the three answer formats."""


# ── Request wrapper ──────────────────────────────────────────────────


class SubmitAnswersRequest(BaseModel):
    """Batch submission of questionnaire answers."""

    answers: list[Answer]
