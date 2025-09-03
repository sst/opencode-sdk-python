# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["KeybindsConfig"]


class KeybindsConfig(BaseModel):
    agent_cycle: str
    """Next agent"""

    agent_cycle_reverse: str
    """Previous agent"""

    agent_list: str
    """List agents"""

    app_exit: str
    """Exit the application"""

    app_help: str
    """Show help dialog"""

    editor_open: str
    """Open external editor"""

    file_close: str
    """@deprecated Close file"""

    file_diff_toggle: str
    """@deprecated Split/unified diff"""

    file_list: str
    """@deprecated Currently not available. List files"""

    file_search: str
    """@deprecated Search file"""

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
    """@deprecated Toggle layout"""

    messages_next: str
    """@deprecated Navigate to next message"""

    messages_page_down: str
    """Scroll messages down by one page"""

    messages_page_up: str
    """Scroll messages up by one page"""

    messages_previous: str
    """@deprecated Navigate to previous message"""

    messages_redo: str
    """Redo message"""

    messages_revert: str
    """@deprecated use messages_undo. Revert message"""

    messages_undo: str
    """Undo message"""

    api_model_cycle_recent: str = FieldInfo(alias="model_cycle_recent")
    """Next recent model"""

    api_model_cycle_recent_reverse: str = FieldInfo(alias="model_cycle_recent_reverse")
    """Previous recent model"""

    api_model_list: str = FieldInfo(alias="model_list")
    """List available models"""

    project_init: str
    """Create/update AGENTS.md"""

    session_child_cycle: str
    """Cycle to next child session"""

    session_child_cycle_reverse: str
    """Cycle to previous child session"""

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

    session_timeline: str
    """Show session timeline"""

    session_unshare: str
    """Unshare current session"""

    switch_agent: str
    """@deprecated use agent_cycle. Next agent"""

    switch_agent_reverse: str
    """@deprecated use agent_cycle_reverse. Previous agent"""

    switch_mode: str
    """@deprecated use agent_cycle. Next mode"""

    switch_mode_reverse: str
    """@deprecated use agent_cycle_reverse. Previous mode"""

    theme_list: str
    """List available themes"""

    thinking_blocks: str
    """Toggle thinking blocks"""

    tool_details: str
    """Toggle tool details"""
