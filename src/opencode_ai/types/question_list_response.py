# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import List
from typing_extensions import TypeAlias

from .question_request import QuestionRequest

__all__ = ["QuestionListResponse"]

QuestionListResponse: TypeAlias = List[QuestionRequest]
