# POST /v3/delta/campaign → Query.campaignDelta

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-delta-campaign
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/delta/campaign → Query.campaignDelta

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/delta/campaign` |
| GraphQL query | `Query.campaignDelta` |
| Return type | `CampaignDelta` |

> **Note:** This endpoint will be deprecated in the near future. Use 'delta/campaign/query/advertiser' instead. Prefer the canonical GraphQL field `Query.campaignDelta` via `POST /v3/delta/campaign/query/advertiser`.

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `LastChangeTrackingVersion` | `input.advertiser.changeTrackingVersion` | Long! | Optional | REST optional long? defaults when omitted; GraphQL requires non-null Long |
| `AdvertiserId` | `input.advertiser.ids` | [ID!] | Optional | REST single optional/required ID → GraphQL IDs list (wrap single value in array) REST AdvertiserId maps to one element in AdvertiserDeltaInput.ids. |
| `ReturnEntireCampaign` | N/A | N/A | Optional | GraphQL delta always returns full entity objects; no IDs-only mode. |

### GraphQL-only input fields (no REST equivalent)

| GraphQL field | GraphQL type | Description |
| --- | --- | --- |
| `pageSize` | Int | Placement: `input.advertiser.pageSize`. GraphQL-only pagination control; REST delta has implicit paging via More*Available without explicit page size on most endpoints. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `LastChangeTrackingVersion` | `currentMinimumTrackingVersion` | Long! | Not nullable | REST single version → GraphQL splits into `currentMinimumTrackingVersion` and `nextChangeTrackingVersion`. |
| `LastChangeTrackingVersion` | `nextChangeTrackingVersion` | Long! | Not nullable | GraphQL-only companion cursor for subsequent delta calls. |
| `ElementIds` | N/A | N/A | N/A | GraphQL always returns full entity objects; derive IDs from `campaigns[].id`. |
| `Campaigns` | `campaigns` | [Campaign!]! | Not nullable | REST `Campaigns` → `Campaign` entities in `campaigns`. |
| `MoreCampaignsAvailable` | `moreAvailable` | Boolean! | Not nullable | N/A |
| `Campaigns[].AdvertiserId` | `advertiserId` | String! | Not nullable | N/A |
| `Campaigns[].CampaignId` | `id` | ID! | Not nullable | Entity key. |
| `Campaigns[].CampaignName` | `name` | String! | Not nullable | N/A |
| `Campaigns[].Description` | `description` | String | Nullable | N/A |
| `Campaigns[].PartnerCostPercentageFee` | N/A | N/A | N/A | Deprecated on REST |
| `Campaigns[].PartnerCPMFee` | N/A | N/A | N/A | Deprecated on REST |
| `Campaigns[].PartnerCPCFee` | N/A | N/A | N/A | Deprecated on REST |
| `Campaigns[].CampaignConversionReportingColumns` | `conversionReportingColumns` | ConversionReportingColumnsConnection | Nullable | Access via `conversionReportingColumns.nodes`. |
| `Campaigns[].Availability` | `status` | CampaignStatus! | Not nullable | REST `Available`/`Archived` maps to `status` and `isArchived`. |
| `Campaigns[].Availability` | `isArchived` | Boolean! | Not nullable | REST `Available`/`Archived` maps to `status` and `isArchived`. |
| `Campaigns[].CtvTargetingAndAttribution` | N/A | N/A | N/A | Deprecated on REST |
| `Campaigns[].CreatedAtUTC` | `createdAtUtc` | DateTime! | Not nullable | N/A |
| `Campaigns[].LastUpdatedAtUTC` | N/A | N/A | N/A | Deprecated on REST |
| `Campaigns[].FrequencySettings` | `frequencySettings` | FrequencySettings! | Not nullable | Access via `frequencySettings.{lifetimeFrequencyCap, frequencyCap, frequencyPeriodInMinutes}`. |
| `Campaigns[].PurchaseOrderNumber` | `purchaseOrderNumber` | String | Nullable | N/A |
| `Campaigns[].TimeZone` | `timeZone` | String! | Not nullable | N/A |
| `Campaigns[].Budget` | `budget.total` | Decimal! | Not nullable | REST Money amount → `CampaignBudget.total`. |
| `Campaigns[].BudgetInImpressions` | `budget.totalInImpressions` | Decimal | Nullable | N/A |
| `Campaigns[].ImpressionsOnlyBudgetingCpm` | `impressionsOnlyBudgetingCPM` | Decimal | Nullable | N/A |
| `Campaigns[].DailyBudget` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Campaigns[].DailyBudgetInImpressions` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Campaigns[].StartDate` | `startDate` | DateTime! | Not nullable | N/A |
| `Campaigns[].EndDate` | `endDate` | DateTime | Nullable | N/A |
| `Campaigns[].AutoAllocatorEnabled` | N/A | N/A | N/A | Deprecated on REST |
| `Campaigns[].AutoPrioritizationEnabled` | N/A | N/A | N/A | Deprecated on REST |
| `Campaigns[].MinimumAdGroupSpendInAdvertiserCurrency` | `minimumAdGroupSpendInAdvertiserCurrency` | Decimal! | Not nullable | N/A |
| `Campaigns[].IsMediaOceanCampaign` | `isMediaOceanCampaign` | Boolean | Nullable | N/A |
| `Campaigns[].PacingMode` | `pacingMode` | CampaignPacingMode! | Not nullable | N/A |
| `Campaigns[].CampaignFlights` | `flights` | FlightsConnection | Nullable | Access via `flights.nodes`. |
| `Campaigns[].CustomLabels` | `customLabels` | CustomLabelsConnection | Nullable | `CustomLabelId` → `customLabels.nodes[].id`. |
| `Campaigns[].CustomCPAType` | `customCPAType` | CustomCPAType! | Not nullable | N/A |
| `Campaigns[].CustomCPAClickWeight` | `customCPAClickWeight` | Decimal | Nullable | N/A |
| `Campaigns[].CustomCPAViewthroughWeight` | `customCPAViewthroughWeight` | Decimal | Nullable | N/A |
| `Campaigns[].CustomROASType` | `customROASType` | CustomROASType! | Not nullable | N/A |
| `Campaigns[].IsBuildInProgress` | `isBuildInProgress` | Boolean! | Not nullable | N/A |
| `Campaigns[].AssociatedBidLists` | `associatedBidLists` | AssociatedBidListsConnection | Nullable | N/A |
| `Campaigns[].IncludeDefaultsFromAdvertiser` | N/A | N/A | N/A | Update-only |
| `Campaigns[].DefaultBidLists` | `defaultBidLists` | DefaultBidListsConnection | Nullable | BidListId → `defaultBidLists.nodes[].id`. |
| `Campaigns[].CurrentAndFutureAdditionalFeeCards` | `passThroughFeeCards` | PassThroughFeeCardsConnection | Nullable | Access via `passThroughFeeCards.nodes`. |
| `Campaigns[].AdditionalFeeCardOnCreate` | N/A | N/A | N/A | Update-only |
| `Campaigns[].CampaignType` | `type` | CampaignType | Nullable | N/A |
| `Campaigns[].BallotMeasureProfile` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Campaigns[].IsBallotMeasure` | `isBallotMeasure` | Boolean | Nullable | N/A |
| `Campaigns[].Increments` | `increments` | [Increment] | Nullable | N/A |
| `Campaigns[].NewFrequencyConfigs` | N/A | N/A | N/A | Read-only |
| `Campaigns[].Objective` | N/A | N/A | N/A | Deprecated on REST |
| `Campaigns[].PrimaryGoal` | `primaryGoal` | Goal! | Not nullable | REST discriminated goal → `primaryGoal.type` + `primaryGoal.target`. |
| `Campaigns[].SecondaryGoal` | `secondaryGoal` | Goal! | Not nullable | Same structure as `primaryGoal`. |
| `Campaigns[].TertiaryGoal` | `tertiaryGoal` | Goal! | Not nullable | Same structure as `primaryGoal`. |
| `Campaigns[].PrimaryChannel` | `channelType` | CampaignChannelType! | Not nullable | REST `PrimaryChannel` → `channelType`. |
| `Campaigns[].EnabledValueAddedProviders` | N/A | N/A | N/A | Deprecated on REST |
| `Campaigns[].EnabledValueAddedProviderIds` | `enabledValueAddedProviders[].id` | [ID!]! | Not nullable | N/A |
| `Campaigns[].Version` | `version` | CampaignVersion | Nullable | N/A |
| `Campaigns[].TradingModeDetails` | `tradingModeDetails` | CampaignTradingModeDetails! | Not nullable | REST `Mode` → `tradingModeDetails.mode`; `AudienceUnlimitedTier` → `tradingModeDetails.audienceUnlimitedTier`. |
| `Campaigns[].RTBAttributes` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Campaigns[].RTBAttributes.AudienceTargeting` | N/A | N/A | N/A | Not currently available in GraphQL |

## Endpoint-specific nested types and enums

### BallotMeasureProfile

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `PoliticalDataId` | N/A | N/A | N/A | Not currently available in GraphQL |
| `ElectionState` | N/A | N/A | N/A | Not currently available in GraphQL |
| `PayingEntityName` | N/A | N/A | N/A | Not currently available in GraphQL |
| `PayingEntityAddress` | N/A | N/A | N/A | Not currently available in GraphQL |
| `PayingEntityExecutiveName` | N/A | N/A | N/A | Not currently available in GraphQL |
| `PayingEntityExecutiveTitle` | N/A | N/A | N/A | Not currently available in GraphQL |
| `GeoDescription` | N/A | N/A | N/A | Not currently available in GraphQL |
| `AudienceDescription` | N/A | N/A | N/A | Not currently available in GraphQL |
| `IsAdvertiserIEC` | N/A | N/A | N/A | Not currently available in GraphQL |
| `FileLocationInS3` | N/A | N/A | N/A | Not currently available in GraphQL |

### RTBAttributes → AudienceTargeting → TargetDemographicSettings

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

The following are examples of querying campaign deltas with REST and GraphQL.

Basic delta query:

### REST example

```
POST /v3/delta/campaign HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "LastChangeTrackingVersion": null,
  "AdvertiserId": "example-id",
  "ReturnEntireCampaign": false
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query CampaignDelta {
  campaignDelta(input: {
    advertiser: {
      changeTrackingVersion: 0
      ids: ["adv123"]
      pageSize: 100
    }
  }) {
    currentMinimumTrackingVersion
    nextChangeTrackingVersion
    moreAvailable
    campaigns {
      id
      name
      status
      pacingMode
      primaryGoal {
        type
        target
      }
    }
  }
}
```

Campaign goals, budget, and flights:

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query CampaignDeltaDetails {
  campaignDelta(input: {
    advertiser: {
      changeTrackingVersion: 0
      ids: ["adv123"]
      pageSize: 10
    }
  }) {
    campaigns {
      id
      name
      status
      pacingMode
      primaryGoal {
        type
        target
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
          budgetInAdvertiserCurrency
        }
      }
      associatedBidLists {
        nodes {
          bidList { id source adjustmentType }
          isEnabled
        }
      }
      frequencyConfigs {
        counter { id name resetIntervalInMinutes }
      }
    }
  }
}
```
