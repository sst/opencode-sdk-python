# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .mcp_status_failed import MCPStatusFailed
from .mcp_status_disabled import MCPStatusDisabled
from .mcp_status_connected import MCPStatusConnected
from .mcp_status_needs_auth import MCPStatusNeedsAuth
from .mcp_status_needs_client_registration import MCPStatusNeedsClientRegistration

__all__ = ["MCPStatus"]

MCPStatus: TypeAlias = Annotated[
    Union[
        MCPStatusConnected,
        MCPStatusDisabled,
        MCPStatusFailed,
        MCPStatusNeedsAuth,
        MCPStatusNeedsClientRegistration,
    ],
    PropertyInfo(discriminator="status"),
]
