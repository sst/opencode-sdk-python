# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import List

from .._models import BaseModel

__all__ = ["V2SessionPermissionListResponse"]


class V2SessionPermissionListResponse(BaseModel):
    data: List[object]
