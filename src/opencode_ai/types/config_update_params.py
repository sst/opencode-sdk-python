# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Tuple, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "ConfigUpdateParams",
    "Agent",
    "AgentConfig",
    "Attachment",
    "AttachmentImage",
    "CommandConfig",
    "Compaction",
    "Enterprise",
    "Experimental",
    "ExperimentalPolicy",
    "FormatterConfig",
    "LspConfig",
    "LspConfigDisabled",
    "LspConfigEnabled",
    "Mcp",
    "McpLocal",
    "McpRemote",
    "McpRemoteOAuth",
    "McpRemoteOAuthMcpOAuthConfig",
    "McpDisabled",
    "Mode",
    "PermissionActionConfig",
    "PermissionRuleConfig",
    "PermissionConfig",
    "PermissionConfigObject",
    "Provider",
    "ProviderItem",
    "ProviderModels",
    "ProviderModelsCost",
    "ProviderModelsCostContextOver200k",
    "ProviderModelsLimit",
    "ProviderModelsModalities",
    "ProviderModelsProvider",
    "ProviderModelsVariants",
    "ProviderOptions",
    "ReferenceConfigEntry",
    "ReferenceConfigEntryReferenceConfigEntryRepository",
    "ReferenceConfigEntryReferenceConfigEntryPath",
    "Server",
    "Skills",
    "ToolOutput",
    "Watcher",
]

PermissionActionConfig: TypeAlias = Literal["ask", "allow", "deny"]

PermissionRuleConfig: TypeAlias = Union[PermissionActionConfig, Dict[str, PermissionActionConfig]]


class PermissionConfigObject(TypedDict, total=False):
    bash: PermissionRuleConfig

    doom_loop: PermissionActionConfig

    edit: PermissionRuleConfig

    external_directory: PermissionRuleConfig

    glob: PermissionRuleConfig

    grep: PermissionRuleConfig

    list: PermissionRuleConfig

    lsp: PermissionRuleConfig

    question: PermissionActionConfig

    read: PermissionRuleConfig

    skill: PermissionRuleConfig

    task: PermissionRuleConfig

    todowrite: PermissionActionConfig

    webfetch: PermissionActionConfig

    websearch: PermissionActionConfig


PermissionConfig: TypeAlias = Union[PermissionActionConfig, PermissionConfigObject]


class AgentConfig(TypedDict, total=False):
    color: str
    """Hex color code (e.g., #FF5733) or theme color (e.g., primary)"""

    description: str

    disable: bool

    hidden: bool

    max_steps: Annotated[int, PropertyInfo(alias="maxSteps")]

    mode: Literal["subagent", "primary", "all"]

    model: str

    options: object

    permission: PermissionConfig

    prompt: str

    steps: int

    temperature: float

    tools: Dict[str, bool]

    top_p: float

    variant: str


Agent: TypeAlias = Dict[str, AgentConfig]


class AttachmentImage(TypedDict, total=False):
    auto_resize: bool

    max_base64_bytes: int

    max_height: int

    max_width: int


class Attachment(TypedDict, total=False):
    image: AttachmentImage


class CommandConfig(TypedDict, total=False):
    template: Required[str]

    agent: str

    description: str

    model: str

    subtask: bool

    variant: str


class Compaction(TypedDict, total=False):
    auto: bool

    preserve_recent_tokens: int

    prune: bool

    reserved: int

    tail_turns: int


class Enterprise(TypedDict, total=False):
    url: str


class ExperimentalPolicy(TypedDict, total=False):
    action: Required[Literal["provider.use"]]

    effect: Required[Literal["allow", "deny"]]

    resource: Required[str]


class Experimental(TypedDict, total=False):
    batch_tool: bool

    continue_loop_on_deny: bool

    disable_paste_summary: bool

    mcp_timeout: int

    open_telemetry: Annotated[bool, PropertyInfo(alias="openTelemetry")]

    policies: List[ExperimentalPolicy]

    primary_tools: List[str]


class FormatterConfig(TypedDict, total=False):
    command: List[str]

    disabled: bool

    environment: Dict[str, str]

    extensions: List[str]


class LspConfigDisabled(TypedDict, total=False):
    disabled: Required[Literal[True]]


class LspConfigEnabled(TypedDict, total=False):
    command: Required[List[str]]

    disabled: bool

    env: Dict[str, str]

    extensions: List[str]

    initialization: object


LspConfig: TypeAlias = Union[LspConfigDisabled, LspConfigEnabled]


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


class McpDisabled(TypedDict, total=False):
    enabled: Required[bool]


Mcp: TypeAlias = Union[McpLocal, McpRemote, McpDisabled]


Mode: TypeAlias = Dict[str, AgentConfig]


class ProviderModelsCostContextOver200k(TypedDict, total=False):
    input: Required[float]

    output: Required[float]

    cache_read: float

    cache_write: float


class ProviderModelsCost(TypedDict, total=False):
    input: Required[float]

    output: Required[float]

    cache_read: float

    cache_write: float

    context_over_200k: ProviderModelsCostContextOver200k


class ProviderModelsLimit(TypedDict, total=False):
    context: Required[float]

    output: Required[float]

    input: float


class ProviderModelsModalities(TypedDict, total=False):
    input: List[Literal["text", "audio", "image", "video", "pdf"]]

    output: List[Literal["text", "audio", "image", "video", "pdf"]]


class ProviderModelsProvider(TypedDict, total=False):
    api: str

    npm: str


class ProviderModelsVariants(TypedDict, total=False):
    disabled: bool


class ProviderModels(TypedDict, total=False):
    id: str

    attachment: bool

    cost: ProviderModelsCost

    experimental: bool

    family: str

    headers: Dict[str, str]

    interleaved: Union[Literal[True], object]
    """Either `true`, or an object with a `field` discriminator.

    Modeled loosely (`object`) for the object variant since it is a small,
    single-purpose shape (`{"field": "reasoning_content" | "reasoning_details"}`).
    """

    limit: ProviderModelsLimit

    modalities: ProviderModelsModalities

    name: str

    options: object

    provider: ProviderModelsProvider

    reasoning: bool

    release_date: str

    status: Literal["alpha", "beta", "deprecated", "active"]

    temperature: bool

    tool_call: bool

    variants: Dict[str, ProviderModelsVariants]


class ProviderOptions(TypedDict, total=False):
    api_key: Annotated[str, PropertyInfo(alias="apiKey")]

    base_url: Annotated[str, PropertyInfo(alias="baseURL")]

    chunk_timeout: Annotated[int, PropertyInfo(alias="chunkTimeout")]

    enterprise_url: Annotated[str, PropertyInfo(alias="enterpriseUrl")]

    header_timeout: Annotated[Union[int, Literal[False]], PropertyInfo(alias="headerTimeout")]
    """Timeout in milliseconds to wait for response headers.

    Provider integrations may set defaults. Set to false to disable timeout.
    """

    set_cache_key: Annotated[bool, PropertyInfo(alias="setCacheKey")]

    timeout: Union[int, Literal[False]]
    """Timeout in milliseconds for full requests to this provider.

    Set to false to disable timeout.
    """


class ProviderItem(TypedDict, total=False):
    api: str

    blacklist: List[str]

    env: List[str]

    id: str

    models: Dict[str, ProviderModels]

    name: str

    npm: str

    options: ProviderOptions

    whitelist: List[str]


Provider: TypeAlias = Dict[str, ProviderItem]


class ReferenceConfigEntryReferenceConfigEntryRepository(TypedDict, total=False):
    repository: Required[str]
    """Git repository URL, host/path reference, or GitHub owner/repo shorthand"""

    branch: str


class ReferenceConfigEntryReferenceConfigEntryPath(TypedDict, total=False):
    path: Required[str]
    """Absolute path, ~/ path, or workspace-relative path to a local reference directory"""


ReferenceConfigEntry: TypeAlias = Union[
    str, ReferenceConfigEntryReferenceConfigEntryRepository, ReferenceConfigEntryReferenceConfigEntryPath
]


class Server(TypedDict, total=False):
    cors: List[str]

    hostname: str

    mdns: bool

    mdns_domain: Annotated[str, PropertyInfo(alias="mdnsDomain")]

    port: int


class Skills(TypedDict, total=False):
    paths: List[str]

    urls: List[str]


class ToolOutput(TypedDict, total=False):
    max_bytes: int

    max_lines: int


class Watcher(TypedDict, total=False):
    ignore: List[str]


class ConfigUpdateParams(TypedDict, total=False):
    schema_: Annotated[str, PropertyInfo(alias="$schema")]
    """JSON schema reference for configuration validation"""

    agent: Agent
    """Agents configuration, see https://opencode.ai/docs/agents"""

    attachment: Attachment
    """Configuration for file attachments"""

    autoshare: bool
    """@deprecated Use 'share' field instead.

    Share newly created sessions automatically
    """

    autoupdate: Union[bool, Literal["notify"]]
    """Automatically update to the latest version.

    Set to true to auto-update, false to disable, or 'notify' to show update
    notifications
    """

    command: Dict[str, CommandConfig]
    """Custom commands available in the TUI and CLI"""

    compaction: Compaction
    """Configuration for automatic conversation compaction"""

    default_agent: str
    """Default agent to use for new sessions"""

    disabled_providers: List[str]
    """Disable providers that are loaded automatically"""

    enabled_providers: List[str]
    """Only enable these providers, disabling all others loaded automatically"""

    enterprise: Enterprise
    """Enterprise configuration"""

    experimental: Experimental
    """Experimental features that may change or be removed at any time"""

    formatter: Union[bool, Dict[str, FormatterConfig]]
    """Enable or configure formatters.

    Omit or set to false to disable, true to enable built-ins, or an object to
    enable built-ins with overrides.
    """

    instructions: List[str]
    """Additional instruction files or patterns to include"""

    layout: Literal["auto", "stretch"]
    """@deprecated Always uses stretch layout."""

    log_level: Annotated[Literal["DEBUG", "INFO", "WARN", "ERROR"], PropertyInfo(alias="logLevel")]
    """Log level"""

    lsp: Union[bool, Dict[str, LspConfig]]
    """Enable or configure LSP servers.

    Omit or set to false to disable, true to enable built-ins, or an object to
    enable built-ins with overrides.
    """

    mcp: Dict[str, Mcp]
    """MCP (Model Context Protocol) server configurations"""

    mode: Mode
    """Modes configuration, see https://opencode.ai/docs/modes"""

    model: str
    """Model to use in the format of provider/model, eg anthropic/claude-2"""

    permission: PermissionConfig
    """Permission rules, either a single action for all tools or per-tool rules"""

    plugin: List[Union[str, Tuple[str, object]]]
    """Plugins to load, either by name/path or a [name, options] tuple"""

    provider: Provider
    """Custom provider configurations and model overrides"""

    reference: Dict[str, ReferenceConfigEntry]
    """Named reference repositories or directories"""

    server: Server
    """Server configuration for opencode serve and web commands"""

    share: Literal["manual", "auto", "disabled"]
    """
    Control sharing behavior:'manual' allows manual sharing via commands, 'auto'
    enables automatic sharing, 'disabled' disables all sharing
    """

    shell: str
    """Shell to use for bash-like tools"""

    skills: Skills
    """Configuration for skill discovery"""

    small_model: str
    """
    Small model to use for tasks like summarization and title generation in the
    format of provider/model
    """

    snapshot: bool
    """Enable or disable automatic snapshot creation"""

    tool_output: ToolOutput
    """Limits applied to tool output before it is truncated"""

    tools: Dict[str, bool]
    """Enable or disable specific tools globally"""

    username: str
    """Custom username to display in conversations instead of system username"""

    watcher: Watcher
    """Configuration for the file watcher"""
