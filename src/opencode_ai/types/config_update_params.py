# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "ConfigUpdateParams",
    "Agent",
    "AgentItem",
    "Experimental",
    "ExperimentalHook",
    "ExperimentalHookFileEdited",
    "ExperimentalHookSessionCompleted",
    "Keybinds",
    "Mcp",
    "McpLocal",
    "McpRemote",
    "McpRemoteOAuth",
    "McpRemoteOAuthMcpOAuthConfig",
    "Mode",
    "ModeItem",
    "Provider",
    "ProviderItem",
    "ProviderModels",
    "ProviderModelsCost",
    "ProviderModelsLimit",
    "ProviderOptions",
]


class AgentItem(TypedDict, total=False):
    description: Required[str]

    disable: bool

    model: str

    prompt: str

    temperature: float

    tools: Dict[str, bool]


Agent: TypeAlias = Dict[str, AgentItem]


class ExperimentalHookFileEdited(TypedDict, total=False):
    command: Required[List[str]]

    environment: Dict[str, str]


class ExperimentalHookSessionCompleted(TypedDict, total=False):
    command: Required[List[str]]

    environment: Dict[str, str]


class ExperimentalHook(TypedDict, total=False):
    file_edited: Dict[str, List[ExperimentalHookFileEdited]]

    session_completed: List[ExperimentalHookSessionCompleted]


class Experimental(TypedDict, total=False):
    hook: ExperimentalHook


class Keybinds(TypedDict, total=False):
    app_exit: Required[str]
    """Exit the application"""

    app_help: Required[str]
    """Show help dialog"""

    editor_open: Required[str]
    """Open external editor"""

    file_close: Required[str]
    """Close file"""

    file_diff_toggle: Required[str]
    """Split/unified diff"""

    file_list: Required[str]
    """List files"""

    file_search: Required[str]
    """Search file"""

    input_clear: Required[str]
    """Clear input field"""

    input_newline: Required[str]
    """Insert newline in input"""

    input_paste: Required[str]
    """Paste from clipboard"""

    input_submit: Required[str]
    """Submit input"""

    leader: Required[str]
    """Leader key for keybind combinations"""

    messages_copy: Required[str]
    """Copy message"""

    messages_first: Required[str]
    """Navigate to first message"""

    messages_half_page_down: Required[str]
    """Scroll messages down by half page"""

    messages_half_page_up: Required[str]
    """Scroll messages up by half page"""

    messages_last: Required[str]
    """Navigate to last message"""

    messages_layout_toggle: Required[str]
    """Toggle layout"""

    messages_next: Required[str]
    """Navigate to next message"""

    messages_page_down: Required[str]
    """Scroll messages down by one page"""

    messages_page_up: Required[str]
    """Scroll messages up by one page"""

    messages_previous: Required[str]
    """Navigate to previous message"""

    messages_redo: Required[str]
    """Redo message"""

    messages_revert: Required[str]
    """@deprecated use messages_undo. Revert message"""

    messages_undo: Required[str]
    """Undo message"""

    model_list: Required[str]
    """List available models"""

    project_init: Required[str]
    """Create/update AGENTS.md"""

    session_compact: Required[str]
    """Compact the session"""

    session_export: Required[str]
    """Export session to editor"""

    session_interrupt: Required[str]
    """Interrupt current session"""

    session_list: Required[str]
    """List all sessions"""

    session_new: Required[str]
    """Create a new session"""

    session_share: Required[str]
    """Share current session"""

    session_unshare: Required[str]
    """Unshare current session"""

    switch_mode: Required[str]
    """Next mode"""

    switch_mode_reverse: Required[str]
    """Previous Mode"""

    theme_list: Required[str]
    """List available themes"""

    tool_details: Required[str]
    """Toggle tool details"""


class McpLocal(TypedDict, total=False):
    command: Required[List[str]]
    """Command and arguments to run the MCP server"""

    type: Required[Literal["local"]]
    """Type of MCP server connection"""

    enabled: bool
    """Enable or disable the MCP server on startup"""

    environment: Dict[str, str]
    """Environment variables to set when running the MCP server"""

    timeout: int
    """Timeout for the MCP server connection"""


class McpRemoteOAuthMcpOAuthConfig(TypedDict, total=False):
    callback_port: Annotated[int, PropertyInfo(alias="callbackPort")]

    client_id: Annotated[str, PropertyInfo(alias="clientId")]

    client_secret: Annotated[str, PropertyInfo(alias="clientSecret")]

    redirect_uri: Annotated[str, PropertyInfo(alias="redirectUri")]

    scope: str


McpRemoteOAuth: TypeAlias = Union[McpRemoteOAuthMcpOAuthConfig, Literal[False]]


class McpRemote(TypedDict, total=False):
    type: Required[Literal["remote"]]
    """Type of MCP server connection"""

    url: Required[str]
    """URL of the remote MCP server"""

    enabled: bool
    """Enable or disable the MCP server on startup"""

    headers: Dict[str, str]
    """Headers to send with the request"""

    oauth: McpRemoteOAuth
    """OAuth authentication configuration for the MCP server.

    Set to false to disable OAuth auto-detection.
    """

    timeout: int
    """Timeout for the MCP server connection"""


Mcp: TypeAlias = Union[McpLocal, McpRemote]


class ModeItem(TypedDict, total=False):
    disable: bool

    model: str

    prompt: str

    temperature: float

    tools: Dict[str, bool]


Mode: TypeAlias = Dict[str, ModeItem]


class ProviderModelsCost(TypedDict, total=False):
    input: Required[float]

    output: Required[float]

    cache_read: float

    cache_write: float


class ProviderModelsLimit(TypedDict, total=False):
    context: Required[float]

    output: Required[float]


class ProviderModels(TypedDict, total=False):
    id: str

    attachment: bool

    cost: ProviderModelsCost

    limit: ProviderModelsLimit

    name: str

    options: Dict[str, object]

    reasoning: bool

    release_date: str

    temperature: bool

    tool_call: bool


class ProviderOptions(TypedDict, total=False):
    api_key: Annotated[str, PropertyInfo(alias="apiKey")]

    base_url: Annotated[str, PropertyInfo(alias="baseURL")]


class ProviderItem(TypedDict, total=False):
    models: Required[Dict[str, ProviderModels]]

    id: str

    api: str

    env: List[str]

    name: str

    npm: str

    options: ProviderOptions


Provider: TypeAlias = Dict[str, ProviderItem]


class ConfigUpdateParams(TypedDict, total=False):
    schema_: Annotated[str, PropertyInfo(alias="$schema")]
    """JSON schema reference for configuration validation"""

    agent: Agent
    """Modes configuration, see https://opencode.ai/docs/modes"""

    autoshare: bool
    """@deprecated Use 'share' field instead.

    Share newly created sessions automatically
    """

    autoupdate: bool
    """Automatically update to the latest version"""

    disabled_providers: List[str]
    """Disable providers that are loaded automatically"""

    experimental: Experimental

    instructions: List[str]
    """Additional instruction files or patterns to include"""

    keybinds: Keybinds
    """Custom keybind configurations"""

    layout: Literal["auto", "stretch"]
    """@deprecated Always uses stretch layout."""

    mcp: Dict[str, Mcp]
    """MCP (Model Context Protocol) server configurations"""

    mode: Mode
    """Modes configuration, see https://opencode.ai/docs/modes"""

    model: str
    """Model to use in the format of provider/model, eg anthropic/claude-2"""

    provider: Provider
    """Custom provider configurations and model overrides"""

    share: Literal["manual", "auto", "disabled"]
    """
    Control sharing behavior:'manual' allows manual sharing via commands, 'auto'
    enables automatic sharing, 'disabled' disables all sharing
    """

    small_model: str
    """
    Small model to use for tasks like summarization and title generation in the
    format of provider/model
    """

    theme: str
    """Theme name to use for the interface"""

    username: str
    """Custom username to display in conversations instead of system username"""
