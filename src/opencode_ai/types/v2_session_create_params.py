# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["V2SessionCreateParams"]


class V2SessionCreateParams(TypedDict, total=False):
    id: str

    agent: str

    model: object

    location: object
