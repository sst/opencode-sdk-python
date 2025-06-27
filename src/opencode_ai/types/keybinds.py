# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Keybinds"]


class Keybinds(BaseModel):
    app_exit: Optional[str] = None
    """Exit the application"""

    editor_open: Optional[str] = None
    """Open external editor"""

    help: Optional[str] = None
    """Show help dialog"""

    history_next: Optional[str] = None
    """Navigate to next history item"""

    history_previous: Optional[str] = None
    """Navigate to previous history item"""

    input_clear: Optional[str] = None
    """Clear input field"""

    input_newline: Optional[str] = None
    """Insert newline in input"""

    input_paste: Optional[str] = None
    """Paste from clipboard"""

    input_submit: Optional[str] = None
    """Submit input"""

    leader: Optional[str] = None
    """Leader key for keybind combinations"""

    messages_first: Optional[str] = None
    """Navigate to first message"""

    messages_half_page_down: Optional[str] = None
    """Scroll messages down by half page"""

    messages_half_page_up: Optional[str] = None
    """Scroll messages up by half page"""

    messages_last: Optional[str] = None
    """Navigate to last message"""

    messages_next: Optional[str] = None
    """Navigate to next message"""

    messages_page_down: Optional[str] = None
    """Scroll messages down by one page"""

    messages_page_up: Optional[str] = None
    """Scroll messages up by one page"""

    messages_previous: Optional[str] = None
    """Navigate to previous message"""

    api_model_list: Optional[str] = FieldInfo(alias="model_list", default=None)
    """List available models"""

    project_init: Optional[str] = None
    """Initialize project configuration"""

    session_compact: Optional[str] = None
    """Toggle compact mode for session"""

    session_interrupt: Optional[str] = None
    """Interrupt current session"""

    session_list: Optional[str] = None
    """List all sessions"""

    session_new: Optional[str] = None
    """Create a new session"""

    session_share: Optional[str] = None
    """Share current session"""

    theme_list: Optional[str] = None
    """List available themes"""

    tool_details: Optional[str] = None
    """Show tool details"""
