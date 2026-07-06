# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SessionShellParams", "Model"]


class Model(TypedDict, total=False):
    provider_id: Required[Annotated[str, PropertyInfo(alias="providerID")]]

    model_id: Required[Annotated[str, PropertyInfo(alias="modelID")]]


class SessionShellParams(TypedDict, total=False):
    agent: Required[str]

    command: Required[str]

    message_id: Annotated[str, PropertyInfo(alias="messageID")]

    model: Model
