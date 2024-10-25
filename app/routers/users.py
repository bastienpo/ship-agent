"""Users router."""

from typing import Any

from fastapi import APIRouter, Request

router = APIRouter(prefix="/v1", tags=["users"])


@router.post("/users")
async def register_users(request: Request) -> dict[str, Any]:
    """Register a user."""
    pool = request.app.async_pool
    async with pool.connection(timeout=3) as conn:
        rows = await conn.execute("SELECT * FROM test")
        rows = await rows.fetchall()

    return {"message": rows}
