# POST /v3/campaign → campaignCreate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-campaign
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/campaign → campaignCreate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/campaign` |
| GraphQL operation | `campaignCreate` |
| Input type | `CampaignCreateInput` |
| Output type | `PayloadWithErrorsOfCampaign` (`data: Campaign`, `userErrors: [UserError!]!`) |

## Multi-step operations

| REST-only behavior | GraphQL target |
| --- | --- |
| `AssociatedBidLists` on create | `campaignAssociateBidList` after create |
| `IsBuildInProgress` | REST transport only |
| Top-level `Budget`, `StartDate`, `EndDate` without `CampaignFlights` | GraphQL requires `flights` on `CampaignCreateInput`; map REST dates/budgets into `flights[]` |
| `CampaignName` | `name` on `CampaignCreateInput` |
| `CustomLabels` (assigned-label objects) | `customLabelNames` (label name strings only) |
| `NewFrequencyConfigs` | `frequencyConfigs` (different input shape—see `FrequencyConfigInput`) |
| `AdditionalFeeCardOnCreate` | `passThroughFeeCard` |

## Input field mapping

Input type: `CampaignCreateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | `advertiserId` | String! | Required | RequiredOnCreate |
| `CampaignName` | `name` | String! | Required | RequiredOnCreate |
| `Description` | `description` | String | Optional | N/A |
| `PartnerCostPercentageFee` | N/A | N/A | Optional | Not currently available in GraphQL |
| `PartnerCPMFee` | N/A | N/A | Optional | Deprecated on REST |
| `PartnerCPCFee` | N/A | N/A | Optional | Deprecated on REST |
| `CampaignConversionReportingColumns` | `campaignConversionReportingColumns` | [CampaignConversionReportingColumnInput!] | Optional | Required on REST create; optional on GraphQL create but typically set |
| `Availability` | N/A | N/A | Optional | Not currently available in GraphQL |
| `FrequencySettings` | N/A | N/A | Optional | Use `frequencyConfigs` instead (different shape) |
| `PurchaseOrderNumber` | `purchaseOrderNumber` | String | Optional | N/A |
| `CtvTargetingAndAttribution` | N/A | N/A | Optional | Create-only |
| `TimeZone` | `timeZone` | IANATimeZone | Optional | GraphQL uses IANA/Olson format |
| `Budget` | `flights[].budgetInAdvertiserCurrency` | Decimal! | Optional | Campaign-level budget maps into flight budget when flights are provided |
| `BudgetInImpressions` | `flights[].budgetInImpressions` | Long | Optional | Per-flight impressions budget |
| `ImpressionsOnlyBudgetingCpm` | `impressionsOnlyBudgetingCpm` | Decimal | Optional | N/A |
| `DailyBudget` | `flights[].dailyTargetInAdvertiserCurrency` | Decimal | Optional | Per-flight daily target |
| `DailyBudgetInImpressions` | `flights[].dailyTargetInImpressions` | Long | Optional | Per-flight daily impressions target |
| `StartDate` | `flights[].startDateInclusiveUTC` | DateTime! | Optional | Required on each flight when flights are used |
| `EndDate` | `flights[].endDateExclusiveUTC` | DateTime | Optional | N/A |
| `PacingMode` | `pacingMode` | CampaignPacingMode | Optional | N/A |
| `AutoAllocatorEnabled` | N/A | N/A | Optional | Deprecated on REST |
| `AutoPrioritizationEnabled` | N/A | N/A | Optional | Deprecated on REST |
| `MinimumAdGroupSpendInAdvertiserCurrency` | N/A | N/A | Optional | Deprecated on REST |
| `CampaignFlights` | `flights` | [FlightCreateInput!]! | Required | Required on GraphQL create (at least one flight) |
| `IsMediaOceanCampaign` | N/A | N/A | Optional | Not currently available in GraphQL |
| `CustomLabels` | `customLabelNames` | [String!] | Optional | GraphQL accepts label names only |
| `CustomCPAType` | `customCPAType` | CustomCPAType | Optional | N/A |
| `CustomCPAType` | `customCPATypeInput` | CustomCPATypeInput | Optional | GraphQL alternative enum input for the same REST field; supply one of `customCPAType` or `customCPATypeInput` |
| `CustomCPAClickWeight` | `customCPAClickWeight` | Decimal | Optional | N/A |
| `CustomCPAViewthroughWeight` | `customCPAViewthroughWeight` | Decimal | Optional | N/A |
| `CustomROASType` | `customRoasType` | CustomROASType | Optional | N/A |
| `IsBuildInProgress` | N/A | N/A | Optional | Create-only |
| `AssociatedBidLists` | N/A | N/A | Optional | Use `campaignAssociateBidList` after create |
| `IncludeDefaultsFromAdvertiser` | `includeDefaultsFromAdvertiser` | Boolean! | Required | Required on GraphQL create (defaults to `false` when omitted on REST) |
| `DefaultBidLists` | `defaultBidLists` | [DefaultBidListInput!] | Optional | N/A |
| `AdditionalFeeCardOnCreate` | `passThroughFeeCard` | CampaignCreatePassThroughFeeCardInput | Optional | N/A |
| `CampaignType` | `campaignType` | CampaignType! | Required | Required on GraphQL create |
| `BallotMeasureProfile` | `ballotMeasureProfile` | BallotMeasureProfileInput | Optional | N/A |
| `IsBallotMeasure` | `isBallotMeasure` | Boolean | Optional | N/A |
| `Increments` | `increments` | [String!] | Optional | Frequency counter IDs |
| `NewFrequencyConfigs` | `frequencyConfigs` | [FrequencyConfigInput!] | Optional | Different input shape |
| `Objective` | N/A | N/A | Optional | Deprecated on REST |
| `PrimaryGoal` | `primaryGoal` | CampaignCreateROIGoalInput! | Required | Required on GraphQL create |
| `SecondaryGoal` | `secondaryGoal` | CampaignCreateROIGoalInput | Optional | N/A |
| `TertiaryGoal` | `tertiaryGoal` | CampaignCreateROIGoalInput | Optional | N/A |
| `PrimaryChannel` | `primaryChannel` | CampaignChannelType! | Required | Required on GraphQL create |
| `RTBAttributes` | N/A | N/A | Optional | Not currently available in GraphQL |
| `EnabledValueAddedProviders` | N/A | N/A | Optional | Deprecated on REST |
| `EnabledValueAddedProviderIds` | `enabledValueAddedProviderIds` | [ID!] | Optional | N/A |
| `Version` | N/A | N/A | Optional | Read-only |

### GraphQL-only input fields (no REST equivalent)

| GraphQL field | GraphQL type | Description |
| --- | --- | --- |
| `campaignGroupId` | Long |  |
| `campaignIncrementalReachSetting` | IncrementalReachCampaignSettingInput |  |
| `campaignRetailBrandSettings` | KokaiCampaignRetailBrandSettingsInput |  |
| `iOContractId` | Long |  |
| `isManagedByTTD` | Boolean |  |
| `lastTouchAttributionMeasuredByTheTradeDesk` | Boolean |  |
| `outcomeGoalType` | OutcomeGoalTypeInput |  |
| `pharmaCampaignBrandProductSettings` | PharmaCampaignBrandProductSettingsInput |  |
| `tradingModeSettingsInput` | CampaignCreateTradingModeSettingsInput |  |
| `userBidFactorsAsMaxBidEnabled` | Boolean |  |
| `validateInputOnly` | Boolean | Validate without executing |
| `callerSource` | String |  |

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
| `DailyBudget` | N/A | N/A | N/A | Nested under `budget` / `flights` on `Campaign` |
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
| `IsBuildInProgress` | `isBuildInProgress` | Boolean! | Not nullable | N/A |
| `IsMediaOceanCampaign` | `isMediaOceanCampaign` | Boolean | Nullable | N/A |
| `AssociatedBidLists` | `associatedBidLists` | AssociatedBidListsConnection | Nullable | Use `nodes { … }` |
| `DefaultBidLists` | `defaultBidLists` | DefaultBidListsConnection | Nullable | BidListId → connection `nodes[].id`. |
| `CurrentAndFutureAdditionalFeeCards` | `passThroughFeeCards` | PassThroughFeeCardsConnection | Nullable | Use `nodes { … }` |
| `AdditionalFeeCardOnCreate` | N/A | N/A | N/A | Create input only; read via `passThroughFeeCards` |
| `CampaignType` | `type` | CampaignType | Nullable | N/A |
| `BallotMeasureProfile` | N/A | N/A | N/A | Write-only |
| `IsBallotMeasure` | `isBallotMeasure` | Boolean | Nullable | N/A |
| `Increments` | `increments` | [Increment] | Nullable | N/A |
| `NewFrequencyConfigs` | `frequencyConfigs` | [FrequencyConfig!]! | Not nullable | Populated on create response when `NewFrequencyConfigs` were provided in the request; `GetAPIModel` leaves the field default on GET. |
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

### FlightCreateInput

Nested under `CampaignCreateInput.flights`.

| GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- |
| `startDateInclusiveUTC` | DateTime! | Required | REST `CampaignFlights[].StartDateInclusiveUTC` or top-level `StartDate` |
| `endDateExclusiveUTC` | DateTime | Optional | REST `EndDateExclusiveUTC` or top-level `EndDate` |
| `budgetInAdvertiserCurrency` | Decimal! | Required | REST flight `BudgetInAdvertiserCurrency` or top-level `Budget.Amount` |
| `budgetInImpressions` | Long | Optional | N/A |
| `dailyTargetInAdvertiserCurrency` | Decimal | Optional | REST `DailyTargetInAdvertiserCurrency` or top-level `DailyBudget` |
| `dailyTargetInImpressions` | Long | Optional | N/A |
| `budgetInOutcomes` | Long | Optional | GraphQL-only outcomes budgeting |

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

### FrequencyConfigInput

Nested under `frequencyConfigs` (maps from REST `NewFrequencyConfigs`).

| GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- |
| `counterName` | String! | Required | REST `CounterName` |
| `resetIntervalInMinutes` | Int! | Required | REST `ResetIntervalInMinutes` |
| `frequencyCap` | Int | Optional | REST `FrequencyCap` |
| `frequencyGoal` | Int | Optional | REST `FrequencyGoal` |

### DefaultBidListInput

Nested under `defaultBidLists`.

| GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- |
| `bidListId` | ID! | Required | REST `BidListId` |

### CampaignCreatePassThroughFeeCardInput

Nested under `passThroughFeeCard` (maps from REST `AdditionalFeeCardOnCreate`).

| GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- |
| `passThroughFees` | [CampaignCreatePassThroughFeesInput!]! | Required | Fee line items |
| `startDateUtc` | DateTime | Optional | Effective start date |

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
POST /v3/campaign HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserId": "adv123",
  "CampaignName": "Summer Sale",
  "CampaignConversionReportingColumns": [
    {
      "TrackingTagId": "tag1",
      "ReportingColumnId": 1,
      "IncludeInCustomCPA": true
    }
  ],
  "CampaignFlights": [
    {
      "StartDateInclusiveUTC": "2026-07-01T00:00:00Z",
      "EndDateExclusiveUTC": "2026-09-01T00:00:00Z",
      "BudgetInAdvertiserCurrency": 10000.00
    }
  ],
  "PrimaryChannel": "Display",
  "PrimaryGoal": { "MaximizeReach": true }
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation CreateCampaign($input: CampaignCreateInput!) {
  campaignCreate(input: $input) {
    data {
      id
      name
      advertiser { id }
      channelType
      flights(first: 5) {
        nodes {
          id
          startDateInclusiveUTC
          budgetInAdvertiserCurrency
        }
      }
      conversionReportingColumns(first: 5) {
        nodes {
          reportingColumnId
          trackingTag {
            id
          }
        }
      }
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
    "advertiserId": "adv123",
    "name": "Summer Sale",
    "campaignType": "NONE",
    "primaryChannel": "DISPLAY",
    "includeDefaultsFromAdvertiser": false,
    "primaryGoal": { "maximizeReach": true },
    "campaignConversionReportingColumns": [
      {
        "trackingTagId": "tag1",
        "reportingColumnId": 1,
        "includeInCustomCPA": true
      }
    ],
    "flights": [
      {
        "startDateInclusiveUTC": "2026-07-01T00:00:00Z",
        "endDateExclusiveUTC": "2026-09-01T00:00:00Z",
        "budgetInAdvertiserCurrency": 10000.00
      }
    ]
  }
}
```

The REST example includes fields (partner fees, associated bid lists, build-in-progress) that are not all available on `CampaignCreateInput`. Use `campaignAssociateBidList` and other GraphQL mutations for capabilities not covered here.
