# POST /v3/audience/insights/interests → Audience.interestAudienceInsights

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-audience-insights-interests
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/audience/insights/interests → Audience.interestAudienceInsights

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/audience/insights/interests` |
| GraphQL query | `Audience.interestAudienceInsights` |
| Return type | `InterestAudienceInsights` |

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
| `Metrics` | `metrics` | [InterestAudienceInsight!]! | Not nullable | N/A |
| `Metrics.InterestName` | `metrics.interestName` | String! | Not nullable | N/A |
| `Metrics.RelevanceScore` | `metrics.relevanceScore` | Float! | Not nullable | N/A |

## Code examples

### REST example

```
POST /v3/audience/insights/interests HTTP/1.1
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
query InterestAudienceInsights {
  audience(id: "<audience-id>") {
    interestAudienceInsights(filter: { geoSegmentIds: ["<geo-segment-id>"] }) {
      metrics {
        interestName
        relevanceScore
      }
    }
  }
}
```
