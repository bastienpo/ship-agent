"""Database utilities."""

from functools import lru_cache

from psycopg_pool import AsyncConnectionPool

from app.internal.settings import get_settings


@lru_cache(maxsize=1)
def get_database_pool() -> AsyncConnectionPool:
    """Create a new database pool."""
    settings = get_settings()
    dsn = settings.get_dsn()

    return AsyncConnectionPool(conninfo=dsn, open=False, max_size=50, max_idle=50)
