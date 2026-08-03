# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import List
from typing_extensions import TypeAlias

from .todo import Todo

__all__ = ["SessionTodoResponse"]

SessionTodoResponse: TypeAlias = List[Todo]
