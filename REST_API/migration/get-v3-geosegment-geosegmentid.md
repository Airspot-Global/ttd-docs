# GET /v3/geosegment/{geoSegmentId} → Query.geoSegmentsSearch

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-geosegment-geosegmentid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/geosegment/{geoSegmentId} → Query.geoSegmentsSearch

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/geosegment/{geoSegmentId}` |
| GraphQL query | `Query.geoSegmentsSearch` |
| Return type | `GeoSegmentsSearchConnection` |

> **Advisory:** Load a segment by ID via `geoSegmentsSearch` with `where: { id: { eq: "…" } }` and required `input.geoSegmentType`. Request `geoElements` and other fields on the returned `GeoSegment` nodes.

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `geoSegmentId` | `where.id.eq` | String | Required | Path parameter → `GeoSegmentFilterInput.id` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `GeoSegmentId` | `nodes[].id` | ID! | Not nullable | Entity key |
| `AdvertiserId` | `nodes[].advertiser` | Advertiser | Nullable | N/A |
| `PartnerId` | `nodes[].partner` | Partner | Nullable | N/A |
| `GeoSegmentName` | `nodes[].name` | String! | Not nullable | N/A |
| `GeoSegmentDescription` | `nodes[].description` | String | Nullable | N/A |
| `IsReadonly` | `nodes[].isReadonly` | Boolean | Nullable | N/A |
| `GeoElements` | `nodes[].geoElements` | [GeoElement!]! | Not nullable | N/A |
| `GeoElements[].GeoElementId` | `id` | ID! | Not nullable | N/A |
| `GeoElements[].IsDeprecated` | `isDeprecated` | Boolean | Nullable | N/A |
| `GeoElements[].GeoElementType` | `type` | GeoElementKind | Nullable | N/A |
| `GeoElements[].CountryCode` | `countryCode` | String | Nullable | N/A |
| `GeoElements[].CountryName` | `countryName` | String | Nullable | N/A |
| `GeoElements[].MetroCode` | N/A | N/A | N/A | MetroCode/MetroName deprecated on REST; GraphQL maps NielsenDma fields only |
| `GeoElements[].MetroName` | N/A | N/A | N/A | MetroCode/MetroName deprecated on REST; GraphQL maps NielsenDma fields only |
| `GeoElements[].NielsenDmaCode` | `nielsenDmaCode` | String | Nullable | N/A |
| `GeoElements[].NielsenDmaName` | `nielsenDmaName` | String | Nullable | N/A |
| `GeoElements[].RegionCode` | `regionCode` | String | Nullable | N/A |
| `GeoElements[].RegionName` | `regionName` | String | Nullable | N/A |
| `GeoElements[].CityName` | `cityName` | String | Nullable | N/A |
| `GeoElements[].Zip` | `zip` | String | Nullable | N/A |

## Endpoint-specific nested types and enums

### GeoElement

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `GeoElementId` | `id` | ID! | Not nullable | N/A |
| `IsDeprecated` | `isDeprecated` | Boolean | Nullable | N/A |
| `GeoElementType` | `type` | GeoElementKind | Nullable | N/A |
| `CountryCode` | `countryCode` | String | Nullable | N/A |
| `CountryName` | `countryName` | String | Nullable | N/A |
| `MetroCode` | N/A | N/A | N/A | Deprecated on REST |
| `MetroName` | N/A | N/A | N/A | Deprecated on REST |
| `NielsenDmaCode` | `nielsenDmaCode` | String | Nullable | N/A |
| `NielsenDmaName` | `nielsenDmaName` | String | Nullable | N/A |
| `RegionCode` | `regionCode` | String | Nullable | N/A |
| `RegionName` | `regionName` | String | Nullable | N/A |
| `CityName` | `cityName` | String | Nullable | N/A |
| `Zip` | `zip` | String | Nullable | N/A |

## Code examples

### REST example

```
GET /v3/geosegment/{geoSegmentId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GeoSegmentDetail {
  geoSegmentsSearch(
    first: 1
    input: { geoSegmentType: ALL }
    where: { id: { eq: "gs123" } }
  ) {
    nodes {
      id
      name
      isReadonly
      geoElements {
        id
        type
        countryCode
        nielsenDmaCode
      }
    }
  }
}
```
