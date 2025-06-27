# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ReasoningPartParam"]


class ReasoningPartParam(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["reasoning"]]

    provider_metadata: Annotated[Dict[str, object], PropertyInfo(alias="providerMetadata")]
