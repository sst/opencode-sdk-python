# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import Dict
from typing_extensions import TypeAlias

from .mcp_status import MCPStatus

__all__ = ["McpAddResponse"]

McpAddResponse: TypeAlias = Dict[str, MCPStatus]
