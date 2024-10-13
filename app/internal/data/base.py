"""Base data models."""

from pydantic import BaseModel, ConfigDict


class BaseDataModel(BaseModel):
    """Base data model."""

    model_config = ConfigDict(
        arbitrary_types_allowed=False,
        extra="allow",
        strict=True,
        frozen=True,
        validate_assignment=True,
    )
