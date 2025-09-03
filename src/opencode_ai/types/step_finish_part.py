# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["StepFinishPart", "Tokens", "TokensCache"]


class TokensCache(BaseModel):
    read: float

    write: float


class Tokens(BaseModel):
    cache: TokensCache

    input: float

    output: float

    reasoning: float


class StepFinishPart(BaseModel):
    id: str

    cost: float

    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")

    tokens: Tokens

    type: Literal["step-finish"]
