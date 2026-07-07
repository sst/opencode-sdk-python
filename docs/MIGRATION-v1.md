# Migrating to the v1-correctness release (0.2.0)

This release realigns the SDK with the current opencode server API. It removes a few
methods that no longer exist server-side, renames one method, and corrects two shared
message models. There is no change to how the client is constructed or authenticated.

## 1. `session.chat` is now `session.prompt`

The request shape changed (nested `model`, `mode` renamed to `agent`) and the response
is now a wrapper object instead of a bare message.

Before:

```python
result = client.session.chat(
    id="ses_1",
    model_id="claude-3-5-sonnet",
    provider_id="anthropic",
    mode="build",
    parts=[{"type": "text", "text": "hello"}],
)
# `result` was the assistant message itself
print(result.id)
```

After:

```python
result = client.session.prompt(
    "ses_1",
    model={"provider_id": "anthropic", "model_id": "claude-3-5-sonnet"},
    agent="build",
    parts=[{"type": "text", "text": "hello"}],
)
# `result` is {info, parts}
print(result.info.id)
print(result.parts)
```

`result.info` holds the assistant message metadata (what `session.chat` used to return
directly); `result.parts` holds the content parts. New optional request fields are also
available: `message_id`, `no_reply`, `tools`, `system`, and `variant`. A `format` field
is not yet exposed on the request.

## 2. `file.read` is split into `file.list` and `file.content`

`GET /file` used to return file content. It now returns a directory listing, and a new
endpoint, `GET /file/content`, returns content.

Before:

```python
result = client.file.read(path="a.py")
print(result.content, result.type)
```

After:

```python
# Directory listing (new), GET /file
nodes = client.file.list(path="src")

# File content, GET /file/content
result = client.file.content(path="a.py")
print(result.content, result.type)  # same shape as before: type is "text" or "binary"
```

`FileContentResponse` also carries optional `diff`/`patch`/`encoding`/`mimeType` fields
that were not present on the old `file.read` response.

## 3. Removed and renamed `app` methods

The server no longer exposes `GET /app` or `POST /app/init`, so `client.app.get()` and
`client.app.init()` are removed with no replacement. `client.app.modes()` is replaced
by `client.app.agents()`. A new `client.app.skills()` method is available.

Before:

```python
info = client.app.get()
client.app.init()
modes = client.app.modes()
```

After:

```python
agents = client.app.agents()  # GET /agent, replaces app.modes()
skills = client.app.skills()  # GET /skill, new
# app.get() and app.init() have no replacement; the server dropped both endpoints.
```

## 4. `AssistantMessage` and `UserMessage` field changes

Both shared message models were corrected to match the current spec. Code that builds
these models directly, or that reads every field exhaustively (for example, an
exhaustive `match`/`if` chain, or strict schema validation), needs to be updated.

`AssistantMessage`:

- `system` field removed.
- `parentID` (`parent_id` in Python) and `agent` are now required, not optional.
- `structured`, `variant`, and `finish` fields added.
- `tokens.total` field added.

`UserMessage`:

- Now requires `model` (a `{provider_id, model_id}` object) and `agent`.

Before:

```python
# AssistantMessage.system existed; parent_id/agent were optional
msg = AssistantMessage(
    id="msg_1",
    role="assistant",
    session_id="ses_1",
    system=["be helpful"],
    ...,
)
```

After:

```python
# system is gone; parent_id and agent are required
msg = AssistantMessage(
    id="msg_1",
    role="assistant",
    session_id="ses_1",
    parent_id="msg_0",
    agent="build",
    ...,
)
```

If you only read these models as returned by the SDK (the common case), no action is
needed beyond dropping any code that reads `AssistantMessage.system`.

## Additive changes (non-breaking)

These do not require code changes but are worth knowing about:

- The event stream now tolerates unknown event variant types by deserializing them to
  a permissive fallback instead of raising an error.
- `client.session.list` gained optional `scope`, `path`, `roots`, `start`, `search`,
  and `limit` parameters.
- `client.session.messages` gained optional `before` and `limit` parameters.
- `client.session.summarize` gained an optional `auto` parameter.
