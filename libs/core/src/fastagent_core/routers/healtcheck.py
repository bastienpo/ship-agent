"""Router for healthcheck."""

from fastapi import APIRouter

router = APIRouter(prefix="/v1", tags=["healthcheck"])


@router.get("/healthcheck")
async def healthcheck() -> dict[str, str]:
    """Healthcheck endpoint."""
    return {"status": "available"}
