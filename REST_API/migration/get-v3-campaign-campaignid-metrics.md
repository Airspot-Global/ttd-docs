# GET /v3/campaign/{campaignId}/metrics → Campaign.pacing, Campaign.goalInfo

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-campaign-campaignid-metrics
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/campaign/{campaignId}/metrics → Campaign.pacing, Campaign.goalInfo

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/campaign/{campaignId}/metrics` |
| GraphQL query | `Query.campaign` |
| Return type | `Pacing`, `ROIGoalValue` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CampaignId` | `id` | ID! | Not nullable | Parent campaign ID on the queried `Campaign`. |
| `CampaignFlightId` | `currentFlight.id` | ID! | Not nullable | Absent when `currentFlight` is null. Flight ID for metrics context; use `currentFlight.id` instead of a dedicated metrics flight ID field. |
| `Pacing.FlightBudgetInAdvertiserCurrency` | `pacing.flightBudgetInAdvertiserCurrency` | Decimal | Nullable | Absent when `pacing` is null. |
| `Pacing.ProjectedSpendInAdvertiserCurrency` | `pacing.projectedSpendInAdvertiserCurrency` | Decimal | Nullable | N/A |
| `Pacing.CurrentSpendInAdvertiserCurrency` | `pacing.currentSpendInAdvertiserCurrency` | Decimal | Nullable | N/A |
| `Pacing.LastCalculatedAt` | `pacing.lastCalculatedAt` | DateTime | Nullable | N/A |
| `Pacing.AdvertiserCurrency` | `pacing.advertiserCurrency` | CurrencyCode! | Not nullable | N/A |
| `GoalInfo.Impressions` | `goalInfo.impressions` | Long | Nullable | Absent when `goalInfo` is null. |
| `GoalInfo.CPMInAdvertiserCurrency` | `goalInfo.cpmInAdvertiserCurrency` | MoneyModel | Nullable | REST Money → MoneyModel. |
| `GoalInfo.CPCInAdvertiserCurrency` | `goalInfo.cpcInAdvertiserCurrency` | MoneyWithTarget | Nullable | N/A |
| `GoalInfo.CTRInPercent` | `goalInfo.ctrInPercent` | NonMonetaryGoalTarget | Nullable | N/A |
| `GoalInfo.NielsenOTPInPercent` | `goalInfo.nielsenOtpInPercent` | NonMonetaryGoalTarget | Nullable | N/A |
| `GoalInfo.CPAInAdvertiserCurrency` | `goalInfo.cpaInAdvertiserCurrency` | MoneyWithTarget | Nullable | N/A |
| `GoalInfo.ReturnOnAdSpendPercent` | `goalInfo.returnOnAdSpendPercent` | NonMonetaryGoalTarget | Nullable | N/A |
| `GoalInfo.VCRInPercent` | `goalInfo.vcrInPercent` | NonMonetaryGoalTarget | Nullable | N/A |
| `GoalInfo.ViewabilityInPercent` | `goalInfo.viewabilityInPercent` | NonMonetaryGoalTarget | Nullable | N/A |
| `GoalInfo.VCPMInAdvertiserCurrency` | `goalInfo.vcpmInAdvertiserCurrency` | MoneyWithTarget | Nullable | N/A |
| `GoalInfo.CPCVInAdvertiserCurrency` | `goalInfo.cpcvInAdvertiserCurrency` | MoneyWithTarget | Nullable | N/A |
| `GoalInfo.MiaozhenOTPInPercent` | `goalInfo.miaozhenOtpInPercent` | NonMonetaryGoalTarget | Nullable | N/A |
| `GoalInfo.LastCalculatedAt` | `goalInfo.lastCalculatedAt` | DateTime | Nullable | N/A |

## Endpoint-specific nested types and enums

### Pacing

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `FlightBudgetInAdvertiserCurrency` | `flightBudgetInAdvertiserCurrency` | Decimal | Nullable | N/A |
| `ProjectedSpendInAdvertiserCurrency` | `projectedSpendInAdvertiserCurrency` | Decimal | Nullable | N/A |
| `CurrentSpendInAdvertiserCurrency` | `currentSpendInAdvertiserCurrency` | Decimal | Nullable | N/A |
| `LastCalculatedAt` | `lastCalculatedAt` | DateTime | Nullable | N/A |
| `AdvertiserCurrency` | `advertiserCurrency` | CurrencyCode! | Not nullable | N/A |

### MoneyModel

Used on `goalInfo.cpmInAdvertiserCurrency` (REST `Money`).

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Amount` | `amount` | Decimal! | Not nullable | N/A |
| `CurrencyCode` | `currencyCode` | CurrencyCode! | Not nullable | ISO 4217 enum. |

### MoneyWithTarget

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Amount` | `amount` | Decimal! | Not nullable | N/A |
| `Target` | `target` | Decimal! | Not nullable | N/A |
| `CurrencyCode` | `currencyCode` | CurrencyCode! | Not nullable | N/A |

### NonMonetaryGoalTarget

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Amount` | `amount` | Decimal | Nullable | N/A |
| `Target` | `target` | Decimal | Nullable | N/A |

## Code examples

### REST example

```
GET /v3/campaign/{campaignId}/metrics HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetCampaignMetrics($id: ID!) {
  campaign(id: $id) {
    id
    pacing {
      flightBudgetInAdvertiserCurrency
      projectedSpendInAdvertiserCurrency
      currentSpendInAdvertiserCurrency
      lastCalculatedAt
      advertiserCurrency
    }
    goalInfo {
      impressions
      lastCalculatedAt
      cpmInAdvertiserCurrency { amount currencyCode }
      cpcInAdvertiserCurrency { amount target currencyCode }
      ctrInPercent { amount target }
      cpaInAdvertiserCurrency { amount target currencyCode }
    }
  }
}
```
