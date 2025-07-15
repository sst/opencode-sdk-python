# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SnapshotPart"]


class SnapshotPart(BaseModel):
    id: str

    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")

    snapshot: str

    type: Literal["snapshot"]
