from opencode_ai.types import AssistantMessage, UserMessage
from opencode_ai._models import construct_type

ASSISTANT_PAYLOAD = {
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

USER_PAYLOAD = {
    "id": "msg_2",
    "sessionID": "ses_1",
    "role": "user",
    "time": {"created": 1.0},
    "agent": "build",
    "model": {"providerID": "anthropic", "modelID": "claude-opus-4-8"},
}


def test_assistant_message_parses_current_shape() -> None:
    msg = construct_type(type_=AssistantMessage, value=ASSISTANT_PAYLOAD)
    assert msg.agent == "build"
    assert msg.parent_id == "msg_0"
    assert not hasattr(msg, "system")


def test_user_message_parses_current_shape() -> None:
    msg = construct_type(type_=UserMessage, value=USER_PAYLOAD)
    assert msg.agent == "build"
    assert msg.model.provider_id == "anthropic"


def test_assistant_message_error_resolves_api_error() -> None:
    payload = {**ASSISTANT_PAYLOAD, "error": {"name": "APIError", "data": {}}}
    msg = construct_type(type_=AssistantMessage, value=payload)
    assert type(msg.error).__name__ == "APIError"
