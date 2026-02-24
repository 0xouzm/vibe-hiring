"""Culture Authenticity Score (CAS) — measures how honestly a company
represents its culture by comparing HR vs employee responses."""

import statistics
from dataclasses import dataclass

from src.models.dna_score import DIMENSIONS, DimensionScores


@dataclass(frozen=True)
class CASResult:
    """Output of the CAS computation."""

    score: float
    tier: str  # "gold" | "silver" | "bronze" | "none"
    internal_consistency: float
    hr_employee_alignment: float


def _tier_from_score(score: float) -> str:
    """Map a CAS score (0-100) to a tier label."""
    if score >= 85:
        return "gold"
    if score >= 65:
        return "silver"
    if score >= 40:
        return "bronze"
    return "none"


def _internal_consistency(all_scores: list[DimensionScores]) -> float:
    """Measure how consistently all respondents agree, across dimensions.

    Formula: 1 - mean(std_d / 100) for each dimension *d*.
    """
    if len(all_scores) < 2:
        return 1.0

    stds: list[float] = []
    for dim in DIMENSIONS:
        values = [getattr(s, dim) for s in all_scores]
        stds.append(statistics.stdev(values))

    return 1.0 - (statistics.mean(stds) / 100.0)


def _hr_employee_alignment(
    hr_scores: list[DimensionScores],
    employee_scores: list[DimensionScores],
) -> float:
    """Measure how closely HR's view matches employees' view.

    Formula: 1 - mean(|mean_hr_d - mean_emp_d| / 100) for each dimension *d*.
    """
    if not hr_scores or not employee_scores:
        return 1.0

    gaps: list[float] = []
    for dim in DIMENSIONS:
        hr_mean = statistics.mean(getattr(s, dim) for s in hr_scores)
        emp_mean = statistics.mean(getattr(s, dim) for s in employee_scores)
        gaps.append(abs(hr_mean - emp_mean))

    return 1.0 - (statistics.mean(gaps) / 100.0)


def calculate_cas(
    hr_scores: list[DimensionScores],
    employee_scores: list[DimensionScores],
) -> CASResult:
    """Compute the Culture Authenticity Score for a company.

    Demo-grade formula:
        CAS = 0.55 * InternalConsistency + 0.45 * HREmployeeAlignment

    Both sub-scores are in [0, 1]; the final CAS is scaled to 0-100.

    Args:
        hr_scores: DimensionScores from each HR respondent.
        employee_scores: DimensionScores from each employee respondent.

    Returns:
        CASResult with score (0-100), tier, and sub-score breakdown.
    """
    all_scores = hr_scores + employee_scores

    ic = _internal_consistency(all_scores)
    alignment = _hr_employee_alignment(hr_scores, employee_scores)

    raw = 0.55 * ic + 0.45 * alignment
    score = round(raw * 100, 2)
    score = max(0.0, min(100.0, score))

    return CASResult(
        score=score,
        tier=_tier_from_score(score),
        internal_consistency=round(ic, 4),
        hr_employee_alignment=round(alignment, 4),
    )
