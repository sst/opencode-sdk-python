# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["V2SessionMessagesResponse", "V2SessionMessagesResponseCursor"]


class V2SessionMessagesResponseCursor(BaseModel):
    next: Optional[str] = None

    previous: Optional[str] = None


class V2SessionMessagesResponse(BaseModel):
    data: List[object]

    cursor: V2SessionMessagesResponseCursor
