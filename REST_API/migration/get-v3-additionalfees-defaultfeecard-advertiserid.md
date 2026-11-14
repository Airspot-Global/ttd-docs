# GET /v3/additionalfees/defaultfeecard/{advertiserId} → Advertiser.defaultFeeCard

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-additionalfees-defaultfeecard-advertiserid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/additionalfees/defaultfeecard/{advertiserId} → Advertiser.defaultFeeCard

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/additionalfees/defaultfeecard/{advertiserId}` |
| GraphQL query | `Advertiser.defaultFeeCard` |
| Return type | Default fee card (`ownerId`, `ownerType`, `startDate`, `fees`) |

Synthetic partner-derived default card for campaign creation. Not persisted as a pass-through fee card row.

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| advertiserId (path) | `Advertiser.id` (parent) | ID | Required | Query via `advertiser(id:)` then select `defaultFeeCard`. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `OwnerId` | `defaultFeeCard.ownerId` | ID | Nullable | Often null on synthetic card. |
| `OwnerType` | `defaultFeeCard.ownerType` | String | Nullable | REST returns `"campaign"`. |
| `StartDateUtc` | `defaultFeeCard.startDate` | DateTime! | Not nullable | N/A |
| `Fees` | `defaultFeeCard.fees` | [AdditionalFee!]! | Not nullable | Plain list of fee line items. |
| `Fees[].Description` | `fees.description` | String! | Not nullable | N/A |
| `Fees[].Amount` | `fees.amount` | Decimal! | Not nullable | REST percentage fees are ×100; GraphQL returns the same wire amount as the REST response. |
| `Fees[].FeeType` | `fees.feeType` | AdditionalFeeType! | Not nullable | N/A |

## Endpoint-specific nested types and enums

### AdditionalFeeType

| REST `AdditionalFeeType` | GraphQL `AdditionalFeeType` | Notes |
| --- | --- | --- |
| None | NONE | N/A |
| MediaCostPercentage | MEDIA_COST_PERCENTAGE | N/A |
| DataCostPercentage | DATA_COST_PERCENTAGE | N/A |
| MediaPlusDataCostPercentage | MEDIA_PLUS_DATA_COST_PERCENTAGE | N/A |
| PartnerCostPercentage | PARTNER_COST_PERCENTAGE | N/A |
| PartnerDataCostPercentage | PARTNER_DATA_COST_PERCENTAGE | N/A |
| FeeCPM | FEE_CPM | N/A |
| RateCPM | RATE_CPM | N/A |
| RateCPC | RATE_CPC | N/A |
| CustomPMP_PartnerCostPercentage | CUSTOM_PMP_PARTNER_COST_PERCENTAGE | N/A |

## Code examples

### REST example

```
GET /v3/additionalfees/defaultfeecard/{advertiserId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query AdvertiserDefaultFeeCard {
  advertiser(id: "<advertiserId>") {
    id
    defaultFeeCard {
      ownerType
      startDate
      fees {
        description
        amount
        feeType
      }
    }
  }
}
```
