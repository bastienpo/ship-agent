"""Healthcheck data models."""

from typing import Literal

from pydantic import BaseModel, Field


class SystemInfo(BaseModel):
    """System information."""

    version: str = Field(description="The version of the system.")
    environment: Literal["development", "staging", "production"] = Field(
        description="The environment the system is running in."
    )


class Healthcheck(BaseModel):
    """Healthcheck response."""

    status: Literal["available", "unavailable", "error"] = Field(
        description="The status of the healthcheck."
    )
    system_info: SystemInfo = Field(description="The system information.")
