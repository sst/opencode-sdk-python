# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import List
from typing_extensions import TypeAlias

from .lsp_status import LSPStatus

__all__ = ["LspStatusResponse"]

LspStatusResponse: TypeAlias = List[LSPStatus]
