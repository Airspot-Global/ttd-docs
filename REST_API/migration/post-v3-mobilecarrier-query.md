# POST /v3/mobilecarrier/query → Query.carriers

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-mobilecarrier-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/mobilecarrier/query → Query.carriers

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/mobilecarrier/query` |
| GraphQL query | `Query.carriers` |
| Return type | `CarriersConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |
| `CarrierNameFilter` | `Query.carriers(where:)` | CarrierFilterInput | Optional | REST filters carriers whose name contains the value. GraphQL uses `where: { name: { contains: "..." } }`. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [Carrier!] | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].CarrierId` | `Carrier.id` | ID! | Not nullable | `int` → `ID` (string). REST integer ID; GraphQL returns a string ID—code that parses the ID as an integer will break. |
| `Result[].CarrierName` | `Carrier.name` | String | Nullable | REST marks `CarrierName` required; GraphQL `name` is nullable. Code assuming a non-null name will break. |

## Endpoint-specific nested types and enums

### MobileCarrier

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CarrierId` | `id` | ID! | Not nullable | `int` → `ID` (string). REST integer ID; GraphQL returns a string ID—code that parses the ID as an integer will break. |
| `CarrierName` | `name` | String | Nullable | REST marks `CarrierName` required; GraphQL `name` is nullable. Code assuming a non-null name will break. |

## Code examples

### REST example

```
POST /v3/mobilecarrier/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "PageStartIndex": 0,
  "PageSize": 100,
  "CarrierNameFilter": "Verizon"
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query Carriers {
  carriers(
    first: 100
    where: {
      name: { contains: "Verizon" }
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
```
