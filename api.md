# Shared Types

```python
from opencode_ai.types import ProviderAuthError, UnknownError
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
from opencode_ai.types import App, AppInitResponse
```

Methods:

- <code title="get /app">client.app.<a href="./src/opencode_ai/resources/app.py">get</a>() -> <a href="./src/opencode_ai/types/app.py">App</a></code>
- <code title="post /app/init">client.app.<a href="./src/opencode_ai/resources/app.py">init</a>() -> <a href="./src/opencode_ai/types/app_init_response.py">AppInitResponse</a></code>

# Find

Types:

```python
from opencode_ai.types import FindFilesResponse, FindSymbolsResponse, FindTextResponse
```

Methods:

- <code title="get /find/file">client.find.<a href="./src/opencode_ai/resources/find.py">files</a>(\*\*<a href="src/opencode_ai/types/find_files_params.py">params</a>) -> <a href="./src/opencode_ai/types/find_files_response.py">FindFilesResponse</a></code>
- <code title="get /find/symbol">client.find.<a href="./src/opencode_ai/resources/find.py">symbols</a>(\*\*<a href="src/opencode_ai/types/find_symbols_params.py">params</a>) -> <a href="./src/opencode_ai/types/find_symbols_response.py">FindSymbolsResponse</a></code>
- <code title="get /find">client.find.<a href="./src/opencode_ai/resources/find.py">text</a>(\*\*<a href="src/opencode_ai/types/find_text_params.py">params</a>) -> <a href="./src/opencode_ai/types/find_text_response.py">FindTextResponse</a></code>

# File

Types:

```python
from opencode_ai.types import FileReadResponse, FileStatusResponse
```

Methods:

- <code title="get /file">client.file.<a href="./src/opencode_ai/resources/file.py">read</a>(\*\*<a href="src/opencode_ai/types/file_read_params.py">params</a>) -> <a href="./src/opencode_ai/types/file_read_response.py">FileReadResponse</a></code>
- <code title="get /file/status">client.file.<a href="./src/opencode_ai/resources/file.py">status</a>() -> <a href="./src/opencode_ai/types/file_status_response.py">FileStatusResponse</a></code>

# Config

Types:

```python
from opencode_ai.types import (
    Config,
    Keybinds,
    McpLocal,
    McpRemote,
    Model,
    Provider,
    ConfigProvidersResponse,
)
```

Methods:

- <code title="get /config">client.config.<a href="./src/opencode_ai/resources/config.py">get</a>() -> <a href="./src/opencode_ai/types/config.py">Config</a></code>
- <code title="get /config/providers">client.config.<a href="./src/opencode_ai/resources/config.py">providers</a>() -> <a href="./src/opencode_ai/types/config_providers_response.py">ConfigProvidersResponse</a></code>

# Session

Types:

```python
from opencode_ai.types import (
    AssistantMessage,
    AssistantMessagePart,
    FilePart,
    Message,
    Session,
    StepStartPart,
    TextPart,
    ToolPart,
    ToolStateCompleted,
    ToolStateError,
    ToolStatePending,
    ToolStateRunning,
    UserMessagePart,
    SessionListResponse,
    SessionDeleteResponse,
    SessionAbortResponse,
    SessionInitResponse,
    SessionMessagesResponse,
    SessionSummarizeResponse,
)
```

Methods:

- <code title="post /session">client.session.<a href="./src/opencode_ai/resources/session.py">create</a>() -> <a href="./src/opencode_ai/types/session.py">Session</a></code>
- <code title="get /session">client.session.<a href="./src/opencode_ai/resources/session.py">list</a>() -> <a href="./src/opencode_ai/types/session_list_response.py">SessionListResponse</a></code>
- <code title="delete /session/{id}">client.session.<a href="./src/opencode_ai/resources/session.py">delete</a>(id) -> <a href="./src/opencode_ai/types/session_delete_response.py">SessionDeleteResponse</a></code>
- <code title="post /session/{id}/abort">client.session.<a href="./src/opencode_ai/resources/session.py">abort</a>(id) -> <a href="./src/opencode_ai/types/session_abort_response.py">SessionAbortResponse</a></code>
- <code title="post /session/{id}/message">client.session.<a href="./src/opencode_ai/resources/session.py">chat</a>(id, \*\*<a href="src/opencode_ai/types/session_chat_params.py">params</a>) -> <a href="./src/opencode_ai/types/assistant_message.py">AssistantMessage</a></code>
- <code title="post /session/{id}/init">client.session.<a href="./src/opencode_ai/resources/session.py">init</a>(id, \*\*<a href="src/opencode_ai/types/session_init_params.py">params</a>) -> <a href="./src/opencode_ai/types/session_init_response.py">SessionInitResponse</a></code>
- <code title="get /session/{id}/message">client.session.<a href="./src/opencode_ai/resources/session.py">messages</a>(id) -> <a href="./src/opencode_ai/types/session_messages_response.py">SessionMessagesResponse</a></code>
- <code title="post /session/{id}/share">client.session.<a href="./src/opencode_ai/resources/session.py">share</a>(id) -> <a href="./src/opencode_ai/types/session.py">Session</a></code>
- <code title="post /session/{id}/summarize">client.session.<a href="./src/opencode_ai/resources/session.py">summarize</a>(id, \*\*<a href="src/opencode_ai/types/session_summarize_params.py">params</a>) -> <a href="./src/opencode_ai/types/session_summarize_response.py">SessionSummarizeResponse</a></code>
- <code title="delete /session/{id}/share">client.session.<a href="./src/opencode_ai/resources/session.py">unshare</a>(id) -> <a href="./src/opencode_ai/types/session.py">Session</a></code>
