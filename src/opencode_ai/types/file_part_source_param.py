# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .file_source_param import FileSourceParam
from .symbol_source_param import SymbolSourceParam

__all__ = ["FilePartSourceParam"]

FilePartSourceParam: TypeAlias = Union[FileSourceParam, SymbolSourceParam]
