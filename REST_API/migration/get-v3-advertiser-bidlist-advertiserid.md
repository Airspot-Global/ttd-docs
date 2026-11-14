# GET /v3/advertiser/bidlist/{advertiserId} → Advertiser.associatedBidLists

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-advertiser-bidlist-advertiserid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/advertiser/bidlist/{advertiserId} → Advertiser.associatedBidLists

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/advertiser/bidlist/{advertiserId}` |
| GraphQL query | `Advertiser.associatedBidLists` |
| Return type | `AssociatedBidListsConnection` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | `id` | ID! | Not nullable | Parent entity key. |
| `AssociatedBidLists[].BidListId` | `associatedBidLists { nodes { bidList { id } } }` | ID! | Not nullable | See AssociatedBidList on the Advertiser domain page. |
| `AssociatedBidLists[].IsEnabled` | `associatedBidLists { nodes { isEnabled } }` | Boolean! | Not nullable | N/A |
| `AssociatedBidLists[].IsDefaultForDimension` | N/A | N/A | N/A | Not currently available in GraphQL |
| `AssociatedBidLists[].BidListSource` | `associatedBidLists { nodes { bidList { source } } }` | BidListSource! | Not nullable | N/A |
| `AssociatedBidLists[].BidListAdjustmentType` | `associatedBidLists { nodes { bidList { adjustmentType } } }` | BidListAdjustmentType! | Not nullable | N/A |
| `AssociatedBidLists[].BidListDimensions` | `associatedBidLists { nodes { bidList { dimensions } } }` | [BidListDimension!]! | Not nullable | N/A |

## Code examples

### REST example

```
GET /v3/advertiser/bidlist/{advertiserId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query AdvertiserAssociatedBidLists {
  advertiser(id: "abc123") {
    id
    associatedBidLists(first: 50) {
      nodes {
        isEnabled
        bidList {
          id
          source
          adjustmentType
          dimensions
        }
      }
    }
  }
}
```
