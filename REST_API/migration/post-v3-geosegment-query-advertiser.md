# POST /v3/geosegment/query/advertiser → Advertiser.geoSegments

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-geosegment-query-advertiser
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/geosegment/query/advertiser → Advertiser.geoSegments

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/geosegment/query/advertiser` |
| GraphQL query | `Advertiser.geoSegments` |
| Return type | `GeoSegmentsConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |
| `SearchTerms` | `where` | GeoSegmentFilterInput | Optional | REST search terms match ID/name/description; filter semantics are not 1:1 |
| `SortFields` | `order` | [GeoSegmentSortInput!] | Optional | N/A |
| `AdvertiserId` | N/A | N/A | Required | Parent advertiser node—not a public argument on `geoSegments` |
| `GeoSegmentFilter` | `where` | GeoSegmentFilterInput | Optional | REST `CustomOnly` default vs GraphQL filter semantics differ; verify filter parity |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [GeoSegment!] | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].GeoSegmentId` | `id` | ID! | Not nullable | GeoSegmentId → `id` |
| `Result[].GeoSegmentName` | `name` | String! | Not nullable | GeoSegmentName → name |
| `Result[].Description` | `description` | String | Nullable | N/A |
| `Result[].IsStandard` | `isStandard` | Boolean! | Not nullable | N/A |
| `Result[].GeoLocationType` | `type` | GeoSegmentType! | Not nullable | Enum rename GeoLocationType → GeoSegmentType |

## Code examples

### REST example

```
POST /v3/geosegment/query/advertiser HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserId": "abc123",
  "PageSize": 100,
  "PageStartIndex": 0
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query AdvertiserGeoSegments {
  advertiser(id: "abc123") {
    geoSegments(first: 100) {
      nodes {
        id
        name
        isStandard
        type
      }
      totalCount
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
}
```
