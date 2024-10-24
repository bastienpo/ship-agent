"""Main application file."""

import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.middlewares import RequestLoggingMiddleware, TestMiddleware
from app.routers import healthcheck

logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)

api = FastAPI(
    title="HeyAPI Chat",
    summary="An API.",
    version="0.0.1",
)

api.include_router(healthcheck.router)

api.add_middleware(RequestLoggingMiddleware, logger=logger)
api.add_middleware(CORSMiddleware, allow_origins=["*"])
