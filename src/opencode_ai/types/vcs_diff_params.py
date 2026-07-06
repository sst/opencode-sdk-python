# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VcsDiffParams"]


class VcsDiffParams(TypedDict, total=False):
    mode: Required[Literal["git", "branch"]]

    context: int
