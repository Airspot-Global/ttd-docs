# POST /v3/crossdevicevendor/query/advertiser → Advertiser.crossDeviceVendors

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-crossdevicevendor-query-advertiser
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/crossdevicevendor/query/advertiser → Advertiser.crossDeviceVendors

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/crossdevicevendor/query/advertiser` |
| GraphQL query | `Advertiser.crossDeviceVendors` |
| Return type | `CrossDeviceVendorsConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | Parent: `Advertiser.crossDeviceVendors` | N/A | Required | `AdvertiserId` is implicit from the parent `Advertiser` entity key—not exposed as a GraphQL argument. |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [CrossDeviceVendor!] | Nullable | Vendor fee fields are on `edges`, not `nodes`—see rows below. |
| `Result.CrossDeviceVendorId` | `CrossDeviceVendor.id` | ID! | Not nullable | N/A |
| `Result.CrossDeviceVendorName` | `CrossDeviceVendor.name` | String! | Not nullable | N/A |
| `Result.CrossDeviceVendorFee` | `CrossDeviceVendorsEdge.fee` | Fee | Nullable | Vendor fee details; exposed on the connection edge, not the vendor node. |
| `Result.CrossDeviceVendorFee.PercentOfMediaCostRate` | `CrossDeviceVendorsEdge.fee.percentOfMediaCostRate` | Decimal | Nullable | N/A |
| `Result.CrossDeviceVendorFee.PercentOfDataCostRate` | `CrossDeviceVendorsEdge.fee.percentOfDataCostRate` | Decimal | Nullable | Always `null` for cross-device vendors; included for API parity. |
| `Result.CrossDeviceVendorFee.CPMRate` | `CrossDeviceVendorsEdge.fee.cpmRate` | MoneyModel | Nullable | N/A |
| `Result.CrossDeviceVendorFee.CPMRate.Amount` | `CrossDeviceVendorsEdge.fee.cpmRate.amount` | Decimal! | Not nullable | N/A |
| `Result.CrossDeviceVendorFee.CPMRate.CurrencyCode` | `CrossDeviceVendorsEdge.fee.cpmRate.currencyCode` | CurrencyCode! | Not nullable | N/A |
| `Result.CrossDeviceVendorFee.CPMRateInAdvertiserCurrency` | `CrossDeviceVendorsEdge.fee.cpmRateInAdvertiserCurrency` | MoneyModel | Nullable | Advertiser-currency-converted CPM. |
| `Result.CrossDeviceVendorFee.CPMRateInAdvertiserCurrency.Amount` | `CrossDeviceVendorsEdge.fee.cpmRateInAdvertiserCurrency.amount` | Decimal! | Not nullable | N/A |
| `Result.CrossDeviceVendorFee.CPMRateInAdvertiserCurrency.CurrencyCode` | `CrossDeviceVendorsEdge.fee.cpmRateInAdvertiserCurrency.currencyCode` | CurrencyCode! | Not nullable | N/A |
| `Result.CrossDeviceVendorFee.CPCRate` | `CrossDeviceVendorsEdge.fee.cpcRate` | MoneyModel | Nullable | Always `null` for cross-device vendors; included for API parity. |
| `Result.CrossDeviceVendorFee.CPCRate.Amount` | `CrossDeviceVendorsEdge.fee.cpcRate.amount` | Decimal! | Not nullable | N/A |
| `Result.CrossDeviceVendorFee.CPCRate.CurrencyCode` | `CrossDeviceVendorsEdge.fee.cpcRate.currencyCode` | CurrencyCode! | Not nullable | N/A |
| `Result.CrossDeviceVendorFee.CPCRateInAdvertiserCurrency` | `CrossDeviceVendorsEdge.fee.cpcRateInAdvertiserCurrency` | MoneyModel | Nullable | Always `null` for cross-device vendors; included for API parity. |
| `Result.CrossDeviceVendorFee.CPCRateInAdvertiserCurrency.Amount` | `CrossDeviceVendorsEdge.fee.cpcRateInAdvertiserCurrency.amount` | Decimal! | Not nullable | N/A |
| `Result.CrossDeviceVendorFee.CPCRateInAdvertiserCurrency.CurrencyCode` | `CrossDeviceVendorsEdge.fee.cpcRateInAdvertiserCurrency.currencyCode` | CurrencyCode! | Not nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |

## Endpoint-specific nested types and enums

### CrossDeviceVendor

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CrossDeviceVendorId` | `id` | ID! | Not nullable | REST `int` serializes as GraphQL `ID`. |
| `CrossDeviceVendorName` | `name` | String! | Not nullable | N/A |

### CrossDeviceVendorsEdge

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CrossDeviceVendorFee` | `fee` | Fee | Nullable | Fee is on the connection edge, not on `CrossDeviceVendor`. |

### Fee

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `PercentOfMediaCostRate` | `percentOfMediaCostRate` | Decimal | Nullable | N/A |
| `PercentOfDataCostRate` | `percentOfDataCostRate` | Decimal | Nullable | Always `null` for cross-device vendors; included for API parity. |
| `CPMRate` | `cpmRate` | MoneyModel | Nullable | N/A |
| `CPMRate.Amount` | `cpmRate.amount` | Decimal! | Not nullable | N/A |
| `CPMRate.CurrencyCode` | `cpmRate.currencyCode` | CurrencyCode! | Not nullable | N/A |
| `CPMRateInAdvertiserCurrency` | `cpmRateInAdvertiserCurrency` | MoneyModel | Nullable | N/A |
| `CPMRateInAdvertiserCurrency.Amount` | `cpmRateInAdvertiserCurrency.amount` | Decimal! | Not nullable | N/A |
| `CPMRateInAdvertiserCurrency.CurrencyCode` | `cpmRateInAdvertiserCurrency.currencyCode` | CurrencyCode! | Not nullable | N/A |
| `CPCRate` | `cpcRate` | MoneyModel | Nullable | Always `null` for cross-device vendors; included for API parity. |
| `CPCRate.Amount` | `cpcRate.amount` | Decimal! | Not nullable | N/A |
| `CPCRate.CurrencyCode` | `cpcRate.currencyCode` | CurrencyCode! | Not nullable | N/A |
| `CPCRateInAdvertiserCurrency` | `cpcRateInAdvertiserCurrency` | MoneyModel | Nullable | Always `null` for cross-device vendors; included for API parity. |
| `CPCRateInAdvertiserCurrency.Amount` | `cpcRateInAdvertiserCurrency.amount` | Decimal! | Not nullable | N/A |
| `CPCRateInAdvertiserCurrency.CurrencyCode` | `cpcRateInAdvertiserCurrency.currencyCode` | CurrencyCode! | Not nullable | N/A |

## Code examples

### REST example

```
POST /v3/crossdevicevendor/query/advertiser HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserId": "<advertiser-id>",
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
query GetCrossDeviceVendors($advertiserId: ID!) {
  advertiser(id: $advertiserId) {
    crossDeviceVendors(first: 20) {
      edges {
        fee {
          percentOfMediaCostRate
          cpmRate {
            amount
            currencyCode
          }
          cpmRateInAdvertiserCurrency {
            amount
            currencyCode
          }
        }
        node {
          id
          name
        }
      }
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
}
```
