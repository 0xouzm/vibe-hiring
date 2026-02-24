"""User-related Pydantic models."""

from enum import Enum

from pydantic import BaseModel, EmailStr


class UserRole(str, Enum):
    """Allowed user roles."""

    candidate = "candidate"
    hr = "hr"


class UserCreate(BaseModel):
    """Request body for user registration."""

    email: EmailStr
    name: str
    password: str
    role: UserRole


class UserLogin(BaseModel):
    """Request body for user login."""

    email: EmailStr
    password: str


class UserResponse(BaseModel):
    """Public user representation returned by the API."""

    id: str
    email: str
    name: str
    role: UserRole
    company_id: str | None = None


class TokenResponse(BaseModel):
    """Authentication token returned after login / registration."""

    access_token: str
    token_type: str = "bearer"
    user: UserResponse
