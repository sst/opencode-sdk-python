# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["V2SessionPromptParams"]


class V2SessionPromptParams(TypedDict, total=False):
    id: str

    prompt: Required[object]

    delivery: Literal["steer", "queue"]

    resume: bool
