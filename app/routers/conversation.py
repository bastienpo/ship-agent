"""Conversation router."""

from fastapi import APIRouter, status

router = APIRouter(prefix="/v1", tags=["conversation"])


@router.post(
    "/conversations",
    summary="Create a new conversation.",
)
def create_conversation() -> tuple[int, dict[str, int]]:
    """Create a new conversation."""
    return status.HTTP_201_CREATED, {"id": 0}


@router.post(
    "/conversations/{id}/messages",
    summary="Send a message to a conversation.",
)
def send_conversation_message(id: int) -> tuple[int, dict[str, int]]:
    """Send a message to a conversation."""
    _ = id
    return status.HTTP_200_OK, {"id": 0}


@router.get(
    "/conversations/{id}",
    summary="Get a conversation by ID.",
)
def show_conversation(id: int) -> tuple[int, dict[str, int]]:
    """Get a conversation by ID."""
    return status.HTTP_200_OK, {"id": id}
