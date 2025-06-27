# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ReasoningPart"]


class ReasoningPart(BaseModel):
    text: str

    type: Literal["reasoning"]

    provider_metadata: Optional[Dict[str, object]] = FieldInfo(alias="providerMetadata", default=None)
