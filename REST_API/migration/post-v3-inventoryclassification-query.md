# POST /v3/inventoryclassification/query → Query.inventoryClassifications

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-inventoryclassification-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/inventoryclassification/query → Query.inventoryClassifications

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/inventoryclassification/query` |
| GraphQL query | `Query.inventoryClassifications` |
| Return type | `InventoryClassificationsConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `SearchTerm` | `input.searchTerm` on `Query.inventoryClassifications` | `String!` (within `InventoryClassificationQueryInput!`) | Required | Required filter (4–100 characters). Top-level query with no parent entity. |
| `PageStartIndex` | `after` | `String` | Optional | N/A |
| `PageSize` | `first` | `Int` | Optional | N/A |
| (entire request body) | `input` | `InventoryClassificationQueryInput!` | Required | Required argument on `Query.inventoryClassifications`. |

## Response field mapping

 | REST response field | GraphQL field | GraphQL type | Nullable | Notes | |---------------------|---------------|--------------|----------|-------| | `Result` | `nodes` | `[InventoryClassification!]` | Nullable | N/A | | `ResultCount` | N/A | N/A | N/A | N/A | | `TotalFilteredCount` | `totalCount` | `Int!` | Not nullable | N/A | | `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |

### InventoryClassification item

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result.DomainApp` | `domainApp` | `String!` | Not nullable | Domain or app identifier. |
| `Result.AdsTxtStatus` | `adsTxtStatus` | `Boolean!` | Not nullable | `true` = valid ads.txt scanned; `false` = absent, invalid, or unscannable. |
| `Result.IsBlocked` | `isBlocked` | `Boolean!` | Not nullable | Computed when blocked class count is greater than zero. |
| `Result.IsApp` | `isApp` | `Boolean!` | Not nullable | Whether the result represents a mobile app. |
| `Result.AppName` | `appName` | `String` | Nullable | Present only when `isApp` is `true` and a name is available. |
| `Result.DomainClasses` | `domainClasses` | `[String!]!` | Not nullable | Comma-separated domain classes split into an array. |

## Code examples

### REST example

```
POST /v3/inventoryclassification/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "SearchTerm": "example.com",
  "PageStartIndex": 0,
  "PageSize": 10
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query SearchInventory {
  inventoryClassifications(input: { searchTerm: "example.com" }, first: 10) {
    nodes {
      domainApp
      adsTxtStatus
      isBlocked
      isApp
      appName
      domainClasses
    }
    totalCount
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```
