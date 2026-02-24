"""Career DNA scoring maps — choice, ranking, and budget question scoring.

Maps each question's options to dimension scores on a 0-100 scale.
Spectrum endpoints:
  - High end (70-85): fast pace / independent / data-driven / direct / high unc tolerance / generalist / mission-driven / structured
  - Mid range (40-60): balanced / contextual
  - Low end (15-30): deliberate pace / collaborative / intuition-driven / reserved / low unc tolerance / specialist / stability-driven / flexible
"""

# ── Choice questions: question_id -> option_key -> {dimension: score} ──

CAREER_SCORING: dict[str, dict[str, dict[str, float]]] = {
    "Q01": {
        "A": {"pace": 80, "decision": 50},
        "B": {"pace": 50, "decision": 55},
        "C": {"pace": 20, "decision": 75},
        "D": {"pace": 75, "decision": 60},
    },
    "Q02": {
        "A": {"collab": 20, "expression": 55},
        "B": {"collab": 75, "expression": 70},
        "C": {"collab": 45, "expression": 40},
        "D": {"collab": 60, "expression": 60},
    },
    "Q03": {
        "A": {"unc": 85},
        "B": {"unc": 45},
        "C": {"unc": 20},
        "D": {"unc": 70},
    },
    "Q04": {
        "A": {"expression": 80},
        "B": {"expression": 65},
        "C": {"expression": 20},
        "D": {"expression": 70},
    },
    "Q05": {
        "A": {"motiv": 80},
        "B": {"motiv": 65},
        "C": {"motiv": 50},
        "D": {"motiv": 25},
    },
    "Q06": {
        "A": {"pace": 25, "unc": 20},
        "B": {"pace": 60, "unc": 60},
        "C": {"pace": 80, "unc": 85},
        "D": {"pace": 45, "unc": 40},
    },
    "Q07": {
        "A": {"collab": 35, "growth": 40},
        "B": {"collab": 75, "growth": 55},
        "C": {"collab": 30, "growth": 60},
        "D": {"collab": 70, "growth": 70},
    },
    "Q08": {
        "A": {"expression": 85},
        "B": {"expression": 55},
        "C": {"expression": 45},
        "D": {"expression": 30},
    },
    # Q09 is ranking — see CAREER_RANKING_SCORING
    # Q10 is budget — see CAREER_BUDGET_DIMENSIONS
    "Q11": {
        "A": {"decision": 85},
        "B": {"decision": 30},
        "C": {"decision": 65},
        "D": {"decision": 40},
    },
    "Q12": {
        "A": {"pace": 80, "execution": 30},
        "B": {"pace": 30, "execution": 75},
        "C": {"pace": 20, "execution": 85},
        "D": {"pace": 70, "execution": 50},
    },
    "Q13": {
        "A": {"unc": 60},
        "B": {"unc": 80},
        "C": {"unc": 15},
        "D": {"unc": 45},
    },
    "Q14": {
        "A": {"decision": 25, "unc": 70},
        "B": {"decision": 75, "unc": 55},
        "C": {"decision": 60, "unc": 20},
        "D": {"decision": 40, "unc": 50},
    },
    "Q15": {
        "A": {"pace": 80, "execution": 25},
        "B": {"pace": 50, "execution": 65},
        "C": {"pace": 70, "execution": 30},
        "D": {"pace": 25, "execution": 85},
    },
    "Q16": {
        "A": {"collab": 20},
        "B": {"collab": 80},
        "C": {"collab": 45},
        "D": {"collab": 65},
    },
    "Q17": {
        "A": {"expression": 80, "decision": 50},
        "B": {"expression": 45, "decision": 60},
        "C": {"expression": 30, "decision": 35},
        "D": {"expression": 75, "decision": 55},
    },
    "Q18": {
        "A": {"expression": 80},
        "B": {"expression": 60},
        "C": {"expression": 45},
        "D": {"expression": 70},
    },
    "Q19": {
        "A": {"execution": 85},
        "B": {"execution": 60},
        "C": {"execution": 25},
        "D": {"execution": 50},
    },
    "Q20": {
        "A": {"execution": 80},
        "B": {"execution": 55},
        "C": {"execution": 45},
        "D": {"execution": 25},
    },
    "Q21": {
        "A": {"motiv": 85},
        "B": {"motiv": 60},
        "C": {"motiv": 45},
        "D": {"motiv": 30},
    },
    "Q22": {
        "A": {"growth": 20},
        "B": {"growth": 80},
        "C": {"growth": 65},
        "D": {"growth": 50},
    },
    "Q23": {
        "A": {"collab": 25},
        "B": {"collab": 85},
        "C": {"collab": 55},
        "D": {"collab": 50},
    },
    # Q24 is ranking — see CAREER_RANKING_SCORING
    "Q25": {
        "A": {"growth": 15},
        "B": {"growth": 85},
        "C": {"growth": 35},
        "D": {"growth": 70},
    },
    "Q26": {
        "A": {"unc": 85},
        "B": {"unc": 50},
        "C": {"unc": 60},
        "D": {"unc": 15},
    },
    # Q27 is budget — see CAREER_BUDGET_DIMENSIONS
    "Q28": {
        "A": {"growth": 15},
        "B": {"growth": 85},
        "C": {"growth": 30},
        "D": {"growth": 70},
    },
    "Q29": {
        "A": {"motiv": 65},
        "B": {"motiv": 55},
        "C": {"motiv": 25},
        "D": {"motiv": 35},
    },
    "Q30": {
        "A": {"expression": 60},
        "B": {"expression": 45},
        "C": {"expression": 35},
        "D": {"expression": 80},
    },
}


# ── Ranking questions: Borda scoring ────────────────────────────────
# Each option maps to a dimension. Rank 1 = high_score, last = low_score.
# Borda points: rank1=100, rank2=75, rank3=50, rank4=25, rank5=0

CAREER_RANKING_SCORING: dict[str, dict[str, str]] = {
    "Q09": {
        # option_key -> dimension it measures
        "A": "growth",      # specialist mastery
        "B": "growth",      # leadership track (high growth breadth)
        "C": "motiv",       # mission-driven
        "D": "motiv",       # financial/reward-driven
        "E": "motiv",       # autonomy-driven
    },
    "Q24": {
        "A": "motiv",       # mission + specialist
        "B": "growth",      # curiosity + generalist
        "C": "growth",      # mastery + depth (low growth = specialist)
        "D": "motiv",       # reward + breadth through influence
    },
}

# Direction for ranking: which end of spectrum does high rank push toward
CAREER_RANKING_DIRECTION: dict[str, dict[str, str]] = {
    "Q09": {
        "A": "specialist",   # growth low end
        "B": "generalist",   # growth high end
        "C": "mission",      # motiv high end
        "D": "financial",    # motiv mid
        "E": "autonomy",     # motiv low end
    },
    "Q24": {
        "A": "mission",      # motiv high
        "B": "generalist",   # growth high
        "C": "specialist",   # growth low
        "D": "financial",    # motiv mid
    },
}


# ── Budget questions: option -> dimension mapping ───────────────────
# Allocation % is used directly or normalized to 0-100 scale

CAREER_BUDGET_DIMENSIONS: dict[str, dict[str, str]] = {
    "Q10": {
        "A": "collab",       # solo → low collab (inverted)
        "B": "collab",       # team discussion → high collab
        "C": "collab",       # cross-functional → moderate collab
        "D": "pace",         # learning → low pace (inverted: exploring vs executing)
        "E": "execution",    # documentation → high execution (structured)
    },
    "Q27": {
        "A": "decision",     # quantitative → high decision (data-driven)
        "B": "decision",     # pattern recognition → low decision (intuition)
        "C": "decision",     # consensus → mid decision
        "D": "decision",     # first-principles → high decision (analytical)
    },
}

# Direction flags: whether higher allocation = higher or lower dimension score
CAREER_BUDGET_DIRECTION: dict[str, dict[str, str]] = {
    "Q10": {
        "A": "low_collab",
        "B": "high_collab",
        "C": "mid_collab",
        "D": "low_pace",
        "E": "high_execution",
    },
    "Q27": {
        "A": "high_decision",
        "B": "low_decision",
        "C": "mid_decision",
        "D": "high_decision",
    },
}
