# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import List
from typing_extensions import TypeAlias

from .file import File

__all__ = ["FileStatusResponse"]

FileStatusResponse: TypeAlias = List[File]
