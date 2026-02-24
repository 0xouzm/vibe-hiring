"""Simple template-based match report generator (Phase 1).

Produces a human-readable compatibility report without LLM dependency.
Will be replaced by LightRAG-powered generation in Phase 2.
"""

from src.models.dna_score import DIMENSIONS, DimensionScores

# Human-friendly labels for each dimension
_DIM_LABELS: dict[str, str] = {
    "pace": "Work Pace",
    "collab": "Collaboration Style",
    "decision": "Decision Making",
    "expression": "Communication & Expression",
    "unc": "Uncertainty Tolerance",
    "growth": "Growth Orientation",
    "motiv": "Motivation & Values",
    "execution": "Execution Style",
}

# Spectrum endpoint descriptions (high / low)
_DIM_DESCRIPTIONS: dict[str, tuple[str, str]] = {
    "pace": ("fast-moving, action-oriented", "deliberate, methodical"),
    "collab": ("independent, self-directed", "highly collaborative, team-first"),
    "decision": ("data-driven, analytical", "intuition-driven, experiential"),
    "expression": ("direct, transparent", "reserved, diplomatic"),
    "unc": ("thrives in ambiguity", "prefers structure and clarity"),
    "growth": ("broad generalist explorer", "deep specialist master"),
    "motiv": ("mission and purpose driven", "stability and reward driven"),
    "execution": ("structured and systematic", "flexible and adaptive"),
}


def _sorted_dimensions_by_gap(
    candidate: DimensionScores,
    company: DimensionScores,
) -> list[tuple[str, float, float, float]]:
    """Return dimensions sorted by absolute gap (ascending).

    Each tuple: (dim_name, candidate_val, company_val, gap).
    """
    items: list[tuple[str, float, float, float]] = []
    for dim in DIMENSIONS:
        c_val = getattr(candidate, dim)
        j_val = getattr(company, dim)
        items.append((dim, c_val, j_val, abs(c_val - j_val)))
    return sorted(items, key=lambda x: x[3])


def _describe_alignment(dim: str, c_val: float, j_val: float) -> str:
    """Produce a one-liner about why candidate and company align on *dim*."""
    label = _DIM_LABELS[dim]
    high_desc, low_desc = _DIM_DESCRIPTIONS[dim]

    # Both lean toward the same end of the spectrum
    if c_val >= 55 and j_val >= 55:
        return f"**{label}** — You both value a {high_desc} approach."
    if c_val <= 45 and j_val <= 45:
        return f"**{label}** — You both appreciate a {low_desc} style."
    return f"**{label}** — You're closely aligned in your preferences."


def _describe_gap(dim: str, c_val: float, j_val: float) -> str:
    """Produce a one-liner about a dimension gap worth exploring."""
    label = _DIM_LABELS[dim]
    high_desc, low_desc = _DIM_DESCRIPTIONS[dim]

    if c_val > j_val:
        return (
            f"**{label}** — You lean {high_desc}, while the company "
            f"favors a more {low_desc} environment. "
            f"Worth discussing how teams handle this in practice."
        )
    return (
        f"**{label}** — You prefer a {low_desc} approach, while the "
        f"company culture is more {high_desc}. "
        f"Ask about flexibility during conversations."
    )


def _confidence_note(consistency: float) -> str:
    """Generate a confidence disclaimer based on consistency score."""
    if consistency >= 0.85:
        return (
            "Your responses were highly consistent, giving us strong "
            "confidence in this match assessment."
        )
    if consistency >= 0.65:
        return (
            "Your responses showed good overall consistency. "
            "This match assessment is reasonably reliable."
        )
    return (
        "Some of your responses showed variability across related questions. "
        "This match should be treated as directional rather than definitive."
    )


def generate_simple_report(
    candidate_name: str,
    company_name: str,
    match_score: float,
    dimension_scores: dict[str, float],  # noqa: ARG001 — reserved for future use
    candidate_dna: DimensionScores,
    company_dna: DimensionScores,
    consistency: float = 0.85,
) -> str:
    """Generate a template-based compatibility report.

    Sections:
        1. Why You're a Great Fit — top 3 closest dimensions.
        2. Something to Explore — top 2 widest-gap dimensions.
        3. Confidence Note — based on consistency score.

    Args:
        candidate_name: Display name of the candidate.
        company_name: Display name of the company.
        match_score: Overall match percentage (0-100).
        dimension_scores: Per-dimension compatibility (unused in v1).
        candidate_dna: Candidate's 8-dimension Career DNA.
        company_dna: Company's 8-dimension Company DNA.
        consistency: Candidate answer consistency in [0, 1].

    Returns:
        Markdown-formatted report string.
    """
    sorted_dims = _sorted_dimensions_by_gap(candidate_dna, company_dna)
    top_matches = sorted_dims[:3]
    top_gaps = sorted_dims[-2:]

    lines: list[str] = [
        f"# Match Report: {candidate_name} + {company_name}",
        f"**Overall Match: {match_score}%**",
        "",
        "## Why You're a Great Fit",
        "",
    ]

    for dim, c_val, j_val, _gap in top_matches:
        lines.append(f"- {_describe_alignment(dim, c_val, j_val)}")

    lines.extend([
        "",
        "## Something to Explore",
        "",
    ])

    for dim, c_val, j_val, _gap in top_gaps:
        lines.append(f"- {_describe_gap(dim, c_val, j_val)}")

    lines.extend([
        "",
        "## Confidence Note",
        "",
        _confidence_note(consistency),
    ])

    return "\n".join(lines)
