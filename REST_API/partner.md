# Partner

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Partner
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Partner (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### GraphQL partner Query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/partner

Get an existing partner by ID.

### GraphQL partners Query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/partners

Get existing partners.

### GraphQL partnerUpdate Mutation

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/partner-update

Updates partner.

### GraphQL partnerAssociateBidList Mutation

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/partner-associate-bid-list

Associate or remove bid lists from a partner and enable or disable them for bidding.

### PUT /v3/partner (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-partner

This is a legacy endpoint. Use the [`partner` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/partner) in GraphQL for improved performance and expanded functionality.

Update an existing partner.

### POST /v3/partner/advertiser/bidlinecounts

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-partner-advertiser-bidlinecounts

Paged query to retrieve the bidline counts for advertisers owned by a given partner.  
Maximum page size for this query is 1,000.

### GET /v3/partner/name/{partnerId} (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-partner-name-partnerid

This is a legacy endpoint. Use the [`partner` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/partner) in GraphQL for improved performance and expanded functionality.

Get the identifier and name for a Partner based on identifier

### GET /v3/partner/{partnerId} (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-partner-partnerid

This is a legacy endpoint. Use the [`partner` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/partner) in GraphQL for improved performance and expanded functionality.

Get an existing partner by ID.

### POST /v3/partner/query (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-partner-query

This is a legacy endpoint. Use the [`partners` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/partners) in GraphQL for improved performance and expanded functionality.

Get all Partners that are accessible.

### GET /v3/partner/query/facets (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-partner-query-facets

This is a legacy endpoint. Use the [`partners` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/partners) in GraphQL for improved performance and expanded functionality.

Get the facets of Partners that can be queried.
