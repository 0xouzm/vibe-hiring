"""Seed the database with demo data from demo-dataset.md."""

import asyncio
import json
import uuid
from datetime import datetime, timezone

import bcrypt as _bcrypt

from src.core.config import settings
from src.core.deps import init_db, close_db
from src.models.database import create_tables
from src.data.seed_data import (
    SEED_COMPANIES,
    SEED_CANDIDATES,
    SEED_ROLES,
    SEED_PROFILES,
)
from src.services.matching import run_matching
from src.services.report import generate_simple_report


async def _seed_companies(db, now: str, default_hash: str) -> None:
    """Insert companies, their DNA scores, and HR users."""
    for comp in SEED_COMPANIES:
        await db.execute(
            "INSERT OR IGNORE INTO companies (id, name, industry, size, created_at) "
            "VALUES (?, ?, ?, ?, ?)",
            (comp["id"], comp["name"], comp["industry"], comp["size"], now),
        )
        await db.execute(
            "INSERT OR IGNORE INTO dna_scores "
            "(id, entity_type, entity_id, scores, consistency, created_at) "
            "VALUES (?, 'company', ?, ?, ?, ?)",
            (f"score-{comp['id']}", comp["id"],
             comp["scores"].model_dump_json(), 1.0, now),
        )
        hr_id = f"hr-{comp['id']}"
        await db.execute(
            "INSERT OR IGNORE INTO users "
            "(id, email, name, role, password_hash, company_id, created_at) "
            "VALUES (?, ?, ?, 'hr', ?, ?, ?)",
            (hr_id, f"hr@{comp['id']}.example.com",
             f"HR at {comp['name']}", default_hash, comp["id"], now),
        )


async def _seed_roles(db, now: str) -> None:
    """Insert open roles for each company."""
    for role in SEED_ROLES:
        await db.execute(
            "INSERT OR IGNORE INTO roles "
            "(id, company_id, title, level, skills, nice_to_have, "
            "salary_range, location, remote_policy, description, created_at) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                role["id"], role["company_id"], role["title"], role["level"],
                json.dumps(role["skills"]), json.dumps(role["nice_to_have"]),
                json.dumps(role["salary_range"]), role["location"],
                role["remote_policy"], role["description"], now,
            ),
        )


async def _seed_candidates(db, now: str, default_hash: str) -> None:
    """Insert candidates, their DNA scores, and profiles."""
    for cand in SEED_CANDIDATES:
        await db.execute(
            "INSERT OR IGNORE INTO users "
            "(id, email, name, role, password_hash, company_id, created_at) "
            "VALUES (?, ?, ?, 'candidate', ?, NULL, ?)",
            (cand["id"], cand["email"], cand["name"], default_hash, now),
        )
        await db.execute(
            "INSERT OR IGNORE INTO dna_scores "
            "(id, entity_type, entity_id, scores, consistency, created_at) "
            "VALUES (?, 'candidate', ?, ?, ?, ?)",
            (f"score-{cand['id']}", cand["id"],
             cand["scores"].model_dump_json(), cand["consistency"], now),
        )

    # Insert profiles
    for prof in SEED_PROFILES:
        profile_id = str(uuid.uuid4())
        await db.execute(
            "INSERT OR IGNORE INTO user_profiles "
            "(id, user_id, title, years_experience, skills, education, "
            "bio, location, remote_preference, created_at, updated_at) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                profile_id, prof["user_id"], prof["title"],
                prof["years_experience"], json.dumps(prof["skills"]),
                json.dumps(prof["education"]), prof["bio"],
                prof["location"], prof["remote_preference"], now, now,
            ),
        )


async def _seed_matches(db, now: str, week_label: str) -> None:
    """Generate all candidate x role matches."""
    # Build company scores lookup
    company_scores: dict[str, dict] = {}
    for comp in SEED_COMPANIES:
        company_scores[comp["id"]] = {
            "name": comp["name"],
            "scores": comp["scores"],
        }

    for cand in SEED_CANDIDATES:
        for role in SEED_ROLES:
            comp = company_scores[role["company_id"]]
            result = run_matching(
                candidate_id=cand["id"],
                candidate_scores=cand["scores"],
                candidate_consistency=cand["consistency"],
                company_id=role["company_id"],
                company_scores=comp["scores"],
            )
            dim_dict = result.dimension_scores.model_dump()
            report = generate_simple_report(
                candidate_name=cand["name"],
                company_name=comp["name"],
                match_score=result.score,
                dimension_scores=dim_dict,
                candidate_dna=cand["scores"],
                company_dna=comp["scores"],
                consistency=cand["consistency"],
            )
            match_id = str(uuid.uuid4())
            await db.execute(
                "INSERT OR IGNORE INTO matches "
                "(id, candidate_id, company_id, role_id, score, "
                "dimension_scores, report, status, drop_week, created_at) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, 'pending', ?, ?)",
                (
                    match_id, cand["id"], role["company_id"], role["id"],
                    result.score, json.dumps(dim_dict), report,
                    week_label, now,
                ),
            )


async def seed() -> None:
    db = await init_db(settings.database_url)
    await create_tables(db)

    now = datetime.now(tz=timezone.utc).isoformat()
    default_hash = _bcrypt.hashpw(b"demo123", _bcrypt.gensalt()).decode()
    week_label = datetime.now(tz=timezone.utc).strftime("%Y-W%W")

    await _seed_companies(db, now, default_hash)
    await _seed_roles(db, now)
    await _seed_candidates(db, now, default_hash)
    await _seed_matches(db, now, week_label)

    await db.commit()
    await close_db()

    print(
        f"Seeded: {len(SEED_COMPANIES)} companies, "
        f"{len(SEED_ROLES)} roles, "
        f"{len(SEED_CANDIDATES)} candidates, "
        f"{len(SEED_CANDIDATES) * len(SEED_ROLES)} matches"
    )


if __name__ == "__main__":
    asyncio.run(seed())
