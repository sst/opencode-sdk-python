# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SessionRevertParams"]


class SessionRevertParams(TypedDict, total=False):
    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    part_id: Annotated[str, PropertyInfo(alias="partID")]
