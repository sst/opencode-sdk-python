# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import app, tui, file, find, path, agent, event, config, command, project, session
    from .resources.app import AppResource, AsyncAppResource
    from .resources.tui import TuiResource, AsyncTuiResource
    from .resources.file import FileResource, AsyncFileResource
    from .resources.find import FindResource, AsyncFindResource
    from .resources.path import PathResource, AsyncPathResource
    from .resources.agent import AgentResource, AsyncAgentResource
    from .resources.event import EventResource, AsyncEventResource
    from .resources.config import ConfigResource, AsyncConfigResource
    from .resources.command import CommandResource, AsyncCommandResource
    from .resources.project import ProjectResource, AsyncProjectResource
    from .resources.session.session import SessionResource, AsyncSessionResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Opencode",
    "AsyncOpencode",
    "Client",
    "AsyncClient",
]


class Opencode(SyncAPIClient):
    # client options

    def __init__(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Opencode client instance."""
        if base_url is None:
            base_url = os.environ.get("OPENCODE_BASE_URL")
        if base_url is None:
            base_url = f"http://localhost:54321"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._default_stream_cls = Stream

    @cached_property
    def event(self) -> EventResource:
        from .resources.event import EventResource

        return EventResource(self)

    @cached_property
    def path(self) -> PathResource:
        from .resources.path import PathResource

        return PathResource(self)

    @cached_property
    def app(self) -> AppResource:
        from .resources.app import AppResource

        return AppResource(self)

    @cached_property
    def agent(self) -> AgentResource:
        from .resources.agent import AgentResource

        return AgentResource(self)

    @cached_property
    def find(self) -> FindResource:
        from .resources.find import FindResource

        return FindResource(self)

    @cached_property
    def file(self) -> FileResource:
        from .resources.file import FileResource

        return FileResource(self)

    @cached_property
    def config(self) -> ConfigResource:
        from .resources.config import ConfigResource

        return ConfigResource(self)

    @cached_property
    def command(self) -> CommandResource:
        from .resources.command import CommandResource

        return CommandResource(self)

    @cached_property
    def project(self) -> ProjectResource:
        from .resources.project import ProjectResource

        return ProjectResource(self)

    @cached_property
    def session(self) -> SessionResource:
        from .resources.session import SessionResource

        return SessionResource(self)

    @cached_property
    def tui(self) -> TuiResource:
        from .resources.tui import TuiResource

        return TuiResource(self)

    @cached_property
    def with_raw_response(self) -> OpencodeWithRawResponse:
        return OpencodeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OpencodeWithStreamedResponse:
        return OpencodeWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncOpencode(AsyncAPIClient):
    # client options

    def __init__(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncOpencode client instance."""
        if base_url is None:
            base_url = os.environ.get("OPENCODE_BASE_URL")
        if base_url is None:
            base_url = f"http://localhost:54321"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._default_stream_cls = AsyncStream

    @cached_property
    def event(self) -> AsyncEventResource:
        from .resources.event import AsyncEventResource

        return AsyncEventResource(self)

    @cached_property
    def path(self) -> AsyncPathResource:
        from .resources.path import AsyncPathResource

        return AsyncPathResource(self)

    @cached_property
    def app(self) -> AsyncAppResource:
        from .resources.app import AsyncAppResource

        return AsyncAppResource(self)

    @cached_property
    def agent(self) -> AsyncAgentResource:
        from .resources.agent import AsyncAgentResource

        return AsyncAgentResource(self)

    @cached_property
    def find(self) -> AsyncFindResource:
        from .resources.find import AsyncFindResource

        return AsyncFindResource(self)

    @cached_property
    def file(self) -> AsyncFileResource:
        from .resources.file import AsyncFileResource

        return AsyncFileResource(self)

    @cached_property
    def config(self) -> AsyncConfigResource:
        from .resources.config import AsyncConfigResource

        return AsyncConfigResource(self)

    @cached_property
    def command(self) -> AsyncCommandResource:
        from .resources.command import AsyncCommandResource

        return AsyncCommandResource(self)

    @cached_property
    def project(self) -> AsyncProjectResource:
        from .resources.project import AsyncProjectResource

        return AsyncProjectResource(self)

    @cached_property
    def session(self) -> AsyncSessionResource:
        from .resources.session import AsyncSessionResource

        return AsyncSessionResource(self)

    @cached_property
    def tui(self) -> AsyncTuiResource:
        from .resources.tui import AsyncTuiResource

        return AsyncTuiResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncOpencodeWithRawResponse:
        return AsyncOpencodeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOpencodeWithStreamedResponse:
        return AsyncOpencodeWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class OpencodeWithRawResponse:
    _client: Opencode

    def __init__(self, client: Opencode) -> None:
        self._client = client

    @cached_property
    def event(self) -> event.EventResourceWithRawResponse:
        from .resources.event import EventResourceWithRawResponse

        return EventResourceWithRawResponse(self._client.event)

    @cached_property
    def path(self) -> path.PathResourceWithRawResponse:
        from .resources.path import PathResourceWithRawResponse

        return PathResourceWithRawResponse(self._client.path)

    @cached_property
    def app(self) -> app.AppResourceWithRawResponse:
        from .resources.app import AppResourceWithRawResponse

        return AppResourceWithRawResponse(self._client.app)

    @cached_property
    def agent(self) -> agent.AgentResourceWithRawResponse:
        from .resources.agent import AgentResourceWithRawResponse

        return AgentResourceWithRawResponse(self._client.agent)

    @cached_property
    def find(self) -> find.FindResourceWithRawResponse:
        from .resources.find import FindResourceWithRawResponse

        return FindResourceWithRawResponse(self._client.find)

    @cached_property
    def file(self) -> file.FileResourceWithRawResponse:
        from .resources.file import FileResourceWithRawResponse

        return FileResourceWithRawResponse(self._client.file)

    @cached_property
    def config(self) -> config.ConfigResourceWithRawResponse:
        from .resources.config import ConfigResourceWithRawResponse

        return ConfigResourceWithRawResponse(self._client.config)

    @cached_property
    def command(self) -> command.CommandResourceWithRawResponse:
        from .resources.command import CommandResourceWithRawResponse

        return CommandResourceWithRawResponse(self._client.command)

    @cached_property
    def project(self) -> project.ProjectResourceWithRawResponse:
        from .resources.project import ProjectResourceWithRawResponse

        return ProjectResourceWithRawResponse(self._client.project)

    @cached_property
    def session(self) -> session.SessionResourceWithRawResponse:
        from .resources.session import SessionResourceWithRawResponse

        return SessionResourceWithRawResponse(self._client.session)

    @cached_property
    def tui(self) -> tui.TuiResourceWithRawResponse:
        from .resources.tui import TuiResourceWithRawResponse

        return TuiResourceWithRawResponse(self._client.tui)


class AsyncOpencodeWithRawResponse:
    _client: AsyncOpencode

    def __init__(self, client: AsyncOpencode) -> None:
        self._client = client

    @cached_property
    def event(self) -> event.AsyncEventResourceWithRawResponse:
        from .resources.event import AsyncEventResourceWithRawResponse

        return AsyncEventResourceWithRawResponse(self._client.event)

    @cached_property
    def path(self) -> path.AsyncPathResourceWithRawResponse:
        from .resources.path import AsyncPathResourceWithRawResponse

        return AsyncPathResourceWithRawResponse(self._client.path)

    @cached_property
    def app(self) -> app.AsyncAppResourceWithRawResponse:
        from .resources.app import AsyncAppResourceWithRawResponse

        return AsyncAppResourceWithRawResponse(self._client.app)

    @cached_property
    def agent(self) -> agent.AsyncAgentResourceWithRawResponse:
        from .resources.agent import AsyncAgentResourceWithRawResponse

        return AsyncAgentResourceWithRawResponse(self._client.agent)

    @cached_property
    def find(self) -> find.AsyncFindResourceWithRawResponse:
        from .resources.find import AsyncFindResourceWithRawResponse

        return AsyncFindResourceWithRawResponse(self._client.find)

    @cached_property
    def file(self) -> file.AsyncFileResourceWithRawResponse:
        from .resources.file import AsyncFileResourceWithRawResponse

        return AsyncFileResourceWithRawResponse(self._client.file)

    @cached_property
    def config(self) -> config.AsyncConfigResourceWithRawResponse:
        from .resources.config import AsyncConfigResourceWithRawResponse

        return AsyncConfigResourceWithRawResponse(self._client.config)

    @cached_property
    def command(self) -> command.AsyncCommandResourceWithRawResponse:
        from .resources.command import AsyncCommandResourceWithRawResponse

        return AsyncCommandResourceWithRawResponse(self._client.command)

    @cached_property
    def project(self) -> project.AsyncProjectResourceWithRawResponse:
        from .resources.project import AsyncProjectResourceWithRawResponse

        return AsyncProjectResourceWithRawResponse(self._client.project)

    @cached_property
    def session(self) -> session.AsyncSessionResourceWithRawResponse:
        from .resources.session import AsyncSessionResourceWithRawResponse

        return AsyncSessionResourceWithRawResponse(self._client.session)

    @cached_property
    def tui(self) -> tui.AsyncTuiResourceWithRawResponse:
        from .resources.tui import AsyncTuiResourceWithRawResponse

        return AsyncTuiResourceWithRawResponse(self._client.tui)


class OpencodeWithStreamedResponse:
    _client: Opencode

    def __init__(self, client: Opencode) -> None:
        self._client = client

    @cached_property
    def event(self) -> event.EventResourceWithStreamingResponse:
        from .resources.event import EventResourceWithStreamingResponse

        return EventResourceWithStreamingResponse(self._client.event)

    @cached_property
    def path(self) -> path.PathResourceWithStreamingResponse:
        from .resources.path import PathResourceWithStreamingResponse

        return PathResourceWithStreamingResponse(self._client.path)

    @cached_property
    def app(self) -> app.AppResourceWithStreamingResponse:
        from .resources.app import AppResourceWithStreamingResponse

        return AppResourceWithStreamingResponse(self._client.app)

    @cached_property
    def agent(self) -> agent.AgentResourceWithStreamingResponse:
        from .resources.agent import AgentResourceWithStreamingResponse

        return AgentResourceWithStreamingResponse(self._client.agent)

    @cached_property
    def find(self) -> find.FindResourceWithStreamingResponse:
        from .resources.find import FindResourceWithStreamingResponse

        return FindResourceWithStreamingResponse(self._client.find)

    @cached_property
    def file(self) -> file.FileResourceWithStreamingResponse:
        from .resources.file import FileResourceWithStreamingResponse

        return FileResourceWithStreamingResponse(self._client.file)

    @cached_property
    def config(self) -> config.ConfigResourceWithStreamingResponse:
        from .resources.config import ConfigResourceWithStreamingResponse

        return ConfigResourceWithStreamingResponse(self._client.config)

    @cached_property
    def command(self) -> command.CommandResourceWithStreamingResponse:
        from .resources.command import CommandResourceWithStreamingResponse

        return CommandResourceWithStreamingResponse(self._client.command)

    @cached_property
    def project(self) -> project.ProjectResourceWithStreamingResponse:
        from .resources.project import ProjectResourceWithStreamingResponse

        return ProjectResourceWithStreamingResponse(self._client.project)

    @cached_property
    def session(self) -> session.SessionResourceWithStreamingResponse:
        from .resources.session import SessionResourceWithStreamingResponse

        return SessionResourceWithStreamingResponse(self._client.session)

    @cached_property
    def tui(self) -> tui.TuiResourceWithStreamingResponse:
        from .resources.tui import TuiResourceWithStreamingResponse

        return TuiResourceWithStreamingResponse(self._client.tui)


class AsyncOpencodeWithStreamedResponse:
    _client: AsyncOpencode

    def __init__(self, client: AsyncOpencode) -> None:
        self._client = client

    @cached_property
    def event(self) -> event.AsyncEventResourceWithStreamingResponse:
        from .resources.event import AsyncEventResourceWithStreamingResponse

        return AsyncEventResourceWithStreamingResponse(self._client.event)

    @cached_property
    def path(self) -> path.AsyncPathResourceWithStreamingResponse:
        from .resources.path import AsyncPathResourceWithStreamingResponse

        return AsyncPathResourceWithStreamingResponse(self._client.path)

    @cached_property
    def app(self) -> app.AsyncAppResourceWithStreamingResponse:
        from .resources.app import AsyncAppResourceWithStreamingResponse

        return AsyncAppResourceWithStreamingResponse(self._client.app)

    @cached_property
    def agent(self) -> agent.AsyncAgentResourceWithStreamingResponse:
        from .resources.agent import AsyncAgentResourceWithStreamingResponse

        return AsyncAgentResourceWithStreamingResponse(self._client.agent)

    @cached_property
    def find(self) -> find.AsyncFindResourceWithStreamingResponse:
        from .resources.find import AsyncFindResourceWithStreamingResponse

        return AsyncFindResourceWithStreamingResponse(self._client.find)

    @cached_property
    def file(self) -> file.AsyncFileResourceWithStreamingResponse:
        from .resources.file import AsyncFileResourceWithStreamingResponse

        return AsyncFileResourceWithStreamingResponse(self._client.file)

    @cached_property
    def config(self) -> config.AsyncConfigResourceWithStreamingResponse:
        from .resources.config import AsyncConfigResourceWithStreamingResponse

        return AsyncConfigResourceWithStreamingResponse(self._client.config)

    @cached_property
    def command(self) -> command.AsyncCommandResourceWithStreamingResponse:
        from .resources.command import AsyncCommandResourceWithStreamingResponse

        return AsyncCommandResourceWithStreamingResponse(self._client.command)

    @cached_property
    def project(self) -> project.AsyncProjectResourceWithStreamingResponse:
        from .resources.project import AsyncProjectResourceWithStreamingResponse

        return AsyncProjectResourceWithStreamingResponse(self._client.project)

    @cached_property
    def session(self) -> session.AsyncSessionResourceWithStreamingResponse:
        from .resources.session import AsyncSessionResourceWithStreamingResponse

        return AsyncSessionResourceWithStreamingResponse(self._client.session)

    @cached_property
    def tui(self) -> tui.AsyncTuiResourceWithStreamingResponse:
        from .resources.tui import AsyncTuiResourceWithStreamingResponse

        return AsyncTuiResourceWithStreamingResponse(self._client.tui)


Client = Opencode

AsyncClient = AsyncOpencode
