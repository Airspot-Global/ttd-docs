# POST /v3/geoelement/region/query/country → Query.regions

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-geoelement-region-query-country
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/geoelement/region/query/country → Query.regions

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/geoelement/region/query/country` |
| GraphQL query | `Query.regions` |
| Return type | `RegionsConnection` |

> **Advisory:** REST returns paged `RegionGeoElement` rows scoped by `CountryCode` with geo-element IDs and deprecation flags. `Query.regions` returns `Region { id, shortName, longName, country }`—a different shape. `RegionFilterInput` does not expose a country-code filter; use `Region.country` on returned nodes for country association. Not a 1:1 geo-element query replacement.

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |
| `IncludeDeprecated` | N/A | N/A | Optional | **Not currently available in GraphQL** |
| `SearchTerms` | `where` | RegionFilterInput | Optional | Filter by `shortName`/`longName`/`id`; semantics differ from REST search terms |
| `SortFields` | `order` | [RegionSortInput!] | Optional | N/A |
| `CountryCode` | N/A | N/A | Required | No country-code filter on `Query.regions`; inspect `Region.country` on nodes |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [Region!] | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].GeoElementId` | N/A | N/A | N/A | No geo-element ID on `Region` |
| `Result[].IsDeprecated` | N/A | N/A | N/A | N/A |
| `Result[].CountryCode` | `country.shortName` | String! | Not nullable | Via nested `Region.country` |
| `Result[].CountryName` | `country.longName` | String! | Not nullable | Via nested `Region.country` |
| `Result[].RegionCode` | `shortName` | String | Nullable | Partial match via `Region.shortName` |
| `Result[].RegionName` | `longName` | String! | Not nullable | Partial match via `Region.longName` |

## Endpoint-specific nested types and enums

### RegionGeoElement

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `GeoElementId` | N/A | N/A | N/A | No geo-element ID on `Region` |
| `IsDeprecated` | N/A | N/A | N/A | N/A |
| `CountryCode` | `country.shortName` | String! | Not nullable | Via nested `Region.country` |
| `CountryName` | `country.longName` | String! | Not nullable | Via nested `Region.country` |
| `RegionCode` | `shortName` | String | Nullable | Partial match via `Region.shortName` |
| `RegionName` | `longName` | String! | Not nullable | Partial match via `Region.longName` |

## Code examples

### REST example

```
POST /v3/geoelement/region/query/country HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "CountryCode": "US",
  "PageSize": 100,
  "PageStartIndex": 0
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query Regions {
  regions(first: 100) {
    nodes {
      id
      shortName
      longName
      country {
        shortName
        longName
      }
    }
    totalCount
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```
