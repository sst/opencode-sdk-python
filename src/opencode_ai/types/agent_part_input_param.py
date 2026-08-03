# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AgentPartInputParam", "Source"]


class Source(TypedDict, total=False):
    end: Required[int]

    start: Required[int]

    value: Required[str]


class AgentPartInputParam(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["agent"]]

    id: str

    source: Source
