"""Company DNA scoring maps — choice, ranking, and budget question scoring.

Maps each Company DNA question's options to dimension scores on a 0-100 scale.
Same spectrum convention as Career DNA scoring_maps.py.
"""

# ── Choice questions: question_id -> option_key -> {dimension: score} ──

COMPANY_SCORING: dict[str, dict[str, dict[str, float]]] = {
    "CQ01": {
        "A": {"pace": 85, "decision": 45},
        "B": {"pace": 55, "decision": 50},
        "C": {"pace": 20, "decision": 60},
        "D": {"pace": 65, "decision": 55},
    },
    "CQ02": {
        "A": {"collab": 20, "expression": 55},
        "B": {"collab": 75, "expression": 70},
        "C": {"collab": 45, "expression": 40},
        "D": {"collab": 60, "expression": 60},
    },
    "CQ03": {
        "A": {"unc": 85},
        "B": {"unc": 50},
        "C": {"unc": 15},
        "D": {"unc": 65},
    },
    "CQ04": {
        "A": {"expression": 85},
        "B": {"expression": 60},
        "C": {"expression": 25},
        "D": {"expression": 40},
    },
    "CQ05": {
        "A": {"motiv": 85},
        "B": {"motiv": 60},
        "C": {"motiv": 45},
        "D": {"motiv": 25},
    },
    "CQ06": {
        "A": {"pace": 20, "unc": 15},
        "B": {"pace": 60, "unc": 60},
        "C": {"pace": 80, "unc": 85},
        "D": {"pace": 45, "unc": 40},
    },
    "CQ07": {
        "A": {"collab": 35, "growth": 40},
        "B": {"collab": 55, "growth": 30},
        "C": {"collab": 65, "growth": 65},
        "D": {"collab": 80, "growth": 75},
    },
    "CQ08": {
        "A": {"expression": 80, "execution": 70},
        "B": {"expression": 60, "execution": 80},
        "C": {"expression": 25, "execution": 25},
        "D": {"expression": 50, "execution": 60},
    },
    "CQ09": {
        "A": {"decision": 30, "unc": 55},
        "B": {"decision": 80, "unc": 45},
        "C": {"decision": 45, "unc": 50},
        "D": {"decision": 55, "unc": 70},
    },
    "CQ10": {
        "A": {"collab": 20},
        "B": {"collab": 80},
        "C": {"collab": 50},
        "D": {"collab": 65},
    },
    "CQ11": {
        "A": {"growth": 20},
        "B": {"growth": 80},
        "C": {"growth": 65},
        "D": {"growth": 50},
    },
    "CQ12": {
        "A": {"motiv": 65},
        "B": {"motiv": 55},
        "C": {"motiv": 35},
        "D": {"motiv": 25},
    },
    "CQ13": {
        "A": {"execution": 30, "pace": 80},
        "B": {"execution": 70, "pace": 30},
        "C": {"execution": 85, "pace": 15},
        "D": {"execution": 50, "pace": 65},
    },
    "CQ14": {
        "A": {"execution": 85},
        "B": {"execution": 60},
        "C": {"execution": 25},
        "D": {"execution": 50},
    },
    "CQ15": {
        "A": {"growth": 15},
        "B": {"growth": 85},
        "C": {"growth": 35},
        "D": {"growth": 70},
    },
    "CQ16": {
        "A": {"expression": 60, "collab": 65},
        "B": {"expression": 45, "collab": 50},
        "C": {"expression": 35, "collab": 40},
        "D": {"expression": 80, "collab": 70},
    },
}


# ── Budget questions: option -> dimension mapping ───────────────────

COMPANY_BUDGET_DIMENSIONS: dict[str, dict[str, str]] = {
    "CQ17": {
        "A": "collab",       # heads-down → low collab (inverted)
        "B": "collab",       # team discussion → high collab
        "C": "collab",       # cross-functional → moderate collab
        "D": "pace",         # learning → low pace (inverted)
        "E": "execution",    # documentation → high execution
    },
    "CQ18": {
        "A": "decision",     # quantitative → high decision
        "B": "decision",     # experience → low decision (intuition)
        "C": "decision",     # stakeholder → mid decision
        "D": "decision",     # first-principles → high decision
    },
}

COMPANY_BUDGET_DIRECTION: dict[str, dict[str, str]] = {
    "CQ17": {
        "A": "low_collab",
        "B": "high_collab",
        "C": "mid_collab",
        "D": "low_pace",
        "E": "high_execution",
    },
    "CQ18": {
        "A": "high_decision",
        "B": "low_decision",
        "C": "mid_decision",
        "D": "high_decision",
    },
}


# ── Ranking questions: option -> dimension mapping ──────────────────

COMPANY_RANKING_SCORING: dict[str, dict[str, str]] = {
    "CQ19": {
        "A": "motiv",       # mission-driven
        "B": "growth",      # growth engine
        "C": "motiv",       # craft culture (mastery)
        "D": "motiv",       # well-compensated
        "E": "motiv",       # life-friendly
    },
    "CQ20": {
        "A": "pace",        # speed-to-impact → pace + execution (flex)
        "B": "execution",   # structured thinker → execution (planned)
        "C": "expression",  # candid communicator → expression (direct)
        "D": "collab",      # independent operator → collab (independent)
        "E": "growth",      # curious learner → growth (breadth)
    },
}

COMPANY_RANKING_DIRECTION: dict[str, dict[str, str]] = {
    "CQ19": {
        "A": "mission",
        "B": "generalist",
        "C": "specialist",
        "D": "financial",
        "E": "balance",
    },
    "CQ20": {
        "A": "high_pace",
        "B": "high_execution",
        "C": "high_expression",
        "D": "low_collab",
        "E": "high_growth",
    },
}
