# POST /v3/campaign/clone → campaignClonesCreate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-campaign-clone
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/campaign/clone → campaignClonesCreate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/campaign/clone` |
| GraphQL operation | `campaignClonesCreate` |
| Input type | `CampaignCloneCreateInput` |
| Output type | `PayloadWithErrorsOfListOfCampaignCloneProgress` (`data: [CampaignCloneProgress!]`, `userErrors: [UserError!]`) |

## Multi-step operations

REST returns a single `ReferenceId` for one clone job. GraphQL `campaignClonesCreate` supports batch cloning via `campaignCloneData`—map a single REST clone to one element with `numberOfClones: 1`. Track progress with `campaignCloneProgress` (see the campaign clone status read endpoint).

## Input field mapping

Input type: `CampaignCloneCreateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `CampaignId` | `campaignCloneData[].campaignId` | String! | Required | REST single-clone maps to one `CampaignCloneDataInput` element |
| `CampaignName` | `campaignCloneData[].cloneNames[]` | String! | Required | REST single name → `cloneNames` list; set `numberOfClones: 1` |
| `TargetAdvertiserId` | `campaignCloneData[].targetAdvertiserId` | String | Optional | N/A |
| `IsBuildInProgress` | N/A | N/A | Optional | No direct GraphQL input equivalent |
| `CampaignFlights` | `campaignCloneData[].campaignFlights` | [CampaignCloneCampaignFlightInput!] | Optional | Nested flight overrides |
| `CampaignFlights.CampaignFlightId` | `campaignCloneData[].campaignFlights[].campaignFlightId` | Long | Optional | Required when overriding an existing flight |
| `CampaignFlights.StartDateInclusiveUTC` | `campaignCloneData[].campaignFlights[].startDateInclusive` | DateTime | Optional | N/A |
| `CampaignFlights.EndDateExclusiveUTC` | `campaignCloneData[].campaignFlights[].endDateExclusive` | DateTime | Optional | N/A |
| `CampaignFlights.BudgetInAdvertiserCurrency` | `campaignCloneData[].campaignFlights[].budgetInAdvertiserCurrency` | Decimal | Optional | N/A |
| `CampaignFlights.BudgetInImpressions` | `campaignCloneData[].campaignFlights[].budgetInImpressions` | Long | Optional | N/A |
| `CampaignFlights.DailyTargetInAdvertiserCurrency` | `campaignCloneData[].campaignFlights[].dailyTargetInAdvertiserCurrency` | Decimal | Optional | N/A |
| `CampaignFlights.DailyTargetInImpressions` | `campaignCloneData[].campaignFlights[].dailyTargetInImpressions` | Long | Optional | N/A |
| `CampaignFlights.CampaignId` | N/A | N/A | Optional | Not currently available in GraphQL |
| `EnableAdGroupIds` | `campaignCloneData[].selectedAdGroups[].enabled` | Boolean | Optional | For each ad group ID in the list, set `enabled: true` on the `selectedAdGroups` entry whose `adGroupId` matches. IDs must belong to the source campaign and appear in `AdGroupIds` when that list is provided. When omitted, no ad groups are enabled on clone. |
| `ImpressionsOnlyBudgetingCPM` | `campaignCloneData[].impressionsOnlyBudgetingCPM` | Decimal | Optional | N/A |
| `Objective` | `campaignCloneData[].objective` | CampaignObjective | Optional | N/A |
| `PrimaryGoal` | `campaignCloneData[].primaryGoal` | CampaignCloneROIGoalInput | Optional | Nested ROI goal |
| `PrimaryGoal.MaximizeReach` | `campaignCloneData[].primaryGoal.maximizeReach` | Boolean | Optional | N/A |
| `PrimaryGoal.MaximizeLtvIncrementalReach` | `campaignCloneData[].primaryGoal.maximizeLtvIncrementalReach` | Boolean | Optional | N/A |
| `PrimaryGoal.CPCInAdvertiserCurrency` | `campaignCloneData[].primaryGoal.cpcInAdvertiserCurrency` | Decimal | Optional | REST Money amount maps to Decimal |
| `PrimaryGoal.CTRInPercent` | `campaignCloneData[].primaryGoal.ctrInPercent` | Decimal | Optional | N/A |
| `PrimaryGoal.NielsenOTPInPercent` | `campaignCloneData[].primaryGoal.nielsenOTPInPercent` | Decimal | Optional | N/A |
| `PrimaryGoal.CPAInAdvertiserCurrency` | `campaignCloneData[].primaryGoal.cpaInAdvertiserCurrency` | Decimal | Optional | REST Money amount maps to Decimal |
| `PrimaryGoal.MaximizeConversionRevenue` | N/A | N/A | Optional | Deprecated on REST |
| `PrimaryGoal.ReturnOnAdSpendPercent` | `campaignCloneData[].primaryGoal.returnOnAdSpendPercent` | Decimal | Optional | N/A |
| `PrimaryGoal.VCRInPercent` | `campaignCloneData[].primaryGoal.vcrInPercent` | Decimal | Optional | N/A |
| `PrimaryGoal.ViewabilityInPercent` | `campaignCloneData[].primaryGoal.viewabilityInPercent` | Decimal | Optional | N/A |
| `PrimaryGoal.VCPMInAdvertiserCurrency` | `campaignCloneData[].primaryGoal.vcpmInAdvertiserCurrency` | Decimal | Optional | REST Money amount maps to Decimal |
| `PrimaryGoal.CPCVInAdvertiserCurrency` | `campaignCloneData[].primaryGoal.cpcvInAdvertiserCurrency` | Decimal | Optional | REST Money amount maps to Decimal |
| `PrimaryGoal.MiaozhenOTPInPercent` | `campaignCloneData[].primaryGoal.miaozhenOTPInPercent` | Decimal | Optional | N/A |
| `PrimaryGoal.NewBuyerTargetValue` | `campaignCloneData[].primaryGoal.newBuyerTargetValue` | Int | Optional | N/A |
| `SecondaryGoal` | `campaignCloneData[].secondaryGoal` | CampaignCloneROIGoalInput | Optional | Same nested fields as PrimaryGoal |
| `TertiaryGoal` | `campaignCloneData[].tertiaryGoal` | CampaignCloneROIGoalInput | Optional | Same nested fields as PrimaryGoal |
| `PrimaryChannel` | `campaignCloneData[].channel` | CampaignChannel | Optional | REST `PrimaryChannel` → GraphQL `channel` |
| `AdGroupIds` | `campaignCloneData[].selectedAdGroups[].adGroupId` | String! | Optional | N/A |
| `ShouldCloneAdGroupBudgets` | `campaignCloneData[].shouldCloneAdGroupBudgets` | Boolean | Optional | N/A |
| `Version` | N/A | N/A | Optional | Not exposed in GraphQL clone mutation |
| `MarketplaceOptOut` | `campaignCloneData[].defaultUseInventoryMarketPlace` | Boolean | Optional | Inverse semantics: REST `MarketplaceOptOut: true` (opt out of marketplace) maps to `defaultUseInventoryMarketPlace: false`; passing the same boolean value without inversion applies the opposite marketplace behavior |

## Output field mapping

Output type: `CampaignCloneProgress` (returned as `data` on `CampaignCloneCreatePayload`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `ReferenceId` | `id` | Long! | Not nullable | Track progress via `campaignCloneProgress` query |

## Endpoint-specific nested types and enums

### CampaignCloneAdGroupInput

Nested under `campaignCloneData[].selectedAdGroups`.

| GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- |
| `adGroupId` | String! | Required | REST `AdGroupIds[]` or each ID in `EnableAdGroupIds` |
| `enabled` | Boolean | Optional | Set `true` for each ID listed in `EnableAdGroupIds` |

### CampaignCloneROIGoalInput

Maps REST `ROIGoal` leaf fields (see `PrimaryGoal.*` rows above). GraphQL-only fields not present on REST `ROIGoal`: `crossixAudienceQualityIndex`, `crossixCostPerTarget`, `iqviaAudienceQualityIndex`, `iqviaAudienceQualityIndexAndCostPerTarget`.

### CampaignCloneCampaignFlightInput

| REST field (`CampaignFlight`) | GraphQL field | GraphQL type |
| --- | --- | --- |
| CampaignFlightId | `campaignFlightId` | Long |
| StartDateInclusiveUTC | `startDateInclusive` | DateTime |
| EndDateExclusiveUTC | `endDateExclusive` | DateTime |
| BudgetInAdvertiserCurrency | `budgetInAdvertiserCurrency` | Decimal |
| BudgetInImpressions | `budgetInImpressions` | Long |
| DailyTargetInAdvertiserCurrency | `dailyTargetInAdvertiserCurrency` | Decimal |
| DailyTargetInImpressions | `dailyTargetInImpressions` | Long |
| CampaignId | N/A | N/A |
| N/A | `budgetInOutcomes` | Long |

## Code examples

### REST example

```
POST /v3/campaign/clone HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "CampaignId": "camp123",
  "CampaignName": "Clone of Summer Sale",
  "TargetAdvertiserId": "adv456",
  "IsBuildInProgress": true
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
  campaignClonesCreate(
    input: {
      campaignCloneData: [
        {
          campaignId: "camp123"
          cloneNames: ["Clone of Summer Sale"]
          numberOfClones: 1
          targetAdvertiserId: "adv456"
        }
      ]
    }
  ) {
    data {
      id
    }
    userErrors {
      message
      field
    }
  }
}
```
