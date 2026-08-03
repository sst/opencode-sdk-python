# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import Dict, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "SessionStatusResponse",
    "SessionStatus",
    "SessionStatusIdle",
    "SessionStatusRetry",
    "SessionStatusRetryAction",
    "SessionStatusBusy",
]


class SessionStatusIdle(BaseModel):
    type: Literal["idle"]


class SessionStatusRetryAction(BaseModel):
    label: str

    message: str

    provider: str

    reason: str

    title: str

    link: Optional[str] = None


class SessionStatusRetry(BaseModel):
    attempt: int

    message: str

    next: int

    type: Literal["retry"]

    action: Optional[SessionStatusRetryAction] = None


class SessionStatusBusy(BaseModel):
    type: Literal["busy"]


SessionStatus: TypeAlias = Annotated[
    Union[SessionStatusIdle, SessionStatusRetry, SessionStatusBusy], PropertyInfo(discriminator="type")
]

SessionStatusResponse: TypeAlias = Dict[str, SessionStatus]
