# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .session import PermissionRule
from .._models import BaseModel
from .snapshot_file_diff import SnapshotFileDiff

__all__ = [
    "ExperimentalSessionListResponse",
    "GlobalSession",
    "GlobalSessionSummary",
    "GlobalSessionTokensCache",
    "GlobalSessionTokens",
    "GlobalSessionModel",
    "GlobalSessionTime",
    "GlobalSessionRevert",
    "GlobalSessionShare",
    "GlobalSessionProject",
]

class GlobalSessionSummary(BaseModel):
    additions: float

    deletions: float

    files: float

    diffs: Optional[List[SnapshotFileDiff]] = None


class GlobalSessionTokensCache(BaseModel):
    read: float

    write: float


class GlobalSessionTokens(BaseModel):
    cache: GlobalSessionTokensCache

    input: float

    output: float

    reasoning: float


class GlobalSessionModel(BaseModel):
    id: str

    provider_id: str = FieldInfo(alias="providerID")

    variant: Optional[str] = None


class GlobalSessionTime(BaseModel):
    created: float

    updated: float

    compacting: Optional[float] = None

    archived: Optional[float] = None


class GlobalSessionRevert(BaseModel):
    message_id: str = FieldInfo(alias="messageID")

    part_id: Optional[str] = FieldInfo(alias="partID", default=None)

    snapshot: Optional[str] = None

    diff: Optional[str] = None


class GlobalSessionShare(BaseModel):
    url: str


class GlobalSessionProject(BaseModel):
    id: str

    worktree: str

    name: Optional[str] = None


class GlobalSession(BaseModel):
    id: str

    slug: str

    project_id: str = FieldInfo(alias="projectID")

    directory: str

    title: str

    version: str

    time: GlobalSessionTime

    project: Optional[GlobalSessionProject] = None

    workspace_id: Optional[str] = FieldInfo(alias="workspaceID", default=None)

    path: Optional[str] = None

    parent_id: Optional[str] = FieldInfo(alias="parentID", default=None)

    summary: Optional[GlobalSessionSummary] = None

    cost: Optional[float] = None

    tokens: Optional[GlobalSessionTokens] = None

    share: Optional[GlobalSessionShare] = None

    agent: Optional[str] = None

    model: Optional[GlobalSessionModel] = None

    metadata: Optional[object] = None

    permission: Optional[List[PermissionRule]] = None

    revert: Optional[GlobalSessionRevert] = None


ExperimentalSessionListResponse: TypeAlias = List[GlobalSession]
