# POST /v3/audience/insights/channelmix → Audience.channelMixInsights

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-audience-insights-channelmix
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/audience/insights/channelmix → Audience.channelMixInsights

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/audience/insights/channelmix` |
| GraphQL query | `Audience.channelMixInsights` |
| Return type | `ChannelMixInsights` |

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
| `Metrics` | `metrics` | [ChannelMixInsight!]! | Not nullable | N/A |
| `Metrics.DeviceType` | `metrics.deviceType` | DeviceType! | Not nullable | N/A |
| `Metrics.MediaType` | `metrics.mediaType` | MediaType! | Not nullable | N/A |
| `Metrics.RenderingContext` | `metrics.environment` | RenderingContext! | Not nullable | REST `RenderingContext` maps to `environment`. |
| `Metrics.PercentageOfAudience` | `metrics.percentageOfAudience` | Float! | Not nullable | N/A |

## Code examples

### REST example

```
POST /v3/audience/insights/channelmix HTTP/1.1
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
query ChannelMix {
  audience(id: "<audience-id>") {
    channelMixInsights(filter: { geoSegmentIds: ["<geo-segment-id>"] }) {
      metrics {
        deviceType
        mediaType
        environment
        percentageOfAudience
      }
    }
  }
}
```
