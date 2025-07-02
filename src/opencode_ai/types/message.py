# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel
from .message_part import MessagePart
from .shared.unknown_error import UnknownError
from .shared.provider_auth_error import ProviderAuthError

__all__ = [
    "Message",
    "Metadata",
    "MetadataTime",
    "MetadataTool",
    "MetadataToolTime",
    "MetadataAssistant",
    "MetadataAssistantPath",
    "MetadataAssistantTokens",
    "MetadataAssistantTokensCache",
    "MetadataError",
    "MetadataErrorMessageOutputLengthError",
    "MetadataUser",
]


class MetadataTime(BaseModel):
    created: float

    completed: Optional[float] = None


class MetadataToolTime(BaseModel):
    end: float

    start: float


class MetadataTool(BaseModel):
    time: MetadataToolTime

    title: str

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class MetadataAssistantPath(BaseModel):
    cwd: str

    root: str


class MetadataAssistantTokensCache(BaseModel):
    read: float

    write: float


class MetadataAssistantTokens(BaseModel):
    cache: MetadataAssistantTokensCache

    input: float

    output: float

    reasoning: float


class MetadataAssistant(BaseModel):
    cost: float

    api_model_id: str = FieldInfo(alias="modelID")

    path: MetadataAssistantPath

    provider_id: str = FieldInfo(alias="providerID")

    system: List[str]

    tokens: MetadataAssistantTokens

    summary: Optional[bool] = None


class MetadataErrorMessageOutputLengthError(BaseModel):
    data: object

    name: Literal["MessageOutputLengthError"]


MetadataError: TypeAlias = Annotated[
    Union[ProviderAuthError, UnknownError, MetadataErrorMessageOutputLengthError], PropertyInfo(discriminator="name")
]


class MetadataUser(BaseModel):
    snapshot: Optional[str] = None


class Metadata(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")

    time: MetadataTime

    tool: Dict[str, MetadataTool]

    assistant: Optional[MetadataAssistant] = None

    error: Optional[MetadataError] = None

    user: Optional[MetadataUser] = None


class Message(BaseModel):
    id: str

    metadata: Metadata

    parts: List[MessagePart]

    role: Literal["user", "assistant"]
