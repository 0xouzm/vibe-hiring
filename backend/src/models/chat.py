"""Chat message Pydantic models."""

from pydantic import BaseModel


class ChatMessageRequest(BaseModel):
    """Request body for sending a chat message."""

    content: str


class ChatMessageResponse(BaseModel):
    """A single chat message."""

    id: str
    user_id: str
    role: str  # user / assistant
    content: str
    extracted_entities: dict | None = None
    created_at: str


class ChatHistoryResponse(BaseModel):
    """Chat history for a user."""

    messages: list[ChatMessageResponse]
    total: int
