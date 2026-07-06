from typing import Any, Dict, cast

from opencode_ai.types import McpLocalConfig, McpRemoteConfig
from opencode_ai._models import construct_type

LOCAL_PAYLOAD: Dict[str, Any] = {
    "type": "local",
    "command": ["node", "server.js"],
    "enabled": True,
    "environment": {"FOO": "bar"},
    "timeout": 5000,
}

REMOTE_PAYLOAD: Dict[str, Any] = {
    "type": "remote",
    "url": "https://example.com/mcp",
    "enabled": True,
    "headers": {"Authorization": "Bearer token"},
    "timeout": 5000,
    "oauth": {
        "clientId": "client-123",
        "clientSecret": "secret-456",
        "scope": "read write",
        "callbackPort": 8080,
        "redirectUri": "https://example.com/callback",
    },
}

REMOTE_PAYLOAD_OAUTH_DISABLED: Dict[str, Any] = {
    "type": "remote",
    "url": "https://example.com/mcp",
    "oauth": False,
}


def test_local_config_parses_timeout() -> None:
    cfg = cast(McpLocalConfig, construct_type(type_=McpLocalConfig, value=LOCAL_PAYLOAD))
    assert cfg.type == "local"
    assert cfg.command == ["node", "server.js"]
    assert cfg.enabled is True
    assert cfg.environment == {"FOO": "bar"}
    assert cfg.timeout == 5000


def test_local_config_timeout_optional() -> None:
    minimal: Dict[str, Any] = {"type": "local", "command": ["node"]}
    cfg = cast(McpLocalConfig, construct_type(type_=McpLocalConfig, value=minimal))
    assert cfg.timeout is None


def test_remote_config_parses_timeout_and_oauth() -> None:
    cfg = cast(McpRemoteConfig, construct_type(type_=McpRemoteConfig, value=REMOTE_PAYLOAD))
    assert cfg.type == "remote"
    assert cfg.url == "https://example.com/mcp"
    assert cfg.timeout == 5000
    assert cfg.oauth is not None
    oauth = cfg.oauth
    assert not isinstance(oauth, bool)
    assert oauth.client_id == "client-123"
    assert oauth.client_secret == "secret-456"
    assert oauth.scope == "read write"
    assert oauth.callback_port == 8080
    assert oauth.redirect_uri == "https://example.com/callback"


def test_remote_config_oauth_disabled() -> None:
    cfg = cast(McpRemoteConfig, construct_type(type_=McpRemoteConfig, value=REMOTE_PAYLOAD_OAUTH_DISABLED))
    assert cfg.oauth is False


def test_remote_config_timeout_and_oauth_optional() -> None:
    minimal: Dict[str, Any] = {"type": "remote", "url": "https://example.com/mcp"}
    cfg = cast(McpRemoteConfig, construct_type(type_=McpRemoteConfig, value=minimal))
    assert cfg.timeout is None
    assert cfg.oauth is None
