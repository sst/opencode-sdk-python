# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .file_part_source_param import FilePartSourceParam

__all__ = ["FilePartInputParam"]


class FilePartInputParam(TypedDict, total=False):
    mime: Required[str]

    type: Required[Literal["file"]]

    url: Required[str]

    id: str

    filename: str

    source: FilePartSourceParam
