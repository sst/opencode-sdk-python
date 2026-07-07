# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["McpRemoteConfig", "OAuth", "OAuthMcpOAuthConfig"]


class OAuthMcpOAuthConfig(BaseModel):
    callback_port: Optional[int] = FieldInfo(alias="callbackPort", default=None)

    client_id: Optional[str] = FieldInfo(alias="clientId", default=None)

    client_secret: Optional[str] = FieldInfo(alias="clientSecret", default=None)

    redirect_uri: Optional[str] = FieldInfo(alias="redirectUri", default=None)

    scope: Optional[str] = None


OAuth = Union[OAuthMcpOAuthConfig, Literal[False]]


class McpRemoteConfig(BaseModel):
    type: Literal["remote"]
    """Type of MCP server connection"""

    url: str
    """URL of the remote MCP server"""

    enabled: Optional[bool] = None
    """Enable or disable the MCP server on startup"""

    headers: Optional[Dict[str, str]] = None
    """Headers to send with the request"""

    oauth: Optional[OAuth] = None
    """OAuth authentication configuration for the MCP server.

    Set to false to disable OAuth auto-detection.
    """

    timeout: Optional[int] = None
    """Timeout for the MCP server connection"""
