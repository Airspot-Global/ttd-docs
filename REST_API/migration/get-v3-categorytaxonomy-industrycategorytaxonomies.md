# GET /v3/categorytaxonomy/industrycategorytaxonomies → Query.industryCategoryTaxonomies

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-categorytaxonomy-industrycategorytaxonomies
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/categorytaxonomy/industrycategorytaxonomies → Query.industryCategoryTaxonomies

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/categorytaxonomy/industrycategorytaxonomies` |
| GraphQL query | `Query.industryCategoryTaxonomies` |
| Return type | `[CategoryTaxonomy!]!` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `industryCategoryTaxonomies` (top-level list) | [CategoryTaxonomy!]! | Not nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | N/A | N/A | N/A | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].CategoryTaxonomyId` | `id` | ID! | Not nullable | Renamed from `CategoryTaxonomyId`. |
| `Result[].CategoryTaxonomyName` | `name` | String! | Not nullable | Renamed from `CategoryTaxonomyName`. |
| `Result[].CategoryTaxonomyVersion` | `version` | String! | Not nullable | Renamed from `CategoryTaxonomyVersion`. |

## Endpoint-specific nested types and enums

### CategoryTaxonomy

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CategoryTaxonomyId` | `id` | ID! | Not nullable | Renamed; `long` → `ID`. |
| `CategoryTaxonomyName` | `name` | String! | Not nullable | N/A |
| `CategoryTaxonomyVersion` | `version` | String! | Not nullable | N/A |

## Code examples

### REST example

```
GET /v3/categorytaxonomy/industrycategorytaxonomies HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query IndustryCategoryTaxonomies {
  industryCategoryTaxonomies {
    id
    name
    version
  }
}
```
