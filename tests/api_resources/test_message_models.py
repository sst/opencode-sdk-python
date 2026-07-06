from __future__ import annotations

from typing import cast

from opencode_ai.types import AssistantMessage, FilePartSource, ResourceSource, UserMessage
from opencode_ai._models import construct_type

ASSISTANT_PAYLOAD: dict[str, object] = {
    "id": "msg_1",
    "sessionID": "ses_1",
    "role": "assistant",
    "time": {"created": 1.0, "completed": 2.0},
    "parentID": "msg_0",
    "modelID": "claude-opus-4-8",
    "providerID": "anthropic",
    "mode": "build",
    "agent": "build",
    "path": {"cwd": "/", "root": "/"},
    "cost": 0.0,
    "tokens": {"input": 1.0, "output": 2.0, "reasoning": 0.0, "total": 3.0,
               "cache": {"read": 0.0, "write": 0.0}},
    "variant": "default",
    "finish": "stop",
}

USER_PAYLOAD: dict[str, object] = {
    "id": "msg_2",
    "sessionID": "ses_1",
    "role": "user",
    "time": {"created": 1.0},
    "agent": "build",
    "model": {"providerID": "anthropic", "modelID": "claude-opus-4-8"},
}


def test_assistant_message_parses_current_shape() -> None:
    msg = cast(AssistantMessage, construct_type(type_=AssistantMessage, value=ASSISTANT_PAYLOAD))
    assert msg.agent == "build"
    assert msg.parent_id == "msg_0"
    assert not hasattr(msg, "system")


def test_user_message_parses_current_shape() -> None:
    msg = cast(UserMessage, construct_type(type_=UserMessage, value=USER_PAYLOAD))
    assert msg.agent == "build"
    assert msg.model.provider_id == "anthropic"


def test_file_part_source_resolves_resource_source() -> None:
    payload: dict[str, object] = {
        "type": "resource",
        "clientName": "my-mcp-server",
        "uri": "resource://docs/readme",
        "text": {"start": 0, "end": 10, "value": "hello"},
    }
    source = cast(ResourceSource, construct_type(type_=FilePartSource, value=payload))
    assert isinstance(source, ResourceSource)
    assert source.type == "resource"
    assert source.client_name == "my-mcp-server"
    assert source.uri == "resource://docs/readme"
    assert source.text.value == "hello"


def test_assistant_message_error_resolves_api_error() -> None:
    payload: dict[str, object] = {
        **ASSISTANT_PAYLOAD,
        "error": {"name": "APIError", "data": {"message": "boom", "isRetryable": True}},
    }
    msg = cast(AssistantMessage, construct_type(type_=AssistantMessage, value=payload))
    assert type(msg.error).__name__ == "APIError"
