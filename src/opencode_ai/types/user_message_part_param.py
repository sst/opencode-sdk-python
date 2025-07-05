# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .file_part_param import FilePartParam
from .text_part_param import TextPartParam

__all__ = ["UserMessagePartParam"]

UserMessagePartParam: TypeAlias = Union[TextPartParam, FilePartParam]
