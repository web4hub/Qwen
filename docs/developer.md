# Developer Connect API

Connect third-party source code management to Google

- [REST Resource: v1.projects.locations](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest#v1.projects.locations)
- [REST Resource: v1.projects.locations.accountConnectors](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest#v1.projects.locations.accountConnectors)
- [REST Resource: v1.projects.locations.accountConnectors.users](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest#v1.projects.locations.accountConnectors.users)
- [REST Resource: v1.projects.locations.connections](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest#v1.projects.locations.connections)
- [REST Resource: v1.projects.locations.connections.gitRepositoryLinks](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest#v1.projects.locations.connections.gitRepositoryLinks)
- [REST Resource: v1.projects.locations.insightsConfigs](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest#v1.projects.locations.insightsConfigs)
- [REST Resource: v1.projects.locations.insightsConfigs.deploymentEvents](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest#v1.projects.locations.insightsConfigs.deploymentEvents)
- [REST Resource: v1.projects.locations.operations](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest#v1.projects.locations.operations)

## Service: developerconnect.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

- <https://developerconnect.googleapis.com/$discovery/rest?version=v1>

### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

- `https://developerconnect.googleapis.com`

## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations)

| Methods ||
|---|---|
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations/get` | `GET /v1/{name=projects/*/locations/*}` Gets information about a location. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations/list` | `GET /v1/{name=projects/*}/locations` Lists information about the supported locations for this service. |

## REST Resource: [v1.projects.locations.accountConnectors](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors)

| Methods ||
|---|---|
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors/create` | `POST /v1/{parent=projects/*/locations/*}/accountConnectors` Creates a new AccountConnector in a given project and location. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors/delete` | `DELETE /v1/{name=projects/*/locations/*/accountConnectors/*}` Deletes a single AccountConnector. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors/get` | `GET /v1/{name=projects/*/locations/*/accountConnectors/*}` Gets details of a single AccountConnector. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors/list` | `GET /v1/{parent=projects/*/locations/*}/accountConnectors` Lists AccountConnectors in a given project and location. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors/patch` | `PATCH /v1/{accountConnector.name=projects/*/locations/*/accountConnectors/*}` Updates the parameters of a single AccountConnector. |

## REST Resource: [v1.projects.locations.accountConnectors.users](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors.users)

| Methods ||
|---|---|
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors.users/delete` | `DELETE /v1/{name=projects/*/locations/*/accountConnectors/*/users/*}` Deletes a single User. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors.users/deleteSelf` | `DELETE /v1/{name=projects/*/locations/*/accountConnectors/*}/users:deleteSelf` Delete the User based on the user credentials. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors.users/fetchAccessToken` | `POST /v1/{accountConnector=projects/*/locations/*/accountConnectors/*}/users:fetchAccessToken` Fetches OAuth access token based on end user credentials. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors.users/fetchSelf` | `GET /v1/{name=projects/*/locations/*/accountConnectors/*}/users:fetchSelf` Fetch the User based on the user credentials. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors.users/finishOAuthFlow` | `GET /v1/{accountConnector=projects/*/locations/*/accountConnectors/*}/users:finishOAuthFlow` Finishes OAuth flow for an account connector. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors.users/list` | `GET /v1/{parent=projects/*/locations/*/accountConnectors/*}/users` Lists Users in a given project, location, and account_connector. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors.users/startOAuthFlow` | `GET /v1/{accountConnector=projects/*/locations/*/accountConnectors/*}/users:startOAuthFlow` Starts OAuth flow for an account connector. |

## REST Resource: [v1.projects.locations.connections](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections)

| Methods ||
|---|---|
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections/create` | `POST /v1/{parent=projects/*/locations/*}/connections` Creates a new Connection in a given project and location. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections/delete` | `DELETE /v1/{name=projects/*/locations/*/connections/*}` Deletes a single Connection. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections/fetchGitHubInstallations` | `GET /v1/{connection=projects/*/locations/*/connections/*}:fetchGitHubInstallations` FetchGitHubInstallations returns the list of GitHub Installations that are available to be added to a Connection. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections/fetchLinkableGitRepositories` | `GET /v1/{connection=projects/*/locations/*/connections/*}:fetchLinkableGitRepositories` FetchLinkableGitRepositories returns a list of git repositories from an SCM that are available to be added to a Connection. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections/get` | `GET /v1/{name=projects/*/locations/*/connections/*}` Gets details of a single Connection. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections/list` | `GET /v1/{parent=projects/*/locations/*}/connections` Lists Connections in a given project and location. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections/patch` | `PATCH /v1/{connection.name=projects/*/locations/*/connections/*}` Updates the parameters of a single Connection. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections/processGitHubEnterpriseWebhook` | `POST /v1/{parent=projects/*/locations/*}/connections:processGitHubEnterpriseWebhook` ProcessGitHubEnterpriseWebhook is called by the external GitHub Enterprise instances for notifying events. |

## REST Resource: [v1.projects.locations.connections.gitRepositoryLinks](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks)

| Methods ||
|---|---|
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/create` | `POST /v1/{parent=projects/*/locations/*/connections/*}/gitRepositoryLinks` Creates a GitRepositoryLink. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/delete` | `DELETE /v1/{name=projects/*/locations/*/connections/*/gitRepositoryLinks/*}` Deletes a single GitRepositoryLink. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/fetchGitRefs` | `GET /v1/{gitRepositoryLink=projects/*/locations/*/connections/*/gitRepositoryLinks/*}:fetchGitRefs` Fetch the list of branches or tags for a given repository. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/fetchReadToken` | `POST /v1/{gitRepositoryLink=projects/*/locations/*/connections/*/gitRepositoryLinks/*}:fetchReadToken` Fetches read token of a given gitRepositoryLink. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/fetchReadWriteToken` | `POST /v1/{gitRepositoryLink=projects/*/locations/*/connections/*/gitRepositoryLinks/*}:fetchReadWriteToken` Fetches read/write token of a given gitRepositoryLink. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/get` | `GET /v1/{name=projects/*/locations/*/connections/*/gitRepositoryLinks/*}` Gets details of a single GitRepositoryLink. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/list` | `GET /v1/{parent=projects/*/locations/*/connections/*}/gitRepositoryLinks` Lists GitRepositoryLinks in a given project, location, and connection. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/processBitbucketCloudWebhook` | `POST /v1/{name=projects/*/locations/*/connections/*/gitRepositoryLinks/*}:processBitbucketCloudWebhook` ProcessBitbucketCloudWebhook is called by the external Bitbucket Cloud instances for notifying events. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/processBitbucketDataCenterWebhook` | `POST /v1/{name=projects/*/locations/*/connections/*/gitRepositoryLinks/*}:processBitbucketDataCenterWebhook` ProcessBitbucketDataCenterWebhook is called by the external Bitbucket Data Center instances for notifying events. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/processGitLabEnterpriseWebhook` | `POST /v1/{name=projects/*/locations/*/connections/*/gitRepositoryLinks/*}:processGitLabEnterpriseWebhook` ProcessGitLabEnterpriseWebhook is called by the external GitLab Enterprise instances for notifying events. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/processGitLabWebhook` | `POST /v1/{name=projects/*/locations/*/connections/*/gitRepositoryLinks/*}:processGitLabWebhook` ProcessGitLabWebhook is called by the GitLab.com for notifying events. |

## REST Resource: [v1.projects.locations.insightsConfigs](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs)

| Methods ||
|---|---|
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs/create` | `POST /v1/{parent=projects/*/locations/*}/insightsConfigs` Creates a new InsightsConfig in a given project and location. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs/delete` | `DELETE /v1/{name=projects/*/locations/*/insightsConfigs/*}` Deletes a single Insight. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs/get` | `GET /v1/{name=projects/*/locations/*/insightsConfigs/*}` Gets details of a single Insight. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs/list` | `GET /v1/{parent=projects/*/locations/*}/insightsConfigs` Lists InsightsConfigs in a given project and location. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs/patch` | `PATCH /v1/{insightsConfig.name=projects/*/locations/*/insightsConfigs/*}` Updates the parameters of a single InsightsConfig. |

## REST Resource: [v1.projects.locations.insightsConfigs.deploymentEvents](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs.deploymentEvents)

| Methods ||
|---|---|
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs.deploymentEvents/get` | `GET /v1/{name=projects/*/locations/*/insightsConfigs/*/deploymentEvents/*}` Gets a single Deployment Event. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs.deploymentEvents/list` | `GET /v1/{parent=projects/*/locations/*/insightsConfigs/*}/deploymentEvents` Lists Deployment Events in a given insights config. |

## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.operations)

| Methods ||
|---|---|
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.operations/cancel` | `POST /v1/{name=projects/*/locations/*/operations/*}:cancel` Starts asynchronous cancellation on a long-running operation. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.operations/delete` | `DELETE /v1/{name=projects/*/locations/*/operations/*}` Deletes a long-running operation. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.operations/get` | `GET /v1/{name=projects/*/locations/*/operations/*}` Gets the latest state of a long-running operation. |
| `https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.operations/list` | `GET /v1/{name=projects/*/locations/*}/operations` Lists operations that match the specified filter in the request. |
