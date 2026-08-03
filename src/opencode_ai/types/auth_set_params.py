# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.
#
# NOTE: `auth.set`'s request body IS the full `Auth` discriminated union (OAuth,
# API key, or well-known auth), not a wrapper object -- this module mirrors the
# `Auth` union's variants one-for-one as TypedDicts.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["AuthSetParams", "OAuthParam", "ApiAuthParam", "WellKnownAuthParam"]


class OAuthParam(TypedDict, total=False):
    access: Required[str]

    expires: Required[int]

    refresh: Required[str]

    type: Required[Literal["oauth"]]

    account_id: Annotated[str, PropertyInfo(alias="accountId")]

    enterprise_url: Annotated[str, PropertyInfo(alias="enterpriseUrl")]


class ApiAuthParam(TypedDict, total=False):
    key: Required[str]

    type: Required[Literal["api"]]

    metadata: Dict[str, str]


class WellKnownAuthParam(TypedDict, total=False):
    key: Required[str]

    token: Required[str]

    type: Required[Literal["wellknown"]]


AuthSetParams: TypeAlias = Union[OAuthParam, ApiAuthParam, WellKnownAuthParam]
