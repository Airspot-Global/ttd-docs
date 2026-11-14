# Merchant product: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/merchantproduct-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Merchant product: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `POST /v3/ecommerce/product/batch/query` | `Merchant.products` | Batch product read; paginated connection replaces unpaged dictionary |
| `POST /v3/ecommerce/advertiser/products/query` | `Advertiser.availableItemsetItems(merchantId:)` | Flat SKU ID list; paginate with `first`/`after` |
| `POST /v3/ecommerce/product/advertisers/query` | `Merchant.advertisersWithProductPermissions(skuIds:)` | Advertiser ids with permission for given SKUs |

## Shared nested types and enums

### MerchantProduct

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `SkuId` | `itemCode` | String! | Not nullable | N/A |
| `ProductName` | `name` | String! | Not nullable | N/A |
| `CategoryId` | `category.id` | ID! | Not nullable | REST exposes source category string; GraphQL resolves `MerchantCategory` object. |
| `BrandName` | `brandName` | String | Nullable | Direct. |
| `Link` | N/A | N/A | N/A | Not currently available in GraphQL. |
| `MobileLink` | N/A | N/A | N/A | Not currently available in GraphQL. |
| `ImageLink` | N/A | N/A | N/A | Not currently available in GraphQL. |
| `Availability` | `availability` | String | Nullable | Direct. |
| `Description` | N/A | N/A | N/A | Not currently available in GraphQL. |
| `AgeGroup` | `ageGroup` | String | Nullable | Direct. |
| `GTIN` | N/A | N/A | N/A | Not currently available in GraphQL. |
| `MPN` | N/A | N/A | N/A | Not currently available in GraphQL. |
| `Color` | `color` | String | Nullable | Direct. |
| `Size` | `size` | String | Nullable | Direct. |
| `Price` | `price` | Decimal | Nullable | Amount only; see `Price.Amount`. |
| `Price.Amount` | `price` | Decimal | Nullable | Flattened to scalar on the GraphQL type. |
| `Price.CurrencyCode` | N/A | N/A | N/A | Not currently available in GraphQL. |
| `Custom1` | `custom1Value` | String | Nullable | N/A |
| `Custom2` | `custom2Value` | String | Nullable | N/A |
| `Custom3` | `custom3Value` | String | Nullable | N/A |
| `Custom4` | `custom4Value` | String | Nullable | N/A |
| `Custom5` | `custom5Value` | String | Nullable | N/A |
| `CustomNumeric1` | `customNumeric1Value` | Decimal | Nullable | N/A |
| `CustomNumeric2` | `customNumeric2Value` | Decimal | Nullable | N/A |
| `CustomNumeric3` | `customNumeric3Value` | Decimal | Nullable | N/A |
| `CustomNumeric4` | `customNumeric4Value` | Decimal | Nullable | N/A |
| `CustomNumeric5` | `customNumeric5Value` | Decimal | Nullable | N/A |
| `CreatedAtUtc` | N/A | N/A | N/A | Not currently available in GraphQL. |
| `LastUpdatedAtUtc` | N/A | N/A | N/A | Not currently available in GraphQL. |

GraphQL-only fields with no REST counterpart: `category.name`, `category.parents`, `category.fullPaths`.
