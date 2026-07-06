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

- <code title="get /event">client.event.<a href="./src/opencode_ai/resources/event.py">list</a>() -> <a href="./src/opencode_ai/types/event_list_response.py">EventListResponse</a></code>

# App

Types:

```python
from opencode_ai.types import (
    Model,
    Provider,
    AppAgentsResponse,
    AppLogResponse,
    AppProvidersResponse,
    AppSkillsResponse,
)
```

Methods:

- <code title="get /agent">client.app.<a href="./src/opencode_ai/resources/app.py">agents</a>() -> <a href="./src/opencode_ai/types/app_agents_response.py">AppAgentsResponse</a></code>
- <code title="post /log">client.app.<a href="./src/opencode_ai/resources/app.py">log</a>(\*\*<a href="src/opencode_ai/types/app_log_params.py">params</a>) -> <a href="./src/opencode_ai/types/app_log_response.py">AppLogResponse</a></code>
- <code title="get /config/providers">client.app.<a href="./src/opencode_ai/resources/app.py">providers</a>() -> <a href="./src/opencode_ai/types/app_providers_response.py">AppProvidersResponse</a></code>
- <code title="get /skill">client.app.<a href="./src/opencode_ai/resources/app.py">skills</a>() -> <a href="./src/opencode_ai/types/app_skills_response.py">AppSkillsResponse</a></code>

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
from opencode_ai.types import File, FileListResponse, FileContentResponse, FileStatusResponse
```

Methods:

- <code title="get /file">client.file.<a href="./src/opencode_ai/resources/file.py">list</a>(\*\*<a href="src/opencode_ai/types/file_content_params.py">params</a>) -> <a href="./src/opencode_ai/types/file_list_response.py">FileListResponse</a></code>
- <code title="get /file/content">client.file.<a href="./src/opencode_ai/resources/file.py">content</a>(\*\*<a href="src/opencode_ai/types/file_content_params.py">params</a>) -> <a href="./src/opencode_ai/types/file_content_response.py">FileContentResponse</a></code>
- <code title="get /file/status">client.file.<a href="./src/opencode_ai/resources/file.py">status</a>() -> <a href="./src/opencode_ai/types/file_status_response.py">FileStatusResponse</a></code>

# Config

Types:

```python
from opencode_ai.types import (
    AgentConfig,
    Config,
    McpLocalConfig,
    McpRemoteConfig,
    PermissionActionConfig,
    PermissionConfig,
    PermissionConfigObject,
    PermissionRuleConfig,
)
```

Methods:

- <code title="get /config">client.config.<a href="./src/opencode_ai/resources/config.py">get</a>() -> <a href="./src/opencode_ai/types/config.py">Config</a></code>
- <code title="patch /config">client.config.<a href="./src/opencode_ai/resources/config.py">update</a>(\*\*<a href="src/opencode_ai/types/config_update_params.py">params</a>) -> <a href="./src/opencode_ai/types/config.py">Config</a></code>

# Session

Types:

```python
from opencode_ai.types import (
    AgentPart,
    AssistantMessage,
    CompactionPart,
    FilePart,
    FilePartInput,
    FilePartSource,
    FilePartSourceText,
    FileSource,
    Message,
    Part,
    PartUnknown,
    PatchPart,
    ReasoningPart,
    ResourceSource,
    RetryPart,
    Session,
    SnapshotPart,
    StepFinishPart,
    StepStartPart,
    SubtaskPart,
    SymbolSource,
    TextPart,
    TextPartInput,
    ToolPart,
    ToolStateCompleted,
    ToolStateError,
    ToolStatePending,
    ToolStateRunning,
    Todo,
    UserMessage,
    SessionListResponse,
    SessionDeleteResponse,
    SessionAbortResponse,
    SessionInitResponse,
    SessionMessagesResponse,
    SessionPromptResponse,
    SessionSummarizeResponse,
    SessionChildrenResponse,
    SessionCommandResponse,
    SessionDeleteMessageResponse,
    SessionDeletePartResponse,
    SessionDiffResponse,
    SessionMessagesResponseItem,
    SessionRespondPermissionResponse,
    SessionShellResponse,
    SessionStatusResponse,
    SessionTodoResponse,
)
```

Methods:

- <code title="post /session">client.session.<a href="./src/opencode_ai/resources/session.py">create</a>() -> <a href="./src/opencode_ai/types/session.py">Session</a></code>
- <code title="get /session">client.session.<a href="./src/opencode_ai/resources/session.py">list</a>(\*\*<a href="src/opencode_ai/types/session_list_params.py">params</a>) -> <a href="./src/opencode_ai/types/session_list_response.py">SessionListResponse</a></code>
- <code title="get /session/{id}">client.session.<a href="./src/opencode_ai/resources/session.py">get</a>(id) -> <a href="./src/opencode_ai/types/session.py">Session</a></code>
- <code title="patch /session/{id}">client.session.<a href="./src/opencode_ai/resources/session.py">update</a>(id, \*\*<a href="src/opencode_ai/types/session_update_params.py">params</a>) -> <a href="./src/opencode_ai/types/session.py">Session</a></code>
- <code title="delete /session/{id}">client.session.<a href="./src/opencode_ai/resources/session.py">delete</a>(id) -> <a href="./src/opencode_ai/types/session_delete_response.py">SessionDeleteResponse</a></code>
- <code title="post /session/{id}/abort">client.session.<a href="./src/opencode_ai/resources/session.py">abort</a>(id) -> <a href="./src/opencode_ai/types/session_abort_response.py">SessionAbortResponse</a></code>
- <code title="get /session/{id}/children">client.session.<a href="./src/opencode_ai/resources/session.py">children</a>(id) -> <a href="./src/opencode_ai/types/session_children_response.py">SessionChildrenResponse</a></code>
- <code title="post /session/{id}/command">client.session.<a href="./src/opencode_ai/resources/session.py">command</a>(id, \*\*<a href="src/opencode_ai/types/session_command_params.py">params</a>) -> <a href="./src/opencode_ai/types/session_command_response.py">SessionCommandResponse</a></code>
- <code title="delete /session/{id}/message/{message_id}">client.session.<a href="./src/opencode_ai/resources/session.py">delete_message</a>(id, \*, message_id) -> <a href="./src/opencode_ai/types/session_delete_message_response.py">SessionDeleteMessageResponse</a></code>
- <code title="delete /session/{id}/message/{message_id}/part/{part_id}">client.session.<a href="./src/opencode_ai/resources/session.py">delete_part</a>(id, \*, message_id, part_id) -> <a href="./src/opencode_ai/types/session_delete_part_response.py">SessionDeletePartResponse</a></code>
- <code title="get /session/{id}/diff">client.session.<a href="./src/opencode_ai/resources/session.py">diff</a>(id, \*\*<a href="src/opencode_ai/types/session_diff_params.py">params</a>) -> <a href="./src/opencode_ai/types/session_diff_response.py">SessionDiffResponse</a></code>
- <code title="post /session/{id}/fork">client.session.<a href="./src/opencode_ai/resources/session.py">fork</a>(id, \*\*<a href="src/opencode_ai/types/session_fork_params.py">params</a>) -> <a href="./src/opencode_ai/types/session.py">Session</a></code>
- <code title="get /session/{id}/message/{message_id}">client.session.<a href="./src/opencode_ai/resources/session.py">get_message</a>(id, \*, message_id) -> <a href="./src/opencode_ai/types/session_messages_response.py">SessionMessagesResponseItem</a></code>
- <code title="post /session/{id}/message">client.session.<a href="./src/opencode_ai/resources/session.py">prompt</a>(id, \*\*<a href="src/opencode_ai/types/session_prompt_params.py">params</a>) -> <a href="./src/opencode_ai/types/session_prompt_response.py">SessionPromptResponse</a></code>
- <code title="post /session/{id}/prompt_async">client.session.<a href="./src/opencode_ai/resources/session.py">prompt_async</a>(id, \*\*<a href="src/opencode_ai/types/session_prompt_async_params.py">params</a>) -> None</code>
- <code title="post /session/{id}/permissions/{permission_id}">client.session.<a href="./src/opencode_ai/resources/session.py">respond_permission</a>(id, \*, permission_id, \*\*<a href="src/opencode_ai/types/session_respond_permission_params.py">params</a>) -> <a href="./src/opencode_ai/types/session_respond_permission_response.py">SessionRespondPermissionResponse</a></code>
- <code title="post /session/{id}/init">client.session.<a href="./src/opencode_ai/resources/session.py">init</a>(id, \*\*<a href="src/opencode_ai/types/session_init_params.py">params</a>) -> <a href="./src/opencode_ai/types/session_init_response.py">SessionInitResponse</a></code>
- <code title="get /session/{id}/message">client.session.<a href="./src/opencode_ai/resources/session.py">messages</a>(id, \*\*<a href="src/opencode_ai/types/session_messages_params.py">params</a>) -> <a href="./src/opencode_ai/types/session_messages_response.py">SessionMessagesResponse</a></code>
- <code title="post /session/{id}/revert">client.session.<a href="./src/opencode_ai/resources/session.py">revert</a>(id, \*\*<a href="src/opencode_ai/types/session_revert_params.py">params</a>) -> <a href="./src/opencode_ai/types/session.py">Session</a></code>
- <code title="post /session/{id}/share">client.session.<a href="./src/opencode_ai/resources/session.py">share</a>(id) -> <a href="./src/opencode_ai/types/session.py">Session</a></code>
- <code title="post /session/{id}/shell">client.session.<a href="./src/opencode_ai/resources/session.py">shell</a>(id, \*\*<a href="src/opencode_ai/types/session_shell_params.py">params</a>) -> <a href="./src/opencode_ai/types/session_shell_response.py">SessionShellResponse</a></code>
- <code title="get /session/status">client.session.<a href="./src/opencode_ai/resources/session.py">status</a>() -> <a href="./src/opencode_ai/types/session_status_response.py">SessionStatusResponse</a></code>
- <code title="post /session/{id}/summarize">client.session.<a href="./src/opencode_ai/resources/session.py">summarize</a>(id, \*\*<a href="src/opencode_ai/types/session_summarize_params.py">params</a>) -> <a href="./src/opencode_ai/types/session_summarize_response.py">SessionSummarizeResponse</a></code>
- <code title="get /session/{id}/todo">client.session.<a href="./src/opencode_ai/resources/session.py">todo</a>(id) -> <a href="./src/opencode_ai/types/session_todo_response.py">SessionTodoResponse</a></code>
- <code title="post /session/{id}/unrevert">client.session.<a href="./src/opencode_ai/resources/session.py">unrevert</a>(id) -> <a href="./src/opencode_ai/types/session.py">Session</a></code>
- <code title="delete /session/{id}/share">client.session.<a href="./src/opencode_ai/resources/session.py">unshare</a>(id) -> <a href="./src/opencode_ai/types/session.py">Session</a></code>
- <code title="patch /session/{id}/message/{message_id}/part/{part_id}">client.session.<a href="./src/opencode_ai/resources/session.py">update_part</a>(id, \*, message_id, part_id, \*\*<a href="src/opencode_ai/types/session_update_part_params.py">params</a>) -> <a href="./src/opencode_ai/types/part.py">Part</a></code>

# Project

Types:

```python
from opencode_ai.types import Project, ProjectListResponse, ProjectDirectoriesResponse
```

Methods:

- <code title="get /project">client.project.<a href="./src/opencode_ai/resources/project.py">list</a>() -> <a href="./src/opencode_ai/types/project_list_response.py">ProjectListResponse</a></code>
- <code title="patch /project/{projectID}">client.project.<a href="./src/opencode_ai/resources/project.py">update</a>(project_id, \*\*<a href="src/opencode_ai/types/project_update_params.py">params</a>) -> <a href="./src/opencode_ai/types/project.py">Project</a></code>
- <code title="get /project/current">client.project.<a href="./src/opencode_ai/resources/project.py">current</a>() -> <a href="./src/opencode_ai/types/project.py">Project</a></code>
- <code title="get /project/{projectID}/directories">client.project.<a href="./src/opencode_ai/resources/project.py">directories</a>(project_id) -> <a href="./src/opencode_ai/types/project_directories_response.py">ProjectDirectoriesResponse</a></code>
- <code title="post /project/git/init">client.project.<a href="./src/opencode_ai/resources/project.py">init_git</a>() -> <a href="./src/opencode_ai/types/project.py">Project</a></code>

# Provider

Types:

```python
from opencode_ai.types import (
    ProviderAuthMethod,
    ProviderListResponse,
    ProviderAuthResponse,
    ProviderAuthAuthorization,
    ProviderOAuthCallbackResponse,
)
```

Methods:

- <code title="get /provider">client.provider.<a href="./src/opencode_ai/resources/provider.py">list</a>() -> <a href="./src/opencode_ai/types/provider_list_response.py">ProviderListResponse</a></code>
- <code title="get /provider/auth">client.provider.<a href="./src/opencode_ai/resources/provider.py">auth</a>() -> <a href="./src/opencode_ai/types/provider_auth_response.py">ProviderAuthResponse</a></code>
- <code title="post /provider/{providerID}/oauth/authorize">client.provider.<a href="./src/opencode_ai/resources/provider.py">oauth_authorize</a>(provider_id, \*\*<a href="src/opencode_ai/types/provider_oauth_authorize_params.py">params</a>) -> <a href="./src/opencode_ai/types/provider_auth_authorization.py">ProviderAuthAuthorization</a></code>
- <code title="post /provider/{providerID}/oauth/callback">client.provider.<a href="./src/opencode_ai/resources/provider.py">oauth_callback</a>(provider_id, \*\*<a href="src/opencode_ai/types/provider_oauth_callback_params.py">params</a>) -> <a href="./src/opencode_ai/types/provider_oauth_callback_response.py">ProviderOAuthCallbackResponse</a></code>

# Sync

Types:

```python
from opencode_ai.types import (
    SyncHistoryListResponse,
    SyncReplayResponse,
    SyncStartResponse,
    SyncStealResponse,
)
```

Methods:

- <code title="post /sync/history">client.sync.<a href="./src/opencode_ai/resources/sync.py">history_list</a>(\*\*<a href="src/opencode_ai/types/sync_history_list_params.py">params</a>) -> <a href="./src/opencode_ai/types/sync_history_list_response.py">SyncHistoryListResponse</a></code>
- <code title="post /sync/replay">client.sync.<a href="./src/opencode_ai/resources/sync.py">replay</a>(\*\*<a href="src/opencode_ai/types/sync_replay_params.py">params</a>) -> <a href="./src/opencode_ai/types/sync_replay_response.py">SyncReplayResponse</a></code>
- <code title="post /sync/start">client.sync.<a href="./src/opencode_ai/resources/sync.py">start</a>() -> <a href="./src/opencode_ai/types/sync_start_response.py">SyncStartResponse</a></code>
- <code title="post /sync/steal">client.sync.<a href="./src/opencode_ai/resources/sync.py">steal</a>(\*\*<a href="src/opencode_ai/types/sync_steal_params.py">params</a>) -> <a href="./src/opencode_ai/types/sync_steal_response.py">SyncStealResponse</a></code>

# Mcp

Types:

```python
from opencode_ai.types import (
    MCPStatus,
    MCPStatusConnected,
    MCPStatusDisabled,
    MCPStatusFailed,
    MCPStatusNeedsAuth,
    MCPStatusNeedsClientRegistration,
    McpLocalConfig,
    McpRemoteConfig,
    McpAddResponse,
    McpAuthRemoveResponse,
    McpAuthStartResponse,
    McpConnectResponse,
    McpDisconnectResponse,
    McpStatusResponse,
)
```

Methods:

- <code title="get /mcp">client.mcp.<a href="./src/opencode_ai/resources/mcp.py">status</a>() -> <a href="./src/opencode_ai/types/mcp_status_response.py">McpStatusResponse</a></code>
- <code title="post /mcp">client.mcp.<a href="./src/opencode_ai/resources/mcp.py">add</a>(\*\*<a href="src/opencode_ai/types/mcp_add_params.py">params</a>) -> <a href="./src/opencode_ai/types/mcp_add_response.py">McpAddResponse</a></code>
- <code title="post /mcp/{name}/auth">client.mcp.<a href="./src/opencode_ai/resources/mcp.py">auth_start</a>(name) -> <a href="./src/opencode_ai/types/mcp_auth_start_response.py">McpAuthStartResponse</a></code>
- <code title="delete /mcp/{name}/auth">client.mcp.<a href="./src/opencode_ai/resources/mcp.py">auth_remove</a>(name) -> <a href="./src/opencode_ai/types/mcp_auth_remove_response.py">McpAuthRemoveResponse</a></code>
- <code title="post /mcp/{name}/auth/callback">client.mcp.<a href="./src/opencode_ai/resources/mcp.py">auth_callback</a>(name, \*\*<a href="src/opencode_ai/types/mcp_auth_callback_params.py">params</a>) -> <a href="./src/opencode_ai/types/mcp_status.py">MCPStatus</a></code>
- <code title="post /mcp/{name}/auth/authenticate">client.mcp.<a href="./src/opencode_ai/resources/mcp.py">auth_authenticate</a>(name) -> <a href="./src/opencode_ai/types/mcp_status.py">MCPStatus</a></code>
- <code title="post /mcp/{name}/connect">client.mcp.<a href="./src/opencode_ai/resources/mcp.py">connect</a>(name) -> <a href="./src/opencode_ai/types/mcp_connect_response.py">McpConnectResponse</a></code>
- <code title="post /mcp/{name}/disconnect">client.mcp.<a href="./src/opencode_ai/resources/mcp.py">disconnect</a>(name) -> <a href="./src/opencode_ai/types/mcp_disconnect_response.py">McpDisconnectResponse</a></code>

# Pty

Types:

```python
from opencode_ai.types import (
    Pty,
    PtyListResponse,
    PtyConnectResponse,
    PtyConnectTokenResponse,
    PtyDeleteResponse,
    PtyShellsResponse,
)
```

Methods:

- <code title="get /pty">client.pty.<a href="./src/opencode_ai/resources/pty.py">list</a>() -> <a href="./src/opencode_ai/types/pty_list_response.py">PtyListResponse</a></code>
- <code title="post /pty">client.pty.<a href="./src/opencode_ai/resources/pty.py">create</a>(\*\*<a href="src/opencode_ai/types/pty_create_params.py">params</a>) -> <a href="./src/opencode_ai/types/pty.py">Pty</a></code>
- <code title="get /pty/{ptyID}">client.pty.<a href="./src/opencode_ai/resources/pty.py">retrieve</a>(pty_id) -> <a href="./src/opencode_ai/types/pty.py">Pty</a></code>
- <code title="put /pty/{ptyID}">client.pty.<a href="./src/opencode_ai/resources/pty.py">update</a>(pty_id, \*\*<a href="src/opencode_ai/types/pty_update_params.py">params</a>) -> <a href="./src/opencode_ai/types/pty.py">Pty</a></code>
- <code title="delete /pty/{ptyID}">client.pty.<a href="./src/opencode_ai/resources/pty.py">delete</a>(pty_id) -> <a href="./src/opencode_ai/types/pty_delete_response.py">PtyDeleteResponse</a></code>
- <code title="get /pty/{ptyID}/connect">client.pty.<a href="./src/opencode_ai/resources/pty.py">connect</a>(pty_id, \*\*<a href="src/opencode_ai/types/pty_connect_params.py">params</a>) -> <a href="./src/opencode_ai/types/pty_connect_response.py">PtyConnectResponse</a></code>
- <code title="post /pty/{ptyID}/connect-token">client.pty.<a href="./src/opencode_ai/resources/pty.py">connect_token</a>(pty_id) -> <a href="./src/opencode_ai/types/pty_connect_token_response.py">PtyConnectTokenResponse</a></code>
- <code title="get /pty/shells">client.pty.<a href="./src/opencode_ai/resources/pty.py">shells</a>() -> <a href="./src/opencode_ai/types/pty_shells_response.py">PtyShellsResponse</a></code>

# Tui

Types:

```python
from opencode_ai.types import (
    TuiAppendPromptResponse,
    TuiOpenHelpResponse,
    TuiOpenSessionsResponse,
    TuiOpenThemesResponse,
    TuiOpenModelsResponse,
    TuiSubmitPromptResponse,
    TuiClearPromptResponse,
    TuiExecuteCommandResponse,
    TuiShowToastResponse,
    TuiPublishResponse,
    TuiSelectSessionResponse,
    TuiControlNextResponse,
    TuiControlResponseResponse,
)
```

Methods:

- <code title="post /tui/append-prompt">client.tui.<a href="./src/opencode_ai/resources/tui.py">append_prompt</a>(\*\*<a href="src/opencode_ai/types/tui_append_prompt_params.py">params</a>) -> <a href="./src/opencode_ai/types/tui_append_prompt_response.py">TuiAppendPromptResponse</a></code>
- <code title="post /tui/open-help">client.tui.<a href="./src/opencode_ai/resources/tui.py">open_help</a>() -> <a href="./src/opencode_ai/types/tui_open_help_response.py">TuiOpenHelpResponse</a></code>
- <code title="post /tui/open-sessions">client.tui.<a href="./src/opencode_ai/resources/tui.py">open_sessions</a>() -> <a href="./src/opencode_ai/types/tui_open_sessions_response.py">TuiOpenSessionsResponse</a></code>
- <code title="post /tui/open-themes">client.tui.<a href="./src/opencode_ai/resources/tui.py">open_themes</a>() -> <a href="./src/opencode_ai/types/tui_open_themes_response.py">TuiOpenThemesResponse</a></code>
- <code title="post /tui/open-models">client.tui.<a href="./src/opencode_ai/resources/tui.py">open_models</a>() -> <a href="./src/opencode_ai/types/tui_open_models_response.py">TuiOpenModelsResponse</a></code>
- <code title="post /tui/submit-prompt">client.tui.<a href="./src/opencode_ai/resources/tui.py">submit_prompt</a>() -> <a href="./src/opencode_ai/types/tui_submit_prompt_response.py">TuiSubmitPromptResponse</a></code>
- <code title="post /tui/clear-prompt">client.tui.<a href="./src/opencode_ai/resources/tui.py">clear_prompt</a>() -> <a href="./src/opencode_ai/types/tui_clear_prompt_response.py">TuiClearPromptResponse</a></code>
- <code title="post /tui/execute-command">client.tui.<a href="./src/opencode_ai/resources/tui.py">execute_command</a>(\*\*<a href="src/opencode_ai/types/tui_execute_command_params.py">params</a>) -> <a href="./src/opencode_ai/types/tui_execute_command_response.py">TuiExecuteCommandResponse</a></code>
- <code title="post /tui/show-toast">client.tui.<a href="./src/opencode_ai/resources/tui.py">show_toast</a>(\*\*<a href="src/opencode_ai/types/tui_show_toast_params.py">params</a>) -> <a href="./src/opencode_ai/types/tui_show_toast_response.py">TuiShowToastResponse</a></code>
- <code title="post /tui/publish">client.tui.<a href="./src/opencode_ai/resources/tui.py">publish</a>(\*\*<a href="src/opencode_ai/types/tui_publish_params.py">params</a>) -> <a href="./src/opencode_ai/types/tui_publish_response.py">TuiPublishResponse</a></code>
- <code title="post /tui/select-session">client.tui.<a href="./src/opencode_ai/resources/tui.py">select_session</a>(\*\*<a href="src/opencode_ai/types/tui_select_session_params.py">params</a>) -> <a href="./src/opencode_ai/types/tui_select_session_response.py">TuiSelectSessionResponse</a></code>
- <code title="get /tui/control/next">client.tui.<a href="./src/opencode_ai/resources/tui.py">control_next</a>() -> <a href="./src/opencode_ai/types/tui_control_next_response.py">TuiControlNextResponse</a></code>
- <code title="post /tui/control/response">client.tui.<a href="./src/opencode_ai/resources/tui.py">control_response</a>(\*\*<a href="src/opencode_ai/types/tui_control_response_params.py">params</a>) -> <a href="./src/opencode_ai/types/tui_control_response_response.py">TuiControlResponseResponse</a></code>

# Question

Types:

```python
from opencode_ai.types import (
    QuestionInfo,
    QuestionOption,
    QuestionRequest,
    QuestionTool,
    QuestionListResponse,
    QuestionRejectResponse,
    QuestionReplyResponse,
)
```

Methods:

- <code title="get /question">client.question.<a href="./src/opencode_ai/resources/question.py">list</a>() -> <a href="./src/opencode_ai/types/question_list_response.py">QuestionListResponse</a></code>
- <code title="post /question/{requestID}/reject">client.question.<a href="./src/opencode_ai/resources/question.py">reject</a>(request_id) -> <a href="./src/opencode_ai/types/question_reject_response.py">QuestionRejectResponse</a></code>
- <code title="post /question/{requestID}/reply">client.question.<a href="./src/opencode_ai/resources/question.py">reply</a>(request_id, \*\*<a href="src/opencode_ai/types/question_reply_params.py">params</a>) -> <a href="./src/opencode_ai/types/question_reply_response.py">QuestionReplyResponse</a></code>

# Permission

Types:

```python
from opencode_ai.types import (
    PermissionRequest,
    PermissionListResponse,
    PermissionReplyResponse,
)
```

Methods:

- <code title="get /permission">client.permission.<a href="./src/opencode_ai/resources/permission.py">list</a>() -> <a href="./src/opencode_ai/types/permission_list_response.py">PermissionListResponse</a></code>
- <code title="post /permission/{requestID}/reply">client.permission.<a href="./src/opencode_ai/resources/permission.py">reply</a>(request_id, \*\*<a href="src/opencode_ai/types/permission_reply_params.py">params</a>) -> <a href="./src/opencode_ai/types/permission_reply_response.py">PermissionReplyResponse</a></code>

# Path

Types:

```python
from opencode_ai.types import Path
```

Methods:

- <code title="get /path">client.path.<a href="./src/opencode_ai/resources/path.py">get</a>() -> <a href="./src/opencode_ai/types/path.py">Path</a></code>

# Vcs

Types:

```python
from opencode_ai.types import (
    VcsInfo,
    VcsFileStatus,
    VcsFileDiff,
    VcsStatusResponse,
    VcsDiffResponse,
    VcsApplyResponse,
)
```

Methods:

- <code title="get /vcs">client.vcs.<a href="./src/opencode_ai/resources/vcs.py">get</a>() -> <a href="./src/opencode_ai/types/vcs_info.py">VcsInfo</a></code>
- <code title="post /vcs/apply">client.vcs.<a href="./src/opencode_ai/resources/vcs.py">apply</a>(\*\*<a href="src/opencode_ai/types/vcs_apply_params.py">params</a>) -> <a href="./src/opencode_ai/types/vcs_apply_response.py">VcsApplyResponse</a></code>
- <code title="get /vcs/diff">client.vcs.<a href="./src/opencode_ai/resources/vcs.py">diff</a>(\*\*<a href="src/opencode_ai/types/vcs_diff_params.py">params</a>) -> <a href="./src/opencode_ai/types/vcs_diff_response.py">VcsDiffResponse</a></code>
- <code title="get /vcs/diff/raw">client.vcs.<a href="./src/opencode_ai/resources/vcs.py">diff_raw</a>() -> str</code>
- <code title="get /vcs/status">client.vcs.<a href="./src/opencode_ai/resources/vcs.py">status</a>() -> <a href="./src/opencode_ai/types/vcs_status_response.py">VcsStatusResponse</a></code>

# Command

Types:

```python
from opencode_ai.types import Command, CommandListResponse
```

Methods:

- <code title="get /command">client.command.<a href="./src/opencode_ai/resources/command.py">list</a>() -> <a href="./src/opencode_ai/types/command_list_response.py">CommandListResponse</a></code>

# Lsp

Types:

```python
from opencode_ai.types import LSPStatus, LspStatusResponse
```

Methods:

- <code title="get /lsp">client.lsp.<a href="./src/opencode_ai/resources/lsp.py">status</a>() -> <a href="./src/opencode_ai/types/lsp_status_response.py">LspStatusResponse</a></code>

# Formatter

Types:

```python
from opencode_ai.types import FormatterStatus, FormatterStatusResponse
```

Methods:

- <code title="get /formatter">client.formatter.<a href="./src/opencode_ai/resources/formatter.py">status</a>() -> <a href="./src/opencode_ai/types/formatter_status_response.py">FormatterStatusResponse</a></code>

# Instance

Types:

```python
from opencode_ai.types import InstanceDisposeResponse
```

Methods:

- <code title="post /instance/dispose">client.instance.<a href="./src/opencode_ai/resources/instance.py">dispose</a>() -> bool</code>
