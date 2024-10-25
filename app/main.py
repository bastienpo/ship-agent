"""Main application file."""

import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.internal.data.database import get_database_pool
from app.internal.server.handlers import http_exception_handler
from app.internal.server.middlewares import RequestLoggingMiddleware
from app.internal.settings import get_settings
from app.routers import healthcheck, users

logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Manage the lifespan of the application.

    Args:
        app: The FastAPI application.
    """
    # Retrieve the settings and open a connection pool to the database
    app.async_pool = get_database_pool()
    await app.async_pool.open()
    logger.info("Connection pool opened")
    yield

    # Close the connection pool when the application shuts down
    await app.async_pool.close()
    logger.info("Connection pool closed")


api = FastAPI(
    title="HeyAPI Chat",
    version="0.0.1",
    lifespan=lifespan,
    dependencies=[Depends(get_settings)],
)

api.add_exception_handler(StarletteHTTPException, http_exception_handler)

api.include_router(healthcheck.router)
api.include_router(users.router)

api.add_middleware(RequestLoggingMiddleware, logger=logger)
api.add_middleware(CORSMiddleware, allow_origins=["*"])
