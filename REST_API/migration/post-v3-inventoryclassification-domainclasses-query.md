# POST /v3/inventoryclassification/domainclasses/query → Query.domainClasses

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-inventoryclassification-domainclasses-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/inventoryclassification/domainclasses/query → Query.domainClasses

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/inventoryclassification/domainclasses/query` |
| GraphQL query | `Query.domainClasses` |
| Return type | `DomainClassesConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `SearchTerm` | `input.searchTerm` on `Query.domainClasses` | `String` (within `DomainClassQueryInput!`) | Optional | Optional search term (4–256 characters) filtering by domain class name. |
| `PageStartIndex` | `after` | `String` | Optional | N/A |
| `PageSize` | `first` | `Int` | Optional | N/A |
| (entire request body) | `input` | `DomainClassQueryInput!` | Required | Required argument on `Query.domainClasses`; pass `{}` when no filter is needed. |

## Response field mapping

 | REST response field | GraphQL field | GraphQL type | Nullable | Notes | |---------------------|---------------|--------------|----------|-------| | `Result` | `nodes` | `[DomainClass!]` | Nullable | N/A | | `ResultCount` | N/A | N/A | N/A | N/A | | `TotalFilteredCount` | `totalCount` | `Int!` | Not nullable | N/A | | `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |

### DomainClass item

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result.Name` | `name` | `String` | Nullable | Display name. REST `Name` maps to the short description column. Nullable in schema; populated when resolved via `domainClasses`. |
| `Result.Description` | `description` | `String` | Nullable | Long description. REST `Description` maps to the long description column. Nullable in schema; populated when resolved via `domainClasses`. |

## Code examples

### REST example

```
POST /v3/inventoryclassification/domainclasses/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
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
query SearchDomainClasses {
  domainClasses(input: {}, first: 10) {
    nodes {
      id
      name
      description
    }
    totalCount
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```
