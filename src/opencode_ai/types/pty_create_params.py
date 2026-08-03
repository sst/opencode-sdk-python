# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

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
