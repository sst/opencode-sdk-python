# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from .._models import BaseModel

__all__ = ["QuestionOption"]


class QuestionOption(BaseModel):
    description: str

    label: str
