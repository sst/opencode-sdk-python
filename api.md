# Shared Types

```python
from opencode.types import ProviderAuthError, UnknownError
```

# Event

Types:

```python
from opencode.types import EventListResponse
```

Methods:

- <code title="get /event">client.event.<a href="./src/opencode/resources/event.py">list</a>() -> <a href="./src/opencode/types/event_list_response.py">EventListResponse</a></code>

# App

Types:

```python
from opencode.types import App, AppInitResponse
```

Methods:

- <code title="get /app">client.app.<a href="./src/opencode/resources/app.py">get</a>() -> <a href="./src/opencode/types/app.py">App</a></code>
- <code title="post /app/init">client.app.<a href="./src/opencode/resources/app.py">init</a>() -> <a href="./src/opencode/types/app_init_response.py">AppInitResponse</a></code>

# File

Types:

```python
from opencode.types import FileSearchResponse
```

Methods:

- <code title="get /file">client.file.<a href="./src/opencode/resources/file.py">search</a>(\*\*<a href="src/opencode/types/file_search_params.py">params</a>) -> <a href="./src/opencode/types/file_search_response.py">FileSearchResponse</a></code>

# Config

Types:

```python
from opencode.types import (
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

- <code title="get /config">client.config.<a href="./src/opencode/resources/config.py">get</a>() -> <a href="./src/opencode/types/config.py">Config</a></code>
- <code title="get /config/providers">client.config.<a href="./src/opencode/resources/config.py">providers</a>() -> <a href="./src/opencode/types/config_providers_response.py">ConfigProvidersResponse</a></code>

# Session

Types:

```python
from opencode.types import (
    FilePart,
    Message,
    MessagePart,
    ReasoningPart,
    Session,
    SourceURLPart,
    StepStartPart,
    TextPart,
    ToolCall,
    ToolInvocationPart,
    ToolPartialCall,
    ToolResult,
    SessionListResponse,
    SessionDeleteResponse,
    SessionAbortResponse,
    SessionInitResponse,
    SessionMessagesResponse,
    SessionSummarizeResponse,
)
```

Methods:

- <code title="post /session">client.session.<a href="./src/opencode/resources/session.py">create</a>() -> <a href="./src/opencode/types/session.py">Session</a></code>
- <code title="get /session">client.session.<a href="./src/opencode/resources/session.py">list</a>() -> <a href="./src/opencode/types/session_list_response.py">SessionListResponse</a></code>
- <code title="delete /session/{id}">client.session.<a href="./src/opencode/resources/session.py">delete</a>(id) -> <a href="./src/opencode/types/session_delete_response.py">SessionDeleteResponse</a></code>
- <code title="post /session/{id}/abort">client.session.<a href="./src/opencode/resources/session.py">abort</a>(id) -> <a href="./src/opencode/types/session_abort_response.py">SessionAbortResponse</a></code>
- <code title="post /session/{id}/message">client.session.<a href="./src/opencode/resources/session.py">chat</a>(id, \*\*<a href="src/opencode/types/session_chat_params.py">params</a>) -> <a href="./src/opencode/types/message.py">Message</a></code>
- <code title="post /session/{id}/init">client.session.<a href="./src/opencode/resources/session.py">init</a>(id, \*\*<a href="src/opencode/types/session_init_params.py">params</a>) -> <a href="./src/opencode/types/session_init_response.py">SessionInitResponse</a></code>
- <code title="get /session/{id}/message">client.session.<a href="./src/opencode/resources/session.py">messages</a>(id) -> <a href="./src/opencode/types/session_messages_response.py">SessionMessagesResponse</a></code>
- <code title="post /session/{id}/share">client.session.<a href="./src/opencode/resources/session.py">share</a>(id) -> <a href="./src/opencode/types/session.py">Session</a></code>
- <code title="post /session/{id}/summarize">client.session.<a href="./src/opencode/resources/session.py">summarize</a>(id, \*\*<a href="src/opencode/types/session_summarize_params.py">params</a>) -> <a href="./src/opencode/types/session_summarize_response.py">SessionSummarizeResponse</a></code>
- <code title="delete /session/{id}/share">client.session.<a href="./src/opencode/resources/session.py">unshare</a>(id) -> <a href="./src/opencode/types/session.py">Session</a></code>
