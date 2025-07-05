# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel
from .assistant_message import AssistantMessage
from .user_message_part import UserMessagePart

__all__ = ["Message", "UserMessage", "UserMessageTime"]


class UserMessageTime(BaseModel):
    created: float


class UserMessage(BaseModel):
    id: str

    parts: List[UserMessagePart]

    role: Literal["user"]

    session_id: str = FieldInfo(alias="sessionID")

    time: UserMessageTime


Message: TypeAlias = Annotated[Union[UserMessage, AssistantMessage], PropertyInfo(discriminator="role")]
