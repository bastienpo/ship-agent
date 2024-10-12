import logging
from fastapi import Request
from datetime import datetime, timezone
from typing import Any


class LoggingFormatter(logging.Formatter):
    """Custom formatter for logging."""

    def format(self, record: dict[str, Any]) -> str:
        """
        Format the record to a string.

        Args:
            record: The record to format.

        Returns:
            The formatted record as a string.
        """
        timestamp = datetime.now(timezone.utc).astimezone().isoformat()

        log_msg = (
            f'time={timestamp} level={record.levelname} msg="{record.getMessage()}"'
        )

        if hasattr(record, "request"):
            req: Request = record.request
            log_msg += f' ip={req.client.host}:{req.client.port} proto={req.scope["scheme"].upper()}/{req.scope["http_version"]} method={req.method} uri={req.url.path}'

        return log_msg
