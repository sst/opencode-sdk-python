# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .user_message import UserMessage
from .assistant_message import AssistantMessage

__all__ = ["Message"]

Message: TypeAlias = Annotated[Union[UserMessage, AssistantMessage], PropertyInfo(discriminator="role")]
