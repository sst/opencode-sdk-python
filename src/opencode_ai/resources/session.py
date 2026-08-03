# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing import Any, Dict, Iterable, cast
from typing_extensions import Literal

import httpx

from ..types import (
    addressing_params,
    session_diff_params,
    session_fork_params,
    session_init_params,
    session_list_params,
    session_shell_params,
    session_prompt_params,
    session_revert_params,
    session_update_params,
    session_command_params,
    session_messages_params,
    session_summarize_params,
    session_update_part_params,
    session_prompt_async_params,
    session_respond_permission_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.part import Part
from .._base_client import make_request_options
from ..types.session import Session
from ..types.file_part_input_param import FilePartInputParam
from ..types.session_diff_response import SessionDiffResponse
from ..types.session_init_response import SessionInitResponse
from ..types.session_list_response import SessionListResponse
from ..types.session_todo_response import SessionTodoResponse
from ..types.session_abort_response import SessionAbortResponse
from ..types.session_shell_response import SessionShellResponse
from ..types.session_delete_response import SessionDeleteResponse
from ..types.session_prompt_response import SessionPromptResponse
from ..types.session_status_response import SessionStatusResponse
from ..types.session_command_response import SessionCommandResponse
from ..types.session_children_response import SessionChildrenResponse
from ..types.session_messages_response import SessionMessagesResponse, SessionMessagesResponseItem
from ..types.session_summarize_response import SessionSummarizeResponse
from ..types.session_delete_part_response import SessionDeletePartResponse
from ..types.session_delete_message_response import SessionDeleteMessageResponse
from ..types.session_respond_permission_response import SessionRespondPermissionResponse

__all__ = ["SessionResource", "AsyncSessionResource"]


class SessionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SessionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SessionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return SessionResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """Create a new session"""
        return self._post(
            "/session",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=Session,
        )

    def list(
        self,
        *,
        limit: float | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        roots: bool | NotGiven = NOT_GIVEN,
        scope: Literal["project"] | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        start: float | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionListResponse:
        """
        List all sessions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/session",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "path": path,
                        "roots": roots,
                        "scope": scope,
                        "search": search,
                        "start": start,
                        "directory": directory,
                        "workspace": workspace,
                    },
                    session_list_params.SessionListParams,
                ),
            ),
            cast_to=SessionListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionDeleteResponse:
        """
        Delete a session and all its data

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/session/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SessionDeleteResponse,
        )

    def abort(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionAbortResponse:
        """
        Abort a session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/session/{id}/abort",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SessionAbortResponse,
        )

    def prompt(
        self,
        id: str,
        *,
        parts: Iterable[session_prompt_params.Part],
        agent: str | NotGiven = NOT_GIVEN,
        message_id: str | NotGiven = NOT_GIVEN,
        model: session_prompt_params.Model | NotGiven = NOT_GIVEN,
        no_reply: bool | NotGiven = NOT_GIVEN,
        system: str | NotGiven = NOT_GIVEN,
        tools: Dict[str, bool] | NotGiven = NOT_GIVEN,
        variant: str | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionPromptResponse:
        """
        Create and send a new message to a session

        Args:
          id: Session ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/session/{id}/message",
            body=maybe_transform(
                {
                    "parts": parts,
                    "model": model,
                    "agent": agent,
                    "message_id": message_id,
                    "no_reply": no_reply,
                    "tools": tools,
                    "system": system,
                    "variant": variant,
                    # "format": format,
                },
                session_prompt_params.SessionPromptParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SessionPromptResponse,
        )

    def init(
        self,
        id: str,
        *,
        message_id: str,
        model_id: str,
        provider_id: str,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionInitResponse:
        """
        Analyze the app and create an AGENTS.md file

        Args:
          id: Session ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/session/{id}/init",
            body=maybe_transform(
                {
                    "message_id": message_id,
                    "model_id": model_id,
                    "provider_id": provider_id,
                },
                session_init_params.SessionInitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SessionInitResponse,
        )

    def messages(
        self,
        id: str,
        *,
        before: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionMessagesResponse:
        """
        List messages for a session

        Args:
          id: Session ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/session/{id}/message",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "before": before,
                        "limit": limit,
                        "directory": directory,
                        "workspace": workspace,
                    },
                    session_messages_params.SessionMessagesParams,
                ),
            ),
            cast_to=SessionMessagesResponse,
        )

    def revert(
        self,
        id: str,
        *,
        message_id: str,
        part_id: str | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Revert a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/session/{id}/revert",
            body=maybe_transform(
                {
                    "message_id": message_id,
                    "part_id": part_id,
                },
                session_revert_params.SessionRevertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=Session,
        )

    def share(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Share a session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/session/{id}/share",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=Session,
        )

    def summarize(
        self,
        id: str,
        *,
        model_id: str,
        provider_id: str,
        auto: bool | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionSummarizeResponse:
        """
        Summarize the session

        Args:
          id: Session ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/session/{id}/summarize",
            body=maybe_transform(
                {
                    "model_id": model_id,
                    "provider_id": provider_id,
                    "auto": auto,
                },
                session_summarize_params.SessionSummarizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SessionSummarizeResponse,
        )

    def unrevert(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Restore all reverted messages

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/session/{id}/unrevert",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=Session,
        )

    def unshare(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Unshare the session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/session/{id}/share",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=Session,
        )

    def status(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionStatusResponse:
        """Get the status of every active session, keyed by session ID"""
        return self._get(
            "/session/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SessionStatusResponse,
        )

    def get(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Get a session by ID

        Args:
          id: Session ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/session/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=Session,
        )

    def update(
        self,
        id: str,
        *,
        metadata: object | NotGiven = NOT_GIVEN,
        permission: Iterable[session_update_params.Permission] | NotGiven = NOT_GIVEN,
        time: session_update_params.Time | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Update session properties such as its title, metadata, permission
        overrides, or archived timestamp

        Args:
          id: Session ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/session/{id}",
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "permission": permission,
                    "time": time,
                    "title": title,
                },
                session_update_params.SessionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=Session,
        )

    def children(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionChildrenResponse:
        """
        List the direct child sessions forked from this session

        Args:
          id: Session ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/session/{id}/children",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SessionChildrenResponse,
        )

    def command(
        self,
        id: str,
        *,
        arguments: str,
        command: str,
        agent: str | NotGiven = NOT_GIVEN,
        message_id: str | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        parts: Iterable[FilePartInputParam] | NotGiven = NOT_GIVEN,
        variant: str | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionCommandResponse:
        """
        Run a slash command within a session

        Args:
          id: Session ID

          arguments: Raw command arguments

          command: Command name to execute

          model: Model in `providerID/modelID` string form

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/session/{id}/command",
            body=maybe_transform(
                {
                    "arguments": arguments,
                    "command": command,
                    "agent": agent,
                    "message_id": message_id,
                    "model": model,
                    "parts": parts,
                    "variant": variant,
                },
                session_command_params.SessionCommandParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SessionCommandResponse,
        )

    def diff(
        self,
        id: str,
        *,
        message_id: str | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionDiffResponse:
        """
        Get the file diffs produced by a session, optionally only up to a given
        message

        Args:
          id: Session ID

          message_id: Only include diffs up to this message ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/session/{id}/diff",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "message_id": message_id,
                        "directory": directory,
                        "workspace": workspace,
                    },
                    session_diff_params.SessionDiffParams,
                ),
            ),
            cast_to=SessionDiffResponse,
        )

    def fork(
        self,
        id: str,
        *,
        message_id: str | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Fork a session, optionally only up to a given message

        Args:
          id: Session ID

          message_id: Fork up to (and including) this message ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/session/{id}/fork",
            body=maybe_transform({"message_id": message_id}, session_fork_params.SessionForkParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=Session,
        )

    def delete_message(
        self,
        id: str,
        *,
        message_id: str,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionDeleteMessageResponse:
        """
        Delete a message (and its parts) from a session

        Args:
          id: Session ID

          message_id: Message ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._delete(
            f"/session/{id}/message/{message_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SessionDeleteMessageResponse,
        )

    def get_message(
        self,
        id: str,
        *,
        message_id: str,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionMessagesResponseItem:
        """
        Get a single message (with its parts) from a session

        Args:
          id: Session ID

          message_id: Message ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get(
            f"/session/{id}/message/{message_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SessionMessagesResponseItem,
        )

    def delete_part(
        self,
        id: str,
        *,
        message_id: str,
        part_id: str,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionDeletePartResponse:
        """
        Delete a part from a message

        Args:
          id: Session ID

          message_id: Message ID

          part_id: Part ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        if not part_id:
            raise ValueError(f"Expected a non-empty value for `part_id` but received {part_id!r}")
        return self._delete(
            f"/session/{id}/message/{message_id}/part/{part_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SessionDeletePartResponse,
        )

    def update_part(
        self,
        id: str,
        *,
        message_id: str,
        part_id: str,
        part: session_update_part_params.SessionUpdatePartParams,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Part:
        """
        Replace a message part with a new value.

        The request body is a *complete* replacement `Part` object (matching one
        of the `Part` union's variants), not a partial patch -- typically a
        caller GETs the part first (e.g. via `get_message`), edits the fields it
        wants to change, and PATCHes the whole object back.

        Args:
          id: Session ID

          message_id: Message ID

          part_id: Part ID

          part: The full replacement part, matching one of the `Part` union's variants

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        if not part_id:
            raise ValueError(f"Expected a non-empty value for `part_id` but received {part_id!r}")
        return cast(
            Part,
            self._patch(
                f"/session/{id}/message/{message_id}/part/{part_id}",
                body=maybe_transform(part, session_update_part_params.SessionUpdatePartParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "directory": directory,
                            "workspace": workspace,
                        },
                        addressing_params.AddressingParams,
                    ),
                ),
                cast_to=cast(Any, Part),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def respond_permission(
        self,
        id: str,
        *,
        permission_id: str,
        response: Literal["once", "always", "reject"],
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionRespondPermissionResponse:
        """
        Respond to a pending permission request for a session.

        Deprecated: the spec marks `permission.respond` as `deprecated: true`.
        Retained for backwards compatibility.

        Args:
          id: Session ID

          permission_id: Permission ID

          response: How to resolve the permission request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not permission_id:
            raise ValueError(f"Expected a non-empty value for `permission_id` but received {permission_id!r}")
        return self._post(
            f"/session/{id}/permissions/{permission_id}",
            body=maybe_transform(
                {"response": response}, session_respond_permission_params.SessionRespondPermissionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SessionRespondPermissionResponse,
        )

    def prompt_async(
        self,
        id: str,
        *,
        parts: Iterable[session_prompt_async_params.Part],
        agent: str | NotGiven = NOT_GIVEN,
        format: session_prompt_async_params.Format | NotGiven = NOT_GIVEN,
        message_id: str | NotGiven = NOT_GIVEN,
        model: session_prompt_async_params.Model | NotGiven = NOT_GIVEN,
        no_reply: bool | NotGiven = NOT_GIVEN,
        system: str | NotGiven = NOT_GIVEN,
        tools: Dict[str, bool] | NotGiven = NOT_GIVEN,
        variant: str | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Send a new message to a session without waiting for the assistant's
        reply (accepted asynchronously; the server responds `204 No Content`).

        Args:
          id: Session ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/session/{id}/prompt_async",
            body=maybe_transform(
                {
                    "parts": parts,
                    "agent": agent,
                    "format": format,
                    "message_id": message_id,
                    "model": model,
                    "no_reply": no_reply,
                    "system": system,
                    "tools": tools,
                    "variant": variant,
                },
                session_prompt_async_params.SessionPromptAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=NoneType,
        )

    def shell(
        self,
        id: str,
        *,
        agent: str,
        command: str,
        message_id: str | NotGiven = NOT_GIVEN,
        model: session_shell_params.Model | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionShellResponse:
        """
        Run a shell command within a session

        Args:
          id: Session ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/session/{id}/shell",
            body=maybe_transform(
                {
                    "agent": agent,
                    "command": command,
                    "message_id": message_id,
                    "model": model,
                },
                session_shell_params.SessionShellParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SessionShellResponse,
        )

    def todo(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionTodoResponse:
        """
        List the todo items tracked for a session

        Args:
          id: Session ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/session/{id}/todo",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SessionTodoResponse,
        )


class AsyncSessionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSessionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSessionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncSessionResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """Create a new session"""
        return await self._post(
            "/session",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=Session,
        )

    async def list(
        self,
        *,
        limit: float | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        roots: bool | NotGiven = NOT_GIVEN,
        scope: Literal["project"] | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        start: float | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionListResponse:
        """
        List all sessions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/session",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "path": path,
                        "roots": roots,
                        "scope": scope,
                        "search": search,
                        "start": start,
                        "directory": directory,
                        "workspace": workspace,
                    },
                    session_list_params.SessionListParams,
                ),
            ),
            cast_to=SessionListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionDeleteResponse:
        """
        Delete a session and all its data

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/session/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SessionDeleteResponse,
        )

    async def abort(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionAbortResponse:
        """
        Abort a session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/session/{id}/abort",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SessionAbortResponse,
        )

    async def prompt(
        self,
        id: str,
        *,
        parts: Iterable[session_prompt_params.Part],
        agent: str | NotGiven = NOT_GIVEN,
        message_id: str | NotGiven = NOT_GIVEN,
        model: session_prompt_params.Model | NotGiven = NOT_GIVEN,
        no_reply: bool | NotGiven = NOT_GIVEN,
        system: str | NotGiven = NOT_GIVEN,
        tools: Dict[str, bool] | NotGiven = NOT_GIVEN,
        variant: str | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionPromptResponse:
        """
        Create and send a new message to a session

        Args:
          id: Session ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/session/{id}/message",
            body=await async_maybe_transform(
                {
                    "parts": parts,
                    "model": model,
                    "agent": agent,
                    "message_id": message_id,
                    "no_reply": no_reply,
                    "tools": tools,
                    "system": system,
                    "variant": variant,
                    # "format": format,
                },
                session_prompt_params.SessionPromptParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SessionPromptResponse,
        )

    async def init(
        self,
        id: str,
        *,
        message_id: str,
        model_id: str,
        provider_id: str,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionInitResponse:
        """
        Analyze the app and create an AGENTS.md file

        Args:
          id: Session ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/session/{id}/init",
            body=await async_maybe_transform(
                {
                    "message_id": message_id,
                    "model_id": model_id,
                    "provider_id": provider_id,
                },
                session_init_params.SessionInitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SessionInitResponse,
        )

    async def messages(
        self,
        id: str,
        *,
        before: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionMessagesResponse:
        """
        List messages for a session

        Args:
          id: Session ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/session/{id}/message",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "before": before,
                        "limit": limit,
                        "directory": directory,
                        "workspace": workspace,
                    },
                    session_messages_params.SessionMessagesParams,
                ),
            ),
            cast_to=SessionMessagesResponse,
        )

    async def revert(
        self,
        id: str,
        *,
        message_id: str,
        part_id: str | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Revert a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/session/{id}/revert",
            body=await async_maybe_transform(
                {
                    "message_id": message_id,
                    "part_id": part_id,
                },
                session_revert_params.SessionRevertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=Session,
        )

    async def share(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Share a session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/session/{id}/share",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=Session,
        )

    async def summarize(
        self,
        id: str,
        *,
        model_id: str,
        provider_id: str,
        auto: bool | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionSummarizeResponse:
        """
        Summarize the session

        Args:
          id: Session ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/session/{id}/summarize",
            body=await async_maybe_transform(
                {
                    "model_id": model_id,
                    "provider_id": provider_id,
                    "auto": auto,
                },
                session_summarize_params.SessionSummarizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SessionSummarizeResponse,
        )

    async def unrevert(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Restore all reverted messages

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/session/{id}/unrevert",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=Session,
        )

    async def unshare(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Unshare the session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/session/{id}/share",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=Session,
        )

    async def status(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionStatusResponse:
        """Get the status of every active session, keyed by session ID"""
        return await self._get(
            "/session/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SessionStatusResponse,
        )

    async def get(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Get a session by ID

        Args:
          id: Session ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/session/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=Session,
        )

    async def update(
        self,
        id: str,
        *,
        metadata: object | NotGiven = NOT_GIVEN,
        permission: Iterable[session_update_params.Permission] | NotGiven = NOT_GIVEN,
        time: session_update_params.Time | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Update session properties such as its title, metadata, permission
        overrides, or archived timestamp

        Args:
          id: Session ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/session/{id}",
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "permission": permission,
                    "time": time,
                    "title": title,
                },
                session_update_params.SessionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=Session,
        )

    async def children(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionChildrenResponse:
        """
        List the direct child sessions forked from this session

        Args:
          id: Session ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/session/{id}/children",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SessionChildrenResponse,
        )

    async def command(
        self,
        id: str,
        *,
        arguments: str,
        command: str,
        agent: str | NotGiven = NOT_GIVEN,
        message_id: str | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        parts: Iterable[FilePartInputParam] | NotGiven = NOT_GIVEN,
        variant: str | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionCommandResponse:
        """
        Run a slash command within a session

        Args:
          id: Session ID

          arguments: Raw command arguments

          command: Command name to execute

          model: Model in `providerID/modelID` string form

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/session/{id}/command",
            body=await async_maybe_transform(
                {
                    "arguments": arguments,
                    "command": command,
                    "agent": agent,
                    "message_id": message_id,
                    "model": model,
                    "parts": parts,
                    "variant": variant,
                },
                session_command_params.SessionCommandParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SessionCommandResponse,
        )

    async def diff(
        self,
        id: str,
        *,
        message_id: str | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionDiffResponse:
        """
        Get the file diffs produced by a session, optionally only up to a given
        message

        Args:
          id: Session ID

          message_id: Only include diffs up to this message ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/session/{id}/diff",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "message_id": message_id,
                        "directory": directory,
                        "workspace": workspace,
                    },
                    session_diff_params.SessionDiffParams,
                ),
            ),
            cast_to=SessionDiffResponse,
        )

    async def fork(
        self,
        id: str,
        *,
        message_id: str | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Fork a session, optionally only up to a given message

        Args:
          id: Session ID

          message_id: Fork up to (and including) this message ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/session/{id}/fork",
            body=await async_maybe_transform({"message_id": message_id}, session_fork_params.SessionForkParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=Session,
        )

    async def delete_message(
        self,
        id: str,
        *,
        message_id: str,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionDeleteMessageResponse:
        """
        Delete a message (and its parts) from a session

        Args:
          id: Session ID

          message_id: Message ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._delete(
            f"/session/{id}/message/{message_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SessionDeleteMessageResponse,
        )

    async def get_message(
        self,
        id: str,
        *,
        message_id: str,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionMessagesResponseItem:
        """
        Get a single message (with its parts) from a session

        Args:
          id: Session ID

          message_id: Message ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._get(
            f"/session/{id}/message/{message_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SessionMessagesResponseItem,
        )

    async def delete_part(
        self,
        id: str,
        *,
        message_id: str,
        part_id: str,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionDeletePartResponse:
        """
        Delete a part from a message

        Args:
          id: Session ID

          message_id: Message ID

          part_id: Part ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        if not part_id:
            raise ValueError(f"Expected a non-empty value for `part_id` but received {part_id!r}")
        return await self._delete(
            f"/session/{id}/message/{message_id}/part/{part_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SessionDeletePartResponse,
        )

    async def update_part(
        self,
        id: str,
        *,
        message_id: str,
        part_id: str,
        part: session_update_part_params.SessionUpdatePartParams,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Part:
        """
        Replace a message part with a new value.

        The request body is a *complete* replacement `Part` object (matching one
        of the `Part` union's variants), not a partial patch -- typically a
        caller GETs the part first (e.g. via `get_message`), edits the fields it
        wants to change, and PATCHes the whole object back.

        Args:
          id: Session ID

          message_id: Message ID

          part_id: Part ID

          part: The full replacement part, matching one of the `Part` union's variants

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        if not part_id:
            raise ValueError(f"Expected a non-empty value for `part_id` but received {part_id!r}")
        return cast(
            Part,
            await self._patch(
                f"/session/{id}/message/{message_id}/part/{part_id}",
                body=await async_maybe_transform(part, session_update_part_params.SessionUpdatePartParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "directory": directory,
                            "workspace": workspace,
                        },
                        addressing_params.AddressingParams,
                    ),
                ),
                cast_to=cast(Any, Part),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def respond_permission(
        self,
        id: str,
        *,
        permission_id: str,
        response: Literal["once", "always", "reject"],
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionRespondPermissionResponse:
        """
        Respond to a pending permission request for a session.

        Deprecated: the spec marks `permission.respond` as `deprecated: true`.
        Retained for backwards compatibility.

        Args:
          id: Session ID

          permission_id: Permission ID

          response: How to resolve the permission request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not permission_id:
            raise ValueError(f"Expected a non-empty value for `permission_id` but received {permission_id!r}")
        return await self._post(
            f"/session/{id}/permissions/{permission_id}",
            body=await async_maybe_transform(
                {"response": response}, session_respond_permission_params.SessionRespondPermissionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SessionRespondPermissionResponse,
        )

    async def prompt_async(
        self,
        id: str,
        *,
        parts: Iterable[session_prompt_async_params.Part],
        agent: str | NotGiven = NOT_GIVEN,
        format: session_prompt_async_params.Format | NotGiven = NOT_GIVEN,
        message_id: str | NotGiven = NOT_GIVEN,
        model: session_prompt_async_params.Model | NotGiven = NOT_GIVEN,
        no_reply: bool | NotGiven = NOT_GIVEN,
        system: str | NotGiven = NOT_GIVEN,
        tools: Dict[str, bool] | NotGiven = NOT_GIVEN,
        variant: str | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Send a new message to a session without waiting for the assistant's
        reply (accepted asynchronously; the server responds `204 No Content`).

        Args:
          id: Session ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/session/{id}/prompt_async",
            body=await async_maybe_transform(
                {
                    "parts": parts,
                    "agent": agent,
                    "format": format,
                    "message_id": message_id,
                    "model": model,
                    "no_reply": no_reply,
                    "system": system,
                    "tools": tools,
                    "variant": variant,
                },
                session_prompt_async_params.SessionPromptAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def shell(
        self,
        id: str,
        *,
        agent: str,
        command: str,
        message_id: str | NotGiven = NOT_GIVEN,
        model: session_shell_params.Model | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionShellResponse:
        """
        Run a shell command within a session

        Args:
          id: Session ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/session/{id}/shell",
            body=await async_maybe_transform(
                {
                    "agent": agent,
                    "command": command,
                    "message_id": message_id,
                    "model": model,
                },
                session_shell_params.SessionShellParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SessionShellResponse,
        )

    async def todo(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionTodoResponse:
        """
        List the todo items tracked for a session

        Args:
          id: Session ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/session/{id}/todo",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SessionTodoResponse,
        )


class SessionResourceWithRawResponse:
    def __init__(self, session: SessionResource) -> None:
        self._session = session

        self.create = to_raw_response_wrapper(
            session.create,
        )
        self.list = to_raw_response_wrapper(
            session.list,
        )
        self.delete = to_raw_response_wrapper(
            session.delete,
        )
        self.abort = to_raw_response_wrapper(
            session.abort,
        )
        self.prompt = to_raw_response_wrapper(
            session.prompt,
        )
        self.init = to_raw_response_wrapper(
            session.init,
        )
        self.messages = to_raw_response_wrapper(
            session.messages,
        )
        self.revert = to_raw_response_wrapper(
            session.revert,
        )
        self.share = to_raw_response_wrapper(
            session.share,
        )
        self.summarize = to_raw_response_wrapper(
            session.summarize,
        )
        self.unrevert = to_raw_response_wrapper(
            session.unrevert,
        )
        self.unshare = to_raw_response_wrapper(
            session.unshare,
        )
        self.status = to_raw_response_wrapper(
            session.status,
        )
        self.get = to_raw_response_wrapper(
            session.get,
        )
        self.update = to_raw_response_wrapper(
            session.update,
        )
        self.children = to_raw_response_wrapper(
            session.children,
        )
        self.command = to_raw_response_wrapper(
            session.command,
        )
        self.diff = to_raw_response_wrapper(
            session.diff,
        )
        self.fork = to_raw_response_wrapper(
            session.fork,
        )
        self.delete_message = to_raw_response_wrapper(
            session.delete_message,
        )
        self.get_message = to_raw_response_wrapper(
            session.get_message,
        )
        self.delete_part = to_raw_response_wrapper(
            session.delete_part,
        )
        self.update_part = to_raw_response_wrapper(
            session.update_part,
        )
        self.respond_permission = to_raw_response_wrapper(
            session.respond_permission,
        )
        self.prompt_async = to_raw_response_wrapper(
            session.prompt_async,
        )
        self.shell = to_raw_response_wrapper(
            session.shell,
        )
        self.todo = to_raw_response_wrapper(
            session.todo,
        )


class AsyncSessionResourceWithRawResponse:
    def __init__(self, session: AsyncSessionResource) -> None:
        self._session = session

        self.create = async_to_raw_response_wrapper(
            session.create,
        )
        self.list = async_to_raw_response_wrapper(
            session.list,
        )
        self.delete = async_to_raw_response_wrapper(
            session.delete,
        )
        self.abort = async_to_raw_response_wrapper(
            session.abort,
        )
        self.prompt = async_to_raw_response_wrapper(
            session.prompt,
        )
        self.init = async_to_raw_response_wrapper(
            session.init,
        )
        self.messages = async_to_raw_response_wrapper(
            session.messages,
        )
        self.revert = async_to_raw_response_wrapper(
            session.revert,
        )
        self.share = async_to_raw_response_wrapper(
            session.share,
        )
        self.summarize = async_to_raw_response_wrapper(
            session.summarize,
        )
        self.unrevert = async_to_raw_response_wrapper(
            session.unrevert,
        )
        self.unshare = async_to_raw_response_wrapper(
            session.unshare,
        )
        self.status = async_to_raw_response_wrapper(
            session.status,
        )
        self.get = async_to_raw_response_wrapper(
            session.get,
        )
        self.update = async_to_raw_response_wrapper(
            session.update,
        )
        self.children = async_to_raw_response_wrapper(
            session.children,
        )
        self.command = async_to_raw_response_wrapper(
            session.command,
        )
        self.diff = async_to_raw_response_wrapper(
            session.diff,
        )
        self.fork = async_to_raw_response_wrapper(
            session.fork,
        )
        self.delete_message = async_to_raw_response_wrapper(
            session.delete_message,
        )
        self.get_message = async_to_raw_response_wrapper(
            session.get_message,
        )
        self.delete_part = async_to_raw_response_wrapper(
            session.delete_part,
        )
        self.update_part = async_to_raw_response_wrapper(
            session.update_part,
        )
        self.respond_permission = async_to_raw_response_wrapper(
            session.respond_permission,
        )
        self.prompt_async = async_to_raw_response_wrapper(
            session.prompt_async,
        )
        self.shell = async_to_raw_response_wrapper(
            session.shell,
        )
        self.todo = async_to_raw_response_wrapper(
            session.todo,
        )


class SessionResourceWithStreamingResponse:
    def __init__(self, session: SessionResource) -> None:
        self._session = session

        self.create = to_streamed_response_wrapper(
            session.create,
        )
        self.list = to_streamed_response_wrapper(
            session.list,
        )
        self.delete = to_streamed_response_wrapper(
            session.delete,
        )
        self.abort = to_streamed_response_wrapper(
            session.abort,
        )
        self.prompt = to_streamed_response_wrapper(
            session.prompt,
        )
        self.init = to_streamed_response_wrapper(
            session.init,
        )
        self.messages = to_streamed_response_wrapper(
            session.messages,
        )
        self.revert = to_streamed_response_wrapper(
            session.revert,
        )
        self.share = to_streamed_response_wrapper(
            session.share,
        )
        self.summarize = to_streamed_response_wrapper(
            session.summarize,
        )
        self.unrevert = to_streamed_response_wrapper(
            session.unrevert,
        )
        self.unshare = to_streamed_response_wrapper(
            session.unshare,
        )
        self.status = to_streamed_response_wrapper(
            session.status,
        )
        self.get = to_streamed_response_wrapper(
            session.get,
        )
        self.update = to_streamed_response_wrapper(
            session.update,
        )
        self.children = to_streamed_response_wrapper(
            session.children,
        )
        self.command = to_streamed_response_wrapper(
            session.command,
        )
        self.diff = to_streamed_response_wrapper(
            session.diff,
        )
        self.fork = to_streamed_response_wrapper(
            session.fork,
        )
        self.delete_message = to_streamed_response_wrapper(
            session.delete_message,
        )
        self.get_message = to_streamed_response_wrapper(
            session.get_message,
        )
        self.delete_part = to_streamed_response_wrapper(
            session.delete_part,
        )
        self.update_part = to_streamed_response_wrapper(
            session.update_part,
        )
        self.respond_permission = to_streamed_response_wrapper(
            session.respond_permission,
        )
        self.prompt_async = to_streamed_response_wrapper(
            session.prompt_async,
        )
        self.shell = to_streamed_response_wrapper(
            session.shell,
        )
        self.todo = to_streamed_response_wrapper(
            session.todo,
        )


class AsyncSessionResourceWithStreamingResponse:
    def __init__(self, session: AsyncSessionResource) -> None:
        self._session = session

        self.create = async_to_streamed_response_wrapper(
            session.create,
        )
        self.list = async_to_streamed_response_wrapper(
            session.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            session.delete,
        )
        self.abort = async_to_streamed_response_wrapper(
            session.abort,
        )
        self.prompt = async_to_streamed_response_wrapper(
            session.prompt,
        )
        self.init = async_to_streamed_response_wrapper(
            session.init,
        )
        self.messages = async_to_streamed_response_wrapper(
            session.messages,
        )
        self.revert = async_to_streamed_response_wrapper(
            session.revert,
        )
        self.share = async_to_streamed_response_wrapper(
            session.share,
        )
        self.summarize = async_to_streamed_response_wrapper(
            session.summarize,
        )
        self.unrevert = async_to_streamed_response_wrapper(
            session.unrevert,
        )
        self.unshare = async_to_streamed_response_wrapper(
            session.unshare,
        )
        self.status = async_to_streamed_response_wrapper(
            session.status,
        )
        self.get = async_to_streamed_response_wrapper(
            session.get,
        )
        self.update = async_to_streamed_response_wrapper(
            session.update,
        )
        self.children = async_to_streamed_response_wrapper(
            session.children,
        )
        self.command = async_to_streamed_response_wrapper(
            session.command,
        )
        self.diff = async_to_streamed_response_wrapper(
            session.diff,
        )
        self.fork = async_to_streamed_response_wrapper(
            session.fork,
        )
        self.delete_message = async_to_streamed_response_wrapper(
            session.delete_message,
        )
        self.get_message = async_to_streamed_response_wrapper(
            session.get_message,
        )
        self.delete_part = async_to_streamed_response_wrapper(
            session.delete_part,
        )
        self.update_part = async_to_streamed_response_wrapper(
            session.update_part,
        )
        self.respond_permission = async_to_streamed_response_wrapper(
            session.respond_permission,
        )
        self.prompt_async = async_to_streamed_response_wrapper(
            session.prompt_async,
        )
        self.shell = async_to_streamed_response_wrapper(
            session.shell,
        )
        self.todo = async_to_streamed_response_wrapper(
            session.todo,
        )
