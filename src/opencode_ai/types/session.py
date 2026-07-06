# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "Session",
    "SummaryDiff",
    "Summary",
    "TokensCache",
    "Tokens",
    "Model",
    "Time",
    "PermissionRule",
    "Revert",
    "Share",
]


class SummaryDiff(BaseModel):
    additions: float

    deletions: float

    file: Optional[str] = None

    patch: Optional[str] = None

    status: Optional[Literal["added", "deleted", "modified"]] = None


class Summary(BaseModel):
    additions: float

    deletions: float

    files: float

    diffs: Optional[List[SummaryDiff]] = None


class TokensCache(BaseModel):
    read: float

    write: float


class Tokens(BaseModel):
    cache: TokensCache

    input: float

    output: float

    reasoning: float


class Model(BaseModel):
    id: str

    provider_id: str = FieldInfo(alias="providerID")

    variant: Optional[str] = None


class Time(BaseModel):
    created: float

    updated: float

    archived: Optional[float] = None

    compacting: Optional[float] = None


class PermissionRule(BaseModel):
    action: Literal["allow", "deny", "ask"]

    pattern: str

    permission: str


class Revert(BaseModel):
    message_id: str = FieldInfo(alias="messageID")

    diff: Optional[str] = None

    part_id: Optional[str] = FieldInfo(alias="partID", default=None)

    snapshot: Optional[str] = None


class Share(BaseModel):
    url: str


class Session(BaseModel):
    id: str

    directory: str

    project_id: str = FieldInfo(alias="projectID")

    slug: str

    time: Time

    title: str

    version: str

    agent: Optional[str] = None

    cost: Optional[float] = None

    metadata: Optional[object] = None

    model: Optional[Model] = None

    parent_id: Optional[str] = FieldInfo(alias="parentID", default=None)

    path: Optional[str] = None

    permission: Optional[List[PermissionRule]] = None

    revert: Optional[Revert] = None

    share: Optional[Share] = None

    summary: Optional[Summary] = None

    tokens: Optional[Tokens] = None

    workspace_id: Optional[str] = FieldInfo(alias="workspaceID", default=None)
