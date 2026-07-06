# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "ProviderAuthMethod",
    "Prompt",
    "PromptProviderAuthMethodPromptText",
    "PromptProviderAuthMethodPromptTextWhen",
    "PromptProviderAuthMethodPromptSelect",
    "PromptProviderAuthMethodPromptSelectOption",
    "PromptProviderAuthMethodPromptSelectWhen",
]


class PromptProviderAuthMethodPromptTextWhen(BaseModel):
    key: str

    op: Literal["eq", "neq"]

    value: str


class PromptProviderAuthMethodPromptText(BaseModel):
    key: str

    message: str

    type: Literal["text"]

    placeholder: Optional[str] = None

    when: Optional[PromptProviderAuthMethodPromptTextWhen] = None


class PromptProviderAuthMethodPromptSelectOption(BaseModel):
    label: str

    value: str

    hint: Optional[str] = None


class PromptProviderAuthMethodPromptSelectWhen(BaseModel):
    key: str

    op: Literal["eq", "neq"]

    value: str


class PromptProviderAuthMethodPromptSelect(BaseModel):
    key: str

    message: str

    options: List[PromptProviderAuthMethodPromptSelectOption]

    type: Literal["select"]

    when: Optional[PromptProviderAuthMethodPromptSelectWhen] = None


Prompt: TypeAlias = Annotated[
    Union[PromptProviderAuthMethodPromptText, PromptProviderAuthMethodPromptSelect],
    PropertyInfo(discriminator="type"),
]


class ProviderAuthMethod(BaseModel):
    label: str

    type: Literal["oauth", "api"]

    prompts: Optional[List[Prompt]] = None
