"""Seed the database with demo data from demo-dataset.md."""

import asyncio
import json
import uuid
from datetime import datetime, timezone

import bcrypt as _bcrypt

from src.core.config import settings
from src.core.deps import init_db, close_db
from src.models.database import create_tables
from src.data.seed_data import SEED_COMPANIES, SEED_CANDIDATES, EXPECTED_MATCHES
from src.services.matching import run_matching
from src.services.report import generate_simple_report


async def seed() -> None:
    db = await init_db(settings.database_url)
    await create_tables(db)

    now = datetime.now(tz=timezone.utc).isoformat()
    default_hash = _bcrypt.hashpw(b"demo123", _bcrypt.gensalt()).decode()
    week_label = datetime.now(tz=timezone.utc).strftime("%Y-W%W")

    # Seed companies
    for comp in SEED_COMPANIES:
        await db.execute(
            "INSERT OR IGNORE INTO companies (id, name, industry, size, created_at) VALUES (?, ?, ?, ?, ?)",
            (comp["id"], comp["name"], comp["industry"], comp["size"], now),
        )
        # Company DNA scores
        await db.execute(
            "INSERT OR IGNORE INTO dna_scores (id, entity_type, entity_id, scores, consistency, created_at) VALUES (?, 'company', ?, ?, ?, ?)",
            (f"score-{comp['id']}", comp["id"], comp["scores"].model_dump_json(), 1.0, now),
        )
        # Create HR user for each company
        hr_id = f"hr-{comp['id']}"
        await db.execute(
            "INSERT OR IGNORE INTO users (id, email, name, role, password_hash, company_id, created_at) VALUES (?, ?, ?, 'hr', ?, ?, ?)",
            (hr_id, f"hr@{comp['id']}.example.com", f"HR at {comp['name']}", default_hash, comp["id"], now),
        )

    # Seed candidates
    for cand in SEED_CANDIDATES:
        await db.execute(
            "INSERT OR IGNORE INTO users (id, email, name, role, password_hash, company_id, created_at) VALUES (?, ?, ?, 'candidate', ?, NULL, ?)",
            (cand["id"], cand["email"], cand["name"], default_hash, now),
        )
        await db.execute(
            "INSERT OR IGNORE INTO dna_scores (id, entity_type, entity_id, scores, consistency, created_at) VALUES (?, 'candidate', ?, ?, ?, ?)",
            (f"score-{cand['id']}", cand["id"], cand["scores"].model_dump_json(), cand["consistency"], now),
        )

    # Generate matches
    for cand in SEED_CANDIDATES:
        for comp in SEED_COMPANIES:
            result = run_matching(
                candidate_id=cand["id"],
                candidate_scores=cand["scores"],
                candidate_consistency=cand["consistency"],
                company_id=comp["id"],
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
                "INSERT OR IGNORE INTO matches (id, candidate_id, company_id, score, dimension_scores, report, status, drop_week, created_at) VALUES (?, ?, ?, ?, ?, ?, 'pending', ?, ?)",
                (match_id, cand["id"], comp["id"], result.score, json.dumps(dim_dict), report, week_label, now),
            )

    await db.commit()
    await close_db()
    print(f"Seeded: {len(SEED_COMPANIES)} companies, {len(SEED_CANDIDATES)} candidates, {len(SEED_COMPANIES) * len(SEED_CANDIDATES)} matches")


if __name__ == "__main__":
    asyncio.run(seed())
