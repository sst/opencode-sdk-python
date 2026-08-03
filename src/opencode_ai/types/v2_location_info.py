# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["V2LocationInfo", "V2LocationInfoProject"]


class V2LocationInfoProject(BaseModel):
    id: str

    directory: str


class V2LocationInfo(BaseModel):
    directory: str

    project: V2LocationInfoProject

    workspace_id: Optional[str] = FieldInfo(alias="workspaceID", default=None)
