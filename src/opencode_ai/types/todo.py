# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from .._models import BaseModel

__all__ = ["Todo"]


class Todo(BaseModel):
    content: str
    """Brief description of the task"""

    # The spec documents this via a free-text `description` (not a JSON Schema
    # `enum`) as one of "pending", "in_progress", "completed", "cancelled" --
    # modeled as `str` rather than `Literal[...]` to stay spec-accurate.
    status: str

    # Same caveat as `status`: documented as "high", "medium", "low" but not
    # enforced as an `enum` in the schema.
    priority: str
