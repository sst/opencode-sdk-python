# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SourceURLPart"]


class SourceURLPart(BaseModel):
    source_id: str = FieldInfo(alias="sourceId")

    type: Literal["source-url"]

    url: str

    provider_metadata: Optional[Dict[str, object]] = FieldInfo(alias="providerMetadata", default=None)

    title: Optional[str] = None
