# GET /v3/campaign/bidlist/{campaignId} → Campaign.associatedBidLists

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-campaign-bidlist-campaignid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/campaign/bidlist/{campaignId} → Campaign.associatedBidLists

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/campaign/bidlist/{campaignId}` |
| GraphQL query | `Campaign.associatedBidLists` |
| Return type | `AssociatedBidListsConnection` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CampaignId` | `id` | ID! | Not nullable | Parent campaign ID on the queried `Campaign`. |
| `AssociatedBidLists[].BidListId` | `associatedBidLists.nodes[].bidList.id` | String! | Not nullable | Connection unwrapping via `nodes`. |
| `AssociatedBidLists[].IsEnabled` | `associatedBidLists.nodes[].isEnabled` | Boolean! | Not nullable | N/A |
| `AssociatedBidLists[].IsDefaultForDimension` | N/A | N/A | N/A | Not currently available in GraphQL |
| `AssociatedBidLists[].BidListSource` | `associatedBidLists.nodes[].bidList.source` | BidListSource! | Not nullable | N/A |
| `AssociatedBidLists[].BidListAdjustmentType` | `associatedBidLists.nodes[].bidList.adjustmentType` | BidListAdjustmentType! | Not nullable | N/A |
| `AssociatedBidLists[].BidListDimensions` | `associatedBidLists.nodes[].bidList.dimensions` | [BidListDimension!]! | Not nullable | N/A |

## Code examples

### REST example

```
GET /v3/campaign/bidlist/{campaignId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetCampaignBidLists($id: ID!) {
  campaign(id: $id) {
    id
    associatedBidLists {
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
