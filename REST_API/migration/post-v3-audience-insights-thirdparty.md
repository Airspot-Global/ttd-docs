# POST /v3/audience/insights/thirdparty → Audience.thirdPartySegmentInsights

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-audience-insights-thirdparty
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/audience/insights/thirdparty → Audience.thirdPartySegmentInsights

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/audience/insights/thirdparty` |
| GraphQL query | `Audience.thirdPartySegmentInsights` |
| Return type | `ThirdPartySegmentInsightsConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AudienceId` | Parent: `Query.audience(id: ID!)` | N/A | Required | Enter via `audience(id: "<audience-id>") { thirdPartySegmentInsights(...) }`. |
| `GeoSegmentIds` | `filter.geoSegmentIds` | [ID!]! | Required | `AudienceThirdPartySegmentInsightsParamInput`. |
| `UseMockData` | N/A | N/A | N/A | **Not currently available in GraphQL** |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [ThirdPartySegmentInsight!] | Nullable | N/A |
| `Result.ThirdPartyDataId` | `nodes.thirdPartyDataId` | Long! | Not nullable | N/A |
| `Result.ThirdPartyDataBrandId` | `nodes.thirdPartyDataBrandId` | String! | Not nullable | N/A |
| `Result.SegmentName` | `nodes.segmentName` | String! | Not nullable | N/A |
| `Result.BrandName` | `nodes.brandName` | String! | Not nullable | N/A |
| `Result.Size` | `nodes.size` | Long! | Not nullable | N/A |
| `Result.Cpm` | `nodes.cpm` | MoneyModel! | Not nullable | N/A |
| `Result.Cpm.Amount` | `nodes.cpm.amount` | Decimal! | Not nullable | N/A |
| `Result.Cpm.CurrencyCode` | `nodes.cpm.currencyCode` | CurrencyCode! | Not nullable | N/A |
| `Result.RelevanceScore` | `nodes.relevanceScore` | Float! | Not nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |

## Endpoint-specific nested types and enums

### ThirdPartySegmentInsight

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `ThirdPartyDataId` | `thirdPartyDataId` | Long! | Not nullable | N/A |
| `ThirdPartyDataBrandId` | `thirdPartyDataBrandId` | String! | Not nullable | N/A |
| `SegmentName` | `segmentName` | String! | Not nullable | N/A |
| `BrandName` | `brandName` | String! | Not nullable | N/A |
| `Size` | `size` | Long! | Not nullable | N/A |
| `Cpm` | `cpm` | MoneyModel! | Not nullable | See the Audience domain page for `MoneyModel`. |
| `RelevanceScore` | `relevanceScore` | Float! | Not nullable | N/A |

## Code examples

### REST example

```
POST /v3/audience/insights/thirdparty HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AudienceId": "<audience-id>",
  "GeoSegmentIds": ["<geo-segment-id>"],
  "PageStartIndex": 0,
  "PageSize": 25
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query ThirdPartyInsights {
  audience(id: "<audience-id>") {
    thirdPartySegmentInsights(
      first: 25
      filter: { geoSegmentIds: ["<geo-segment-id>"] }
    ) {
      nodes {
        segmentName
        brandName
        size
        cpm {
          amount
          currencyCode
        }
        relevanceScore
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
