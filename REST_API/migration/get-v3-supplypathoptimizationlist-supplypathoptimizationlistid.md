# GET /v3/supplypathoptimizationlist/{supplypathoptimizationlistid} → supplyPathOptimizationList(id:)

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-supplypathoptimizationlist-supplypathoptimizationlistid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/supplypathoptimizationlist/{supplypathoptimizationlistid} → supplyPathOptimizationList(id:)

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/supplypathoptimizationlist/{supplypathoptimizationlistid}` |
| GraphQL query | `supplyPathOptimizationList(id:)` |
| Return type | `SupplyPathOptimizationList` |

## Multi-step operations

This REST endpoint returns summary scalars only. To load list items, use the detail REST endpoint or select `SupplyPathOptimizationList.items` in GraphQL, which triggers the separate detail read.

| REST field | GraphQL access | Notes |
| --- | --- | --- |
| `ListItems` | `SupplyPathOptimizationList.items` | Populated only via the detail endpoint |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `supplypathoptimizationlistid` | `supplyPathOptimizationList(id:)` | ID! | Required | Path parameter identifying the SPO list. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `SupplyPathOptimizationListId` | `id` | ID! | Not nullable | Entity identifier. |
| `SupplyPathOptimizationListName` | `name` | String | Nullable | Display name of the SPO list. |
| `AdvertiserId` | `advertiser` | Advertiser | Nullable | Entity reference to the owning advertiser when scoped to an advertiser. |
| `PartnerId` | `partner` | Partner | Nullable | Entity reference to the owning partner when scoped to a partner. |
| `CurrentCount` | `currentCount` | Int | Nullable | Aggregated count of items in the list. |
| `MaxCount` | `maxCount` | Int | Nullable | Maximum allowed list size. |
| `ListItems` | N/A | N/A | N/A | Not exposed by this endpoint; see detail endpoint or `items` field. |

## Code examples

### REST example

```
GET /v3/supplypathoptimizationlist/12345 HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetSPOListSummary($id: ID!) {
  supplyPathOptimizationList(id: $id) {
    id
    name
    currentCount
    maxCount
    advertiser { id }
    partner { id }
  }
}
```
