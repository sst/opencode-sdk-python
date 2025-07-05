# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .file_part import FilePart
from .text_part import TextPart

__all__ = ["UserMessagePart"]

UserMessagePart: TypeAlias = Annotated[Union[TextPart, FilePart], PropertyInfo(discriminator="type")]
