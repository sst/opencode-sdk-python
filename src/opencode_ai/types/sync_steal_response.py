# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SyncStealResponse"]


class SyncStealResponse(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")
