# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .file_part_source_text_param import FilePartSourceTextParam

__all__ = ["FileSourceParam"]


class FileSourceParam(TypedDict, total=False):
    path: Required[str]

    text: Required[FilePartSourceTextParam]

    type: Required[Literal["file"]]
