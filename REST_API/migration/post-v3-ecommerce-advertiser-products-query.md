# POST /v3/ecommerce/advertiser/products/query → Advertiser.availableItemsetItems(merchantId:)

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-ecommerce-advertiser-products-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/ecommerce/advertiser/products/query → Advertiser.availableItemsetItems(merchantId:)

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/ecommerce/advertiser/products/query` |
| GraphQL query | `Advertiser.availableItemsetItems(merchantId:)` |
| Return type | `AvailableItemsetItemsConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `MerchantId` | `availableItemsetItems(merchantId: $merchantId)` | ID! | Required | Required field argument on `Advertiser`. |
| `AdvertiserId` | `advertiser(id: $advertiserId)` | ID! | Required | Root advertiser lookup. |

## Response field mapping

REST returns a top-level JSON array of SKU ID strings (not wrapped in an object).

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| _(top-level array element)_ | `availableItemsetItems.nodes.itemCode` | String! | Not nullable | Map each node's `itemCode` to REST SKU string. Paginate with `first`/`after` until `hasNextPage` is false. |

`availableItemsetItems` returns `MerchantProduct` nodes—any field from the shared `MerchantProduct` mapping on the MerchantProduct domain page is also available on `nodes` when product detail is needed (not just SKU IDs).

## Code examples

### REST example

```
POST /v3/ecommerce/advertiser/products/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "MerchantId": "merchant-id",
  "AdvertiserId": "advertiser-id"
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query AdvertiserPermittedSkus($advertiserId: ID!, $merchantId: ID!) {
  advertiser(id: $advertiserId) {
    id
    availableItemsetItems(merchantId: $merchantId, first: 1000) {
      totalCount
      nodes {
        itemCode
      }
      pageInfo { hasNextPage endCursor }
    }
  }
}
```
