# POST /v3/partner/bidlist → partnerAssociateBidList

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-partner-bidlist
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/partner/bidlist → partnerAssociateBidList

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/partner/bidlist` |
| GraphQL operation | `partnerAssociateBidList` |
| Input type | `PartnerAssociateBidListInput` |
| Output type | `PayloadWithErrorsOfPartner` (`data: Partner`, `userErrors: [UserError!]!`) |

## Input field mapping

Input type: `PartnerAssociateBidListInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PartnerId` | `partnerId` | ID! | Required | N/A |
| `BidList` | `bidListsToAddOrUpdate` | [BidListAddOrUpdateInput!] | Required | REST `BidList` nested object maps to a single `BidListAddOrUpdateInput` entry |
| `BidList.BidListId` | `bidListsToAddOrUpdate[].bidListId` | ID! | Required | N/A |
| `BidList.IsEnabled` | `bidListsToAddOrUpdate[].isEnabled` | Boolean | Optional | N/A |
| `BidList.IsDefaultForDimension` | N/A | Boolean | Optional | Not currently available in GraphQL |
| `BidList.BidListSource` | N/A | BidListSource | Optional | **Read-only** |
| `BidList.BidListAdjustmentType` | N/A | BidListAdjustmentType | Optional | **Read-only** |
| `BidList.BidListDimensions` | N/A | [BidListDimension!] | Optional | **Read-only** |

## Output field mapping

Output type: `Partner` (returned as `data`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `PartnerId` | `id` | ID! | Not nullable | N/A |
| `AssociatedBidLists` | `associatedBidLists` | AssociatedBidListsConnection | Nullable | N/A |
| `AssociatedBidLists[].BidListId` | `associatedBidLists.nodes[].bidList.id` | ID! | Not nullable | Via nested `bidList` on `AssociatedBidList` |
| `AssociatedBidLists[].IsEnabled` | `associatedBidLists.nodes[].isEnabled` | Boolean! | Not nullable | N/A |
| `AssociatedBidLists[].IsDefaultForDimension` | N/A | Boolean | Nullable | **Not currently available in GraphQL** |
| `AssociatedBidLists[].BidListSource` | `associatedBidLists.nodes[].bidList.source` | BidListSource! | Not nullable | N/A |
| `AssociatedBidLists[].BidListAdjustmentType` | `associatedBidLists.nodes[].bidList.adjustmentType` | BidListAdjustmentType! | Not nullable | N/A |
| `AssociatedBidLists[].BidListDimensions` | `associatedBidLists.nodes[].bidList.dimensions` | [BidListDimension!]! | Not nullable | N/A |

## Code examples

### REST example

```
POST /v3/partner/bidlist HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "PartnerId": "abc123",
  "BidList": {
    "BidListId": "bl456",
    "IsEnabled": true,
    "IsDefaultForDimension": false
  }
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation {
  partnerAssociateBidList(
    input: {
      partnerId: "abc123"
      bidListsToAddOrUpdate: [{ bidListId: "bl456", isEnabled: true }]
    }
  ) {
    data {
      id
      associatedBidLists {
        nodes {
          isEnabled
          bidList { id }
        }
      }
    }
    userErrors {
      message
      field
    }
  }
}
```
