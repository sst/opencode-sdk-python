# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["McpRemote"]


class McpRemote(BaseModel):
    type: Literal["remote"]
    """Type of MCP server connection"""

    url: str
    """URL of the remote MCP server"""

    enabled: Optional[bool] = None
    """Enable or disable the MCP server on startup"""
