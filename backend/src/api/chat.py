"""Chat routes — AI conversational profiling."""

import json
import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException

import aiosqlite

from src.core.deps import get_db, get_current_user_id
from src.models.chat import ChatHistoryResponse, ChatMessageRequest, ChatMessageResponse
from src.services.chat_service import chat_completion

router = APIRouter()


@router.post("/profile", response_model=ChatMessageResponse)
async def send_message(
    body: ChatMessageRequest,
    user_id: str = Depends(get_current_user_id),
    db: aiosqlite.Connection = Depends(get_db),
):
    """Send a message and get AI response with entity extraction."""
    now = datetime.now(tz=timezone.utc).isoformat()

    # Save user message
    user_msg_id = str(uuid.uuid4())
    await db.execute(
        """INSERT INTO chat_messages (id, user_id, role, content, created_at)
           VALUES (?, ?, 'user', ?, ?)""",
        (user_msg_id, user_id, body.content, now),
    )

    # Build conversation history
    cursor = await db.execute(
        """SELECT role, content FROM chat_messages
           WHERE user_id = ? ORDER BY created_at ASC""",
        (user_id,),
    )
    rows = await cursor.fetchall()
    messages = [{"role": r["role"], "content": r["content"]} for r in rows]

    # Get AI response
    response_text, entities = await chat_completion(messages)

    # Save assistant message
    assistant_msg_id = str(uuid.uuid4())
    now2 = datetime.now(tz=timezone.utc).isoformat()
    await db.execute(
        """INSERT INTO chat_messages
           (id, user_id, role, content, extracted_entities, created_at)
           VALUES (?, ?, 'assistant', ?, ?, ?)""",
        (assistant_msg_id, user_id, response_text,
         json.dumps(entities) if entities else None, now2),
    )

    # Update profile with extracted entities
    if entities and "entities" in entities:
        await _merge_entities_to_profile(db, user_id, entities["entities"])

    await db.commit()

    return ChatMessageResponse(
        id=assistant_msg_id,
        user_id=user_id,
        role="assistant",
        content=response_text,
        extracted_entities=entities,
        created_at=now2,
    )


@router.get("/history", response_model=ChatHistoryResponse)
async def get_chat_history(
    user_id: str = Depends(get_current_user_id),
    db: aiosqlite.Connection = Depends(get_db),
):
    """Get all chat messages for the current user."""
    cursor = await db.execute(
        """SELECT id, user_id, role, content, extracted_entities, created_at
           FROM chat_messages WHERE user_id = ? ORDER BY created_at ASC""",
        (user_id,),
    )
    rows = await cursor.fetchall()

    messages = [
        ChatMessageResponse(
            id=r["id"],
            user_id=r["user_id"],
            role=r["role"],
            content=r["content"],
            extracted_entities=(
                json.loads(r["extracted_entities"]) if r["extracted_entities"] else None
            ),
            created_at=r["created_at"],
        )
        for r in rows
    ]

    return ChatHistoryResponse(messages=messages, total=len(messages))


async def _merge_entities_to_profile(
    db: aiosqlite.Connection,
    user_id: str,
    entities: dict,
) -> None:
    """Merge extracted entities into the user's profile."""
    now = datetime.now(tz=timezone.utc).isoformat()

    cursor = await db.execute(
        "SELECT id, skills FROM user_profiles WHERE user_id = ?", (user_id,)
    )
    row = await cursor.fetchone()

    new_skills = entities.get("skills", [])
    if not new_skills:
        return

    if row:
        existing_skills = json.loads(row["skills"]) if row["skills"] else []
        merged = list(set(existing_skills + new_skills))
        await db.execute(
            "UPDATE user_profiles SET skills = ?, updated_at = ? WHERE user_id = ?",
            (json.dumps(merged), now, user_id),
        )
    else:
        profile_id = str(uuid.uuid4())
        await db.execute(
            """INSERT INTO user_profiles (id, user_id, skills, created_at, updated_at)
               VALUES (?, ?, ?, ?, ?)""",
            (profile_id, user_id, json.dumps(new_skills), now, now),
        )
