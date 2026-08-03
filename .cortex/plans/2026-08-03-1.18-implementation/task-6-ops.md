# Task 6 — v2 op table, naming mapping, fidelity policy

Source of truth: `spec/openapi-opencode.json` (v1.18.11). 61 v2 operations, matching `local-operationIds.txt`.

## Area counts (spec-actual — the plan's prose counts were stale)

| area | module | count |
|---|---|---|
| session | resources/v2/session.py | 25 |
| integration | resources/v2/integration.py | 7 |
| pty | resources/v2/pty.py | 7 |
| permission | resources/v2/permission.py | 3 |
| fs | resources/v2/fs.py | 3 |
| question | resources/v2/question.py | 1 |
| provider | resources/v2/provider.py | 2 |
| credential | resources/v2/credential.py | 2 |
| health | resources/v2/health.py | 1 |
| location | resources/v2/location.py | 1 |
| agent | resources/v2/agent.py | 1 |
| model | resources/v2/model.py | 1 |
| command | resources/v2/command.py | 1 |
| skill | resources/v2/skill.py | 1 |
| event | resources/v2/event.py | 1 |
| reference | resources/v2/reference.py | 1 |
| projectCopy | resources/v2/project_copy.py | 3 |
| **total** | | **61** |

> Deviations from plan prose, confirmed with the user before building:
> 1. **projectCopy included (61 ops)** — the 3 `/experimental/project/{projectID}/copy` ops; the v2 namespace (`client.v2.project_copy`) is distinct from the v1 `experimental.py` file, so no collision.
> 2. **`location` deepObject query param is faithful to spec** — the plan claimed 'the other 60 ops carry none', but ~48 ops carry an optional `location` (`location[directory]`/`location[workspace]`) deepObject; `session.list` alone carries the flat `directory/workspace/project/subpath/cursor`; `pty.connect` carries flattened `location[directory]`/`location[workspace]`+`cursor`+`ticket`.

## Naming mapping (method = snake_case of the operationId tail after `v2.<area>.`)

| operationId | HTTP | path | method |
|---|---|---|---|
| `v2.agent.list` | GET | `/api/agent` | `v2.agent.list` |
| `v2.command.list` | GET | `/api/command` | `v2.command.list` |
| `v2.credential.remove` | DELETE | `/api/credential/{credentialID}` | `v2.credential.remove` |
| `v2.credential.update` | PATCH | `/api/credential/{credentialID}` | `v2.credential.update` |
| `v2.event.subscribe` | GET | `/api/event` | `v2.event.subscribe` |
| `v2.fs.find` | GET | `/api/fs/find` | `v2.fs.find` |
| `v2.fs.list` | GET | `/api/fs/list` | `v2.fs.list` |
| `v2.fs.read` | GET | `/api/fs/read/*` | `v2.fs.read` |
| `v2.health.get` | GET | `/api/health` | `v2.health.get` |
| `v2.integration.attempt.cancel` | DELETE | `/api/integration/attempt/{attemptID}` | `v2.integration.attempt_cancel` |
| `v2.integration.attempt.complete` | POST | `/api/integration/attempt/{attemptID}/complete` | `v2.integration.attempt_complete` |
| `v2.integration.attempt.status` | GET | `/api/integration/attempt/{attemptID}` | `v2.integration.attempt_status` |
| `v2.integration.connect.key` | POST | `/api/integration/{integrationID}/connect/key` | `v2.integration.connect_key` |
| `v2.integration.connect.oauth` | POST | `/api/integration/{integrationID}/connect/oauth` | `v2.integration.connect_oauth` |
| `v2.integration.get` | GET | `/api/integration/{integrationID}` | `v2.integration.get` |
| `v2.integration.list` | GET | `/api/integration` | `v2.integration.list` |
| `v2.location.get` | GET | `/api/location` | `v2.location.get` |
| `v2.model.list` | GET | `/api/model` | `v2.model.list` |
| `v2.permission.request.list` | GET | `/api/permission/request` | `v2.permission.request_list` |
| `v2.permission.saved.list` | GET | `/api/permission/saved` | `v2.permission.saved_list` |
| `v2.permission.saved.remove` | DELETE | `/api/permission/saved/{id}` | `v2.permission.saved_remove` |
| `v2.projectCopy.create` | POST | `/experimental/project/{projectID}/copy` | `v2.project_copy.create` |
| `v2.projectCopy.refresh` | POST | `/experimental/project/{projectID}/copy/refresh` | `v2.project_copy.refresh` |
| `v2.projectCopy.remove` | DELETE | `/experimental/project/{projectID}/copy` | `v2.project_copy.remove` |
| `v2.provider.get` | GET | `/api/provider/{providerID}` | `v2.provider.get` |
| `v2.provider.list` | GET | `/api/provider` | `v2.provider.list` |
| `v2.pty.connect` | GET | `/api/pty/{ptyID}/connect` | `v2.pty.connect` |
| `v2.pty.connectToken` | POST | `/api/pty/{ptyID}/connect-token` | `v2.pty.connect_token` |
| `v2.pty.create` | POST | `/api/pty` | `v2.pty.create` |
| `v2.pty.get` | GET | `/api/pty/{ptyID}` | `v2.pty.get` |
| `v2.pty.list` | GET | `/api/pty` | `v2.pty.list` |
| `v2.pty.remove` | DELETE | `/api/pty/{ptyID}` | `v2.pty.remove` |
| `v2.pty.update` | PUT | `/api/pty/{ptyID}` | `v2.pty.update` |
| `v2.question.request.list` | GET | `/api/question/request` | `v2.question.request_list` |
| `v2.reference.list` | GET | `/api/reference` | `v2.reference.list` |
| `v2.session.active` | GET | `/api/session/active` | `v2.session.active` |
| `v2.session.compact` | POST | `/api/session/{sessionID}/compact` | `v2.session.compact` |
| `v2.session.context` | GET | `/api/session/{sessionID}/context` | `v2.session.context` |
| `v2.session.create` | POST | `/api/session` | `v2.session.create` |
| `v2.session.events` | GET | `/api/session/{sessionID}/event` | `v2.session.events` |
| `v2.session.get` | GET | `/api/session/{sessionID}` | `v2.session.get` |
| `v2.session.history` | GET | `/api/session/{sessionID}/history` | `v2.session.history` |
| `v2.session.interrupt` | POST | `/api/session/{sessionID}/interrupt` | `v2.session.interrupt` |
| `v2.session.list` | GET | `/api/session` | `v2.session.list` |
| `v2.session.message` | GET | `/api/session/{sessionID}/message/{messageID}` | `v2.session.message` |
| `v2.session.messages` | GET | `/api/session/{sessionID}/message` | `v2.session.messages` |
| `v2.session.permission.create` | POST | `/api/session/{sessionID}/permission` | `v2.session.permission_create` |
| `v2.session.permission.get` | GET | `/api/session/{sessionID}/permission/{requestID}` | `v2.session.permission_get` |
| `v2.session.permission.list` | GET | `/api/session/{sessionID}/permission` | `v2.session.permission_list` |
| `v2.session.permission.reply` | POST | `/api/session/{sessionID}/permission/{requestID}/reply` | `v2.session.permission_reply` |
| `v2.session.prompt` | POST | `/api/session/{sessionID}/prompt` | `v2.session.prompt` |
| `v2.session.question.list` | GET | `/api/session/{sessionID}/question` | `v2.session.question_list` |
| `v2.session.question.reject` | POST | `/api/session/{sessionID}/question/{requestID}/reject` | `v2.session.question_reject` |
| `v2.session.question.reply` | POST | `/api/session/{sessionID}/question/{requestID}/reply` | `v2.session.question_reply` |
| `v2.session.revert.clear` | POST | `/api/session/{sessionID}/revert/clear` | `v2.session.revert_clear` |
| `v2.session.revert.commit` | POST | `/api/session/{sessionID}/revert/commit` | `v2.session.revert_commit` |
| `v2.session.revert.stage` | POST | `/api/session/{sessionID}/revert/stage` | `v2.session.revert_stage` |
| `v2.session.switchAgent` | POST | `/api/session/{sessionID}/agent` | `v2.session.switch_agent` |
| `v2.session.switchModel` | POST | `/api/session/{sessionID}/model` | `v2.session.switch_model` |
| `v2.session.wait` | POST | `/api/session/{sessionID}/wait` | `v2.session.wait` |
| `v2.skill.list` | GET | `/api/skill` | `v2.skill.list` |

Dotted tails keep the full tail in snake_case (per plan Step 2): `permission.request.list`→`request_list`, `permission.saved.list`→`saved_list`, `session.permission.list`→`permission_list`, `session.question.list`→`question_list`, `question.request.list`→`request_list`, `session.revert.stage`→`revert_stage`. `switchAgent`→`switch_agent`, `connectToken`→`connect_token`.

## Fidelity policy (bounded on purpose)

The V2Event/message universe is **245 transitive schemas** (224 new) — full pydantic fidelity is out of scope for an operation-level task. Boundary:
- **Operation shapes** (path/method/path-params/query-params/request-body/response cast) are fully faithful.
- **Request param TypedDicts** model body/query fields faithfully; nested objects/$refs are `object`/`Dict[str, object]`/`Iterable[object]`.
- **Response models** mirror the envelope's direct fields; `location`→shared `V2LocationInfo`, `cursor`→nested class, primitives/enums faithful, `data`/other nested objects→`object`/`List[object]`.
- Primitive/stream/no-content responses: `fs.read`→`str` (octet-stream), `pty.connect`→`bool`, `event.subscribe`/`session.events`→`Stream[...]`, 204 ops→`None`.
