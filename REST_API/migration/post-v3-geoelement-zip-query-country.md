# POST /v3/geoelement/zip/query/country → Query.zipGeoElements

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-geoelement-zip-query-country
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/geoelement/zip/query/country → Query.zipGeoElements

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/geoelement/zip/query/country` |
| GraphQL query | `Query.zipGeoElements` |
| Return type | `ZipGeoElementsConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `CountryCode` | `countryCode` | String! | Required | Required filter key |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |
| `IncludeDeprecated` | `includeDeprecated` | Boolean | Optional | N/A |
| `SortFields` | `sortFields` | [ZipGeoElementSortingFieldSortInput!] | Optional | N/A |
| `SortFields[].FieldId` | `sortFields[].fieldId` | ZipGeoElementSortingFieldInput! | Required | REST enum value `ZipCode` maps to `ZIP_CODE` |
| `SortFields[].Ascending` | `sortFields[].ascending` | Boolean | Optional | N/A |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [ZipGeoElement!] | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].GeoElementId` | `id` | ID! | Not nullable | GeoElementId → `id` |
| `Result[].IsDeprecated` | `isDeprecated` | Boolean | Nullable | N/A |
| `Result[].CountryCode` | `countryCode` | String | Nullable | N/A |
| `Result[].CountryName` | `countryName` | String | Nullable | N/A |
| `Result[].ZipCode` | `zipCode` | String | Nullable | N/A |

## Code examples

### REST example

```
POST /v3/geoelement/zip/query/country HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "CountryCode": "US",
  "PageSize": 100,
  "PageStartIndex": 0,
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
query ZipGeoElements {
  zipGeoElements(
    first: 100
    input: {
      countryCode: "US"
      includeDeprecated: false
    }
  ) {
    nodes {
      id
      zipCode
      countryCode
      countryName
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
