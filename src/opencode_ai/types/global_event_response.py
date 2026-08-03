# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import Optional

from .._models import BaseModel
from .event_list_response import EventListResponse

__all__ = ["GlobalEventResponse"]


class GlobalEventResponse(BaseModel):
    """A single event emitted on the `GET /global/event` SSE stream.

    `payload` carries the same discriminated event union as `GET /event`
    (see `EventListResponse`); the wrapper adds the addressing context the
    event was emitted for.
    """

    directory: str

    payload: EventListResponse

    project: Optional[str] = None

    workspace: Optional[str] = None
