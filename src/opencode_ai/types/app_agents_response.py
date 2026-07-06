# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AppAgentsResponse", "Agent", "AgentModel", "AgentPermission"]


class AgentModel(BaseModel):
    api_model_id: str = FieldInfo(alias="modelID")

    provider_id: str = FieldInfo(alias="providerID")


class AgentPermission(BaseModel):
    action: Literal["allow", "deny", "ask"]

    pattern: str

    permission: str


class Agent(BaseModel):
    mode: Literal["subagent", "primary", "all"]

    name: str

    options: object

    permission: List[AgentPermission]

    color: Optional[str] = None

    description: Optional[str] = None

    hidden: Optional[bool] = None

    model: Optional[AgentModel] = None

    native: Optional[bool] = None

    prompt: Optional[str] = None

    steps: Optional[float] = None

    temperature: Optional[float] = None

    top_p: Optional[float] = FieldInfo(alias="topP", default=None)

    variant: Optional[str] = None


AppAgentsResponse: TypeAlias = List[Agent]
