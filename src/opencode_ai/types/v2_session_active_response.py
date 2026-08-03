# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import Dict

from .._models import BaseModel

__all__ = ["V2SessionActiveResponse"]


class V2SessionActiveResponse(BaseModel):
    data: Dict[str, object]
