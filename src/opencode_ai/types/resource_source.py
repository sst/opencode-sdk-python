# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .file_part_source_text import FilePartSourceText

__all__ = ["ResourceSource"]


class ResourceSource(BaseModel):
    client_name: str = FieldInfo(alias="clientName")

    text: FilePartSourceText

    type: Literal["resource"]

    uri: str
