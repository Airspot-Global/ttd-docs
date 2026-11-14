# POST /v3/crossdeviceattributionmodel/query/advertiser → Advertiser.crossDeviceAttributionModels

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-crossdeviceattributionmodel-query-advertiser
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/crossdeviceattributionmodel/query/advertiser → Advertiser.crossDeviceAttributionModels

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/crossdeviceattributionmodel/query/advertiser` |
| GraphQL query | `Advertiser.crossDeviceAttributionModels` |
| Return type | `CrossDeviceAttributionModelsConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | Parent: `Advertiser.crossDeviceAttributionModels` | N/A | Required | `AdvertiserId` is implicit from the parent `Advertiser` entity key—not exposed as a GraphQL argument. |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [CrossDeviceAttribution!] | Nullable | N/A |
| `Result.CrossDeviceAttributionModelId` | `CrossDeviceAttribution.id` | String! | Not nullable | Renamed from `CrossDeviceAttributionModelId` to `id`. |
| `Result.CrossDeviceAttributionModelName` | `CrossDeviceAttribution.name` | String | Nullable | Renamed from `CrossDeviceAttributionModelName` to `name`. |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |

## Endpoint-specific nested types and enums

### CrossDeviceAttribution

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CrossDeviceAttributionModelId` | `id` | String! | Not nullable | N/A |
| `CrossDeviceAttributionModelName` | `name` | String | Nullable | Display name. |

## Code examples

### REST example

```
POST /v3/crossdeviceattributionmodel/query/advertiser HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserId": "<advertiser-id>",
  "PageStartIndex": 0,
  "PageSize": 20
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetCrossDeviceAttributionModels($advertiserId: ID!) {
  advertiser(id: $advertiserId) {
    crossDeviceAttributionModels(first: 20) {
      nodes {
        id
        name
      }
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
}
```
