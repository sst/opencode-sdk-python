# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .question_info import QuestionInfo
from .question_tool import QuestionTool

__all__ = ["QuestionRequest"]


class QuestionRequest(BaseModel):
    id: str

    questions: List[QuestionInfo]

    session_id: str = FieldInfo(alias="sessionID")

    tool: Optional[QuestionTool] = None
