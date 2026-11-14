# PUT /v3/campaign → campaignUpdate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/put-v3-campaign
- Retrieved: 2026-11-14
- Category: REST_API

---

# PUT /v3/campaign → campaignUpdate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `PUT /v3/campaign` |
| GraphQL operation | `campaignUpdate` |
| Input type | `CampaignUpdateInput` |
| Output type | `PayloadWithErrorsOfCampaign` (`data: Campaign`, `userErrors: [UserError!]!`) |

## Multi-step operations

| REST-only behavior | GraphQL target |
| --- | --- |
| `Budget`, `DailyBudget`, `PacingMode`, flight dates | `campaignFlightUpdate`, `campaignBudgetSettingsUpdate`, or `campaignPacingSettingsUpdate` |
| `Availability` | Create-only |
| `FrequencySettings`, `NewFrequencyConfigs` | Create-only |
| `AssociatedBidLists`, `DefaultBidLists` | `campaignAssociateBidList` |
| `PartnerCostPercentageFee`, `PartnerCPMFee`, `PartnerCPCFee` | Create-only |
| `CampaignName` | `name` on `CampaignUpdateInput` |
| `CustomLabels` (assigned-label objects) | `customLabelNames` (replaces full label list) |

## Input field mapping

Input type: `CampaignUpdateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `CampaignId` | `id` | String! | Required | RequiredOnUpdate |
| `AdvertiserId` | N/A | N/A | Optional | Create-only |
| `CampaignName` | `name` | String | Optional | N/A |
| `Description` | `description` | String | Optional | N/A |
| `PartnerCostPercentageFee` | N/A | N/A | Optional | Create-only |
| `PartnerCPMFee` | N/A | N/A | Optional | Deprecated on REST |
| `PartnerCPCFee` | N/A | N/A | Optional | Deprecated on REST |
| `CampaignConversionReportingColumns` | `campaignConversionReportingColumns` | [CampaignConversionReportingColumnInput!] | Optional | N/A |
| `Availability` | N/A | N/A | Optional | Create-only |
| `FrequencySettings` | N/A | N/A | Optional | Create-only |
| `PurchaseOrderNumber` | `purchaseOrderNumber` | String | Optional | N/A |
| `CtvTargetingAndAttribution` | N/A | N/A | Optional | Create-only |
| `TimeZone` | `timeZone` | String | Optional | Windows time zone ID on update |
| `Budget` | N/A | N/A | Optional | Use flight/budget mutations |
| `BudgetInImpressions` | N/A | N/A | Optional | Use flight/budget mutations |
| `ImpressionsOnlyBudgetingCpm` | N/A | N/A | Optional | Create-only |
| `DailyBudget` | N/A | N/A | Optional | Use flight mutations |
| `DailyBudgetInImpressions` | N/A | N/A | Optional | Use flight mutations |
| `StartDate` | N/A | N/A | Optional | Use `campaignFlightUpdate` |
| `EndDate` | N/A | N/A | Optional | Use `campaignFlightUpdate` |
| `PacingMode` | N/A | N/A | Optional | Use pacing mutations |
| `AutoAllocatorEnabled` | N/A | N/A | Optional | Deprecated on REST |
| `AutoPrioritizationEnabled` | N/A | N/A | Optional | Deprecated on REST |
| `MinimumAdGroupSpendInAdvertiserCurrency` | N/A | N/A | Optional | Deprecated on REST |
| `CampaignFlights` | N/A | N/A | Optional | InvalidOnUpdate; use `campaignFlightUpdate` / flight mutations |
| `IsMediaOceanCampaign` | N/A | N/A | Optional | Create-only |
| `IsBuildInProgress` | N/A | N/A | Optional | Create-only |
| `IncludeDefaultsFromAdvertiser` | N/A | N/A | Optional | POST-only / InvalidOnUpdate |
| `AdditionalFeeCardOnCreate` | N/A | N/A | Optional | Create-only |
| `CustomLabels` | `customLabelNames` | [String!] | Optional | Replaces entire label list |
| `CustomCPAType` | `customCPAType` | CustomCPAType | Optional | N/A |
| `CustomCPAType` | `customCPATypeInput` | CustomCPATypeInput | Optional | GraphQL alternative enum input for the same REST field; supply one of `customCPAType` or `customCPATypeInput` |
| `CustomCPAClickWeight` | `customCPAClickWeight` | Decimal | Optional | N/A |
| `CustomCPAViewthroughWeight` | `customCPAViewthroughWeight` | Decimal | Optional | N/A |
| `CustomROASType` | `customRoasType` | CustomROASType | Optional | N/A |
| `AssociatedBidLists` | N/A | N/A | Optional | Use `campaignAssociateBidList` |
| `DefaultBidLists` | N/A | N/A | Optional | Create-only |
| `CampaignType` | N/A | N/A | Optional | Create-only |
| `BallotMeasureProfile` | `ballotMeasureProfile` | BallotMeasureProfileInput | Optional | N/A |
| `IsBallotMeasure` | `isBallotMeasure` | Boolean | Optional | N/A |
| `Increments` | `increments` | [String!] | Optional | Frequency counter IDs |
| `NewFrequencyConfigs` | N/A | N/A | Optional | Create-only |
| `Objective` | N/A | N/A | Optional | Deprecated on REST |
| `PrimaryGoal` | `primaryGoal` | CampaignCreateROIGoalInput | Optional | N/A |
| `SecondaryGoal` | `secondaryGoal` | CampaignCreateROIGoalInput | Optional | N/A |
| `TertiaryGoal` | `tertiaryGoal` | CampaignCreateROIGoalInput | Optional | N/A |
| `PrimaryChannel` | `primaryChannel` | CampaignChannelType | Optional | N/A |
| `RTBAttributes` | N/A | N/A | Optional | Create-only |
| `EnabledValueAddedProviders` | N/A | N/A | Optional | Deprecated on REST |
| `EnabledValueAddedProviderIds` | `enabledValueAddedProviderIds` | [ID!] | Optional | N/A |
| `Version` | N/A | N/A | Optional | Read-only |

### GraphQL-only input fields (no REST equivalent)

| GraphQL field | GraphQL type | Description |
| --- | --- | --- |
| `adGroupDefaultNielsenSettings` | AdGroupDefaultNielsenSettingsInput |  |
| `campaignIncrementalReachSetting` | IncrementalReachCampaignSettingInput |  |
| `ioContractId` | Long |  |
| `isIPResolutionEnabled` | Boolean |  |
| `isManagedByTTD` | Boolean |  |
| `lastTouchAttributionMeasuredByTheTradeDesk` | Boolean |  |
| `pharmaCampaignBrandProductSettings` | PharmaCampaignBrandProductSettingsInput |  |
| `tradingModeSettingsInput` | CampaignUpdateTradingModeSettingsInput |  |
| `userBidFactorsAsMaxBidEnabled` | Boolean |  |
| `userDataFeatureEnabled` | Boolean |  |
| `validateInputOnly` | Boolean | Validate without executing |

## Output field mapping

Output type: `Campaign` (returned as `data` on `PayloadWithErrorsOfCampaign`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | `advertiser.id` | String! | Not nullable | N/A |
| `CampaignId` | `id` | ID! | Not nullable | N/A |
| `CampaignName` | `name` | String! | Not nullable | N/A |
| `Description` | `description` | String | Nullable | N/A |
| `PartnerCostPercentageFee` | `partnerCostPercentageFee` | Decimal! | Not nullable | N/A |
| `PartnerCPMFee` | N/A | N/A | N/A | Deprecated on REST |
| `PartnerCPCFee` | N/A | N/A | N/A | Deprecated on REST |
| `CampaignConversionReportingColumns` | `conversionReportingColumns` | ConversionReportingColumnsConnection | Nullable | Use `nodes { … }` |
| `Availability` | `isArchived` | Boolean! | Not nullable | REST `Available` → `false`; REST `Archived` → `true` |
| `CtvTargetingAndAttribution` | N/A | N/A | N/A | Deprecated on REST |
| `CreatedAtUTC` | `createdAtUtc` | DateTime! | Not nullable | N/A |
| `LastUpdatedAtUTC` | `lastUpdatedAtUtc` | DateTime! | Not nullable | N/A |
| `FrequencySettings` | `frequencySettings` | FrequencySettings! | Not nullable | N/A |
| `PurchaseOrderNumber` | `purchaseOrderNumber` | String | Nullable | N/A |
| `TimeZone` | `timeZone` | String! | Not nullable | N/A |
| `Budget` | `budget.total` | Decimal! | Not nullable | REST Money amount → `CampaignBudget.total` |
| `BudgetInImpressions` | `budget.totalInImpressions` | Decimal | Nullable | Alternative top-level `budgetInImpressions` also exists on `Campaign`. |
| `ImpressionsOnlyBudgetingCpm` | `impressionsOnlyBudgetingCPM` | Decimal! | Not nullable | N/A |
| `DailyBudget` | N/A | N/A | N/A | Nested under `budget` / `flights` |
| `DailyBudgetInImpressions` | N/A | N/A | N/A | Not a top-level `Campaign` field |
| `StartDate` | `startDate` | DateTime! | Not nullable | N/A |
| `EndDate` | `endDate` | DateTime | Nullable | N/A |
| `AutoAllocatorEnabled` | `autoAllocatorEnabled` | Boolean! | Not nullable | N/A |
| `AutoPrioritizationEnabled` | `autoPrioritizationEnabled` | Boolean! | Not nullable | N/A |
| `MinimumAdGroupSpendInAdvertiserCurrency` | `minimumAdGroupSpendInAdvertiserCurrency` | Decimal! | Not nullable | N/A |
| `PacingMode` | `pacingMode` | CampaignPacingMode! | Not nullable | N/A |
| `CampaignFlights` | `flights` | FlightsConnection | Nullable | Use `nodes { … }` |
| `CustomLabels` | `customLabels` | CustomLabelsConnection | Nullable | Use `nodes { … }` |
| `CustomCPAType` | `customCPAType` | CustomCPAType! | Not nullable | N/A |
| `CustomCPAClickWeight` | `customCPAClickWeight` | Decimal | Nullable | N/A |
| `CustomCPAViewthroughWeight` | `customCPAViewthroughWeight` | Decimal | Nullable | N/A |
| `CustomROASType` | `customROASType` | CustomROASType! | Not nullable | N/A |
| `IsBuildInProgress` | `isBuildInProgress` | Boolean! | Not nullable | Not clearable via `campaignUpdate` |
| `IsMediaOceanCampaign` | `isMediaOceanCampaign` | Boolean | Nullable | N/A |
| `AssociatedBidLists` | `associatedBidLists` | AssociatedBidListsConnection | Nullable | Use `nodes { … }` |
| `DefaultBidLists` | `defaultBidLists` | DefaultBidListsConnection | Nullable | BidListId → connection `nodes[].id`. |
| `CurrentAndFutureAdditionalFeeCards` | `passThroughFeeCards` | PassThroughFeeCardsConnection | Nullable | Use `nodes { … }` |
| `CampaignType` | `type` | CampaignType | Nullable | N/A |
| `BallotMeasureProfile` | N/A | N/A | N/A | Write-only |
| `IsBallotMeasure` | `isBallotMeasure` | Boolean | Nullable | N/A |
| `Increments` | `increments` | [Increment] | Nullable | N/A |
| `NewFrequencyConfigs` | `frequencyConfigs` | [FrequencyConfig!]! | Not nullable | Populated on update response when `NewFrequencyConfigs` were provided in the request; `GetAPIModel` leaves the field default on GET. |
| `Objective` | `objective` | CampaignObjective! | Not nullable | N/A |
| `PrimaryGoal` | `primaryGoal` | Goal! | Not nullable | N/A |
| `SecondaryGoal` | `secondaryGoal` | Goal! | Not nullable | N/A |
| `TertiaryGoal` | `tertiaryGoal` | Goal! | Not nullable | N/A |
| `PrimaryChannel` | `channelType` | CampaignChannelType! | Not nullable | N/A |
| `RTBAttributes` | N/A | N/A | N/A | Not currently available in GraphQL |
| `RTBAttributes.AudienceTargeting` | N/A | N/A | N/A | Not currently available in GraphQL |
| `RTBAttributes.AudienceTargeting.TargetDemographicSettings` | N/A | N/A | N/A | Not currently available in GraphQL |
| `EnabledValueAddedProviders` | `enabledValueAddedProviders` | [ValueAddedProviderInfo!]! | Not nullable | N/A |
| `EnabledValueAddedProviderIds` | `enabledValueAddedProviders[].id` | ID! | Not nullable | N/A |
| `Version` | `version` | CampaignVersion | Nullable | N/A |
| `TradingModeDetails` | `tradingModeDetails` | CampaignTradingModeDetails! | Not nullable | N/A |

## Endpoint-specific nested types and enums

### CampaignConversionReportingColumnInput

Nested under `campaignConversionReportingColumns`.

| GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- |
| `trackingTagId` | String! | Required | REST `TrackingTagId` |
| `reportingColumnId` | Int! | Required | REST `ReportingColumnId` |
| `includeInCustomCPA` | Boolean! | Required | REST `IncludeInCustomCPA` |
| `weight` | Decimal | Optional | REST `Weight` |
| `crossDeviceAttributionModelId` | String | Optional | N/A |
| `customROASConfig` | CustomROASConfigInput | Optional | Nested custom ROAS settings |
| `productListReportingType` | ProductListReportingTypeInput | Optional | N/A |

### CustomROASConfigInput

Nested under `CampaignConversionReportingColumnInput.customROASConfig`.

| GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- |
| `includeInCustomROAS` | Boolean! | Required | N/A |
| `customROASWeight` | Decimal | Optional | N/A |
| `customROASClickWeight` | Decimal | Optional | N/A |
| `customROASViewthroughWeight` | Decimal | Optional | N/A |

### CampaignCreateROIGoalInput

Nested under `primaryGoal`, `secondaryGoal`, `tertiaryGoal`. Set exactly one goal metric field.

| GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- |
| `maximizeReach` | Boolean | Optional | Reach goal; exactly one goal metric field per goal object (mutually exclusive) |
| `maximizeLtvIncrementalReach` | Boolean | Optional | Incremental reach goal; exactly one goal metric field per goal object (mutually exclusive) |
| `cpaInAdvertiserCurrency` | Decimal | Optional | CPA goal; exactly one goal metric field per goal object (mutually exclusive) |
| `cpcInAdvertiserCurrency` | Decimal | Optional | CPC goal; exactly one goal metric field per goal object (mutually exclusive) |
| `returnOnAdSpendPercent` | Decimal | Optional | ROAS goal; exactly one goal metric field per goal object (mutually exclusive) |
| `viewabilityInPercent` | Decimal | Optional | Viewability goal; exactly one goal metric field per goal object (mutually exclusive) |
| `vcrInPercent` | Decimal | Optional | Video completion rate goal; exactly one goal metric field per goal object (mutually exclusive) |
| `ctrInPercent` | Decimal | Optional | CTR goal; exactly one goal metric field per goal object (mutually exclusive) |

### BallotMeasureProfileInput

Nested under `ballotMeasureProfile`.

| GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- |
| `audienceDescription` | String | Optional | N/A |
| `electionState` | UsStateInput | Optional | N/A |
| `fileLocationInS3` | String | Optional | Required for some states |
| `geoDescription` | String | Optional | N/A |
| `isAdvertiserIEC` | Boolean | Optional | N/A |
| `payingEntityAddress` | String | Optional | N/A |
| `payingEntityExecutiveName` | String | Optional | N/A |
| `payingEntityExecutiveTitle` | String | Optional | N/A |
| `payingEntityName` | String | Optional | N/A |
| `politicalDataId` | ID | Optional | N/A |

### CampaignBudget

Nested under `budget` on the response `Campaign`.

| GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- |
| `total` | Decimal! | Not nullable | REST `Budget` amount |
| `totalInImpressions` | Decimal | Nullable | REST impressions budget cap |
| `version` | CampaignBudgetingVersion! | Not nullable | REST `BudgetingVersion` |
| `adGroupSpendPrioritizationType` | AdGroupSpendPrioritizationType! | Not nullable | N/A |
| `allocationMode` | CampaignBudgetAllocationMode! | Not nullable | N/A |
| `currentOrUpComing` | Decimal! | Not nullable | Current or next upcoming flight budget |
| `outcomeGoalType` | OutcomeGoalType | Nullable | N/A |
| `pacingMode` | CampaignPacingMode! | Not nullable | N/A |
| `spendMode` | CampaignBudgetSpendMode | Nullable | N/A |
| `spendStrategy` | KoaSpendStrategy | Nullable | N/A |
| `totalInOutcomes` | Long | Nullable | N/A |
| `usesImpressionBudgets` | Boolean! | Not nullable | N/A |
| `usesMaximumAllocationType` | Boolean! | Not nullable | N/A |

### Increment

Elements of `increments` on the response `Campaign` (input `increments` accepts counter IDs as `[String!]`).

| GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- |
| `creationDateUtc` | DateTime! | Not nullable | N/A |
| `frequencyCounter` | FrequencyCounter | Nullable | Use `frequencyCounter { id name }` for counter ID |

### BallotMeasureProfile

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `PoliticalDataId` | N/A | N/A | N/A | Write-only |
| `ElectionState` | N/A | N/A | N/A | Write-only |
| `PayingEntityName` | N/A | N/A | N/A | Write-only |
| `PayingEntityAddress` | N/A | N/A | N/A | Write-only |
| `PayingEntityExecutiveName` | N/A | N/A | N/A | Write-only |
| `PayingEntityExecutiveTitle` | N/A | N/A | N/A | Write-only |
| `GeoDescription` | N/A | N/A | N/A | Write-only |
| `AudienceDescription` | N/A | N/A | N/A | Write-only |
| `IsAdvertiserIEC` | N/A | N/A | N/A | Write-only |
| `FileLocationInS3` | N/A | N/A | N/A | Write-only |

### TargetDemographicSettings

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AudienceTargeting` | N/A | N/A | N/A | Not currently available in GraphQL |
| `TargetDemographicSettings` | N/A | N/A | N/A | Not currently available in GraphQL |
| `TargetDemographicSettings.DataRateType` | N/A | N/A | N/A | Not currently available in GraphQL |
| `TargetDemographicSettings.CountryCode` | N/A | N/A | N/A | Not currently available in GraphQL |
| `TargetDemographicSettings.Gender` | N/A | N/A | N/A | Not currently available in GraphQL |
| `TargetDemographicSettings.StartAge` | N/A | N/A | N/A | Not currently available in GraphQL |
| `TargetDemographicSettings.EndAge` | N/A | N/A | N/A | Not currently available in GraphQL |

## Code examples

### REST example

```
PUT /v3/campaign HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "CampaignId": "camp123",
  "CampaignName": "Updated Campaign Name",
  "Description": "Updated description"
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation UpdateCampaign($input: CampaignUpdateInput!) {
  campaignUpdate(input: $input) {
    data {
      id
      name
      description
      lastUpdatedAtUtc
    }
    userErrors {
      message
      field
    }
  }
}
```

Variables:

```
{
  "input": {
    "id": "camp123",
    "name": "Updated Campaign Name",
    "description": "Updated description"
  }
}
```

Budget, pacing, flights, availability, and associated bid lists from the REST body require separate GraphQL mutations not covered by `campaignUpdate`.
