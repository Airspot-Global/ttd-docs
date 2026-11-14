# POST /v3/geoelement/nielsendma/query → Query.nielsenDmaGeoElements

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-geoelement-nielsendma-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/geoelement/nielsendma/query → Query.nielsenDmaGeoElements

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/geoelement/nielsendma/query` |
| GraphQL query | `Query.nielsenDmaGeoElements` |
| Return type | `NielsenDmaGeoElementsConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |
| `IncludeDeprecated` | `includeDeprecated` | Boolean | Optional | N/A |
| `SearchTerms` | `searchTerms` | [String!] | Optional | N/A |
| `SortFields` | `sortFields` | [NielsenDmaGeoElementSortingFieldSortInput!] | Optional | N/A |
| `SortFields[].FieldId` | `sortFields[].fieldId` | NielsenDmaGeoElementSortingFieldInput! | Required | REST enum values `NielsenDmaCode`, `NielsenDmaName` map to `NIELSEN_DMA_CODE`, `NIELSEN_DMA_NAME` |
| `SortFields[].Ascending` | `sortFields[].ascending` | Boolean | Optional | N/A |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [NielsenDmaGeoElement!] | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].GeoElementId` | `id` | ID! | Not nullable | GeoElementId → `id` |
| `Result[].IsDeprecated` | `isDeprecated` | Boolean | Nullable | N/A |
| `Result[].NielsenDmaCode` | `nielsenDmaCode` | String | Nullable | N/A |
| `Result[].NielsenDmaName` | `nielsenDmaName` | String | Nullable | N/A |

## Code examples

### REST example

```
POST /v3/geoelement/nielsendma/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "PageSize": 100,
  "PageStartIndex": 0,
  "IncludeDeprecated": false,
  "SearchTerms": ["501"]
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query NielsenDmaGeoElements {
  nielsenDmaGeoElements(
    first: 100
    input: {
      includeDeprecated: false
      searchTerms: ["501"]
    }
  ) {
    nodes {
      id
      nielsenDmaCode
      nielsenDmaName
      isDeprecated
    }
    totalCount
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```
