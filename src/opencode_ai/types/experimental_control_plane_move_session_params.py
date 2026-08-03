# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExperimentalControlPlaneMoveSessionParams", "MoveSessionDestination"]


class MoveSessionDestination(TypedDict, total=False):
    directory: Required[str]


class ExperimentalControlPlaneMoveSessionParams(TypedDict, total=False):
    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    destination: Required[MoveSessionDestination]

    move_changes: Annotated[bool, PropertyInfo(alias="moveChanges")]
