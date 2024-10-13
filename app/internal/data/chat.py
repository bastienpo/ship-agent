"""Chat data models."""

from pydantic import BaseModel, Field


class ChatInput(BaseModel):
    """Chat input."""

    message: str = Field(description="The message to send to the chat.")


class Chat(BaseModel):
    """Chat output."""

    message: str = Field(description="The message from the chat.")
