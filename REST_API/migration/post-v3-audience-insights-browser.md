# POST /v3/audience/insights/browser → Audience.browserInsights

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-audience-insights-browser
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/audience/insights/browser → Audience.browserInsights

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/audience/insights/browser` |
| GraphQL query | `Audience.browserInsights` |
| Return type | `BrowserInsights` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AudienceId` | Parent: `Query.audience(id: ID!)` | N/A | Required | Audience ID is taken from the parent entity. |
| `GeoSegmentIds` | `filter.geoSegmentIds` | [ID!]! | Required | `AudienceBreakdownInsightsParamInput`. |
| `UseMockData` | N/A | N/A | N/A | **Not currently available in GraphQL** |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AudienceId` | N/A | N/A | N/A | Taken from parent `audience(id)` query; not echoed in response. |
| `GeoSegmentIds` | N/A | N/A | N/A | Supplied via `filter.geoSegmentIds`; not echoed in response. |
| `Metrics` | `metrics` | [BrowserInsight!]! | Not nullable | N/A |
| `Metrics.Browser` | `metrics.browser` | Browser! | Not nullable | N/A |
| `Metrics.PercentageOfAudience` | `metrics.percentageOfAudience` | Float! | Not nullable | N/A |

## Code examples

### REST example

```
POST /v3/audience/insights/browser HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AudienceId": "<audience-id>",
  "GeoSegmentIds": ["<geo-segment-id>"]
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query BrowserInsights {
  audience(id: "<audience-id>") {
    browserInsights(filter: { geoSegmentIds: ["<geo-segment-id>"] }) {
      metrics {
        browser
        percentageOfAudience
      }
    }
  }
}
```
