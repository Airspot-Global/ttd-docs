# PUT /v3/adgroup/bidlist → adGroupAssociateBidListBatch

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/put-v3-adgroup-bidlist
- Retrieved: 2026-11-14
- Category: REST_API

---

# PUT /v3/adgroup/bidlist → adGroupAssociateBidListBatch

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `PUT /v3/adgroup/bidlist` |
| GraphQL operation | `adGroupAssociateBidListBatch` |
| Input type | `AdGroupWithAssociatedBidLists` (REST request body) |
| Output type | `AdGroupAssociateBidListBatchPayload` (`data: [AdGroup!]`, `errors: [AdGroupAssociateBidListBatchMutationError!]`) |

## Multi-step operations

REST `PUT /v3/adgroup/bidlist` completely replaces the ad group's associated bid-list set in one call. GraphQL `adGroupAssociateBidListBatch` **merges** into existing associations when called with only `bidListsToAddOrUpdate`—unlisted associations remain attached.

To achieve REST full-replace semantics:

1. **Read** current associations via `adGroup(id: …) { associatedBidLists { nodes { bidList { id } } } }`.
2. **Compute removals:** for each bid list ID currently associated but omitted from the REST body's `AssociatedBidLists`, include it in `bidListIdsToRemove`.
3. **Write** via `adGroupAssociateBidListBatch` with `bidListsToAddOrUpdate` for the target set and `bidListIdsToRemove` for the computed removals.

`toReplace` on `AdGroupAssociateBidListInput` removes associations whose dimension descriptor and adjustment type match the rule—not the entire association set. Use it only for dimension-scoped replacement, not as a substitute for REST PUT full-replace.

| Step | GraphQL operation | Purpose |
| --- | --- | --- |
| 1 | `Query.adGroup` | Read `associatedBidLists.nodes[].bidList.id` to discover current associations |
| 2 | `Mutation.adGroupAssociateBidListBatch` | Apply `bidListsToAddOrUpdate` + `bidListIdsToRemove` to match REST full-replace |

## Input field mapping

Input type: `AdGroupAssociateBidListBatchInput` → `adGroupAssociates[]` of `AdGroupAssociateBidListInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdGroupId` | `adGroupAssociates[].adGroupId` | ID! | Required | Single REST object maps to one element in `adGroupAssociates` |
| `AssociatedBidLists` | `adGroupAssociates[].bidListsToAddOrUpdate` | [AdGroupBidListAddOrUpdateInput!] | Required | Desired final associations (add or update flags) |
| N/A | `adGroupAssociates[].bidListIdsToRemove` | [ID!] | Optional | Not in REST body; supply IDs of currently associated lists omitted from `AssociatedBidLists` (see Multi-Step Operations) |
| `AssociatedBidLists[].BidListId` | `bidListsToAddOrUpdate[].bidListId` | ID! | Required | N/A |
| `AssociatedBidLists[].IsEnabled` | `bidListsToAddOrUpdate[].isEnabled` | Boolean | Optional | N/A |
| `AssociatedBidLists[].IsDefaultForDimension` | `bidListsToAddOrUpdate[].isDefault` | Boolean | Optional | REST `IsDefaultForDimension` → GraphQL `isDefault` |
| `AssociatedBidLists[].BidListSource` | N/A | N/A | Optional | Read-only |
| `AssociatedBidLists[].BidListAdjustmentType` | N/A | N/A | Optional | Set on bid list create/update, not on association |
| `AssociatedBidLists[].BidListDimensions` | N/A | N/A | Optional | Set on bid list create/update |

## Output field mapping

Output type: `[AdGroup!]` (returned as `data` on `AdGroupAssociateBidListBatchPayload`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdGroupId` | `data[].id` | ID! | Not nullable | Batch returns one `AdGroup` per `adGroupAssociates` entry |
| `AssociatedBidLists` | `data[].associatedBidLists.nodes` | [AdGroupAssociatedBidList!] | Nullable | See domain page **AssociatedBidList** nested mapping; parent `associatedBidLists` is nullable on `AdGroup` |

## Code examples

### Example—PUT bidlist (full-replace associations)

Assume the ad group currently has `bl_002` and `bl_003` associated. REST PUT replaces the entire set with only `bl_001`.

### REST example

```
PUT /v3/adgroup/bidlist HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdGroupId": "ag_xyz789",
  "AssociatedBidLists": [
    { "BidListId": "bl_001", "IsEnabled": true, "IsDefaultForDimension": false }
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
# Step 1: read current associations to compute removals
query CurrentAdGroupBidLists {
  adGroup(id: "ag_xyz789") {
    associatedBidLists(first: 100) {
      nodes {
        bidList { id }
      }
    }
  }
}

# Step 2: full-replace—add/update target set and remove omitted lists
mutation ReplaceAdGroupBidLists {
  adGroupAssociateBidListBatch(input: {
    adGroupAssociates: [
      {
        adGroupId: "ag_xyz789"
        bidListsToAddOrUpdate: [
          { bidListId: "bl_001", isEnabled: true, isDefault: false }
        ]
        bidListIdsToRemove: ["bl_002", "bl_003"]
      }
    ]
  }) {
    data {
      id
      associatedBidLists(first: 10) {
        nodes {
          isEnabled
          isDefaultForUI
          bidList { id adjustmentType }
        }
      }
    }
    errors {
      ... on BidListAssociationInvalidBidListError {
        message
        field
      }
      ... on BidListAssociationAdGroupArchivedError {
        message
        field
      }
      ... on BidListAssociationNoAdGroupError {
        message
        field
      }
    }
  }
}
```
