"""Chat router."""

from fastapi import APIRouter

from app.internal.data import Chat, ChatInput

router = APIRouter(prefix="/v1", tags=["chat"])


@router.post(
    "/chat/completions",
    summary="Generate a completion for the provided messages.",
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
