# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import TypedDict

__all__ = ["PtyCreateParams"]


class PtyCreateParams(TypedDict, total=False):
    args: List[str]

    command: str

    cwd: str

    env: Dict[str, str]

    title: str
