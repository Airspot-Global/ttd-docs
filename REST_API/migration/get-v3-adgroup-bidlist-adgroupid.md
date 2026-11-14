# GET /v3/adgroup/bidlist/{adGroupId} → AdGroup.associatedBidLists

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-adgroup-bidlist-adgroupid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/adgroup/bidlist/{adGroupId} → AdGroup.associatedBidLists

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/adgroup/bidlist/{adGroupId}` |
| GraphQL query | `AdGroup.associatedBidLists` |
| Return type | `AdGroupAssociatedBidListsConnection` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdGroupId` | `id` | ID! | Not nullable | On parent `AdGroup` |
| `AssociatedBidLists[].BidListId` | `bidList.id` | ID! | Not nullable | On nested `IBidList` |
| `AssociatedBidLists[].IsEnabled` | `isEnabled` | Boolean! | Not nullable | On `AdGroupAssociatedBidList` node |
| `AssociatedBidLists[].IsDefaultForDimension` | `isDefaultForUI` | Boolean! | Not nullable | REST name; GraphQL field is `isDefaultForUI` |
| `AssociatedBidLists[].BidListSource` | `bidList.source` | BidListSource! | Not nullable | On nested `IBidList` |
| `AssociatedBidLists[].BidListAdjustmentType` | `bidList.adjustmentType` | BidListAdjustmentType! | Not nullable | On nested `IBidList` |
| `AssociatedBidLists[].BidListDimensions` | `bidList.dimensions` | [BidListDimension!]! | Not nullable | On nested `IBidList` |

## Code examples

### REST example

```
GET /v3/adgroup/bidlist/{adGroupId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetAdGroupBidLists($id: ID!) {
  adGroup(id: $id) {
    associatedBidLists {
      nodes {
        isEnabled
        isDefaultForUI
        bidList {
          id
          name
          source
          adjustmentType
          dimensions
        }
      }
    }
  }
}
```
