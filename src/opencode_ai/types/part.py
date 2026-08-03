# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.
#
# NOTE: This module is produced by `scripts/gen_union_models.py --union Part
# --unknown-fallback PartUnknown` (see that script for the generator design).
# Regenerate with:
#   ./.venv/Scripts/python.exe scripts/gen_union_models.py --union Part --unknown-fallback PartUnknown
# then re-run `scripts/format` / `ruff format` on the output.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel
from .file_part_source import FilePartSource
from .shared.api_error import APIError
from .tool_state_error import ToolStateError
from .tool_state_pending import ToolStatePending
from .tool_state_running import ToolStateRunning
from .tool_state_completed import ToolStateCompleted

__all__ = [
    "Part",
    "PartUnknown",
    "TextPartTime",
    "TextPart",
    "SubtaskPartModel",
    "SubtaskPart",
    "ReasoningPartTime",
    "ReasoningPart",
    "FilePart",
    "ToolPartState",
    "ToolPart",
    "StepStartPart",
    "StepFinishPartTokensCache",
    "StepFinishPartTokens",
    "StepFinishPart",
    "SnapshotPart",
    "PatchPart",
    "AgentPartSource",
    "AgentPart",
    "RetryPartTime",
    "RetryPart",
    "CompactionPart",
]


class TextPartTime(BaseModel):
    start: int

    end: Optional[int] = None


class TextPart(BaseModel):
    id: str

    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")

    text: str

    type: Literal["text"]

    ignored: Optional[bool] = None

    metadata: Optional[object] = None

    synthetic: Optional[bool] = None

    time: Optional[TextPartTime] = None


class SubtaskPartModel(BaseModel):
    model_id: str = FieldInfo(alias="modelID")

    provider_id: str = FieldInfo(alias="providerID")


class SubtaskPart(BaseModel):
    id: str

    agent: str

    description: str

    message_id: str = FieldInfo(alias="messageID")

    prompt: str

    session_id: str = FieldInfo(alias="sessionID")

    type: Literal["subtask"]

    command: Optional[str] = None

    model: Optional[SubtaskPartModel] = None


class ReasoningPartTime(BaseModel):
    start: int

    end: Optional[int] = None


class ReasoningPart(BaseModel):
    id: str

    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")

    text: str

    time: ReasoningPartTime

    type: Literal["reasoning"]

    metadata: Optional[object] = None


class FilePart(BaseModel):
    id: str

    message_id: str = FieldInfo(alias="messageID")

    mime: str

    session_id: str = FieldInfo(alias="sessionID")

    type: Literal["file"]

    url: str

    filename: Optional[str] = None

    source: Optional[FilePartSource] = None


ToolPartState: TypeAlias = Annotated[
    Union[ToolStatePending, ToolStateRunning, ToolStateCompleted, ToolStateError], PropertyInfo(discriminator="status")
]


class ToolPart(BaseModel):
    id: str

    call_id: str = FieldInfo(alias="callID")

    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")

    state: ToolPartState

    tool: str

    type: Literal["tool"]

    metadata: Optional[object] = None


class StepStartPart(BaseModel):
    id: str

    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")

    type: Literal["step-start"]

    snapshot: Optional[str] = None


class StepFinishPartTokensCache(BaseModel):
    read: float

    write: float


class StepFinishPartTokens(BaseModel):
    cache: StepFinishPartTokensCache

    input: float

    output: float

    reasoning: float

    total: Optional[float] = None


class StepFinishPart(BaseModel):
    id: str

    cost: float

    message_id: str = FieldInfo(alias="messageID")

    reason: str

    session_id: str = FieldInfo(alias="sessionID")

    tokens: StepFinishPartTokens

    type: Literal["step-finish"]

    snapshot: Optional[str] = None


class SnapshotPart(BaseModel):
    id: str

    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")

    snapshot: str

    type: Literal["snapshot"]


class PatchPart(BaseModel):
    id: str

    files: List[str]

    hash: str

    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")

    type: Literal["patch"]


class AgentPartSource(BaseModel):
    end: int

    start: int

    value: str


class AgentPart(BaseModel):
    id: str

    message_id: str = FieldInfo(alias="messageID")

    name: str

    session_id: str = FieldInfo(alias="sessionID")

    type: Literal["agent"]

    source: Optional[AgentPartSource] = None


class RetryPartTime(BaseModel):
    created: int


class RetryPart(BaseModel):
    id: str

    attempt: int

    error: APIError

    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")

    time: RetryPartTime

    type: Literal["retry"]


class CompactionPart(BaseModel):
    id: str

    auto: bool

    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")

    type: Literal["compaction"]

    overflow: Optional[bool] = None

    tail_start_id: Optional[str] = None


class PartUnknown(BaseModel):
    """Permissive fallback for `Part` `type` values not yet enumerated by this SDK.

    The server's part union may grow beyond the variants modeled here. Rather
    than raising when an unrecognized `type` is encountered, unmatched parts
    deserialize into this open-ended model so message/session responses keep
    working as the server adds new part kinds. See `EventUnknown` in
    `event_list_response.py` for the sibling pattern and the ordering rationale
    reproduced below.
    """

    type: str


# Note on ordering: `PartUnknown` is intentionally listed *first*, not last.
#
# `_models.construct_type()` (the non-strict path used by default response
# parsing) resolves a `PropertyInfo(discriminator=...)` union in two steps:
#   1. If the discriminator value is present in the precomputed
#      `{literal value: variant type}` mapping, that exact variant is
#      constructed directly -- this happens regardless of the union's
#      ordering, so every known `type` literal below is still matched
#      correctly no matter where `PartUnknown` sits.
#   2. Otherwise (unknown/unmapped discriminator value) it falls back to
#      `for variant in args: try construct_type(...) except: continue` and
#      returns the *first* variant that doesn't raise. Because `BaseModel`
#      variants are built via the SDK's overridden `.construct()`, which
#      never validates and therefore never raises, this loop always "succeeds"
#      on the first variant tried -- so whichever variant is listed first
#      is what unknown parts actually resolve to.
#
# `PartUnknown`'s own `type` field is a plain `str` (not a `Literal`), so it is
# never added to the discriminator mapping itself -- it only ever gets reached
# through the unmatched-value fallback path above, and being first guarantees
# it -- rather than an arbitrary known variant -- is what's chosen.
Part: TypeAlias = Annotated[
    Union[
        PartUnknown,
        TextPart,
        SubtaskPart,
        ReasoningPart,
        FilePart,
        ToolPart,
        StepStartPart,
        StepFinishPart,
        SnapshotPart,
        PatchPart,
        AgentPart,
        RetryPart,
        CompactionPart,
    ],
    PropertyInfo(discriminator="type"),
]
