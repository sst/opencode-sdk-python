from opencode_ai.types import Session
from opencode_ai._models import construct_type

SESSION_PAYLOAD = {
    "id": "ses_1",
    "slug": "my-session",
    "projectID": "prj_1",
    "workspaceID": "wrk_1",
    "directory": "/home/user/project",
    "path": "/home/user/project",
    "parentID": "ses_0",
    "summary": {
        "additions": 10.0,
        "deletions": 2.0,
        "files": 3.0,
        "diffs": [{"file": "a.py", "patch": "@@", "additions": 10.0, "deletions": 2.0, "status": "modified"}],
    },
    "cost": 0.05,
    "tokens": {
        "input": 100.0,
        "output": 50.0,
        "reasoning": 0.0,
        "cache": {"read": 10.0, "write": 5.0},
    },
    "share": {"url": "https://example.com/s/ses_1"},
    "title": "My Session",
    "agent": "build",
    "model": {"id": "claude-opus-4-8", "providerID": "anthropic", "variant": "default"},
    "version": "1.0.0",
    "metadata": {"foo": "bar"},
    "time": {"created": 1.0, "updated": 2.0, "compacting": 1.5, "archived": 3.0},
    "permission": [{"action": "allow", "pattern": "*", "permission": "edit"}],
    "revert": {"messageID": "msg_1", "partID": "prt_1", "snapshot": "snap", "diff": "diff"},
}


def test_session_parses_current_shape() -> None:
    msg = construct_type(type_=Session, value=SESSION_PAYLOAD)
    assert msg.slug == "my-session"
    assert msg.project_id == "prj_1"
    assert msg.workspace_id == "wrk_1"
    assert msg.directory == "/home/user/project"
    assert msg.path == "/home/user/project"
    assert msg.cost == 0.05
    assert msg.tokens.input == 100.0
    assert msg.tokens.cache.read == 10.0
    assert msg.agent == "build"
    assert msg.model.id == "claude-opus-4-8"
    assert msg.model.provider_id == "anthropic"
    assert msg.metadata == {"foo": "bar"}
    assert msg.time.created == 1.0
    assert msg.time.updated == 2.0
    assert msg.time.compacting == 1.5
    assert msg.time.archived == 3.0
    assert msg.summary.additions == 10.0
    assert msg.summary.diffs[0].file == "a.py"
    assert msg.permission[0].action == "allow"
    assert msg.permission[0].pattern == "*"
    assert msg.permission[0].permission == "edit"


def test_session_minimal_required_fields() -> None:
    minimal = {
        "id": "ses_2",
        "slug": "min",
        "projectID": "prj_2",
        "directory": "/dir",
        "title": "Minimal",
        "version": "1.0.0",
        "time": {"created": 1.0, "updated": 2.0},
    }
    msg = construct_type(type_=Session, value=minimal)
    assert msg.id == "ses_2"
    assert msg.workspace_id is None
    assert msg.summary is None
    assert msg.tokens is None
    assert msg.permission is None
