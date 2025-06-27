# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SourceURLPartParam"]


class SourceURLPartParam(TypedDict, total=False):
    source_id: Required[Annotated[str, PropertyInfo(alias="sourceId")]]

    type: Required[Literal["source-url"]]

    url: Required[str]

    provider_metadata: Annotated[Dict[str, object], PropertyInfo(alias="providerMetadata")]

    title: str
