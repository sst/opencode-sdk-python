# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PermissionRequest", "PermissionRequestTool"]


class PermissionRequestTool(BaseModel):
    call_id: str = FieldInfo(alias="callID")

    message_id: str = FieldInfo(alias="messageID")


class PermissionRequest(BaseModel):
    id: str

    always: List[str]

    metadata: object

    patterns: List[str]

    permission: str

    session_id: str = FieldInfo(alias="sessionID")

    tool: Optional[PermissionRequestTool] = None
