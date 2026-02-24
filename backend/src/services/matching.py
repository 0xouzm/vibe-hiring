"""L1-L2 matching engine — DNA compatibility scoring between candidate and company."""

from dataclasses import dataclass

from src.models.dna_score import DIMENSIONS, DimensionScores


@dataclass(frozen=True)
class MatchResult:
    """Output of the two-layer matching engine."""

    candidate_id: str
    company_id: str
    score: int  # 0-100 overall match percentage
    dimension_scores: DimensionScores  # per-dimension compatibility (0-100)
    passed_l1: bool


def _l1_boolean_filter(
    candidate_id: str,  # noqa: ARG001 — reserved for future filters
    company_id: str,  # noqa: ARG001
) -> bool:
    """L1: hard-constraint boolean filter.

    Demo phase: all candidates pass (no location / visa / salary filters yet).
    """
    return True


def _l2_dna_compatibility(
    candidate: DimensionScores,
    company: DimensionScores,
    consistency: float,
) -> tuple[int, DimensionScores]:
    """L2: weighted DNA vector distance.

    Per-dimension compatibility:
        score_d = 1 - |C_d - J_d| / 100

    Overall score (demo: equal weights):
        weighted_avg = mean(score_d for all d) * consistency

    Args:
        candidate: Candidate Career DNA profile.
        company: Company DNA profile.
        consistency: Candidate questionnaire consistency in [0, 1].

    Returns:
        (overall_score_int, per_dimension_scores)
    """
    dim_scores: dict[str, float] = {}
    total = 0.0

    for dim in DIMENSIONS:
        c_val = getattr(candidate, dim)
        j_val = getattr(company, dim)
        compat = 1.0 - abs(c_val - j_val) / 100.0
        dim_scores[dim] = round(compat * 100, 2)
        total += compat

    raw_avg = total / len(DIMENSIONS)
    final = raw_avg * consistency
    overall = round(final * 100)
    overall = max(0, min(100, overall))

    return overall, DimensionScores(**dim_scores)


def run_matching(
    candidate_id: str,
    candidate_scores: DimensionScores,
    candidate_consistency: float,
    company_id: str,
    company_scores: DimensionScores,
) -> MatchResult:
    """Execute the full L1 + L2 matching pipeline.

    Args:
        candidate_id: Unique candidate identifier.
        candidate_scores: 8-dimension Career DNA profile.
        candidate_consistency: Answer consistency coefficient in [0, 1].
        company_id: Unique company identifier.
        company_scores: 8-dimension Company DNA profile.

    Returns:
        MatchResult with overall score, per-dimension breakdown, and L1 status.
    """
    passed = _l1_boolean_filter(candidate_id, company_id)

    if not passed:
        zero_dims = DimensionScores(**{d: 0.0 for d in DIMENSIONS})
        return MatchResult(
            candidate_id=candidate_id,
            company_id=company_id,
            score=0,
            dimension_scores=zero_dims,
            passed_l1=False,
        )

    overall, dim_scores = _l2_dna_compatibility(
        candidate_scores,
        company_scores,
        candidate_consistency,
    )

    return MatchResult(
        candidate_id=candidate_id,
        company_id=company_id,
        score=overall,
        dimension_scores=dim_scores,
        passed_l1=True,
    )
