# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["StepStartPartParam"]


class StepStartPartParam(TypedDict, total=False):
    id: Required[str]

    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    type: Required[Literal["step-start"]]
