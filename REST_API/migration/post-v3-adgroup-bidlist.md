# POST /v3/adgroup/bidlist → bidListCreate + adGroupAssociateBidList

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-adgroup-bidlist
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/adgroup/bidlist → bidListCreate + adGroupAssociateBidList

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/adgroup/bidlist` |
| GraphQL operation | `bidListCreate` + `adGroupAssociateBidList` |
| Input type | `AdGroupBidList` (REST request body) |
| Output type | `PayloadWithErrorsOfAdGroup` (`data: AdGroup`, `userErrors: [UserError!]!`) |

## Multi-step operations

One REST call maps to two GraphQL mutations when the bid list does not yet exist: create the bid list (`bidListCreate`), then associate it with the ad group (`adGroupAssociateBidList`). If the bid list already exists, use `bidListSet` (update) instead of `bidListCreate`, then `adGroupAssociateBidList`. Run both in order.

## Input field mapping

### Step 1—`bidListCreate` (when creating a new bid list)

Input type: `BidListCreateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `BidList.BidListId` | N/A | N/A | Optional | Omit on create; REST ignores on POST |
| BidList (new list body) | name, owner, dimensions, bidLines, … | BidListCreateInput fields | Required | See BidList domain page for `BidListCreateInput` mapping |
| `BidList.IsEnabled` | N/A | N/A | Optional | Set via `adGroupAssociateBidList` (`isEnabled` on `AdGroupBidListAddOrUpdateInput`) |
| `BidList.IsDefaultForDimension` | N/A | N/A | Optional | Set via `adGroupAssociateBidList` (`isDefault`) |
| `BidList.BidListAdjustmentType` | `adjustmentType` | BidListAdjustmentType! | Required | On `BidListCreateInput` |
| `BidList.BidListDimensions` | `dimensions` | [BidListDimension!]! | Required | On `BidListCreateInput` |

### Step 2—`adGroupAssociateBidList`

Input type: `AdGroupAssociateBidListInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdGroupId` | `adGroupId` | ID! | Required | N/A |
| `BidList.BidListId` | `bidListsToAddOrUpdate[].bidListId` | ID! | Required | Use ID returned from step 1 when creating |
| `BidList.IsEnabled` | `bidListsToAddOrUpdate[].isEnabled` | Boolean | Optional | N/A |
| `BidList.IsDefaultForDimension` | `bidListsToAddOrUpdate[].isDefault` | Boolean | Optional | REST `IsDefaultForDimension` → GraphQL `isDefault` |
| `BidList.BidListSource` | N/A | N/A | Optional | Read-only |
| `BidList.BidListAdjustmentType` | N/A | N/A | Optional | Immutable after bid list creation |
| `BidList.BidListDimensions` | N/A | N/A | Optional | Set on create via `dimensions` |

## Output field mapping

Output type: `AdGroup` (returned as `data` on `PayloadWithErrorsOfAdGroup` from step 2)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdGroupId` | `id` | ID! | Not nullable | N/A |
| `AssociatedBidLists` | `associatedBidLists.nodes` | `[AdGroupAssociatedBidList!]` | Nullable | See domain page **AssociatedBidList** nested mapping |

## Code examples

### Example—POST bidlist (create + associate)

### REST example

```
POST /v3/adgroup/bidlist HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdGroupId": "ag_xyz789",
  "BidList": {
    "BidListAdjustmentType": "Optimized",
    "BidListDimensions": ["HasDomainFragmentId"],
    "IsEnabled": true
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
mutation CreateAndAssociateBidList {
  # Step 1: create the bid list
  bidListCreate(input: {
    name: "Site/App Target List"
    adjustmentType: OPTIMIZED
    resolutionType: APPLY_MULTIPLY_ADJUSTMENT
    source: USER
    owner: { adGroupId: "ag_xyz789" }
    associateBehavior: DO_NOT_ASSOCIATE
    dimensions: [HAS_DOMAIN_FRAGMENT_ID]
    isAvailableForLibraryUse: false
    bidLines: [
      {
        bidAdjustment: 1.0
        domainFragment: "example.com"
        volumeControlPriority: NEUTRAL
      }
    ]
  }) {
    data { id }
    userErrors { message field }
  }

  # Step 2: associate with the ad group
  adGroupAssociateBidList(input: {
    adGroupId: "ag_xyz789"
    bidListsToAddOrUpdate: [
      { bidListId: "bl_new_id", isEnabled: true }
    ]
  }) {
    data {
      id
      associatedBidLists(first: 10) {
        nodes {
          isEnabled
          isDefaultForUI
          bidList { id source adjustmentType }
        }
      }
    }
    userErrors { message field }
  }
}
```
