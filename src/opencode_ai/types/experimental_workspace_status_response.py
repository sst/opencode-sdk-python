# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import List
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ExperimentalWorkspaceStatusResponse", "WorkspaceEventConnectionStatus"]


class WorkspaceEventConnectionStatus(BaseModel):
    workspace_id: str = FieldInfo(alias="workspaceID")

    status: Literal["connected", "connecting", "disconnected", "error"]


ExperimentalWorkspaceStatusResponse: TypeAlias = List[WorkspaceEventConnectionStatus]
