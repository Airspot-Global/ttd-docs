# POST /v3/ecommerce/product/batch/query → Merchant.products

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-ecommerce-product-batch-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/ecommerce/product/batch/query → Merchant.products

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/ecommerce/product/batch/query` |
| GraphQL query | `Merchant.products` |
| Return type | `ProductsConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `MerchantId` | `merchant(id: $merchantId)` | ID! | Required | Root merchant lookup. |
| `SkuIds` | `products(where: { itemCode: { in: $skuIds } })` | [String!]! | Required | Pass SKU strings directly; no wrapper object in GraphQL. |
| `SkuIds[].SkuId` | Each element of `$skuIds` | String! | Required | Max length 128 in REST. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `ContainsError` | N/A | N/A | N/A | **Not currently available in GraphQL** |
| `BatchResponses` | `products.nodes` | `[MerchantProduct!]` | Nullable | Partial. Dictionary → list of products; no per-key error object. Paginate with `first`/`after`. |
| BatchResponses.{key} (dict key) | `nodes[].itemCode` | String! | Not nullable | SKU id on each returned product node. |
| `ApiBatchValue.Response` | Each element of `products.nodes` | MerchantProduct! | Not nullable | Present when SKU lookup succeeded. |
| `ApiBatchValue.Error` | N/A | N/A | N/A | **Not currently available in GraphQL** |
| `ApiBatchError.ErrorCode` | N/A | N/A | N/A | **Not currently available in GraphQL** |
| `ApiBatchError.Message` | N/A | N/A | N/A | **Not currently available in GraphQL** |

Product detail fields on each `products.nodes` element follow the shared `MerchantProduct` mapping on the MerchantProduct domain page.

## Code examples

### REST example

```
POST /v3/ecommerce/product/batch/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "MerchantId": "merchant-id",
  "SkuIds": [
    { "SkuId": "sku-001" },
    { "SkuId": "sku-002" }
  ]
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query MerchantProductBatch($merchantId: ID!, $skuIds: [String!]!) {
  merchant(id: $merchantId) {
    id
    products(first: 1000, where: { itemCode: { in: $skuIds } }) {
      totalCount
      nodes {
        itemCode
        name
        brandName
        availability
        price
        category { id name }
        ageGroup
        color
        size
        custom1Value
        custom2Value
        custom3Value
        custom4Value
        custom5Value
        customNumeric1Value
        customNumeric2Value
        customNumeric3Value
        customNumeric4Value
        customNumeric5Value
      }
      pageInfo { hasNextPage endCursor }
    }
  }
}
```
