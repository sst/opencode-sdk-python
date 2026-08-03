# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["McpRemoteConfigParam", "OAuth", "OAuthMcpOAuthConfig"]


class OAuthMcpOAuthConfig(TypedDict, total=False):
    callback_port: Annotated[int, PropertyInfo(alias="callbackPort")]

    client_id: Annotated[str, PropertyInfo(alias="clientId")]

    client_secret: Annotated[str, PropertyInfo(alias="clientSecret")]

    redirect_uri: Annotated[str, PropertyInfo(alias="redirectUri")]

    scope: str


OAuth: TypeAlias = Union[OAuthMcpOAuthConfig, Literal[False]]


class McpRemoteConfigParam(TypedDict, total=False):
    type: Required[Literal["remote"]]
    """Type of MCP server connection"""

    url: Required[str]
    """URL of the remote MCP server"""

    enabled: bool
    """Enable or disable the MCP server on startup"""

    headers: Dict[str, str]
    """Headers to send with the request"""

    oauth: OAuth
    """OAuth authentication configuration for the MCP server.

    Set to false to disable OAuth auto-detection.
    """

    timeout: int
    """Timeout for the MCP server connection"""
