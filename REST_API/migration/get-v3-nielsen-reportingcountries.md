# GET /v3/nielsen/reportingcountries → Query.nielsenReportingCountries

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-nielsen-reportingcountries
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/nielsen/reportingcountries → Query.nielsenReportingCountries

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/nielsen/reportingcountries` |
| GraphQL query | `Query.nielsenReportingCountries` |
| Return type | `NielsenReportingCountry` connection |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [NielsenReportingCountry!] | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].Code` | `code` | String! | Not nullable | N/A |
| `Result[].DisplayName` | `displayName` | String! | Not nullable | N/A |
| N/A | `id` | ID! | Not nullable | GraphQL-only surrogate key; not in REST contract. |
| N/A | `isActive` | Boolean! | Not nullable | GraphQL-only; filter with `where: { isActive: { eq: true } }` for active countries. |

## Code examples

### REST example

```
GET /v3/nielsen/reportingcountries HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query NielsenReportingCountries {
  nielsenReportingCountries(first: 100, where: { isActive: { eq: true } }) {
    nodes {
      id
      code
      displayName
      isActive
    }
  }
}
```
