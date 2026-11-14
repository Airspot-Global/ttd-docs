# GET /v3/datarate/brands/{providerId} → ThirdPartyDataProvider.brandsForDataRates

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-datarate-brands-providerid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/datarate/brands/{providerId} → ThirdPartyDataProvider.brandsForDataRates

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/datarate/brands/{providerId}` |
| GraphQL query | `ThirdPartyDataProvider.brandsForDataRates` |
| Return type | `[ThirdPartyDataBrand!]!` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `providerId` | `ThirdPartyDataProvider(id:)` | N/A | Required | Path parameter—parent lookup for `brandsForDataRates`. |

## Response field mapping

REST returns a top-level JSON array of brand objects.

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `BrandId` | `id` | ID! | Not nullable | List element. |
| `BrandName` | `name` | String! | Not nullable | List element. |
| `LogoUrl` | `logoUrl` | String | Nullable | List element. |

## Code examples

### REST example

```
GET /v3/datarate/brands/prov123 HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query BrandsForDataRates {
  thirdPartyDataProvider(id: "prov123") {
    brandsForDataRates {
      id
      name
      logoUrl
    }
  }
}
```
