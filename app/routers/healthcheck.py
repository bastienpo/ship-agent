"""Healthcheck router."""


from fastapi import APIRouter

from app.internal.data.healthcheck import Healthcheck

router = APIRouter(prefix="/v1", tags=["healthcheck"])


@router.get(
    "/healthcheck",
    summary="Healthcheck endpoint.",
    response_model=Healthcheck,
)
async def healthcheck() -> Healthcheck:
    """Healthcheck endpoint."""
    return {
        "status": "available",
        "system_info": {
            "environment": "development",
            "version": "0.0.1",
        },
    }
