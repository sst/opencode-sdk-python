# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from .fs import (
    V2FsResource,
    AsyncV2FsResource,
    V2FsResourceWithRawResponse,
    AsyncV2FsResourceWithRawResponse,
    V2FsResourceWithStreamingResponse,
    AsyncV2FsResourceWithStreamingResponse,
)
from .pty import (
    V2PtyResource,
    AsyncV2PtyResource,
    V2PtyResourceWithRawResponse,
    AsyncV2PtyResourceWithRawResponse,
    V2PtyResourceWithStreamingResponse,
    AsyncV2PtyResourceWithStreamingResponse,
)
from .agent import (
    V2AgentResource,
    AsyncV2AgentResource,
    V2AgentResourceWithRawResponse,
    AsyncV2AgentResourceWithRawResponse,
    V2AgentResourceWithStreamingResponse,
    AsyncV2AgentResourceWithStreamingResponse,
)
from .event import (
    V2EventResource,
    AsyncV2EventResource,
    V2EventResourceWithRawResponse,
    AsyncV2EventResourceWithRawResponse,
    V2EventResourceWithStreamingResponse,
    AsyncV2EventResourceWithStreamingResponse,
)
from .model import (
    V2ModelResource,
    AsyncV2ModelResource,
    V2ModelResourceWithRawResponse,
    AsyncV2ModelResourceWithRawResponse,
    V2ModelResourceWithStreamingResponse,
    AsyncV2ModelResourceWithStreamingResponse,
)
from .skill import (
    V2SkillResource,
    AsyncV2SkillResource,
    V2SkillResourceWithRawResponse,
    AsyncV2SkillResourceWithRawResponse,
    V2SkillResourceWithStreamingResponse,
    AsyncV2SkillResourceWithStreamingResponse,
)
from .health import (
    V2HealthResource,
    AsyncV2HealthResource,
    V2HealthResourceWithRawResponse,
    AsyncV2HealthResourceWithRawResponse,
    V2HealthResourceWithStreamingResponse,
    AsyncV2HealthResourceWithStreamingResponse,
)
from .command import (
    V2CommandResource,
    AsyncV2CommandResource,
    V2CommandResourceWithRawResponse,
    AsyncV2CommandResourceWithRawResponse,
    V2CommandResourceWithStreamingResponse,
    AsyncV2CommandResourceWithStreamingResponse,
)
from .session import (
    V2SessionResource,
    AsyncV2SessionResource,
    V2SessionResourceWithRawResponse,
    AsyncV2SessionResourceWithRawResponse,
    V2SessionResourceWithStreamingResponse,
    AsyncV2SessionResourceWithStreamingResponse,
)
from .location import (
    V2LocationResource,
    AsyncV2LocationResource,
    V2LocationResourceWithRawResponse,
    AsyncV2LocationResourceWithRawResponse,
    V2LocationResourceWithStreamingResponse,
    AsyncV2LocationResourceWithStreamingResponse,
)
from .provider import (
    V2ProviderResource,
    AsyncV2ProviderResource,
    V2ProviderResourceWithRawResponse,
    AsyncV2ProviderResourceWithRawResponse,
    V2ProviderResourceWithStreamingResponse,
    AsyncV2ProviderResourceWithStreamingResponse,
)
from .question import (
    V2QuestionResource,
    AsyncV2QuestionResource,
    V2QuestionResourceWithRawResponse,
    AsyncV2QuestionResourceWithRawResponse,
    V2QuestionResourceWithStreamingResponse,
    AsyncV2QuestionResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .reference import (
    V2ReferenceResource,
    AsyncV2ReferenceResource,
    V2ReferenceResourceWithRawResponse,
    AsyncV2ReferenceResourceWithRawResponse,
    V2ReferenceResourceWithStreamingResponse,
    AsyncV2ReferenceResourceWithStreamingResponse,
)
from .credential import (
    V2CredentialResource,
    AsyncV2CredentialResource,
    V2CredentialResourceWithRawResponse,
    AsyncV2CredentialResourceWithRawResponse,
    V2CredentialResourceWithStreamingResponse,
    AsyncV2CredentialResourceWithStreamingResponse,
)
from .permission import (
    V2PermissionResource,
    AsyncV2PermissionResource,
    V2PermissionResourceWithRawResponse,
    AsyncV2PermissionResourceWithRawResponse,
    V2PermissionResourceWithStreamingResponse,
    AsyncV2PermissionResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .integration import (
    V2IntegrationResource,
    AsyncV2IntegrationResource,
    V2IntegrationResourceWithRawResponse,
    AsyncV2IntegrationResourceWithRawResponse,
    V2IntegrationResourceWithStreamingResponse,
    AsyncV2IntegrationResourceWithStreamingResponse,
)
from .project_copy import (
    V2ProjectCopyResource,
    AsyncV2ProjectCopyResource,
    V2ProjectCopyResourceWithRawResponse,
    AsyncV2ProjectCopyResourceWithRawResponse,
    V2ProjectCopyResourceWithStreamingResponse,
    AsyncV2ProjectCopyResourceWithStreamingResponse,
)

__all__ = [
    "V2Resource",
    "AsyncV2Resource",
    "V2ResourceWithRawResponse",
    "AsyncV2ResourceWithRawResponse",
    "V2ResourceWithStreamingResponse",
    "AsyncV2ResourceWithStreamingResponse",
    "V2SessionResource",
    "AsyncV2SessionResource",
    "V2IntegrationResource",
    "AsyncV2IntegrationResource",
    "V2PtyResource",
    "AsyncV2PtyResource",
    "V2PermissionResource",
    "AsyncV2PermissionResource",
    "V2FsResource",
    "AsyncV2FsResource",
    "V2QuestionResource",
    "AsyncV2QuestionResource",
    "V2ProviderResource",
    "AsyncV2ProviderResource",
    "V2CredentialResource",
    "AsyncV2CredentialResource",
    "V2HealthResource",
    "AsyncV2HealthResource",
    "V2LocationResource",
    "AsyncV2LocationResource",
    "V2AgentResource",
    "AsyncV2AgentResource",
    "V2ModelResource",
    "AsyncV2ModelResource",
    "V2CommandResource",
    "AsyncV2CommandResource",
    "V2SkillResource",
    "AsyncV2SkillResource",
    "V2EventResource",
    "AsyncV2EventResource",
    "V2ReferenceResource",
    "AsyncV2ReferenceResource",
    "V2ProjectCopyResource",
    "AsyncV2ProjectCopyResource",
]


class V2Resource(SyncAPIResource):
    @cached_property
    def session(self) -> V2SessionResource:
        return V2SessionResource(self._client)

    @cached_property
    def integration(self) -> V2IntegrationResource:
        return V2IntegrationResource(self._client)

    @cached_property
    def pty(self) -> V2PtyResource:
        return V2PtyResource(self._client)

    @cached_property
    def permission(self) -> V2PermissionResource:
        return V2PermissionResource(self._client)

    @cached_property
    def fs(self) -> V2FsResource:
        return V2FsResource(self._client)

    @cached_property
    def question(self) -> V2QuestionResource:
        return V2QuestionResource(self._client)

    @cached_property
    def provider(self) -> V2ProviderResource:
        return V2ProviderResource(self._client)

    @cached_property
    def credential(self) -> V2CredentialResource:
        return V2CredentialResource(self._client)

    @cached_property
    def health(self) -> V2HealthResource:
        return V2HealthResource(self._client)

    @cached_property
    def location(self) -> V2LocationResource:
        return V2LocationResource(self._client)

    @cached_property
    def agent(self) -> V2AgentResource:
        return V2AgentResource(self._client)

    @cached_property
    def model(self) -> V2ModelResource:
        return V2ModelResource(self._client)

    @cached_property
    def command(self) -> V2CommandResource:
        return V2CommandResource(self._client)

    @cached_property
    def skill(self) -> V2SkillResource:
        return V2SkillResource(self._client)

    @cached_property
    def event(self) -> V2EventResource:
        return V2EventResource(self._client)

    @cached_property
    def reference(self) -> V2ReferenceResource:
        return V2ReferenceResource(self._client)

    @cached_property
    def project_copy(self) -> V2ProjectCopyResource:
        return V2ProjectCopyResource(self._client)

    @cached_property
    def with_raw_response(self) -> V2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return V2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return V2ResourceWithStreamingResponse(self)


class AsyncV2Resource(AsyncAPIResource):
    @cached_property
    def session(self) -> AsyncV2SessionResource:
        return AsyncV2SessionResource(self._client)

    @cached_property
    def integration(self) -> AsyncV2IntegrationResource:
        return AsyncV2IntegrationResource(self._client)

    @cached_property
    def pty(self) -> AsyncV2PtyResource:
        return AsyncV2PtyResource(self._client)

    @cached_property
    def permission(self) -> AsyncV2PermissionResource:
        return AsyncV2PermissionResource(self._client)

    @cached_property
    def fs(self) -> AsyncV2FsResource:
        return AsyncV2FsResource(self._client)

    @cached_property
    def question(self) -> AsyncV2QuestionResource:
        return AsyncV2QuestionResource(self._client)

    @cached_property
    def provider(self) -> AsyncV2ProviderResource:
        return AsyncV2ProviderResource(self._client)

    @cached_property
    def credential(self) -> AsyncV2CredentialResource:
        return AsyncV2CredentialResource(self._client)

    @cached_property
    def health(self) -> AsyncV2HealthResource:
        return AsyncV2HealthResource(self._client)

    @cached_property
    def location(self) -> AsyncV2LocationResource:
        return AsyncV2LocationResource(self._client)

    @cached_property
    def agent(self) -> AsyncV2AgentResource:
        return AsyncV2AgentResource(self._client)

    @cached_property
    def model(self) -> AsyncV2ModelResource:
        return AsyncV2ModelResource(self._client)

    @cached_property
    def command(self) -> AsyncV2CommandResource:
        return AsyncV2CommandResource(self._client)

    @cached_property
    def skill(self) -> AsyncV2SkillResource:
        return AsyncV2SkillResource(self._client)

    @cached_property
    def event(self) -> AsyncV2EventResource:
        return AsyncV2EventResource(self._client)

    @cached_property
    def reference(self) -> AsyncV2ReferenceResource:
        return AsyncV2ReferenceResource(self._client)

    @cached_property
    def project_copy(self) -> AsyncV2ProjectCopyResource:
        return AsyncV2ProjectCopyResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncV2ResourceWithStreamingResponse(self)


class V2ResourceWithRawResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

    @cached_property
    def session(self) -> V2SessionResourceWithRawResponse:
        return V2SessionResourceWithRawResponse(self._v2.session)

    @cached_property
    def integration(self) -> V2IntegrationResourceWithRawResponse:
        return V2IntegrationResourceWithRawResponse(self._v2.integration)

    @cached_property
    def pty(self) -> V2PtyResourceWithRawResponse:
        return V2PtyResourceWithRawResponse(self._v2.pty)

    @cached_property
    def permission(self) -> V2PermissionResourceWithRawResponse:
        return V2PermissionResourceWithRawResponse(self._v2.permission)

    @cached_property
    def fs(self) -> V2FsResourceWithRawResponse:
        return V2FsResourceWithRawResponse(self._v2.fs)

    @cached_property
    def question(self) -> V2QuestionResourceWithRawResponse:
        return V2QuestionResourceWithRawResponse(self._v2.question)

    @cached_property
    def provider(self) -> V2ProviderResourceWithRawResponse:
        return V2ProviderResourceWithRawResponse(self._v2.provider)

    @cached_property
    def credential(self) -> V2CredentialResourceWithRawResponse:
        return V2CredentialResourceWithRawResponse(self._v2.credential)

    @cached_property
    def health(self) -> V2HealthResourceWithRawResponse:
        return V2HealthResourceWithRawResponse(self._v2.health)

    @cached_property
    def location(self) -> V2LocationResourceWithRawResponse:
        return V2LocationResourceWithRawResponse(self._v2.location)

    @cached_property
    def agent(self) -> V2AgentResourceWithRawResponse:
        return V2AgentResourceWithRawResponse(self._v2.agent)

    @cached_property
    def model(self) -> V2ModelResourceWithRawResponse:
        return V2ModelResourceWithRawResponse(self._v2.model)

    @cached_property
    def command(self) -> V2CommandResourceWithRawResponse:
        return V2CommandResourceWithRawResponse(self._v2.command)

    @cached_property
    def skill(self) -> V2SkillResourceWithRawResponse:
        return V2SkillResourceWithRawResponse(self._v2.skill)

    @cached_property
    def event(self) -> V2EventResourceWithRawResponse:
        return V2EventResourceWithRawResponse(self._v2.event)

    @cached_property
    def reference(self) -> V2ReferenceResourceWithRawResponse:
        return V2ReferenceResourceWithRawResponse(self._v2.reference)

    @cached_property
    def project_copy(self) -> V2ProjectCopyResourceWithRawResponse:
        return V2ProjectCopyResourceWithRawResponse(self._v2.project_copy)


class AsyncV2ResourceWithRawResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

    @cached_property
    def session(self) -> AsyncV2SessionResourceWithRawResponse:
        return AsyncV2SessionResourceWithRawResponse(self._v2.session)

    @cached_property
    def integration(self) -> AsyncV2IntegrationResourceWithRawResponse:
        return AsyncV2IntegrationResourceWithRawResponse(self._v2.integration)

    @cached_property
    def pty(self) -> AsyncV2PtyResourceWithRawResponse:
        return AsyncV2PtyResourceWithRawResponse(self._v2.pty)

    @cached_property
    def permission(self) -> AsyncV2PermissionResourceWithRawResponse:
        return AsyncV2PermissionResourceWithRawResponse(self._v2.permission)

    @cached_property
    def fs(self) -> AsyncV2FsResourceWithRawResponse:
        return AsyncV2FsResourceWithRawResponse(self._v2.fs)

    @cached_property
    def question(self) -> AsyncV2QuestionResourceWithRawResponse:
        return AsyncV2QuestionResourceWithRawResponse(self._v2.question)

    @cached_property
    def provider(self) -> AsyncV2ProviderResourceWithRawResponse:
        return AsyncV2ProviderResourceWithRawResponse(self._v2.provider)

    @cached_property
    def credential(self) -> AsyncV2CredentialResourceWithRawResponse:
        return AsyncV2CredentialResourceWithRawResponse(self._v2.credential)

    @cached_property
    def health(self) -> AsyncV2HealthResourceWithRawResponse:
        return AsyncV2HealthResourceWithRawResponse(self._v2.health)

    @cached_property
    def location(self) -> AsyncV2LocationResourceWithRawResponse:
        return AsyncV2LocationResourceWithRawResponse(self._v2.location)

    @cached_property
    def agent(self) -> AsyncV2AgentResourceWithRawResponse:
        return AsyncV2AgentResourceWithRawResponse(self._v2.agent)

    @cached_property
    def model(self) -> AsyncV2ModelResourceWithRawResponse:
        return AsyncV2ModelResourceWithRawResponse(self._v2.model)

    @cached_property
    def command(self) -> AsyncV2CommandResourceWithRawResponse:
        return AsyncV2CommandResourceWithRawResponse(self._v2.command)

    @cached_property
    def skill(self) -> AsyncV2SkillResourceWithRawResponse:
        return AsyncV2SkillResourceWithRawResponse(self._v2.skill)

    @cached_property
    def event(self) -> AsyncV2EventResourceWithRawResponse:
        return AsyncV2EventResourceWithRawResponse(self._v2.event)

    @cached_property
    def reference(self) -> AsyncV2ReferenceResourceWithRawResponse:
        return AsyncV2ReferenceResourceWithRawResponse(self._v2.reference)

    @cached_property
    def project_copy(self) -> AsyncV2ProjectCopyResourceWithRawResponse:
        return AsyncV2ProjectCopyResourceWithRawResponse(self._v2.project_copy)


class V2ResourceWithStreamingResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

    @cached_property
    def session(self) -> V2SessionResourceWithStreamingResponse:
        return V2SessionResourceWithStreamingResponse(self._v2.session)

    @cached_property
    def integration(self) -> V2IntegrationResourceWithStreamingResponse:
        return V2IntegrationResourceWithStreamingResponse(self._v2.integration)

    @cached_property
    def pty(self) -> V2PtyResourceWithStreamingResponse:
        return V2PtyResourceWithStreamingResponse(self._v2.pty)

    @cached_property
    def permission(self) -> V2PermissionResourceWithStreamingResponse:
        return V2PermissionResourceWithStreamingResponse(self._v2.permission)

    @cached_property
    def fs(self) -> V2FsResourceWithStreamingResponse:
        return V2FsResourceWithStreamingResponse(self._v2.fs)

    @cached_property
    def question(self) -> V2QuestionResourceWithStreamingResponse:
        return V2QuestionResourceWithStreamingResponse(self._v2.question)

    @cached_property
    def provider(self) -> V2ProviderResourceWithStreamingResponse:
        return V2ProviderResourceWithStreamingResponse(self._v2.provider)

    @cached_property
    def credential(self) -> V2CredentialResourceWithStreamingResponse:
        return V2CredentialResourceWithStreamingResponse(self._v2.credential)

    @cached_property
    def health(self) -> V2HealthResourceWithStreamingResponse:
        return V2HealthResourceWithStreamingResponse(self._v2.health)

    @cached_property
    def location(self) -> V2LocationResourceWithStreamingResponse:
        return V2LocationResourceWithStreamingResponse(self._v2.location)

    @cached_property
    def agent(self) -> V2AgentResourceWithStreamingResponse:
        return V2AgentResourceWithStreamingResponse(self._v2.agent)

    @cached_property
    def model(self) -> V2ModelResourceWithStreamingResponse:
        return V2ModelResourceWithStreamingResponse(self._v2.model)

    @cached_property
    def command(self) -> V2CommandResourceWithStreamingResponse:
        return V2CommandResourceWithStreamingResponse(self._v2.command)

    @cached_property
    def skill(self) -> V2SkillResourceWithStreamingResponse:
        return V2SkillResourceWithStreamingResponse(self._v2.skill)

    @cached_property
    def event(self) -> V2EventResourceWithStreamingResponse:
        return V2EventResourceWithStreamingResponse(self._v2.event)

    @cached_property
    def reference(self) -> V2ReferenceResourceWithStreamingResponse:
        return V2ReferenceResourceWithStreamingResponse(self._v2.reference)

    @cached_property
    def project_copy(self) -> V2ProjectCopyResourceWithStreamingResponse:
        return V2ProjectCopyResourceWithStreamingResponse(self._v2.project_copy)


class AsyncV2ResourceWithStreamingResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

    @cached_property
    def session(self) -> AsyncV2SessionResourceWithStreamingResponse:
        return AsyncV2SessionResourceWithStreamingResponse(self._v2.session)

    @cached_property
    def integration(self) -> AsyncV2IntegrationResourceWithStreamingResponse:
        return AsyncV2IntegrationResourceWithStreamingResponse(self._v2.integration)

    @cached_property
    def pty(self) -> AsyncV2PtyResourceWithStreamingResponse:
        return AsyncV2PtyResourceWithStreamingResponse(self._v2.pty)

    @cached_property
    def permission(self) -> AsyncV2PermissionResourceWithStreamingResponse:
        return AsyncV2PermissionResourceWithStreamingResponse(self._v2.permission)

    @cached_property
    def fs(self) -> AsyncV2FsResourceWithStreamingResponse:
        return AsyncV2FsResourceWithStreamingResponse(self._v2.fs)

    @cached_property
    def question(self) -> AsyncV2QuestionResourceWithStreamingResponse:
        return AsyncV2QuestionResourceWithStreamingResponse(self._v2.question)

    @cached_property
    def provider(self) -> AsyncV2ProviderResourceWithStreamingResponse:
        return AsyncV2ProviderResourceWithStreamingResponse(self._v2.provider)

    @cached_property
    def credential(self) -> AsyncV2CredentialResourceWithStreamingResponse:
        return AsyncV2CredentialResourceWithStreamingResponse(self._v2.credential)

    @cached_property
    def health(self) -> AsyncV2HealthResourceWithStreamingResponse:
        return AsyncV2HealthResourceWithStreamingResponse(self._v2.health)

    @cached_property
    def location(self) -> AsyncV2LocationResourceWithStreamingResponse:
        return AsyncV2LocationResourceWithStreamingResponse(self._v2.location)

    @cached_property
    def agent(self) -> AsyncV2AgentResourceWithStreamingResponse:
        return AsyncV2AgentResourceWithStreamingResponse(self._v2.agent)

    @cached_property
    def model(self) -> AsyncV2ModelResourceWithStreamingResponse:
        return AsyncV2ModelResourceWithStreamingResponse(self._v2.model)

    @cached_property
    def command(self) -> AsyncV2CommandResourceWithStreamingResponse:
        return AsyncV2CommandResourceWithStreamingResponse(self._v2.command)

    @cached_property
    def skill(self) -> AsyncV2SkillResourceWithStreamingResponse:
        return AsyncV2SkillResourceWithStreamingResponse(self._v2.skill)

    @cached_property
    def event(self) -> AsyncV2EventResourceWithStreamingResponse:
        return AsyncV2EventResourceWithStreamingResponse(self._v2.event)

    @cached_property
    def reference(self) -> AsyncV2ReferenceResourceWithStreamingResponse:
        return AsyncV2ReferenceResourceWithStreamingResponse(self._v2.reference)

    @cached_property
    def project_copy(self) -> AsyncV2ProjectCopyResourceWithStreamingResponse:
        return AsyncV2ProjectCopyResourceWithStreamingResponse(self._v2.project_copy)
