# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VcsApplyParams"]


class VcsApplyParams(TypedDict, total=False):
    patch: Required[str]

    directory: str

    workspace: str
