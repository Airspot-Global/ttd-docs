# POST /v3/currency/query → Query.currencies

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-currency-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/currency/query → Query.currencies

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/currency/query` |
| GraphQL query | `Query.currencies` |
| Return type | `CurrenciesConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |
| `SearchTerms` | N/A | N/A | Optional | Not currently available in GraphQL |
| `SortFields` | N/A | N/A | Optional | Not currently available in GraphQL |
| `SortFields[].FieldId` | N/A | N/A | Optional | Not currently available in GraphQL |
| `SortFields[].Ascending` | N/A | N/A | Optional | Not currently available in GraphQL |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [Currency!] | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].CurrencyCode` | `Currency.id` | ID! | Not nullable | Enum in REST; ISO 4217 string as GraphQL `ID`. |
| `Result[].CurrencyName` | `Currency.name` | String! | Not nullable | GraphQL field is `@deprecated`—prefer `id` and infer client-side; still populated. |
| `Result[].CurrencyNamePlural` | `Currency.namePlural` | String! | Not nullable | GraphQL field is `@deprecated`—prefer `id` and infer client-side. |

## Endpoint-specific nested types and enums

### Currency

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CurrencyCode` | `id` | ID! | Not nullable | Enum in REST; ISO 4217 string as GraphQL `ID`. |
| `CurrencyName` | `name` | String! | Not nullable | `@deprecated` on GraphQL schema. |
| `CurrencyNamePlural` | `namePlural` | String! | Not nullable | `@deprecated` on GraphQL schema. |

Extra GraphQL-only `Currency` fields (`symbol`, `decimalPlaces`, `isVisible`, `currentExchangeRateFromUsd`) are available on the same entity but not in the REST `Currency` response.

### Sorting_CurrencySortingField

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `FieldId` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Ascending` | N/A | N/A | N/A | Defaults to ascending when omitted in REST. |

### CurrencySortingField (enum)

REST values: `Name`, `NamePlural`, `CurrencyCode`. Not currently available in GraphQL.

### CurrencyCode (enum)

REST uses ISO 4217 currency codes. GraphQL exposes currency identity as `Currency.id` (`ID!`) with string values such as `USD`, `EUR`, `GBP`.

## Code examples

### REST example

```
POST /v3/currency/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "PageStartIndex": 0,
  "PageSize": 100,
  "SearchTerms": ["USD"],
  "SortFields": [
    { "FieldId": "Name", "Ascending": true }
  ]
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query Currencies {
  currencies(first: 100) {
    nodes {
      id
      name
      namePlural
      symbol
      decimalPlaces
    }
    totalCount
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```
