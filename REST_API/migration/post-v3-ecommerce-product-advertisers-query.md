# POST /v3/ecommerce/product/advertisers/query → Merchant.advertisersWithProductPermissions(skuIds:)

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-ecommerce-product-advertisers-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/ecommerce/product/advertisers/query → Merchant.advertisersWithProductPermissions(skuIds:)

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/ecommerce/product/advertisers/query` |
| GraphQL query | `Merchant.advertisersWithProductPermissions(skuIds:)` |
| Return type | `[Advertiser!]!` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `MerchantId` | `merchant(id: $merchantId)` | ID! | Required | Root merchant lookup. |
| `SkuId` | `advertisersWithProductPermissions(skuIds: [$skuId])` | [ID!]! | Required | Single SKU wrapped in array argument. |

## Response field mapping

REST returns a top-level JSON array of advertiser ID strings.

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| _(top-level array element)_ | `advertisersWithProductPermissions[].id` | ID! | Not nullable | Returns maximal subset of advertisers with permission to all given SKUs. |

## Code examples

### REST example

```
POST /v3/ecommerce/product/advertisers/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "MerchantId": "merchant-id",
  "SkuId": "sku-001"
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query ProductAdvertiserPermissions($merchantId: ID!, $skuId: ID!) {
  merchant(id: $merchantId) {
    id
    advertisersWithProductPermissions(skuIds: [$skuId]) {
      id
      name
    }
  }
}
```
