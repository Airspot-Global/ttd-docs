# DELETE /v3/campaign/bidlist → campaignAssociateBidList

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/delete-v3-campaign-bidlist
- Retrieved: 2026-11-14
- Category: REST_API

---

# DELETE /v3/campaign/bidlist → campaignAssociateBidList

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `DELETE /v3/campaign/bidlist` |
| GraphQL operation | `campaignAssociateBidList` |
| Input type | `CampaignAssociateBidListInput` |
| Output type | `PayloadWithErrorsOfCampaign` (`data: Campaign`, `userErrors: [UserError!]`) |

## Input field mapping

Input type: `CampaignAssociateBidListInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `CampaignId` | `campaignId` | ID! | Required | N/A |
| `BidList` | `bidListIdsToRemove` | [ID!] | Required | REST `BidList` nested object maps to one ID in `bidListIdsToRemove` |
| `BidList.BidListId` | `bidListIdsToRemove[]` | ID! | Required | N/A |
| `BidList.IsEnabled` | N/A | Boolean | Optional | Not used on DELETE |
| `BidList.IsDefaultForDimension` | N/A | Boolean | Optional | Not used on DELETE |
| `BidList.BidListSource` | N/A | BidListSource | Optional | Not used on DELETE |
| `BidList.BidListAdjustmentType` | N/A | BidListAdjustmentType | Optional | Not used on DELETE |
| `BidList.BidListDimensions` | N/A | [BidListDimension!] | Optional | Not used on DELETE |

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

## Code examples

### REST example

```
DELETE /v3/campaign/bidlist HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "CampaignId": "camp123",
  "BidList": {
    "BidListId": "bl456"
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
  campaignAssociateBidList(
    input: {
      campaignId: "camp123"
      bidListIdsToRemove: ["bl456"]
    }
  ) {
    data {
      id
      associatedBidLists {
        nodes {
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
