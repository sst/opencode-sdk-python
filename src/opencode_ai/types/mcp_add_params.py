# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

from .mcp_local_config_param import McpLocalConfigParam
from .mcp_remote_config_param import McpRemoteConfigParam

__all__ = ["McpAddParams"]


class McpAddParams(TypedDict, total=False):
    name: Required[str]

    config: Required[Union[McpLocalConfigParam, McpRemoteConfigParam]]
