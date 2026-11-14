# Advertiser

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Advertiser
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Advertiser (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### GraphQL advertiser Query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/advertiser

Get an existing advertiser by ID.

### GraphQL advertisers Query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/advertisers

Get existing advertisers.

### GraphQL advertiserCreate Mutation

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/advertiser-create

Create a new advertiser.

### GraphQL advertiserUpdate Mutation

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/advertiser-update

Update an advertiser.

### GraphQL advertiserDelta Query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/advertiser-delta

Get all changed advertisers for a partner since the last change-tracking version.

### POST /v3/advertiser (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-advertiser

This is a legacy endpoint. Use the [`advertiserCreate` mutation](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/advertiser-create) in GraphQL for improved performance and expanded functionality.

Create a new advertiser.

### PUT /v3/advertiser (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-advertiser

This is a legacy endpoint. Use the [`advertiserUpdate` mutation](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/advertiser-update) in GraphQL for improved performance and expanded functionality.

Update an existing advertiser.

### POST /v3/advertiser/adgroup/bidlinecounts

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-advertiser-adgroup-bidlinecounts

Paged query to retrieve the bidline counts for adgroups owned by a given advertiser.  
Maximum page size for this query is 1,000.

### GET /v3/advertiser/{advertiserId} (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-advertiser-advertiserid

This is a legacy endpoint. Use the [`advertiser` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/advertiser) in GraphQL for improved performance and expanded functionality.

Get an existing advertiser by ID.  
**TIP**: Using the equivalent advertiser GraphQL query, you can enhance performance, customize criteria, and, if needed, expand your search across multiple advertisers.  
For details, see [Look Up Advertiser Settings](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/AdvertiserGQLQueryExamples#query-advertiser-settings).

### GET /v3/advertiser/name/{advertiserId} (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-advertiser-name-advertiserid

This is a legacy endpoint. Use the [`advertiser` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/advertiser) in GraphQL for improved performance and expanded functionality.

Get the identifier and name for an Advertiser based on identifier

### GET /v3/advertiser/query/facets (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-advertiser-query-facets

This is a legacy endpoint. Use the [`advertiser` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/advertiser-create) with filtering in GraphQL for improved performance and expanded functionality.

Get the facets of Advertisers that can be queried.

### POST /v3/advertiser/query/partner (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-advertiser-query-partner

This is a legacy endpoint. Use the [`partner` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/partner) with filtering in GraphQL for improved performance and expanded functionality.

Get Advertisers that belong to the specified Partner.
