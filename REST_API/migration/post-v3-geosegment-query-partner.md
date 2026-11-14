# POST /v3/geosegment/query/partner → Partner.geoSegments

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-geosegment-query-partner
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/geosegment/query/partner → Partner.geoSegments

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/geosegment/query/partner` |
| GraphQL query | `Partner.geoSegments` |
| Return type | `GeoSegmentsConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |
| `SearchTerms` | `where` | GeoSegmentFilterInput | Optional | N/A |
| `SortFields` | `order` | [GeoSegmentSortInput!] | Optional | N/A |
| `PartnerId` | N/A | N/A | Optional | Parent partner node; REST optional `PartnerId` defaults to primary partner |
| `GeoSegmentFilter` | `where` | GeoSegmentFilterInput | Optional | N/A |

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
POST /v3/geosegment/query/partner HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "PartnerId": "partner1",
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
query PartnerGeoSegments {
  partner(id: "partner1") {
    geoSegments(first: 100) {
      nodes {
        id
        name
        isStandard
      }
      totalCount
    }
  }
}
```
