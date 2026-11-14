# GET /v3/bidlist/{bidListId} → Query.bidList(id:)

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-bidlist-bidlistid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/bidlist/{bidListId} → Query.bidList(id:)

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/bidlist/{bidListId}` |
| GraphQL query | `Query.bidList(id:)` |
| Return type | `IBidList` |

## Multi-step operations

This REST GET is fully covered by an existing GraphQL query. Call `bidList(id:)` directly. The return type is the `IBidList` interface (`BidList` is one concrete implementer).

| REST endpoint | GraphQL equivalent | Notes |
| --- | --- | --- |
| `GET /v3/bidlist/{bidListId}` | `Query.bidList(id:)` | Single bid list with bid lines |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `BidListId` | `id` | ID! | Not nullable | N/A |
| `Name` | `name` | String! | Not nullable | N/A |
| `BidListSource` | `source` | BidListSource! | Not nullable | N/A |
| `BidListAdjustmentType` | `adjustmentType` | BidListAdjustmentType! | Not nullable | N/A |
| `ResolutionType` | `resolutionType` | MultipleMatchResolutionType! | Not nullable | N/A |
| `BidLines` | `bidLines` | [BidLine!]! | Not nullable | Plain list, not a connection |
| `BidListOwner` | `ownerType` | BidListOwnerType! | Not nullable | N/A |
| `BidListOwnerId` | `owner` | BidListOwner | Nullable | Union; resolve `id` via inline fragment on the member type |
| `IsAvailableForLibraryUse` | `isAvailableForLibraryUse` | Boolean! | Not nullable | N/A |
| `BidListDimensions` | `dimensions` | [BidListDimension!]! | Not nullable | N/A |
| `IsGlobal` | N/A | N/A | N/A | **Not currently available in GraphQL** |
| `BidListType` | `volumeControlOnly` | Boolean! | Not nullable | REST `VolumeControl` → `true`; `BidAdjustment` → `false` |
| N/A | `bidLinesCount` | Int! | Not nullable | Available on `IBidList`; not a separate REST field on `BidListResult` |
| N/A | `dimensionDescriptorId` | Long! | Not nullable | Available on `IBidList` |
| N/A | `activeBidLineBatchId` | Long | Nullable | Available on `IBidList` |
| N/A | `lastUpdateDate` | DateTime | Nullable | Available on `IBidList` |

## Code examples

### REST example

```
GET /v3/bidlist/{bidListId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query OneBidList($id: ID!) {
  bidList(id: $id) {
    id
    name
    source
    adjustmentType
    dimensions
    bidLines { bidAdjustment domainFragment }
    bidLinesCount
    ownerType
    owner {
      __typename
      ... on AdGroup { id }
      ... on Campaign { id }
      ... on Advertiser { id }
      ... on Partner { id }
    }
  }
}
```
