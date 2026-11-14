# Data Group

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Data%20Group
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Data%20Group (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### POST /v3/datagroup

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-datagroup

Create a new Data Group.

### PUT /v3/datagroup

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-datagroup

Update an existing Data Group.

### GET /v3/datagroup/{dataGroupId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-datagroup-datagroupid

Get an existing Data Group.

### GET /v3/datagroup/{dataGroupId}/{geoForCounts}

<!-- airspot:begin anchor="GET /v3/datagroup/{dataGroupId}/{geoForCounts}" -->
> **Airspot note (observed 2026-11-09, sandbox; not in TTD's official docs):** **Retired.** `GET /v3/datagroup/{dataGroupId}/{geoForCounts}` returns HTTP 410 with the body "Access denied to legacy endpoint 'get_datagroup/{dataGroupId}/{geoForCounts}' since 2026 August 03." Do not build on it. For geo-filtered counts, the audience variant `GET /v3/audience/{audienceId}/{geoForCounts}` still works (see the Airspot note in `REST_API/audience.md`).
<!-- airspot:end -->

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-datagroup-datagroupid-geoforcounts

Get an existing Data Group, and filter the returned counts by geo.

### GET /v3/datagroup/name/{dataGroupId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-datagroup-name-datagroupid

Get the identifier and name for an DataGroup based on identifier

### POST /v3/datagroup/query/advertiser

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-datagroup-query-advertiser

Get a page of Data Groups that belong to the specified Advertiser.

### GET /v3/datagroup/query/facets

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-datagroup-query-facets

Get the facets of Data Groups that can be queried.
