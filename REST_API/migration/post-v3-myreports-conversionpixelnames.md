# POST /v3/myreports/conversionpixelnames → Query.historicalConversionPixels

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-myreports-conversionpixelnames
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/myreports/conversionpixelnames → Query.historicalConversionPixels

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/myreports/conversionpixelnames` |
| GraphQL query | `Query.historicalConversionPixels` or `Advertiser.historicalConversionPixels` |
| Return type | `HistoricalConversionPixelsConnection` (`HistoricalConversionPixel` nodes) |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |
| `PartnerIds` | N/A | N/A | Optional | **Remodelled in GraphQL** |
| `AdvertiserIds` | `where.advertiserIds.in` | [String] | Optional | N/A |
| `CampaignIds` | N/A | N/A | Optional | **Remodelled in GraphQL** |
| `AdGroupIds` | N/A | N/A | Optional | **Remodelled in GraphQL** |
| `ReportTemplateId` | N/A | N/A | Required | **Remodelled in GraphQL** |
| `CrossDeviceAttributionModelId` | `where.crossDeviceAttributionModel.eq` | CrossDeviceAttributionModelId | Optional | REST string IDs map to enum members (e.g. REST `"Identity"` → `IDENTITY_ALLIANCE`). |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [HistoricalConversionPixel!] | Nullable | N/A |
| `ResultCount` | (derived from `nodes`) | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].AdvertiserId` | `advertiser.id` | ID! | Not nullable | N/A |
| `Result[].ConversionPixelName` | `trackingTag.name` | String! | Not nullable | N/A |
| `Result[].ConversionType` | `trackingTag.id` | String! | Not nullable | Tracking tag ID. |
| `Result[].CrossDeviceAttributionModelId` | `crossDeviceAttribution.model` | CrossDeviceAttributionModelId | Nullable | N/A |

## Endpoint-specific nested types and enums

### ConversionPixel

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | `advertiser.id` | ID! | Not nullable | N/A |
| `ConversionPixelName` | `trackingTag.name` | String! | Not nullable | N/A |
| `ConversionType` | `trackingTag.id` | String! | Not nullable | Tracking tag ID. |
| `CrossDeviceAttributionModelId` | `crossDeviceAttribution.model` | CrossDeviceAttributionModelId | Nullable | REST `"Identity"` → `IDENTITY_ALLIANCE`. |

## Code examples

### REST example

```
POST /v3/myreports/conversionpixelnames HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "PageStartIndex": 0,
  "PageSize": 100,
  "AdvertiserIds": ["abc123"],
  "ReportTemplateId": 98765,
  "CrossDeviceAttributionModelId": "Identity"
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query HistoricalConversionPixels {
  historicalConversionPixels(
    first: 100
    where: {
      advertiserIds: { in: ["abc123"] }
      crossDeviceAttributionModel: { eq: IDENTITY_ALLIANCE }
    }
  ) {
    nodes {
      advertiser {
        id
      }
      trackingTag {
        id
        name
      }
      crossDeviceAttribution {
        model
      }
    }
    totalCount
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```
