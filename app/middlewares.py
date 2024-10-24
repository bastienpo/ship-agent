"""Collection of middlewares."""

import logging

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """Request logging middleware."""

    logger: logging.Logger

    def __init__(self, app: ASGIApp, logger: logging.Logger) -> None:
        """Initialize the middleware."""
        super().__init__(app)
        self.logger = logger

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        """Dispatch the request."""
        self.logger.info("received request", extra={"request": request})

        print("Logging middleware called")

        return await call_next(request)


class TestMiddleware(BaseHTTPMiddleware):
    """Test middleware."""

    def __init__(self, app: ASGIApp) -> None:
        """Initialize the middleware."""
        super().__init__(app)

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        """Dispatch the request."""
        print("Test middleware called")
        return await call_next(request)
