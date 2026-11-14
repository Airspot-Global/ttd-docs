# POST /v3/geoelement/country/query → Query.countries

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-geoelement-country-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/geoelement/country/query → Query.countries

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/geoelement/country/query` |
| GraphQL query | `Query.countries` |
| Return type | `CountriesConnection` |

> **Advisory:** REST returns paged `CountryGeoElement` rows with `GeoElementId` and deprecation flags. `Query.countries` returns `Country { id, shortName, longName }`—a different shape with no geo-element ID or deprecation metadata. Use for country code/name lookup only; not a 1:1 geo-element query replacement.

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |
| `IncludeDeprecated` | N/A | N/A | Optional | **Not currently available in GraphQL** |
| `SearchTerms` | `where` | CountryFilterInput | Optional | Filter by `shortName`/`longName`/`id`; semantics differ from REST search terms |
| `SortFields` | `order` | [CountrySortInput!] | Optional | N/A |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [Country!] | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].GeoElementId` | N/A | N/A | N/A | `Query.countries` returns `Country`—no geo-element ID |
| `Result[].IsDeprecated` | N/A | N/A | N/A | No deprecation flag on `Country` |
| `Result[].CountryCode` | `shortName` | String! | Not nullable | Partial match via `Country.shortName` |
| `Result[].CountryName` | `longName` | String! | Not nullable | Partial match via `Country.longName` |

## Endpoint-specific nested types and enums

### CountryGeoElement

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `GeoElementId` | N/A | N/A | N/A | `Query.countries` returns `Country`—no geo-element ID |
| `IsDeprecated` | N/A | N/A | N/A | N/A |
| `CountryCode` | `shortName` | String! | Not nullable | Partial match via `Country.shortName` |
| `CountryName` | `longName` | String! | Not nullable | Partial match via `Country.longName` |

## Code examples

### REST example

```
POST /v3/geoelement/country/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
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
query Countries {
  countries(first: 100) {
    nodes {
      id
      shortName
      longName
    }
    totalCount
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```
