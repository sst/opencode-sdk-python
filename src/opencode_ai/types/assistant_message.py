# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel
from .shared.api_error import APIError
from .shared.unknown_error import UnknownError
from .shared.provider_auth_error import ProviderAuthError
from .shared.message_aborted_error import MessageAbortedError
from .shared.context_overflow_error import ContextOverflowError
from .shared.structured_output_error import StructuredOutputError

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

    total: Optional[float] = None


class ErrorMessageOutputLengthError(BaseModel):
    data: object

    name: Literal["MessageOutputLengthError"]


Error: TypeAlias = Annotated[
    Union[
        ProviderAuthError,
        UnknownError,
        ErrorMessageOutputLengthError,
        MessageAbortedError,
        StructuredOutputError,
        ContextOverflowError,
        APIError,
    ],
    PropertyInfo(discriminator="name"),
]


class AssistantMessage(BaseModel):
    id: str

    agent: str

    cost: float

    mode: str

    api_model_id: str = FieldInfo(alias="modelID")

    parent_id: str = FieldInfo(alias="parentID")

    path: Path

    provider_id: str = FieldInfo(alias="providerID")

    role: Literal["assistant"]

    session_id: str = FieldInfo(alias="sessionID")

    time: Time

    tokens: Tokens

    error: Optional[Error] = None

    finish: Optional[str] = None

    # Precise structured-output model is deferred; typed as an untyped object for now.
    structured: Optional[object] = None

    summary: Optional[bool] = None

    variant: Optional[str] = None
