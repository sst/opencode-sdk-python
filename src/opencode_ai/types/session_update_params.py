# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SessionUpdateParams", "Permission", "Time"]


class Permission(TypedDict, total=False):
    action: Required[Literal["allow", "deny", "ask"]]

    pattern: Required[str]

    permission: Required[str]


class Time(TypedDict, total=False):
    archived: float


class SessionUpdateParams(TypedDict, total=False):
    title: str

    metadata: object

    permission: Iterable[Permission]

    time: Time
