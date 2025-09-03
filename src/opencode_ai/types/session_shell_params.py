# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SessionShellParams"]


class SessionShellParams(TypedDict, total=False):
    agent: Required[str]

    command: Required[str]

    directory: str
