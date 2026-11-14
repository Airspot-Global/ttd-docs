# Geo Segment

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Geo%20Segment
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Geo%20Segment (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### GET /v3/geosegment/name/{geoSegmentId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-geosegment-name-geosegmentid

Get the identifier and name for a GeoSegment based on identifier

### POST /v3/geosegment/query/advertiser

<!-- airspot:begin anchor="POST /v3/geosegment/query/advertiser" -->
> **Airspot note (observed 2026-11-09, sandbox + production; not in TTD's official docs):** In production, a request body with `AdvertiserId`, `SearchTerms: ["Sweden"]`, `GeoSegmentFilter: "Country"`, `PageStartIndex` and `PageSize` works. Each item in `Result` has `GeoSegmentId`, `GeoSegmentName`, `Description`, `GeoLocationType` and `IsStandard`. The same request returned HTTP 500 in the sandbox, with both `GeoSegmentFilter: "Country"` and `"All"`.
<!-- airspot:end -->

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-geosegment-query-advertiser

Query Geo Segments for use by an Advertiser

### GET /v3/geosegment/query/facets

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-geosegment-query-facets

Get the facets of Geo Segments that can be queried.

### POST /v3/geosegment/query/partner

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-geosegment-query-partner

Query Geo Segments that are available for all advertisers for a partner
