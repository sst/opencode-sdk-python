# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["ExperimentalWorkspaceAdapterListResponse", "WorkspaceAdapter"]


class WorkspaceAdapter(BaseModel):
    type: str

    name: str

    description: str


ExperimentalWorkspaceAdapterListResponse: TypeAlias = List[WorkspaceAdapter]
