# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["V2LocationGetResponse"]


class V2LocationGetResponse(BaseModel):
    directory: str

    workspace_id: Optional[str] = FieldInfo(alias="workspaceID", default=None)

    project: object
