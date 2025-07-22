# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["KeybindsConfig"]


class KeybindsConfig(BaseModel):
    app_exit: str
    """Exit the application"""

    app_help: str
    """Show help dialog"""

    editor_open: str
    """Open external editor"""

    file_close: str
    """Close file"""

    file_diff_toggle: str
    """Split/unified diff"""

    file_list: str
    """List files"""

    file_search: str
    """Search file"""

    input_clear: str
    """Clear input field"""

    input_newline: str
    """Insert newline in input"""

    input_paste: str
    """Paste from clipboard"""

    input_submit: str
    """Submit input"""

    leader: str
    """Leader key for keybind combinations"""

    messages_copy: str
    """Copy message"""

    messages_first: str
    """Navigate to first message"""

    messages_half_page_down: str
    """Scroll messages down by half page"""

    messages_half_page_up: str
    """Scroll messages up by half page"""

    messages_last: str
    """Navigate to last message"""

    messages_layout_toggle: str
    """Toggle layout"""

    messages_next: str
    """Navigate to next message"""

    messages_page_down: str
    """Scroll messages down by one page"""

    messages_page_up: str
    """Scroll messages up by one page"""

    messages_previous: str
    """Navigate to previous message"""

    messages_redo: str
    """Redo message"""

    messages_revert: str
    """@deprecated use messages_undo. Revert message"""

    messages_undo: str
    """Undo message"""

    api_model_list: str = FieldInfo(alias="model_list")
    """List available models"""

    project_init: str
    """Create/update AGENTS.md"""

    session_compact: str
    """Compact the session"""

    session_export: str
    """Export session to editor"""

    session_interrupt: str
    """Interrupt current session"""

    session_list: str
    """List all sessions"""

    session_new: str
    """Create a new session"""

    session_share: str
    """Share current session"""

    session_unshare: str
    """Unshare current session"""

    switch_mode: str
    """Next mode"""

    switch_mode_reverse: str
    """Previous Mode"""

    theme_list: str
    """List available themes"""

    tool_details: str
    """Toggle tool details"""
