# GET /v3/supplypathoptimizationlist/detail/{supplypathoptimizationlistid} → SupplyPathOptimizationList.items

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-supplypathoptimizationlist-detail-supplypathoptimizationlistid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/supplypathoptimizationlist/detail/{supplypathoptimizationlistid} → SupplyPathOptimizationList.items

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/supplypathoptimizationlist/detail/{supplypathoptimizationlistid}` |
| GraphQL query | `SupplyPathOptimizationList.items` |
| Return type | `[SupplyPathOptimizationItem!]` |

## Multi-step operations

Scalar summary fields (`name`, `currentCount`, `maxCount`, `advertiser`, `partner`) are available from `GET /v3/supplypathoptimizationlist/{supplypathoptimizationlistid}` via `supplyPathOptimizationList(id:)`. Selecting `items` in GraphQL triggers this detail read. REST also returns scalars on the detail response; in GraphQL those scalars come from `supplyPathOptimizationList(id:)`.

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `supplypathoptimizationlistid` | Parent: `supplyPathOptimizationList(id:)` | ID! | Required | Path parameter identifying the SPO list. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `SupplyPathOptimizationListId` | `id` | ID! | Not nullable | Entity identifier; same as summary endpoint. |
| `SupplyPathOptimizationListName` | `name` | String | Nullable | Display name of the SPO list. |
| `AdvertiserId` | `advertiser` | Advertiser | Nullable | Entity reference to the owning advertiser when scoped to an advertiser. |
| `PartnerId` | `partner` | Partner | Nullable | Entity reference to the owning partner when scoped to a partner. |
| `CurrentCount` | `currentCount` | Int | Nullable | Aggregated count of items in the list. |
| `MaxCount` | `maxCount` | Int | Nullable | Maximum allowed list size. |
| `ListItems` | `items` | [SupplyPathOptimizationItem!] | Nullable | Collection of SPO list entries. |
| `ListItems[].Site` | `items.site` | String | Nullable | Optional site targeting, e.g. `google.com`. |
| `ListItems[].SupplyVendorId` | `items.supplyVendor` | SupplyVendor | Nullable | Supply vendor entity; select `supplyVendor { id }` for the vendor identifier. |
| `ListItems[].SupplyVendorPublisherId` | `items.supplyVendorPublisherId` | ID | Nullable | Optional supply vendor publisher identifier. |
| `ListItems[].InventoryType` | `items.inventoryType` | MediaType! | Not nullable | Inventory media type. |

## Endpoint-specific nested types and enums

### SupplyPathOptimizationItem

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Site` | `site` | String | Nullable | Optional site targeting. |
| `SupplyVendorId` | `supplyVendor` | SupplyVendor | Nullable | Supply vendor entity; use `supplyVendor { id }` for the vendor identifier. |
| `SupplyVendorPublisherId` | `supplyVendorPublisherId` | ID | Nullable | Optional publisher identifier. |
| `InventoryType` | `inventoryType` | MediaType! | Not nullable | Inventory media type. |

### MediaType

| Enum value | Notes |
| --- | --- |
| `Display` | Display inventory. |
| `Video` | Video inventory. |
| `Native` | Native inventory. |
| `Audio` | Audio inventory. |
| `NativeVideo` | Native video inventory. |

GraphQL also defines `UNKNOWN` on `MediaType`; it is not a member of the REST `MediaType` enum for this endpoint.

## Code examples

### REST example

```
GET /v3/supplypathoptimizationlist/detail/12345 HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetSPOListWithItems($id: ID!) {
  supplyPathOptimizationList(id: $id) {
    id
    name
    currentCount
    maxCount
    items {
      site
      supplyVendor { id }
      supplyVendorPublisherId
      inventoryType
    }
  }
}
```
