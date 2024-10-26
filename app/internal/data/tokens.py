"""Token models for activation and authentication."""

import base64
import hashlib
from datetime import UTC, datetime, timedelta
from secrets import token_bytes
from typing import Literal

from psycopg import AsyncConnection
from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    SecretBytes,
    SecretStr,
    model_serializer,
)

Scope = Literal["activation", "authentication"]


class AuthenticationTokenCreate(BaseModel):
    """Authentication token create model."""

    email: EmailStr = Field(max_length=256)
    password: SecretStr = Field(min_length=8, max_length=256)


class TokenModel(BaseModel):
    """Token model."""

    plain_text: SecretStr = Field(min_length=26, max_length=26)
    hash: SecretBytes
    user_id: int
    expiry: datetime
    scope: Scope

    @model_serializer
    def serialize_without_plain_text(
        self: "TokenModel",
    ) -> dict[str, str | bytes | datetime | Scope]:
        """Serialize the model to a dictionary without the plain text."""
        return {
            "hash": self.hash.get_secret_value(),
            "user_id": self.user_id,
            "expiry": self.expiry,
            "scope": self.scope,
        }


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
        plain_text=SecretStr(token_plain_text),
        hash=SecretBytes(token_hash),
        user_id=user_id,
        expiry=datetime.now(UTC) + ttl,
        scope=scope,
    )


async def insert_token(conn: AsyncConnection, token: TokenModel) -> None:
    """CRUD operation: Insert a token into the database.

    Args:
        conn: The database connection.
        token: The token model.
    """
    query = """
    INSERT INTO tokens (hash, user_id, expiry, scope)
    VALUES (%(hash)s, %(user_id)s, %(expiry)s, %(scope)s)
    """

    await conn.execute(query, token.model_dump())


async def new_token(
    conn: AsyncConnection, user_id: int, ttl: timedelta, scope: Scope
) -> TokenModel:
    """Create a new token and insert it into the database.

    Generate a new token, insert it into the database, and return the token.

    Args:
        conn: The database connection.
        user_id: The user ID to associate with the token.
        ttl: The time-to-live for the token.
        scope: The scope of the token.

    Returns:
        A token model.
    """
    token = create_token(user_id, ttl, scope)
    await insert_token(conn, token)

    return token


async def delete_all_for_user(
    conn: AsyncConnection, user_id: int, scope: Scope
) -> None:
    """CRUD operation: Delete all tokens for a user.

    Args:
        conn: The database connection.
        user_id: The user ID to delete tokens for.
        scope: The scope of the tokens to delete.
    """
    query = """
    DELETE FROM tokens WHERE scope = %(scope)s AND user_id = %(user_id)s
    """

    await conn.execute(query, {"scope": scope, "user_id": user_id})
