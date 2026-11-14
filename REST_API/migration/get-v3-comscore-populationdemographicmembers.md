# GET /v3/comscore/populationdemographicmembers → Query.comscorePopulations

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-comscore-populationdemographicmembers
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/comscore/populationdemographicmembers → Query.comscorePopulations

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/comscore/populationdemographicmembers` |
| GraphQL query | `Query.comscorePopulations` |
| Return type | `[ComscorePopulation!]!` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `comscorePopulations` (top-level list) | [ComscorePopulation!]! | Not nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | N/A | N/A | N/A | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `ComscorePopulation.Id` | `id` | Int! | Not nullable | N/A |
| `ComscorePopulation.Name` | `name` | String! | Not nullable | Population display name. |
| `ComscorePopulation.ComscoreDemographicMembers` | `demographicMembers` | [ComscoreDemographicMember!]! | Not nullable | Nested collection. |
| `ComscoreDemographicMember.Id` | `demographicMembers { id }` | Int! | Not nullable | Nested leaf. |
| `ComscoreDemographicMember.Name` | `demographicMembers { name }` | String! | Not nullable | Nested leaf. |
| `ComscoreDemographicMember.IsMobileDemographic` | `demographicMembers { isMobileDemographic }` | Boolean! | Not nullable | Nested leaf. |

## Endpoint-specific nested types and enums

### ComscorePopulation

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Id` | `id` | Int! | Not nullable | N/A |
| `Name` | `name` | String! | Not nullable | Population display name. |
| `ComscoreDemographicMembers` | `demographicMembers` | [ComscoreDemographicMember!]! | Not nullable | Nested collection. |

### ComscoreDemographicMember

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Id` | `id` | Int! | Not nullable | N/A |
| `Name` | `name` | String! | Not nullable | N/A |
| `IsMobileDemographic` | `isMobileDemographic` | Boolean! | Not nullable | N/A |

## Code examples

### REST example

```
GET /v3/comscore/populationdemographicmembers HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query ComscorePopulations {
  comscorePopulations {
    id
    name
    demographicMembers {
      id
      name
      isMobileDemographic
    }
  }
}
```
