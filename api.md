# Shared Types

```python
from opencode_ai.types import MessageAbortedError, ProviderAuthError, UnknownError
```

# Event

Types:

```python
from opencode_ai.types import EventListResponse
```

Methods:

- <code title="get /event">client.event.<a href="./src/opencode_ai/resources/event.py">list</a>(\*\*<a href="src/opencode_ai/types/event_list_params.py">params</a>) -> <a href="./src/opencode_ai/types/event_list_response.py">EventListResponse</a></code>

# Path

Types:

```python
from opencode_ai.types import Path
```

Methods:

- <code title="get /path">client.path.<a href="./src/opencode_ai/resources/path.py">get</a>(\*\*<a href="src/opencode_ai/types/path_get_params.py">params</a>) -> <a href="./src/opencode_ai/types/path.py">Path</a></code>

# App

Types:

```python
from opencode_ai.types import Model, Provider, AppLogResponse, AppProvidersResponse
```

Methods:

- <code title="post /log">client.app.<a href="./src/opencode_ai/resources/app.py">log</a>(\*\*<a href="src/opencode_ai/types/app_log_params.py">params</a>) -> <a href="./src/opencode_ai/types/app_log_response.py">AppLogResponse</a></code>
- <code title="get /config/providers">client.app.<a href="./src/opencode_ai/resources/app.py">providers</a>(\*\*<a href="src/opencode_ai/types/app_providers_params.py">params</a>) -> <a href="./src/opencode_ai/types/app_providers_response.py">AppProvidersResponse</a></code>

# Agent

Types:

```python
from opencode_ai.types import Agent, AgentListResponse
```

Methods:

- <code title="get /agent">client.agent.<a href="./src/opencode_ai/resources/agent.py">list</a>(\*\*<a href="src/opencode_ai/types/agent_list_params.py">params</a>) -> <a href="./src/opencode_ai/types/agent_list_response.py">AgentListResponse</a></code>

# Find

Types:

```python
from opencode_ai.types import Symbol, FindFilesResponse, FindSymbolsResponse, FindTextResponse
```

Methods:

- <code title="get /find/file">client.find.<a href="./src/opencode_ai/resources/find.py">files</a>(\*\*<a href="src/opencode_ai/types/find_files_params.py">params</a>) -> <a href="./src/opencode_ai/types/find_files_response.py">FindFilesResponse</a></code>
- <code title="get /find/symbol">client.find.<a href="./src/opencode_ai/resources/find.py">symbols</a>(\*\*<a href="src/opencode_ai/types/find_symbols_params.py">params</a>) -> <a href="./src/opencode_ai/types/find_symbols_response.py">FindSymbolsResponse</a></code>
- <code title="get /find">client.find.<a href="./src/opencode_ai/resources/find.py">text</a>(\*\*<a href="src/opencode_ai/types/find_text_params.py">params</a>) -> <a href="./src/opencode_ai/types/find_text_response.py">FindTextResponse</a></code>

# File

Types:

```python
from opencode_ai.types import File, FileNode, FileListResponse, FileReadResponse, FileStatusResponse
```

Methods:

- <code title="get /file">client.file.<a href="./src/opencode_ai/resources/file.py">list</a>(\*\*<a href="src/opencode_ai/types/file_list_params.py">params</a>) -> <a href="./src/opencode_ai/types/file_list_response.py">FileListResponse</a></code>
- <code title="get /file/content">client.file.<a href="./src/opencode_ai/resources/file.py">read</a>(\*\*<a href="src/opencode_ai/types/file_read_params.py">params</a>) -> <a href="./src/opencode_ai/types/file_read_response.py">FileReadResponse</a></code>
- <code title="get /file/status">client.file.<a href="./src/opencode_ai/resources/file.py">status</a>(\*\*<a href="src/opencode_ai/types/file_status_params.py">params</a>) -> <a href="./src/opencode_ai/types/file_status_response.py">FileStatusResponse</a></code>

# Config

Types:

```python
from opencode_ai.types import Config, KeybindsConfig, McpLocalConfig, McpRemoteConfig
```

Methods:

- <code title="get /config">client.config.<a href="./src/opencode_ai/resources/config.py">get</a>(\*\*<a href="src/opencode_ai/types/config_get_params.py">params</a>) -> <a href="./src/opencode_ai/types/config.py">Config</a></code>

# Command

Types:

```python
from opencode_ai.types import Command, CommandListResponse
```

Methods:

- <code title="get /command">client.command.<a href="./src/opencode_ai/resources/command.py">list</a>(\*\*<a href="src/opencode_ai/types/command_list_params.py">params</a>) -> <a href="./src/opencode_ai/types/command_list_response.py">CommandListResponse</a></code>

# Project

Types:

```python
from opencode_ai.types import Project, ProjectListResponse
```

Methods:

- <code title="get /project">client.project.<a href="./src/opencode_ai/resources/project.py">list</a>(\*\*<a href="src/opencode_ai/types/project_list_params.py">params</a>) -> <a href="./src/opencode_ai/types/project_list_response.py">ProjectListResponse</a></code>
- <code title="get /project/current">client.project.<a href="./src/opencode_ai/resources/project.py">current</a>(\*\*<a href="src/opencode_ai/types/project_current_params.py">params</a>) -> <a href="./src/opencode_ai/types/project.py">Project</a></code>

# Session

Types:

```python
from opencode_ai.types import (
    AgentPart,
    AgentPartInput,
    AssistantMessage,
    FilePart,
    FilePartInput,
    FilePartSource,
    FilePartSourceText,
    FileSource,
    Message,
    Part,
    ReasoningPart,
    Session,
    SnapshotPart,
    StepFinishPart,
    StepStartPart,
    SymbolSource,
    TextPart,
    TextPartInput,
    ToolPart,
    ToolStateCompleted,
    ToolStateError,
    ToolStatePending,
    ToolStateRunning,
    UserMessage,
    SessionListResponse,
    SessionDeleteResponse,
    SessionAbortResponse,
    SessionChildrenResponse,
    SessionCommandResponse,
    SessionInitResponse,
    SessionMessageResponse,
    SessionMessagesResponse,
    SessionPromptResponse,
    SessionSummarizeResponse,
)
```

Methods:

- <code title="post /session">client.session.<a href="./src/opencode_ai/resources/session/session.py">create</a>(\*\*<a href="src/opencode_ai/types/session_create_params.py">params</a>) -> <a href="./src/opencode_ai/types/session/session.py">Session</a></code>
- <code title="patch /session/{id}">client.session.<a href="./src/opencode_ai/resources/session/session.py">update</a>(id, \*\*<a href="src/opencode_ai/types/session_update_params.py">params</a>) -> <a href="./src/opencode_ai/types/session/session.py">Session</a></code>
- <code title="get /session">client.session.<a href="./src/opencode_ai/resources/session/session.py">list</a>(\*\*<a href="src/opencode_ai/types/session_list_params.py">params</a>) -> <a href="./src/opencode_ai/types/session_list_response.py">SessionListResponse</a></code>
- <code title="delete /session/{id}">client.session.<a href="./src/opencode_ai/resources/session/session.py">delete</a>(id, \*\*<a href="src/opencode_ai/types/session_delete_params.py">params</a>) -> <a href="./src/opencode_ai/types/session_delete_response.py">SessionDeleteResponse</a></code>
- <code title="post /session/{id}/abort">client.session.<a href="./src/opencode_ai/resources/session/session.py">abort</a>(id, \*\*<a href="src/opencode_ai/types/session_abort_params.py">params</a>) -> <a href="./src/opencode_ai/types/session_abort_response.py">SessionAbortResponse</a></code>
- <code title="get /session/{id}/children">client.session.<a href="./src/opencode_ai/resources/session/session.py">children</a>(id, \*\*<a href="src/opencode_ai/types/session_children_params.py">params</a>) -> <a href="./src/opencode_ai/types/session_children_response.py">SessionChildrenResponse</a></code>
- <code title="post /session/{id}/command">client.session.<a href="./src/opencode_ai/resources/session/session.py">command</a>(id, \*\*<a href="src/opencode_ai/types/session_command_params.py">params</a>) -> <a href="./src/opencode_ai/types/session_command_response.py">SessionCommandResponse</a></code>
- <code title="get /session/{id}">client.session.<a href="./src/opencode_ai/resources/session/session.py">get</a>(id, \*\*<a href="src/opencode_ai/types/session_get_params.py">params</a>) -> <a href="./src/opencode_ai/types/session/session.py">Session</a></code>
- <code title="post /session/{id}/init">client.session.<a href="./src/opencode_ai/resources/session/session.py">init</a>(id, \*\*<a href="src/opencode_ai/types/session_init_params.py">params</a>) -> <a href="./src/opencode_ai/types/session_init_response.py">SessionInitResponse</a></code>
- <code title="get /session/{id}/message/{messageID}">client.session.<a href="./src/opencode_ai/resources/session/session.py">message</a>(message_id, \*, id, \*\*<a href="src/opencode_ai/types/session_message_params.py">params</a>) -> <a href="./src/opencode_ai/types/session_message_response.py">SessionMessageResponse</a></code>
- <code title="get /session/{id}/message">client.session.<a href="./src/opencode_ai/resources/session/session.py">messages</a>(id, \*\*<a href="src/opencode_ai/types/session_messages_params.py">params</a>) -> <a href="./src/opencode_ai/types/session_messages_response.py">SessionMessagesResponse</a></code>
- <code title="post /session/{id}/message">client.session.<a href="./src/opencode_ai/resources/session/session.py">prompt</a>(id, \*\*<a href="src/opencode_ai/types/session_prompt_params.py">params</a>) -> <a href="./src/opencode_ai/types/session_prompt_response.py">SessionPromptResponse</a></code>
- <code title="post /session/{id}/revert">client.session.<a href="./src/opencode_ai/resources/session/session.py">revert</a>(id, \*\*<a href="src/opencode_ai/types/session_revert_params.py">params</a>) -> <a href="./src/opencode_ai/types/session/session.py">Session</a></code>
- <code title="post /session/{id}/share">client.session.<a href="./src/opencode_ai/resources/session/session.py">share</a>(id, \*\*<a href="src/opencode_ai/types/session_share_params.py">params</a>) -> <a href="./src/opencode_ai/types/session/session.py">Session</a></code>
- <code title="post /session/{id}/shell">client.session.<a href="./src/opencode_ai/resources/session/session.py">shell</a>(id, \*\*<a href="src/opencode_ai/types/session_shell_params.py">params</a>) -> <a href="./src/opencode_ai/types/assistant_message.py">AssistantMessage</a></code>
- <code title="post /session/{id}/summarize">client.session.<a href="./src/opencode_ai/resources/session/session.py">summarize</a>(id, \*\*<a href="src/opencode_ai/types/session_summarize_params.py">params</a>) -> <a href="./src/opencode_ai/types/session_summarize_response.py">SessionSummarizeResponse</a></code>
- <code title="post /session/{id}/unrevert">client.session.<a href="./src/opencode_ai/resources/session/session.py">unrevert</a>(id, \*\*<a href="src/opencode_ai/types/session_unrevert_params.py">params</a>) -> <a href="./src/opencode_ai/types/session/session.py">Session</a></code>
- <code title="delete /session/{id}/share">client.session.<a href="./src/opencode_ai/resources/session/session.py">unshare</a>(id, \*\*<a href="src/opencode_ai/types/session_unshare_params.py">params</a>) -> <a href="./src/opencode_ai/types/session/session.py">Session</a></code>

## Permissions

Types:

```python
from opencode_ai.types.session import Permission, PermissionRespondResponse
```

Methods:

- <code title="post /session/{id}/permissions/{permissionID}">client.session.permissions.<a href="./src/opencode_ai/resources/session/permissions.py">respond</a>(permission_id, \*, id, \*\*<a href="src/opencode_ai/types/session/permission_respond_params.py">params</a>) -> <a href="./src/opencode_ai/types/session/permission_respond_response.py">PermissionRespondResponse</a></code>

# Tui

Types:

```python
from opencode_ai.types import (
    TuiAppendPromptResponse,
    TuiClearPromptResponse,
    TuiExecuteCommandResponse,
    TuiOpenHelpResponse,
    TuiOpenModelsResponse,
    TuiOpenSessionsResponse,
    TuiOpenThemesResponse,
    TuiShowToastResponse,
    TuiSubmitPromptResponse,
)
```

Methods:

- <code title="post /tui/append-prompt">client.tui.<a href="./src/opencode_ai/resources/tui.py">append_prompt</a>(\*\*<a href="src/opencode_ai/types/tui_append_prompt_params.py">params</a>) -> <a href="./src/opencode_ai/types/tui_append_prompt_response.py">TuiAppendPromptResponse</a></code>
- <code title="post /tui/clear-prompt">client.tui.<a href="./src/opencode_ai/resources/tui.py">clear_prompt</a>(\*\*<a href="src/opencode_ai/types/tui_clear_prompt_params.py">params</a>) -> <a href="./src/opencode_ai/types/tui_clear_prompt_response.py">TuiClearPromptResponse</a></code>
- <code title="post /tui/execute-command">client.tui.<a href="./src/opencode_ai/resources/tui.py">execute_command</a>(\*\*<a href="src/opencode_ai/types/tui_execute_command_params.py">params</a>) -> <a href="./src/opencode_ai/types/tui_execute_command_response.py">TuiExecuteCommandResponse</a></code>
- <code title="post /tui/open-help">client.tui.<a href="./src/opencode_ai/resources/tui.py">open_help</a>(\*\*<a href="src/opencode_ai/types/tui_open_help_params.py">params</a>) -> <a href="./src/opencode_ai/types/tui_open_help_response.py">TuiOpenHelpResponse</a></code>
- <code title="post /tui/open-models">client.tui.<a href="./src/opencode_ai/resources/tui.py">open_models</a>(\*\*<a href="src/opencode_ai/types/tui_open_models_params.py">params</a>) -> <a href="./src/opencode_ai/types/tui_open_models_response.py">TuiOpenModelsResponse</a></code>
- <code title="post /tui/open-sessions">client.tui.<a href="./src/opencode_ai/resources/tui.py">open_sessions</a>(\*\*<a href="src/opencode_ai/types/tui_open_sessions_params.py">params</a>) -> <a href="./src/opencode_ai/types/tui_open_sessions_response.py">TuiOpenSessionsResponse</a></code>
- <code title="post /tui/open-themes">client.tui.<a href="./src/opencode_ai/resources/tui.py">open_themes</a>(\*\*<a href="src/opencode_ai/types/tui_open_themes_params.py">params</a>) -> <a href="./src/opencode_ai/types/tui_open_themes_response.py">TuiOpenThemesResponse</a></code>
- <code title="post /tui/show-toast">client.tui.<a href="./src/opencode_ai/resources/tui.py">show_toast</a>(\*\*<a href="src/opencode_ai/types/tui_show_toast_params.py">params</a>) -> <a href="./src/opencode_ai/types/tui_show_toast_response.py">TuiShowToastResponse</a></code>
- <code title="post /tui/submit-prompt">client.tui.<a href="./src/opencode_ai/resources/tui.py">submit_prompt</a>(\*\*<a href="src/opencode_ai/types/tui_submit_prompt_params.py">params</a>) -> <a href="./src/opencode_ai/types/tui_submit_prompt_response.py">TuiSubmitPromptResponse</a></code>
