# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel
from .keybinds import Keybinds
from .mcp_local import McpLocal
from .mcp_remote import McpRemote

__all__ = [
    "Config",
    "Experimental",
    "ExperimentalHook",
    "ExperimentalHookFileEdited",
    "ExperimentalHookSessionCompleted",
    "Mcp",
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
    """Share newly created sessions automatically"""

    autoupdate: Optional[bool] = None
    """Automatically update to the latest version"""

    disabled_providers: Optional[List[str]] = None
    """Disable providers that are loaded automatically"""

    experimental: Optional[Experimental] = None

    instructions: Optional[List[str]] = None
    """Additional instruction files or patterns to include"""

    keybinds: Optional[Keybinds] = None
    """Custom keybind configurations"""

    mcp: Optional[Dict[str, Mcp]] = None
    """MCP (Model Context Protocol) server configurations"""

    model: Optional[str] = None
    """Model to use in the format of provider/model, eg anthropic/claude-2"""

    provider: Optional[Dict[str, Provider]] = None
    """Custom provider configurations and model overrides"""

    theme: Optional[str] = None
    """Theme name to use for the interface"""
