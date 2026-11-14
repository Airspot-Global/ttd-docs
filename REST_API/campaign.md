# Campaign

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Campaign
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Campaign (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### GraphQL campaignCreate Mutation

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/campaign-create

Create a new campaign.

### GraphQL campaign Query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/campaign

Get an existing campaign by ID.

### GraphQL campaigns Query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/campaigns

Get existing campaigns.

### GraphQL campaignUpdate Mutation

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/campaign-update

Update a campaign.

### GraphQL campaignBudgetSettingsUpdate Mutation

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/campaign-budget-settings-update

Updates the campaign budget settings.

### GraphQL campaignClonesCreate Mutation

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/campaign-clones-create

Clones the specified campaigns and their components. Returns an ID that can be used to track the progress of each job created as a result.To use this mutation, you must have access to Kokai.

### GraphQL campaignAssociateBidList Mutation

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/campaign-associate-bid-list

Associate or remove bid lists from a campaign and enable or disable them for bidding.

### GraphQL campaignVersionUpgrade Mutation

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/campaign-version-upgrade

Upgrades the specified campaigns, performing necessary migrations in the process.

### POST /v3/campaign (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-campaign

This is a legacy endpoint. Use the [`campaignCreate` mutation](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/campaign-create) in GraphQL for improved performance and expanded functionality.

Create a new campaign.

### PUT /v3/campaign (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-campaign

This is a legacy endpoint. Use the [`campaignUpdate` mutation](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/campaign-update) in GraphQL for improved performance and expanded functionality.

Update an existing campaign.

### GET /v3/campaign/{campaignId} (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-campaign-campaignid

This is a legacy endpoint. Use the [`campaign` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/campaign) in GraphQL for improved performance and expanded functionality.

Get an existing campaign by ID.  
**TIP**: Using the equivalent campaign GraphQL query, you can enhance performance, customize criteria, and, if needed, expand your search across multiple campaigns.  
For details, see [GraphQL Campaign Query Examples](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/CampaignQueryExamplesGQL).

### GET /v3/campaign/{campaignId}/metrics (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-campaign-campaignid-metrics

This is a legacy endpoint. Use the [`campaign` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/campaign) in GraphQL for improved performance and expanded functionality.

Get metrics for an existing campaign.

### POST /v3/campaign/clone (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-campaign-clone

This is a legacy endpoint. Use the [`campaignClonesCreate` mutation](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/campaign-clones-create) in GraphQL for improved performance and expanded functionality.

Submits a job to clone a campaign.  
**IMPORTANT**: Here's what you need to know about this endpoint:

*   The API does not wait for the clone process to complete.
*   You can check outcome of the cloning process by calling the [GET /campaign/clone/status/{referenceId}](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-campaign-clone-status-referenceid) endpoint.
*   The URL, including the `ReferenceId`, is also given in the Location header.
*   You may not use this endpoint to clone campaigns with more than 500 ad group.
*   If the campaign to be cloned has Advanced Frequency Settings configured, they will not be cloned. To avoid unintentional spend, be sure to update your cloned campaign frequency settings accordingly.

### GET /v3/campaign/clone/status/{referenceId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-campaign-clone-status-referenceid

Gets status of the clone campaign job

### GET /v3/campaign/name/{campaignId} (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-campaign-name-campaignid

This is a legacy endpoint. Use the [`campaign` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/campaign) in GraphQL for improved performance and expanded functionality.

Get the identifier and name for a Campaign based on identifier

### POST /v3/campaign/query/advertiser (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-campaign-query-advertiser

This is a legacy endpoint. Use the [`advertiser` query](/v3/portal/api/gql-doc/advetiser) in GraphQL for improved performance and expanded functionality.

Get a page of Campaigns that belong to the specified Advertiser.

### GET /v3/campaign/query/facets (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-campaign-query-facets

This is a legacy endpoint. Use the [`campaigns` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/campaigns) in GraphQL for improved performance and expanded functionality.

Get the facets of Campaigns that can be queried.

### PUT /v3/campaign/template

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-campaign-template

Updates an existing Campaign template

### GET /v3/campaign/template/{campaignId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-campaign-template-campaignid

Get an existing Campaign template by ID.

### POST /v3/campaign/template/clone

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-campaign-template-clone

Submits a job to clone a campaign. The API does not wait for the clone process to complete.  
You can check outcome of the cloning process by calling the [GET /campaign/clone/status/{referenceId}](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-campaign-clone-status-referenceid) endpoint.  
The URL, including the `ReferenceId`, is also given in the Location header.  
NOTE: You may not use this endpoint to clone campaigns with more than 500 ad group.

### POST /v3/campaign/template/query/advertiser

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-campaign-template-query-advertiser

Get a page of Campaign templates that belong to the specified Advertiser.
