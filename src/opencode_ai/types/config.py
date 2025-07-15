# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .config import ModeUnnamedTypeWithobjectParent0ModeUnnamedTypeWithobjectParent0Item
from .._utils import PropertyInfo
from .._models import BaseModel
from .keybinds import Keybinds
from .log_level import LogLevel
from .mcp_local import McpLocal
from .mcp_remote import McpRemote

__all__ = [
    "Config",
    "Experimental",
    "ExperimentalHook",
    "ExperimentalHookFileEdited",
    "ExperimentalHookSessionCompleted",
    "Mcp",
    "Mode",
    "ModeBuild",
    "ModePlan",
    "Provider",
    "ProviderModels",
    "ProviderModelsCost",
    "ProviderModelsLimit",
]


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


Mcp: TypeAlias = Annotated[Union[McpLocal, McpRemote], PropertyInfo(discriminator="type")]


class ModeBuild(BaseModel):
    model: Optional[str] = None

    prompt: Optional[str] = None

    tools: Optional[Dict[str, bool]] = None


class ModePlan(BaseModel):
    model: Optional[str] = None

    prompt: Optional[str] = None

    tools: Optional[Dict[str, bool]] = None


class Mode(BaseModel):
    build: Optional[ModeBuild] = None

    plan: Optional[ModePlan] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> ModeUnnamedTypeWithobjectParent0ModeUnnamedTypeWithobjectParent0Item: ...


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


class Provider(BaseModel):
    models: Dict[str, ProviderModels]

    id: Optional[str] = None

    api: Optional[str] = None

    env: Optional[List[str]] = None

    name: Optional[str] = None

    npm: Optional[str] = None

    options: Optional[Dict[str, object]] = None


class Config(BaseModel):
    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """JSON schema reference for configuration validation"""

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

    keybinds: Optional[Keybinds] = None
    """Custom keybind configurations"""

    log_level: Optional[LogLevel] = None
    """Minimum log level to write to log files"""

    mcp: Optional[Dict[str, Mcp]] = None
    """MCP (Model Context Protocol) server configurations"""

    mode: Optional[Mode] = None

    model: Optional[str] = None
    """Model to use in the format of provider/model, eg anthropic/claude-2"""

    provider: Optional[Dict[str, Provider]] = None
    """Custom provider configurations and model overrides"""

    share: Optional[Literal["auto", "disabled"]] = None
    """
    Control sharing behavior: 'auto' enables automatic sharing, 'disabled' disables
    all sharing
    """

    theme: Optional[str] = None
    """Theme name to use for the interface"""

    username: Optional[str] = None
    """Custom username to display in conversations instead of system username"""
