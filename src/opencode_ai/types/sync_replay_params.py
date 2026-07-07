# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SyncReplayParams", "Event"]


class Event(TypedDict, total=False):
    id: Required[str]

    aggregate_id: Required[Annotated[str, PropertyInfo(alias="aggregateID")]]
    """Wire field is `aggregateID` (camelCase) per this operation's own schema.

    Contrast with `SyncHistoryListResponseItem`'s `aggregate_id` (snake_case) --
    the two inline schemas are independently defined in the spec and are not
    unified, so each is modeled exactly as its own schema declares.
    """

    data: Required[object]

    seq: Required[int]

    type: Required[str]


class SyncReplayParams(TypedDict, total=False):
    directory: Required[str]
    """Directory whose sync events should be replayed.

    Note: this is a request **body** field, distinct from the `directory`
    **query** parameter that may also be present on this same request.
    """

    events: Required[Iterable[Event]]
