# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .file_source import FileSource
from .symbol_source import SymbolSource

__all__ = ["FilePartSource"]

FilePartSource: TypeAlias = Annotated[Union[FileSource, SymbolSource], PropertyInfo(discriminator="type")]
