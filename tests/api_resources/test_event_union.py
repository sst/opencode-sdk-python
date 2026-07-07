"""Regression coverage for the full 87-variant Event union.

`EventListResponse` is a discriminated union (`type`) generated from the spec's
`Event` schema by `scripts/gen_union_models.py`, with `EventUnknown` prepended
as a permissive fallback for any `type` value not in the 87 known variants
(see the ordering-rationale comment above the union declaration in
`event_list_response.py` for why `EventUnknown` must stay first).

`EVENT_VARIANT_SAMPLES` below is one minimal-but-schema-valid payload per
variant (every field required by that variant's `properties` model is
present, recursively, including nested Message/Session/Part/error shapes) --
generated once from the OpenAPI spec and pinned here so the test suite has no
runtime dependency on that external file.
"""

from typing import Any, Dict, List, Tuple

from opencode_ai.types import EventListResponse
from opencode_ai._models import construct_type

# (wire `type` value, expected class name, minimal valid payload) for every
# one of the 87 spec variants.
EVENT_VARIANT_SAMPLES: List[Tuple[str, str, Dict[str, Any]]] = [
    ("plugin.added", "EventPluginAdded", {"id": "x", "type": "plugin.added", "properties": {"id": "x"}}),
    (
        "catalog.model.updated",
        "EventCatalogModelUpdated",
        {
            "id": "x",
            "type": "catalog.model.updated",
            "properties": {
                "model": {
                    "id": "x",
                    "providerID": "x",
                    "name": "x",
                    "api": {"id": "x", "type": "aisdk", "package": "x"},
                    "capabilities": {"tools": False, "input": [], "output": []},
                    "request": {"headers": {}, "body": {}},
                    "variants": [],
                    "time": {"released": 1.0},
                    "cost": [],
                    "status": "alpha",
                    "enabled": False,
                    "limit": {"context": 1, "output": 1},
                }
            },
        },
    ),
    (
        "session.created",
        "EventSessionCreated",
        {
            "id": "x",
            "type": "session.created",
            "properties": {
                "sessionID": "x",
                "info": {
                    "id": "x",
                    "slug": "x",
                    "projectID": "x",
                    "directory": "x",
                    "title": "x",
                    "version": "x",
                    "time": {"created": 1, "updated": 1},
                },
            },
        },
    ),
    (
        "session.updated",
        "EventSessionUpdated",
        {
            "id": "x",
            "type": "session.updated",
            "properties": {
                "sessionID": "x",
                "info": {
                    "id": "x",
                    "slug": "x",
                    "projectID": "x",
                    "directory": "x",
                    "title": "x",
                    "version": "x",
                    "time": {"created": 1, "updated": 1},
                },
            },
        },
    ),
    (
        "session.deleted",
        "EventSessionDeleted",
        {
            "id": "x",
            "type": "session.deleted",
            "properties": {
                "sessionID": "x",
                "info": {
                    "id": "x",
                    "slug": "x",
                    "projectID": "x",
                    "directory": "x",
                    "title": "x",
                    "version": "x",
                    "time": {"created": 1, "updated": 1},
                },
            },
        },
    ),
    (
        "message.updated",
        "EventMessageUpdated",
        {
            "id": "x",
            "type": "message.updated",
            "properties": {
                "sessionID": "x",
                "info": {
                    "id": "x",
                    "sessionID": "x",
                    "role": "user",
                    "time": {"created": 1.0},
                    "agent": "x",
                    "model": {"providerID": "x", "modelID": "x"},
                },
            },
        },
    ),
    (
        "message.removed",
        "EventMessageRemoved",
        {"id": "x", "type": "message.removed", "properties": {"sessionID": "x", "messageID": "x"}},
    ),
    (
        "message.part.updated",
        "EventMessagePartUpdated",
        {
            "id": "x",
            "type": "message.part.updated",
            "properties": {
                "sessionID": "x",
                "part": {"id": "x", "sessionID": "x", "messageID": "x", "type": "text", "text": "x"},
                "time": 1.0,
            },
        },
    ),
    (
        "message.part.removed",
        "EventMessagePartRemoved",
        {
            "id": "x",
            "type": "message.part.removed",
            "properties": {"sessionID": "x", "messageID": "x", "partID": "x"},
        },
    ),
    (
        "models-dev.refreshed",
        "EventModelsDevRefreshed",
        {"id": "x", "type": "models-dev.refreshed", "properties": {}},
    ),
    (
        "session.next.agent.switched",
        "EventSessionNextAgentSwitched",
        {
            "id": "x",
            "type": "session.next.agent.switched",
            "properties": {"timestamp": 1.0, "sessionID": "x", "messageID": "x", "agent": "x"},
        },
    ),
    (
        "session.next.model.switched",
        "EventSessionNextModelSwitched",
        {
            "id": "x",
            "type": "session.next.model.switched",
            "properties": {
                "timestamp": 1.0,
                "sessionID": "x",
                "messageID": "x",
                "model": {"id": "x", "providerID": "x"},
            },
        },
    ),
    (
        "session.next.moved",
        "EventSessionNextMoved",
        {
            "id": "x",
            "type": "session.next.moved",
            "properties": {"timestamp": 1.0, "sessionID": "x", "location": {"directory": "x"}},
        },
    ),
    (
        "session.next.prompted",
        "EventSessionNextPrompted",
        {
            "id": "x",
            "type": "session.next.prompted",
            "properties": {
                "timestamp": 1.0,
                "sessionID": "x",
                "messageID": "x",
                "prompt": {"text": "x"},
                "delivery": "steer",
            },
        },
    ),
    (
        "session.next.prompt.admitted",
        "EventSessionNextPromptAdmitted",
        {
            "id": "x",
            "type": "session.next.prompt.admitted",
            "properties": {
                "timestamp": 1.0,
                "sessionID": "x",
                "messageID": "x",
                "prompt": {"text": "x"},
                "delivery": "steer",
            },
        },
    ),
    (
        "session.next.prompt.promoted",
        "EventSessionNextPromptPromoted",
        {
            "id": "x",
            "type": "session.next.prompt.promoted",
            "properties": {
                "timestamp": 1.0,
                "sessionID": "x",
                "messageID": "x",
                "prompt": {"text": "x"},
                "timeCreated": 1.0,
            },
        },
    ),
    (
        "session.next.context.updated",
        "EventSessionNextContextUpdated",
        {
            "id": "x",
            "type": "session.next.context.updated",
            "properties": {"timestamp": 1.0, "sessionID": "x", "messageID": "x", "text": "x"},
        },
    ),
    (
        "session.next.synthetic",
        "EventSessionNextSynthetic",
        {
            "id": "x",
            "type": "session.next.synthetic",
            "properties": {"timestamp": 1.0, "sessionID": "x", "messageID": "x", "text": "x"},
        },
    ),
    (
        "session.next.shell.started",
        "EventSessionNextShellStarted",
        {
            "id": "x",
            "type": "session.next.shell.started",
            "properties": {
                "timestamp": 1.0,
                "sessionID": "x",
                "messageID": "x",
                "callID": "x",
                "command": "x",
            },
        },
    ),
    (
        "session.next.shell.ended",
        "EventSessionNextShellEnded",
        {
            "id": "x",
            "type": "session.next.shell.ended",
            "properties": {"timestamp": 1.0, "sessionID": "x", "callID": "x", "output": "x"},
        },
    ),
    (
        "session.next.step.started",
        "EventSessionNextStepStarted",
        {
            "id": "x",
            "type": "session.next.step.started",
            "properties": {
                "timestamp": 1.0,
                "sessionID": "x",
                "assistantMessageID": "x",
                "agent": "x",
                "model": {"id": "x", "providerID": "x"},
            },
        },
    ),
    (
        "session.next.step.ended",
        "EventSessionNextStepEnded",
        {
            "id": "x",
            "type": "session.next.step.ended",
            "properties": {
                "timestamp": 1.0,
                "sessionID": "x",
                "assistantMessageID": "x",
                "finish": "x",
                "cost": 1.0,
                "tokens": {
                    "input": 1.0,
                    "output": 1.0,
                    "reasoning": 1.0,
                    "cache": {"read": 1.0, "write": 1.0},
                },
            },
        },
    ),
    (
        "session.next.step.failed",
        "EventSessionNextStepFailed",
        {
            "id": "x",
            "type": "session.next.step.failed",
            "properties": {
                "timestamp": 1.0,
                "sessionID": "x",
                "assistantMessageID": "x",
                "error": {"type": "unknown", "message": "x"},
            },
        },
    ),
    (
        "session.next.text.started",
        "EventSessionNextTextStarted",
        {
            "id": "x",
            "type": "session.next.text.started",
            "properties": {"timestamp": 1.0, "sessionID": "x", "assistantMessageID": "x", "textID": "x"},
        },
    ),
    (
        "session.next.text.delta",
        "EventSessionNextTextDelta",
        {
            "id": "x",
            "type": "session.next.text.delta",
            "properties": {
                "timestamp": 1.0,
                "sessionID": "x",
                "assistantMessageID": "x",
                "textID": "x",
                "delta": "x",
            },
        },
    ),
    (
        "session.next.text.ended",
        "EventSessionNextTextEnded",
        {
            "id": "x",
            "type": "session.next.text.ended",
            "properties": {
                "timestamp": 1.0,
                "sessionID": "x",
                "assistantMessageID": "x",
                "textID": "x",
                "text": "x",
            },
        },
    ),
    (
        "session.next.reasoning.started",
        "EventSessionNextReasoningStarted",
        {
            "id": "x",
            "type": "session.next.reasoning.started",
            "properties": {
                "timestamp": 1.0,
                "sessionID": "x",
                "assistantMessageID": "x",
                "reasoningID": "x",
            },
        },
    ),
    (
        "session.next.reasoning.delta",
        "EventSessionNextReasoningDelta",
        {
            "id": "x",
            "type": "session.next.reasoning.delta",
            "properties": {
                "timestamp": 1.0,
                "sessionID": "x",
                "assistantMessageID": "x",
                "reasoningID": "x",
                "delta": "x",
            },
        },
    ),
    (
        "session.next.reasoning.ended",
        "EventSessionNextReasoningEnded",
        {
            "id": "x",
            "type": "session.next.reasoning.ended",
            "properties": {
                "timestamp": 1.0,
                "sessionID": "x",
                "assistantMessageID": "x",
                "reasoningID": "x",
                "text": "x",
            },
        },
    ),
    (
        "session.next.tool.input.started",
        "EventSessionNextToolInputStarted",
        {
            "id": "x",
            "type": "session.next.tool.input.started",
            "properties": {
                "timestamp": 1.0,
                "sessionID": "x",
                "assistantMessageID": "x",
                "callID": "x",
                "name": "x",
            },
        },
    ),
    (
        "session.next.tool.input.delta",
        "EventSessionNextToolInputDelta",
        {
            "id": "x",
            "type": "session.next.tool.input.delta",
            "properties": {
                "timestamp": 1.0,
                "sessionID": "x",
                "assistantMessageID": "x",
                "callID": "x",
                "delta": "x",
            },
        },
    ),
    (
        "session.next.tool.input.ended",
        "EventSessionNextToolInputEnded",
        {
            "id": "x",
            "type": "session.next.tool.input.ended",
            "properties": {
                "timestamp": 1.0,
                "sessionID": "x",
                "assistantMessageID": "x",
                "callID": "x",
                "text": "x",
            },
        },
    ),
    (
        "session.next.tool.called",
        "EventSessionNextToolCalled",
        {
            "id": "x",
            "type": "session.next.tool.called",
            "properties": {
                "timestamp": 1.0,
                "sessionID": "x",
                "assistantMessageID": "x",
                "callID": "x",
                "tool": "x",
                "input": {},
                "provider": {"executed": False},
            },
        },
    ),
    (
        "session.next.tool.progress",
        "EventSessionNextToolProgress",
        {
            "id": "x",
            "type": "session.next.tool.progress",
            "properties": {
                "timestamp": 1.0,
                "sessionID": "x",
                "assistantMessageID": "x",
                "callID": "x",
                "structured": {},
                "content": [],
            },
        },
    ),
    (
        "session.next.tool.success",
        "EventSessionNextToolSuccess",
        {
            "id": "x",
            "type": "session.next.tool.success",
            "properties": {
                "timestamp": 1.0,
                "sessionID": "x",
                "assistantMessageID": "x",
                "callID": "x",
                "structured": {},
                "content": [],
                "provider": {"executed": False},
            },
        },
    ),
    (
        "session.next.tool.failed",
        "EventSessionNextToolFailed",
        {
            "id": "x",
            "type": "session.next.tool.failed",
            "properties": {
                "timestamp": 1.0,
                "sessionID": "x",
                "assistantMessageID": "x",
                "callID": "x",
                "error": {"type": "unknown", "message": "x"},
                "provider": {"executed": False},
            },
        },
    ),
    (
        "session.next.retried",
        "EventSessionNextRetried",
        {
            "id": "x",
            "type": "session.next.retried",
            "properties": {
                "timestamp": 1.0,
                "sessionID": "x",
                "attempt": 1.0,
                "error": {"message": "x", "isRetryable": False},
            },
        },
    ),
    (
        "session.next.compaction.started",
        "EventSessionNextCompactionStarted",
        {
            "id": "x",
            "type": "session.next.compaction.started",
            "properties": {"timestamp": 1.0, "sessionID": "x", "messageID": "x", "reason": "auto"},
        },
    ),
    (
        "session.next.compaction.delta",
        "EventSessionNextCompactionDelta",
        {
            "id": "x",
            "type": "session.next.compaction.delta",
            "properties": {"timestamp": 1.0, "sessionID": "x", "text": "x"},
        },
    ),
    (
        "session.next.compaction.ended",
        "EventSessionNextCompactionEnded",
        {
            "id": "x",
            "type": "session.next.compaction.ended",
            "properties": {"timestamp": 1.0, "sessionID": "x", "text": "x"},
        },
    ),
    (
        "permission.v2.asked",
        "EventPermissionV2Asked",
        {
            "id": "x",
            "type": "permission.v2.asked",
            "properties": {"id": "x", "sessionID": "x", "action": "x", "resources": []},
        },
    ),
    (
        "permission.v2.replied",
        "EventPermissionV2Replied",
        {
            "id": "x",
            "type": "permission.v2.replied",
            "properties": {"sessionID": "x", "requestID": "x", "reply": "once"},
        },
    ),
    (
        "account.added",
        "EventAccountAdded",
        {
            "id": "x",
            "type": "account.added",
            "properties": {
                "account": {
                    "id": "x",
                    "serviceID": "x",
                    "description": "x",
                    "credential": {"type": "oauth", "refresh": "x", "access": "x", "expires": 1},
                }
            },
        },
    ),
    (
        "account.removed",
        "EventAccountRemoved",
        {
            "id": "x",
            "type": "account.removed",
            "properties": {
                "account": {
                    "id": "x",
                    "serviceID": "x",
                    "description": "x",
                    "credential": {"type": "oauth", "refresh": "x", "access": "x", "expires": 1},
                }
            },
        },
    ),
    (
        "account.switched",
        "EventAccountSwitched",
        {"id": "x", "type": "account.switched", "properties": {"serviceID": "x"}},
    ),
    (
        "permission.asked",
        "EventPermissionAsked",
        {
            "id": "x",
            "type": "permission.asked",
            "properties": {
                "id": "x",
                "sessionID": "x",
                "permission": "x",
                "patterns": [],
                "metadata": {},
                "always": [],
            },
        },
    ),
    (
        "permission.replied",
        "EventPermissionReplied",
        {
            "id": "x",
            "type": "permission.replied",
            "properties": {"sessionID": "x", "requestID": "x", "reply": "once"},
        },
    ),
    (
        "message.part.delta",
        "EventMessagePartDelta",
        {
            "id": "x",
            "type": "message.part.delta",
            "properties": {
                "sessionID": "x",
                "messageID": "x",
                "partID": "x",
                "field": "x",
                "delta": "x",
            },
        },
    ),
    (
        "session.diff",
        "EventSessionDiff",
        {"id": "x", "type": "session.diff", "properties": {"sessionID": "x", "diff": []}},
    ),
    ("session.error", "EventSessionError", {"id": "x", "type": "session.error", "properties": {}}),
    ("lsp.updated", "EventLspUpdated", {"id": "x", "type": "lsp.updated", "properties": {}}),
    (
        "file.watcher.updated",
        "EventFileWatcherUpdated",
        {"id": "x", "type": "file.watcher.updated", "properties": {"file": "x", "event": "add"}},
    ),
    ("file.edited", "EventFileEdited", {"id": "x", "type": "file.edited", "properties": {"file": "x"}}),
    (
        "pty.created",
        "EventPtyCreated",
        {
            "id": "x",
            "type": "pty.created",
            "properties": {
                "info": {
                    "id": "x",
                    "title": "x",
                    "command": "x",
                    "args": [],
                    "cwd": "x",
                    "status": "running",
                    "pid": 1,
                }
            },
        },
    ),
    (
        "pty.updated",
        "EventPtyUpdated",
        {
            "id": "x",
            "type": "pty.updated",
            "properties": {
                "info": {
                    "id": "x",
                    "title": "x",
                    "command": "x",
                    "args": [],
                    "cwd": "x",
                    "status": "running",
                    "pid": 1,
                }
            },
        },
    ),
    (
        "pty.exited",
        "EventPtyExited",
        {"id": "x", "type": "pty.exited", "properties": {"id": "x", "exitCode": 1}},
    ),
    ("pty.deleted", "EventPtyDeleted", {"id": "x", "type": "pty.deleted", "properties": {"id": "x"}}),
    (
        "question.v2.asked",
        "EventQuestionV2Asked",
        {
            "id": "x",
            "type": "question.v2.asked",
            "properties": {"id": "x", "sessionID": "x", "questions": []},
        },
    ),
    (
        "question.v2.replied",
        "EventQuestionV2Replied",
        {
            "id": "x",
            "type": "question.v2.replied",
            "properties": {"sessionID": "x", "requestID": "x", "answers": []},
        },
    ),
    (
        "question.v2.rejected",
        "EventQuestionV2Rejected",
        {"id": "x", "type": "question.v2.rejected", "properties": {"sessionID": "x", "requestID": "x"}},
    ),
    (
        "todo.updated",
        "EventTodoUpdated",
        {"id": "x", "type": "todo.updated", "properties": {"sessionID": "x", "todos": []}},
    ),
    (
        "installation.updated",
        "EventInstallationUpdated",
        {"id": "x", "type": "installation.updated", "properties": {"version": "x"}},
    ),
    (
        "installation.update-available",
        "EventInstallationUpdateAvailable",
        {"id": "x", "type": "installation.update-available", "properties": {"version": "x"}},
    ),
    (
        "tui.prompt.append",
        "EventTuiPromptAppend",
        {"id": "x", "type": "tui.prompt.append", "properties": {"text": "x"}},
    ),
    (
        "tui.command.execute",
        "EventTuiCommandExecute",
        {"id": "x", "type": "tui.command.execute", "properties": {"command": "session.list"}},
    ),
    (
        "tui.toast.show",
        "EventTuiToastShow",
        {"id": "x", "type": "tui.toast.show", "properties": {"message": "x", "variant": "info"}},
    ),
    (
        "tui.session.select",
        "EventTuiSessionSelect",
        {"id": "x", "type": "tui.session.select", "properties": {"sessionID": "x"}},
    ),
    (
        "mcp.tools.changed",
        "EventMcpToolsChanged",
        {"id": "x", "type": "mcp.tools.changed", "properties": {"server": "x"}},
    ),
    (
        "mcp.browser.open.failed",
        "EventMcpBrowserOpenFailed",
        {"id": "x", "type": "mcp.browser.open.failed", "properties": {"mcpName": "x", "url": "x"}},
    ),
    (
        "question.asked",
        "EventQuestionAsked",
        {"id": "x", "type": "question.asked", "properties": {"id": "x", "sessionID": "x", "questions": []}},
    ),
    (
        "question.replied",
        "EventQuestionReplied",
        {
            "id": "x",
            "type": "question.replied",
            "properties": {"sessionID": "x", "requestID": "x", "answers": []},
        },
    ),
    (
        "question.rejected",
        "EventQuestionRejected",
        {"id": "x", "type": "question.rejected", "properties": {"sessionID": "x", "requestID": "x"}},
    ),
    (
        "command.executed",
        "EventCommandExecuted",
        {
            "id": "x",
            "type": "command.executed",
            "properties": {"name": "x", "sessionID": "x", "arguments": "x", "messageID": "x"},
        },
    ),
    (
        "session.status",
        "EventSessionStatus",
        {"id": "x", "type": "session.status", "properties": {"sessionID": "x", "status": {"type": "idle"}}},
    ),
    (
        "session.idle",
        "EventSessionIdle",
        {"id": "x", "type": "session.idle", "properties": {"sessionID": "x"}},
    ),
    (
        "session.compacted",
        "EventSessionCompacted",
        {"id": "x", "type": "session.compacted", "properties": {"sessionID": "x"}},
    ),
    (
        "project.directories.updated",
        "EventProjectDirectoriesUpdated",
        {"id": "x", "type": "project.directories.updated", "properties": {"projectID": "x"}},
    ),
    (
        "project.updated",
        "EventProjectUpdated",
        {
            "id": "x",
            "type": "project.updated",
            "properties": {
                "id": "x",
                "worktree": "x",
                "time": {"created": 1, "updated": 1},
                "sandboxes": [],
            },
        },
    ),
    ("vcs.branch.updated", "EventVcsBranchUpdated", {"id": "x", "type": "vcs.branch.updated", "properties": {}}),
    (
        "workspace.ready",
        "EventWorkspaceReady",
        {"id": "x", "type": "workspace.ready", "properties": {"name": "x"}},
    ),
    (
        "workspace.failed",
        "EventWorkspaceFailed",
        {"id": "x", "type": "workspace.failed", "properties": {"message": "x"}},
    ),
    (
        "workspace.status",
        "EventWorkspaceStatus",
        {"id": "x", "type": "workspace.status", "properties": {"workspaceID": "x", "status": "connected"}},
    ),
    (
        "worktree.ready",
        "EventWorktreeReady",
        {"id": "x", "type": "worktree.ready", "properties": {"name": "x"}},
    ),
    (
        "worktree.failed",
        "EventWorktreeFailed",
        {"id": "x", "type": "worktree.failed", "properties": {"message": "x"}},
    ),
    ("server.connected", "EventServerConnected", {"id": "x", "type": "server.connected", "properties": {}}),
    ("global.disposed", "EventGlobalDisposed", {"id": "x", "type": "global.disposed", "properties": {}}),
    (
        "server.instance.disposed",
        "EventServerInstanceDisposed",
        {"id": "x", "type": "server.instance.disposed", "properties": {"directory": "x"}},
    ),
]


def test_known_streaming_delta_variant_resolves() -> None:
    # EventSessionNextTextDelta is one of the new session-next streaming variants.
    payload = {
        "id": "evt_1",
        "type": "session.next.text.delta",
        "properties": {
            "timestamp": 1.0,
            "sessionID": "ses_1",
            "assistantMessageID": "msg_1",
            "textID": "txt_1",
            "delta": "hello",
        },
    }
    ev = construct_type(type_=EventListResponse, value=payload)
    assert type(ev).__name__ == "EventSessionNextTextDelta"


def test_sanitized_name_variant_resolves() -> None:
    # Schema name `Event.tui.prompt.append` (type "tui.prompt.append") sanitizes
    # to class `EventTuiPromptAppend`.
    payload = {"id": "evt_1", "type": "tui.prompt.append", "properties": {"text": "hello"}}
    ev = construct_type(type_=EventListResponse, value=payload)
    assert type(ev).__name__ == "EventTuiPromptAppend"


def test_session_error_resolves() -> None:
    payload: Dict[str, Any] = {"id": "evt_1", "type": "session.error", "properties": {}}
    ev = construct_type(type_=EventListResponse, value=payload)
    assert type(ev).__name__ == "EventSessionError"


def test_session_idle_resolves() -> None:
    payload = {"id": "evt_1", "type": "session.idle", "properties": {"sessionID": "ses_1"}}
    ev = construct_type(type_=EventListResponse, value=payload)
    assert type(ev).__name__ == "EventSessionIdle"


def test_message_updated_resolves() -> None:
    payload: Dict[str, Any] = {
        "id": "evt_1",
        "type": "message.updated",
        "properties": {
            "sessionID": "ses_1",
            "info": {
                "id": "msg_1",
                "sessionID": "ses_1",
                "role": "user",
                "time": {"created": 1.0},
                "agent": "build",
                "model": {"providerID": "anthropic", "modelID": "claude"},
            },
        },
    }
    ev = construct_type(type_=EventListResponse, value=payload)
    assert type(ev).__name__ == "EventMessageUpdated"


def test_unknown_still_falls_back() -> None:
    ev = construct_type(type_=EventListResponse, value={"type": "not.a.real.event", "properties": {}})
    assert type(ev).__name__ == "EventUnknown"


def test_all_87_variants_resolve_to_their_own_class() -> None:
    assert len(EVENT_VARIANT_SAMPLES) == 87
    wire_types = {sample[0] for sample in EVENT_VARIANT_SAMPLES}
    assert len(wire_types) == 87, "expected 87 distinct wire `type` values"

    for wire_type, expected_class_name, payload in EVENT_VARIANT_SAMPLES:
        ev = construct_type(type_=EventListResponse, value=payload)
        actual_class_name = type(ev).__name__
        assert actual_class_name == expected_class_name, (
            f"type={wire_type!r} resolved to {actual_class_name}, expected {expected_class_name}"
        )
        assert actual_class_name != "EventUnknown"
