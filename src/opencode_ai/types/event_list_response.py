# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .part import Part
from .._utils import PropertyInfo
from .message import Message
from .session import Session
from .._models import BaseModel
from .shared.unknown_error import UnknownError
from .shared.provider_auth_error import ProviderAuthError
from .shared.message_aborted_error import MessageAbortedError

__all__ = [
    "EventListResponse",
    "EventUnknown",
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
    "EventStorageWrite",
    "EventStorageWriteProperties",
    "EventPermissionUpdated",
    "EventPermissionUpdatedProperties",
    "EventPermissionUpdatedPropertiesTime",
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
    "EventFileWatcherUpdated",
    "EventFileWatcherUpdatedProperties",
    "EventIdeInstalled",
    "EventIdeInstalledProperties",
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


class EventStorageWriteProperties(BaseModel):
    key: str

    content: Optional[object] = None


class EventStorageWrite(BaseModel):
    properties: EventStorageWriteProperties

    type: Literal["storage.write"]


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


class EventFileWatcherUpdatedProperties(BaseModel):
    event: Literal["rename", "change"]

    file: str


class EventFileWatcherUpdated(BaseModel):
    properties: EventFileWatcherUpdatedProperties

    type: Literal["file.watcher.updated"]


class EventIdeInstalledProperties(BaseModel):
    ide: str


class EventIdeInstalled(BaseModel):
    properties: EventIdeInstalledProperties

    type: Literal["ide.installed"]


class EventUnknown(BaseModel):
    """Permissive fallback for event `type` values not yet enumerated by this SDK.

    The server's event union has grown well beyond the variants modeled here
    (full enumeration is tracked separately). Rather than raising when an
    unrecognized `type` is encountered, unmatched events deserialize into this
    open-ended model so `client.event.list()` keeps working as the server adds
    new event kinds.
    """

    type: str

    properties: Optional[object] = None


# Note on ordering: `EventUnknown` is intentionally listed *first*, not last.
#
# `_models.construct_type()` (the non-strict path used by default response
# parsing) resolves a `PropertyInfo(discriminator=...)` union in two steps:
#   1. If the discriminator value is present in the precomputed
#      `{literal value: variant type}` mapping, that exact variant is
#      constructed directly -- this happens regardless of the union's
#      ordering, so every known `type` literal below is still matched
#      correctly no matter where `EventUnknown` sits.
#   2. Otherwise (unknown/unmapped discriminator value) it falls back to
#      `for variant in args: try construct_type(...) except: continue` and
#      returns the *first* variant that doesn't raise. Because `BaseModel`
#      variants are built via the SDK's overridden `.construct()`, which
#      never validates and therefore never raises, this loop always "succeeds"
#      on the first variant tried -- so whichever variant is listed first
#      is what unknown events actually resolve to.
#
# `EventUnknown`'s own `type` field is a plain `str` (not a `Literal`), so it
# is never added to the discriminator mapping itself -- it only ever gets
# reached through the unmatched-value fallback path above, and being first
# guarantees it -- rather than an arbitrary known variant -- is what's chosen.
EventListResponse: TypeAlias = Annotated[
    Union[
        EventUnknown,
        EventInstallationUpdated,
        EventLspClientDiagnostics,
        EventMessageUpdated,
        EventMessageRemoved,
        EventMessagePartUpdated,
        EventMessagePartRemoved,
        EventStorageWrite,
        EventPermissionUpdated,
        EventFileEdited,
        EventSessionUpdated,
        EventSessionDeleted,
        EventSessionIdle,
        EventSessionError,
        EventServerConnected,
        EventFileWatcherUpdated,
        EventIdeInstalled,
    ],
    PropertyInfo(discriminator="type"),
]
