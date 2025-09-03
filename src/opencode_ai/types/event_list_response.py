# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .part import Part
from .._utils import PropertyInfo
from .message import Message
from .._models import BaseModel
from .session.session import Session
from .session.permission import Permission
from .shared.unknown_error import UnknownError
from .shared.provider_auth_error import ProviderAuthError
from .shared.message_aborted_error import MessageAbortedError

__all__ = [
    "EventListResponse",
    "EventInstallationUpdated",
    "EventInstallationUpdatedProperties",
    "EventLspClientDiagnostics",
    "EventLspClientDiagnosticsProperties",
    "EventMessageUpdated",
    "EventMessageUpdatedProperties",
    "EventMessageRemoved",
    "EventMessageRemovedProperties",
    "EventMessagePartUpdated",
    "EventMessagePartUpdatedProperties",
    "EventMessagePartRemoved",
    "EventMessagePartRemovedProperties",
    "EventPermissionUpdated",
    "EventPermissionReplied",
    "EventPermissionRepliedProperties",
    "EventFileEdited",
    "EventFileEditedProperties",
    "EventSessionUpdated",
    "EventSessionUpdatedProperties",
    "EventSessionDeleted",
    "EventSessionDeletedProperties",
    "EventSessionIdle",
    "EventSessionIdleProperties",
    "EventSessionError",
    "EventSessionErrorProperties",
    "EventSessionErrorPropertiesError",
    "EventSessionErrorPropertiesErrorMessageOutputLengthError",
    "EventServerConnected",
]


class EventInstallationUpdatedProperties(BaseModel):
    version: str


class EventInstallationUpdated(BaseModel):
    properties: EventInstallationUpdatedProperties

    type: Literal["installation.updated"]


class EventLspClientDiagnosticsProperties(BaseModel):
    path: str

    server_id: str = FieldInfo(alias="serverID")


class EventLspClientDiagnostics(BaseModel):
    properties: EventLspClientDiagnosticsProperties

    type: Literal["lsp.client.diagnostics"]


class EventMessageUpdatedProperties(BaseModel):
    info: Message


class EventMessageUpdated(BaseModel):
    properties: EventMessageUpdatedProperties

    type: Literal["message.updated"]


class EventMessageRemovedProperties(BaseModel):
    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")


class EventMessageRemoved(BaseModel):
    properties: EventMessageRemovedProperties

    type: Literal["message.removed"]


class EventMessagePartUpdatedProperties(BaseModel):
    part: Part


class EventMessagePartUpdated(BaseModel):
    properties: EventMessagePartUpdatedProperties

    type: Literal["message.part.updated"]


class EventMessagePartRemovedProperties(BaseModel):
    message_id: str = FieldInfo(alias="messageID")

    part_id: str = FieldInfo(alias="partID")

    session_id: str = FieldInfo(alias="sessionID")


class EventMessagePartRemoved(BaseModel):
    properties: EventMessagePartRemovedProperties

    type: Literal["message.part.removed"]


class EventPermissionUpdated(BaseModel):
    properties: Permission

    type: Literal["permission.updated"]


class EventPermissionRepliedProperties(BaseModel):
    permission_id: str = FieldInfo(alias="permissionID")

    response: str

    session_id: str = FieldInfo(alias="sessionID")


class EventPermissionReplied(BaseModel):
    properties: EventPermissionRepliedProperties

    type: Literal["permission.replied"]


class EventFileEditedProperties(BaseModel):
    file: str


class EventFileEdited(BaseModel):
    properties: EventFileEditedProperties

    type: Literal["file.edited"]


class EventSessionUpdatedProperties(BaseModel):
    info: Session


class EventSessionUpdated(BaseModel):
    properties: EventSessionUpdatedProperties

    type: Literal["session.updated"]


class EventSessionDeletedProperties(BaseModel):
    info: Session


class EventSessionDeleted(BaseModel):
    properties: EventSessionDeletedProperties

    type: Literal["session.deleted"]


class EventSessionIdleProperties(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")


class EventSessionIdle(BaseModel):
    properties: EventSessionIdleProperties

    type: Literal["session.idle"]


class EventSessionErrorPropertiesErrorMessageOutputLengthError(BaseModel):
    data: object

    name: Literal["MessageOutputLengthError"]


EventSessionErrorPropertiesError: TypeAlias = Annotated[
    Union[
        ProviderAuthError, UnknownError, EventSessionErrorPropertiesErrorMessageOutputLengthError, MessageAbortedError
    ],
    PropertyInfo(discriminator="name"),
]


class EventSessionErrorProperties(BaseModel):
    error: Optional[EventSessionErrorPropertiesError] = None

    session_id: Optional[str] = FieldInfo(alias="sessionID", default=None)


class EventSessionError(BaseModel):
    properties: EventSessionErrorProperties

    type: Literal["session.error"]


class EventServerConnected(BaseModel):
    properties: object

    type: Literal["server.connected"]


EventListResponse: TypeAlias = Annotated[
    Union[
        EventInstallationUpdated,
        EventLspClientDiagnostics,
        EventMessageUpdated,
        EventMessageRemoved,
        EventMessagePartUpdated,
        EventMessagePartRemoved,
        EventPermissionUpdated,
        EventPermissionReplied,
        EventFileEdited,
        EventSessionUpdated,
        EventSessionDeleted,
        EventSessionIdle,
        EventSessionError,
        EventServerConnected,
    ],
    PropertyInfo(discriminator="type"),
]
