# Task 5: experimental operations table (spec v1.18.11)

Source: `spec/openapi-opencode.json`; cross-checked against
`.cortex/plans/2026-08-03-flake-uv-1.18-audit/missing-ops.json` (all 16 present).

Addressing: every op carries `directory`/`workspace` query params EXCEPT
`experimental.controlPlane.moveSession` (spec has none; design D6).

## Method naming (step 3, D5)

One flat module, no nested classes. Bare tails collide (`get` x2, `list` x4), so
method names keep the full tail after `experimental.` in snake_case (same rule as
task-6's dotted tails, e.g. `permission.request_list`). The step-3 chain
`client.experimental.console.list_orgs()` is the conceptual namespace chain; the
implemented surface is `client.experimental.console_list_orgs()` (task-7 wires
`client.experimental`).

| # | operationId | method | path | method name |
|---|---|---|---|---|
| 1 | experimental.capabilities.get | GET | /experimental/capabilities | `capabilities_get` |
| 2 | experimental.console.get | GET | /experimental/console | `console_get` |
| 3 | experimental.console.listOrgs | GET | /experimental/console/orgs | `console_list_orgs` |
| 4 | experimental.console.switchOrg | POST | /experimental/console/switch | `console_switch_org` |
| 5 | experimental.session.list | GET | /experimental/session | `session_list` |
| 6 | experimental.session.background | POST | /experimental/session/{sessionID}/background | `session_background` |
| 7 | experimental.resource.list | GET | /experimental/resource | `resource_list` |
| 8 | experimental.controlPlane.moveSession | POST | /experimental/control-plane/move-session | `control_plane_move_session` |
| 9 | experimental.projectCopy.generateName | POST | /experimental/project/{projectID}/copy/generate-name | `project_copy_generate_name` |
| 10 | experimental.workspace.list | GET | /experimental/workspace | `workspace_list` |
| 11 | experimental.workspace.create | POST | /experimental/workspace | `workspace_create` |
| 12 | experimental.workspace.syncList | POST | /experimental/workspace/sync-list | `workspace_sync_list` |
| 13 | experimental.workspace.status | GET | /experimental/workspace/status | `workspace_status` |
| 14 | experimental.workspace.remove | DELETE | /experimental/workspace/{id} | `workspace_remove` |
| 15 | experimental.workspace.warp | POST | /experimental/workspace/warp | `workspace_warp` |
| 16 | experimental.workspace.adapter.list | GET | /experimental/workspace/adapter | `workspace_adapter_list` |

## Per-operation detail

| op | query params | path params | body | response |
|---|---|---|---|---|
| capabilities.get | directory, workspace | - | - | ExperimentalCapabilities {backgroundSubagents: bool} |
| console.get | directory, workspace | - | - | ConsoleState {consoleManagedProviders: string[], activeOrgName?: string, switchableOrgCount: int} |
| console.listOrgs | directory, workspace | - | - | {orgs: [{accountID, accountEmail, accountUrl, orgID, orgName, active}]} |
| console.switchOrg | directory, workspace | - | {accountID: str, orgID: str} (both req) | boolean |
| session.list | directory, workspace, roots: bool\|str, start: number, cursor: number, search: str, limit: number, archived: bool\|str | - | - | GlobalSession[] |
| session.background | directory, workspace | sessionID (req) | - | boolean |
| resource.list | directory, workspace | - | - | {[name]: McpResource} |
| controlPlane.moveSession | - (none) | - | {sessionID: str, destination: {directory: str}, moveChanges?: bool} (sessionID+destination req) | 204 |
| projectCopy.generateName | directory, workspace | projectID (req) | {context?: str} | {name: str} |
| workspace.list | directory, workspace | - | - | Workspace[] |
| workspace.create | directory, workspace | - | {id?: str(^wrk), type: str, branch?: str\|null, extra?: object\|null} (type req) | Workspace |
| workspace.syncList | directory, workspace | - | - | 204 |
| workspace.status | directory, workspace | - | - | WorkspaceEventConnectionStatus[] |
| workspace.remove | directory, workspace | id (req, ^wrk) | - | Workspace |
| workspace.warp | directory, workspace | - | {id: str(^wrk)\|null, sessionID: str(^ses), copyChanges?: bool} (id+sessionID req) | 204 |
| workspace.adapter.list | directory, workspace | - | - | {type, name, description}[] |

## Schemas

- **Workspace**: id(^wrk), type, name, branch?: str|null, directory?: str|null,
  extra?: object|null, projectID, timeUsed: number|"NaN"|"Infinity"|"-Infinity";
  required id, type, name, projectID, timeUsed.
- **McpResource**: name, uri, description?, mimeType?, client; required name, uri, client.
- **GlobalSession**: id(^ses), slug, projectID, workspaceID?(^wrk), directory,
  path?, parentID?(^ses), summary? {additions, deletions, files, diffs?: SnapshotFileDiff[]},
  cost?, tokens? {cache {read, write}, input, output, reasoning}, share? {url},
  title, agent?, model? {id, providerID, variant?}, version, metadata?: object,
  time {created, updated, compacting?, archived?}, permission?: PermissionRule[],
  revert? {messageID, partID?, snapshot?, diff?}, project?: ProjectSummary|null;
  required id, slug, projectID, directory, title, version, time, project.
  (PermissionRule and SnapshotFileDiff reused from existing types.)
- **ProjectSummary**: id, name?, worktree; required id, worktree.
- **WorkspaceEventConnectionStatus**: workspaceID(^wrk), status: "connected"|"connecting"|"disconnected"|"error".

## Type files

Responses (types/experimental_*_response.py): capabilities_get, console_get,
console_list_orgs, console_switch_org (bool alias), session_list, session_background
(bool alias), resource_list, project_copy_generate_name, workspace_list (defines
Workspace), workspace_create (alias of Workspace), workspace_status, workspace_remove
(alias of Workspace), workspace_adapter_list.
Params: control_plane_move_session (defines MoveSessionDestination),
console_switch_org, project_copy_generate_name, workspace_create, workspace_warp,
session_list (query incl. directory/workspace).

## Verification notes

- 204 ops (moveSession, syncList, warp) -> `cast_to=NoneType`, return None.
- bool-body ops (switchOrg, session.background) -> TypeAlias bool like AuthSetResponse.
- types/__init__.py untouched: `from ..types import X` resolves via submodule import.
- Tests construct `ExperimentalResource(client)` directly (client.experimental is
  task-7's wiring; tests must pass before and after wiring).
