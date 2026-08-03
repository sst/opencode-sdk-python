# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.
#
# NOTE: `part.update`'s request body IS the full `Part` discriminated union (a
# read-modify-write replacement of the part, not a partial patch), so this
# module mirrors `types/part.py`'s variants one-for-one as TypedDicts (suffixed
# `Param`) rather than flattening the union into method kwargs.

from __future__ import annotations

from typing import Dict, List, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared.api_error import APIError
from .file_part_source_param import FilePartSourceParam

__all__ = [
    "SessionUpdatePartParams",
    "TextPartParam",
    "TextPartParamTime",
    "SubtaskPartParam",
    "SubtaskPartParamModel",
    "ReasoningPartParam",
    "ReasoningPartParamTime",
    "FilePartParam",
    "ToolPartParam",
    "ToolPartParamState",
    "ToolPartParamStatePending",
    "ToolPartParamStateRunning",
    "ToolPartParamStateRunningTime",
    "ToolPartParamStateCompleted",
    "ToolPartParamStateCompletedTime",
    "ToolPartParamStateError",
    "ToolPartParamStateErrorTime",
    "StepStartPartParam",
    "StepFinishPartParam",
    "StepFinishPartParamTokens",
    "StepFinishPartParamTokensCache",
    "SnapshotPartParam",
    "PatchPartParam",
    "AgentPartParam",
    "AgentPartParamSource",
    "RetryPartParam",
    "RetryPartParamTime",
    "CompactionPartParam",
]


class TextPartParamTime(TypedDict, total=False):
    start: Required[int]

    end: int


class TextPartParam(TypedDict, total=False):
    id: Required[str]

    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    text: Required[str]

    type: Required[Literal["text"]]

    ignored: bool

    metadata: object

    synthetic: bool

    time: TextPartParamTime


class SubtaskPartParamModel(TypedDict, total=False):
    model_id: Required[Annotated[str, PropertyInfo(alias="modelID")]]

    provider_id: Required[Annotated[str, PropertyInfo(alias="providerID")]]


class SubtaskPartParam(TypedDict, total=False):
    id: Required[str]

    agent: Required[str]

    description: Required[str]

    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    prompt: Required[str]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    type: Required[Literal["subtask"]]

    command: str

    model: SubtaskPartParamModel


class ReasoningPartParamTime(TypedDict, total=False):
    start: Required[int]

    end: int


class ReasoningPartParam(TypedDict, total=False):
    id: Required[str]

    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    text: Required[str]

    time: Required[ReasoningPartParamTime]

    type: Required[Literal["reasoning"]]

    metadata: object


class FilePartParam(TypedDict, total=False):
    id: Required[str]

    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    mime: Required[str]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    type: Required[Literal["file"]]

    url: Required[str]

    filename: str

    source: FilePartSourceParam


class ToolPartParamStatePending(TypedDict, total=False):
    status: Required[Literal["pending"]]


class ToolPartParamStateRunningTime(TypedDict, total=False):
    start: Required[float]


class ToolPartParamStateRunning(TypedDict, total=False):
    status: Required[Literal["running"]]

    time: Required[ToolPartParamStateRunningTime]

    input: object

    metadata: Dict[str, object]

    title: str


class ToolPartParamStateCompletedTime(TypedDict, total=False):
    end: Required[float]

    start: Required[float]


class ToolPartParamStateCompleted(TypedDict, total=False):
    input: Required[Dict[str, object]]

    metadata: Required[Dict[str, object]]

    output: Required[str]

    status: Required[Literal["completed"]]

    time: Required[ToolPartParamStateCompletedTime]

    title: Required[str]


class ToolPartParamStateErrorTime(TypedDict, total=False):
    end: Required[float]

    start: Required[float]


class ToolPartParamStateError(TypedDict, total=False):
    error: Required[str]

    input: Required[Dict[str, object]]

    status: Required[Literal["error"]]

    time: Required[ToolPartParamStateErrorTime]


ToolPartParamState: TypeAlias = Union[
    ToolPartParamStatePending, ToolPartParamStateRunning, ToolPartParamStateCompleted, ToolPartParamStateError
]


class ToolPartParam(TypedDict, total=False):
    id: Required[str]

    call_id: Required[Annotated[str, PropertyInfo(alias="callID")]]

    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    state: Required[ToolPartParamState]

    tool: Required[str]

    type: Required[Literal["tool"]]

    metadata: object


class StepStartPartParam(TypedDict, total=False):
    id: Required[str]

    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    type: Required[Literal["step-start"]]

    snapshot: str


class StepFinishPartParamTokensCache(TypedDict, total=False):
    read: Required[float]

    write: Required[float]


class StepFinishPartParamTokens(TypedDict, total=False):
    cache: Required[StepFinishPartParamTokensCache]

    input: Required[float]

    output: Required[float]

    reasoning: Required[float]

    total: float


class StepFinishPartParam(TypedDict, total=False):
    id: Required[str]

    cost: Required[float]

    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    reason: Required[str]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    tokens: Required[StepFinishPartParamTokens]

    type: Required[Literal["step-finish"]]

    snapshot: str


class SnapshotPartParam(TypedDict, total=False):
    id: Required[str]

    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    snapshot: Required[str]

    type: Required[Literal["snapshot"]]


class PatchPartParam(TypedDict, total=False):
    id: Required[str]

    files: Required[List[str]]

    hash: Required[str]

    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    type: Required[Literal["patch"]]


class AgentPartParamSource(TypedDict, total=False):
    end: Required[int]

    start: Required[int]

    value: Required[str]


class AgentPartParam(TypedDict, total=False):
    id: Required[str]

    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    name: Required[str]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    type: Required[Literal["agent"]]

    source: AgentPartParamSource


class RetryPartParamTime(TypedDict, total=False):
    created: Required[int]


class RetryPartParam(TypedDict, total=False):
    id: Required[str]

    attempt: Required[int]

    error: Required[APIError]

    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    time: Required[RetryPartParamTime]

    type: Required[Literal["retry"]]


class CompactionPartParam(TypedDict, total=False):
    id: Required[str]

    auto: Required[bool]

    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    type: Required[Literal["compaction"]]

    overflow: bool

    # Spec inconsistency: this field's wire name is literally `tail_start_id`
    # (snake_case), not the camelCase `tailStartID` used by sibling ID fields --
    # see `CompactionPart.tail_start_id` in `types/part.py` for the same quirk.
    tail_start_id: str


SessionUpdatePartParams: TypeAlias = Union[
    TextPartParam,
    SubtaskPartParam,
    ReasoningPartParam,
    FilePartParam,
    ToolPartParam,
    StepStartPartParam,
    StepFinishPartParam,
    SnapshotPartParam,
    PatchPartParam,
    AgentPartParam,
    RetryPartParam,
    CompactionPartParam,
]
