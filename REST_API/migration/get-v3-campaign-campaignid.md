# GET /v3/campaign/{campaignId} → Campaign

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-campaign-campaignid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/campaign/{campaignId} → Campaign

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/campaign/{campaignId}` |
| GraphQL query | `Campaign` (via entity lookup by `id`) |
| Return type | `Campaign` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | `advertiser.id` | String! | Not nullable | N/A |
| `CampaignId` | `id` | ID! | Not nullable | Entity key. |
| `CampaignName` | `name` | String! | Not nullable | N/A |
| `Description` | `description` | String | Nullable | N/A |
| `PartnerCostPercentageFee` | N/A | N/A | N/A | Deprecated on REST |
| `PartnerCPMFee` | N/A | N/A | N/A | Deprecated on REST |
| `PartnerCPCFee` | N/A | N/A | N/A | Deprecated on REST |
| `CampaignConversionReportingColumns[].TrackingTagId` | `conversionReportingColumns.nodes[].trackingTag.id` | String! | Not nullable | Absent when `conversionReportingColumns` is null. |
| `CampaignConversionReportingColumns[].TrackingTagName` | `conversionReportingColumns.nodes[].trackingTag.name` | String | Nullable | N/A |
| `CampaignConversionReportingColumns[].ReportingColumnId` | `conversionReportingColumns.nodes[].reportingColumnId` | Int! | Not nullable | N/A |
| `CampaignConversionReportingColumns[].CrossDeviceAttributionModelId` | `conversionReportingColumns.nodes[].crossDeviceAttribution.model` | CrossDeviceAttributionModelId | Nullable | N/A |
| `CampaignConversionReportingColumns[].IncludeInCustomCPA` | `conversionReportingColumns.nodes[].customCPAConfig.include` | Boolean! | Not nullable | N/A |
| `CampaignConversionReportingColumns[].Weight` | `conversionReportingColumns.nodes[].customCPAConfig.weight` | Decimal | Nullable | N/A |
| `Availability` | `status` | CampaignStatus! | Not nullable | REST `Available`/`Archived` maps to `status` and `isArchived`. |
| `Availability` | `isArchived` | Boolean! | Not nullable | REST `Available`/`Archived` maps to `status` and `isArchived`. |
| `CtvTargetingAndAttribution` | N/A | N/A | N/A | Deprecated on REST |
| `CreatedAtUTC` | `createdAtUtc` | DateTime! | Not nullable | N/A |
| `LastUpdatedAtUTC` | N/A | N/A | N/A | Deprecated on REST |
| `FrequencySettings` | `frequencySettings` | FrequencySettings! | Not nullable | Access via `frequencySettings.{lifetimeFrequencyCap, frequencyCap, frequencyPeriodInMinutes}`. |
| `PurchaseOrderNumber` | `purchaseOrderNumber` | String | Nullable | N/A |
| `TimeZone` | `timeZone` | String! | Not nullable | N/A |
| `Budget` | `budget.total` | Decimal! | Not nullable | REST Money amount → `CampaignBudget.total`. |
| `BudgetInImpressions` | `budget.totalInImpressions` | Decimal | Nullable | N/A |
| `ImpressionsOnlyBudgetingCpm` | `impressionsOnlyBudgetingCPM` | Decimal! | Not nullable | N/A |
| `DailyBudget` | N/A | N/A | N/A | Not currently available in GraphQL |
| `DailyBudgetInImpressions` | N/A | N/A | N/A | Not currently available in GraphQL |
| `StartDate` | `startDate` | DateTime! | Not nullable | N/A |
| `EndDate` | `endDate` | DateTime | Nullable | N/A |
| `AutoAllocatorEnabled` | N/A | N/A | N/A | Deprecated on REST |
| `AutoPrioritizationEnabled` | N/A | N/A | N/A | Deprecated on REST |
| `MinimumAdGroupSpendInAdvertiserCurrency` | `minimumAdGroupSpendInAdvertiserCurrency` | Decimal! | Not nullable | N/A |
| `IsMediaOceanCampaign` | `isMediaOceanCampaign` | Boolean | Nullable | N/A |
| `PacingMode` | `pacingMode` | CampaignPacingMode! | Not nullable | N/A |
| `CampaignFlights` | `flights` | FlightsConnection | Nullable | See Campaign domain page for flight field details—access via `flights.nodes`. |
| `CustomLabels` | `customLabels` | CustomLabelsConnection | Nullable | CustomLabelId → connection `nodes[].id`. |
| `CustomCPAType` | `customCPAType` | CustomCPAType! | Not nullable | N/A |
| `CustomCPAClickWeight` | `customCPAClickWeight` | Decimal | Nullable | N/A |
| `CustomCPAViewthroughWeight` | `customCPAViewthroughWeight` | Decimal | Nullable | N/A |
| `CustomROASType` | `customROASType` | CustomROASType! | Not nullable | N/A |
| `IsBuildInProgress` | `isBuildInProgress` | Boolean! | Not nullable | N/A |
| `AssociatedBidLists[].BidListId` | `associatedBidLists.nodes[].bidList.id` | String! | Not nullable | Absent when `associatedBidLists` is null. |
| `AssociatedBidLists[].IsEnabled` | `associatedBidLists.nodes[].isEnabled` | Boolean! | Not nullable | N/A |
| `AssociatedBidLists[].IsDefaultForDimension` | N/A | N/A | N/A | Not currently available in GraphQL |
| `AssociatedBidLists[].BidListSource` | `associatedBidLists.nodes[].bidList.source` | BidListSource! | Not nullable | N/A |
| `AssociatedBidLists[].BidListAdjustmentType` | `associatedBidLists.nodes[].bidList.adjustmentType` | BidListAdjustmentType! | Not nullable | N/A |
| `AssociatedBidLists[].BidListDimensions` | `associatedBidLists.nodes[].bidList.dimensions` | [BidListDimension!]! | Not nullable | N/A |
| `DefaultBidLists` | `defaultBidLists` | DefaultBidListsConnection | Nullable | BidListId → connection `nodes[].id`. |
| `CurrentAndFutureAdditionalFeeCards[].OwnerId` | `passThroughFeeCards.nodes[].target.<inline fragment>.id` | String | Nullable | Absent when `passThroughFeeCards` is null. |
| `CurrentAndFutureAdditionalFeeCards[].OwnerType` | `passThroughFeeCards.nodes[].targetType` | PassThroughFeeTargetType! | Not nullable | REST OwnerType → `targetType`. |
| `CurrentAndFutureAdditionalFeeCards[].StartDateUtc` | `passThroughFeeCards.nodes[].startDateUtc` | DateTime! | Not nullable | N/A |
| `CurrentAndFutureAdditionalFeeCards[].Fees` | `passThroughFeeCards.nodes[].passThroughFees.nodes` | [PassThroughFee!] | Nullable | Connection unwrapping. |
| `CampaignType` | `type` | CampaignType | Nullable | N/A |
| `BallotMeasureProfile` | N/A | N/A | N/A | Write-only |
| `IsBallotMeasure` | `isBallotMeasure` | Boolean | Nullable | N/A |
| `Increments` | `increments` | [Increment] | Nullable | N/A |
| `NewFrequencyConfigs[]` | N/A | N/A | N/A | Write-only |
| N/A | `frequencyConfigs` | [FrequencyConfig!]! | Not nullable | GraphQL read field; no REST GET field parity. |
| `RTBAttributes` | N/A | N/A | N/A | Not currently available in GraphQL |
| `RTBAttributes.AudienceTargeting` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Objective` | N/A | N/A | N/A | Deprecated on REST |
| PrimaryGoal.type (discriminated) | `primaryGoal.type` | ROIGoalType! | Not nullable | Each REST boolean/value field maps to a `ROIGoalType` enum value plus a target scalar. |
| PrimaryGoal.type (discriminated) | `primaryGoal.target` | Decimal | Nullable | Each REST boolean/value field maps to a `ROIGoalType` enum value plus a target scalar. |
| `PrimaryGoal.MaximizeConversionRevenue` | N/A | N/A | N/A | Deprecated on REST |
| `PrimaryGoal.NewBuyerTargetValue` | N/A | N/A | N/A | Not currently available in GraphQL |
| `SecondaryGoal` | `secondaryGoal` | Goal! | Not nullable | Same structure as `primaryGoal`. |
| `TertiaryGoal` | `tertiaryGoal` | Goal! | Not nullable | Same structure as `primaryGoal`. |
| `PrimaryChannel` | `channelType` | CampaignChannelType! | Not nullable | REST Channel → `CampaignChannelType`. |
| `EnabledValueAddedProviders` | N/A | N/A | N/A | Deprecated on REST |
| `EnabledValueAddedProviderIds` | `enabledValueAddedProviders[].id` | ID! | Not nullable | N/A |
| `Version` | `version` | CampaignVersion | Nullable | N/A |
| `TradingModeDetails` | `tradingModeDetails` | CampaignTradingModeDetails! | Not nullable | REST Mode → `tradingModeDetails.mode`; AudienceUnlimitedTier → `tradingModeDetails.audienceUnlimitedTier`. |
| `RTBAttributes.AudienceTargeting.TargetDemographicSettings` | N/A | N/A | N/A | Not currently available in GraphQL |

## Endpoint-specific nested types and enums

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
GET /v3/campaign/{campaignId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetCampaignDetails($id: ID!) {
  campaign(id: $id) {
    id
    name
    status
    isArchived
    pacingMode
    type
    channelType
    startDate
    endDate
    isMediaOceanCampaign
    isBallotMeasure
    primaryGoal {
      type
      target
    }
    associatedBidLists {
      nodes {
        bidList { id source adjustmentType dimensions }
        isEnabled
      }
    }
    frequencyConfigs {
      counter { id name resetIntervalInMinutes }
      bidLists { id }
      increments { campaigns { id } }
    }
    budget {
      total
      version
    }
    flights(first: 10) {
      nodes {
        id
        startDateInclusiveUTC
        endDateExclusiveUTC
      }
    }
  }
}
```
