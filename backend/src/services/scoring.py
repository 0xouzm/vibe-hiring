"""Career DNA scoring engine — compute 8-dimension scores from answers."""

import statistics
from collections import defaultdict

from src.models.questionnaire import (
    Answer,
    BudgetAnswer,
    ChoiceAnswer,
    RankingAnswer,
)
from src.models.dna_score import DIMENSIONS, DimensionScores
from src.data.scoring_maps import (
    CAREER_BUDGET_DIMENSIONS,
    CAREER_BUDGET_DIRECTION,
    CAREER_RANKING_DIRECTION,
    CAREER_RANKING_SCORING,
    CAREER_SCORING,
)


def _score_choice(
    answer: ChoiceAnswer,
    accum: dict[str, list[float]],
) -> None:
    """Look up dimension scores for the chosen option and accumulate."""
    mapping = CAREER_SCORING.get(answer.question_id)
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
    option_dims = CAREER_RANKING_SCORING.get(qid)
    directions = CAREER_RANKING_DIRECTION.get(qid)
    if not option_dims or not directions:
        return

    n = len(answer.ranking)
    for rank_idx, key in enumerate(answer.ranking):
        dim = option_dims.get(key)
        direction = directions.get(key, "")
        if dim is None:
            continue

        # Borda: rank 0 (top) → n points, rank n-1 (bottom) → 1 point
        borda = n - rank_idx
        score = (borda / n) * 100

        # Invert if the direction label implies the "low" end of the spectrum
        if direction in ("specialist", "financial", "balance"):
            score = 100 - score

        accum[dim].append(score)


def _score_budget(
    answer: BudgetAnswer,
    accum: dict[str, list[float]],
) -> None:
    """Map budget allocation percentages directly to dimension scores."""
    qid = answer.question_id
    dim_map = CAREER_BUDGET_DIMENSIONS.get(qid)
    dir_map = CAREER_BUDGET_DIRECTION.get(qid)
    if not dim_map or not dir_map:
        return

    for key, pct in answer.allocations.items():
        dim = dim_map.get(key)
        direction = dir_map.get(key, "")
        if dim is None:
            continue

        score = float(pct)

        # Invert for "low_*" directions — higher allocation means lower score
        if direction.startswith("low_"):
            score = 100 - score
        # "mid_*" directions stay as-is (centre of spectrum)

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


def _compute_consistency(accum: dict[str, list[float]]) -> float:
    """Consistency = 1 - mean(std_per_dimension / 50).

    When a dimension has only one data point, its std is 0.
    Result is clamped to [0, 1].
    """
    stds: list[float] = []
    for dim in DIMENSIONS:
        values = accum.get(dim, [])
        if len(values) >= 2:
            stds.append(statistics.stdev(values))
        else:
            stds.append(0.0)

    if not stds:
        return 1.0

    mean_std = statistics.mean(stds)
    consistency = 1.0 - (mean_std / 50.0)
    return round(max(0.0, min(1.0, consistency)), 4)


def calculate_career_dna(
    answers: list[Answer],
) -> tuple[DimensionScores, float]:
    """Compute Career DNA scores and consistency from questionnaire answers.

    Returns:
        (DimensionScores, consistency) where consistency is in [0, 1].
    """
    accum: dict[str, list[float]] = defaultdict(list)

    for ans in answers:
        if isinstance(ans, ChoiceAnswer):
            _score_choice(ans, accum)
        elif isinstance(ans, RankingAnswer):
            _score_ranking(ans, accum)
        elif isinstance(ans, BudgetAnswer):
            _score_budget(ans, accum)

    scores = _build_dimension_scores(accum)
    consistency = _compute_consistency(accum)
    return scores, consistency
