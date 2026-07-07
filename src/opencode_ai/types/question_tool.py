# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["QuestionTool"]


class QuestionTool(BaseModel):
    call_id: str = FieldInfo(alias="callID")

    message_id: str = FieldInfo(alias="messageID")
