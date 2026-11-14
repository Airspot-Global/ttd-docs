# GET /v3/campaign/template/{campaignId} → Campaign

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-campaign-template-campaignid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/campaign/template/{campaignId} → Campaign

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/campaign/template/{campaignId}` |
| GraphQL query | `Campaign` (via entity lookup by `id`) |
| Return type | `Campaign` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `IsTemplatePublished` | `isTemplatePublished` | Boolean | Nullable | Null for non-template campaigns. |
| `ShareType` | `templateShareType` | ShareType | Nullable | Enum values: `ADVERTISER`, `PARTNER`, `GLOBAL`, `NONE`. Null for regular campaigns. |
| `AdvertiserId` | `advertiser.id` | String! | Not nullable | Inherited from `CampaignBase`. |
| `CampaignId` | `id` | ID! | Not nullable | Inherited from `CampaignBase`. |
| `CampaignName` | `name` | String! | Not nullable | Inherited from `CampaignBase`. |
| `Description` | `description` | String | Nullable | Inherited from `CampaignBase`. |
| `PartnerCostPercentageFee` | N/A | N/A | N/A | Deprecated on REST |
| `PartnerCPMFee` | N/A | N/A | N/A | Deprecated on REST |
| `PartnerCPCFee` | N/A | N/A | N/A | Deprecated on REST |
| `CampaignConversionReportingColumns` | `conversionReportingColumns` | ConversionReportingColumnsConnection | Nullable | Inherited—connection via `nodes`. |
| `Availability` | `status` | CampaignStatus! | Not nullable | Operational state (`LIVE`, `PAUSED`, `ENDED`, …); not the REST archive flag alone |
| `Availability` | `isArchived` | Boolean! | Not nullable | REST `Available` → `false`; REST `Archived` → `true` |
| `CreatedAtUTC` | `createdAtUtc` | DateTime! | Not nullable | Inherited from `CampaignBase`. |
| `LastUpdatedAtUTC` | N/A | N/A | N/A | Deprecated on REST |
| `FrequencySettings` | `frequencySettings` | FrequencySettings! | Not nullable | Inherited from `CampaignBase`. |
| `PurchaseOrderNumber` | `purchaseOrderNumber` | String | Nullable | Inherited from `CampaignBase`. |
| `CtvTargetingAndAttribution` | N/A | N/A | N/A | Deprecated on REST |
| `TimeZone` | `timeZone` | String! | Not nullable | Inherited from `CampaignBase`. |
| `CurrentAndFutureAdditionalFeeCards` | `passThroughFeeCards` | PassThroughFeeCardsConnection | Nullable | Connection via `nodes`. |

## Code examples

### REST example

```
GET /v3/campaign/template/{campaignId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetCampaignTemplate($id: ID!) {
  campaign(id: $id) {
    id
    name
    isTemplatePublished
    templateShareType
    advertiser { id }
    description
    timeZone
    frequencySettings {
      lifetimeFrequencyCap
      frequencyCap
      frequencyPeriodInMinutes
    }
  }
}
```
