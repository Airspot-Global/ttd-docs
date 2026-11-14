# POST /v3/geoelement/city/query/region → Query.cityGeoElements

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-geoelement-city-query-region
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/geoelement/city/query/region → Query.cityGeoElements

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/geoelement/city/query/region` |
| GraphQL query | `Query.cityGeoElements` |
| Return type | `CityGeoElementsConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |
| `RegionCode` | `regionCode` | String! | Required | Required filter key |
| `IncludeDeprecated` | `includeDeprecated` | Boolean | Optional | N/A |
| `MetroCode` | N/A | N/A | Optional | Deprecated on REST; use `nielsenDmaCode` filter instead |
| `NielsenDmaCode` | `nielsenDmaCode` | String | Optional | Replacement for deprecated REST `MetroCode` filter |
| `SearchTerms` | `searchTerms` | [String!] | Optional | N/A |
| `SortFields` | `sortFields` | [CityGeoElementSortingFieldSortInput!] | Optional | N/A |
| `SortFields[].FieldId` | `sortFields[].fieldId` | CityGeoElementSortingFieldInput! | Required | REST enum values `CityName`, `NielsenDmaCode`, `NielsenDmaName` map to `CITY_NAME`, `NIELSEN_DMA_CODE`, `NIELSEN_DMA_NAME`; deprecated REST-only values `MetroCode` and `MetroName` have no GraphQL enum counterpart |
| `SortFields[].Ascending` | `sortFields[].ascending` | Boolean | Optional | N/A |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [CityGeoElement!] | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].GeoElementId` | `id` | ID! | Not nullable | GeoElementId → `id` |
| `Result[].IsDeprecated` | `isDeprecated` | Boolean | Nullable | N/A |
| `Result[].CityName` | `cityName` | String | Nullable | N/A |
| `Result[].MetroCode` | N/A | N/A | N/A | Deprecated on REST; use `nielsenDmaCode` on the node instead |
| `Result[].MetroName` | N/A | N/A | N/A | Deprecated on REST; use `nielsenDmaName` on the node instead |
| `Result[].NielsenDmaCode` | `nielsenDmaCode` | String | Nullable | Replacement for deprecated REST `MetroCode` |
| `Result[].NielsenDmaName` | `nielsenDmaName` | String | Nullable | Replacement for deprecated REST `MetroName` |
| `Result[].RegionCode` | `regionCode` | String | Nullable | N/A |
| `Result[].RegionName` | `regionName` | String | Nullable | N/A |

## Code examples

### REST example

```
POST /v3/geoelement/city/query/region HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "RegionCode": "CA",
  "PageSize": 100,
  "PageStartIndex": 0,
  "NielsenDmaCode": "803",
  "IncludeDeprecated": false
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query CityGeoElements {
  cityGeoElements(
    first: 100
    input: {
      regionCode: "CA"
      nielsenDmaCode: "803"
      includeDeprecated: false
    }
  ) {
    nodes {
      id
      cityName
      nielsenDmaCode
      nielsenDmaName
      regionCode
      regionName
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
