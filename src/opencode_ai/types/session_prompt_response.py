# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import List

from .part import Part
from .._models import BaseModel
from .assistant_message import AssistantMessage

__all__ = ["SessionPromptResponse"]


class SessionPromptResponse(BaseModel):
    info: AssistantMessage

    parts: List[Part]
