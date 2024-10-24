"""Main application file."""

import logging

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.internal.server.handlers import http_exception_handler
from app.internal.server.middlewares import RequestLoggingMiddleware
from app.internal.settings import get_settings
from app.routers import healthcheck

logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)

api = FastAPI(
    title="HeyAPI Chat",
    summary="An API.",
    version="0.0.1",
    dependencies=[Depends(get_settings)],
    exception_handlers={StarletteHTTPException: http_exception_handler},
)

api.include_router(healthcheck.router)

api.add_middleware(RequestLoggingMiddleware, logger=logger)
api.add_middleware(CORSMiddleware, allow_origins=["*"])
