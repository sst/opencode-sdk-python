# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["QuestionReplyParams"]


class QuestionReplyParams(TypedDict, total=False):
    answers: Required[List[List[str]]]
    """User answers in order of questions (each answer is an array of selected labels)"""
