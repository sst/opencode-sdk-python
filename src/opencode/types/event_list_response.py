# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .message import Message
from .session import Session
from .._models import BaseModel
from .message_part import MessagePart
from .shared.unknown_error import UnknownError
from .shared.provider_auth_error import ProviderAuthError

__all__ = [
    "EventListResponse",
    "EventStorageWrite",
    "EventStorageWriteProperties",
    "EventInstallationUpdated",
    "EventInstallationUpdatedProperties",
    "EventLspClientDiagnostics",
    "EventLspClientDiagnosticsProperties",
    "EventPermissionUpdated",
    "EventPermissionUpdatedProperties",
    "EventPermissionUpdatedPropertiesTime",
    "EventMessageUpdated",
    "EventMessageUpdatedProperties",
    "EventMessagePartUpdated",
    "EventMessagePartUpdatedProperties",
    "EventSessionUpdated",
    "EventSessionUpdatedProperties",
    "EventSessionDeleted",
    "EventSessionDeletedProperties",
    "EventSessionError",
    "EventSessionErrorProperties",
    "EventSessionErrorPropertiesError",
    "EventSessionErrorPropertiesErrorMessageOutputLengthError",
]


class EventStorageWriteProperties(BaseModel):
    key: str

    content: Optional[object] = None


class EventStorageWrite(BaseModel):
    properties: EventStorageWriteProperties

    type: Literal["storage.write"]


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


class EventMessageUpdatedProperties(BaseModel):
    info: Message


class EventMessageUpdated(BaseModel):
    properties: EventMessageUpdatedProperties

    type: Literal["message.updated"]


class EventMessagePartUpdatedProperties(BaseModel):
    message_id: str = FieldInfo(alias="messageID")

    part: MessagePart

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


EventListResponse: TypeAlias = Annotated[
    Union[
        EventStorageWrite,
        EventInstallationUpdated,
        EventLspClientDiagnostics,
        EventPermissionUpdated,
        EventMessageUpdated,
        EventMessagePartUpdated,
        EventSessionUpdated,
        EventSessionDeleted,
        EventSessionError,
    ],
    PropertyInfo(discriminator="type"),
]
