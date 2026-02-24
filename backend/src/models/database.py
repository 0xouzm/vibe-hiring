"""SQLite database schema and table creation logic."""

import aiosqlite


async def create_tables(db: aiosqlite.Connection) -> None:
    """Create all application tables if they do not exist."""

    await db.execute("""
        CREATE TABLE IF NOT EXISTS companies (
            id          TEXT PRIMARY KEY,
            name        TEXT NOT NULL,
            industry    TEXT NOT NULL,
            size        TEXT NOT NULL,
            created_at  TEXT NOT NULL
        )
    """)

    await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id            TEXT PRIMARY KEY,
            email         TEXT NOT NULL UNIQUE,
            name          TEXT NOT NULL,
            role          TEXT NOT NULL CHECK (role IN ('candidate', 'hr')),
            password_hash TEXT NOT NULL,
            company_id    TEXT,
            created_at    TEXT NOT NULL,
            FOREIGN KEY (company_id) REFERENCES companies (id)
        )
    """)

    await db.execute("""
        CREATE TABLE IF NOT EXISTS career_answers (
            id          TEXT PRIMARY KEY,
            user_id     TEXT NOT NULL,
            answers     TEXT NOT NULL,
            created_at  TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)

    await db.execute("""
        CREATE TABLE IF NOT EXISTS company_answers (
            id          TEXT PRIMARY KEY,
            user_id     TEXT NOT NULL,
            company_id  TEXT NOT NULL,
            answers     TEXT NOT NULL,
            created_at  TEXT NOT NULL,
            FOREIGN KEY (user_id)    REFERENCES users (id),
            FOREIGN KEY (company_id) REFERENCES companies (id)
        )
    """)

    await db.execute("""
        CREATE TABLE IF NOT EXISTS dna_scores (
            id            TEXT PRIMARY KEY,
            entity_type   TEXT NOT NULL CHECK (entity_type IN ('candidate', 'company')),
            entity_id     TEXT NOT NULL,
            scores        TEXT NOT NULL,
            consistency   REAL NOT NULL,
            created_at    TEXT NOT NULL
        )
    """)

    await db.execute("""
        CREATE TABLE IF NOT EXISTS matches (
            id                TEXT PRIMARY KEY,
            candidate_id      TEXT NOT NULL,
            company_id        TEXT NOT NULL,
            score             REAL NOT NULL,
            dimension_scores  TEXT NOT NULL,
            report            TEXT,
            status            TEXT NOT NULL CHECK (status IN ('pending', 'accepted', 'passed')),
            drop_week         TEXT NOT NULL,
            created_at        TEXT NOT NULL,
            FOREIGN KEY (candidate_id) REFERENCES users (id),
            FOREIGN KEY (company_id)   REFERENCES companies (id)
        )
    """)

    await db.execute("""
        CREATE TABLE IF NOT EXISTS drops (
            id            TEXT PRIMARY KEY,
            week          TEXT NOT NULL,
            candidate_id  TEXT NOT NULL,
            match_ids     TEXT NOT NULL,
            revealed_at   TEXT,
            created_at    TEXT NOT NULL,
            FOREIGN KEY (candidate_id) REFERENCES users (id)
        )
    """)

    await db.commit()
