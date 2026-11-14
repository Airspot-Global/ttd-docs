# Contract Group

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Contract%20Group
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Contract%20Group (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### POST /v3/contractgroup

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-contractgroup

Create a new Contract Group.

### PUT /v3/contractgroup

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-contractgroup

Update an existing Contract Group.

### GET /v3/contractgroup/{contractGroupId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-contractgroup-contractgroupid

Get an existing Contract Group.

### GET /v3/contractgroup/name/{contractGroupId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-contractgroup-name-contractgroupid

Get the identifier and name for an Contract Group based on identifier

### POST /v3/contractgroup/query/advertiser/available

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-contractgroup-query-advertiser-available

Get the page of Contract Groups that a specific Advertiser is allowed to buy

### POST /v3/contractgroup/query/deliveryprofile

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-contractgroup-query-deliveryprofile

Query for a page of Contracts Groups that are associated with specified DeliveryProfileId

### POST /v3/contractgroup/query/partner

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-contractgroup-query-partner

Get the page of Contract Groups owned by Partner

### POST /v3/contractgroup/report/impressions/available

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-contractgroup-report-impressions-available

Query for a page of an Available Impressions Report for a specific Contract Group.
