from typing import Any, Dict

from opencode_ai.types import Part
from opencode_ai._models import construct_type
from opencode_ai.types.part import (
    TextPart,
    ToolPart,
    AgentPart,
    PartUnknown,
    SubtaskPart,
    CompactionPart,
)

BASE: Dict[str, Any] = {"id": "prt_1", "sessionID": "ses_1", "messageID": "msg_1"}


def test_text_part_resolves() -> None:
    payload = {**BASE, "type": "text", "text": "hello"}
    part = construct_type(type_=Part, value=payload)
    assert isinstance(part, TextPart)
    assert part.text == "hello"


def test_tool_part_resolves() -> None:
    payload: Dict[str, Any] = {
        **BASE,
        "type": "tool",
        "callID": "call_1",
        "tool": "bash",
        "state": {"status": "pending", "input": {}, "raw": ""},
    }
    part = construct_type(type_=Part, value=payload)
    assert isinstance(part, ToolPart)
    assert part.call_id == "call_1"
    assert type(part.state).__name__ == "ToolStatePending"


def test_subtask_part_resolves() -> None:
    payload = {
        **BASE,
        "type": "subtask",
        "prompt": "do the thing",
        "description": "a subtask",
        "agent": "build",
    }
    part = construct_type(type_=Part, value=payload)
    assert isinstance(part, SubtaskPart)
    assert part.agent == "build"


def test_agent_part_resolves() -> None:
    payload = {**BASE, "type": "agent", "name": "build"}
    part = construct_type(type_=Part, value=payload)
    assert isinstance(part, AgentPart)
    assert part.name == "build"


def test_compaction_part_resolves() -> None:
    payload = {**BASE, "type": "compaction", "auto": True}
    part = construct_type(type_=Part, value=payload)
    assert isinstance(part, CompactionPart)
    assert part.auto is True


def test_unknown_part_type_does_not_raise() -> None:
    payload = {**BASE, "type": "some.future.part.kind", "whatever": 1}
    part = construct_type(type_=Part, value=payload)
    assert isinstance(part, PartUnknown)
    assert part.type == "some.future.part.kind"
