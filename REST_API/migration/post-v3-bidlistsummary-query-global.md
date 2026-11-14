# POST /v3/bidlistsummary/query/global → Query.globalBidLists

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-bidlistsummary-query-global
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/bidlistsummary/query/global → Query.globalBidLists

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/bidlistsummary/query/global` |
| GraphQL query | `Query.globalBidLists` |
| Return type | `GlobalBidListsConnection` |

## Request and filter field mapping

Input type: `GlobalBidListQuery` (five filter fields; no `EntityId`, `MaximumLevel`, or `ReturnOnlyEnabledBidLists`).

| REST request field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |
| `BidListIds` | `where.id` | LongOperationFilterInput | Optional | Filter to specific bid list IDs |
| `DimensionDescriptorFilters` | `where.dimensions` | DimensionsFilterInput | Optional | Filter by bid list dimensions |
| `ReturnBidListsUnavailableForLibraryUse` | `where.isAvailableForLibraryUse` | BooleanOperationFilterInput | Optional | When `false` (default), excludes lists unavailable for library use |

## Response field mapping

Connection nodes are `IBidList` objects. This endpoint returns `BidListSummary` rows with no per-row association metadata.

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [IBidList!] | Nullable | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `BidListId` | `nodes.id` | ID! | Not nullable | N/A |
| `Name` | `nodes.name` | String! | Not nullable | N/A |
| `BidListSource` | `nodes.source` | BidListSource! | Not nullable | N/A |
| `BidListAdjustmentType` | `nodes.adjustmentType` | BidListAdjustmentType! | Not nullable | N/A |
| `ResolutionType` | `nodes.resolutionType` | MultipleMatchResolutionType! | Not nullable | N/A |
| `BidLinesCount` | `nodes.bidLinesCount` | Int! | Not nullable | N/A |
| `BidListOwner` | `nodes.ownerType` | BidListOwnerType! | Not nullable | N/A |
| `BidListOwnerId` | `nodes.owner` | BidListOwner | Nullable | Union |
| `IsGlobal` | N/A | N/A | N/A | **Not currently available in GraphQL** |
| `IsDeleted` | N/A | N/A | N/A | **Not currently available in GraphQL** |
| `BidListDimensions` | `nodes.dimensions` | [BidListDimension!]! | Not nullable | N/A |
| `IsAvailableForLibraryUse` | `nodes.isAvailableForLibraryUse` | Boolean! | Not nullable | N/A |

## Code examples

### REST example

```
POST /v3/bidlistsummary/query/global HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "PageStartIndex": 0,
  "PageSize": 25
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GlobalBidLists($first: Int) {
  globalBidLists(first: $first) {
    nodes { id name source dimensions ownerType }
    totalCount
    pageInfo { hasNextPage endCursor }
  }
}
```
