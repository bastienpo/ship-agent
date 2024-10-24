"""Main application file."""

import logging

from fastapi import FastAPI

from app.middlewares import RequestLoggingMiddleware
from app.routers import healthcheck

logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)

api = FastAPI(
    title="HeyAPI Chat",
    summary="An API for chatting with LLMs with OpenAI compatibility.",
)

api.include_router(healthcheck.router)
# api.add_middleware(RequestLoggingMiddleware, logger=logger)
