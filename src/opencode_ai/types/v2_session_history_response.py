# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["V2SessionHistoryResponse"]


class V2SessionHistoryResponse(BaseModel):
    data: List[object]

    has_more: bool = FieldInfo(alias="hasMore")
