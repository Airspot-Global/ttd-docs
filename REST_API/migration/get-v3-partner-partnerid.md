# GET /v3/partner/{partnerId} → Query.partner

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-partner-partnerid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/partner/{partnerId} → Query.partner

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/partner/{partnerId}` |
| GraphQL query | `Query.partner(id:)` |
| Return type | `Partner` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `PartnerId` | `id` | ID! | Not nullable | Entity identifier on `Partner`. |
| `PartnerIdInteger` | `idInteger` | Int! | Not nullable | N/A |
| `PartnerName` | `name` | String! | Not nullable | N/A |
| `AssociatedBidLists` | `associatedBidLists` | AssociatedBidListsConnection | Nullable | See the Partner domain page for nested fields; select via `nodes`. |
| `AssociatedBidLists.BidListId` | `associatedBidLists { nodes { bidList { id } } }` | ID! | Not nullable | Nested—see AssociatedBidList on the Partner domain page. |
| `AssociatedBidLists.IsEnabled` | `associatedBidLists { nodes { isEnabled } }` | Boolean! | Not nullable | N/A |
| `AssociatedBidLists.IsDefaultForDimension` | N/A | N/A | N/A | Not currently available in GraphQL |
| `AssociatedBidLists.BidListSource` | `associatedBidLists { nodes { bidList { source } } }` | BidListSource! | Not nullable | N/A |
| `AssociatedBidLists.BidListAdjustmentType` | `associatedBidLists { nodes { bidList { adjustmentType } } }` | BidListAdjustmentType! | Not nullable | N/A |
| `AssociatedBidLists.BidListDimensions` | `associatedBidLists { nodes { bidList { dimensions } } }` | [BidListDimension!]! | Not nullable | N/A |
| `Increments` | `increments` | [String!]! | Not nullable | N/A |
| `NewFrequencyConfigs` | N/A | N/A | N/A | Never returned by this endpoint—omitted from GraphQL output. |

## Code examples

### REST example

```
GET /v3/partner/{partnerId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetPartnerDetails($id: ID!) {
  partner(id: $id, withObjectLevelPermissions: false) {
    id
    idInteger
    name
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
    increments
  }
}
```
