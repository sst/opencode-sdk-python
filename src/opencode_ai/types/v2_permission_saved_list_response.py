# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import List

from .._models import BaseModel

__all__ = ["V2PermissionSavedListResponse"]


class V2PermissionSavedListResponse(BaseModel):
    data: List[object]
