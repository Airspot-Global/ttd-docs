# POST /v3/nielsen/brand/query → Query.nielsenBrands

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-nielsen-brand-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/nielsen/brand/query → Query.nielsenBrands

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/nielsen/brand/query` |
| GraphQL query | `Query.nielsenBrands` |
| Return type | `NielsenBrand` connection |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |
| `SearchTerm` | `searchTerm` | String | Optional | Explicit argument; not a generic filter input. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [NielsenBrand!] | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].BrandCode` | `brandCode` | Long! | Not nullable | N/A |
| `Result[].BrandVariant` | `brandVariant` | String | Nullable | Brand name; nullable in GraphQL. REST strings may surface as null. |
| `Result[].BrandDesc` | `brandDesc` | String | Nullable | Brand description; nullable in GraphQL. REST strings may surface as null. |

## Endpoint-specific nested types and enums

### NielsenBrand

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `BrandCode` | `brandCode` | Long! | Not nullable | N/A |
| `BrandVariant` | `brandVariant` | String | Nullable | Brand name; nullable in GraphQL. |
| `BrandDesc` | `brandDesc` | String | Nullable | Brand description; nullable in GraphQL. |

## Code examples

### REST example

```
POST /v3/nielsen/brand/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "PageStartIndex": 0,
  "PageSize": 50,
  "SearchTerm": "Acme"
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query NielsenBrands {
  nielsenBrands(first: 50, searchTerm: "Acme") {
    nodes {
      brandCode
      brandVariant
      brandDesc
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```
