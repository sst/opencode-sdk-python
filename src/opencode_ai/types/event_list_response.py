# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .message import Message
from .session import Session
from .._models import BaseModel
from .shared.unknown_error import UnknownError
from .assistant_message_part import AssistantMessagePart
from .shared.provider_auth_error import ProviderAuthError

__all__ = [
    "EventListResponse",
    "EventLspClientDiagnostics",
    "EventLspClientDiagnosticsProperties",
    "EventPermissionUpdated",
    "EventPermissionUpdatedProperties",
    "EventPermissionUpdatedPropertiesTime",
    "EventFileEdited",
    "EventFileEditedProperties",
    "EventInstallationUpdated",
    "EventInstallationUpdatedProperties",
    "EventStorageWrite",
    "EventStorageWriteProperties",
    "EventMessageUpdated",
    "EventMessageUpdatedProperties",
    "EventMessageRemoved",
    "EventMessageRemovedProperties",
    "EventMessagePartUpdated",
    "EventMessagePartUpdatedProperties",
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
    "EventFileWatcherUpdated",
    "EventFileWatcherUpdatedProperties",
]


class EventLspClientDiagnosticsProperties(BaseModel):
    path: str

    server_id: str = FieldInfo(alias="serverID")


class EventLspClientDiagnostics(BaseModel):
    properties: EventLspClientDiagnosticsProperties

    type: Literal["lsp.client.diagnostics"]


class EventPermissionUpdatedPropertiesTime(BaseModel):
    created: float


class EventPermissionUpdatedProperties(BaseModel):
    id: str

    metadata: Dict[str, object]

    session_id: str = FieldInfo(alias="sessionID")

    time: EventPermissionUpdatedPropertiesTime

    title: str


class EventPermissionUpdated(BaseModel):
    properties: EventPermissionUpdatedProperties

    type: Literal["permission.updated"]


class EventFileEditedProperties(BaseModel):
    file: str


class EventFileEdited(BaseModel):
    properties: EventFileEditedProperties

    type: Literal["file.edited"]


class EventInstallationUpdatedProperties(BaseModel):
    version: str


class EventInstallationUpdated(BaseModel):
    properties: EventInstallationUpdatedProperties

    type: Literal["installation.updated"]


class EventStorageWriteProperties(BaseModel):
    key: str

    content: Optional[object] = None


class EventStorageWrite(BaseModel):
    properties: EventStorageWriteProperties

    type: Literal["storage.write"]


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
    message_id: str = FieldInfo(alias="messageID")

    part: AssistantMessagePart

    session_id: str = FieldInfo(alias="sessionID")


class EventMessagePartUpdated(BaseModel):
    properties: EventMessagePartUpdatedProperties

    type: Literal["message.part.updated"]


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
    Union[ProviderAuthError, UnknownError, EventSessionErrorPropertiesErrorMessageOutputLengthError],
    PropertyInfo(discriminator="name"),
]


class EventSessionErrorProperties(BaseModel):
    error: Optional[EventSessionErrorPropertiesError] = None


class EventSessionError(BaseModel):
    properties: EventSessionErrorProperties

    type: Literal["session.error"]


class EventFileWatcherUpdatedProperties(BaseModel):
    event: Literal["rename", "change"]

    file: str


class EventFileWatcherUpdated(BaseModel):
    properties: EventFileWatcherUpdatedProperties

    type: Literal["file.watcher.updated"]


EventListResponse: TypeAlias = Annotated[
    Union[
        EventLspClientDiagnostics,
        EventPermissionUpdated,
        EventFileEdited,
        EventInstallationUpdated,
        EventStorageWrite,
        EventMessageUpdated,
        EventMessageRemoved,
        EventMessagePartUpdated,
        EventSessionUpdated,
        EventSessionDeleted,
        EventSessionIdle,
        EventSessionError,
        EventFileWatcherUpdated,
    ],
    PropertyInfo(discriminator="type"),
]
