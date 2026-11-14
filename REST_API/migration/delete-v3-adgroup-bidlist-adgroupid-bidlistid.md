# DELETE /v3/adgroup/bidlist/{adGroupId}/{bidListId} → adGroupAssociateBidList

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/delete-v3-adgroup-bidlist-adgroupid-bidlistid
- Retrieved: 2026-11-14
- Category: REST_API

---

# DELETE /v3/adgroup/bidlist/{adGroupId}/{bidListId} → adGroupAssociateBidList

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `DELETE /v3/adgroup/bidlist/{adGroupId}/{bidListId}` |
| GraphQL operation | `adGroupAssociateBidList` |
| Input type | `AdGroupAssociateBidListInput` |
| Output type | `PayloadWithErrorsOfAdGroup` (`data: AdGroup`, `userErrors: [UserError!]!`) |

## Input field mapping

Input type: `AdGroupAssociateBidListInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `path:adGroupId` | `adGroupId` | ID! | Required | REST path parameter |
| `path:bidListId` | `bidListIdsToRemove` | [ID!] | Required | Pass the path `bidListId` as a single-element list |

## Output field mapping

Output type: `AdGroup` (returned as `data` on `PayloadWithErrorsOfAdGroup`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdGroupId` | `id` | ID! | Not nullable | N/A |
| `AssociatedBidLists` | `associatedBidLists.nodes` | `[AdGroupAssociatedBidList!]` | Nullable | See domain page for node field mapping |

## Code examples

### Example—DELETE bid list association

### REST example

```
DELETE /v3/adgroup/bidlist/ag_xyz789/bl_456 HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation DisassociateBidList {
  adGroupAssociateBidList(input: {
    adGroupId: "ag_xyz789"
    bidListIdsToRemove: ["bl_456"]
  }) {
    data {
      id
      associatedBidLists(first: 10) {
        nodes {
          isEnabled
          isDefaultForUI
          bidList {
            id
            source
            adjustmentType
          }
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
