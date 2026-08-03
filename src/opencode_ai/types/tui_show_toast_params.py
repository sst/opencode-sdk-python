# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TuiShowToastParams"]


class TuiShowToastParams(TypedDict, total=False):
    message: Required[str]

    variant: Required[Literal["info", "success", "warning", "error"]]

    duration: int

    title: str
