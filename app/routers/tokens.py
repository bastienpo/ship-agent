"""Users router."""

from datetime import timedelta
from typing import Annotated

from argon2 import PasswordHasher
from argon2.exceptions import VerificationError
from fastapi import APIRouter, Depends, HTTPException, status
from psycopg_pool import AsyncConnectionPool

from app.internal.data.database import get_database_pool
from app.internal.data.tokens import AuthenticationTokenCreate, new_token
from app.internal.data.users import get_user_by_email

router = APIRouter(prefix="/v1", tags=["tokens"])


@router.post(
    "/tokens/authentification",
    status_code=status.HTTP_201_CREATED,
)
async def create_authentication_token_handler(
    payload: AuthenticationTokenCreate,
    pool: Annotated[AsyncConnectionPool, Depends(get_database_pool)],
) -> dict[str, str]:
    """Create an authentication token."""
    async with pool.connection(timeout=3) as conn:
        user = await get_user_by_email(conn, payload.email)

    try:
        PasswordHasher().verify(
            user.password_hash.get_secret_value(),
            payload.password.get_secret_value(),
        )
    except VerificationError as e:
        msg = "Invalid credentials"
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=msg) from e

    async with pool.connection(timeout=3) as conn:
        token = await new_token(
            conn, user_id=user.id, scope="authentication", ttl=timedelta(days=1)
        )

    return {
        "expiry": token.expiry.isoformat(),
        "token": token.plain_text.get_secret_value(),
    }
