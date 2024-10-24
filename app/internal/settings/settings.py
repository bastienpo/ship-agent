"""Configuration of the API."""

from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuration used by the application."""

    model_config = SettingsConfigDict(
        arbitrary_types_allowed=False,
        validate_default=True,
        extra="ignore",
        strict=True,
        frozen=True,
        case_sensitive=False,
    )

    environment: Literal["development", "staging", "production"] = Field(
        default="development", description="The environment."
    )

    granian_port: str = Field(description="The port to use.")

    granian_reload: Literal["True", "False", "true", "false"] = Field(
        description="Whether to reload the application."
    )

    granian_interface: Literal["asgi", "asginl"] = Field(
        description="The interface to use."
    )

    granian_loop: Literal["uvloop", "asyncio"] = Field(
        description="The event loop to use."
    )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Get the configuration."""
    return Settings()
