"""Weekly Drop service — curate and deliver top matches to candidates."""

import json
import uuid
from datetime import datetime, timezone

import aiosqlite


async def generate_drop(
    db: aiosqlite.Connection,
    candidate_id: str,
) -> str:
    """Generate a weekly drop by selecting top-3 pending matches.

    Steps:
        1. Fetch all pending matches for the candidate.
        2. Sort by score descending, take top 3.
        3. Insert a new drop record linking to those matches.
        4. Return the new drop_id.

    Args:
        db: Active aiosqlite database connection.
        candidate_id: The candidate receiving the drop.

    Returns:
        The generated drop ID string.
    """
    # 1. Fetch pending matches, ordered by score
    cursor = await db.execute(
        """
        SELECT id, company_id, score, dimension_scores, report
        FROM matches
        WHERE candidate_id = ? AND status = 'pending'
        ORDER BY score DESC
        LIMIT 3
        """,
        (candidate_id,),
    )
    rows = await cursor.fetchall()

    if not rows:
        msg = f"No pending matches for candidate {candidate_id}"
        raise ValueError(msg)

    # 2. Build match ID list
    match_ids = [row[0] for row in rows]

    # 3. Create drop record
    drop_id = str(uuid.uuid4())
    week_label = datetime.now(tz=timezone.utc).strftime("%Y-W%W")
    revealed_at = datetime.now(tz=timezone.utc).isoformat()

    now = datetime.now(tz=timezone.utc).isoformat()
    await db.execute(
        """
        INSERT INTO drops (id, candidate_id, week, match_ids, revealed_at, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (drop_id, candidate_id, week_label, json.dumps(match_ids), revealed_at, now),
    )
    await db.commit()

    return drop_id


async def get_current_drop(
    db: aiosqlite.Connection,
    candidate_id: str,
) -> dict | None:
    """Retrieve the most recent drop for a candidate.

    Args:
        db: Active aiosqlite database connection.
        candidate_id: The candidate whose drop to fetch.

    Returns:
        A dict with drop metadata and nested match details, or None.
    """
    cursor = await db.execute(
        """
        SELECT id, week, match_ids, revealed_at
        FROM drops
        WHERE candidate_id = ?
        ORDER BY revealed_at DESC
        LIMIT 1
        """,
        (candidate_id,),
    )
    row = await cursor.fetchone()
    if not row:
        return None

    drop_id, week, match_ids_json, revealed_at = row
    match_ids: list[str] = json.loads(match_ids_json)

    # Fetch each match's details
    matches: list[dict] = []
    for mid in match_ids:
        mcursor = await db.execute(
            """
            SELECT id, candidate_id, company_id, score,
                   dimension_scores, report, status
            FROM matches
            WHERE id = ?
            """,
            (mid,),
        )
        mrow = await mcursor.fetchone()
        if mrow:
            matches.append({
                "id": mrow[0],
                "candidate_id": mrow[1],
                "company_id": mrow[2],
                "score": mrow[3],
                "dimension_scores": json.loads(mrow[4]) if mrow[4] else {},
                "report": mrow[5],
                "status": mrow[6],
            })

    return {
        "id": drop_id,
        "week": week,
        "matches": matches,
        "revealed_at": revealed_at,
    }
