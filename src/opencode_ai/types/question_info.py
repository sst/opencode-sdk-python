# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import List, Optional

from .._models import BaseModel
from .question_option import QuestionOption

__all__ = ["QuestionInfo"]


class QuestionInfo(BaseModel):
    header: str

    options: List[QuestionOption]

    question: str

    custom: Optional[bool] = None

    multiple: Optional[bool] = None
