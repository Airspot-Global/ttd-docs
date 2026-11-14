# Ad Group

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Ad%20Group
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Ad%20Group (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### GraphQL adGroup Query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/ad-group

Get an existing ad group.

### GraphQL adGroups Query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/ad-groups

Get existing ad groups.

### GraphQL adGroupCreate Mutation

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/ad-group-create

Create an ad group.

### GraphQL adGroupUpdate Mutation

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/ad-group-update

Update an ad group.

### GraphQL adGroupSpendPrioritizationUpdate Mutation

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/ad-group-spend-prioritization-update

Updates the ad group spend prioritization settings.

### POST /v3/adgroup

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-adgroup

Create a new Ad Group.

### PUT /v3/adgroup

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-adgroup

Update an existing Ad Group.

### GET /v3/adgroup/{adGroupId} (deprecated)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-adgroup-adgroupid

We recommend using the [`adGroup` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/ad-group) in GraphQL for improved performance and expanded functionality. Existing integrations using this endpoint will continue to work.

Get an existing Ad Group.

### GET /v3/adgroup/analyticsreport/{adGroupId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-adgroup-analyticsreport-adgroupid

Get the analytics report(s) for an existing Ad Group.

### GET /v3/adgroup/koaapplieditems/{adGroupId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-adgroup-koaapplieditems-adgroupid

Retrieve Koa optimizations applied to the specified ad group, including impact and last attempt details. For details and code samples [Koa Optimizations](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/KoaOptimizations).

### GET /v3/adgroup/koarecommendations/{adGroupId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-adgroup-koarecommendations-adgroupid

Retrieve the current list of available optimizations recommended by Koa for the specified ad group.

### GET /v3/adgroup/name/{adGroupId} (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-adgroup-name-adgroupid

This is a legacy endpoint. Use the [`adGroup` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/ad-group) in GraphQL for improved performance and expanded functionality.

Get the identifier and name for an AdGroup based on identifier

### POST /v3/adgroup/query/advertiser (deprecated)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-adgroup-query-advertiser

We recommend using the [`adGroups` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/ad-groups) with filtering, or the [`advertiser` → `adGroups` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/advertiser), in GraphQL for improved performance and expanded functionality. Existing integrations using this endpoint will continue to work.

Look up and optionally filter a list of ad groups for a specified advertiser.

### POST /v3/adgroup/query/campaign (deprecated)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-adgroup-query-campaign

We recommend using the [`adGroups` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/ad-groups) with filtering, or the [`campaign` → `adGroups` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/campaign), in GraphQL for improved performance and expanded functionality. Existing integrations using this endpoint will continue to work.

Look up and optionally filter a list of ad groups for a specified campaign.

### POST /v3/adgroup/query/campaign/template

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-adgroup-query-campaign-template

Look up and optionally filter a list of ad groups for a specified campaign template.

### GET /v3/adgroup/query/facets (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-adgroup-query-facets

This is a legacy endpoint. Use the [`adGroup` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/ad-group) with filtering in GraphQL for improved performance and expanded functionality.

The facets of Ad Groups that can be queried.

### PUT /v3/adgroup/status (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-adgroup-status

This is a legacy endpoint. Use the [`adGroupUpdate` mutation](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/ad-group-update) in GraphQL for improved performance and expanded functionality.

Enable or disable a given Ad Group.

### GET /v3/adgroup/status/{adGroupId} (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-adgroup-status-adgroupid

This is a legacy endpoint. Use the [`adGroup` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/ad-group) in GraphQL for improved performance and expanded functionality.

Get the status of an Ad Group.
