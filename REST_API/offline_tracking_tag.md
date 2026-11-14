# Offline Tracking Tag

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Offline%20Tracking%20Tag
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Offline%20Tracking%20Tag (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### POST /v3/offlinetrackingtag

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-offlinetrackingtag

Create a new offline tracking tag.

### PUT /v3/offlinetrackingtag

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-offlinetrackingtag

Update an existing offline tracking tag. We currenly only allow the name to be updated - the rest of the fields are read-only.

### POST /v3/offlinetrackingtag/query/advertiser

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-offlinetrackingtag-query-advertiser

Get a page of offline tracking tags that belong to a specified advertiser

### GET /v3/offlinetrackingtag/query/facets

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-offlinetrackingtag-query-facets

Get the facets of offline tracking tags that can be queried.

### GET /v3/offlinetrackingtag/{trackingTagId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-offlinetrackingtag-trackingtagid

Get an offline tracking tag.
