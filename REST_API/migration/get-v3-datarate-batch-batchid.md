# GET /v3/datarate/batch/{batchId} → Query.thirdPartyDataRateBatch

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-datarate-batch-batchid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/datarate/batch/{batchId} → Query.thirdPartyDataRateBatch

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/datarate/batch/{batchId}` |
| GraphQL query | `Query.thirdPartyDataRateBatch` |
| Return type | `ThirdPartyDataRateBatch` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `batchId` | `batchId` | ID! | Required | Path parameter. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `BatchId` | `id` | ID! | Not nullable | N/A |
| `ProviderId` | `provider.id` | ID! | Not nullable | N/A |
| `ApprovalStatus` | `approvalStatus` | DataRateBatchApprovalStatus | Nullable | N/A |
| `ProcessingStatus` | `processingStatus` | DataRateBatchProcessingStatus | Nullable | N/A |
| `CreatedAtUtc` | `createdAtUtc` | DateTime | Nullable | N/A |
| `EstimatedProcessAtUtc` | `estimatedProcessAtUtc` | DateTime | Nullable | N/A |
| `ProcessedAtUtc` | `processedAtUtc` | DateTime | Nullable | N/A |
| `DataRates` | `dataRates` | `[ThirdPartyDataRateBatchItem!]!` | Not nullable | N/A |
| `DataRates[].BrandId` | `brand.id` | ID! | Not nullable | REST flat ID maps to nested object reference. |
| `DataRates[].PartnerId` | `partner.id` | ID! | Not nullable | Parent `partner` nullable; absent unless `rateLevel` is `PARTNER`. When present, `id` is not nullable. |
| `DataRates[].AdvertiserId` | `advertiser.id` | ID! | Not nullable | Parent `advertiser` nullable; absent unless `rateLevel` is `ADVERTISER`. When present, `id` is not nullable. |
| `DataRates[].RateLevel` | `rateLevel` | DataRateLevel! | Not nullable | N/A |
| `DataRates[].RateType` | `rateType` | ThirdPartyDataRateType! | Not nullable | N/A |
| `DataRates[].CPMRate` | `cpmRate` | MoneyModel | Nullable | N/A |
| `DataRates[].PercentOfMediaCostRate` | `percentOfMediaCostRate` | Decimal | Nullable | N/A |
| `DataRates[].ProviderElementId` | `providerElementId` | ID! | Not nullable | N/A |

## Endpoint-specific nested types and enums

### DataRate

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `BrandId` | `brand.id` | ID! | Not nullable | REST flat ID maps to nested object reference. |
| `PartnerId` | `partner.id` | ID! | Not nullable | Parent `partner` nullable; absent unless `rateLevel` is `PARTNER`. When present, `id` is not nullable. |
| `AdvertiserId` | `advertiser.id` | ID! | Not nullable | Parent `advertiser` nullable; absent unless `rateLevel` is `ADVERTISER`. When present, `id` is not nullable. |
| `RateLevel` | `rateLevel` | DataRateLevel! | Not nullable | N/A |
| `RateType` | `rateType` | ThirdPartyDataRateType! | Not nullable | N/A |
| `CPMRate` | `cpmRate` | MoneyModel | Nullable | N/A |
| `PercentOfMediaCostRate` | `percentOfMediaCostRate` | Decimal | Nullable | N/A |
| `ProviderElementId` | `providerElementId` | ID! | Not nullable | N/A |

## Code examples

### REST example

```
GET /v3/datarate/batch/batch789 HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query DataRateBatch {
  thirdPartyDataRateBatch(batchId: "batch789") {
    id
    provider {
      id
    }
    approvalStatus
    processingStatus
    dataRates {
      brand {
        id
      }
      partner {
        id
      }
      advertiser {
        id
      }
      rateLevel
      rateType
      cpmRate {
        amount
        currencyCode
      }
      providerElementId
    }
  }
}
```
