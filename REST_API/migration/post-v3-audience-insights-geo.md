# POST /v3/audience/insights/geo → Audience.geoInsights

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-audience-insights-geo
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/audience/insights/geo → Audience.geoInsights

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/audience/insights/geo` |
| GraphQL query | `Audience.geoInsights` |
| Return type | `GeoInsightsConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AudienceId` | Parent: `Query.audience(id: ID!)` | N/A | Required | Enter via `audience(id: "<audience-id>") { geoInsights(...) }`. |
| `GeoSegmentIds` | `filter.geoSegmentIds` | [ID!]! | Required | `AudienceGeoInsightsParamInput`. |
| `UseMockData` | N/A | N/A | N/A | **Not currently available in GraphQL** |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [GeoInsight!] | Nullable | N/A |
| `Result.Name` | `nodes.geoSegment.name` | String! | Not nullable | Nested on `GeoSegment`. |
| `Result.GeoSegmentId` | `nodes.geoSegment.id` | ID! | Not nullable | N/A |
| `Result.GeoType` | `nodes.geoSegment.type` | GeoSegmentType! | Not nullable | N/A |
| `Result.Cpm` | `nodes.cpm` | MoneyModel! | Not nullable | N/A |
| `Result.Cpm.Amount` | `nodes.cpm.amount` | Decimal! | Not nullable | N/A |
| `Result.Cpm.CurrencyCode` | `nodes.cpm.currencyCode` | CurrencyCode! | Not nullable | N/A |
| `Result.Avails` | `nodes.avails` | Long! | Not nullable | N/A |
| `Result.RelevanceScore` | `nodes.relevanceScore` | Float! | Not nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |

## Endpoint-specific nested types and enums

### GeoInsight

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Name` | `geoSegment.name` | String! | Not nullable | N/A |
| `GeoSegmentId` | `geoSegment.id` | ID! | Not nullable | N/A |
| `GeoType` | `geoSegment.type` | GeoSegmentType! | Not nullable | N/A |
| `Cpm` | `cpm` | MoneyModel! | Not nullable | See the Audience domain page for `MoneyModel`. |
| `Avails` | `avails` | Long! | Not nullable | N/A |
| `RelevanceScore` | `relevanceScore` | Float! | Not nullable | N/A |

## Code examples

### REST example

```
POST /v3/audience/insights/geo HTTP/1.1
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
query GeoInsights {
  audience(id: "<audience-id>") {
    geoInsights(
      first: 25
      filter: { geoSegmentIds: ["<geo-segment-id>"] }
    ) {
      nodes {
        geoSegment {
          id
          name
          type
        }
        avails
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
