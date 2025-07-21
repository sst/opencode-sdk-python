# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .part_param import PartParam

__all__ = ["TuiPromptParams"]


class TuiPromptParams(TypedDict, total=False):
    parts: Required[Iterable[PartParam]]

    text: Required[str]
