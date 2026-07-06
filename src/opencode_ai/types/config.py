# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Tuple, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .agent_config import AgentConfig
from .mcp_local_config import McpLocalConfig
from .mcp_remote_config import McpRemoteConfig
from .permission_config import PermissionConfig

__all__ = [
    "Config",
    "Agent",
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
    "McpDisabled",
    "Mode",
    "Provider",
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


class Agent(BaseModel):
    build: Optional[AgentConfig] = None

    explore: Optional[AgentConfig] = None

    general: Optional[AgentConfig] = None

    plan: Optional[AgentConfig] = None

    summary: Optional[AgentConfig] = None

    title: Optional[AgentConfig] = None

    __pydantic_extra__: Dict[str, AgentConfig] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> AgentConfig: ...


class AttachmentImage(BaseModel):
    auto_resize: Optional[bool] = None

    max_base64_bytes: Optional[int] = None

    max_height: Optional[int] = None

    max_width: Optional[int] = None


class Attachment(BaseModel):
    image: Optional[AttachmentImage] = None


class CommandConfig(BaseModel):
    template: str

    agent: Optional[str] = None

    description: Optional[str] = None

    model: Optional[str] = None

    subtask: Optional[bool] = None

    variant: Optional[str] = None


class Compaction(BaseModel):
    auto: Optional[bool] = None

    preserve_recent_tokens: Optional[int] = None

    prune: Optional[bool] = None

    reserved: Optional[int] = None

    tail_turns: Optional[int] = None


class Enterprise(BaseModel):
    url: Optional[str] = None


class ExperimentalPolicy(BaseModel):
    action: Literal["provider.use"]

    effect: Literal["allow", "deny"]

    resource: str


class Experimental(BaseModel):
    batch_tool: Optional[bool] = None

    continue_loop_on_deny: Optional[bool] = None

    disable_paste_summary: Optional[bool] = None

    mcp_timeout: Optional[int] = None

    open_telemetry: Optional[bool] = FieldInfo(alias="openTelemetry", default=None)

    policies: Optional[List[ExperimentalPolicy]] = None

    primary_tools: Optional[List[str]] = None


class FormatterConfig(BaseModel):
    command: Optional[List[str]] = None

    disabled: Optional[bool] = None

    environment: Optional[Dict[str, str]] = None

    extensions: Optional[List[str]] = None


class LspConfigDisabled(BaseModel):
    disabled: Literal[True]


class LspConfigEnabled(BaseModel):
    command: List[str]

    disabled: Optional[bool] = None

    env: Optional[Dict[str, str]] = None

    extensions: Optional[List[str]] = None

    initialization: Optional[object] = None


LspConfig: TypeAlias = Union[LspConfigDisabled, LspConfigEnabled]


class McpDisabled(BaseModel):
    enabled: bool


Mcp: TypeAlias = Union[McpLocalConfig, McpRemoteConfig, McpDisabled]


class Mode(BaseModel):
    build: Optional[AgentConfig] = None

    plan: Optional[AgentConfig] = None

    __pydantic_extra__: Dict[str, AgentConfig] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> AgentConfig: ...


class ProviderModelsCostContextOver200k(BaseModel):
    input: float

    output: float

    cache_read: Optional[float] = None

    cache_write: Optional[float] = None


class ProviderModelsCost(BaseModel):
    input: float

    output: float

    cache_read: Optional[float] = None

    cache_write: Optional[float] = None

    context_over_200k: Optional[ProviderModelsCostContextOver200k] = None


class ProviderModelsLimit(BaseModel):
    context: float

    output: float

    input: Optional[float] = None


class ProviderModelsModalities(BaseModel):
    input: Optional[List[Literal["text", "audio", "image", "video", "pdf"]]] = None

    output: Optional[List[Literal["text", "audio", "image", "video", "pdf"]]] = None


class ProviderModelsProvider(BaseModel):
    api: Optional[str] = None

    npm: Optional[str] = None


class ProviderModelsVariants(BaseModel):
    disabled: Optional[bool] = None

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ProviderModels(BaseModel):
    id: Optional[str] = None

    attachment: Optional[bool] = None

    cost: Optional[ProviderModelsCost] = None

    experimental: Optional[bool] = None

    family: Optional[str] = None

    headers: Optional[Dict[str, str]] = None

    interleaved: Optional[Union[Literal[True], object]] = None
    """Either `true`, or an object with a `field` discriminator.

    Modeled loosely (`object`) for the object variant since it is a small,
    single-purpose shape (`{"field": "reasoning_content" | "reasoning_details"}`).
    """

    limit: Optional[ProviderModelsLimit] = None

    modalities: Optional[ProviderModelsModalities] = None

    name: Optional[str] = None

    options: Optional[object] = None

    provider: Optional[ProviderModelsProvider] = None

    reasoning: Optional[bool] = None

    release_date: Optional[str] = None

    status: Optional[Literal["alpha", "beta", "deprecated", "active"]] = None

    temperature: Optional[bool] = None

    tool_call: Optional[bool] = None

    variants: Optional[Dict[str, ProviderModelsVariants]] = None


class ProviderOptions(BaseModel):
    api_key: Optional[str] = FieldInfo(alias="apiKey", default=None)

    base_url: Optional[str] = FieldInfo(alias="baseURL", default=None)

    chunk_timeout: Optional[int] = FieldInfo(alias="chunkTimeout", default=None)

    enterprise_url: Optional[str] = FieldInfo(alias="enterpriseUrl", default=None)

    header_timeout: Optional[Union[int, Literal[False]]] = FieldInfo(alias="headerTimeout", default=None)
    """Timeout in milliseconds to wait for response headers.

    Provider integrations may set defaults. Set to false to disable timeout.
    """

    set_cache_key: Optional[bool] = FieldInfo(alias="setCacheKey", default=None)

    timeout: Optional[Union[int, Literal[False]]] = None
    """Timeout in milliseconds for full requests to this provider.

    Set to false to disable timeout.
    """

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class Provider(BaseModel):
    api: Optional[str] = None

    blacklist: Optional[List[str]] = None

    env: Optional[List[str]] = None

    id: Optional[str] = None

    models: Optional[Dict[str, ProviderModels]] = None

    name: Optional[str] = None

    npm: Optional[str] = None

    options: Optional[ProviderOptions] = None

    whitelist: Optional[List[str]] = None


class ReferenceConfigEntryReferenceConfigEntryRepository(BaseModel):
    repository: str
    """Git repository URL, host/path reference, or GitHub owner/repo shorthand"""

    branch: Optional[str] = None


class ReferenceConfigEntryReferenceConfigEntryPath(BaseModel):
    path: str
    """Absolute path, ~/ path, or workspace-relative path to a local reference directory"""


ReferenceConfigEntry: TypeAlias = Union[
    str, ReferenceConfigEntryReferenceConfigEntryRepository, ReferenceConfigEntryReferenceConfigEntryPath
]


class Server(BaseModel):
    cors: Optional[List[str]] = None

    hostname: Optional[str] = None

    mdns: Optional[bool] = None

    mdns_domain: Optional[str] = FieldInfo(alias="mdnsDomain", default=None)

    port: Optional[int] = None


class Skills(BaseModel):
    paths: Optional[List[str]] = None

    urls: Optional[List[str]] = None


class ToolOutput(BaseModel):
    max_bytes: Optional[int] = None

    max_lines: Optional[int] = None


class Watcher(BaseModel):
    ignore: Optional[List[str]] = None


class Config(BaseModel):
    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """JSON schema reference for configuration validation"""

    agent: Optional[Agent] = None
    """Agents configuration, see https://opencode.ai/docs/agents"""

    attachment: Optional[Attachment] = None
    """Configuration for file attachments"""

    autoshare: Optional[bool] = None
    """@deprecated Use 'share' field instead.

    Share newly created sessions automatically
    """

    autoupdate: Optional[Union[bool, Literal["notify"]]] = None
    """Automatically update to the latest version.

    Set to true to auto-update, false to disable, or 'notify' to show update
    notifications
    """

    command: Optional[Dict[str, CommandConfig]] = None
    """Custom commands available in the TUI and CLI"""

    compaction: Optional[Compaction] = None
    """Configuration for automatic conversation compaction"""

    default_agent: Optional[str] = None
    """Default agent to use for new sessions"""

    disabled_providers: Optional[List[str]] = None
    """Disable providers that are loaded automatically"""

    enabled_providers: Optional[List[str]] = None
    """Only enable these providers, disabling all others loaded automatically"""

    enterprise: Optional[Enterprise] = None
    """Enterprise configuration"""

    experimental: Optional[Experimental] = None
    """Experimental features that may change or be removed at any time"""

    formatter: Optional[Union[bool, Dict[str, FormatterConfig]]] = None
    """Enable or configure formatters.

    Omit or set to false to disable, true to enable built-ins, or an object to
    enable built-ins with overrides.
    """

    instructions: Optional[List[str]] = None
    """Additional instruction files or patterns to include"""

    layout: Optional[Literal["auto", "stretch"]] = None
    """@deprecated Always uses stretch layout."""

    log_level: Optional[Literal["DEBUG", "INFO", "WARN", "ERROR"]] = FieldInfo(alias="logLevel", default=None)
    """Log level"""

    lsp: Optional[Union[bool, Dict[str, LspConfig]]] = None
    """Enable or configure LSP servers.

    Omit or set to false to disable, true to enable built-ins, or an object to
    enable built-ins with overrides.
    """

    mcp: Optional[Dict[str, Mcp]] = None
    """MCP (Model Context Protocol) server configurations"""

    mode: Optional[Mode] = None
    """Modes configuration, see https://opencode.ai/docs/modes"""

    model: Optional[str] = None
    """Model to use in the format of provider/model, eg anthropic/claude-2"""

    permission: Optional[PermissionConfig] = None
    """Permission rules, either a single action for all tools or per-tool rules"""

    plugin: Optional[List[Union[str, Tuple[str, object]]]] = None
    """Plugins to load, either by name/path or a [name, options] tuple"""

    provider: Optional[Dict[str, Provider]] = None
    """Custom provider configurations and model overrides"""

    reference: Optional[Dict[str, ReferenceConfigEntry]] = None
    """Named reference repositories or directories"""

    server: Optional[Server] = None
    """Server configuration for opencode serve and web commands"""

    share: Optional[Literal["manual", "auto", "disabled"]] = None
    """
    Control sharing behavior:'manual' allows manual sharing via commands, 'auto'
    enables automatic sharing, 'disabled' disables all sharing
    """

    shell: Optional[str] = None
    """Shell to use for bash-like tools"""

    skills: Optional[Skills] = None
    """Configuration for skill discovery"""

    small_model: Optional[str] = None
    """
    Small model to use for tasks like summarization and title generation in the
    format of provider/model
    """

    snapshot: Optional[bool] = None
    """Enable or disable automatic snapshot creation"""

    tool_output: Optional[ToolOutput] = None
    """Limits applied to tool output before it is truncated"""

    tools: Optional[Dict[str, bool]] = None
    """Enable or disable specific tools globally"""

    username: Optional[str] = None
    """Custom username to display in conversations instead of system username"""

    watcher: Optional[Watcher] = None
    """Configuration for the file watcher"""
