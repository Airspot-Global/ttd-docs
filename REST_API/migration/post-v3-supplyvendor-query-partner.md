# POST /v3/supplyvendor/query/partner → Partner.supplyVendors

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-supplyvendor-query-partner
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/supplyvendor/query/partner → Partner.supplyVendors

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/supplyvendor/query/partner` |
| GraphQL query | `Partner.supplyVendors` |
| Return type | `SupplyVendorsConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PartnerId` | Parent: `partner(id:)` | ID! | Required | Partner context is implicit from the parent `Partner` entity. When a `filter` object is supplied, `filter.partnerId` is also required and must match the parent partner ID. |
| `SearchTerms` | `filter.searchTerms` | `[String!]` | Optional | Optional text search filter. |
| `SortFields` | `filter.sortFields` | `[SupplyVendorSortingFieldSortingInput!]` | Optional | Optional sort specification. Defaults to Name ascending when omitted. |
| `AreDealsSupported` | `filter.areDealsSupported` | Boolean | Optional | Optional filter for deal-supported vendors. |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [SupplyVendor!] | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].SupplyVendorId` | `SupplyVendor.id` | ID! | Not nullable | `long` → `ID` (string). |
| `Result[].SupplyVendorName` | `SupplyVendor.name` | String! | Not nullable | Supply vendor display name. |

## Endpoint-specific nested types and enums

### SupplyVendor

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `SupplyVendorId` | `id` | ID! | Not nullable | `long` → `ID` (string). |
| `SupplyVendorName` | `name` | String! | Not nullable | Supply vendor display name. |

### SupplyVendorSortingFieldSortingInput

| Field | GraphQL type | Required | Notes |
| --- | --- | --- | --- |
| fieldId | SupplyVendorSortingFieldInput! | Required | Sort field to apply. |
| ascending | Boolean | Optional | Sort direction; defaults to ascending when omitted. |

### SupplyVendorSortingFieldInput

| Enum value | Notes |
| --- | --- |
| `NAME` | N/A |

## Code examples

### REST example

```
POST /v3/supplyvendor/query/partner HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "PartnerId": "<partner-id>",
  "SearchTerms": ["example"],
  "AreDealsSupported": true,
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
query SupplyVendorsForPartner {
  partner(id: "<partner-id>") {
    supplyVendors(
      first: 20
      filter: {
        partnerId: "<partner-id>"
        searchTerms: ["example"]
        areDealsSupported: true
      }
    ) {
      nodes {
        id
        name
      }
      totalCount
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
}
```
