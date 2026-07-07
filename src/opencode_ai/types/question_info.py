# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
