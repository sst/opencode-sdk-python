# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing import List

import httpx

from ..types import addressing_params, question_reply_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.question_list_response import QuestionListResponse
from ..types.question_reply_response import QuestionReplyResponse
from ..types.question_reject_response import QuestionRejectResponse

__all__ = ["QuestionResource", "AsyncQuestionResource"]


class QuestionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QuestionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return QuestionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QuestionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return QuestionResourceWithStreamingResponse(self)

    def list(
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
    ) -> QuestionListResponse:
        """Get a list of all pending questions awaiting a response."""
        return self._get(
            "/question",
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
            cast_to=QuestionListResponse,
        )

    def reject(
        self,
        request_id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QuestionRejectResponse:
        """
        Reject a pending question, dismissing it without providing an answer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return self._post(
            f"/question/{request_id}/reject",
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
            cast_to=QuestionRejectResponse,
        )

    def reply(
        self,
        request_id: str,
        *,
        answers: List[List[str]],
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QuestionReplyResponse:
        """
        Answer a pending question with the given responses.

        Args:
          answers: User answers in order of questions (each answer is an array of selected
              labels)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return self._post(
            f"/question/{request_id}/reply",
            body=maybe_transform({"answers": answers}, question_reply_params.QuestionReplyParams),
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
            cast_to=QuestionReplyResponse,
        )


class AsyncQuestionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQuestionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQuestionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQuestionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncQuestionResourceWithStreamingResponse(self)

    async def list(
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
    ) -> QuestionListResponse:
        """Get a list of all pending questions awaiting a response."""
        return await self._get(
            "/question",
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
            cast_to=QuestionListResponse,
        )

    async def reject(
        self,
        request_id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QuestionRejectResponse:
        """
        Reject a pending question, dismissing it without providing an answer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return await self._post(
            f"/question/{request_id}/reject",
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
            cast_to=QuestionRejectResponse,
        )

    async def reply(
        self,
        request_id: str,
        *,
        answers: List[List[str]],
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QuestionReplyResponse:
        """
        Answer a pending question with the given responses.

        Args:
          answers: User answers in order of questions (each answer is an array of selected
              labels)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return await self._post(
            f"/question/{request_id}/reply",
            body=await async_maybe_transform({"answers": answers}, question_reply_params.QuestionReplyParams),
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
            cast_to=QuestionReplyResponse,
        )


class QuestionResourceWithRawResponse:
    def __init__(self, question: QuestionResource) -> None:
        self._question = question

        self.list = to_raw_response_wrapper(
            question.list,
        )
        self.reject = to_raw_response_wrapper(
            question.reject,
        )
        self.reply = to_raw_response_wrapper(
            question.reply,
        )


class AsyncQuestionResourceWithRawResponse:
    def __init__(self, question: AsyncQuestionResource) -> None:
        self._question = question

        self.list = async_to_raw_response_wrapper(
            question.list,
        )
        self.reject = async_to_raw_response_wrapper(
            question.reject,
        )
        self.reply = async_to_raw_response_wrapper(
            question.reply,
        )


class QuestionResourceWithStreamingResponse:
    def __init__(self, question: QuestionResource) -> None:
        self._question = question

        self.list = to_streamed_response_wrapper(
            question.list,
        )
        self.reject = to_streamed_response_wrapper(
            question.reject,
        )
        self.reply = to_streamed_response_wrapper(
            question.reply,
        )


class AsyncQuestionResourceWithStreamingResponse:
    def __init__(self, question: AsyncQuestionResource) -> None:
        self._question = question

        self.list = async_to_streamed_response_wrapper(
            question.list,
        )
        self.reject = async_to_streamed_response_wrapper(
            question.reject,
        )
        self.reply = async_to_streamed_response_wrapper(
            question.reply,
        )
