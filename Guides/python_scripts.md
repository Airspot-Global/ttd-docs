# Python Scripts

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/PythonScripts
- Category: Guides

---

# Python Scripts

To facilitate and illustrate the campaign upgrade, create, and other workflows in Kokai, we've provided a comprehensive collection of Python scripts for each API. These scripts are for an ever growing quickstart that focuses on the core functions in Kokai. The following sections list the available scripts grouped by API, sorted alphabetically, and provides links to relevant user guides in the Partner Portal for guidance on implementation details and requirements.

Here's what you need to know about our Python scripts:

*   You can access the latest version of our [Python Scripts](https://github.com/thetradedesk/Platform/tree/main/Python) on GitHub.
*   Some scripts require you to fill-in-the-blank for placeholder values.
*   Scripts have a _REST_ or _GQL_ suffix to denote which API is supported.
*   Scripts with no suffix require the usage of both REST and GraphQL.
*   Scripts use a prefix to denote the type of operation, such as _Create_, _Get_, _Clone_, and so on.
*   Files are organized alphabetically and grouped by area, such as campaign, budgets, cloning, and more.

## 

Git Directory[](#git)

The following table lists the available directories on Github and links to user guides, sorted alphabetically.

| Directory | Description | User Guide |
| [Campaign](https://github.com/thetradedesk/Platform/tree/main/Python/Campaign) | Create and manage campaigns for Kokai using GraphQL or REST. | [Campaigns](/v3/portal/api/doc/Campaigns) |
| [Delta](https://github.com/thetradedesk/Platform/tree/main/Python/Delta) | Track periodic metadata-level changes using GraphQL or REST. | [Platform Synchronization](/v3/portal/api/doc/PlatformSynchronization) |
| [Report](https://github.com/thetradedesk/Platform/tree/main/Python/Report) | Download and query different kinds of reports using GraphQL. | [Reports](/v3/portal/reds/doc/DimensionSpecificReports) (More coming soon) |
| [Seed](https://github.com/thetradedesk/Platform/tree/main/Python/Seed) | Create an ideal audience to target your campaigns using GraphQL. | [Seeds](/v3/portal/api/doc/Seed) |

## 

Campaign Scripts[](#campaign)

Learn how to create and update campaigns for Kokai using GraphQL or REST. For details on which scripts to use, see [Campaign Creation Workflows](/v3/portal/api/doc/CampaignCreateWorkflows).

### 

GraphQL API[](#gql)

Create campaigns in Kokai with the GraphQL API, through these fill-in-the-blank GQL Python scripts.

The following table lists the available scripts for GraphQL and user guides, sorted alphabetically.

| Script | Description | User Guide |
| [CloneCampaignGQL.py](https://github.com/thetradedesk/Platform/blob/main/Python/Campaign/Cloning/CloneCampaignGQL.py) | Create one or more Kokai copies of an existing campaign using GraphQL. | [Clone Campaigns with the GraphQL API](/v3/portal/api/doc/CampaignCloning#gql) |
| [CreateCampaignWorkflowGQL.py](https://github.com/thetradedesk/Platform/blob/main/Python/Campaign/Creating/CreateCampaignWorkflowGQL.py) | Create a Kokai campaign using GraphQL. | [Campaign Creation Workflow with GraphQL](/v3/portal/api/doc/CampaignCreateGQL) |
| [CreateCampaignsBulkGQL](https://github.com/thetradedesk/Platform/blob/main/Python/Campaign/Creating/CreateCampaignsBulkGQL.py) | Create multiple Kokai campaigns in a single request using GraphQL. | [GraphQL Bulk Operations](/v3/portal/api/doc/GqlBulkOperations) |
| [GetCampaignBudgetGQL.py](https://github.com/thetradedesk/Platform/blob/main/Python/Campaign/Budgets/GetCampaignBudgetGQL.py) | Retrieve campaign budget settings using GraphQL. | [Budget Allocation](/v3/portal/api/doc/CampaignBudgets) |
| [GetCampaignGQL.py](https://github.com/thetradedesk/Platform/blob/main/Python/Campaign/Querying/GetCampaignGQL.py) | Retrieve campaign information using GraphQL. | [GraphQL Campaign Query Examples](/v3/portal/api/doc/CampaignQueryExamplesGQL) |

### 

REST API[](#rest)

Create campaigns in Kokai with the REST API, through these fill-in-the-blank REST Python scripts.

The following table lists the available scripts for REST and user guides, sorted alphabetically.

| Script | Description | User Guide |
| [CloneCampaignREST.py](https://github.com/thetradedesk/Platform/blob/main/Python/Campaign/Cloning/CloneCampaignREST.py) | Create a Kokai campaign copy of an existing campaign using REST. | [Clone a Campaign with the REST API](/v3/portal/api/doc/CampaignCloning#rest) |
| [CreateCampaignWorkflowREST.py](https://github.com/thetradedesk/Platform/blob/main/Python/Campaign/Creating/CreateCampaignWorkflowREST.py) | Create a Kokai campaign using REST. | [Campaign Creation Workflow with REST](/v3/portal/api/doc/CampaignCreateREST) |
| [GetCampaignREST.py](https://github.com/thetradedesk/Platform/blob/main/Python/Campaign/Querying/GetCampaignREST.py) | Retrieve campaign information using REST. | [Campaign REST Endpoints](/v3/portal/api/area/Campaign) |

### 

Solimar-to-Kokai Upgrade[](#upgrade)

Upgrade campaigns and/or their budgets to be fully compatible with Kokai using both GraphQL and REST.

> **IMPORTANT**: The following scripts are listed in alphabetical order. To determine which scripts must be run, see [Upgrade Solimar Campaigns to Kokai](/v3/portal/api/doc/KokaiCampaignUpgrade).

The following table lists the available scripts and user guides.

| Script | Description | User Guide |
| [UpdateCampaignBudgetWorkflow.py](https://github.com/thetradedesk/Platform/blob/main/Python/Campaign/Budgets/UpdateCampaignBudgetWorkflow.py) | Check the campaign version (Kokai or Solimar) and update its budget accordingly, using REST and GraphQL. | [Budget Allocation](/v3/portal/api/doc/CampaignBudgets) |
| [UpgradeBudgetSettingsToKokaiGQL.py](https://github.com/thetradedesk/Platform/blob/main/Python/Campaign/Budgets/UpgradeBudgetSettingsToKokaiGQL.py) | Upgrade a campaign's Solimar budget to Kokai using GraphQL. | [Budget Allocation](/v3/portal/api/doc/CampaignBudgets) |
| [UpgradeCampaignToKokaiGQL.py](https://github.com/thetradedesk/Platform/blob/main/Python/Campaign/Upgrading/UpgradeCampaignToKokaiGQL.py) | Upgrade a Solimar campaign to Kokai using GraphQL. | [Upgrade Solimar Campaigns to Kokai](/v3/portal/api/doc/KokaiCampaignUpgrade) |

## 

Data Scripts[](#data)

> **NOTE**: For samples on targeting data and rate information, see [Data Insights](/v3/portal/data/doc/DataInsights).

Search through your data and audiences with scripts using GraphQL.

### 

First-Party Data[](#fpd)

The following table lists the available scripts for GraphQL and user guides, sorted alphabetically.

| Script | Description | User Guide |
| [GetAdvertiserFirstPartyDataGQL.py](https://github.com/thetradedesk/Platform/blob/main/Python/FirstPartyData/GetAdvertiserFirstPartyDataGQL.py) | Retrieve all first-party data elements for an advertiser. | [Audiences](/v3/portal/api/doc/Audience#data-elements-1p-lookup-tasks) |
| [GetPartnerFirstPartyDataGQL.py](https://github.com/thetradedesk/Platform/blob/main/Python/FirstPartyData/GetPartnerFirstPartyDataGQL.py) | Retrieve first-party data from all advertisers under a partner. | N/A |

### 

Third-Party Data[](#tpd)

The following table lists the available scripts for GraphQL and user guides, sorted alphabetically.

| Script | Description | User Guide |
| [GetAllThirdPartyDataForPartnerGQL.py](https://github.com/thetradedesk/Platform/blob/main/Python/ThirdPartyData/GetAllThirdPartyDataForPartnerGQL.py) | Retrieve all the third-party data elements of an audience. | [Audiences](/v3/portal/api/doc/Audience#lookup-3p-data-elements-lookup-tasks) |