# POST /v3/supplypathoptimizationlist/query/advertiser → Advertiser.supplyPathOptimizationLists

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-supplypathoptimizationlist-query-advertiser
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/supplypathoptimizationlist/query/advertiser → Advertiser.supplyPathOptimizationLists

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/supplypathoptimizationlist/query/advertiser` |
| GraphQL query | `Advertiser.supplyPathOptimizationLists` |
| Return type | `SupplyPathOptimizationListsConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | Parent: `advertiser(id:)` | ID! | Required | Advertiser context is supplied from the parent `Advertiser` entity—not exposed as a GraphQL argument. |
| `PartnerId` | `filter.partnerId` | ID | Optional | Optional partner filter inside `SupplyPathOptimizationListsByAdvertiserInput`. |
| `SearchTerms` | `filter.searchTerms` | [String!] | Optional | Optional name search inside `SupplyPathOptimizationListsByAdvertiserInput`. |
| `SupplyPathOptimizationListFilter` | `filter.supplyPathOptimizationListFilter` | SupplyPathOptimizationListFilterInput | Optional | Scope filter: advertiser-only, partner-only, global-only, or all lists. |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | SupplyPathOptimizationList | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].SupplyPathOptimizationListId` | `SupplyPathOptimizationList.id` | ID! | Not nullable | N/A |
| `Result[].SupplyPathOptimizationListName` | `SupplyPathOptimizationList.name` | String | Nullable | N/A |
| `Result[].AdvertiserId` | `SupplyPathOptimizationList.advertiser` | Advertiser | Nullable | Entity reference; select `advertiser { id }` for the identifier. |
| `Result[].PartnerId` | `SupplyPathOptimizationList.partner` | Partner | Nullable | Entity reference; select `partner { id }` for the identifier. |
| `Result[].CurrentCount` | `SupplyPathOptimizationList.currentCount` | Int | Nullable | N/A |
| `Result[].MaxCount` | `SupplyPathOptimizationList.maxCount` | Int | Nullable | N/A |
| `Result[].ListItems` | N/A | N/A | N/A | Query response returns an empty list; items are available via the detail GET or `node.items`. |

## Endpoint-specific nested types and enums

### SupplyPathOptimizationList

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `SupplyPathOptimizationListId` | `id` | ID! | Not nullable | N/A |
| `SupplyPathOptimizationListName` | `name` | String | Nullable | N/A |
| `AdvertiserId` | `advertiser` | Advertiser | Nullable | Entity reference; select `advertiser { id }` for the identifier. |
| `PartnerId` | `partner` | Partner | Nullable | Entity reference; select `partner { id }` for the identifier. |
| `CurrentCount` | `currentCount` | Int | Nullable | N/A |
| `MaxCount` | `maxCount` | Int | Nullable | N/A |

## Code examples

### REST example

```
POST /v3/supplypathoptimizationlist/query/advertiser HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserId": "<advertiser-id>",
  "SupplyPathOptimizationListFilter": "AdvertiserOnly",
  "PageStartIndex": 0,
  "PageSize": 20
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetAdvertiserSPOLists($advertiserId: ID!, $first: Int, $after: String) {
  advertiser(id: $advertiserId) {
    supplyPathOptimizationLists(
      first: $first
      after: $after
      filter: { supplyPathOptimizationListFilter: ADVERTISER_ONLY }
    ) {
      totalCount
      pageInfo { hasNextPage endCursor }
      edges {
        node {
          id
          name
          currentCount
          maxCount
        }
      }
    }
  }
}
```
