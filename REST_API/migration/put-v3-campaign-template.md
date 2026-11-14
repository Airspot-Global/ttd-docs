# PUT /v3/campaign/template → campaignUpdate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/put-v3-campaign-template
- Retrieved: 2026-11-14
- Category: REST_API

---

# PUT /v3/campaign/template → campaignUpdate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `PUT /v3/campaign/template` |
| GraphQL operation | `campaignUpdate` |
| Input type | `CampaignUpdateInput` |
| Output type | `PayloadWithErrorsOfCampaign` (`data: Campaign`, `userErrors: [UserError!]`) |

## Multi-step operations

REST `PUT /v3/campaign/template` updates template-specific fields including publish and share settings. GraphQL `campaignUpdate` covers overlapping campaign fields only; template publish (`IsTemplatePublished`) and share type (`ShareType`) are read-only on `Campaign`—no update input fields exist for those in the current schema.

| REST field | GraphQL coverage |
| --- | --- |
| `IsTemplatePublished` | Read via `Campaign.isTemplatePublished`—no update input |
| `ShareType` | Read via `Campaign.templateShareType`—no update input |
| `AdvertiserId` | Create-only |
| PartnerCostPercentageFee, PartnerCPMFee, PartnerCPCFee | Create-only |
| Availability, FrequencySettings | Create-only |

## Input field mapping

Input type: `CampaignUpdateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | N/A | N/A | Optional | Create-only |
| `CampaignId` | `id` | String! | Required | N/A |
| `CampaignName` | `name` | String | Optional | N/A |
| `Description` | `description` | String | Optional | N/A |
| `PartnerCostPercentageFee` | N/A | N/A | Optional | Create-only |
| `PartnerCPMFee` | N/A | N/A | Optional | Create-only |
| `PartnerCPCFee` | N/A | N/A | Optional | Create-only |
| `CampaignConversionReportingColumns` | `campaignConversionReportingColumns` | [CampaignConversionReportingColumnInput!] | Optional | N/A |
| `Availability` | N/A | N/A | Optional | Create-only |
| `FrequencySettings` | N/A | N/A | Optional | Create-only |
| `PurchaseOrderNumber` | `purchaseOrderNumber` | String | Optional | N/A |
| `TimeZone` | `timeZone` | String | Optional | N/A |
| `IsTemplatePublished` | N/A | N/A | Optional | Read on `Campaign.isTemplatePublished`; no update input |
| `ShareType` | N/A | N/A | Optional | Read on `Campaign.templateShareType`; no update input |

## Output field mapping

Output type: `Campaign` (returned as `data` on `PayloadWithErrorsOfCampaign`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | `advertiser.id` | String! | Not nullable | N/A |
| `CampaignId` | `id` | ID! | Not nullable | N/A |
| `CampaignName` | `name` | String! | Not nullable | N/A |
| `Description` | `description` | String | Nullable | N/A |
| `PartnerCostPercentageFee` | `partnerCostPercentageFee` | Decimal! | Not nullable | N/A |
| `PartnerCPMFee` | N/A | N/A | N/A | Not currently available in GraphQL |
| `PartnerCPCFee` | N/A | N/A | N/A | Not currently available in GraphQL |
| `CampaignConversionReportingColumns` | `conversionReportingColumns` | ConversionReportingColumnsConnection | Nullable | Use `nodes { … }` |
| `Availability` | `isArchived` | Boolean! | Not nullable | REST `Available` → `false`; REST `Archived` → `true`. Not `Campaign.status` (operational state: `LIVE`, `PAUSED`, `ENDED`, …) |
| `CtvTargetingAndAttribution` | N/A | N/A | N/A | Not currently available in GraphQL |
| `CreatedAtUTC` | `createdAtUtc` | DateTime! | Not nullable | N/A |
| `LastUpdatedAtUTC` | `lastUpdatedAtUtc` | DateTime! | Not nullable | N/A |
| `FrequencySettings` | `frequencySettings` | FrequencySettings! | Not nullable | N/A |
| `PurchaseOrderNumber` | `purchaseOrderNumber` | String | Nullable | N/A |
| `TimeZone` | `timeZone` | String! | Not nullable | N/A |
| `IsTemplatePublished` | `isTemplatePublished` | Boolean | Nullable | N/A |
| `ShareType` | `templateShareType` | ShareType | Nullable | N/A |
| `CurrentAndFutureAdditionalFeeCards` | `passThroughFeeCards` | PassThroughFeeCardsConnection | Nullable | Use `nodes { … }` |

## Code examples

### REST example

```
PUT /v3/campaign/template HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "CampaignId": "camp123",
  "AdvertiserId": "adv456",
  "CampaignName": "Updated Template",
  "Description": "Template description"
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation {
  campaignUpdate(
    input: {
      id: "camp123"
      name: "Updated Template"
      description: "Template description"
    }
  ) {
    data {
      id
      name
      description
      isTemplatePublished
      templateShareType
    }
    userErrors {
      message
      field
    }
  }
}
```
