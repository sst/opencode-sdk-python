# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel
from .mode_config import ModeConfig
from .keybinds_config import KeybindsConfig
from .mcp_local_config import McpLocalConfig
from .mcp_remote_config import McpRemoteConfig

__all__ = [
    "Config",
    "Agent",
    "AgentGeneral",
    "AgentAgentItem",
    "Experimental",
    "ExperimentalHook",
    "ExperimentalHookFileEdited",
    "ExperimentalHookSessionCompleted",
    "Mcp",
    "Mode",
    "Provider",
    "ProviderModels",
    "ProviderModelsCost",
    "ProviderModelsLimit",
    "ProviderOptions",
]


class AgentGeneral(ModeConfig):
    description: str


class AgentAgentItem(ModeConfig):
    description: str


class Agent(BaseModel):
    general: Optional[AgentGeneral] = None

    __pydantic_extra__: Dict[str, AgentAgentItem] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> AgentAgentItem: ...


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


Mcp: TypeAlias = Annotated[Union[McpLocalConfig, McpRemoteConfig], PropertyInfo(discriminator="type")]


class Mode(BaseModel):
    build: Optional[ModeConfig] = None

    plan: Optional[ModeConfig] = None

    __pydantic_extra__: Dict[str, ModeConfig] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> ModeConfig: ...


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

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class Provider(BaseModel):
    models: Dict[str, ProviderModels]

    id: Optional[str] = None

    api: Optional[str] = None

    env: Optional[List[str]] = None

    name: Optional[str] = None

    npm: Optional[str] = None

    options: Optional[ProviderOptions] = None


class Config(BaseModel):
    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """JSON schema reference for configuration validation"""

    agent: Optional[Agent] = None
    """Modes configuration, see https://opencode.ai/docs/modes"""

    autoshare: Optional[bool] = None
    """@deprecated Use 'share' field instead.

    Share newly created sessions automatically
    """

    autoupdate: Optional[bool] = None
    """Automatically update to the latest version"""

    disabled_providers: Optional[List[str]] = None
    """Disable providers that are loaded automatically"""

    experimental: Optional[Experimental] = None

    instructions: Optional[List[str]] = None
    """Additional instruction files or patterns to include"""

    keybinds: Optional[KeybindsConfig] = None
    """Custom keybind configurations"""

    layout: Optional[Literal["auto", "stretch"]] = None
    """@deprecated Always uses stretch layout."""

    mcp: Optional[Dict[str, Mcp]] = None
    """MCP (Model Context Protocol) server configurations"""

    mode: Optional[Mode] = None
    """Modes configuration, see https://opencode.ai/docs/modes"""

    model: Optional[str] = None
    """Model to use in the format of provider/model, eg anthropic/claude-2"""

    provider: Optional[Dict[str, Provider]] = None
    """Custom provider configurations and model overrides"""

    share: Optional[Literal["manual", "auto", "disabled"]] = None
    """
    Control sharing behavior:'manual' allows manual sharing via commands, 'auto'
    enables automatic sharing, 'disabled' disables all sharing
    """

    small_model: Optional[str] = None
    """
    Small model to use for tasks like summarization and title generation in the
    format of provider/model
    """

    theme: Optional[str] = None
    """Theme name to use for the interface"""

    username: Optional[str] = None
    """Custom username to display in conversations instead of system username"""
