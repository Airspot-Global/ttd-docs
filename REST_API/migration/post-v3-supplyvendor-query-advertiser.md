# POST /v3/supplyvendor/query/advertiser → Advertiser.supplyVendors

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-supplyvendor-query-advertiser
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/supplyvendor/query/advertiser → Advertiser.supplyVendors

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/supplyvendor/query/advertiser` |
| GraphQL query | `Advertiser.supplyVendors` |
| Return type | `SupplyVendorsConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | Parent: `advertiser(id:)` | ID! | Required | Advertiser context is implicit from the parent `Advertiser` entity—not exposed as a GraphQL argument. `filter.advertiserId` is ignored when present (kept for backwards compatibility). |
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
POST /v3/supplyvendor/query/advertiser HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserId": "<advertiser-id>",
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
query SupplyVendorsForAdvertiser {
  advertiser(id: "<advertiser-id>") {
    supplyVendors(
      first: 20
      filter: { searchTerms: ["example"], areDealsSupported: true }
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
