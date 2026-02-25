"""L1-L2 matching engine — DNA compatibility scoring between candidate and role."""

from dataclasses import dataclass

from src.models.dna_score import DIMENSIONS, DimensionScores


@dataclass(frozen=True)
class MatchResult:
    """Output of the two-layer matching engine."""

    candidate_id: str
    company_id: str
    role_id: str | None = None
    score: int = 0       # 0-100 overall match percentage
    dimension_scores: DimensionScores | None = None
    passed_l1: bool = True
    l1_total: int = 0    # total candidates before L1 filter
    l1_passed: int = 0   # candidates after L1 filter


def _l1_boolean_filter(
    candidate_skills: list[str] | None,
    role_skills: list[str] | None,
    candidate_location: str | None,
    role_location: str | None,
    role_remote_policy: str | None,
) -> bool:
    """L1: hard-constraint boolean filter.

    Checks skill overlap and location/remote compatibility.
    Returns True if candidate passes all filters.
    """
    # Remote-first roles pass everyone
    if role_remote_policy == "remote":
        return True

    # If both have location info, check compatibility
    if candidate_location and role_location and role_remote_policy == "onsite":
        # Simple city match for demo
        if candidate_location != role_location:
            return False

    # Skill check: at least 1 required skill must match (if both defined)
    if candidate_skills and role_skills:
        overlap = set(s.lower() for s in candidate_skills) & set(
            s.lower() for s in role_skills
        )
        if not overlap:
            return False

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
    role_id: str | None = None,
    candidate_skills: list[str] | None = None,
    role_skills: list[str] | None = None,
    candidate_location: str | None = None,
    role_location: str | None = None,
    role_remote_policy: str | None = None,
    l1_total: int = 0,
) -> MatchResult:
    """Execute the full L1 + L2 matching pipeline."""
    passed = _l1_boolean_filter(
        candidate_skills, role_skills,
        candidate_location, role_location, role_remote_policy,
    )

    if not passed:
        zero_dims = DimensionScores(**{d: 0.0 for d in DIMENSIONS})
        return MatchResult(
            candidate_id=candidate_id,
            company_id=company_id,
            role_id=role_id,
            score=0,
            dimension_scores=zero_dims,
            passed_l1=False,
            l1_total=l1_total,
            l1_passed=0,
        )

    overall, dim_scores = _l2_dna_compatibility(
        candidate_scores, company_scores, candidate_consistency,
    )

    return MatchResult(
        candidate_id=candidate_id,
        company_id=company_id,
        role_id=role_id,
        score=overall,
        dimension_scores=dim_scores,
        passed_l1=True,
        l1_total=l1_total,
        l1_passed=l1_total,  # demo: all pass L1
    )
