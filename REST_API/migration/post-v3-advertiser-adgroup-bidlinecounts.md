# POST /v3/advertiser/adgroup/bidlinecounts → Advertiser.bidLineLimit

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-advertiser-adgroup-bidlinecounts
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/advertiser/adgroup/bidlinecounts → Advertiser.bidLineLimit

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/advertiser/adgroup/bidlinecounts` |
| GraphQL query | `Advertiser.bidLineLimit` |
| Return type | `Long` |

## Multi-step operations

The REST endpoint returns per-ad-group bid line counts plus an advertiser-level limit. GraphQL exposes only the advertiser-level `bidLineLimit` field on `Advertiser`; per-ad-group rows and current bid line counts are not surfaced.

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PageStartIndex` | N/A | N/A | Optional | N/A |
| `PageSize` | N/A | N/A | Optional | N/A |
| `AdvertiserId` | Parent: `advertiser(id:)` | ID! | Required | Parent entity key; sent as POST body filter when loading `bidLineLimit`. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | N/A | N/A | N/A | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | N/A | N/A | N/A | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].AdGroupId` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Result[].AdGroupBidLineCount` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Result[].AdGroupBidLineLimit` | N/A | N/A | N/A | Not currently available in GraphQL |
| `AdvertiserId` | `id` | ID! | Not nullable | Parent entity key. |
| `AdvertiserBidLineCount` | N/A | N/A | N/A | Not currently available in GraphQL |
| `AdvertiserBidLineLimit` | `bidLineLimit` | Long | Nullable | N/A |

## Endpoint-specific nested types and enums

### AdGroupBidLineCounts

Per-ad-group bid line count rows in the REST `Result` collection. GraphQL does not expose these; only advertiser-level `bidLineLimit` is available.

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdGroupId` | N/A | N/A | N/A | Not currently available in GraphQL |
| `AdGroupBidLineCount` | N/A | N/A | N/A | Not currently available in GraphQL |
| `AdGroupBidLineLimit` | N/A | N/A | N/A | Not currently available in GraphQL |

## Code examples

### REST example

```
POST /v3/advertiser/adgroup/bidlinecounts HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserId": "abc123",
  "PageStartIndex": 0,
  "PageSize": 0
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query AdvertiserBidLineLimit {
  advertiser(id: "abc123") {
    id
    bidLineLimit
  }
}
```
