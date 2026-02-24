"""Company DNA aggregation — trimmed weighted-median across multiple respondents."""

from src.models.dna_score import DIMENSIONS, DimensionScores

# Role-based weights: HR voices are down-weighted to reduce institutional bias
_ROLE_WEIGHTS: dict[str, float] = {
    "hr": 0.5,
    "employee": 1.0,
}


def _weighted_median(values: list[float], weights: list[float]) -> float:
    """Compute the weighted median of *values* with corresponding *weights*.

    Algorithm:
        1. Sort (value, weight) pairs by value.
        2. Walk through cumulative weight until it reaches half the total.
        3. The value at that threshold is the weighted median.
    """
    if not values:
        return 50.0

    pairs = sorted(zip(values, weights), key=lambda p: p[0])
    total_weight = sum(weights)
    if total_weight == 0:
        return 50.0

    half = total_weight / 2.0
    cumulative = 0.0
    for val, w in pairs:
        cumulative += w
        if cumulative >= half:
            return val

    # Fallback (shouldn't reach here)
    return pairs[-1][0]


def _trim_extremes(
    values: list[float],
    weights: list[float],
) -> tuple[list[float], list[float]]:
    """Remove highest and lowest value when N >= 7 to reduce outlier impact.

    Returns:
        Trimmed (values, weights) lists.
    """
    if len(values) < 7:
        return values, weights

    pairs = sorted(zip(values, weights), key=lambda p: p[0])
    trimmed = pairs[1:-1]
    return [v for v, _ in trimmed], [w for _, w in trimmed]


def aggregate_company_scores(
    scores_with_roles: list[tuple[DimensionScores, str]],
) -> DimensionScores:
    """Aggregate multiple respondents into a single Company DNA profile.

    Algorithm (per dimension):
        1. Assign weights by role (HR = 0.5, employee = 1.0).
        2. If N >= 7, trim the highest and lowest score.
        3. Compute weighted median of remaining values.

    Args:
        scores_with_roles: List of (DimensionScores, role) tuples where
            role is ``"hr"`` or ``"employee"``.

    Returns:
        Aggregated DimensionScores.
    """
    if not scores_with_roles:
        return DimensionScores(
            **{dim: 50.0 for dim in DIMENSIONS},
        )

    result: dict[str, float] = {}

    for dim in DIMENSIONS:
        values: list[float] = []
        weights: list[float] = []

        for scores, role in scores_with_roles:
            val = getattr(scores, dim)
            values.append(val)
            weights.append(_ROLE_WEIGHTS.get(role, 1.0))

        trimmed_vals, trimmed_wts = _trim_extremes(values, weights)
        result[dim] = round(_weighted_median(trimmed_vals, trimmed_wts), 2)

    return DimensionScores(**result)
