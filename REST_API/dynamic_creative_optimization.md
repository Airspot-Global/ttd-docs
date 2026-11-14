# Dynamic Creative Optimization

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Dynamic%20Creative%20Optimization
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Dynamic%20Creative%20Optimization (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### POST /v3/dynamiccreativerule

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-dynamiccreativerule

Create a new dynamic creative rule that can be attached to a  
[creative](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Creative). Learn more about what dynamic creative rules are and how to use them  
by logging into the platform and viewing our  
[Dynamic Creative Rules](https://app.getguru.com/card/i4kp6kLT/Dynamic-Creative-Rules) Knowledge Portal article.

### PUT /v3/dynamiccreativerule

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-dynamiccreativerule

Update an existing dynamic creative rule.

### GET /v3/dynamiccreativerule/{dynamicCreativeRuleId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-dynamiccreativerule-dynamiccreativeruleid

Retrieve the details for an existing dynamic creative rule using a specific `DynamicCreativeRuleId`

### POST /v3/dynamiccreativerule/query/advertiser

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-dynamiccreativerule-query-advertiser

Retrieve a paged, sortable and filterable list of dynamic creative rules owned by a specific advertiser. Use the [GET /dynamiccreativerule/query/facets](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-dynamiccreativerule-query-facets) endpoint to look up properties available to use for sorting.

### GET /v3/dynamiccreativerule/query/facets

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-dynamiccreativerule-query-facets

Retrieve the dynamic creative rule properties that can be used for sorting on the [POST /dynamiccreativerule/query/advertiser](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-dynamiccreativerule-query-advertiser) endpoint.
