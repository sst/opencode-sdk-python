# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .file_part_source_text_param import FilePartSourceTextParam

__all__ = ["ResourceSourceParam"]


class ResourceSourceParam(TypedDict, total=False):
    client_name: Required[Annotated[str, PropertyInfo(alias="clientName")]]

    text: Required[FilePartSourceTextParam]

    type: Required[Literal["resource"]]

    uri: Required[str]
