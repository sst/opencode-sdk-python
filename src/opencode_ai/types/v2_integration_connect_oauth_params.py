# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["V2IntegrationConnectOauthParams"]


class V2IntegrationConnectOauthParams(TypedDict, total=False):
    method_id: Required[Annotated[str, PropertyInfo(alias="methodID")]]

    inputs: Required[Dict[str, object]]

    label: str
