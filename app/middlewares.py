"""Request logging middleware."""

import logging

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """Request logging middleware."""

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


class CommonHeadersMiddleware(BaseHTTPMiddleware):
    """Common headers middleware."""

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        """Dispatch the request."""
        response = await call_next(request)
        response.headers.append("Referrer-Policy", "strict-origin-when-cross-origin")
        response.headers.append("X-Content-Type-Options", "nosniff")
        response.headers.append("X-Frame-Options", "deny")
        response.headers.append("X-XSS-Protection", "0")

        return response
