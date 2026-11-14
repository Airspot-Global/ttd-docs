# Tracking Tag

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Tracking%20Tag
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Tracking%20Tag (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### POST /v3/trackingtag

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-trackingtag

Create a new tracking tag.

### PUT /v3/trackingtag

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-trackingtag

Update an existing tracking tag. Offline tracking tags are readonly tags and may not be modified using this endpoint.

### POST /v3/trackingtag/query/advertiser

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-trackingtag-query-advertiser

Retrieve a paged, filterable list of tracking tags owned by or shared with the specified advertiser.

### GET /v3/trackingtag/query/facets

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-trackingtag-query-facets

Get the facets of Tracking Tags that can be queried.

### GET /v3/trackingtag/{trackingTagId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-trackingtag-trackingtagid

Get a tracking tag.
