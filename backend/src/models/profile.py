"""User profile Pydantic models."""

from pydantic import BaseModel


class ProfileUpdate(BaseModel):
    """Request body for updating user profile."""

    title: str | None = None
    years_experience: int | None = None
    skills: list[str] | None = None
    education: list[dict] | None = None
    bio: str | None = None
    location: str | None = None
    remote_preference: str | None = None  # remote / hybrid / onsite
    salary_expectation: dict | None = None  # {min, max, currency}


class ProfileResponse(BaseModel):
    """Public representation of a user profile."""

    id: str
    user_id: str
    title: str | None = None
    years_experience: int | None = None
    skills: list[str] = []
    education: list[dict] = []
    bio: str | None = None
    resume_text: str | None = None
    chat_summary: str | None = None
    location: str | None = None
    remote_preference: str | None = None
    salary_expectation: dict | None = None
    created_at: str
    updated_at: str
