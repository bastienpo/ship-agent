"""Chat router."""

from fastapi import APIRouter

from app.internal.data.chat import Chat, ChatInput

router = APIRouter(prefix="/v1")


@router.post(
    "/chat/completions",
    summary="Post a message to the chat.",
    response_model=Chat,
)
async def chat_post(data: ChatInput) -> Chat:
    """Post a message to the chat.

    Args:
        data: The input to the chat.

    Returns:
        The response from the chat.
    """
    _ = data

    return Chat(message="Hello, World!")
