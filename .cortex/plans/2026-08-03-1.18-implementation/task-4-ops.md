# Task 4 ops table (extracted from spec/openapi-opencode.json v1.18.11, cross-checked against missing-ops.json)

All 12 operationIds present in both the spec and `missing-ops.json` / `local-operationIds.txt` (`*`-marked).
Response schemas resolved via `components/schemas`; required = spec `required` array.

## global (module `resources/global_.py`, class `GlobalResource`, client attr `global_`)

No operation under `/global/*` carries directory/workspace query params (spec `parameters: []` for all six).

| operationId | method | path | query params | request body | 200 response |
|---|---|---|---|---|---|
| `global.health` | GET | `/global/health` | - | - | object `{healthy: Literal[True], version: str}` (both required) |
| `global.event` | GET | `/global/event` | - | - | SSE `GlobalEvent`: `{directory: str (req), payload: EventUnion (req), project?: str, workspace?: str}`; payload anyOf = 88 named event types + 36 generic catch-alls, same variant set as `Event` (the `/event` union already modeled as `EventListResponse`) |
| `global.config.get` | GET | `/global/config` | - | - | `Config` schema (identical to `/config` GET response; modeled as `opencode_ai.types.config.Config`) |
| `global.config.update` | PATCH | `/global/config` | - | `Config` schema (identical to `/config` PATCH body; modeled as `config_update_params.ConfigUpdateParams`) | `Config` |
| `global.dispose` | POST | `/global/dispose` | - | - | `boolean` |
| `global.upgrade` | POST | `/global/upgrade` | - | `{target?: str}` | anyOf: `{success: Literal[True], version: str}` \| `{success: Literal[False], error: str}` (discriminator `success`) |

## tool (module `resources/tool.py`, class `ToolResource`, client attr `tool`)

`tool.*` carries the fork's v1 addressing convention (directory/workspace query params) per spec.

| operationId | method | path | query params | request body | 200 response |
|---|---|---|---|---|---|
| `tool.list` | GET | `/experimental/tool` | `directory?`, `workspace?`, `provider` (required), `model` (required) | - | `ToolList` = array of `ToolListItem` `{id: str, description: str, parameters: {} (free-form JSON Schema, required)}` |
| `tool.ids` | GET | `/experimental/tool/ids` | `directory?`, `workspace?` | - | `ToolIDs` = array of `string` |

## worktree (module `resources/worktree.py`, class `WorktreeResource`, client attr `worktree`)

`worktree.*` carries the fork's v1 addressing convention (directory/workspace query params) per spec.

| operationId | method | path | query params | request body | 200 response |
|---|---|---|---|---|---|
| `worktree.list` | GET | `/experimental/worktree` | `directory?`, `workspace?` | - | array of `string` |
| `worktree.create` | POST | `/experimental/worktree` | `directory?`, `workspace?` | `WorktreeCreateInput` `{name?: str, startCommand?: str}` | `Worktree` `{name: str, branch?: str, directory: str}` |
| `worktree.remove` | DELETE | `/experimental/worktree` | `directory?`, `workspace?` | `WorktreeRemoveInput` `{directory: str (req)}` | `boolean` |
| `worktree.reset` | POST | `/experimental/worktree/reset` | `directory?`, `workspace?` | `WorktreeResetInput` `{directory: str (req)}` | `boolean` |

## Type files created (named after the spec schemas each op uses)

| file | content |
|---|---|
| `types/global_health_response.py` | `GlobalHealthResponse(BaseModel)` healthy/version |
| `types/global_event_response.py` | `GlobalEventResponse(BaseModel)` wrapping `EventListResponse` payload |
| `types/global_config_get_response.py` | `GlobalConfigGetResponse: TypeAlias = Config` |
| `types/global_dispose_response.py` | `GlobalDisposeResponse: TypeAlias = bool` |
| `types/global_upgrade_params.py` | `GlobalUpgradeParams(TypedDict)` target |
| `types/global_upgrade_response.py` | `GlobalUpgradeResponse` discriminated union on `success` |
| `types/tool_list_params.py` | `ToolListParams(TypedDict)` provider/model required + addressing |
| `types/tool_list_response.py` | `ToolListResponse: TypeAlias = List[ToolListResponseItem]` |
| `types/tool_ids_response.py` | `ToolIDsResponse: TypeAlias = List[str]` |
| `types/worktree.py` | `Worktree(BaseModel)` name/branch/directory |
| `types/worktree_list_response.py` | `WorktreeListResponse: TypeAlias = List[str]` |
| `types/worktree_create_params.py` | `WorktreeCreateParams(TypedDict)` name/startCommand |
| `types/worktree_remove_params.py` | `WorktreeRemoveParams(TypedDict)` directory required |
| `types/worktree_reset_params.py` | `WorktreeResetParams(TypedDict)` directory required |
| `types/worktree_remove_response.py` | `WorktreeRemoveResponse: TypeAlias = bool` |
| `types/worktree_reset_response.py` | `WorktreeResetResponse: TypeAlias = bool` |

Notes:
- `global.config.update` reuses `config_update_params.ConfigUpdateParams` and `Config` (identical spec schemas to `/config`); no duplicate 30-field TypedDict.
- `global.event` is SSE: sync returns `Stream[GlobalEventResponse]`, async `AsyncStream[GlobalEventResponse]`, mirroring `resources/event.py`.
- Wiring (`resources/__init__.py`, `_client.py`) and api.md are task-7's; tests construct resources directly.
