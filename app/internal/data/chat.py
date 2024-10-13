"""Chat data models."""

from typing import Literal

from pydantic import Field

from app.internal.data import BaseDataModel


class Function(BaseDataModel):
    """A function to call."""

    name: str = Field(description="The name of the function.")
    arguments: str = Field(description="A stringified JSON object with the arguments.")


class ToolCall(BaseDataModel):
    """A tool call in a message."""

    id: str = Field(description="The ID of the tool call.")
    type: Literal["function"] = Field(description="The type of the tool call.")
    function: Function = Field(description="The function to call.")


class Message(BaseDataModel):
    """A message in the chat."""

    role: Literal["user", "assistant", "system"] = Field(
        description="The role of the message."
    )
    content: str = Field(description="The content of the message.")
    tool_calls: list[ToolCall] = Field(
        description="The tool calls made in this message."
    )


class ChatInput(BaseDataModel):
    """Chat input."""

    model: Literal["gpt-4o", "claude-3-5-sonnet-20240620"] = Field(
        description="The model to use for the chat."
    )
    messages: list[Message] = Field(description="The messages to send to the chat.")


class Chat(BaseDataModel):
    """Chat output."""

    message: str = Field(description="The message from the chat.")


class Choice(BaseDataModel):
    """A choice in the chat."""

    index: int = Field(description="The index of the choice.")
    message: Message = Field(description="The message from the choice.")
    logprobs: float | None = Field(description="The log probabilities of the message.")
    finish_reason: str = Field(description="The reason the message finished.")


class CompletionTokensDetails(BaseDataModel):
    """Completion tokens details."""

    reasoning_tokens: int = Field(description="The number of reasoning tokens.")


class Usage(BaseDataModel):
    """Usage details."""

    prompt_tokens: int = Field(description="The number of prompt tokens.")
    completion_tokens: int = Field(description="The number of completion tokens.")
    total_tokens: int = Field(description="The total number of tokens.")
    completion_tokens_details: CompletionTokensDetails = Field(
        description="The details of the completion tokens."
    )


class Model(BaseDataModel):
    """A model response."""

    id: str = Field(description="The ID of the model.")
    object: str = Field(description="The object of the model.")
    created: int = Field(description="The creation timestamp of the model.")
    model: str = Field(description="The model name.")
    system_fingerprint: str = Field(description="The system fingerprint of the model.")
    choices: list[Choice] = Field(description="The choices from the model.")
    usage: Usage = Field(description="The usage details of the model.")
