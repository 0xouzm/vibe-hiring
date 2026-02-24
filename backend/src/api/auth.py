"""Authentication routes — register, login, current user."""

import uuid
from datetime import datetime, timezone, timedelta

import bcrypt as _bcrypt
from fastapi import APIRouter, Depends, HTTPException, status
from jose import jwt

import aiosqlite

from src.core.config import settings
from src.core.deps import get_db, get_current_user_id
from src.models.user import (
    TokenResponse,
    UserCreate,
    UserLogin,
    UserResponse,
)

router = APIRouter()


def _create_token(user_id: str) -> str:
    """Generate a JWT access token for the given user."""
    expire = datetime.now(tz=timezone.utc) + timedelta(
        minutes=settings.jwt_expire_minutes,
    )
    payload = {"sub": user_id, "exp": expire}
    return jwt.encode(payload, settings.jwt_secret, algorithm=settings.jwt_algorithm)


def _user_response(row: aiosqlite.Row) -> UserResponse:
    """Build a UserResponse from a database row."""
    return UserResponse(
        id=row["id"],
        email=row["email"],
        name=row["name"],
        role=row["role"],
        company_id=row["company_id"],
    )


@router.post("/register", response_model=TokenResponse)
async def register(body: UserCreate, db: aiosqlite.Connection = Depends(get_db)):
    """Register a new candidate or HR user."""
    # Check duplicate email
    cursor = await db.execute(
        "SELECT id FROM users WHERE email = ?", (body.email,)
    )
    if await cursor.fetchone():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered",
        )

    user_id = str(uuid.uuid4())
    password_hash = _bcrypt.hashpw(body.password.encode(), _bcrypt.gensalt()).decode()
    now = datetime.now(tz=timezone.utc).isoformat()

    await db.execute(
        """
        INSERT INTO users (id, email, name, role, password_hash, company_id, created_at)
        VALUES (?, ?, ?, ?, ?, NULL, ?)
        """,
        (user_id, body.email, body.name, body.role.value, password_hash, now),
    )
    await db.commit()

    # Fetch back for response
    cursor = await db.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    row = await cursor.fetchone()

    return TokenResponse(
        access_token=_create_token(user_id),
        user=_user_response(row),
    )


@router.post("/login", response_model=TokenResponse)
async def login(body: UserLogin, db: aiosqlite.Connection = Depends(get_db)):
    """Authenticate and return a JWT token."""
    cursor = await db.execute(
        "SELECT * FROM users WHERE email = ?", (body.email,)
    )
    row = await cursor.fetchone()

    if not row or not _bcrypt.checkpw(body.password.encode(), row["password_hash"].encode()):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    return TokenResponse(
        access_token=_create_token(row["id"]),
        user=_user_response(row),
    )


@router.get("/me", response_model=UserResponse)
async def me(
    user_id: str = Depends(get_current_user_id),
    db: aiosqlite.Connection = Depends(get_db),
):
    """Return the currently authenticated user's profile."""
    cursor = await db.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    row = await cursor.fetchone()

    if not row:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return _user_response(row)
