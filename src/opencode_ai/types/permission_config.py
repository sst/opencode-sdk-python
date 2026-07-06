# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "PermissionActionConfig",
    "PermissionRuleConfig",
    "PermissionConfigObject",
    "PermissionConfig",
]

PermissionActionConfig: TypeAlias = Literal["ask", "allow", "deny"]

PermissionRuleConfig: TypeAlias = Union[PermissionActionConfig, Dict[str, PermissionActionConfig]]


class PermissionConfigObject(BaseModel):
    bash: Optional[PermissionRuleConfig] = None

    doom_loop: Optional[PermissionActionConfig] = None

    edit: Optional[PermissionRuleConfig] = None

    external_directory: Optional[PermissionRuleConfig] = None

    glob: Optional[PermissionRuleConfig] = None

    grep: Optional[PermissionRuleConfig] = None

    list: Optional[PermissionRuleConfig] = None

    lsp: Optional[PermissionRuleConfig] = None

    question: Optional[PermissionActionConfig] = None

    read: Optional[PermissionRuleConfig] = None

    skill: Optional[PermissionRuleConfig] = None

    task: Optional[PermissionRuleConfig] = None

    todowrite: Optional[PermissionActionConfig] = None

    webfetch: Optional[PermissionActionConfig] = None

    websearch: Optional[PermissionActionConfig] = None

    __pydantic_extra__: Dict[str, PermissionRuleConfig] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> PermissionRuleConfig: ...


PermissionConfig: TypeAlias = Union[PermissionActionConfig, PermissionConfigObject]
