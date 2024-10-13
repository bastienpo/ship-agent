"""Healthcheck router."""

import os

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
            "environment": os.getenv("ENVIRONMENT"),
            "version": "0.0.1",
        },
    }
