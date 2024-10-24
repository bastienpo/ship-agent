"""Request logging middleware."""

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

        return await call_next(request)
