"""Main application file."""

import logging

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from app.middlewares import CommonHeadersMiddleware, RequestLoggingMiddleware
from app.routers import chat, healthcheck

logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)

api = FastAPI(
    title="HeyAPI Chat",
    summary="An API compatible with OpenAI compatibility.",
    default_response_class=ORJSONResponse,
)

api.include_router(healthcheck.router)
api.include_router(chat.router)

api.add_middleware(RequestLoggingMiddleware, logger=logger)
api.add_middleware(CommonHeadersMiddleware)
