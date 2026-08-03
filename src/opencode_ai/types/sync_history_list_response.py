# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["SyncHistoryListResponse", "SyncHistoryListResponseItem"]


class SyncHistoryListResponseItem(BaseModel):
    id: str

    aggregate_id: str
    """Wire field is `aggregate_id` (snake_case) per this operation's own schema.

    Contrast with `SyncReplayParams`'s per-event `aggregateID` (camelCase) --
    the two inline schemas are independently defined in the spec and are not
    unified, so each is modeled exactly as its own schema declares.
    """

    data: object

    seq: int

    type: str


SyncHistoryListResponse: TypeAlias = List[SyncHistoryListResponseItem]
