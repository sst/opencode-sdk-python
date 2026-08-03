# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ExperimentalWorkspaceListResponse", "Workspace"]


class Workspace(BaseModel):
    id: str

    type: str

    name: str

    project_id: str = FieldInfo(alias="projectID")

    time_used: float = FieldInfo(alias="timeUsed")

    branch: Optional[str] = None

    directory: Optional[str] = None

    extra: Optional[object] = None


ExperimentalWorkspaceListResponse: TypeAlias = List[Workspace]
