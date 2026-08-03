# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["V2SessionQuestionReplyParams"]


class V2SessionQuestionReplyParams(TypedDict, total=False):
    answers: Required[Iterable[object]]
