"""Resume upload routes — PDF upload and AI parsing."""

import json
import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

import aiosqlite

from src.core.deps import get_db, get_current_user_id
from src.models.profile import ProfileResponse
from src.services.resume_service import extract_text_from_pdf, parse_resume_text

router = APIRouter()


@router.post("/upload", response_model=ProfileResponse)
async def upload_resume(
    file: UploadFile = File(...),
    user_id: str = Depends(get_current_user_id),
    db: aiosqlite.Connection = Depends(get_db),
):
    """Upload a resume file, extract text, parse with AI, update profile."""
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file provided")

    # Read file content
    content = await file.read()
    if len(content) > 10 * 1024 * 1024:  # 10MB limit
        raise HTTPException(status_code=400, detail="File too large (max 10MB)")

    # Extract text based on file type
    if file.filename.lower().endswith(".pdf"):
        resume_text = extract_text_from_pdf(content)
    else:
        resume_text = content.decode("utf-8", errors="ignore")[:5000]

    if not resume_text.strip():
        raise HTTPException(status_code=400, detail="Could not extract text from file")

    # Parse with AI
    parsed = await parse_resume_text(resume_text)

    # Update profile
    now = datetime.now(tz=timezone.utc).isoformat()

    cursor = await db.execute(
        "SELECT id, skills FROM user_profiles WHERE user_id = ?", (user_id,)
    )
    existing = await cursor.fetchone()

    if existing:
        # Merge skills
        old_skills = json.loads(existing["skills"]) if existing["skills"] else []
        new_skills = parsed.get("skills", [])
        merged_skills = list(set(old_skills + new_skills))

        updates = ["resume_text = ?", "skills = ?", "updated_at = ?"]
        values = [resume_text[:10000], json.dumps(merged_skills), now]

        if parsed.get("title"):
            updates.append("title = ?")
            values.append(parsed["title"])
        if parsed.get("years_experience"):
            updates.append("years_experience = ?")
            values.append(parsed["years_experience"])
        if parsed.get("education"):
            updates.append("education = ?")
            values.append(json.dumps(parsed["education"]))
        if parsed.get("bio"):
            updates.append("bio = ?")
            values.append(parsed["bio"])

        values.append(user_id)
        await db.execute(
            f"UPDATE user_profiles SET {', '.join(updates)} WHERE user_id = ?",
            values,
        )
    else:
        profile_id = str(uuid.uuid4())
        await db.execute(
            """INSERT INTO user_profiles
               (id, user_id, title, years_experience, skills, education,
                bio, resume_text, created_at, updated_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                profile_id, user_id,
                parsed.get("title"),
                parsed.get("years_experience"),
                json.dumps(parsed.get("skills", [])),
                json.dumps(parsed.get("education", [])),
                parsed.get("bio"),
                resume_text[:10000],
                now, now,
            ),
        )

    await db.commit()

    # Return updated profile
    cursor = await db.execute(
        "SELECT * FROM user_profiles WHERE user_id = ?", (user_id,)
    )
    row = await cursor.fetchone()
    return ProfileResponse(
        id=row["id"],
        user_id=row["user_id"],
        title=row["title"],
        years_experience=row["years_experience"],
        skills=json.loads(row["skills"]) if row["skills"] else [],
        education=json.loads(row["education"]) if row["education"] else [],
        bio=row["bio"],
        resume_text=row["resume_text"],
        chat_summary=row["chat_summary"],
        location=row["location"],
        remote_preference=row["remote_preference"],
        salary_expectation=(
            json.loads(row["salary_expectation"]) if row["salary_expectation"] else None
        ),
        created_at=row["created_at"],
        updated_at=row["updated_at"],
    )
