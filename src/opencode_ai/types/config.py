# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel
from .keybinds_config import KeybindsConfig
from .mcp_local_config import McpLocalConfig
from .mcp_remote_config import McpRemoteConfig

__all__ = [
    "Config",
    "Agent",
    "AgentBuild",
    "AgentBuildPermission",
    "AgentGeneral",
    "AgentGeneralPermission",
    "AgentPlan",
    "AgentPlanPermission",
    "AgentAgentItem",
    "AgentAgentItemPermission",
    "Command",
    "Experimental",
    "ExperimentalHook",
    "ExperimentalHookFileEdited",
    "ExperimentalHookSessionCompleted",
    "Formatter",
    "Lsp",
    "LspDisabled",
    "LspUnionMember1",
    "Mcp",
    "Mode",
    "ModeBuild",
    "ModeBuildPermission",
    "ModePlan",
    "ModePlanPermission",
    "ModeModeItem",
    "ModeModeItemPermission",
    "Permission",
    "Provider",
    "ProviderModels",
    "ProviderModelsCost",
    "ProviderModelsLimit",
    "ProviderOptions",
    "Tui",
]


class AgentBuildPermission(BaseModel):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]], None] = None

    edit: Optional[Literal["ask", "allow", "deny"]] = None

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


class AgentBuild(BaseModel):
    description: Optional[str] = None
    """Description of when to use the agent"""

    disable: Optional[bool] = None

    mode: Optional[Literal["subagent", "primary", "all"]] = None

    model: Optional[str] = None

    permission: Optional[AgentBuildPermission] = None

    prompt: Optional[str] = None

    temperature: Optional[float] = None

    tools: Optional[Dict[str, bool]] = None

    top_p: Optional[float] = None

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class AgentGeneralPermission(BaseModel):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]], None] = None

    edit: Optional[Literal["ask", "allow", "deny"]] = None

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


class AgentGeneral(BaseModel):
    description: Optional[str] = None
    """Description of when to use the agent"""

    disable: Optional[bool] = None

    mode: Optional[Literal["subagent", "primary", "all"]] = None

    model: Optional[str] = None

    permission: Optional[AgentGeneralPermission] = None

    prompt: Optional[str] = None

    temperature: Optional[float] = None

    tools: Optional[Dict[str, bool]] = None

    top_p: Optional[float] = None

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class AgentPlanPermission(BaseModel):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]], None] = None

    edit: Optional[Literal["ask", "allow", "deny"]] = None

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


class AgentPlan(BaseModel):
    description: Optional[str] = None
    """Description of when to use the agent"""

    disable: Optional[bool] = None

    mode: Optional[Literal["subagent", "primary", "all"]] = None

    model: Optional[str] = None

    permission: Optional[AgentPlanPermission] = None

    prompt: Optional[str] = None

    temperature: Optional[float] = None

    tools: Optional[Dict[str, bool]] = None

    top_p: Optional[float] = None

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class AgentAgentItemPermission(BaseModel):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]], None] = None

    edit: Optional[Literal["ask", "allow", "deny"]] = None

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


class AgentAgentItem(BaseModel):
    description: Optional[str] = None
    """Description of when to use the agent"""

    disable: Optional[bool] = None

    mode: Optional[Literal["subagent", "primary", "all"]] = None

    model: Optional[str] = None

    permission: Optional[AgentAgentItemPermission] = None

    prompt: Optional[str] = None

    temperature: Optional[float] = None

    tools: Optional[Dict[str, bool]] = None

    top_p: Optional[float] = None

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class Agent(BaseModel):
    build: Optional[AgentBuild] = None

    general: Optional[AgentGeneral] = None

    plan: Optional[AgentPlan] = None

    __pydantic_extra__: Dict[str, AgentAgentItem] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> AgentAgentItem: ...


class Command(BaseModel):
    template: str

    agent: Optional[str] = None

    description: Optional[str] = None

    model: Optional[str] = None


class ExperimentalHookFileEdited(BaseModel):
    command: List[str]

    environment: Optional[Dict[str, str]] = None


class ExperimentalHookSessionCompleted(BaseModel):
    command: List[str]

    environment: Optional[Dict[str, str]] = None


class ExperimentalHook(BaseModel):
    file_edited: Optional[Dict[str, List[ExperimentalHookFileEdited]]] = None

    session_completed: Optional[List[ExperimentalHookSessionCompleted]] = None


class Experimental(BaseModel):
    hook: Optional[ExperimentalHook] = None


class Formatter(BaseModel):
    command: Optional[List[str]] = None

    disabled: Optional[bool] = None

    environment: Optional[Dict[str, str]] = None

    extensions: Optional[List[str]] = None


class LspDisabled(BaseModel):
    disabled: Literal[True]


class LspUnionMember1(BaseModel):
    command: List[str]

    disabled: Optional[bool] = None

    env: Optional[Dict[str, str]] = None

    extensions: Optional[List[str]] = None

    initialization: Optional[Dict[str, object]] = None


Lsp: TypeAlias = Union[LspDisabled, LspUnionMember1]

Mcp: TypeAlias = Annotated[Union[McpLocalConfig, McpRemoteConfig], PropertyInfo(discriminator="type")]


class ModeBuildPermission(BaseModel):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]], None] = None

    edit: Optional[Literal["ask", "allow", "deny"]] = None

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


class ModeBuild(BaseModel):
    description: Optional[str] = None
    """Description of when to use the agent"""

    disable: Optional[bool] = None

    mode: Optional[Literal["subagent", "primary", "all"]] = None

    model: Optional[str] = None

    permission: Optional[ModeBuildPermission] = None

    prompt: Optional[str] = None

    temperature: Optional[float] = None

    tools: Optional[Dict[str, bool]] = None

    top_p: Optional[float] = None

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ModePlanPermission(BaseModel):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]], None] = None

    edit: Optional[Literal["ask", "allow", "deny"]] = None

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


class ModePlan(BaseModel):
    description: Optional[str] = None
    """Description of when to use the agent"""

    disable: Optional[bool] = None

    mode: Optional[Literal["subagent", "primary", "all"]] = None

    model: Optional[str] = None

    permission: Optional[ModePlanPermission] = None

    prompt: Optional[str] = None

    temperature: Optional[float] = None

    tools: Optional[Dict[str, bool]] = None

    top_p: Optional[float] = None

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ModeModeItemPermission(BaseModel):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]], None] = None

    edit: Optional[Literal["ask", "allow", "deny"]] = None

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


class ModeModeItem(BaseModel):
    description: Optional[str] = None
    """Description of when to use the agent"""

    disable: Optional[bool] = None

    mode: Optional[Literal["subagent", "primary", "all"]] = None

    model: Optional[str] = None

    permission: Optional[ModeModeItemPermission] = None

    prompt: Optional[str] = None

    temperature: Optional[float] = None

    tools: Optional[Dict[str, bool]] = None

    top_p: Optional[float] = None

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class Mode(BaseModel):
    build: Optional[ModeBuild] = None

    plan: Optional[ModePlan] = None

    __pydantic_extra__: Dict[str, ModeModeItem] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> ModeModeItem: ...


class Permission(BaseModel):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]], None] = None

    edit: Optional[Literal["ask", "allow", "deny"]] = None

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


class ProviderModelsCost(BaseModel):
    input: float

    output: float

    cache_read: Optional[float] = None

    cache_write: Optional[float] = None


class ProviderModelsLimit(BaseModel):
    context: float

    output: float


class ProviderModels(BaseModel):
    id: Optional[str] = None

    attachment: Optional[bool] = None

    cost: Optional[ProviderModelsCost] = None

    limit: Optional[ProviderModelsLimit] = None

    name: Optional[str] = None

    options: Optional[Dict[str, object]] = None

    reasoning: Optional[bool] = None

    release_date: Optional[str] = None

    temperature: Optional[bool] = None

    tool_call: Optional[bool] = None


class ProviderOptions(BaseModel):
    api_key: Optional[str] = FieldInfo(alias="apiKey", default=None)

    base_url: Optional[str] = FieldInfo(alias="baseURL", default=None)

    timeout: Union[int, bool, None] = None
    """Timeout in milliseconds for requests to this provider.

    Default is 300000 (5 minutes). Set to false to disable timeout.
    """

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class Provider(BaseModel):
    id: Optional[str] = None

    api: Optional[str] = None

    env: Optional[List[str]] = None

    models: Optional[Dict[str, ProviderModels]] = None

    name: Optional[str] = None

    npm: Optional[str] = None

    options: Optional[ProviderOptions] = None


class Tui(BaseModel):
    scroll_speed: float
    """TUI scroll speed"""


class Config(BaseModel):
    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """JSON schema reference for configuration validation"""

    agent: Optional[Agent] = None
    """Agent configuration, see https://opencode.ai/docs/agent"""

    autoshare: Optional[bool] = None
    """@deprecated Use 'share' field instead.

    Share newly created sessions automatically
    """

    autoupdate: Optional[bool] = None
    """Automatically update to the latest version"""

    command: Optional[Dict[str, Command]] = None
    """Command configuration, see https://opencode.ai/docs/commands"""

    disabled_providers: Optional[List[str]] = None
    """Disable providers that are loaded automatically"""

    experimental: Optional[Experimental] = None

    formatter: Optional[Dict[str, Formatter]] = None

    instructions: Optional[List[str]] = None
    """Additional instruction files or patterns to include"""

    keybinds: Optional[KeybindsConfig] = None
    """Custom keybind configurations"""

    layout: Optional[Literal["auto", "stretch"]] = None
    """@deprecated Always uses stretch layout."""

    lsp: Optional[Dict[str, Lsp]] = None

    mcp: Optional[Dict[str, Mcp]] = None
    """MCP (Model Context Protocol) server configurations"""

    mode: Optional[Mode] = None
    """@deprecated Use `agent` field instead."""

    model: Optional[str] = None
    """Model to use in the format of provider/model, eg anthropic/claude-2"""

    permission: Optional[Permission] = None

    plugin: Optional[List[str]] = None

    provider: Optional[Dict[str, Provider]] = None
    """Custom provider configurations and model overrides"""

    share: Optional[Literal["manual", "auto", "disabled"]] = None
    """
    Control sharing behavior:'manual' allows manual sharing via commands, 'auto'
    enables automatic sharing, 'disabled' disables all sharing
    """

    small_model: Optional[str] = None
    """
    Small model to use for tasks like title generation in the format of
    provider/model
    """

    snapshot: Optional[bool] = None

    theme: Optional[str] = None
    """Theme name to use for the interface"""

    tools: Optional[Dict[str, bool]] = None

    tui: Optional[Tui] = None
    """TUI specific settings"""

    username: Optional[str] = None
    """Custom username to display in conversations instead of system username"""
