# POST /v3/delta/bidlist/query/partner → Partner.bidListDelta(input: BidListDeltaByPartnerInput)

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-delta-bidlist-query-partner
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/delta/bidlist/query/partner → Partner.bidListDelta(input: BidListDeltaByPartnerInput)

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/delta/bidlist/query/partner` |
| GraphQL query | `Partner.bidListDelta(input: BidListDeltaByPartnerInput)` |
| Return type | `BidListDelta` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PartnerId` | Parent: `Partner.bidListDelta` (relationship field) | N/A | Optional | Injected from `partner(id:)` parent at resolution time; omit from `input`. |
| `LastChangeTrackingVersion` | `input.lastChangeId` | ID | Optional | String form of the REST tracking version. Pass null or omit for the latest change ID. |
| `ReturnEntireBidList` | N/A | N/A | Optional | Not currently available in GraphQL |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `LastChangeTrackingVersion` | `nextChangeTrackingVersion` | Long! | Not nullable | Use the string form as `input.lastChangeId` on the next delta call. |
| `ElementIds` | `changedBidLists[].bidList.id` | ID! | Not nullable | Derive IDs from `changedBidLists { bidList { id } }` when not selecting full bid list fields. |
| `BidLists` | `changedBidLists` | [BidListDeltaEntry!]! | Not nullable | Each entry wraps a `BidList` entity reference plus optional `isDeleted`. |
| `MoreBidListsAvailable` | `moreBidListsAvailable` | Boolean | Nullable | True when additional changed bid lists exist beyond this page. |

## Endpoint-specific nested types and enums

### BidListDeltaEntry

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `BidLists[].IsDeleted` | `isDeleted` | Boolean | Nullable | True when the bid list was deleted; null when REST returned IDs only. |
| `BidLists[].BidListId` | `bidList.id` | ID! | Not nullable | Entity reference to the changed bid list. |

### BidList (via `changedBidLists[].bidList`)

| REST field (BidListSummary) | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| BidListId | `id` | ID! | Not nullable | N/A |
| Name | `name` | String! | Not nullable | N/A |
| BidListSource | `source` | BidListSource! | Not nullable | N/A |
| BidListAdjustmentType | `adjustmentType` | BidListAdjustmentType! | Not nullable | N/A |
| ResolutionType | `resolutionType` | MultipleMatchResolutionType! | Not nullable | N/A |
| BidLinesCount | `bidLinesCount` | Int! | Not nullable | N/A |
| BidListOwner | `ownerType` | BidListOwnerType! | Not nullable | REST `BidListOwner` enum → `ownerType`. |
| BidListOwnerId | `owner` | BidListOwner | Nullable | Entity reference for the owning partner/advertiser/campaign/ad group. |
| IsGlobal | N/A | N/A | N/A | Not currently available in GraphQL |
| IsDeleted | `isDeleted` | Boolean | Nullable | On parent `BidListDeltaEntry`, not on `BidList`. |
| BidListDimensions | `dimensions` | [BidListDimension!]! | Not nullable | N/A |
| IsAvailableForLibraryUse | `isAvailableForLibraryUse` | Boolean! | Not nullable | N/A |

## Code examples

The following are examples of querying partner bid list deltas with REST and GraphQL.

Basic delta query:

### REST example

```
POST /v3/delta/bidlist/query/partner HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "PartnerId": "partner789",
  "LastChangeTrackingVersion": null,
  "ReturnEntireBidList": false
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query BidListDeltaByPartner {
  partner(id: "partner789") {
    bidListDelta(input: {}) {
      nextChangeTrackingVersion
      moreBidListsAvailable
      changedBidLists {
        isDeleted
        bidList {
          id
        }
      }
    }
  }
}
```

Full bid list summary fields:

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query BidListDeltaWithSummaries {
  partner(id: "partner789") {
    bidListDelta(input: {
      lastChangeId: "100"
    }) {
      nextChangeTrackingVersion
      moreBidListsAvailable
      changedBidLists {
        isDeleted
        bidList {
          id
          name
          source
          adjustmentType
          resolutionType
          bidLinesCount
          dimensions
          isAvailableForLibraryUse
          ownerType
        }
      }
    }
  }
}
```
