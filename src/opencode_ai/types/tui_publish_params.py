# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "TuiPublishParams",
    "EventTuiPromptAppend",
    "EventTuiPromptAppendProperties",
    "EventTuiCommandExecute",
    "EventTuiCommandExecuteProperties",
    "EventTuiToastShow",
    "EventTuiToastShowProperties",
    "EventTuiSessionSelect",
    "EventTuiSessionSelectProperties",
]


class EventTuiPromptAppendProperties(TypedDict, total=False):
    text: Required[str]


class EventTuiPromptAppend(TypedDict, total=False):
    type: Required[Literal["tui.prompt.append"]]

    properties: Required[EventTuiPromptAppendProperties]


class EventTuiCommandExecuteProperties(TypedDict, total=False):
    command: Required[
        Union[
            Literal[
                "session.list",
                "session.new",
                "session.share",
                "session.interrupt",
                "session.compact",
                "session.page.up",
                "session.page.down",
                "session.line.up",
                "session.line.down",
                "session.half.page.up",
                "session.half.page.down",
                "session.first",
                "session.last",
                "prompt.clear",
                "prompt.submit",
                "agent.cycle",
            ],
            str,
        ]
    ]


class EventTuiCommandExecute(TypedDict, total=False):
    type: Required[Literal["tui.command.execute"]]

    properties: Required[EventTuiCommandExecuteProperties]


class EventTuiToastShowProperties(TypedDict, total=False):
    message: Required[str]

    variant: Required[Literal["info", "success", "warning", "error"]]

    duration: int

    title: str


class EventTuiToastShow(TypedDict, total=False):
    type: Required[Literal["tui.toast.show"]]

    properties: Required[EventTuiToastShowProperties]


class EventTuiSessionSelectProperties(TypedDict, total=False):
    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]
    """Session ID to navigate to"""


class EventTuiSessionSelect(TypedDict, total=False):
    type: Required[Literal["tui.session.select"]]

    properties: Required[EventTuiSessionSelectProperties]


TuiPublishParams: TypeAlias = Union[
    EventTuiPromptAppend, EventTuiCommandExecute, EventTuiToastShow, EventTuiSessionSelect
]
