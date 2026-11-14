# POST /v3/adtechnology/query → Query.adTechnologies

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-adtechnology-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/adtechnology/query → Query.adTechnologies

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/adtechnology/query` |
| GraphQL query | `Query.adTechnologies` |
| Return type | `AdTechnologiesConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `SearchTerms` | `AdTechnologyQueryInput.searchTerms` | `[String!]` | Optional | Filter argument on the top-level query. |
| `SortFields` | `AdTechnologyQueryInput.sortFields` | `[AdTechnologySortingFieldSortingInput!]` | Optional | Sort argument on the top-level query. |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [AdTechnology!] | Nullable | N/A |
| `Result[].AdTechnologyId` | `AdTechnology.id` | ID! | Not nullable | `string` → `ID`. |
| `Result[].AdTechnologyName` | `AdTechnology.name` | String! | Not nullable | Ad technology display name. |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |

## Endpoint-specific nested types and enums

### AdTechnology

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdTechnologyId` | `id` | ID! | Not nullable | N/A |
| `AdTechnologyName` | `name` | String! | Not nullable | N/A |

### AdTechnologySortingFieldSortingInput

| Field | GraphQL type | Required | Notes |
| --- | --- | --- | --- |
| fieldId | AdTechnologySortingFieldInput! | Required | Sort field to apply. |
| ascending | Boolean | Optional | Sort direction; omit for default ordering. |

### AdTechnologySortingFieldInput

| Enum value | Notes |
| --- | --- |
| `NAME` | Sort by ad technology name. |

## Code examples

### REST example

```
POST /v3/adtechnology/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "SearchTerms": ["google"],
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
query LegacyAdTechnologies {
  adTechnologies(first: 20, filter: { searchTerms: ["google"] }) {
    nodes {
      id
      name
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```
