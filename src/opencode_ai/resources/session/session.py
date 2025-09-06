# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable

import httpx

from ...types import (
    session_get_params,
    session_init_params,
    session_list_params,
    session_abort_params,
    session_share_params,
    session_shell_params,
    session_create_params,
    session_delete_params,
    session_prompt_params,
    session_revert_params,
    session_update_params,
    session_command_params,
    session_message_params,
    session_unshare_params,
    session_children_params,
    session_messages_params,
    session_unrevert_params,
    session_summarize_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .permissions import (
    PermissionsResource,
    AsyncPermissionsResource,
    PermissionsResourceWithRawResponse,
    AsyncPermissionsResourceWithRawResponse,
    PermissionsResourceWithStreamingResponse,
    AsyncPermissionsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.session.session import Session
from ...types.assistant_message import AssistantMessage
from ...types.session_init_response import SessionInitResponse
from ...types.session_list_response import SessionListResponse
from ...types.session_abort_response import SessionAbortResponse
from ...types.session_delete_response import SessionDeleteResponse
from ...types.session_prompt_response import SessionPromptResponse
from ...types.session_command_response import SessionCommandResponse
from ...types.session_message_response import SessionMessageResponse
from ...types.session_children_response import SessionChildrenResponse
from ...types.session_messages_response import SessionMessagesResponse
from ...types.session_summarize_response import SessionSummarizeResponse

__all__ = ["SessionResource", "AsyncSessionResource"]


class SessionResource(SyncAPIResource):
    @cached_property
    def permissions(self) -> PermissionsResource:
        return PermissionsResource(self._client)

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
        parent_id: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Create a new session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/session",
            body=maybe_transform(
                {
                    "parent_id": parent_id,
                    "title": title,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, session_create_params.SessionCreateParams),
            ),
            cast_to=Session,
        )

    def update(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Update session properties

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/session/{id}",
            body=maybe_transform({"title": title}, session_update_params.SessionUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, session_update_params.SessionUpdateParams),
            ),
            cast_to=Session,
        )

    def list(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
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
                query=maybe_transform({"directory": directory}, session_list_params.SessionListParams),
            ),
            cast_to=SessionListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
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
                query=maybe_transform({"directory": directory}, session_delete_params.SessionDeleteParams),
            ),
            cast_to=SessionDeleteResponse,
        )

    def abort(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
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
                query=maybe_transform({"directory": directory}, session_abort_params.SessionAbortParams),
            ),
            cast_to=SessionAbortResponse,
        )

    def children(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionChildrenResponse:
        """
        Get a session's children

        Args:
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
                query=maybe_transform({"directory": directory}, session_children_params.SessionChildrenParams),
            ),
            cast_to=SessionChildrenResponse,
        )

    def command(
        self,
        id: str,
        *,
        arguments: str,
        command: str,
        directory: str | NotGiven = NOT_GIVEN,
        agent: str | NotGiven = NOT_GIVEN,
        message_id: str | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionCommandResponse:
        """
        Send a new command to a session

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
            f"/session/{id}/command",
            body=maybe_transform(
                {
                    "arguments": arguments,
                    "command": command,
                    "agent": agent,
                    "message_id": message_id,
                    "model": model,
                },
                session_command_params.SessionCommandParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, session_command_params.SessionCommandParams),
            ),
            cast_to=SessionCommandResponse,
        )

    def get(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Get session

        Args:
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
                query=maybe_transform({"directory": directory}, session_get_params.SessionGetParams),
            ),
            cast_to=Session,
        )

    def init(
        self,
        id: str,
        *,
        message_id: str,
        model_id: str,
        provider_id: str,
        directory: str | NotGiven = NOT_GIVEN,
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
                query=maybe_transform({"directory": directory}, session_init_params.SessionInitParams),
            ),
            cast_to=SessionInitResponse,
        )

    def message(
        self,
        message_id: str,
        *,
        id: str,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionMessageResponse:
        """
        Get a message from a session

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
                query=maybe_transform({"directory": directory}, session_message_params.SessionMessageParams),
            ),
            cast_to=SessionMessageResponse,
        )

    def messages(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
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
                query=maybe_transform({"directory": directory}, session_messages_params.SessionMessagesParams),
            ),
            cast_to=SessionMessagesResponse,
        )

    def prompt(
        self,
        id: str,
        *,
        parts: Iterable[session_prompt_params.Part],
        directory: str | NotGiven = NOT_GIVEN,
        agent: str | NotGiven = NOT_GIVEN,
        message_id: str | NotGiven = NOT_GIVEN,
        model: session_prompt_params.Model | NotGiven = NOT_GIVEN,
        system: str | NotGiven = NOT_GIVEN,
        tools: Dict[str, bool] | NotGiven = NOT_GIVEN,
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
                    "agent": agent,
                    "message_id": message_id,
                    "model": model,
                    "system": system,
                    "tools": tools,
                },
                session_prompt_params.SessionPromptParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, session_prompt_params.SessionPromptParams),
            ),
            cast_to=SessionPromptResponse,
        )

    def revert(
        self,
        id: str,
        *,
        message_id: str,
        directory: str | NotGiven = NOT_GIVEN,
        part_id: str | NotGiven = NOT_GIVEN,
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
                query=maybe_transform({"directory": directory}, session_revert_params.SessionRevertParams),
            ),
            cast_to=Session,
        )

    def share(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
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
                query=maybe_transform({"directory": directory}, session_share_params.SessionShareParams),
            ),
            cast_to=Session,
        )

    def shell(
        self,
        id: str,
        *,
        agent: str,
        command: str,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantMessage:
        """
        Run a shell command

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
                },
                session_shell_params.SessionShellParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, session_shell_params.SessionShellParams),
            ),
            cast_to=AssistantMessage,
        )

    def summarize(
        self,
        id: str,
        *,
        model_id: str,
        provider_id: str,
        directory: str | NotGiven = NOT_GIVEN,
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
                },
                session_summarize_params.SessionSummarizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, session_summarize_params.SessionSummarizeParams),
            ),
            cast_to=SessionSummarizeResponse,
        )

    def unrevert(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
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
                query=maybe_transform({"directory": directory}, session_unrevert_params.SessionUnrevertParams),
            ),
            cast_to=Session,
        )

    def unshare(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
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
                query=maybe_transform({"directory": directory}, session_unshare_params.SessionUnshareParams),
            ),
            cast_to=Session,
        )


class AsyncSessionResource(AsyncAPIResource):
    @cached_property
    def permissions(self) -> AsyncPermissionsResource:
        return AsyncPermissionsResource(self._client)

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
        parent_id: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Create a new session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/session",
            body=await async_maybe_transform(
                {
                    "parent_id": parent_id,
                    "title": title,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, session_create_params.SessionCreateParams),
            ),
            cast_to=Session,
        )

    async def update(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Update session properties

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/session/{id}",
            body=await async_maybe_transform({"title": title}, session_update_params.SessionUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, session_update_params.SessionUpdateParams),
            ),
            cast_to=Session,
        )

    async def list(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
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
                query=await async_maybe_transform({"directory": directory}, session_list_params.SessionListParams),
            ),
            cast_to=SessionListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
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
                query=await async_maybe_transform({"directory": directory}, session_delete_params.SessionDeleteParams),
            ),
            cast_to=SessionDeleteResponse,
        )

    async def abort(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
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
                query=await async_maybe_transform({"directory": directory}, session_abort_params.SessionAbortParams),
            ),
            cast_to=SessionAbortResponse,
        )

    async def children(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionChildrenResponse:
        """
        Get a session's children

        Args:
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
                    {"directory": directory}, session_children_params.SessionChildrenParams
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
        directory: str | NotGiven = NOT_GIVEN,
        agent: str | NotGiven = NOT_GIVEN,
        message_id: str | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionCommandResponse:
        """
        Send a new command to a session

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
            f"/session/{id}/command",
            body=await async_maybe_transform(
                {
                    "arguments": arguments,
                    "command": command,
                    "agent": agent,
                    "message_id": message_id,
                    "model": model,
                },
                session_command_params.SessionCommandParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, session_command_params.SessionCommandParams
                ),
            ),
            cast_to=SessionCommandResponse,
        )

    async def get(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Session:
        """
        Get session

        Args:
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
                query=await async_maybe_transform({"directory": directory}, session_get_params.SessionGetParams),
            ),
            cast_to=Session,
        )

    async def init(
        self,
        id: str,
        *,
        message_id: str,
        model_id: str,
        provider_id: str,
        directory: str | NotGiven = NOT_GIVEN,
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
                query=await async_maybe_transform({"directory": directory}, session_init_params.SessionInitParams),
            ),
            cast_to=SessionInitResponse,
        )

    async def message(
        self,
        message_id: str,
        *,
        id: str,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionMessageResponse:
        """
        Get a message from a session

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
                    {"directory": directory}, session_message_params.SessionMessageParams
                ),
            ),
            cast_to=SessionMessageResponse,
        )

    async def messages(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
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
                    {"directory": directory}, session_messages_params.SessionMessagesParams
                ),
            ),
            cast_to=SessionMessagesResponse,
        )

    async def prompt(
        self,
        id: str,
        *,
        parts: Iterable[session_prompt_params.Part],
        directory: str | NotGiven = NOT_GIVEN,
        agent: str | NotGiven = NOT_GIVEN,
        message_id: str | NotGiven = NOT_GIVEN,
        model: session_prompt_params.Model | NotGiven = NOT_GIVEN,
        system: str | NotGiven = NOT_GIVEN,
        tools: Dict[str, bool] | NotGiven = NOT_GIVEN,
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
                    "agent": agent,
                    "message_id": message_id,
                    "model": model,
                    "system": system,
                    "tools": tools,
                },
                session_prompt_params.SessionPromptParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, session_prompt_params.SessionPromptParams),
            ),
            cast_to=SessionPromptResponse,
        )

    async def revert(
        self,
        id: str,
        *,
        message_id: str,
        directory: str | NotGiven = NOT_GIVEN,
        part_id: str | NotGiven = NOT_GIVEN,
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
                query=await async_maybe_transform({"directory": directory}, session_revert_params.SessionRevertParams),
            ),
            cast_to=Session,
        )

    async def share(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
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
                query=await async_maybe_transform({"directory": directory}, session_share_params.SessionShareParams),
            ),
            cast_to=Session,
        )

    async def shell(
        self,
        id: str,
        *,
        agent: str,
        command: str,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantMessage:
        """
        Run a shell command

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
                },
                session_shell_params.SessionShellParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, session_shell_params.SessionShellParams),
            ),
            cast_to=AssistantMessage,
        )

    async def summarize(
        self,
        id: str,
        *,
        model_id: str,
        provider_id: str,
        directory: str | NotGiven = NOT_GIVEN,
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
                },
                session_summarize_params.SessionSummarizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, session_summarize_params.SessionSummarizeParams
                ),
            ),
            cast_to=SessionSummarizeResponse,
        )

    async def unrevert(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
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
                    {"directory": directory}, session_unrevert_params.SessionUnrevertParams
                ),
            ),
            cast_to=Session,
        )

    async def unshare(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
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
                    {"directory": directory}, session_unshare_params.SessionUnshareParams
                ),
            ),
            cast_to=Session,
        )


class SessionResourceWithRawResponse:
    def __init__(self, session: SessionResource) -> None:
        self._session = session

        self.create = to_raw_response_wrapper(
            session.create,
        )
        self.update = to_raw_response_wrapper(
            session.update,
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
        self.children = to_raw_response_wrapper(
            session.children,
        )
        self.command = to_raw_response_wrapper(
            session.command,
        )
        self.get = to_raw_response_wrapper(
            session.get,
        )
        self.init = to_raw_response_wrapper(
            session.init,
        )
        self.message = to_raw_response_wrapper(
            session.message,
        )
        self.messages = to_raw_response_wrapper(
            session.messages,
        )
        self.prompt = to_raw_response_wrapper(
            session.prompt,
        )
        self.revert = to_raw_response_wrapper(
            session.revert,
        )
        self.share = to_raw_response_wrapper(
            session.share,
        )
        self.shell = to_raw_response_wrapper(
            session.shell,
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

    @cached_property
    def permissions(self) -> PermissionsResourceWithRawResponse:
        return PermissionsResourceWithRawResponse(self._session.permissions)


class AsyncSessionResourceWithRawResponse:
    def __init__(self, session: AsyncSessionResource) -> None:
        self._session = session

        self.create = async_to_raw_response_wrapper(
            session.create,
        )
        self.update = async_to_raw_response_wrapper(
            session.update,
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
        self.children = async_to_raw_response_wrapper(
            session.children,
        )
        self.command = async_to_raw_response_wrapper(
            session.command,
        )
        self.get = async_to_raw_response_wrapper(
            session.get,
        )
        self.init = async_to_raw_response_wrapper(
            session.init,
        )
        self.message = async_to_raw_response_wrapper(
            session.message,
        )
        self.messages = async_to_raw_response_wrapper(
            session.messages,
        )
        self.prompt = async_to_raw_response_wrapper(
            session.prompt,
        )
        self.revert = async_to_raw_response_wrapper(
            session.revert,
        )
        self.share = async_to_raw_response_wrapper(
            session.share,
        )
        self.shell = async_to_raw_response_wrapper(
            session.shell,
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

    @cached_property
    def permissions(self) -> AsyncPermissionsResourceWithRawResponse:
        return AsyncPermissionsResourceWithRawResponse(self._session.permissions)


class SessionResourceWithStreamingResponse:
    def __init__(self, session: SessionResource) -> None:
        self._session = session

        self.create = to_streamed_response_wrapper(
            session.create,
        )
        self.update = to_streamed_response_wrapper(
            session.update,
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
        self.children = to_streamed_response_wrapper(
            session.children,
        )
        self.command = to_streamed_response_wrapper(
            session.command,
        )
        self.get = to_streamed_response_wrapper(
            session.get,
        )
        self.init = to_streamed_response_wrapper(
            session.init,
        )
        self.message = to_streamed_response_wrapper(
            session.message,
        )
        self.messages = to_streamed_response_wrapper(
            session.messages,
        )
        self.prompt = to_streamed_response_wrapper(
            session.prompt,
        )
        self.revert = to_streamed_response_wrapper(
            session.revert,
        )
        self.share = to_streamed_response_wrapper(
            session.share,
        )
        self.shell = to_streamed_response_wrapper(
            session.shell,
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

    @cached_property
    def permissions(self) -> PermissionsResourceWithStreamingResponse:
        return PermissionsResourceWithStreamingResponse(self._session.permissions)


class AsyncSessionResourceWithStreamingResponse:
    def __init__(self, session: AsyncSessionResource) -> None:
        self._session = session

        self.create = async_to_streamed_response_wrapper(
            session.create,
        )
        self.update = async_to_streamed_response_wrapper(
            session.update,
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
        self.children = async_to_streamed_response_wrapper(
            session.children,
        )
        self.command = async_to_streamed_response_wrapper(
            session.command,
        )
        self.get = async_to_streamed_response_wrapper(
            session.get,
        )
        self.init = async_to_streamed_response_wrapper(
            session.init,
        )
        self.message = async_to_streamed_response_wrapper(
            session.message,
        )
        self.messages = async_to_streamed_response_wrapper(
            session.messages,
        )
        self.prompt = async_to_streamed_response_wrapper(
            session.prompt,
        )
        self.revert = async_to_streamed_response_wrapper(
            session.revert,
        )
        self.share = async_to_streamed_response_wrapper(
            session.share,
        )
        self.shell = async_to_streamed_response_wrapper(
            session.shell,
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

    @cached_property
    def permissions(self) -> AsyncPermissionsResourceWithStreamingResponse:
        return AsyncPermissionsResourceWithStreamingResponse(self._session.permissions)
