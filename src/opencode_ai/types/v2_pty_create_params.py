# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import TypedDict

__all__ = ["V2PtyCreateParams"]


class V2PtyCreateParams(TypedDict, total=False):
    command: str

    args: List[str]

    cwd: str

    title: str

    env: Dict[str, object]
