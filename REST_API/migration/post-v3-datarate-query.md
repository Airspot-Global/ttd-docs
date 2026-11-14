# POST /v3/datarate/query → ThirdPartyDataProvider.thirdPartyDataRates

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-datarate-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/datarate/query → ThirdPartyDataProvider.thirdPartyDataRates

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/datarate/query` |
| GraphQL query | `ThirdPartyDataProvider.thirdPartyDataRates` |
| Return type | `ThirdPartyDataRatesConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PageSize` | `first` | Int | Optional | N/A |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `BrandId` | `filter.brandId` | ID! | Required | N/A |
| `ProviderId` | `ThirdPartyDataProvider(id:)` | N/A | Required | Parent lookup—not a connection argument. |
| `RateLevel` | `filter.rateLevel` | DataRateLevelInput! | Required | N/A |
| `AdvertiserId` | `filter.advertiserId` | ID | Optional | N/A |
| `IncludeInheritedRates` | `filter.includeInheritedRates` | Boolean | Optional | N/A |
| `PartnerId` | `filter.partnerId` | ID | Optional | N/A |
| `ProviderElementIds` | `filter.providerElementIds` | `[String!]` | Optional | N/A |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | `[ThirdPartyDataRate!]` | Nullable | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].BrandId` | `brand.id` | ID! | Not nullable | REST flat ID maps to nested object reference. |
| `Result[].PartnerId` | `partner.id` | ID! | Not nullable | Parent `partner` nullable; absent unless `rateLevel` is `PARTNER`. When present, `id` is not nullable. |
| `Result[].AdvertiserId` | `advertiser.id` | ID! | Not nullable | Parent `advertiser` nullable; absent unless `rateLevel` is `ADVERTISER`. When present, `id` is not nullable. |
| `Result[].RateLevel` | `rateLevel` | DataRateLevel! | Not nullable | Response field; distinct from request filter.`rateLevel`. |
| `Result[].RateType` | `rateType` | ThirdPartyDataRateType! | Not nullable | N/A |
| `Result[].CPMRate` | `cpmRate` | MoneyModel | Nullable | N/A |
| `Result[].PercentOfMediaCostRate` | `percentOfMediaCostRate` | Decimal | Nullable | N/A |
| `Result[].ProviderId` | `provider.id` | ID! | Not nullable | Provider ID is the parent entity key. |
| `Result[].ProviderElementId` | `providerElementId` | ID! | Not nullable | N/A |
| `Result[].IsInherited` | `isInherited` | Boolean | Nullable | N/A |
| `Result[].InheritedFromProviderElementId` | `inheritedFromProviderElementId` | ID | Nullable | N/A |

## Endpoint-specific nested types and enums

### ThirdPartyData

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `BrandId` | `brand.id` | ID! | Not nullable | REST flat ID maps to nested object reference. |
| `PartnerId` | `partner.id` | ID! | Not nullable | Parent `partner` nullable; absent unless `rateLevel` is `PARTNER`. When present, `id` is not nullable. |
| `AdvertiserId` | `advertiser.id` | ID! | Not nullable | Parent `advertiser` nullable; absent unless `rateLevel` is `ADVERTISER`. When present, `id` is not nullable. |
| `RateLevel` | `rateLevel` | DataRateLevel! | Not nullable | Response field; distinct from request filter.`rateLevel`. |
| `RateType` | `rateType` | ThirdPartyDataRateType! | Not nullable | N/A |
| `CPMRate` | `cpmRate` | MoneyModel | Nullable | N/A |
| `PercentOfMediaCostRate` | `percentOfMediaCostRate` | Decimal | Nullable | N/A |
| `ProviderId` | `provider.id` | ID! | Not nullable | Provider ID is the parent entity key. |
| `ProviderElementId` | `providerElementId` | ID! | Not nullable | N/A |
| `IsInherited` | `isInherited` | Boolean | Nullable | N/A |
| `InheritedFromProviderElementId` | `inheritedFromProviderElementId` | ID | Nullable | N/A |

## Code examples

### REST example

```
POST /v3/datarate/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "ProviderId": "prov123",
  "BrandId": "brand123",
  "RateLevel": "Partner",
  "PageStartIndex": 0,
  "PageSize": 100
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query ProviderDataRates {
  thirdPartyDataProvider(id: "prov123") {
    thirdPartyDataRates(
      first: 100
      filter: {
        brandId: "brand123"
        rateLevel: PARTNER
      }
    ) {
      nodes {
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
        isInherited
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
