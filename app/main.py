"""Main application file."""

import logging

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from app.middlewares import RequestLoggingMiddleware
from app.routers import chat

logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)

api = FastAPI(default_response_class=ORJSONResponse)

api.add_middleware(RequestLoggingMiddleware, logger=logger)
api.include_router(chat.router)
