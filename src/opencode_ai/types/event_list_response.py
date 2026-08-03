# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .part import Part
from .._utils import PropertyInfo
from .message import Message
from .session import Session
from .._models import BaseModel
from .shared.api_error import APIError
from .shared.unknown_error import UnknownError
from .shared.provider_auth_error import ProviderAuthError
from .shared.message_aborted_error import MessageAbortedError
from .shared.context_overflow_error import ContextOverflowError
from .shared.structured_output_error import StructuredOutputError

__all__ = [
    "EventListResponse",
    "EventUnknown",
    "EventPluginAddedProperties",
    "EventPluginAdded",
    "EventCatalogModelUpdatedPropertiesModelApiAisdk",
    "EventCatalogModelUpdatedPropertiesModelApiNative",
    "EventCatalogModelUpdatedPropertiesModelApi",
    "EventCatalogModelUpdatedPropertiesModelCapabilities",
    "EventCatalogModelUpdatedPropertiesModelCostCache",
    "EventCatalogModelUpdatedPropertiesModelCostTier",
    "EventCatalogModelUpdatedPropertiesModelCost",
    "EventCatalogModelUpdatedPropertiesModelLimit",
    "EventCatalogModelUpdatedPropertiesModelRequest",
    "EventCatalogModelUpdatedPropertiesModelTime",
    "EventCatalogModelUpdatedPropertiesModelVariants",
    "EventCatalogModelUpdatedPropertiesModel",
    "EventCatalogModelUpdatedProperties",
    "EventCatalogModelUpdated",
    "EventSessionCreatedProperties",
    "EventSessionCreated",
    "EventSessionUpdatedProperties",
    "EventSessionUpdated",
    "EventSessionDeletedProperties",
    "EventSessionDeleted",
    "EventMessageUpdatedProperties",
    "EventMessageUpdated",
    "EventMessageRemovedProperties",
    "EventMessageRemoved",
    "EventMessagePartUpdatedProperties",
    "EventMessagePartUpdated",
    "EventMessagePartRemovedProperties",
    "EventMessagePartRemoved",
    "EventModelsDevRefreshed",
    "EventSessionNextAgentSwitchedProperties",
    "EventSessionNextAgentSwitched",
    "EventSessionNextModelSwitchedPropertiesModel",
    "EventSessionNextModelSwitchedProperties",
    "EventSessionNextModelSwitched",
    "EventSessionNextMovedPropertiesLocation",
    "EventSessionNextMovedProperties",
    "EventSessionNextMoved",
    "EventSessionNextPromptedPropertiesPromptAgentsSource",
    "EventSessionNextPromptedPropertiesPromptAgents",
    "EventSessionNextPromptedPropertiesPromptFilesSource",
    "EventSessionNextPromptedPropertiesPromptFiles",
    "EventSessionNextPromptedPropertiesPromptReferencesSource",
    "EventSessionNextPromptedPropertiesPromptReferences",
    "EventSessionNextPromptedPropertiesPrompt",
    "EventSessionNextPromptedProperties",
    "EventSessionNextPrompted",
    "EventSessionNextPromptAdmittedPropertiesPromptAgentsSource",
    "EventSessionNextPromptAdmittedPropertiesPromptAgents",
    "EventSessionNextPromptAdmittedPropertiesPromptFilesSource",
    "EventSessionNextPromptAdmittedPropertiesPromptFiles",
    "EventSessionNextPromptAdmittedPropertiesPromptReferencesSource",
    "EventSessionNextPromptAdmittedPropertiesPromptReferences",
    "EventSessionNextPromptAdmittedPropertiesPrompt",
    "EventSessionNextPromptAdmittedProperties",
    "EventSessionNextPromptAdmitted",
    "EventSessionNextPromptPromotedPropertiesPromptAgentsSource",
    "EventSessionNextPromptPromotedPropertiesPromptAgents",
    "EventSessionNextPromptPromotedPropertiesPromptFilesSource",
    "EventSessionNextPromptPromotedPropertiesPromptFiles",
    "EventSessionNextPromptPromotedPropertiesPromptReferencesSource",
    "EventSessionNextPromptPromotedPropertiesPromptReferences",
    "EventSessionNextPromptPromotedPropertiesPrompt",
    "EventSessionNextPromptPromotedProperties",
    "EventSessionNextPromptPromoted",
    "EventSessionNextContextUpdatedProperties",
    "EventSessionNextContextUpdated",
    "EventSessionNextSyntheticProperties",
    "EventSessionNextSynthetic",
    "EventSessionNextShellStartedProperties",
    "EventSessionNextShellStarted",
    "EventSessionNextShellEndedProperties",
    "EventSessionNextShellEnded",
    "EventSessionNextStepStartedPropertiesModel",
    "EventSessionNextStepStartedProperties",
    "EventSessionNextStepStarted",
    "EventSessionNextStepEndedPropertiesTokensCache",
    "EventSessionNextStepEndedPropertiesTokens",
    "EventSessionNextStepEndedProperties",
    "EventSessionNextStepEnded",
    "EventSessionNextStepFailedPropertiesError",
    "EventSessionNextStepFailedProperties",
    "EventSessionNextStepFailed",
    "EventSessionNextTextStartedProperties",
    "EventSessionNextTextStarted",
    "EventSessionNextTextDeltaProperties",
    "EventSessionNextTextDelta",
    "EventSessionNextTextEndedProperties",
    "EventSessionNextTextEnded",
    "EventSessionNextReasoningStartedProperties",
    "EventSessionNextReasoningStarted",
    "EventSessionNextReasoningDeltaProperties",
    "EventSessionNextReasoningDelta",
    "EventSessionNextReasoningEndedProperties",
    "EventSessionNextReasoningEnded",
    "EventSessionNextToolInputStartedProperties",
    "EventSessionNextToolInputStarted",
    "EventSessionNextToolInputDeltaProperties",
    "EventSessionNextToolInputDelta",
    "EventSessionNextToolInputEndedProperties",
    "EventSessionNextToolInputEnded",
    "EventSessionNextToolCalledPropertiesProvider",
    "EventSessionNextToolCalledProperties",
    "EventSessionNextToolCalled",
    "EventSessionNextToolProgressPropertiesContentToolTextContent",
    "EventSessionNextToolProgressPropertiesContentToolFileContentSourceData",
    "EventSessionNextToolProgressPropertiesContentToolFileContentSourceUrl",
    "EventSessionNextToolProgressPropertiesContentToolFileContentSourceFile",
    "EventSessionNextToolProgressPropertiesContentToolFileContentSource",
    "EventSessionNextToolProgressPropertiesContentToolFileContent",
    "EventSessionNextToolProgressPropertiesContent",
    "EventSessionNextToolProgressProperties",
    "EventSessionNextToolProgress",
    "EventSessionNextToolSuccessPropertiesContentToolTextContent",
    "EventSessionNextToolSuccessPropertiesContentToolFileContentSourceData",
    "EventSessionNextToolSuccessPropertiesContentToolFileContentSourceUrl",
    "EventSessionNextToolSuccessPropertiesContentToolFileContentSourceFile",
    "EventSessionNextToolSuccessPropertiesContentToolFileContentSource",
    "EventSessionNextToolSuccessPropertiesContentToolFileContent",
    "EventSessionNextToolSuccessPropertiesContent",
    "EventSessionNextToolSuccessPropertiesProvider",
    "EventSessionNextToolSuccessProperties",
    "EventSessionNextToolSuccess",
    "EventSessionNextToolFailedPropertiesError",
    "EventSessionNextToolFailedPropertiesProvider",
    "EventSessionNextToolFailedProperties",
    "EventSessionNextToolFailed",
    "EventSessionNextRetriedPropertiesError",
    "EventSessionNextRetriedProperties",
    "EventSessionNextRetried",
    "EventSessionNextCompactionStartedProperties",
    "EventSessionNextCompactionStarted",
    "EventSessionNextCompactionDeltaProperties",
    "EventSessionNextCompactionDelta",
    "EventSessionNextCompactionEndedProperties",
    "EventSessionNextCompactionEnded",
    "EventPermissionV2AskedPropertiesSource",
    "EventPermissionV2AskedProperties",
    "EventPermissionV2Asked",
    "EventPermissionV2RepliedProperties",
    "EventPermissionV2Replied",
    "EventAccountAddedPropertiesAccountCredentialAuthOAuthCredential",
    "EventAccountAddedPropertiesAccountCredentialAuthApiKeyCredential",
    "EventAccountAddedPropertiesAccountCredential",
    "EventAccountAddedPropertiesAccount",
    "EventAccountAddedProperties",
    "EventAccountAdded",
    "EventAccountRemovedPropertiesAccountCredentialAuthOAuthCredential",
    "EventAccountRemovedPropertiesAccountCredentialAuthApiKeyCredential",
    "EventAccountRemovedPropertiesAccountCredential",
    "EventAccountRemovedPropertiesAccount",
    "EventAccountRemovedProperties",
    "EventAccountRemoved",
    "EventAccountSwitchedProperties",
    "EventAccountSwitched",
    "EventPermissionAskedPropertiesTool",
    "EventPermissionAskedProperties",
    "EventPermissionAsked",
    "EventPermissionRepliedProperties",
    "EventPermissionReplied",
    "EventMessagePartDeltaProperties",
    "EventMessagePartDelta",
    "EventSessionDiffPropertiesDiff",
    "EventSessionDiffProperties",
    "EventSessionDiff",
    "EventSessionErrorPropertiesErrorMessageOutputLengthError",
    "EventSessionErrorPropertiesError",
    "EventSessionErrorProperties",
    "EventSessionError",
    "EventLspUpdated",
    "EventFileWatcherUpdatedProperties",
    "EventFileWatcherUpdated",
    "EventFileEditedProperties",
    "EventFileEdited",
    "EventPtyCreatedPropertiesInfo",
    "EventPtyCreatedProperties",
    "EventPtyCreated",
    "EventPtyUpdatedPropertiesInfo",
    "EventPtyUpdatedProperties",
    "EventPtyUpdated",
    "EventPtyExitedProperties",
    "EventPtyExited",
    "EventPtyDeletedProperties",
    "EventPtyDeleted",
    "EventQuestionV2AskedPropertiesQuestionsOptions",
    "EventQuestionV2AskedPropertiesQuestions",
    "EventQuestionV2AskedPropertiesTool",
    "EventQuestionV2AskedProperties",
    "EventQuestionV2Asked",
    "EventQuestionV2RepliedProperties",
    "EventQuestionV2Replied",
    "EventQuestionV2RejectedProperties",
    "EventQuestionV2Rejected",
    "EventTodoUpdatedPropertiesTodos",
    "EventTodoUpdatedProperties",
    "EventTodoUpdated",
    "EventInstallationUpdatedProperties",
    "EventInstallationUpdated",
    "EventInstallationUpdateAvailableProperties",
    "EventInstallationUpdateAvailable",
    "EventTuiPromptAppendProperties",
    "EventTuiPromptAppend",
    "EventTuiCommandExecuteProperties",
    "EventTuiCommandExecute",
    "EventTuiToastShowProperties",
    "EventTuiToastShow",
    "EventTuiSessionSelectProperties",
    "EventTuiSessionSelect",
    "EventMcpToolsChangedProperties",
    "EventMcpToolsChanged",
    "EventMcpBrowserOpenFailedProperties",
    "EventMcpBrowserOpenFailed",
    "EventQuestionAskedPropertiesQuestionsOptions",
    "EventQuestionAskedPropertiesQuestions",
    "EventQuestionAskedPropertiesTool",
    "EventQuestionAskedProperties",
    "EventQuestionAsked",
    "EventQuestionRepliedProperties",
    "EventQuestionReplied",
    "EventQuestionRejectedProperties",
    "EventQuestionRejected",
    "EventCommandExecutedProperties",
    "EventCommandExecuted",
    "EventSessionStatusPropertiesStatusIdle",
    "EventSessionStatusPropertiesStatusRetryAction",
    "EventSessionStatusPropertiesStatusRetry",
    "EventSessionStatusPropertiesStatusBusy",
    "EventSessionStatusPropertiesStatus",
    "EventSessionStatusProperties",
    "EventSessionStatus",
    "EventSessionIdleProperties",
    "EventSessionIdle",
    "EventSessionCompactedProperties",
    "EventSessionCompacted",
    "EventProjectDirectoriesUpdatedProperties",
    "EventProjectDirectoriesUpdated",
    "EventProjectUpdatedPropertiesTime",
    "EventProjectUpdatedPropertiesCommands",
    "EventProjectUpdatedPropertiesIcon",
    "EventProjectUpdatedProperties",
    "EventProjectUpdated",
    "EventVcsBranchUpdatedProperties",
    "EventVcsBranchUpdated",
    "EventWorkspaceReadyProperties",
    "EventWorkspaceReady",
    "EventWorkspaceFailedProperties",
    "EventWorkspaceFailed",
    "EventWorkspaceStatusProperties",
    "EventWorkspaceStatus",
    "EventWorktreeReadyProperties",
    "EventWorktreeReady",
    "EventWorktreeFailedProperties",
    "EventWorktreeFailed",
    "EventServerConnected",
    "EventGlobalDisposed",
    "EventServerInstanceDisposedProperties",
    "EventServerInstanceDisposed",
]


class EventPluginAddedProperties(BaseModel):
    id: str


class EventPluginAdded(BaseModel):
    id: str

    properties: EventPluginAddedProperties

    type: Literal["plugin.added"]


class EventCatalogModelUpdatedPropertiesModelApiAisdk(BaseModel):
    id: str

    package: str

    type: Literal["aisdk"]

    settings: Optional[object] = None

    url: Optional[str] = None


class EventCatalogModelUpdatedPropertiesModelApiNative(BaseModel):
    id: str

    settings: object

    type: Literal["native"]

    url: Optional[str] = None


EventCatalogModelUpdatedPropertiesModelApi: TypeAlias = Annotated[
    Union[EventCatalogModelUpdatedPropertiesModelApiAisdk, EventCatalogModelUpdatedPropertiesModelApiNative],
    PropertyInfo(discriminator="type"),
]


class EventCatalogModelUpdatedPropertiesModelCapabilities(BaseModel):
    input: List[str]

    output: List[str]

    tools: bool


class EventCatalogModelUpdatedPropertiesModelCostCache(BaseModel):
    read: float

    write: float


class EventCatalogModelUpdatedPropertiesModelCostTier(BaseModel):
    size: int

    type: Literal["context"]


class EventCatalogModelUpdatedPropertiesModelCost(BaseModel):
    cache: EventCatalogModelUpdatedPropertiesModelCostCache

    input: float

    output: float

    tier: Optional[EventCatalogModelUpdatedPropertiesModelCostTier] = None


class EventCatalogModelUpdatedPropertiesModelLimit(BaseModel):
    context: int

    output: int

    input: Optional[int] = None


class EventCatalogModelUpdatedPropertiesModelRequest(BaseModel):
    body: object

    headers: object

    variant: Optional[str] = None


class EventCatalogModelUpdatedPropertiesModelTime(BaseModel):
    released: object


class EventCatalogModelUpdatedPropertiesModelVariants(BaseModel):
    id: str

    body: object

    headers: object


class EventCatalogModelUpdatedPropertiesModel(BaseModel):
    id: str

    api: EventCatalogModelUpdatedPropertiesModelApi

    capabilities: EventCatalogModelUpdatedPropertiesModelCapabilities

    cost: List[EventCatalogModelUpdatedPropertiesModelCost]

    enabled: bool

    limit: EventCatalogModelUpdatedPropertiesModelLimit

    name: str

    provider_id: str = FieldInfo(alias="providerID")

    request: EventCatalogModelUpdatedPropertiesModelRequest

    status: Literal["alpha", "beta", "deprecated", "active"]

    time: EventCatalogModelUpdatedPropertiesModelTime

    variants: List[EventCatalogModelUpdatedPropertiesModelVariants]

    family: Optional[str] = None


class EventCatalogModelUpdatedProperties(BaseModel):
    model: EventCatalogModelUpdatedPropertiesModel


class EventCatalogModelUpdated(BaseModel):
    id: str

    properties: EventCatalogModelUpdatedProperties

    type: Literal["catalog.model.updated"]


class EventSessionCreatedProperties(BaseModel):
    info: Session

    session_id: str = FieldInfo(alias="sessionID")


class EventSessionCreated(BaseModel):
    id: str

    properties: EventSessionCreatedProperties

    type: Literal["session.created"]


class EventSessionUpdatedProperties(BaseModel):
    info: Session

    session_id: str = FieldInfo(alias="sessionID")


class EventSessionUpdated(BaseModel):
    id: str

    properties: EventSessionUpdatedProperties

    type: Literal["session.updated"]


class EventSessionDeletedProperties(BaseModel):
    info: Session

    session_id: str = FieldInfo(alias="sessionID")


class EventSessionDeleted(BaseModel):
    id: str

    properties: EventSessionDeletedProperties

    type: Literal["session.deleted"]


class EventMessageUpdatedProperties(BaseModel):
    info: Message

    session_id: str = FieldInfo(alias="sessionID")


class EventMessageUpdated(BaseModel):
    id: str

    properties: EventMessageUpdatedProperties

    type: Literal["message.updated"]


class EventMessageRemovedProperties(BaseModel):
    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")


class EventMessageRemoved(BaseModel):
    id: str

    properties: EventMessageRemovedProperties

    type: Literal["message.removed"]


class EventMessagePartUpdatedProperties(BaseModel):
    part: Part

    session_id: str = FieldInfo(alias="sessionID")

    time: float


class EventMessagePartUpdated(BaseModel):
    id: str

    properties: EventMessagePartUpdatedProperties

    type: Literal["message.part.updated"]


class EventMessagePartRemovedProperties(BaseModel):
    message_id: str = FieldInfo(alias="messageID")

    part_id: str = FieldInfo(alias="partID")

    session_id: str = FieldInfo(alias="sessionID")


class EventMessagePartRemoved(BaseModel):
    id: str

    properties: EventMessagePartRemovedProperties

    type: Literal["message.part.removed"]


class EventModelsDevRefreshed(BaseModel):
    id: str

    properties: object

    type: Literal["models-dev.refreshed"]


class EventSessionNextAgentSwitchedProperties(BaseModel):
    agent: str

    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")

    timestamp: float


class EventSessionNextAgentSwitched(BaseModel):
    id: str

    properties: EventSessionNextAgentSwitchedProperties

    type: Literal["session.next.agent.switched"]


class EventSessionNextModelSwitchedPropertiesModel(BaseModel):
    id: str

    provider_id: str = FieldInfo(alias="providerID")

    variant: Optional[str] = None


class EventSessionNextModelSwitchedProperties(BaseModel):
    message_id: str = FieldInfo(alias="messageID")

    model: EventSessionNextModelSwitchedPropertiesModel

    session_id: str = FieldInfo(alias="sessionID")

    timestamp: float


class EventSessionNextModelSwitched(BaseModel):
    id: str

    properties: EventSessionNextModelSwitchedProperties

    type: Literal["session.next.model.switched"]


class EventSessionNextMovedPropertiesLocation(BaseModel):
    directory: str

    workspace_id: Optional[str] = FieldInfo(alias="workspaceID", default=None)


class EventSessionNextMovedProperties(BaseModel):
    location: EventSessionNextMovedPropertiesLocation

    session_id: str = FieldInfo(alias="sessionID")

    timestamp: float

    subdirectory: Optional[str] = None


class EventSessionNextMoved(BaseModel):
    id: str

    properties: EventSessionNextMovedProperties

    type: Literal["session.next.moved"]


class EventSessionNextPromptedPropertiesPromptAgentsSource(BaseModel):
    end: float

    start: float

    text: str


class EventSessionNextPromptedPropertiesPromptAgents(BaseModel):
    name: str

    source: Optional[EventSessionNextPromptedPropertiesPromptAgentsSource] = None


class EventSessionNextPromptedPropertiesPromptFilesSource(BaseModel):
    end: float

    start: float

    text: str


class EventSessionNextPromptedPropertiesPromptFiles(BaseModel):
    mime: str

    uri: str

    description: Optional[str] = None

    name: Optional[str] = None

    source: Optional[EventSessionNextPromptedPropertiesPromptFilesSource] = None


class EventSessionNextPromptedPropertiesPromptReferencesSource(BaseModel):
    end: float

    start: float

    text: str


class EventSessionNextPromptedPropertiesPromptReferences(BaseModel):
    kind: Literal["local", "git", "invalid"]

    name: str

    branch: Optional[str] = None

    problem: Optional[str] = None

    repository: Optional[str] = None

    source: Optional[EventSessionNextPromptedPropertiesPromptReferencesSource] = None

    target: Optional[str] = None

    target_uri: Optional[str] = FieldInfo(alias="targetUri", default=None)

    uri: Optional[str] = None


class EventSessionNextPromptedPropertiesPrompt(BaseModel):
    text: str

    agents: Optional[List[EventSessionNextPromptedPropertiesPromptAgents]] = None

    files: Optional[List[EventSessionNextPromptedPropertiesPromptFiles]] = None

    references: Optional[List[EventSessionNextPromptedPropertiesPromptReferences]] = None


class EventSessionNextPromptedProperties(BaseModel):
    delivery: Literal["steer", "queue"]

    message_id: str = FieldInfo(alias="messageID")

    prompt: EventSessionNextPromptedPropertiesPrompt

    session_id: str = FieldInfo(alias="sessionID")

    timestamp: float


class EventSessionNextPrompted(BaseModel):
    id: str

    properties: EventSessionNextPromptedProperties

    type: Literal["session.next.prompted"]


class EventSessionNextPromptAdmittedPropertiesPromptAgentsSource(BaseModel):
    end: float

    start: float

    text: str


class EventSessionNextPromptAdmittedPropertiesPromptAgents(BaseModel):
    name: str

    source: Optional[EventSessionNextPromptAdmittedPropertiesPromptAgentsSource] = None


class EventSessionNextPromptAdmittedPropertiesPromptFilesSource(BaseModel):
    end: float

    start: float

    text: str


class EventSessionNextPromptAdmittedPropertiesPromptFiles(BaseModel):
    mime: str

    uri: str

    description: Optional[str] = None

    name: Optional[str] = None

    source: Optional[EventSessionNextPromptAdmittedPropertiesPromptFilesSource] = None


class EventSessionNextPromptAdmittedPropertiesPromptReferencesSource(BaseModel):
    end: float

    start: float

    text: str


class EventSessionNextPromptAdmittedPropertiesPromptReferences(BaseModel):
    kind: Literal["local", "git", "invalid"]

    name: str

    branch: Optional[str] = None

    problem: Optional[str] = None

    repository: Optional[str] = None

    source: Optional[EventSessionNextPromptAdmittedPropertiesPromptReferencesSource] = None

    target: Optional[str] = None

    target_uri: Optional[str] = FieldInfo(alias="targetUri", default=None)

    uri: Optional[str] = None


class EventSessionNextPromptAdmittedPropertiesPrompt(BaseModel):
    text: str

    agents: Optional[List[EventSessionNextPromptAdmittedPropertiesPromptAgents]] = None

    files: Optional[List[EventSessionNextPromptAdmittedPropertiesPromptFiles]] = None

    references: Optional[List[EventSessionNextPromptAdmittedPropertiesPromptReferences]] = None


class EventSessionNextPromptAdmittedProperties(BaseModel):
    delivery: Literal["steer", "queue"]

    message_id: str = FieldInfo(alias="messageID")

    prompt: EventSessionNextPromptAdmittedPropertiesPrompt

    session_id: str = FieldInfo(alias="sessionID")

    timestamp: float


class EventSessionNextPromptAdmitted(BaseModel):
    id: str

    properties: EventSessionNextPromptAdmittedProperties

    type: Literal["session.next.prompt.admitted"]


class EventSessionNextPromptPromotedPropertiesPromptAgentsSource(BaseModel):
    end: float

    start: float

    text: str


class EventSessionNextPromptPromotedPropertiesPromptAgents(BaseModel):
    name: str

    source: Optional[EventSessionNextPromptPromotedPropertiesPromptAgentsSource] = None


class EventSessionNextPromptPromotedPropertiesPromptFilesSource(BaseModel):
    end: float

    start: float

    text: str


class EventSessionNextPromptPromotedPropertiesPromptFiles(BaseModel):
    mime: str

    uri: str

    description: Optional[str] = None

    name: Optional[str] = None

    source: Optional[EventSessionNextPromptPromotedPropertiesPromptFilesSource] = None


class EventSessionNextPromptPromotedPropertiesPromptReferencesSource(BaseModel):
    end: float

    start: float

    text: str


class EventSessionNextPromptPromotedPropertiesPromptReferences(BaseModel):
    kind: Literal["local", "git", "invalid"]

    name: str

    branch: Optional[str] = None

    problem: Optional[str] = None

    repository: Optional[str] = None

    source: Optional[EventSessionNextPromptPromotedPropertiesPromptReferencesSource] = None

    target: Optional[str] = None

    target_uri: Optional[str] = FieldInfo(alias="targetUri", default=None)

    uri: Optional[str] = None


class EventSessionNextPromptPromotedPropertiesPrompt(BaseModel):
    text: str

    agents: Optional[List[EventSessionNextPromptPromotedPropertiesPromptAgents]] = None

    files: Optional[List[EventSessionNextPromptPromotedPropertiesPromptFiles]] = None

    references: Optional[List[EventSessionNextPromptPromotedPropertiesPromptReferences]] = None


class EventSessionNextPromptPromotedProperties(BaseModel):
    message_id: str = FieldInfo(alias="messageID")

    prompt: EventSessionNextPromptPromotedPropertiesPrompt

    session_id: str = FieldInfo(alias="sessionID")

    time_created: float = FieldInfo(alias="timeCreated")

    timestamp: float


class EventSessionNextPromptPromoted(BaseModel):
    id: str

    properties: EventSessionNextPromptPromotedProperties

    type: Literal["session.next.prompt.promoted"]


class EventSessionNextContextUpdatedProperties(BaseModel):
    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")

    text: str

    timestamp: float


class EventSessionNextContextUpdated(BaseModel):
    id: str

    properties: EventSessionNextContextUpdatedProperties

    type: Literal["session.next.context.updated"]


class EventSessionNextSyntheticProperties(BaseModel):
    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")

    text: str

    timestamp: float


class EventSessionNextSynthetic(BaseModel):
    id: str

    properties: EventSessionNextSyntheticProperties

    type: Literal["session.next.synthetic"]


class EventSessionNextShellStartedProperties(BaseModel):
    call_id: str = FieldInfo(alias="callID")

    command: str

    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")

    timestamp: float


class EventSessionNextShellStarted(BaseModel):
    id: str

    properties: EventSessionNextShellStartedProperties

    type: Literal["session.next.shell.started"]


class EventSessionNextShellEndedProperties(BaseModel):
    call_id: str = FieldInfo(alias="callID")

    output: str

    session_id: str = FieldInfo(alias="sessionID")

    timestamp: float


class EventSessionNextShellEnded(BaseModel):
    id: str

    properties: EventSessionNextShellEndedProperties

    type: Literal["session.next.shell.ended"]


class EventSessionNextStepStartedPropertiesModel(BaseModel):
    id: str

    provider_id: str = FieldInfo(alias="providerID")

    variant: Optional[str] = None


class EventSessionNextStepStartedProperties(BaseModel):
    agent: str

    assistant_message_id: str = FieldInfo(alias="assistantMessageID")

    model: EventSessionNextStepStartedPropertiesModel

    session_id: str = FieldInfo(alias="sessionID")

    timestamp: float

    snapshot: Optional[str] = None


class EventSessionNextStepStarted(BaseModel):
    id: str

    properties: EventSessionNextStepStartedProperties

    type: Literal["session.next.step.started"]


class EventSessionNextStepEndedPropertiesTokensCache(BaseModel):
    read: float

    write: float


class EventSessionNextStepEndedPropertiesTokens(BaseModel):
    cache: EventSessionNextStepEndedPropertiesTokensCache

    input: float

    output: float

    reasoning: float


class EventSessionNextStepEndedProperties(BaseModel):
    assistant_message_id: str = FieldInfo(alias="assistantMessageID")

    cost: float

    finish: str

    session_id: str = FieldInfo(alias="sessionID")

    timestamp: float

    tokens: EventSessionNextStepEndedPropertiesTokens

    snapshot: Optional[str] = None


class EventSessionNextStepEnded(BaseModel):
    id: str

    properties: EventSessionNextStepEndedProperties

    type: Literal["session.next.step.ended"]


class EventSessionNextStepFailedPropertiesError(BaseModel):
    message: str

    type: Literal["unknown"]


class EventSessionNextStepFailedProperties(BaseModel):
    assistant_message_id: str = FieldInfo(alias="assistantMessageID")

    error: EventSessionNextStepFailedPropertiesError

    session_id: str = FieldInfo(alias="sessionID")

    timestamp: float


class EventSessionNextStepFailed(BaseModel):
    id: str

    properties: EventSessionNextStepFailedProperties

    type: Literal["session.next.step.failed"]


class EventSessionNextTextStartedProperties(BaseModel):
    assistant_message_id: str = FieldInfo(alias="assistantMessageID")

    session_id: str = FieldInfo(alias="sessionID")

    text_id: str = FieldInfo(alias="textID")

    timestamp: float


class EventSessionNextTextStarted(BaseModel):
    id: str

    properties: EventSessionNextTextStartedProperties

    type: Literal["session.next.text.started"]


class EventSessionNextTextDeltaProperties(BaseModel):
    assistant_message_id: str = FieldInfo(alias="assistantMessageID")

    delta: str

    session_id: str = FieldInfo(alias="sessionID")

    text_id: str = FieldInfo(alias="textID")

    timestamp: float


class EventSessionNextTextDelta(BaseModel):
    id: str

    properties: EventSessionNextTextDeltaProperties

    type: Literal["session.next.text.delta"]


class EventSessionNextTextEndedProperties(BaseModel):
    assistant_message_id: str = FieldInfo(alias="assistantMessageID")

    session_id: str = FieldInfo(alias="sessionID")

    text: str

    text_id: str = FieldInfo(alias="textID")

    timestamp: float


class EventSessionNextTextEnded(BaseModel):
    id: str

    properties: EventSessionNextTextEndedProperties

    type: Literal["session.next.text.ended"]


class EventSessionNextReasoningStartedProperties(BaseModel):
    assistant_message_id: str = FieldInfo(alias="assistantMessageID")

    reasoning_id: str = FieldInfo(alias="reasoningID")

    session_id: str = FieldInfo(alias="sessionID")

    timestamp: float

    provider_metadata: Optional[object] = FieldInfo(alias="providerMetadata", default=None)


class EventSessionNextReasoningStarted(BaseModel):
    id: str

    properties: EventSessionNextReasoningStartedProperties

    type: Literal["session.next.reasoning.started"]


class EventSessionNextReasoningDeltaProperties(BaseModel):
    assistant_message_id: str = FieldInfo(alias="assistantMessageID")

    delta: str

    reasoning_id: str = FieldInfo(alias="reasoningID")

    session_id: str = FieldInfo(alias="sessionID")

    timestamp: float


class EventSessionNextReasoningDelta(BaseModel):
    id: str

    properties: EventSessionNextReasoningDeltaProperties

    type: Literal["session.next.reasoning.delta"]


class EventSessionNextReasoningEndedProperties(BaseModel):
    assistant_message_id: str = FieldInfo(alias="assistantMessageID")

    reasoning_id: str = FieldInfo(alias="reasoningID")

    session_id: str = FieldInfo(alias="sessionID")

    text: str

    timestamp: float

    provider_metadata: Optional[object] = FieldInfo(alias="providerMetadata", default=None)


class EventSessionNextReasoningEnded(BaseModel):
    id: str

    properties: EventSessionNextReasoningEndedProperties

    type: Literal["session.next.reasoning.ended"]


class EventSessionNextToolInputStartedProperties(BaseModel):
    assistant_message_id: str = FieldInfo(alias="assistantMessageID")

    call_id: str = FieldInfo(alias="callID")

    name: str

    session_id: str = FieldInfo(alias="sessionID")

    timestamp: float


class EventSessionNextToolInputStarted(BaseModel):
    id: str

    properties: EventSessionNextToolInputStartedProperties

    type: Literal["session.next.tool.input.started"]


class EventSessionNextToolInputDeltaProperties(BaseModel):
    assistant_message_id: str = FieldInfo(alias="assistantMessageID")

    call_id: str = FieldInfo(alias="callID")

    delta: str

    session_id: str = FieldInfo(alias="sessionID")

    timestamp: float


class EventSessionNextToolInputDelta(BaseModel):
    id: str

    properties: EventSessionNextToolInputDeltaProperties

    type: Literal["session.next.tool.input.delta"]


class EventSessionNextToolInputEndedProperties(BaseModel):
    assistant_message_id: str = FieldInfo(alias="assistantMessageID")

    call_id: str = FieldInfo(alias="callID")

    session_id: str = FieldInfo(alias="sessionID")

    text: str

    timestamp: float


class EventSessionNextToolInputEnded(BaseModel):
    id: str

    properties: EventSessionNextToolInputEndedProperties

    type: Literal["session.next.tool.input.ended"]


class EventSessionNextToolCalledPropertiesProvider(BaseModel):
    executed: bool

    metadata: Optional[object] = None


class EventSessionNextToolCalledProperties(BaseModel):
    assistant_message_id: str = FieldInfo(alias="assistantMessageID")

    call_id: str = FieldInfo(alias="callID")

    input: object

    provider: EventSessionNextToolCalledPropertiesProvider

    session_id: str = FieldInfo(alias="sessionID")

    timestamp: float

    tool: str


class EventSessionNextToolCalled(BaseModel):
    id: str

    properties: EventSessionNextToolCalledProperties

    type: Literal["session.next.tool.called"]


class EventSessionNextToolProgressPropertiesContentToolTextContent(BaseModel):
    text: str

    type: Literal["text"]


class EventSessionNextToolProgressPropertiesContentToolFileContentSourceData(BaseModel):
    data: str

    type: Literal["data"]


class EventSessionNextToolProgressPropertiesContentToolFileContentSourceUrl(BaseModel):
    type: Literal["url"]

    url: str


class EventSessionNextToolProgressPropertiesContentToolFileContentSourceFile(BaseModel):
    type: Literal["file"]

    uri: str


EventSessionNextToolProgressPropertiesContentToolFileContentSource: TypeAlias = Annotated[
    Union[
        EventSessionNextToolProgressPropertiesContentToolFileContentSourceData,
        EventSessionNextToolProgressPropertiesContentToolFileContentSourceUrl,
        EventSessionNextToolProgressPropertiesContentToolFileContentSourceFile,
    ],
    PropertyInfo(discriminator="type"),
]


class EventSessionNextToolProgressPropertiesContentToolFileContent(BaseModel):
    mime: str

    source: EventSessionNextToolProgressPropertiesContentToolFileContentSource

    type: Literal["file"]

    name: Optional[str] = None


EventSessionNextToolProgressPropertiesContent: TypeAlias = Annotated[
    Union[
        EventSessionNextToolProgressPropertiesContentToolTextContent,
        EventSessionNextToolProgressPropertiesContentToolFileContent,
    ],
    PropertyInfo(discriminator="type"),
]


class EventSessionNextToolProgressProperties(BaseModel):
    assistant_message_id: str = FieldInfo(alias="assistantMessageID")

    call_id: str = FieldInfo(alias="callID")

    content: List[EventSessionNextToolProgressPropertiesContent]

    session_id: str = FieldInfo(alias="sessionID")

    structured: object

    timestamp: float


class EventSessionNextToolProgress(BaseModel):
    id: str

    properties: EventSessionNextToolProgressProperties

    type: Literal["session.next.tool.progress"]


class EventSessionNextToolSuccessPropertiesContentToolTextContent(BaseModel):
    text: str

    type: Literal["text"]


class EventSessionNextToolSuccessPropertiesContentToolFileContentSourceData(BaseModel):
    data: str

    type: Literal["data"]


class EventSessionNextToolSuccessPropertiesContentToolFileContentSourceUrl(BaseModel):
    type: Literal["url"]

    url: str


class EventSessionNextToolSuccessPropertiesContentToolFileContentSourceFile(BaseModel):
    type: Literal["file"]

    uri: str


EventSessionNextToolSuccessPropertiesContentToolFileContentSource: TypeAlias = Annotated[
    Union[
        EventSessionNextToolSuccessPropertiesContentToolFileContentSourceData,
        EventSessionNextToolSuccessPropertiesContentToolFileContentSourceUrl,
        EventSessionNextToolSuccessPropertiesContentToolFileContentSourceFile,
    ],
    PropertyInfo(discriminator="type"),
]


class EventSessionNextToolSuccessPropertiesContentToolFileContent(BaseModel):
    mime: str

    source: EventSessionNextToolSuccessPropertiesContentToolFileContentSource

    type: Literal["file"]

    name: Optional[str] = None


EventSessionNextToolSuccessPropertiesContent: TypeAlias = Annotated[
    Union[
        EventSessionNextToolSuccessPropertiesContentToolTextContent,
        EventSessionNextToolSuccessPropertiesContentToolFileContent,
    ],
    PropertyInfo(discriminator="type"),
]


class EventSessionNextToolSuccessPropertiesProvider(BaseModel):
    executed: bool

    metadata: Optional[object] = None


class EventSessionNextToolSuccessProperties(BaseModel):
    assistant_message_id: str = FieldInfo(alias="assistantMessageID")

    call_id: str = FieldInfo(alias="callID")

    content: List[EventSessionNextToolSuccessPropertiesContent]

    provider: EventSessionNextToolSuccessPropertiesProvider

    session_id: str = FieldInfo(alias="sessionID")

    structured: object

    timestamp: float

    result: Optional[object] = None


class EventSessionNextToolSuccess(BaseModel):
    id: str

    properties: EventSessionNextToolSuccessProperties

    type: Literal["session.next.tool.success"]


class EventSessionNextToolFailedPropertiesError(BaseModel):
    message: str

    type: Literal["unknown"]


class EventSessionNextToolFailedPropertiesProvider(BaseModel):
    executed: bool

    metadata: Optional[object] = None


class EventSessionNextToolFailedProperties(BaseModel):
    assistant_message_id: str = FieldInfo(alias="assistantMessageID")

    call_id: str = FieldInfo(alias="callID")

    error: EventSessionNextToolFailedPropertiesError

    provider: EventSessionNextToolFailedPropertiesProvider

    session_id: str = FieldInfo(alias="sessionID")

    timestamp: float

    result: Optional[object] = None


class EventSessionNextToolFailed(BaseModel):
    id: str

    properties: EventSessionNextToolFailedProperties

    type: Literal["session.next.tool.failed"]


class EventSessionNextRetriedPropertiesError(BaseModel):
    is_retryable: bool = FieldInfo(alias="isRetryable")

    message: str

    metadata: Optional[object] = None

    response_body: Optional[str] = FieldInfo(alias="responseBody", default=None)

    response_headers: Optional[object] = FieldInfo(alias="responseHeaders", default=None)

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)


class EventSessionNextRetriedProperties(BaseModel):
    attempt: float

    error: EventSessionNextRetriedPropertiesError

    session_id: str = FieldInfo(alias="sessionID")

    timestamp: float


class EventSessionNextRetried(BaseModel):
    id: str

    properties: EventSessionNextRetriedProperties

    type: Literal["session.next.retried"]


class EventSessionNextCompactionStartedProperties(BaseModel):
    message_id: str = FieldInfo(alias="messageID")

    reason: Literal["auto", "manual"]

    session_id: str = FieldInfo(alias="sessionID")

    timestamp: float


class EventSessionNextCompactionStarted(BaseModel):
    id: str

    properties: EventSessionNextCompactionStartedProperties

    type: Literal["session.next.compaction.started"]


class EventSessionNextCompactionDeltaProperties(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")

    text: str

    timestamp: float


class EventSessionNextCompactionDelta(BaseModel):
    id: str

    properties: EventSessionNextCompactionDeltaProperties

    type: Literal["session.next.compaction.delta"]


class EventSessionNextCompactionEndedProperties(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")

    text: str

    timestamp: float

    include: Optional[str] = None


class EventSessionNextCompactionEnded(BaseModel):
    id: str

    properties: EventSessionNextCompactionEndedProperties

    type: Literal["session.next.compaction.ended"]


class EventPermissionV2AskedPropertiesSource(BaseModel):
    call_id: str = FieldInfo(alias="callID")

    message_id: str = FieldInfo(alias="messageID")

    type: Literal["tool"]


class EventPermissionV2AskedProperties(BaseModel):
    id: str

    action: str

    resources: List[str]

    session_id: str = FieldInfo(alias="sessionID")

    metadata: Optional[object] = None

    save: Optional[List[str]] = None

    source: Optional[EventPermissionV2AskedPropertiesSource] = None


class EventPermissionV2Asked(BaseModel):
    id: str

    properties: EventPermissionV2AskedProperties

    type: Literal["permission.v2.asked"]


class EventPermissionV2RepliedProperties(BaseModel):
    reply: Literal["once", "always", "reject"]

    request_id: str = FieldInfo(alias="requestID")

    session_id: str = FieldInfo(alias="sessionID")


class EventPermissionV2Replied(BaseModel):
    id: str

    properties: EventPermissionV2RepliedProperties

    type: Literal["permission.v2.replied"]


class EventAccountAddedPropertiesAccountCredentialAuthOAuthCredential(BaseModel):
    access: str

    expires: int

    refresh: str

    type: Literal["oauth"]


class EventAccountAddedPropertiesAccountCredentialAuthApiKeyCredential(BaseModel):
    key: str

    type: Literal["api"]

    metadata: Optional[object] = None


EventAccountAddedPropertiesAccountCredential: TypeAlias = Annotated[
    Union[
        EventAccountAddedPropertiesAccountCredentialAuthOAuthCredential,
        EventAccountAddedPropertiesAccountCredentialAuthApiKeyCredential,
    ],
    PropertyInfo(discriminator="type"),
]


class EventAccountAddedPropertiesAccount(BaseModel):
    id: str

    credential: EventAccountAddedPropertiesAccountCredential

    description: str

    service_id: str = FieldInfo(alias="serviceID")


class EventAccountAddedProperties(BaseModel):
    account: EventAccountAddedPropertiesAccount


class EventAccountAdded(BaseModel):
    id: str

    properties: EventAccountAddedProperties

    type: Literal["account.added"]


class EventAccountRemovedPropertiesAccountCredentialAuthOAuthCredential(BaseModel):
    access: str

    expires: int

    refresh: str

    type: Literal["oauth"]


class EventAccountRemovedPropertiesAccountCredentialAuthApiKeyCredential(BaseModel):
    key: str

    type: Literal["api"]

    metadata: Optional[object] = None


EventAccountRemovedPropertiesAccountCredential: TypeAlias = Annotated[
    Union[
        EventAccountRemovedPropertiesAccountCredentialAuthOAuthCredential,
        EventAccountRemovedPropertiesAccountCredentialAuthApiKeyCredential,
    ],
    PropertyInfo(discriminator="type"),
]


class EventAccountRemovedPropertiesAccount(BaseModel):
    id: str

    credential: EventAccountRemovedPropertiesAccountCredential

    description: str

    service_id: str = FieldInfo(alias="serviceID")


class EventAccountRemovedProperties(BaseModel):
    account: EventAccountRemovedPropertiesAccount


class EventAccountRemoved(BaseModel):
    id: str

    properties: EventAccountRemovedProperties

    type: Literal["account.removed"]


class EventAccountSwitchedProperties(BaseModel):
    service_id: str = FieldInfo(alias="serviceID")

    from_: Optional[str] = FieldInfo(alias="from", default=None)

    to: Optional[str] = None


class EventAccountSwitched(BaseModel):
    id: str

    properties: EventAccountSwitchedProperties

    type: Literal["account.switched"]


class EventPermissionAskedPropertiesTool(BaseModel):
    call_id: str = FieldInfo(alias="callID")

    message_id: str = FieldInfo(alias="messageID")


class EventPermissionAskedProperties(BaseModel):
    id: str

    always: List[str]

    metadata: object

    patterns: List[str]

    permission: str

    session_id: str = FieldInfo(alias="sessionID")

    tool: Optional[EventPermissionAskedPropertiesTool] = None


class EventPermissionAsked(BaseModel):
    id: str

    properties: EventPermissionAskedProperties

    type: Literal["permission.asked"]


class EventPermissionRepliedProperties(BaseModel):
    reply: Literal["once", "always", "reject"]

    request_id: str = FieldInfo(alias="requestID")

    session_id: str = FieldInfo(alias="sessionID")


class EventPermissionReplied(BaseModel):
    id: str

    properties: EventPermissionRepliedProperties

    type: Literal["permission.replied"]


class EventMessagePartDeltaProperties(BaseModel):
    delta: str

    field: str

    message_id: str = FieldInfo(alias="messageID")

    part_id: str = FieldInfo(alias="partID")

    session_id: str = FieldInfo(alias="sessionID")


class EventMessagePartDelta(BaseModel):
    id: str

    properties: EventMessagePartDeltaProperties

    type: Literal["message.part.delta"]


class EventSessionDiffPropertiesDiff(BaseModel):
    additions: float

    deletions: float

    file: Optional[str] = None

    patch: Optional[str] = None

    status: Optional[Literal["added", "deleted", "modified"]] = None


class EventSessionDiffProperties(BaseModel):
    diff: List[EventSessionDiffPropertiesDiff]

    session_id: str = FieldInfo(alias="sessionID")


class EventSessionDiff(BaseModel):
    id: str

    properties: EventSessionDiffProperties

    type: Literal["session.diff"]


class EventSessionErrorPropertiesErrorMessageOutputLengthError(BaseModel):
    data: object

    name: Literal["MessageOutputLengthError"]


EventSessionErrorPropertiesError: TypeAlias = Annotated[
    Union[
        ProviderAuthError,
        UnknownError,
        EventSessionErrorPropertiesErrorMessageOutputLengthError,
        MessageAbortedError,
        StructuredOutputError,
        ContextOverflowError,
        APIError,
    ],
    PropertyInfo(discriminator="name"),
]


class EventSessionErrorProperties(BaseModel):
    error: Optional[EventSessionErrorPropertiesError] = None

    session_id: Optional[str] = FieldInfo(alias="sessionID", default=None)


class EventSessionError(BaseModel):
    id: str

    properties: EventSessionErrorProperties

    type: Literal["session.error"]


class EventLspUpdated(BaseModel):
    id: str

    properties: object

    type: Literal["lsp.updated"]


class EventFileWatcherUpdatedProperties(BaseModel):
    event: Literal["add", "change", "unlink"]

    file: str


class EventFileWatcherUpdated(BaseModel):
    id: str

    properties: EventFileWatcherUpdatedProperties

    type: Literal["file.watcher.updated"]


class EventFileEditedProperties(BaseModel):
    file: str


class EventFileEdited(BaseModel):
    id: str

    properties: EventFileEditedProperties

    type: Literal["file.edited"]


class EventPtyCreatedPropertiesInfo(BaseModel):
    id: str

    args: List[str]

    command: str

    cwd: str

    pid: int

    status: Literal["running", "exited"]

    title: str


class EventPtyCreatedProperties(BaseModel):
    info: EventPtyCreatedPropertiesInfo


class EventPtyCreated(BaseModel):
    id: str

    properties: EventPtyCreatedProperties

    type: Literal["pty.created"]


class EventPtyUpdatedPropertiesInfo(BaseModel):
    id: str

    args: List[str]

    command: str

    cwd: str

    pid: int

    status: Literal["running", "exited"]

    title: str


class EventPtyUpdatedProperties(BaseModel):
    info: EventPtyUpdatedPropertiesInfo


class EventPtyUpdated(BaseModel):
    id: str

    properties: EventPtyUpdatedProperties

    type: Literal["pty.updated"]


class EventPtyExitedProperties(BaseModel):
    id: str

    exit_code: int = FieldInfo(alias="exitCode")


class EventPtyExited(BaseModel):
    id: str

    properties: EventPtyExitedProperties

    type: Literal["pty.exited"]


class EventPtyDeletedProperties(BaseModel):
    id: str


class EventPtyDeleted(BaseModel):
    id: str

    properties: EventPtyDeletedProperties

    type: Literal["pty.deleted"]


class EventQuestionV2AskedPropertiesQuestionsOptions(BaseModel):
    description: str

    label: str


class EventQuestionV2AskedPropertiesQuestions(BaseModel):
    header: str

    options: List[EventQuestionV2AskedPropertiesQuestionsOptions]

    question: str

    custom: Optional[bool] = None

    multiple: Optional[bool] = None


class EventQuestionV2AskedPropertiesTool(BaseModel):
    call_id: str = FieldInfo(alias="callID")

    message_id: str = FieldInfo(alias="messageID")


class EventQuestionV2AskedProperties(BaseModel):
    id: str

    questions: List[EventQuestionV2AskedPropertiesQuestions]

    session_id: str = FieldInfo(alias="sessionID")

    tool: Optional[EventQuestionV2AskedPropertiesTool] = None


class EventQuestionV2Asked(BaseModel):
    id: str

    properties: EventQuestionV2AskedProperties

    type: Literal["question.v2.asked"]


class EventQuestionV2RepliedProperties(BaseModel):
    answers: List[List[str]]

    request_id: str = FieldInfo(alias="requestID")

    session_id: str = FieldInfo(alias="sessionID")


class EventQuestionV2Replied(BaseModel):
    id: str

    properties: EventQuestionV2RepliedProperties

    type: Literal["question.v2.replied"]


class EventQuestionV2RejectedProperties(BaseModel):
    request_id: str = FieldInfo(alias="requestID")

    session_id: str = FieldInfo(alias="sessionID")


class EventQuestionV2Rejected(BaseModel):
    id: str

    properties: EventQuestionV2RejectedProperties

    type: Literal["question.v2.rejected"]


class EventTodoUpdatedPropertiesTodos(BaseModel):
    content: str

    priority: str

    status: str


class EventTodoUpdatedProperties(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")

    todos: List[EventTodoUpdatedPropertiesTodos]


class EventTodoUpdated(BaseModel):
    id: str

    properties: EventTodoUpdatedProperties

    type: Literal["todo.updated"]


class EventInstallationUpdatedProperties(BaseModel):
    version: str


class EventInstallationUpdated(BaseModel):
    id: str

    properties: EventInstallationUpdatedProperties

    type: Literal["installation.updated"]


class EventInstallationUpdateAvailableProperties(BaseModel):
    version: str


class EventInstallationUpdateAvailable(BaseModel):
    id: str

    properties: EventInstallationUpdateAvailableProperties

    type: Literal["installation.update-available"]


class EventTuiPromptAppendProperties(BaseModel):
    text: str


class EventTuiPromptAppend(BaseModel):
    id: str

    properties: EventTuiPromptAppendProperties

    type: Literal["tui.prompt.append"]


class EventTuiCommandExecuteProperties(BaseModel):
    command: str


class EventTuiCommandExecute(BaseModel):
    id: str

    properties: EventTuiCommandExecuteProperties

    type: Literal["tui.command.execute"]


class EventTuiToastShowProperties(BaseModel):
    message: str

    variant: Literal["info", "success", "warning", "error"]

    duration: Optional[int] = None

    title: Optional[str] = None


class EventTuiToastShow(BaseModel):
    id: str

    properties: EventTuiToastShowProperties

    type: Literal["tui.toast.show"]


class EventTuiSessionSelectProperties(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")


class EventTuiSessionSelect(BaseModel):
    id: str

    properties: EventTuiSessionSelectProperties

    type: Literal["tui.session.select"]


class EventMcpToolsChangedProperties(BaseModel):
    server: str


class EventMcpToolsChanged(BaseModel):
    id: str

    properties: EventMcpToolsChangedProperties

    type: Literal["mcp.tools.changed"]


class EventMcpBrowserOpenFailedProperties(BaseModel):
    mcp_name: str = FieldInfo(alias="mcpName")

    url: str


class EventMcpBrowserOpenFailed(BaseModel):
    id: str

    properties: EventMcpBrowserOpenFailedProperties

    type: Literal["mcp.browser.open.failed"]


class EventQuestionAskedPropertiesQuestionsOptions(BaseModel):
    description: str

    label: str


class EventQuestionAskedPropertiesQuestions(BaseModel):
    header: str

    options: List[EventQuestionAskedPropertiesQuestionsOptions]

    question: str

    custom: Optional[bool] = None

    multiple: Optional[bool] = None


class EventQuestionAskedPropertiesTool(BaseModel):
    call_id: str = FieldInfo(alias="callID")

    message_id: str = FieldInfo(alias="messageID")


class EventQuestionAskedProperties(BaseModel):
    id: str

    questions: List[EventQuestionAskedPropertiesQuestions]

    session_id: str = FieldInfo(alias="sessionID")

    tool: Optional[EventQuestionAskedPropertiesTool] = None


class EventQuestionAsked(BaseModel):
    id: str

    properties: EventQuestionAskedProperties

    type: Literal["question.asked"]


class EventQuestionRepliedProperties(BaseModel):
    answers: List[List[str]]

    request_id: str = FieldInfo(alias="requestID")

    session_id: str = FieldInfo(alias="sessionID")


class EventQuestionReplied(BaseModel):
    id: str

    properties: EventQuestionRepliedProperties

    type: Literal["question.replied"]


class EventQuestionRejectedProperties(BaseModel):
    request_id: str = FieldInfo(alias="requestID")

    session_id: str = FieldInfo(alias="sessionID")


class EventQuestionRejected(BaseModel):
    id: str

    properties: EventQuestionRejectedProperties

    type: Literal["question.rejected"]


class EventCommandExecutedProperties(BaseModel):
    arguments: str

    message_id: str = FieldInfo(alias="messageID")

    name: str

    session_id: str = FieldInfo(alias="sessionID")


class EventCommandExecuted(BaseModel):
    id: str

    properties: EventCommandExecutedProperties

    type: Literal["command.executed"]


class EventSessionStatusPropertiesStatusIdle(BaseModel):
    type: Literal["idle"]


class EventSessionStatusPropertiesStatusRetryAction(BaseModel):
    label: str

    message: str

    provider: str

    reason: str

    title: str

    link: Optional[str] = None


class EventSessionStatusPropertiesStatusRetry(BaseModel):
    attempt: int

    message: str

    next: int

    type: Literal["retry"]

    action: Optional[EventSessionStatusPropertiesStatusRetryAction] = None


class EventSessionStatusPropertiesStatusBusy(BaseModel):
    type: Literal["busy"]


EventSessionStatusPropertiesStatus: TypeAlias = Annotated[
    Union[
        EventSessionStatusPropertiesStatusIdle,
        EventSessionStatusPropertiesStatusRetry,
        EventSessionStatusPropertiesStatusBusy,
    ],
    PropertyInfo(discriminator="type"),
]


class EventSessionStatusProperties(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")

    status: EventSessionStatusPropertiesStatus


class EventSessionStatus(BaseModel):
    id: str

    properties: EventSessionStatusProperties

    type: Literal["session.status"]


class EventSessionIdleProperties(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")


class EventSessionIdle(BaseModel):
    id: str

    properties: EventSessionIdleProperties

    type: Literal["session.idle"]


class EventSessionCompactedProperties(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")


class EventSessionCompacted(BaseModel):
    id: str

    properties: EventSessionCompactedProperties

    type: Literal["session.compacted"]


class EventProjectDirectoriesUpdatedProperties(BaseModel):
    project_id: str = FieldInfo(alias="projectID")


class EventProjectDirectoriesUpdated(BaseModel):
    id: str

    properties: EventProjectDirectoriesUpdatedProperties

    type: Literal["project.directories.updated"]


class EventProjectUpdatedPropertiesTime(BaseModel):
    created: int

    updated: int

    initialized: Optional[int] = None


class EventProjectUpdatedPropertiesCommands(BaseModel):
    start: Optional[str] = None


class EventProjectUpdatedPropertiesIcon(BaseModel):
    color: Optional[str] = None

    override: Optional[str] = None

    url: Optional[str] = None


class EventProjectUpdatedProperties(BaseModel):
    id: str

    sandboxes: List[str]

    time: EventProjectUpdatedPropertiesTime

    worktree: str

    commands: Optional[EventProjectUpdatedPropertiesCommands] = None

    icon: Optional[EventProjectUpdatedPropertiesIcon] = None

    name: Optional[str] = None

    vcs: Optional[Literal["git"]] = None


class EventProjectUpdated(BaseModel):
    id: str

    properties: EventProjectUpdatedProperties

    type: Literal["project.updated"]


class EventVcsBranchUpdatedProperties(BaseModel):
    branch: Optional[str] = None


class EventVcsBranchUpdated(BaseModel):
    id: str

    properties: EventVcsBranchUpdatedProperties

    type: Literal["vcs.branch.updated"]


class EventWorkspaceReadyProperties(BaseModel):
    name: str


class EventWorkspaceReady(BaseModel):
    id: str

    properties: EventWorkspaceReadyProperties

    type: Literal["workspace.ready"]


class EventWorkspaceFailedProperties(BaseModel):
    message: str


class EventWorkspaceFailed(BaseModel):
    id: str

    properties: EventWorkspaceFailedProperties

    type: Literal["workspace.failed"]


class EventWorkspaceStatusProperties(BaseModel):
    status: Literal["connected", "connecting", "disconnected", "error"]

    workspace_id: str = FieldInfo(alias="workspaceID")


class EventWorkspaceStatus(BaseModel):
    id: str

    properties: EventWorkspaceStatusProperties

    type: Literal["workspace.status"]


class EventWorktreeReadyProperties(BaseModel):
    name: str

    branch: Optional[str] = None


class EventWorktreeReady(BaseModel):
    id: str

    properties: EventWorktreeReadyProperties

    type: Literal["worktree.ready"]


class EventWorktreeFailedProperties(BaseModel):
    message: str


class EventWorktreeFailed(BaseModel):
    id: str

    properties: EventWorktreeFailedProperties

    type: Literal["worktree.failed"]


class EventServerConnected(BaseModel):
    id: str

    properties: object

    type: Literal["server.connected"]


class EventGlobalDisposed(BaseModel):
    id: str

    properties: object

    type: Literal["global.disposed"]


class EventServerInstanceDisposedProperties(BaseModel):
    directory: str


class EventServerInstanceDisposed(BaseModel):
    id: str

    properties: EventServerInstanceDisposedProperties

    type: Literal["server.instance.disposed"]


class EventUnknown(BaseModel):
    """Permissive fallback for event `type` values not yet enumerated by this SDK.

    The server's event union has grown well beyond the variants modeled here
    (full enumeration is tracked separately). Rather than raising when an
    unrecognized `type` is encountered, unmatched events deserialize into this
    open-ended model so `client.event.list()` keeps working as the server adds
    new event kinds.
    """

    type: str

    properties: Optional[object] = None


# Note on ordering: `EventUnknown` is intentionally listed *first*, not last.
#
# `_models.construct_type()` (the non-strict path used by default response
# parsing) resolves a `PropertyInfo(discriminator=...)` union in two steps:
#   1. If the discriminator value is present in the precomputed
#      `{literal value: variant type}` mapping, that exact variant is
#      constructed directly -- this happens regardless of the union's
#      ordering, so every known `type` literal below is still matched
#      correctly no matter where `EventUnknown` sits.
#   2. Otherwise (unknown/unmapped discriminator value) it falls back to
#      `for variant in args: try construct_type(...) except: continue` and
#      returns the *first* variant that doesn't raise. Because `BaseModel`
#      variants are built via the SDK's overridden `.construct()`, which
#      never validates and therefore never raises, this loop always "succeeds"
#      on the first variant tried -- so whichever variant is listed first
#      is what unknown events actually resolve to.
#
# `EventUnknown`'s own `type` field is a plain `str` (not a `Literal`), so it
# is never added to the discriminator mapping itself -- it only ever gets
# reached through the unmatched-value fallback path above, and being first
# guarantees it -- rather than an arbitrary known variant -- is what's chosen.
EventListResponse: TypeAlias = Annotated[
    Union[
        EventUnknown,
        EventPluginAdded,
        EventCatalogModelUpdated,
        EventSessionCreated,
        EventSessionUpdated,
        EventSessionDeleted,
        EventMessageUpdated,
        EventMessageRemoved,
        EventMessagePartUpdated,
        EventMessagePartRemoved,
        EventModelsDevRefreshed,
        EventSessionNextAgentSwitched,
        EventSessionNextModelSwitched,
        EventSessionNextMoved,
        EventSessionNextPrompted,
        EventSessionNextPromptAdmitted,
        EventSessionNextPromptPromoted,
        EventSessionNextContextUpdated,
        EventSessionNextSynthetic,
        EventSessionNextShellStarted,
        EventSessionNextShellEnded,
        EventSessionNextStepStarted,
        EventSessionNextStepEnded,
        EventSessionNextStepFailed,
        EventSessionNextTextStarted,
        EventSessionNextTextDelta,
        EventSessionNextTextEnded,
        EventSessionNextReasoningStarted,
        EventSessionNextReasoningDelta,
        EventSessionNextReasoningEnded,
        EventSessionNextToolInputStarted,
        EventSessionNextToolInputDelta,
        EventSessionNextToolInputEnded,
        EventSessionNextToolCalled,
        EventSessionNextToolProgress,
        EventSessionNextToolSuccess,
        EventSessionNextToolFailed,
        EventSessionNextRetried,
        EventSessionNextCompactionStarted,
        EventSessionNextCompactionDelta,
        EventSessionNextCompactionEnded,
        EventPermissionV2Asked,
        EventPermissionV2Replied,
        EventAccountAdded,
        EventAccountRemoved,
        EventAccountSwitched,
        EventPermissionAsked,
        EventPermissionReplied,
        EventMessagePartDelta,
        EventSessionDiff,
        EventSessionError,
        EventLspUpdated,
        EventFileWatcherUpdated,
        EventFileEdited,
        EventPtyCreated,
        EventPtyUpdated,
        EventPtyExited,
        EventPtyDeleted,
        EventQuestionV2Asked,
        EventQuestionV2Replied,
        EventQuestionV2Rejected,
        EventTodoUpdated,
        EventInstallationUpdated,
        EventInstallationUpdateAvailable,
        EventTuiPromptAppend,
        EventTuiCommandExecute,
        EventTuiToastShow,
        EventTuiSessionSelect,
        EventMcpToolsChanged,
        EventMcpBrowserOpenFailed,
        EventQuestionAsked,
        EventQuestionReplied,
        EventQuestionRejected,
        EventCommandExecuted,
        EventSessionStatus,
        EventSessionIdle,
        EventSessionCompacted,
        EventProjectDirectoriesUpdated,
        EventProjectUpdated,
        EventVcsBranchUpdated,
        EventWorkspaceReady,
        EventWorkspaceFailed,
        EventWorkspaceStatus,
        EventWorktreeReady,
        EventWorktreeFailed,
        EventServerConnected,
        EventGlobalDisposed,
        EventServerInstanceDisposed,
    ],
    PropertyInfo(discriminator="type"),
]
