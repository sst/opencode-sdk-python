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
from opencode_ai.types import Config, KeybindsConfig, McpLocalConfig, McpRemoteConfig, ModeConfig
```

Methods:

- <code title="get /config">client.config.<a href="./src/opencode_ai/resources/config.py">get</a>() -> <a href="./src/opencode_ai/types/config.py">Config</a></code>

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
    UserMessage,
    SessionListResponse,
    SessionDeleteResponse,
    SessionAbortResponse,
    SessionInitResponse,
    SessionMessagesResponse,
    SessionPromptResponse,
    SessionSummarizeResponse,
)
```

Methods:

- <code title="post /session">client.session.<a href="./src/opencode_ai/resources/session.py">create</a>() -> <a href="./src/opencode_ai/types/session.py">Session</a></code>
- <code title="get /session">client.session.<a href="./src/opencode_ai/resources/session.py">list</a>(\*\*<a href="src/opencode_ai/types/session_list_params.py">params</a>) -> <a href="./src/opencode_ai/types/session_list_response.py">SessionListResponse</a></code>
- <code title="delete /session/{id}">client.session.<a href="./src/opencode_ai/resources/session.py">delete</a>(id) -> <a href="./src/opencode_ai/types/session_delete_response.py">SessionDeleteResponse</a></code>
- <code title="post /session/{id}/abort">client.session.<a href="./src/opencode_ai/resources/session.py">abort</a>(id) -> <a href="./src/opencode_ai/types/session_abort_response.py">SessionAbortResponse</a></code>
- <code title="post /session/{id}/message">client.session.<a href="./src/opencode_ai/resources/session.py">prompt</a>(id, \*\*<a href="src/opencode_ai/types/session_prompt_params.py">params</a>) -> <a href="./src/opencode_ai/types/session_prompt_response.py">SessionPromptResponse</a></code>
- <code title="post /session/{id}/init">client.session.<a href="./src/opencode_ai/resources/session.py">init</a>(id, \*\*<a href="src/opencode_ai/types/session_init_params.py">params</a>) -> <a href="./src/opencode_ai/types/session_init_response.py">SessionInitResponse</a></code>
- <code title="get /session/{id}/message">client.session.<a href="./src/opencode_ai/resources/session.py">messages</a>(id, \*\*<a href="src/opencode_ai/types/session_messages_params.py">params</a>) -> <a href="./src/opencode_ai/types/session_messages_response.py">SessionMessagesResponse</a></code>
- <code title="post /session/{id}/revert">client.session.<a href="./src/opencode_ai/resources/session.py">revert</a>(id, \*\*<a href="src/opencode_ai/types/session_revert_params.py">params</a>) -> <a href="./src/opencode_ai/types/session.py">Session</a></code>
- <code title="post /session/{id}/share">client.session.<a href="./src/opencode_ai/resources/session.py">share</a>(id) -> <a href="./src/opencode_ai/types/session.py">Session</a></code>
- <code title="post /session/{id}/summarize">client.session.<a href="./src/opencode_ai/resources/session.py">summarize</a>(id, \*\*<a href="src/opencode_ai/types/session_summarize_params.py">params</a>) -> <a href="./src/opencode_ai/types/session_summarize_response.py">SessionSummarizeResponse</a></code>
- <code title="post /session/{id}/unrevert">client.session.<a href="./src/opencode_ai/resources/session.py">unrevert</a>(id) -> <a href="./src/opencode_ai/types/session.py">Session</a></code>
- <code title="delete /session/{id}/share">client.session.<a href="./src/opencode_ai/resources/session.py">unshare</a>(id) -> <a href="./src/opencode_ai/types/session.py">Session</a></code>

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

# Tui

Types:

```python
from opencode_ai.types import TuiAppendPromptResponse, TuiOpenHelpResponse
```

Methods:

- <code title="post /tui/append-prompt">client.tui.<a href="./src/opencode_ai/resources/tui.py">append_prompt</a>(\*\*<a href="src/opencode_ai/types/tui_append_prompt_params.py">params</a>) -> <a href="./src/opencode_ai/types/tui_append_prompt_response.py">TuiAppendPromptResponse</a></code>
- <code title="post /tui/open-help">client.tui.<a href="./src/opencode_ai/resources/tui.py">open_help</a>() -> <a href="./src/opencode_ai/types/tui_open_help_response.py">TuiOpenHelpResponse</a></code>
