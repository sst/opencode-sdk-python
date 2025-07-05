# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel
from .shared.unknown_error import UnknownError
from .assistant_message_part import AssistantMessagePart
from .shared.provider_auth_error import ProviderAuthError

__all__ = ["AssistantMessage", "Path", "Time", "Tokens", "TokensCache", "Error", "ErrorMessageOutputLengthError"]


class Path(BaseModel):
    cwd: str

    root: str


class Time(BaseModel):
    created: float

    completed: Optional[float] = None


class TokensCache(BaseModel):
    read: float

    write: float


class Tokens(BaseModel):
    cache: TokensCache

    input: float

    output: float

    reasoning: float


class ErrorMessageOutputLengthError(BaseModel):
    data: object

    name: Literal["MessageOutputLengthError"]


Error: TypeAlias = Annotated[
    Union[ProviderAuthError, UnknownError, ErrorMessageOutputLengthError], PropertyInfo(discriminator="name")
]


class AssistantMessage(BaseModel):
    id: str

    cost: float

    api_model_id: str = FieldInfo(alias="modelID")

    parts: List[AssistantMessagePart]

    path: Path

    provider_id: str = FieldInfo(alias="providerID")

    role: Literal["assistant"]

    session_id: str = FieldInfo(alias="sessionID")

    system: List[str]

    time: Time

    tokens: Tokens

    error: Optional[Error] = None

    summary: Optional[bool] = None
