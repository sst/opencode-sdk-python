# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

from .mcp_local_config_param import McpLocalConfigParam
from .mcp_remote_config_param import McpRemoteConfigParam

__all__ = ["McpAddParams"]


class McpAddParams(TypedDict, total=False):
    name: Required[str]

    config: Required[Union[McpLocalConfigParam, McpRemoteConfigParam]]
