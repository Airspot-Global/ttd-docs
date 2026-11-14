# GET /v3/interesttargeting/query → Query.interestTargetingCategories

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-interesttargeting-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/interesttargeting/query → Query.interestTargetingCategories

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/interesttargeting/query` |
| GraphQL query | `Query.interestTargetingCategories` |
| Return type | `[InterestTargetingCategory!]!` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `interestTargetingCategories` | [InterestTargetingCategory!]! | Not nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | N/A | N/A | N/A | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].CategoryId` | `categoryId` | ID! | Not nullable | Non-null per REST `isOptional: false`. |
| `Result[].CategoryName` | `categoryName` | String | Nullable | Nullable per REST `isOptional: true`. |

## Endpoint-specific nested types and enums

### InterestTargetingCategory

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CategoryId` | `categoryId` | ID! | Not nullable | Non-null per REST `isOptional: false`. |
| `CategoryName` | `categoryName` | String | Nullable | Nullable per REST `isOptional: true`. |

## Code examples

### REST example

```
GET /v3/interesttargeting/query HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query InterestTargetingCategories {
  interestTargetingCategories {
    categoryId
    categoryName
  }
}
```
