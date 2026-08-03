# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import Optional

from .._models import BaseModel

__all__ = ["V2EventSubscribeResponse"]


class V2EventSubscribeResponse(BaseModel):
    type: Optional[str] = None
