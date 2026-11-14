# GET /v3/geosegment/name/{geoSegmentId} → Query.geoSegmentsSearch

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-geosegment-name-geosegmentid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/geosegment/name/{geoSegmentId} → Query.geoSegmentsSearch

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/geosegment/name/{geoSegmentId}` |
| GraphQL query | `Query.geoSegmentsSearch` |
| Return type | `GeoSegmentsSearchConnection` |

> **Advisory:** Load id and name via `geoSegmentsSearch` with `where: { id: { eq: "…" } }` and required `input.geoSegmentType`.

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `geoSegmentId` | `where.id.eq` | String | Required | Path parameter → `GeoSegmentFilterInput.id` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Id` | `nodes[].id` | ID! | Not nullable | N/A |
| `Name` | `nodes[].name` | String! | Not nullable | N/A |

## Code examples

### REST example

```
GET /v3/geosegment/name/{geoSegmentId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GeoSegmentName {
  geoSegmentsSearch(
    first: 1
    input: { geoSegmentType: ALL }
    where: { id: { eq: "gs123" } }
  ) {
    nodes {
      id
      name
    }
  }
}
```
