from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

router = APIRouter(prefix="/v1")


@router.post("/chat")
def chat_post() -> ORJSONResponse:
    return {"message": "Hello, World!"}
