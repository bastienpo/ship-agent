"""Healthcheck router."""

import os

from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

router = APIRouter(prefix="/v1")


@router.get("/healthcheck")
async def healthcheck() -> ORJSONResponse:
    """Healthcheck endpoint."""
    return {
        "status": "available",
        "system_info": {
            "environment": os.getenv("ENVIRONMENT"),
            "version": "0.0.1",
        },
    }
