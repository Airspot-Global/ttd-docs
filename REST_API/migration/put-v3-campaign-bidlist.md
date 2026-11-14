# PUT /v3/campaign/bidlist → campaignAssociateBidList

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/put-v3-campaign-bidlist
- Retrieved: 2026-11-14
- Category: REST_API

---

# PUT /v3/campaign/bidlist → campaignAssociateBidList

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `PUT /v3/campaign/bidlist` |
| GraphQL operation | `campaignAssociateBidList` |
| Input type | `CampaignAssociateBidListInput` |
| Output type | `PayloadWithErrorsOfCampaign` (`data: Campaign`, `userErrors: [UserError!]`) |

## Input field mapping

Input type: `CampaignAssociateBidListInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `CampaignId` | `campaignId` | ID! | Required | N/A |
| `AssociatedBidLists` | `bidListsToAddOrUpdate` | [BidListAddOrUpdateInput!] | Required | REST PUT replaces the full association set via `bidListsToAddOrUpdate`; may also need `bidListIdsToRemove` for removals |
| `AssociatedBidLists[].BidListId` | `bidListsToAddOrUpdate[].bidListId` | ID! | Required | N/A |
| `AssociatedBidLists[].IsEnabled` | `bidListsToAddOrUpdate[].isEnabled` | Boolean | Optional | N/A |
| `AssociatedBidLists[].IsDefaultForDimension` | N/A | Boolean | Optional | Not exposed on `BidListAddOrUpdateInput` |
| `AssociatedBidLists[].BidListSource` | N/A | BidListSource | Optional | Read-only |
| `AssociatedBidLists[].BidListAdjustmentType` | N/A | BidListAdjustmentType | Optional | Read-only |
| `AssociatedBidLists[].BidListDimensions` | N/A | [BidListDimension!] | Optional | Read-only |

## Output field mapping

Output type: `Campaign` (returned as `data` on `CampaignAssociateBidListPayload`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CampaignId` | `id` | ID! | Not nullable | N/A |
| `AssociatedBidLists` | `associatedBidLists` | AssociatedBidListsConnection | Nullable | N/A |
| `AssociatedBidLists[].BidListId` | `associatedBidLists.nodes[].bidList.id` | ID! | Not nullable | Via nested `bidList` on `AssociatedBidList` |
| `AssociatedBidLists[].IsEnabled` | `associatedBidLists.nodes[].isEnabled` | Boolean! | Not nullable | N/A |
| `AssociatedBidLists[].IsDefaultForDimension` | N/A | Boolean | Nullable | Not currently available in GraphQL |
| `AssociatedBidLists[].BidListSource` | `associatedBidLists.nodes[].bidList.source` | BidListSource! | Not nullable | N/A |
| `AssociatedBidLists[].BidListAdjustmentType` | `associatedBidLists.nodes[].bidList.adjustmentType` | BidListAdjustmentType! | Not nullable | N/A |
| `AssociatedBidLists[].BidListDimensions` | `associatedBidLists.nodes[].bidList.dimensions` | [BidListDimension!]! | Not nullable | N/A |

## Endpoint-specific nested types and enums

### BidListAddOrUpdateInput

Nested under `bidListsToAddOrUpdate`.

| GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- |
| `bidListId` | ID! | Required | REST `AssociatedBidLists[].BidListId` |
| `isEnabled` | Boolean | Optional | REST `AssociatedBidLists[].IsEnabled` |

## Code examples

### REST example

```
PUT /v3/campaign/bidlist HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "CampaignId": "camp123",
  "AssociatedBidLists": [
    { "BidListId": "bl456", "IsEnabled": true },
    { "BidListId": "bl789", "IsEnabled": false }
  ]
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
  campaignAssociateBidList(
    input: {
      campaignId: "camp123"
      bidListsToAddOrUpdate: [
        { bidListId: "bl456", isEnabled: true }
        { bidListId: "bl789", isEnabled: false }
      ]
    }
  ) {
    data {
      id
      associatedBidLists {
        nodes {
          bidList { id }
          isEnabled
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
