"""Chat router."""

from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

from app.internal.data.chat import Chat, ChatInput

router = APIRouter(prefix="/v1")


@router.post(
    "/chat/completions",
    summary="Post a message to the chat.",
    response_model=Chat,
)
async def chat_post(input: ChatInput) -> ORJSONResponse:
    """Post a message to the chat.

    Args:
        input: The input to the chat.

    Returns:
        The response from the chat.
    """
    _ = input

    return Chat(message="Hello, World!")
