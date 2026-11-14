# POST /v3/bidderservice/query/partner → Partner.bidderServices

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-bidderservice-query-partner
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/bidderservice/query/partner → Partner.bidderServices

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/bidderservice/query/partner` |
| GraphQL query | `Partner.bidderServices` |
| Return type | `BidderServicesConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PartnerId` | Parent: `Partner.bidderServices` (relationship field) | N/A | Required | Supplied by parent `Partner.id`; not a filter arg. |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [BidderService!] | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `BidderServiceId` | `nodes[].id` | ID! | Not nullable | Per-item field on `BidderService`. |
| `Name` | `nodes[].name` | String! | Not nullable | N/A |
| `PartnerId` | `nodes[].partner` | Partner | Nullable | Nested `Partner` relationship—use `partner { id }` to read the owning partner identifier. |
| `IsEnabled` | `nodes[].isEnabled` | Boolean | Nullable | N/A |
| `BidderEndpoints` | `nodes[].bidderEndpoints` | [BidderEndpoint!]! | Not nullable | See BidderEndpoint on the domain page. |
| `BidderFeedbackEndpoints` | `nodes[].bidderFeedbackEndpoints` | [BidderFeedbackEndpoint!]! | Not nullable | See BidderFeedbackEndpoint on the domain page. |
| `VolumeControlPriorities` | `nodes[].volumeControlPriorities` | [VolumeControlPriority!]! | Not nullable | Enum list—see VolumeControlPriority on the domain page. |

## Code examples

### REST example

```
POST /v3/bidderservice/query/partner HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "PartnerId": "<partnerId>",
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
query PartnerBidderServices($partnerId: ID!) {
  partner(id: $partnerId) {
    id
    bidderServices(first: 20) {
      nodes {
        id
        name
        isEnabled
        partner {
          id
        }
        volumeControlPriorities
        bidderEndpoints {
          dataCenter
          url
          isEnabled
        }
        bidderFeedbackEndpoints {
          dataCenter
          url
          isEnabled
        }
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
