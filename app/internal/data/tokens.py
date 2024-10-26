"""Token models for activation and authentication."""

import base64
import hashlib
from datetime import UTC, datetime, timedelta
from secrets import token_bytes
from typing import Literal

from psycopg import AsyncConnection
from pydantic import BaseModel, Field

Scope = Literal["activation", "authentication"]


class TokenModel(BaseModel):
    """Token model."""

    plain_text: str = Field(min_length=26, max_length=26)
    hash: bytes
    user_id: int
    expiry: datetime
    scope: Scope


def create_token(user_id: int, ttl: timedelta, scope: Scope) -> TokenModel:
    """Create a token hashed with sha256.

    Args:
        user_id: The user ID to associate with the token.
        ttl: The time-to-live for the token.
        scope: The scope of the token.

    Returns:
        A token model.
    """
    random_bytes = token_bytes(16)

    # Encode to base32 without padding
    token_plain_text = base64.b32encode(random_bytes).decode().rstrip("=")

    # Hash the token using sha256
    token_hash = hashlib.sha256(token_plain_text.encode("utf-8")).digest()

    return TokenModel(
        plain_text=token_plain_text,
        hash=token_hash,
        user_id=user_id,
        expiry=datetime.now(UTC) + ttl,
        scope=scope,
    )


