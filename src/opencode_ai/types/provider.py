# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import Dict, List, Optional

from .model import Model
from .._models import BaseModel

__all__ = ["Provider"]


class Provider(BaseModel):
    id: str

    env: List[str]

    models: Dict[str, Model]

    name: str

    api: Optional[str] = None

    npm: Optional[str] = None
