"""Seed data for demo — 3 companies, 6 candidates, and expected matches.

All scores sourced from discuss/demo-dataset.md.
"""

from src.models.dna_score import DimensionScores

# ── Seed companies ──────────────────────────────────────────────────

SEED_COMPANIES: list[dict] = [
    {
        "id": "velocity-labs",
        "name": "Velocity Labs",
        "industry": "Technology",
        "size": "50-200",
        "description": (
            "Fast-growing B2B SaaS startup, just closed Series B. "
            "Rapid product iteration, free engineering culture, remote-first."
        ),
        "scores": DimensionScores(
            pace=82, collab=40, decision=55, expression=78,
            unc=75, growth=35, motiv=70, execution=30,
        ),
        "cas": 81,
        "cas_tier": "Silver",
    },
    {
        "id": "meridian-financial",
        "name": "Meridian Financial Systems",
        "industry": "Fintech",
        "size": "2000+",
        "description": (
            "Public financial technology company serving banks and insurers. "
            "High compliance requirements, stable engineering, hybrid work."
        ),
        "scores": DimensionScores(
            pace=32, collab=68, decision=80, expression=45,
            unc=25, growth=55, motiv=40, execution=82,
        ),
        "cas": 88,
        "cas_tier": "Gold",
    },
    {
        "id": "bloom-education",
        "name": "Bloom Education",
        "industry": "EdTech",
        "size": "50-200",
        "description": (
            "Mission-driven edtech company helping K-12 schools personalize "
            "teaching. Young, passionate engineering team, office-first."
        ),
        "scores": DimensionScores(
            pace=60, collab=75, decision=48, expression=72,
            unc=58, growth=70, motiv=88, execution=55,
        ),
        "cas": 74,
        "cas_tier": "Silver",
    },
]

# ── Seed candidates ─────────────────────────────────────────────────

SEED_CANDIDATES: list[dict] = [
    {
        "id": "alex-chen",
        "name": "Alex Chen",
        "title": "Senior Frontend Engineer",
        "email": "alex@example.com",
        "scores": DimensionScores(
            pace=78, collab=45, decision=60, expression=75,
            unc=70, growth=30, motiv=55, execution=35,
        ),
        "consistency": 0.91,
    },
    {
        "id": "maria-santos",
        "name": "Maria Santos",
        "title": "Full-Stack Engineer",
        "email": "maria@example.com",
        "scores": DimensionScores(
            pace=55, collab=72, decision=50, expression=65,
            unc=50, growth=75, motiv=82, execution=60,
        ),
        "consistency": 0.87,
    },
    {
        "id": "james-wright",
        "name": "James Wright",
        "title": "Backend Engineer",
        "email": "james@example.com",
        "scores": DimensionScores(
            pace=28, collab=60, decision=85, expression=55,
            unc=20, growth=25, motiv=35, execution=85,
        ),
        "consistency": 0.94,
    },
    {
        "id": "priya-sharma",
        "name": "Priya Sharma",
        "title": "Product Engineer",
        "email": "priya@example.com",
        "scores": DimensionScores(
            pace=68, collab=80, decision=42, expression=70,
            unc=62, growth=80, motiv=90, execution=50,
        ),
        "consistency": 0.89,
    },
    {
        "id": "david-kim",
        "name": "David Kim",
        "title": "DevOps Engineer",
        "email": "david@example.com",
        "scores": DimensionScores(
            pace=50, collab=35, decision=75, expression=40,
            unc=30, growth=40, motiv=45, execution=78,
        ),
        "consistency": 0.92,
    },
    {
        "id": "sophie-zhang",
        "name": "Sophie Zhang",
        "title": "Junior Engineer",
        "email": "sophie@example.com",
        "scores": DimensionScores(
            pace=72, collab=70, decision=45, expression=50,
            unc=65, growth=85, motiv=75, execution=45,
        ),
        "consistency": 0.78,
    },
]

# ── Expected match matrix (for validation) ──────────────────────────
# Format: (candidate_id, company_id, expected_match_percentage)

EXPECTED_MATCHES: list[tuple[str, str, int]] = [
    # Velocity Labs
    ("alex-chen", "velocity-labs", 91),
    ("maria-santos", "velocity-labs", 72),
    ("james-wright", "velocity-labs", 48),
    ("priya-sharma", "velocity-labs", 74),
    ("david-kim", "velocity-labs", 56),
    ("sophie-zhang", "velocity-labs", 76),
    # Meridian Financial
    ("alex-chen", "meridian-financial", 52),
    ("maria-santos", "meridian-financial", 65),
    ("james-wright", "meridian-financial", 92),
    ("priya-sharma", "meridian-financial", 58),
    ("david-kim", "meridian-financial", 83),
    ("sophie-zhang", "meridian-financial", 54),
    # Bloom Education
    ("alex-chen", "bloom-education", 72),
    ("maria-santos", "bloom-education", 89),
    ("james-wright", "bloom-education", 55),
    ("priya-sharma", "bloom-education", 93),
    ("david-kim", "bloom-education", 60),
    ("sophie-zhang", "bloom-education", 81),
]
