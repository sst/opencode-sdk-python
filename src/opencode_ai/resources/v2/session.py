# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing import Any, Dict, List, Iterable, cast
from typing_extensions import Literal

import httpx

from ...types import (
    v2_session_list_params,
    v2_session_create_params,
    v2_session_events_params,
    v2_session_prompt_params,
    v2_session_history_params,
    v2_session_messages_params,
    v2_session_revert_stage_params,
    v2_session_switch_agent_params,
    v2_session_switch_model_params,
    v2_session_question_reply_params,
    v2_session_permission_reply_params,
    v2_session_permission_create_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._streaming import Stream, AsyncStream
from ..._base_client import make_request_options
from ...types.v2_session_get_response import V2SessionGetResponse
from ...types.v2_session_list_response import V2SessionListResponse
from ...types.v2_session_active_response import V2SessionActiveResponse
from ...types.v2_session_create_response import V2SessionCreateResponse
from ...types.v2_session_events_response import V2SessionEventsResponse
from ...types.v2_session_prompt_response import V2SessionPromptResponse
from ...types.v2_session_context_response import V2SessionContextResponse
from ...types.v2_session_history_response import V2SessionHistoryResponse
from ...types.v2_session_message_response import V2SessionMessageResponse
from ...types.v2_session_messages_response import V2SessionMessagesResponse
from ...types.v2_session_revert_stage_response import V2SessionRevertStageResponse
from ...types.v2_session_question_list_response import V2SessionQuestionListResponse
from ...types.v2_session_permission_get_response import V2SessionPermissionGetResponse
from ...types.v2_session_permission_list_response import V2SessionPermissionListResponse
from ...types.v2_session_permission_create_response import V2SessionPermissionCreateResponse

__all__ = ["V2SessionResource", "AsyncV2SessionResource"]


class V2SessionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V2SessionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return V2SessionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2SessionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return V2SessionResourceWithStreamingResponse(self)

    def active(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2SessionActiveResponse:
        """List active sessions"""
        return self._get(
            "/api/session/active",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V2SessionActiveResponse,
        )

    def compact(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Compact session"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/api/session/{session_id}/compact",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=NoneType,
        )

    def context(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2SessionContextResponse:
        """Get session context"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/api/session/{session_id}/context",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V2SessionContextResponse,
        )

    def create(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        agent: str | NotGiven = NOT_GIVEN,
        model: object | NotGiven = NOT_GIVEN,
        location: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2SessionCreateResponse:
        """Create session"""
        return self._post(
            "/api/session",
            body=maybe_transform(
                {
                    "id": id,
                    "agent": agent,
                    "model": model,
                    "location": location,
                },
                v2_session_create_params.V2SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V2SessionCreateResponse,
        )

    def events(
        self,
        session_id: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Stream[V2SessionEventsResponse]:
        """Subscribe to session events"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/api/session/{session_id}/event",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                    },
                    v2_session_events_params.V2SessionEventsParams,
                ),
            ),
            cast_to=cast(Any, V2SessionEventsResponse),
            stream=True,
            stream_cls=Stream[V2SessionEventsResponse],
        )

    def get(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2SessionGetResponse:
        """Get session"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/api/session/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V2SessionGetResponse,
        )

    def history(
        self,
        session_id: str,
        *,
        limit: str | NotGiven = NOT_GIVEN,
        after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2SessionHistoryResponse:
        """Get session history"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/api/session/{session_id}/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "after": after,
                    },
                    v2_session_history_params.V2SessionHistoryParams,
                ),
            ),
            cast_to=V2SessionHistoryResponse,
        )

    def interrupt(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Interrupt session execution"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/api/session/{session_id}/interrupt",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        workspace: str | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        project: str | NotGiven = NOT_GIVEN,
        subpath: str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2SessionListResponse:
        """List sessions"""
        return self._get(
            "/api/session",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "workspace": workspace,
                        "limit": limit,
                        "order": order,
                        "search": search,
                        "directory": directory,
                        "project": project,
                        "subpath": subpath,
                        "cursor": cursor,
                    },
                    v2_session_list_params.V2SessionListParams,
                ),
            ),
            cast_to=V2SessionListResponse,
        )

    def message(
        self,
        session_id: str,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2SessionMessageResponse:
        """Get session message"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get(
            f"/api/session/{session_id}/message/{message_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V2SessionMessageResponse,
        )

    def messages(
        self,
        session_id: str,
        *,
        limit: float | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2SessionMessagesResponse:
        """Get session messages"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/api/session/{session_id}/message",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "order": order,
                        "cursor": cursor,
                    },
                    v2_session_messages_params.V2SessionMessagesParams,
                ),
            ),
            cast_to=V2SessionMessagesResponse,
        )

    def permission_create(
        self,
        session_id: str,
        *,
        action: str,
        resources: List[str],
        id: str | NotGiven = NOT_GIVEN,
        save: List[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        source: object | NotGiven = NOT_GIVEN,
        agent: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2SessionPermissionCreateResponse:
        """Create permission request"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/api/session/{session_id}/permission",
            body=maybe_transform(
                {
                    "action": action,
                    "resources": resources,
                    "id": id,
                    "save": save,
                    "metadata": metadata,
                    "source": source,
                    "agent": agent,
                },
                v2_session_permission_create_params.V2SessionPermissionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V2SessionPermissionCreateResponse,
        )

    def permission_get(
        self,
        session_id: str,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2SessionPermissionGetResponse:
        """Get permission request"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return self._get(
            f"/api/session/{session_id}/permission/{request_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V2SessionPermissionGetResponse,
        )

    def permission_list(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2SessionPermissionListResponse:
        """List session permission requests"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/api/session/{session_id}/permission",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V2SessionPermissionListResponse,
        )

    def permission_reply(
        self,
        session_id: str,
        request_id: str,
        *,
        reply: Literal["once", "always", "reject"],
        message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Reply to pending permission request"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return self._post(
            f"/api/session/{session_id}/permission/{request_id}/reply",
            body=maybe_transform(
                {
                    "reply": reply,
                    "message": message,
                },
                v2_session_permission_reply_params.V2SessionPermissionReplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=NoneType,
        )

    def prompt(
        self,
        session_id: str,
        *,
        prompt: object,
        id: str | NotGiven = NOT_GIVEN,
        delivery: Literal["steer", "queue"] | NotGiven = NOT_GIVEN,
        resume: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2SessionPromptResponse:
        """Send message"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/api/session/{session_id}/prompt",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "id": id,
                    "delivery": delivery,
                    "resume": resume,
                },
                v2_session_prompt_params.V2SessionPromptParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V2SessionPromptResponse,
        )

    def question_list(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2SessionQuestionListResponse:
        """List session question requests"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/api/session/{session_id}/question",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V2SessionQuestionListResponse,
        )

    def question_reject(
        self,
        session_id: str,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Reject pending question request"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return self._post(
            f"/api/session/{session_id}/question/{request_id}/reject",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=NoneType,
        )

    def question_reply(
        self,
        session_id: str,
        request_id: str,
        *,
        answers: Iterable[object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Reply to pending question request"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return self._post(
            f"/api/session/{session_id}/question/{request_id}/reply",
            body=maybe_transform(
                {
                    "answers": answers,
                },
                v2_session_question_reply_params.V2SessionQuestionReplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=NoneType,
        )

    def revert_clear(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Clear staged revert"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/api/session/{session_id}/revert/clear",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=NoneType,
        )

    def revert_commit(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Commit staged revert"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/api/session/{session_id}/revert/commit",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=NoneType,
        )

    def revert_stage(
        self,
        session_id: str,
        *,
        message_id: str,
        files: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2SessionRevertStageResponse:
        """Stage session revert"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/api/session/{session_id}/revert/stage",
            body=maybe_transform(
                {
                    "message_id": message_id,
                    "files": files,
                },
                v2_session_revert_stage_params.V2SessionRevertStageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V2SessionRevertStageResponse,
        )

    def switch_agent(
        self,
        session_id: str,
        *,
        agent: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Switch session agent"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/api/session/{session_id}/agent",
            body=maybe_transform(
                {
                    "agent": agent,
                },
                v2_session_switch_agent_params.V2SessionSwitchAgentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=NoneType,
        )

    def switch_model(
        self,
        session_id: str,
        *,
        model: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Switch session model"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/api/session/{session_id}/model",
            body=maybe_transform(
                {
                    "model": model,
                },
                v2_session_switch_model_params.V2SessionSwitchModelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=NoneType,
        )

    def wait(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Wait for session"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/api/session/{session_id}/wait",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=NoneType,
        )


class AsyncV2SessionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV2SessionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2SessionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2SessionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncV2SessionResourceWithStreamingResponse(self)

    async def active(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2SessionActiveResponse:
        """List active sessions"""
        return await self._get(
            "/api/session/active",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V2SessionActiveResponse,
        )

    async def compact(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Compact session"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/api/session/{session_id}/compact",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=NoneType,
        )

    async def context(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2SessionContextResponse:
        """Get session context"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/api/session/{session_id}/context",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V2SessionContextResponse,
        )

    async def create(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        agent: str | NotGiven = NOT_GIVEN,
        model: object | NotGiven = NOT_GIVEN,
        location: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2SessionCreateResponse:
        """Create session"""
        return await self._post(
            "/api/session",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "agent": agent,
                    "model": model,
                    "location": location,
                },
                v2_session_create_params.V2SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V2SessionCreateResponse,
        )

    async def events(
        self,
        session_id: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncStream[V2SessionEventsResponse]:
        """Subscribe to session events"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/api/session/{session_id}/event",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                    },
                    v2_session_events_params.V2SessionEventsParams,
                ),
            ),
            cast_to=cast(Any, V2SessionEventsResponse),
            stream=True,
            stream_cls=AsyncStream[V2SessionEventsResponse],
        )

    async def get(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2SessionGetResponse:
        """Get session"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/api/session/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V2SessionGetResponse,
        )

    async def history(
        self,
        session_id: str,
        *,
        limit: str | NotGiven = NOT_GIVEN,
        after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2SessionHistoryResponse:
        """Get session history"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/api/session/{session_id}/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "after": after,
                    },
                    v2_session_history_params.V2SessionHistoryParams,
                ),
            ),
            cast_to=V2SessionHistoryResponse,
        )

    async def interrupt(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Interrupt session execution"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/api/session/{session_id}/interrupt",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        workspace: str | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        project: str | NotGiven = NOT_GIVEN,
        subpath: str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2SessionListResponse:
        """List sessions"""
        return await self._get(
            "/api/session",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "workspace": workspace,
                        "limit": limit,
                        "order": order,
                        "search": search,
                        "directory": directory,
                        "project": project,
                        "subpath": subpath,
                        "cursor": cursor,
                    },
                    v2_session_list_params.V2SessionListParams,
                ),
            ),
            cast_to=V2SessionListResponse,
        )

    async def message(
        self,
        session_id: str,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2SessionMessageResponse:
        """Get session message"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._get(
            f"/api/session/{session_id}/message/{message_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V2SessionMessageResponse,
        )

    async def messages(
        self,
        session_id: str,
        *,
        limit: float | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2SessionMessagesResponse:
        """Get session messages"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/api/session/{session_id}/message",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "order": order,
                        "cursor": cursor,
                    },
                    v2_session_messages_params.V2SessionMessagesParams,
                ),
            ),
            cast_to=V2SessionMessagesResponse,
        )

    async def permission_create(
        self,
        session_id: str,
        *,
        action: str,
        resources: List[str],
        id: str | NotGiven = NOT_GIVEN,
        save: List[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        source: object | NotGiven = NOT_GIVEN,
        agent: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2SessionPermissionCreateResponse:
        """Create permission request"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/api/session/{session_id}/permission",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "resources": resources,
                    "id": id,
                    "save": save,
                    "metadata": metadata,
                    "source": source,
                    "agent": agent,
                },
                v2_session_permission_create_params.V2SessionPermissionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V2SessionPermissionCreateResponse,
        )

    async def permission_get(
        self,
        session_id: str,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2SessionPermissionGetResponse:
        """Get permission request"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return await self._get(
            f"/api/session/{session_id}/permission/{request_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V2SessionPermissionGetResponse,
        )

    async def permission_list(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2SessionPermissionListResponse:
        """List session permission requests"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/api/session/{session_id}/permission",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V2SessionPermissionListResponse,
        )

    async def permission_reply(
        self,
        session_id: str,
        request_id: str,
        *,
        reply: Literal["once", "always", "reject"],
        message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Reply to pending permission request"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return await self._post(
            f"/api/session/{session_id}/permission/{request_id}/reply",
            body=await async_maybe_transform(
                {
                    "reply": reply,
                    "message": message,
                },
                v2_session_permission_reply_params.V2SessionPermissionReplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=NoneType,
        )

    async def prompt(
        self,
        session_id: str,
        *,
        prompt: object,
        id: str | NotGiven = NOT_GIVEN,
        delivery: Literal["steer", "queue"] | NotGiven = NOT_GIVEN,
        resume: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2SessionPromptResponse:
        """Send message"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/api/session/{session_id}/prompt",
            body=await async_maybe_transform(
                {
                    "prompt": prompt,
                    "id": id,
                    "delivery": delivery,
                    "resume": resume,
                },
                v2_session_prompt_params.V2SessionPromptParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V2SessionPromptResponse,
        )

    async def question_list(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2SessionQuestionListResponse:
        """List session question requests"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/api/session/{session_id}/question",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V2SessionQuestionListResponse,
        )

    async def question_reject(
        self,
        session_id: str,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Reject pending question request"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return await self._post(
            f"/api/session/{session_id}/question/{request_id}/reject",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=NoneType,
        )

    async def question_reply(
        self,
        session_id: str,
        request_id: str,
        *,
        answers: Iterable[object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Reply to pending question request"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return await self._post(
            f"/api/session/{session_id}/question/{request_id}/reply",
            body=await async_maybe_transform(
                {
                    "answers": answers,
                },
                v2_session_question_reply_params.V2SessionQuestionReplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=NoneType,
        )

    async def revert_clear(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Clear staged revert"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/api/session/{session_id}/revert/clear",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=NoneType,
        )

    async def revert_commit(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Commit staged revert"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/api/session/{session_id}/revert/commit",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=NoneType,
        )

    async def revert_stage(
        self,
        session_id: str,
        *,
        message_id: str,
        files: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2SessionRevertStageResponse:
        """Stage session revert"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/api/session/{session_id}/revert/stage",
            body=await async_maybe_transform(
                {
                    "message_id": message_id,
                    "files": files,
                },
                v2_session_revert_stage_params.V2SessionRevertStageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V2SessionRevertStageResponse,
        )

    async def switch_agent(
        self,
        session_id: str,
        *,
        agent: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Switch session agent"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/api/session/{session_id}/agent",
            body=await async_maybe_transform(
                {
                    "agent": agent,
                },
                v2_session_switch_agent_params.V2SessionSwitchAgentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=NoneType,
        )

    async def switch_model(
        self,
        session_id: str,
        *,
        model: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Switch session model"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/api/session/{session_id}/model",
            body=await async_maybe_transform(
                {
                    "model": model,
                },
                v2_session_switch_model_params.V2SessionSwitchModelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=NoneType,
        )

    async def wait(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Wait for session"""
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/api/session/{session_id}/wait",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=NoneType,
        )


class V2SessionResourceWithRawResponse:
    def __init__(self, session: V2SessionResource) -> None:
        self._session = session

        self.active = to_raw_response_wrapper(
            session.active,
        )
        self.compact = to_raw_response_wrapper(
            session.compact,
        )
        self.context = to_raw_response_wrapper(
            session.context,
        )
        self.create = to_raw_response_wrapper(
            session.create,
        )
        self.events = to_raw_response_wrapper(
            session.events,
        )
        self.get = to_raw_response_wrapper(
            session.get,
        )
        self.history = to_raw_response_wrapper(
            session.history,
        )
        self.interrupt = to_raw_response_wrapper(
            session.interrupt,
        )
        self.list = to_raw_response_wrapper(
            session.list,
        )
        self.message = to_raw_response_wrapper(
            session.message,
        )
        self.messages = to_raw_response_wrapper(
            session.messages,
        )
        self.permission_create = to_raw_response_wrapper(
            session.permission_create,
        )
        self.permission_get = to_raw_response_wrapper(
            session.permission_get,
        )
        self.permission_list = to_raw_response_wrapper(
            session.permission_list,
        )
        self.permission_reply = to_raw_response_wrapper(
            session.permission_reply,
        )
        self.prompt = to_raw_response_wrapper(
            session.prompt,
        )
        self.question_list = to_raw_response_wrapper(
            session.question_list,
        )
        self.question_reject = to_raw_response_wrapper(
            session.question_reject,
        )
        self.question_reply = to_raw_response_wrapper(
            session.question_reply,
        )
        self.revert_clear = to_raw_response_wrapper(
            session.revert_clear,
        )
        self.revert_commit = to_raw_response_wrapper(
            session.revert_commit,
        )
        self.revert_stage = to_raw_response_wrapper(
            session.revert_stage,
        )
        self.switch_agent = to_raw_response_wrapper(
            session.switch_agent,
        )
        self.switch_model = to_raw_response_wrapper(
            session.switch_model,
        )
        self.wait = to_raw_response_wrapper(
            session.wait,
        )


class AsyncV2SessionResourceWithRawResponse:
    def __init__(self, session: AsyncV2SessionResource) -> None:
        self._session = session

        self.active = async_to_raw_response_wrapper(
            session.active,
        )
        self.compact = async_to_raw_response_wrapper(
            session.compact,
        )
        self.context = async_to_raw_response_wrapper(
            session.context,
        )
        self.create = async_to_raw_response_wrapper(
            session.create,
        )
        self.events = async_to_raw_response_wrapper(
            session.events,
        )
        self.get = async_to_raw_response_wrapper(
            session.get,
        )
        self.history = async_to_raw_response_wrapper(
            session.history,
        )
        self.interrupt = async_to_raw_response_wrapper(
            session.interrupt,
        )
        self.list = async_to_raw_response_wrapper(
            session.list,
        )
        self.message = async_to_raw_response_wrapper(
            session.message,
        )
        self.messages = async_to_raw_response_wrapper(
            session.messages,
        )
        self.permission_create = async_to_raw_response_wrapper(
            session.permission_create,
        )
        self.permission_get = async_to_raw_response_wrapper(
            session.permission_get,
        )
        self.permission_list = async_to_raw_response_wrapper(
            session.permission_list,
        )
        self.permission_reply = async_to_raw_response_wrapper(
            session.permission_reply,
        )
        self.prompt = async_to_raw_response_wrapper(
            session.prompt,
        )
        self.question_list = async_to_raw_response_wrapper(
            session.question_list,
        )
        self.question_reject = async_to_raw_response_wrapper(
            session.question_reject,
        )
        self.question_reply = async_to_raw_response_wrapper(
            session.question_reply,
        )
        self.revert_clear = async_to_raw_response_wrapper(
            session.revert_clear,
        )
        self.revert_commit = async_to_raw_response_wrapper(
            session.revert_commit,
        )
        self.revert_stage = async_to_raw_response_wrapper(
            session.revert_stage,
        )
        self.switch_agent = async_to_raw_response_wrapper(
            session.switch_agent,
        )
        self.switch_model = async_to_raw_response_wrapper(
            session.switch_model,
        )
        self.wait = async_to_raw_response_wrapper(
            session.wait,
        )


class V2SessionResourceWithStreamingResponse:
    def __init__(self, session: V2SessionResource) -> None:
        self._session = session

        self.active = to_streamed_response_wrapper(
            session.active,
        )
        self.compact = to_streamed_response_wrapper(
            session.compact,
        )
        self.context = to_streamed_response_wrapper(
            session.context,
        )
        self.create = to_streamed_response_wrapper(
            session.create,
        )
        self.events = to_streamed_response_wrapper(
            session.events,
        )
        self.get = to_streamed_response_wrapper(
            session.get,
        )
        self.history = to_streamed_response_wrapper(
            session.history,
        )
        self.interrupt = to_streamed_response_wrapper(
            session.interrupt,
        )
        self.list = to_streamed_response_wrapper(
            session.list,
        )
        self.message = to_streamed_response_wrapper(
            session.message,
        )
        self.messages = to_streamed_response_wrapper(
            session.messages,
        )
        self.permission_create = to_streamed_response_wrapper(
            session.permission_create,
        )
        self.permission_get = to_streamed_response_wrapper(
            session.permission_get,
        )
        self.permission_list = to_streamed_response_wrapper(
            session.permission_list,
        )
        self.permission_reply = to_streamed_response_wrapper(
            session.permission_reply,
        )
        self.prompt = to_streamed_response_wrapper(
            session.prompt,
        )
        self.question_list = to_streamed_response_wrapper(
            session.question_list,
        )
        self.question_reject = to_streamed_response_wrapper(
            session.question_reject,
        )
        self.question_reply = to_streamed_response_wrapper(
            session.question_reply,
        )
        self.revert_clear = to_streamed_response_wrapper(
            session.revert_clear,
        )
        self.revert_commit = to_streamed_response_wrapper(
            session.revert_commit,
        )
        self.revert_stage = to_streamed_response_wrapper(
            session.revert_stage,
        )
        self.switch_agent = to_streamed_response_wrapper(
            session.switch_agent,
        )
        self.switch_model = to_streamed_response_wrapper(
            session.switch_model,
        )
        self.wait = to_streamed_response_wrapper(
            session.wait,
        )


class AsyncV2SessionResourceWithStreamingResponse:
    def __init__(self, session: AsyncV2SessionResource) -> None:
        self._session = session

        self.active = async_to_streamed_response_wrapper(
            session.active,
        )
        self.compact = async_to_streamed_response_wrapper(
            session.compact,
        )
        self.context = async_to_streamed_response_wrapper(
            session.context,
        )
        self.create = async_to_streamed_response_wrapper(
            session.create,
        )
        self.events = async_to_streamed_response_wrapper(
            session.events,
        )
        self.get = async_to_streamed_response_wrapper(
            session.get,
        )
        self.history = async_to_streamed_response_wrapper(
            session.history,
        )
        self.interrupt = async_to_streamed_response_wrapper(
            session.interrupt,
        )
        self.list = async_to_streamed_response_wrapper(
            session.list,
        )
        self.message = async_to_streamed_response_wrapper(
            session.message,
        )
        self.messages = async_to_streamed_response_wrapper(
            session.messages,
        )
        self.permission_create = async_to_streamed_response_wrapper(
            session.permission_create,
        )
        self.permission_get = async_to_streamed_response_wrapper(
            session.permission_get,
        )
        self.permission_list = async_to_streamed_response_wrapper(
            session.permission_list,
        )
        self.permission_reply = async_to_streamed_response_wrapper(
            session.permission_reply,
        )
        self.prompt = async_to_streamed_response_wrapper(
            session.prompt,
        )
        self.question_list = async_to_streamed_response_wrapper(
            session.question_list,
        )
        self.question_reject = async_to_streamed_response_wrapper(
            session.question_reject,
        )
        self.question_reply = async_to_streamed_response_wrapper(
            session.question_reply,
        )
        self.revert_clear = async_to_streamed_response_wrapper(
            session.revert_clear,
        )
        self.revert_commit = async_to_streamed_response_wrapper(
            session.revert_commit,
        )
        self.revert_stage = async_to_streamed_response_wrapper(
            session.revert_stage,
        )
        self.switch_agent = async_to_streamed_response_wrapper(
            session.switch_agent,
        )
        self.switch_model = async_to_streamed_response_wrapper(
            session.switch_model,
        )
        self.wait = async_to_streamed_response_wrapper(
            session.wait,
        )
