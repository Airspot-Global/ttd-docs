# POST /v3/bidlistsummary/query/advertiser/available → Advertiser.availableBidLists

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-bidlistsummary-query-advertiser-available
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/bidlistsummary/query/advertiser/available → Advertiser.availableBidLists

> **NOTE**: Deprecated on REST. Prefer `Advertiser.associatedBidLists` for associated bid lists and `Advertiser.ownedBidLists` for owned bid lists.

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/bidlistsummary/query/advertiser/available` |
| GraphQL query | `Advertiser.availableBidLists` |
| Return type | `AdvertiserAvailableBidListConnection` |

## Multi-step operations

| REST endpoint | GraphQL equivalent | Notes |
| --- | --- | --- |
| `POST /v3/bidlistsummary/query/advertiser/available` | `Advertiser.availableBidLists` | Paged list of bid lists available to associate with the advertiser |

## Request and filter field mapping

| REST request field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `EntityId` | `advertiser(id: $advertiserId)` | ID! | Required | Parent entity; not a field on `availableBidLists` |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |
| `MaximumLevel` | N/A | N/A | N/A | Not applicable at advertiser scope; hierarchy is built into the resolver |
| `ReturnOnlyEnabledBidLists` | `where.isAssociated` | BooleanOperationFilterInput | Optional | When `true`, filter to bid lists already associated and enabled |
| `ReturnBidListsUnavailableForLibraryUse` | `where.bidList.isAvailableForLibraryUse` | BooleanOperationFilterInput | Optional | When `false` (default), excludes lists unavailable for library use |
| `BidListIds` | `where.bidList.id` | LongOperationFilterInput | Optional | Filter to specific bid list IDs |
| `DimensionDescriptorFilters` | `where.bidList.dimensions` | DimensionsFilterInput | Optional | Filter by bid list dimensions |

## Response field mapping

Connection nodes are `IBidList` objects. Per-row association metadata is on `edges.associatedEntity`.

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [IBidList!] | Nullable | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `AssociatedBidListsEntity` | `edges.associatedEntity` (via `__typename`) | AdvertiserAvailableBidListAssociatedEntity | Nullable | Union of `Advertiser`, `Partner`; null when not yet associated |
| `AssociatedBidListsEntityId` | `edges.associatedEntity.id` | ID | Nullable | Resolve via inline fragment on the union member |
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
POST /v3/bidlistsummary/query/advertiser/available HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "EntityId": "abc123",
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
query Available($advertiserId: ID!, $first: Int) {
  advertiser(id: $advertiserId) {
    availableBidLists(first: $first) {
      nodes { id name source dimensions }
      edges {
        associatedEntity {
          __typename
          ... on Advertiser { id }
          ... on Partner { id }
        }
      }
      totalCount
      pageInfo { hasNextPage endCursor }
    }
  }
}
```
