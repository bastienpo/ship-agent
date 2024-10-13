"""Chat router."""

from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

router = APIRouter(prefix="/v1")


@router.post("/chat/completions", summary="")
async def chat_post() -> ORJSONResponse:
    """Post a message to the chat."""
    return {"message": "Hello, World!"}
