# GET /v3/bidderservice/{bidderServiceId} → Query.bidderService

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-bidderservice-bidderserviceid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/bidderservice/{bidderServiceId} → Query.bidderService

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/bidderservice/{bidderServiceId}` |
| GraphQL query | `Query.bidderService(id:)` |
| Return type | `BidderService` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `BidderServiceId` | `id` | ID! | Not nullable | Entity identifier. |
| `Name` | `name` | String! | Not nullable | N/A |
| `PartnerId` | `partner` | Partner | Nullable | Nested `Partner` relationship—use `partner { id }` to read the owning partner identifier. |
| `IsEnabled` | `isEnabled` | Boolean | Nullable | N/A |
| `BidderEndpoints` | `bidderEndpoints` | [BidderEndpoint!]! | Not nullable | Aggregated collection—see BidderEndpoint. |
| `BidderFeedbackEndpoints` | `bidderFeedbackEndpoints` | [BidderFeedbackEndpoint!]! | Not nullable | Aggregated collection—see BidderFeedbackEndpoint. |
| `VolumeControlPriorities` | `volumeControlPriorities` | [VolumeControlPriority!]! | Not nullable | Enum list—see VolumeControlPriority on the domain page. |

## Endpoint-specific nested types and enums

### BidderEndpoint

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `DataCenter` | `dataCenter` | BiddingDataCenter! | Not nullable | N/A |
| `Url` | `url` | String! | Not nullable | N/A |
| `IsEnabled` | `isEnabled` | Boolean! | Not nullable | N/A |

### BidderFeedbackEndpoint

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `DataCenter` | `dataCenter` | BiddingDataCenter! | Not nullable | N/A |
| `Url` | `url` | String! | Not nullable | N/A |
| `IsEnabled` | `isEnabled` | Boolean! | Not nullable | N/A |

## Code examples

### REST example

```
GET /v3/bidderservice/{bidderServiceId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetBidderService($id: ID!) {
  bidderService(id: $id) {
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
}
```
