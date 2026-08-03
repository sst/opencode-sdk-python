# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VcsDiffParams"]


class VcsDiffParams(TypedDict, total=False):
    mode: Required[Literal["git", "branch"]]

    context: int

    directory: str

    workspace: str
