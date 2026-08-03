# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Required, TypedDict

__all__ = ["V2SessionPermissionCreateParams"]


class V2SessionPermissionCreateParams(TypedDict, total=False):
    id: str

    action: Required[str]

    resources: Required[List[str]]

    save: List[str]

    metadata: Dict[str, object]

    source: object

    agent: str
