# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .lsp_status import LSPStatus

__all__ = ["LspStatusResponse"]

LspStatusResponse: TypeAlias = List[LSPStatus]
