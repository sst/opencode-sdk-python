# Shared Types

```python
from opencode_ai.types import MessageAbortedError, ProviderAuthError, UnknownError
```

<!-- expanded:start -->

<details>
<summary>Expanded definitions (top-level types; referenced subtypes link to source)</summary>

<pre><code>class MessageAbortedError(BaseModel):
    data: object
    name: Literal['MessageAbortedError']</code></pre>

<pre><code>class ProviderAuthError(BaseModel):
    data: <a href="./src/opencode_ai/types/shared/provider_auth_error.py#L12">Data</a>
    name: Literal['ProviderAuthError']</code></pre>

<pre><code>class UnknownError(BaseModel):
    data: <a href="./src/opencode_ai/types/shared/unknown_error.py#L10">Data</a>
    name: Literal['UnknownError']</code></pre>

</details>

<!-- expanded:end -->

# Event

Types:

```python
from opencode_ai.types import EventListResponse
```

<!-- expanded:start -->

<details>
<summary>Expanded definitions (top-level types; referenced subtypes link to source)</summary>

<pre><code>EventListResponse: TypeAlias = Union[
    <a href="./src/opencode_ai/types/event_list_response.py#L2470">EventUnknown</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L288">EventPluginAdded</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L414">EventCatalogModelUpdated</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L428">EventSessionCreated</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L442">EventSessionUpdated</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L456">EventSessionDeleted</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L470">EventMessageUpdated</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L484">EventMessageRemoved</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L500">EventMessagePartUpdated</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L516">EventMessagePartRemoved</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L524">EventModelsDevRefreshed</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L542">EventSessionNextAgentSwitched</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L568">EventSessionNextModelSwitched</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L592">EventSessionNextMoved</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L684">EventSessionNextPrompted</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L776">EventSessionNextPromptAdmitted</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L868">EventSessionNextPromptPromoted</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L886">EventSessionNextContextUpdated</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L904">EventSessionNextSynthetic</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L924">EventSessionNextShellStarted</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L942">EventSessionNextShellEnded</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L972">EventSessionNextStepStarted</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1012">EventSessionNextStepEnded</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1036">EventSessionNextStepFailed</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1054">EventSessionNextTextStarted</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1074">EventSessionNextTextDelta</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1094">EventSessionNextTextEnded</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1114">EventSessionNextReasoningStarted</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1134">EventSessionNextReasoningDelta</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1156">EventSessionNextReasoningEnded</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1176">EventSessionNextToolInputStarted</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1196">EventSessionNextToolInputDelta</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1216">EventSessionNextToolInputEnded</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1246">EventSessionNextToolCalled</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1321">EventSessionNextToolProgress</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1406">EventSessionNextToolSuccess</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1442">EventSessionNextToolFailed</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1474">EventSessionNextRetried</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1492">EventSessionNextCompactionStarted</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1508">EventSessionNextCompactionDelta</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1526">EventSessionNextCompactionEnded</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1558">EventPermissionV2Asked</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1574">EventPermissionV2Replied</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1623">EventAccountAdded</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1672">EventAccountRemoved</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1688">EventAccountSwitched</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1718">EventPermissionAsked</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1734">EventPermissionReplied</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1754">EventMessagePartDelta</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1780">EventSessionDiff</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1814">EventSessionError</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1822">EventLspUpdated</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1836">EventFileWatcherUpdated</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1848">EventFileEdited</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1876">EventPtyCreated</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1904">EventPtyUpdated</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1918">EventPtyExited</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1930">EventPtyDeleted</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1972">EventQuestionV2Asked</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L1988">EventQuestionV2Replied</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L2002">EventQuestionV2Rejected</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L2024">EventTodoUpdated</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L2036">EventInstallationUpdated</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L2048">EventInstallationUpdateAvailable</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L2060">EventTuiPromptAppend</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L2072">EventTuiCommandExecute</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L2090">EventTuiToastShow</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L2102">EventTuiSessionSelect</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L2114">EventMcpToolsChanged</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L2128">EventMcpBrowserOpenFailed</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L2170">EventQuestionAsked</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L2186">EventQuestionReplied</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L2200">EventQuestionRejected</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L2218">EventCommandExecuted</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L2276">EventSessionStatus</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L2288">EventSessionIdle</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L2300">EventSessionCompacted</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L2312">EventProjectDirectoriesUpdated</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L2358">EventProjectUpdated</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L2370">EventVcsBranchUpdated</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L2382">EventWorkspaceReady</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L2394">EventWorkspaceFailed</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L2408">EventWorkspaceStatus</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L2422">EventWorktreeReady</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L2434">EventWorktreeFailed</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L2442">EventServerConnected</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L2450">EventGlobalDisposed</a>,
    <a href="./src/opencode_ai/types/event_list_response.py#L2462">EventServerInstanceDisposed</a>,
]  # discriminated by "type"</code></pre>

</details>

<!-- expanded:end -->

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

<!-- expanded:start -->

<details>
<summary>Expanded definitions (top-level types; referenced subtypes link to source)</summary>

<pre><code>class Model(BaseModel):
    id: str
    attachment: bool
    cost: <a href="./src/opencode_ai/types/model.py#L10">Cost</a>
    limit: <a href="./src/opencode_ai/types/model.py#L20">Limit</a>
    name: str
    options: Dict[str, object]
    reasoning: bool
    release_date: str
    temperature: bool
    tool_call: bool</code></pre>

<pre><code>class Provider(BaseModel):
    api: Optional[str]
    blacklist: Optional[List[str]]
    env: Optional[List[str]]
    id: Optional[str]
    models: Optional[Dict[str, <a href="./src/opencode_ai/types/config.py#L243">ProviderModels</a>]]
    name: Optional[str]
    npm: Optional[str]
    options: Optional[<a href="./src/opencode_ai/types/config.py#L286">ProviderOptions</a>]
    whitelist: Optional[List[str]]</code></pre>

<pre><code>AppAgentsResponse: TypeAlias = List[<a href="./src/opencode_ai/types/app_agents_response.py#L27">Agent</a>]</code></pre>

<pre><code>AppLogResponse: TypeAlias = bool</code></pre>

<pre><code>class AppProvidersResponse(BaseModel):
    default: Dict[str, str]
    providers: List[<a href="./src/opencode_ai/types/config.py#L317">Provider</a>]</code></pre>

<pre><code>AppSkillsResponse: TypeAlias = List[<a href="./src/opencode_ai/types/app_skills_response.py#L11">Skill</a>]</code></pre>

</details>

<!-- expanded:end -->

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

<!-- expanded:start -->

<details>
<summary>Expanded definitions (top-level types; referenced subtypes link to source)</summary>

<pre><code>class Symbol(BaseModel):
    kind: float
    location: <a href="./src/opencode_ai/types/symbol.py#L26">Location</a>
    name: str</code></pre>

<pre><code>FindFilesResponse: TypeAlias = List[str]</code></pre>

<pre><code>FindSymbolsResponse: TypeAlias = List[<a href="./src/opencode_ai/types/symbol.py#L32">Symbol</a>]</code></pre>

<pre><code>FindTextResponse: TypeAlias = List[<a href="./src/opencode_ai/types/find_text_response.py#L38">FindTextResponseItem</a>]</code></pre>

</details>

<!-- expanded:end -->

Methods:

- <code title="get /find/file">client.find.<a href="./src/opencode_ai/resources/find.py">files</a>(\*\*<a href="src/opencode_ai/types/find_files_params.py">params</a>) -> <a href="./src/opencode_ai/types/find_files_response.py">FindFilesResponse</a></code>
- <code title="get /find/symbol">client.find.<a href="./src/opencode_ai/resources/find.py">symbols</a>(\*\*<a href="src/opencode_ai/types/find_symbols_params.py">params</a>) -> <a href="./src/opencode_ai/types/find_symbols_response.py">FindSymbolsResponse</a></code>
- <code title="get /find">client.find.<a href="./src/opencode_ai/resources/find.py">text</a>(\*\*<a href="src/opencode_ai/types/find_text_params.py">params</a>) -> <a href="./src/opencode_ai/types/find_text_response.py">FindTextResponse</a></code>

# File

Types:

```python
from opencode_ai.types import File, FileListResponse, FileContentResponse, FileStatusResponse
```

<!-- expanded:start -->

<details>
<summary>Expanded definitions (top-level types; referenced subtypes link to source)</summary>

<pre><code>class File(BaseModel):
    added: int
    path: str
    removed: int
    status: Literal['added', 'deleted', 'modified']</code></pre>

<pre><code>FileListResponse: TypeAlias = List[<a href="./src/opencode_ai/types/file_list_response.py#L11">FileNode</a>]</code></pre>

<pre><code>class FileContentResponse(BaseModel):
    content: str
    type: Literal['text', 'binary']
    diff: Optional[str]
    encoding: Optional[Literal['base64']]
    mime_type: Optional[str]  # wire name: "mimeType"
    patch: Optional[object]</code></pre>

<pre><code>FileStatusResponse: TypeAlias = List[<a href="./src/opencode_ai/types/file.py#L10">File</a>]</code></pre>

</details>

<!-- expanded:end -->

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

<!-- expanded:start -->

<details>
<summary>Expanded definitions (top-level types; referenced subtypes link to source)</summary>

<pre><code>class AgentConfig(BaseModel):
    color: Optional[str]
    description: Optional[str]
    disable: Optional[bool]
    hidden: Optional[bool]
    max_steps: Optional[int]  # wire name: "maxSteps"
    mode: Optional[Literal['subagent', 'primary', 'all']]
    model: Optional[str]
    options: Optional[object]
    permission: Optional[<a href="./src/opencode_ai/types/permission_config.py#L61">PermissionConfig</a>]
    prompt: Optional[str]
    steps: Optional[int]
    temperature: Optional[float]
    tools: Optional[Dict[str, bool]]
    top_p: Optional[float]
    variant: Optional[str]</code></pre>

<pre><code>class Config(BaseModel):
    schema_: Optional[str]  # wire name: "$schema"
    agent: Optional[<a href="./src/opencode_ai/types/config.py#L50">Agent</a>]
    attachment: Optional[<a href="./src/opencode_ai/types/config.py#L83">Attachment</a>]
    autoshare: Optional[bool]
    autoupdate: Optional[Union[bool, Literal['notify']]]
    command: Optional[Dict[str, <a href="./src/opencode_ai/types/config.py#L87">CommandConfig</a>]]
    compaction: Optional[<a href="./src/opencode_ai/types/config.py#L101">Compaction</a>]
    default_agent: Optional[str]
    disabled_providers: Optional[List[str]]
    enabled_providers: Optional[List[str]]
    enterprise: Optional[<a href="./src/opencode_ai/types/config.py#L113">Enterprise</a>]
    experimental: Optional[<a href="./src/opencode_ai/types/config.py#L125">Experimental</a>]
    formatter: Optional[Union[bool, Dict[str, <a href="./src/opencode_ai/types/config.py#L141">FormatterConfig</a>]]]
    instructions: Optional[List[str]]
    layout: Optional[Literal['auto', 'stretch']]
    log_level: Optional[Literal['DEBUG', 'INFO', 'WARN', 'ERROR']]  # wire name: "logLevel"
    lsp: Optional[Union[bool, Dict[str, <a href="./src/opencode_ai/types/config.py#L167">LspConfig</a>]]]
    mcp: Optional[Dict[str, <a href="./src/opencode_ai/types/config.py#L174">Mcp</a>]]
    mode: Optional[<a href="./src/opencode_ai/types/config.py#L177">Mode</a>]
    model: Optional[str]
    permission: Optional[<a href="./src/opencode_ai/types/permission_config.py#L61">PermissionConfig</a>]
    plugin: Optional[List[Union[str, Tuple[str, object]]]]
    provider: Optional[Dict[str, <a href="./src/opencode_ai/types/config.py#L317">Provider</a>]]
    reference: Optional[Dict[str, <a href="./src/opencode_ai/types/config.py#L349">ReferenceConfigEntry</a>]]
    server: Optional[<a href="./src/opencode_ai/types/config.py#L354">Server</a>]
    share: Optional[Literal['manual', 'auto', 'disabled']]
    shell: Optional[str]
    skills: Optional[<a href="./src/opencode_ai/types/config.py#L366">Skills</a>]
    small_model: Optional[str]
    snapshot: Optional[bool]
    subagent_depth: Optional[int]
    tool_output: Optional[<a href="./src/opencode_ai/types/config.py#L372">ToolOutput</a>]
    tools: Optional[Dict[str, bool]]
    username: Optional[str]
    watcher: Optional[<a href="./src/opencode_ai/types/config.py#L378">Watcher</a>]</code></pre>

<pre><code>class McpLocalConfig(BaseModel):
    command: List[str]
    type: Literal['local']
    enabled: Optional[bool]
    environment: Optional[Dict[str, str]]
    timeout: Optional[int]</code></pre>

<pre><code>class McpRemoteConfig(BaseModel):
    type: Literal['remote']
    url: str
    enabled: Optional[bool]
    headers: Optional[Dict[str, str]]
    oauth: Optional[<a href="./src/opencode_ai/types/mcp_remote_config.py#L25">OAuth</a>]
    timeout: Optional[int]</code></pre>

<pre><code>PermissionActionConfig: TypeAlias = Literal['ask', 'allow', 'deny']</code></pre>

<pre><code>PermissionConfig: TypeAlias = Union[
    <a href="./src/opencode_ai/types/permission_config.py#L17">PermissionActionConfig</a>,
    <a href="./src/opencode_ai/types/permission_config.py#L22">PermissionConfigObject</a>,
]</code></pre>

<pre><code>class PermissionConfigObject(BaseModel):
    bash: Optional[<a href="./src/opencode_ai/types/permission_config.py#L19">PermissionRuleConfig</a>]
    doom_loop: Optional[<a href="./src/opencode_ai/types/permission_config.py#L17">PermissionActionConfig</a>]
    edit: Optional[<a href="./src/opencode_ai/types/permission_config.py#L19">PermissionRuleConfig</a>]
    external_directory: Optional[<a href="./src/opencode_ai/types/permission_config.py#L19">PermissionRuleConfig</a>]
    glob: Optional[<a href="./src/opencode_ai/types/permission_config.py#L19">PermissionRuleConfig</a>]
    grep: Optional[<a href="./src/opencode_ai/types/permission_config.py#L19">PermissionRuleConfig</a>]
    list: Optional[<a href="./src/opencode_ai/types/permission_config.py#L19">PermissionRuleConfig</a>]
    lsp: Optional[<a href="./src/opencode_ai/types/permission_config.py#L19">PermissionRuleConfig</a>]
    question: Optional[<a href="./src/opencode_ai/types/permission_config.py#L17">PermissionActionConfig</a>]
    read: Optional[<a href="./src/opencode_ai/types/permission_config.py#L19">PermissionRuleConfig</a>]
    skill: Optional[<a href="./src/opencode_ai/types/permission_config.py#L19">PermissionRuleConfig</a>]
    task: Optional[<a href="./src/opencode_ai/types/permission_config.py#L19">PermissionRuleConfig</a>]
    todowrite: Optional[<a href="./src/opencode_ai/types/permission_config.py#L17">PermissionActionConfig</a>]
    webfetch: Optional[<a href="./src/opencode_ai/types/permission_config.py#L17">PermissionActionConfig</a>]
    websearch: Optional[<a href="./src/opencode_ai/types/permission_config.py#L17">PermissionActionConfig</a>]
    __pydantic_extra__: Dict[str, <a href="./src/opencode_ai/types/permission_config.py#L19">PermissionRuleConfig</a>]</code></pre>

<pre><code>PermissionRuleConfig: TypeAlias = Union[
    <a href="./src/opencode_ai/types/permission_config.py#L17">PermissionActionConfig</a>,
    Dict[str, <a href="./src/opencode_ai/types/permission_config.py#L17">PermissionActionConfig</a>],
]</code></pre>

</details>

<!-- expanded:end -->

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
    FilePartInputParam,
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
    TextPartInputParam,
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

<!-- expanded:start -->

<details>
<summary>Expanded definitions (top-level types; referenced subtypes link to source)</summary>

<pre><code>class AgentPart(BaseModel):
    id: str
    message_id: str  # wire name: "messageID"
    name: str
    session_id: str  # wire name: "sessionID"
    type: Literal['agent']
    source: Optional[<a href="./src/opencode_ai/types/part.py#L238">AgentPartSource</a>]</code></pre>

<pre><code>class AssistantMessage(BaseModel):
    id: str
    agent: str
    cost: float
    mode: str
    api_model_id: str  # wire name: "modelID"
    parent_id: str  # wire name: "parentID"
    path: <a href="./src/opencode_ai/types/assistant_message.py#L20">Path</a>
    provider_id: str  # wire name: "providerID"
    role: Literal['assistant']
    session_id: str  # wire name: "sessionID"
    time: <a href="./src/opencode_ai/types/assistant_message.py#L26">Time</a>
    tokens: <a href="./src/opencode_ai/types/assistant_message.py#L38">Tokens</a>
    error: Optional[<a href="./src/opencode_ai/types/assistant_message.py#L56">Error</a>]
    finish: Optional[str]
    structured: Optional[object]
    summary: Optional[bool]
    variant: Optional[str]</code></pre>

<pre><code>class CompactionPart(BaseModel):
    id: str
    auto: bool
    message_id: str  # wire name: "messageID"
    session_id: str  # wire name: "sessionID"
    type: Literal['compaction']
    overflow: Optional[bool]
    tail_start_id: Optional[str]</code></pre>

<pre><code>class FilePart(BaseModel):
    id: str
    message_id: str  # wire name: "messageID"
    mime: str
    session_id: str  # wire name: "sessionID"
    type: Literal['file']
    url: str
    filename: Optional[str]
    source: Optional[<a href="./src/opencode_ai/types/file_part_source.py#L13">FilePartSource</a>]</code></pre>

<pre><code>class FilePartInputParam(TypedDict):
    mime: Required[str]
    type: Required[Literal['file']]
    url: Required[str]
    id: str
    filename: str
    source: <a href="./src/opencode_ai/types/file_part_source_param.py#L14">FilePartSourceParam</a></code></pre>

<pre><code>FilePartSource: TypeAlias = Union[
    <a href="./src/opencode_ai/types/file_source.py#L11">FileSource</a>,
    <a href="./src/opencode_ai/types/symbol_source.py#L29">SymbolSource</a>,
    <a href="./src/opencode_ai/types/resource_source.py#L13">ResourceSource</a>,
]  # discriminated by "type"</code></pre>

<pre><code>class FilePartSourceText(BaseModel):
    end: int
    start: int
    value: str</code></pre>

<pre><code>class FileSource(BaseModel):
    path: str
    text: <a href="./src/opencode_ai/types/file_part_source_text.py#L8">FilePartSourceText</a>
    type: Literal['file']</code></pre>

<pre><code>Message: TypeAlias = Union[
    <a href="./src/opencode_ai/types/user_message.py#L25">UserMessage</a>,
    <a href="./src/opencode_ai/types/assistant_message.py#L70">AssistantMessage</a>,
]  # discriminated by "role"</code></pre>

<pre><code>Part: TypeAlias = Union[
    <a href="./src/opencode_ai/types/part.py#L296">PartUnknown</a>,
    <a href="./src/opencode_ai/types/part.py#L55">TextPart</a>,
    <a href="./src/opencode_ai/types/part.py#L81">SubtaskPart</a>,
    <a href="./src/opencode_ai/types/part.py#L107">ReasoningPart</a>,
    <a href="./src/opencode_ai/types/part.py#L123">FilePart</a>,
    <a href="./src/opencode_ai/types/part.py#L146">ToolPart</a>,
    <a href="./src/opencode_ai/types/part.py#L164">StepStartPart</a>,
    <a href="./src/opencode_ai/types/part.py#L194">StepFinishPart</a>,
    <a href="./src/opencode_ai/types/part.py#L212">SnapshotPart</a>,
    <a href="./src/opencode_ai/types/part.py#L224">PatchPart</a>,
    <a href="./src/opencode_ai/types/part.py#L246">AgentPart</a>,
    <a href="./src/opencode_ai/types/part.py#L264">RetryPart</a>,
    <a href="./src/opencode_ai/types/part.py#L280">CompactionPart</a>,
]  # discriminated by "type"</code></pre>

<pre><code>class PartUnknown(BaseModel):
    """Permissive fallback for `Part` `type` values not yet enumerated by this SDK.

    The server's part union may grow beyond the variants modeled here. Rather
    than raising when an unrecognized `type` is encountered, unmatched parts
    deserialize into this open-ended model so message/session responses keep
    working as the server adds new part kinds. See `EventUnknown` in
    `event_list_response.py` for the sibling pattern and the ordering rationale
    reproduced below."""
    type: str</code></pre>

<pre><code>class PatchPart(BaseModel):
    id: str
    files: List[str]
    hash: str
    message_id: str  # wire name: "messageID"
    session_id: str  # wire name: "sessionID"
    type: Literal['patch']</code></pre>

<pre><code>class ReasoningPart(BaseModel):
    id: str
    message_id: str  # wire name: "messageID"
    session_id: str  # wire name: "sessionID"
    text: str
    time: <a href="./src/opencode_ai/types/part.py#L101">ReasoningPartTime</a>
    type: Literal['reasoning']
    metadata: Optional[object]</code></pre>

<pre><code>class ResourceSource(BaseModel):
    client_name: str  # wire name: "clientName"
    text: <a href="./src/opencode_ai/types/file_part_source_text.py#L8">FilePartSourceText</a>
    type: Literal['resource']
    uri: str</code></pre>

<pre><code>class RetryPart(BaseModel):
    id: str
    attempt: int
    error: <a href="./src/opencode_ai/types/shared/api_error.py#L27">APIError</a>
    message_id: str  # wire name: "messageID"
    session_id: str  # wire name: "sessionID"
    time: <a href="./src/opencode_ai/types/part.py#L260">RetryPartTime</a>
    type: Literal['retry']</code></pre>

<pre><code>class Session(BaseModel):
    id: str
    directory: str
    project_id: str  # wire name: "projectID"
    slug: str
    time: <a href="./src/opencode_ai/types/session.py#L70">Time</a>
    title: str
    version: str
    agent: Optional[str]
    cost: Optional[float]
    metadata: Optional[object]
    model: Optional[<a href="./src/opencode_ai/types/session.py#L62">Model</a>]
    parent_id: Optional[str]  # wire name: "parentID"
    path: Optional[str]
    permission: Optional[List[<a href="./src/opencode_ai/types/session.py#L80">PermissionRule</a>]]
    revert: Optional[<a href="./src/opencode_ai/types/session.py#L88">Revert</a>]
    share: Optional[<a href="./src/opencode_ai/types/session.py#L98">Share</a>]
    summary: Optional[<a href="./src/opencode_ai/types/session.py#L36">Summary</a>]
    tokens: Optional[<a href="./src/opencode_ai/types/session.py#L52">Tokens</a>]
    workspace_id: Optional[str]  # wire name: "workspaceID"</code></pre>

<pre><code>class SnapshotPart(BaseModel):
    id: str
    message_id: str  # wire name: "messageID"
    session_id: str  # wire name: "sessionID"
    snapshot: str
    type: Literal['snapshot']</code></pre>

<pre><code>class StepFinishPart(BaseModel):
    id: str
    cost: float
    message_id: str  # wire name: "messageID"
    reason: str
    session_id: str  # wire name: "sessionID"
    tokens: <a href="./src/opencode_ai/types/part.py#L182">StepFinishPartTokens</a>
    type: Literal['step-finish']
    snapshot: Optional[str]</code></pre>

<pre><code>class StepStartPart(BaseModel):
    id: str
    message_id: str  # wire name: "messageID"
    session_id: str  # wire name: "sessionID"
    type: Literal['step-start']
    snapshot: Optional[str]</code></pre>

<pre><code>class SubtaskPart(BaseModel):
    id: str
    agent: str
    description: str
    message_id: str  # wire name: "messageID"
    prompt: str
    session_id: str  # wire name: "sessionID"
    type: Literal['subtask']
    command: Optional[str]
    model: Optional[<a href="./src/opencode_ai/types/part.py#L75">SubtaskPartModel</a>]</code></pre>

<pre><code>class SymbolSource(BaseModel):
    kind: int
    name: str
    path: str
    range: <a href="./src/opencode_ai/types/symbol_source.py#L23">Range</a>
    text: <a href="./src/opencode_ai/types/file_part_source_text.py#L8">FilePartSourceText</a>
    type: Literal['symbol']</code></pre>

<pre><code>class TextPart(BaseModel):
    id: str
    message_id: str  # wire name: "messageID"
    session_id: str  # wire name: "sessionID"
    text: str
    type: Literal['text']
    ignored: Optional[bool]
    metadata: Optional[object]
    synthetic: Optional[bool]
    time: Optional[<a href="./src/opencode_ai/types/part.py#L49">TextPartTime</a>]</code></pre>

<pre><code>class TextPartInputParam(TypedDict):
    text: Required[str]
    type: Required[Literal['text']]
    id: str
    synthetic: bool
    time: <a href="./src/opencode_ai/types/text_part_input_param.py#L10">Time</a></code></pre>

<pre><code>class ToolPart(BaseModel):
    id: str
    call_id: str  # wire name: "callID"
    message_id: str  # wire name: "messageID"
    session_id: str  # wire name: "sessionID"
    state: <a href="./src/opencode_ai/types/part.py#L141">ToolPartState</a>
    tool: str
    type: Literal['tool']
    metadata: Optional[object]</code></pre>

<pre><code>class ToolStateCompleted(BaseModel):
    input: Dict[str, object]
    metadata: Dict[str, object]
    output: str
    status: Literal['completed']
    time: <a href="./src/opencode_ai/types/tool_state_completed.py#L11">Time</a>
    title: str</code></pre>

<pre><code>class ToolStateError(BaseModel):
    error: str
    input: Dict[str, object]
    status: Literal['error']
    time: <a href="./src/opencode_ai/types/tool_state_error.py#L11">Time</a></code></pre>

<pre><code>class ToolStatePending(BaseModel):
    status: Literal['pending']</code></pre>

<pre><code>class ToolStateRunning(BaseModel):
    status: Literal['running']
    time: <a href="./src/opencode_ai/types/tool_state_running.py#L11">Time</a>
    input: Optional[object]
    metadata: Optional[Dict[str, object]]
    title: Optional[str]</code></pre>

<pre><code>class Todo(BaseModel):
    content: str
    status: str
    priority: str</code></pre>

<pre><code>class UserMessage(BaseModel):
    id: str
    agent: str
    model: <a href="./src/opencode_ai/types/user_message.py#L17">Model</a>
    role: Literal['user']
    session_id: str  # wire name: "sessionID"
    time: <a href="./src/opencode_ai/types/user_message.py#L13">Time</a>
    format: Optional[object]
    summary: Optional[object]
    system: Optional[str]
    tools: Optional[Dict[str, bool]]</code></pre>

<pre><code>SessionListResponse: TypeAlias = List[<a href="./src/opencode_ai/types/session.py#L102">Session</a>]</code></pre>

<pre><code>SessionDeleteResponse: TypeAlias = bool</code></pre>

<pre><code>SessionAbortResponse: TypeAlias = bool</code></pre>

<pre><code>SessionInitResponse: TypeAlias = bool</code></pre>

<pre><code>SessionMessagesResponse: TypeAlias = List[<a href="./src/opencode_ai/types/session_messages_response.py#L13">SessionMessagesResponseItem</a>]</code></pre>

<pre><code>class SessionPromptResponse(BaseModel):
    info: <a href="./src/opencode_ai/types/assistant_message.py#L70">AssistantMessage</a>
    parts: List[<a href="./src/opencode_ai/types/part.py#L331">Part</a>]</code></pre>

<pre><code>SessionSummarizeResponse: TypeAlias = bool</code></pre>

<pre><code>SessionChildrenResponse: TypeAlias = List[<a href="./src/opencode_ai/types/session.py#L102">Session</a>]</code></pre>

<pre><code>class SessionCommandResponse(BaseModel):
    info: <a href="./src/opencode_ai/types/assistant_message.py#L70">AssistantMessage</a>
    parts: List[<a href="./src/opencode_ai/types/part.py#L331">Part</a>]</code></pre>

<pre><code>SessionDeleteMessageResponse: TypeAlias = bool</code></pre>

<pre><code>SessionDeletePartResponse: TypeAlias = bool</code></pre>

<pre><code>SessionDiffResponse: TypeAlias = List[<a href="./src/opencode_ai/types/snapshot_file_diff.py#L11">SnapshotFileDiff</a>]</code></pre>

<pre><code>class SessionMessagesResponseItem(BaseModel):
    info: <a href="./src/opencode_ai/types/message.py#L12">Message</a>
    parts: List[<a href="./src/opencode_ai/types/part.py#L331">Part</a>]</code></pre>

<pre><code>SessionRespondPermissionResponse: TypeAlias = bool</code></pre>

<pre><code>class SessionShellResponse(BaseModel):
    info: <a href="./src/opencode_ai/types/message.py#L12">Message</a>
    parts: List[<a href="./src/opencode_ai/types/part.py#L331">Part</a>]</code></pre>

<pre><code>SessionStatusResponse: TypeAlias = Dict[str, <a href="./src/opencode_ai/types/session_status_response.py#L53">SessionStatus</a>]</code></pre>

<pre><code>SessionTodoResponse: TypeAlias = List[<a href="./src/opencode_ai/types/todo.py#L8">Todo</a>]</code></pre>

</details>

<!-- expanded:end -->

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

<!-- expanded:start -->

<details>
<summary>Expanded definitions (top-level types; referenced subtypes link to source)</summary>

<pre><code>class Project(BaseModel):
    id: str
    sandboxes: List[str]
    time: <a href="./src/opencode_ai/types/project.py#L24">Time</a>
    worktree: str
    commands: Optional[<a href="./src/opencode_ai/types/project.py#L11">Commands</a>]
    icon: Optional[<a href="./src/opencode_ai/types/project.py#L16">Icon</a>]
    name: Optional[str]
    vcs: Optional[Literal['git']]</code></pre>

<pre><code>ProjectListResponse: TypeAlias = List[<a href="./src/opencode_ai/types/project.py#L32">Project</a>]</code></pre>

<pre><code>ProjectDirectoriesResponse: TypeAlias = List[str]</code></pre>

</details>

<!-- expanded:end -->

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

<!-- expanded:start -->

<details>
<summary>Expanded definitions (top-level types; referenced subtypes link to source)</summary>

<pre><code>class ProviderAuthMethod(BaseModel):
    label: str
    type: Literal['oauth', 'api']
    prompts: Optional[List[<a href="./src/opencode_ai/types/provider_auth_method.py#L68">Prompt</a>]]</code></pre>

<pre><code>class ProviderListResponse(BaseModel):
    all: List[<a href="./src/opencode_ai/types/provider_list_response.py#L12">ProviderListResponseProvider</a>]
    connected: List[str]
    default: Dict[str, str]</code></pre>

<pre><code>ProviderAuthResponse: TypeAlias = Dict[str, List[<a href="./src/opencode_ai/types/provider_auth_method.py#L74">ProviderAuthMethod</a>]]</code></pre>

<pre><code>class ProviderAuthAuthorization(BaseModel):
    instructions: str
    method: Literal['auto', 'code']
    url: str</code></pre>

<pre><code>ProviderOAuthCallbackResponse: TypeAlias = bool</code></pre>

</details>

<!-- expanded:end -->

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

<!-- expanded:start -->

<details>
<summary>Expanded definitions (top-level types; referenced subtypes link to source)</summary>

<pre><code>SyncHistoryListResponse: TypeAlias = List[<a href="./src/opencode_ai/types/sync_history_list_response.py#L11">SyncHistoryListResponseItem</a>]</code></pre>

<pre><code>class SyncReplayResponse(BaseModel):
    session_id: str  # wire name: "sessionID"</code></pre>

<pre><code>SyncStartResponse: TypeAlias = bool</code></pre>

<pre><code>class SyncStealResponse(BaseModel):
    session_id: str  # wire name: "sessionID"</code></pre>

</details>

<!-- expanded:end -->

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

<!-- expanded:start -->

<details>
<summary>Expanded definitions (top-level types; referenced subtypes link to source)</summary>

<pre><code>MCPStatus: TypeAlias = Union[
    <a href="./src/opencode_ai/types/mcp_status_connected.py#L10">MCPStatusConnected</a>,
    <a href="./src/opencode_ai/types/mcp_status_disabled.py#L10">MCPStatusDisabled</a>,
    <a href="./src/opencode_ai/types/mcp_status_failed.py#L10">MCPStatusFailed</a>,
    <a href="./src/opencode_ai/types/mcp_status_needs_auth.py#L10">MCPStatusNeedsAuth</a>,
    <a href="./src/opencode_ai/types/mcp_status_needs_client_registration.py#L10">MCPStatusNeedsClientRegistration</a>,
]  # discriminated by "status"</code></pre>

<pre><code>class MCPStatusConnected(BaseModel):
    status: Literal['connected']</code></pre>

<pre><code>class MCPStatusDisabled(BaseModel):
    status: Literal['disabled']</code></pre>

<pre><code>class MCPStatusFailed(BaseModel):
    error: str
    status: Literal['failed']</code></pre>

<pre><code>class MCPStatusNeedsAuth(BaseModel):
    status: Literal['needs_auth']</code></pre>

<pre><code>class MCPStatusNeedsClientRegistration(BaseModel):
    error: str
    status: Literal['needs_client_registration']</code></pre>

<pre><code>class McpLocalConfig(BaseModel):
    command: List[str]
    type: Literal['local']
    enabled: Optional[bool]
    environment: Optional[Dict[str, str]]
    timeout: Optional[int]</code></pre>

<pre><code>class McpRemoteConfig(BaseModel):
    type: Literal['remote']
    url: str
    enabled: Optional[bool]
    headers: Optional[Dict[str, str]]
    oauth: Optional[<a href="./src/opencode_ai/types/mcp_remote_config.py#L25">OAuth</a>]
    timeout: Optional[int]</code></pre>

<pre><code>McpAddResponse: TypeAlias = Dict[str, <a href="./src/opencode_ai/types/mcp_status.py#L15">MCPStatus</a>]</code></pre>

<pre><code>class McpAuthRemoveResponse(BaseModel):
    success: Literal[True]</code></pre>

<pre><code>class McpAuthStartResponse(BaseModel):
    authorization_url: str  # wire name: "authorizationUrl"
    oauth_state: str  # wire name: "oauthState"</code></pre>

<pre><code>McpConnectResponse: TypeAlias = bool</code></pre>

<pre><code>McpDisconnectResponse: TypeAlias = bool</code></pre>

<pre><code>McpStatusResponse: TypeAlias = Dict[str, <a href="./src/opencode_ai/types/mcp_status.py#L15">MCPStatus</a>]</code></pre>

</details>

<!-- expanded:end -->

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

<!-- expanded:start -->

<details>
<summary>Expanded definitions (top-level types; referenced subtypes link to source)</summary>

<pre><code>class Pty(BaseModel):
    id: str
    args: List[str]
    command: str
    cwd: str
    pid: int
    status: Literal['running', 'exited']
    title: str</code></pre>

<pre><code>PtyListResponse: TypeAlias = List[<a href="./src/opencode_ai/types/pty.py#L11">Pty</a>]</code></pre>

<pre><code>PtyConnectResponse: TypeAlias = bool</code></pre>

<pre><code>class PtyConnectTokenResponse(BaseModel):
    expires_in: int
    ticket: str</code></pre>

<pre><code>PtyDeleteResponse: TypeAlias = bool</code></pre>

<pre><code>PtyShellsResponse: TypeAlias = List[<a href="./src/opencode_ai/types/pty_shells_response_item.py#L8">PtyShellsResponseItem</a>]</code></pre>

</details>

<!-- expanded:end -->

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

<!-- expanded:start -->

<details>
<summary>Expanded definitions (top-level types; referenced subtypes link to source)</summary>

<pre><code>TuiAppendPromptResponse: TypeAlias = bool</code></pre>

<pre><code>TuiOpenHelpResponse: TypeAlias = bool</code></pre>

<pre><code>TuiOpenSessionsResponse: TypeAlias = bool</code></pre>

<pre><code>TuiOpenThemesResponse: TypeAlias = bool</code></pre>

<pre><code>TuiOpenModelsResponse: TypeAlias = bool</code></pre>

<pre><code>TuiSubmitPromptResponse: TypeAlias = bool</code></pre>

<pre><code>TuiClearPromptResponse: TypeAlias = bool</code></pre>

<pre><code>TuiExecuteCommandResponse: TypeAlias = bool</code></pre>

<pre><code>TuiShowToastResponse: TypeAlias = bool</code></pre>

<pre><code>TuiPublishResponse: TypeAlias = bool</code></pre>

<pre><code>TuiSelectSessionResponse: TypeAlias = bool</code></pre>

<pre><code>class TuiControlNextResponse(BaseModel):
    path: str
    body: object</code></pre>

<pre><code>TuiControlResponseResponse: TypeAlias = bool</code></pre>

</details>

<!-- expanded:end -->

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

<!-- expanded:start -->

<details>
<summary>Expanded definitions (top-level types; referenced subtypes link to source)</summary>

<pre><code>class QuestionInfo(BaseModel):
    header: str
    options: List[<a href="./src/opencode_ai/types/question_option.py#L8">QuestionOption</a>]
    question: str
    custom: Optional[bool]
    multiple: Optional[bool]</code></pre>

<pre><code>class QuestionOption(BaseModel):
    description: str
    label: str</code></pre>

<pre><code>class QuestionRequest(BaseModel):
    id: str
    questions: List[<a href="./src/opencode_ai/types/question_info.py#L11">QuestionInfo</a>]
    session_id: str  # wire name: "sessionID"
    tool: Optional[<a href="./src/opencode_ai/types/question_tool.py#L10">QuestionTool</a>]</code></pre>

<pre><code>class QuestionTool(BaseModel):
    call_id: str  # wire name: "callID"
    message_id: str  # wire name: "messageID"</code></pre>

<pre><code>QuestionListResponse: TypeAlias = List[<a href="./src/opencode_ai/types/question_request.py#L14">QuestionRequest</a>]</code></pre>

<pre><code>QuestionRejectResponse: TypeAlias = bool</code></pre>

<pre><code>QuestionReplyResponse: TypeAlias = bool</code></pre>

</details>

<!-- expanded:end -->

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

<!-- expanded:start -->

<details>
<summary>Expanded definitions (top-level types; referenced subtypes link to source)</summary>

<pre><code>class PermissionRequest(BaseModel):
    id: str
    always: List[str]
    metadata: object
    patterns: List[str]
    permission: str
    session_id: str  # wire name: "sessionID"
    tool: Optional[<a href="./src/opencode_ai/types/permission_request.py#L12">PermissionRequestTool</a>]</code></pre>

<pre><code>PermissionListResponse: TypeAlias = List[<a href="./src/opencode_ai/types/permission_request.py#L18">PermissionRequest</a>]</code></pre>

<pre><code>PermissionReplyResponse: TypeAlias = bool</code></pre>

</details>

<!-- expanded:end -->

Methods:

- <code title="get /permission">client.permission.<a href="./src/opencode_ai/resources/permission.py">list</a>() -> <a href="./src/opencode_ai/types/permission_list_response.py">PermissionListResponse</a></code>
- <code title="post /permission/{requestID}/reply">client.permission.<a href="./src/opencode_ai/resources/permission.py">reply</a>(request_id, \*\*<a href="src/opencode_ai/types/permission_reply_params.py">params</a>) -> <a href="./src/opencode_ai/types/permission_reply_response.py">PermissionReplyResponse</a></code>

# Path

Types:

```python
from opencode_ai.types import Path
```

<!-- expanded:start -->

<details>
<summary>Expanded definitions (top-level types; referenced subtypes link to source)</summary>

<pre><code>class Path(BaseModel):
    cwd: str
    root: str</code></pre>

</details>

<!-- expanded:end -->

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

<!-- expanded:start -->

<details>
<summary>Expanded definitions (top-level types; referenced subtypes link to source)</summary>

<pre><code>class VcsInfo(BaseModel):
    branch: Optional[str]
    default_branch: Optional[str]</code></pre>

<pre><code>class VcsFileStatus(BaseModel):
    additions: float
    deletions: float
    file: str
    status: Literal['added', 'deleted', 'modified']</code></pre>

<pre><code>class VcsFileDiff(BaseModel):
    additions: float
    deletions: float
    file: str
    patch: Optional[str]
    status: Optional[Literal['added', 'deleted', 'modified']]</code></pre>

<pre><code>VcsStatusResponse: TypeAlias = List[<a href="./src/opencode_ai/types/vcs_file_status.py#L10">VcsFileStatus</a>]</code></pre>

<pre><code>VcsDiffResponse: TypeAlias = List[<a href="./src/opencode_ai/types/vcs_file_diff.py#L11">VcsFileDiff</a>]</code></pre>

<pre><code>class VcsApplyResponse(BaseModel):
    applied: bool</code></pre>

</details>

<!-- expanded:end -->

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

<!-- expanded:start -->

<details>
<summary>Expanded definitions (top-level types; referenced subtypes link to source)</summary>

<pre><code>class Command(BaseModel):
    hints: List[str]
    name: str
    template: str
    agent: Optional[str]
    description: Optional[str]
    model: Optional[str]
    source: Optional[Literal['command', 'mcp', 'skill']]
    subtask: Optional[bool]</code></pre>

<pre><code>CommandListResponse: TypeAlias = List[<a href="./src/opencode_ai/types/command.py#L11">Command</a>]</code></pre>

</details>

<!-- expanded:end -->

Methods:

- <code title="get /command">client.command.<a href="./src/opencode_ai/resources/command.py">list</a>() -> <a href="./src/opencode_ai/types/command_list_response.py">CommandListResponse</a></code>

# Lsp

Types:

```python
from opencode_ai.types import LSPStatus, LspStatusResponse
```

<!-- expanded:start -->

<details>
<summary>Expanded definitions (top-level types; referenced subtypes link to source)</summary>

<pre><code>class LSPStatus(BaseModel):
    id: str
    name: str
    root: str
    status: Literal['connected', 'error']</code></pre>

<pre><code>LspStatusResponse: TypeAlias = List[<a href="./src/opencode_ai/types/lsp_status.py#L10">LSPStatus</a>]</code></pre>

</details>

<!-- expanded:end -->

Methods:

- <code title="get /lsp">client.lsp.<a href="./src/opencode_ai/resources/lsp.py">status</a>() -> <a href="./src/opencode_ai/types/lsp_status_response.py">LspStatusResponse</a></code>

# Formatter

Types:

```python
from opencode_ai.types import FormatterStatus, FormatterStatusResponse
```

<!-- expanded:start -->

<details>
<summary>Expanded definitions (top-level types; referenced subtypes link to source)</summary>

<pre><code>class FormatterStatus(BaseModel):
    enabled: bool
    extensions: List[str]
    name: str</code></pre>

<pre><code>FormatterStatusResponse: TypeAlias = List[<a href="./src/opencode_ai/types/formatter_status.py#L10">FormatterStatus</a>]</code></pre>

</details>

<!-- expanded:end -->

Methods:

- <code title="get /formatter">client.formatter.<a href="./src/opencode_ai/resources/formatter.py">status</a>() -> <a href="./src/opencode_ai/types/formatter_status_response.py">FormatterStatusResponse</a></code>

# Instance

Types:

```python
from opencode_ai.types import InstanceDisposeResponse
```

<!-- expanded:start -->

<details>
<summary>Expanded definitions (top-level types; referenced subtypes link to source)</summary>

<pre><code>InstanceDisposeResponse: TypeAlias = bool</code></pre>

</details>

<!-- expanded:end -->

Methods:

- <code title="post /instance/dispose">client.instance.<a href="./src/opencode_ai/resources/instance.py">dispose</a>() -> bool</code>

# Auth

Types:

```python
from opencode_ai.types import AuthSetResponse, AuthRemoveResponse
```

<!-- expanded:start -->

<details>
<summary>Expanded definitions (top-level types; referenced subtypes link to source)</summary>

<pre><code>AuthSetResponse: TypeAlias = bool</code></pre>

<pre><code>AuthRemoveResponse: TypeAlias = bool</code></pre>

</details>

<!-- expanded:end -->

Methods:

- <code title="put /auth/{providerID}">client.auth.<a href="./src/opencode_ai/resources/auth.py">set</a>(id, \*\*<a href="src/opencode_ai/types/auth_set_params.py">params</a>) -> bool</code>
- <code title="delete /auth/{providerID}">client.auth.<a href="./src/opencode_ai/resources/auth.py">remove</a>(id) -> bool</code>
