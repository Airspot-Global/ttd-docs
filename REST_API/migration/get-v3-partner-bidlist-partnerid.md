# GET /v3/partner/bidlist/{partnerId} → Partner.associatedBidLists

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-partner-bidlist-partnerid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/partner/bidlist/{partnerId} → Partner.associatedBidLists

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/partner/bidlist/{partnerId}` |
| GraphQL query | `Partner.associatedBidLists` |
| Return type | `AssociatedBidListsConnection` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `PartnerId` | `id` | ID! | Not nullable | Parent entity key on `Partner`. |
| `AssociatedBidLists` | `associatedBidLists` | AssociatedBidListsConnection | Nullable | Non-optional list on this endpoint. Same field as the main partner read. |
| `AssociatedBidLists.BidListId` | `associatedBidLists { nodes { bidList { id } } }` | ID! | Not nullable | See AssociatedBidList on the Partner domain page. |
| `AssociatedBidLists.IsEnabled` | `associatedBidLists { nodes { isEnabled } }` | Boolean! | Not nullable | N/A |
| `AssociatedBidLists.IsDefaultForDimension` | N/A | N/A | N/A | Not currently available in GraphQL |
| `AssociatedBidLists.BidListSource` | `associatedBidLists { nodes { bidList { source } } }` | BidListSource! | Not nullable | N/A |
| `AssociatedBidLists.BidListAdjustmentType` | `associatedBidLists { nodes { bidList { adjustmentType } } }` | BidListAdjustmentType! | Not nullable | N/A |
| `AssociatedBidLists.BidListDimensions` | `associatedBidLists { nodes { bidList { dimensions } } }` | [BidListDimension!]! | Not nullable | N/A |

## Code examples

### REST example

```
GET /v3/partner/bidlist/{partnerId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetPartnerBidLists($id: ID!) {
  partner(id: $id, withObjectLevelPermissions: false) {
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
      totalCount
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
}
```
