"""Company DNA scoring engine — compute 8-dimension scores for one respondent."""

import statistics
from collections import defaultdict

from src.models.questionnaire import (
    Answer,
    BudgetAnswer,
    ChoiceAnswer,
    RankingAnswer,
)
from src.models.dna_score import DIMENSIONS, DimensionScores
from src.data.company_scoring_maps import (
    COMPANY_BUDGET_DIMENSIONS,
    COMPANY_BUDGET_DIRECTION,
    COMPANY_RANKING_DIRECTION,
    COMPANY_RANKING_SCORING,
    COMPANY_SCORING,
)


def _score_choice(
    answer: ChoiceAnswer,
    accum: dict[str, list[float]],
) -> None:
    """Look up dimension scores for the chosen option and accumulate."""
    mapping = COMPANY_SCORING.get(answer.question_id)
    if not mapping:
        return
    scores = mapping.get(answer.selected_key, {})
    for dim, value in scores.items():
        accum[dim].append(value)


def _score_ranking(
    answer: RankingAnswer,
    accum: dict[str, list[float]],
) -> None:
    """Borda count: rank-1 gets N points ... last gets 1 point, normalised."""
    qid = answer.question_id
    option_dims = COMPANY_RANKING_SCORING.get(qid)
    directions = COMPANY_RANKING_DIRECTION.get(qid)
    if not option_dims or not directions:
        return

    n = len(answer.ranking)
    for rank_idx, key in enumerate(answer.ranking):
        dim = option_dims.get(key)
        direction = directions.get(key, "")
        if dim is None:
            continue

        borda = n - rank_idx
        score = (borda / n) * 100

        # Invert for "low_*" or specialist/financial/balance directions
        if direction in ("specialist", "financial", "balance") or direction.startswith(
            "low_"
        ):
            score = 100 - score

        accum[dim].append(score)


def _score_budget(
    answer: BudgetAnswer,
    accum: dict[str, list[float]],
) -> None:
    """Map budget allocation percentages directly to dimension scores."""
    qid = answer.question_id
    dim_map = COMPANY_BUDGET_DIMENSIONS.get(qid)
    dir_map = COMPANY_BUDGET_DIRECTION.get(qid)
    if not dim_map or not dir_map:
        return

    for key, pct in answer.allocations.items():
        dim = dim_map.get(key)
        direction = dir_map.get(key, "")
        if dim is None:
            continue

        score = float(pct)
        if direction.startswith("low_"):
            score = 100 - score

        accum[dim].append(score)


def _build_dimension_scores(
    accum: dict[str, list[float]],
) -> DimensionScores:
    """Average accumulated per-dimension values into final scores."""
    averaged: dict[str, float] = {}
    for dim in DIMENSIONS:
        values = accum.get(dim, [])
        averaged[dim] = round(statistics.mean(values), 2) if values else 50.0
    return DimensionScores(**averaged)


def calculate_company_dna(answers: list[Answer]) -> DimensionScores:
    """Compute Company DNA scores for a single HR or employee respondent.

    Returns:
        DimensionScores with per-dimension values on a 0-100 scale.
    """
    accum: dict[str, list[float]] = defaultdict(list)

    for ans in answers:
        if isinstance(ans, ChoiceAnswer):
            _score_choice(ans, accum)
        elif isinstance(ans, RankingAnswer):
            _score_ranking(ans, accum)
        elif isinstance(ans, BudgetAnswer):
            _score_budget(ans, accum)

    return _build_dimension_scores(accum)
