"""Weekly Drop service — curate and deliver top matches to candidates and companies."""

import json
import uuid
from datetime import datetime, timezone

import aiosqlite


async def generate_candidate_drop(
    db: aiosqlite.Connection,
    candidate_id: str,
) -> str:
    """Generate a weekly drop for a candidate — top 3 pending matches by score."""
    cursor = await db.execute(
        """
        SELECT id FROM matches
        WHERE candidate_id = ? AND status = 'pending'
            AND candidate_action IS NULL
        ORDER BY score DESC
        LIMIT 3
        """,
        (candidate_id,),
    )
    rows = await cursor.fetchall()

    if not rows:
        msg = f"No pending matches for candidate {candidate_id}"
        raise ValueError(msg)

    match_ids = [row[0] for row in rows]
    drop_id = str(uuid.uuid4())
    now = datetime.now(tz=timezone.utc)
    week_label = now.strftime("%Y-W%W")

    await db.execute(
        """
        INSERT INTO drops (id, week, target_type, target_id, match_ids,
                          revealed_at, created_at)
        VALUES (?, ?, 'candidate', ?, ?, ?, ?)
        """,
        (drop_id, week_label, candidate_id,
         json.dumps(match_ids), now.isoformat(), now.isoformat()),
    )
    await db.commit()
    return drop_id


async def generate_company_drop(
    db: aiosqlite.Connection,
    company_id: str,
) -> str:
    """Generate a weekly drop for a company — top 5 candidates per role."""
    # Get active roles for this company
    cursor = await db.execute(
        "SELECT id FROM roles WHERE company_id = ? AND is_active = 1",
        (company_id,),
    )
    role_rows = await cursor.fetchall()

    if not role_rows:
        msg = f"No active roles for company {company_id}"
        raise ValueError(msg)

    all_match_ids: list[str] = []
    for role_row in role_rows:
        role_id = role_row[0]
        cursor = await db.execute(
            """
            SELECT id FROM matches
            WHERE company_id = ? AND role_id = ? AND status = 'pending'
                AND company_action IS NULL
            ORDER BY score DESC
            LIMIT 5
            """,
            (company_id, role_id),
        )
        matches = await cursor.fetchall()
        all_match_ids.extend(m[0] for m in matches)

    if not all_match_ids:
        msg = f"No pending matches for company {company_id}"
        raise ValueError(msg)

    drop_id = str(uuid.uuid4())
    now = datetime.now(tz=timezone.utc)
    week_label = now.strftime("%Y-W%W")

    await db.execute(
        """
        INSERT INTO drops (id, week, target_type, target_id, match_ids,
                          revealed_at, created_at)
        VALUES (?, ?, 'company', ?, ?, ?, ?)
        """,
        (drop_id, week_label, company_id,
         json.dumps(all_match_ids), now.isoformat(), now.isoformat()),
    )
    await db.commit()
    return drop_id


async def get_current_drop(
    db: aiosqlite.Connection,
    target_id: str,
    target_type: str = "candidate",
) -> dict | None:
    """Retrieve the most recent drop for a target (candidate or company)."""
    cursor = await db.execute(
        """
        SELECT id, week, match_ids, revealed_at
        FROM drops
        WHERE target_id = ? AND target_type = ?
        ORDER BY revealed_at DESC
        LIMIT 1
        """,
        (target_id, target_type),
    )
    row = await cursor.fetchone()
    if not row:
        return None

    drop_id, week, match_ids_json, revealed_at = row
    match_ids: list[str] = json.loads(match_ids_json)

    matches: list[dict] = []
    for mid in match_ids:
        mcursor = await db.execute(
            """
            SELECT id, candidate_id, company_id, role_id, score,
                   dimension_scores, report, status,
                   candidate_action, company_action
            FROM matches WHERE id = ?
            """,
            (mid,),
        )
        mrow = await mcursor.fetchone()
        if mrow:
            matches.append({
                "id": mrow[0],
                "candidate_id": mrow[1],
                "company_id": mrow[2],
                "role_id": mrow[3],
                "score": mrow[4],
                "dimension_scores": json.loads(mrow[5]) if mrow[5] else {},
                "report": mrow[6],
                "status": mrow[7],
                "candidate_action": mrow[8],
                "company_action": mrow[9],
            })

    return {
        "id": drop_id,
        "week": week,
        "matches": matches,
        "revealed_at": revealed_at,
    }


def compute_match_status(
    candidate_action: str | None,
    company_action: str | None,
) -> str:
    """Derive the overall match status from both sides' actions."""
    if candidate_action == "pass" or company_action == "pass":
        return "passed"
    if candidate_action == "accept" and company_action == "accept":
        return "mutual"
    if candidate_action == "accept":
        return "candidate_accepted"
    if company_action == "accept":
        return "company_accepted"
    return "pending"
