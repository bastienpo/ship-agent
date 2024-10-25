"""Users router."""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from psycopg.errors import UniqueViolation
from psycopg_pool import AsyncConnectionPool

from app.internal.data.database import get_database_pool
from app.internal.data.users import UserCreate, insert_user

router = APIRouter(prefix="/v1", tags=["users"])


@router.post(
    "/users",
    status_code=status.HTTP_201_CREATED,
)
async def register_user_handler(
    payload: UserCreate,
    pool: Annotated[AsyncConnectionPool, Depends(get_database_pool)],
) -> dict[str, str]:
    """Register a user."""
    async with pool.connection(timeout=3) as conn:
        try:
            await insert_user(conn, payload)
        except UniqueViolation as e:
            msg = "User already exists"
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=msg) from e

    return {"message": "User registered"}
