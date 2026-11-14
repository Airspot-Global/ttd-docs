# POST /v3/ispot/brand/query → Query.incrementalReachProvider.brands

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-ispot-brand-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/ispot/brand/query → Query.incrementalReachProvider.brands

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/ispot/brand/query` |
| GraphQL query | `Query.incrementalReachProvider.brands` |
| Return type | `IncrementalReachBrandConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |
| `SearchTerm` | `where: { name: { contains: "..." } }` on `brands` | IncrementalReachBrandFilterInput | Optional | Omit or leave empty to skip name filter (same as REST null/empty). |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [IncrementalReachBrand!] | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `BrandId` | `IncrementalReachBrand.id` | ID! | Not nullable | External `iSpot` brand ID. |
| `BrandName` | `IncrementalReachBrand.name` | String! | Not nullable | Brand display name. |

## Endpoint-specific nested types and enums

### IncrementalReachBrand

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `BrandId` | `id` | ID! | Not nullable | External `iSpot` brand ID. |
| `BrandName` | `name` | String! | Not nullable | Brand display name. |

## Code examples

### REST example

```
POST /v3/ispot/brand/query HTTP/1.1
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
query ISpotBrands {
  incrementalReachProvider(provider: I_SPOT) {
    brands(first: 50, where: { name: { contains: "Acme" } }) {
      nodes {
        id
        name
      }
      totalCount
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
}
```
