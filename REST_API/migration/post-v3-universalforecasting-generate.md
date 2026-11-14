# POST /v3/universalforecasting/generate → forecastCreate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-universalforecasting-generate
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/universalforecasting/generate → forecastCreate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/universalforecasting/generate` |
| GraphQL operation | `forecastCreate` |
| Input type | `ForecastCreateInput` |
| Output type | `PayloadWithErrorsOfForecast` (`data: Forecast`, `userErrors: [UserError!]!`) |

> **Parity note:** `forecastCreate` creates a **persisted forecast entity** (optionally calculated asynchronously). It does **not** accept the REST `UniversalForecastingRequest` body or return the ephemeral universal forecast response from REST `generate`. Inputs such as bid-list arrays, forecasting audiences, Nielsen demographic settings, and budget-point generation flags are **Not currently available in GraphQL**. Synchronous outputs such as inline `MetricResults`, `BudgetMetrics`, and `ReachCurveData` are **Not currently available in GraphQL** on create—poll `Forecast.status` and read `adGroupLevelForecastResults` after calculation completes.

## Multi-step operations

GraphQL `forecastCreate` creates a forecast record and may compute results asynchronously (`isAsync`). After creation, query the forecast by `id` and inspect `status` and `adGroupLevelForecastResults` for calculated metrics. REST path: `/v3/universalforecasting/generate` (not `/v3/forecasting/universal`).

## Input field mapping

Input type: `ForecastCreateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | `advertiserId` | String | Required | Required on REST; optional on `ForecastCreateInput` |
| `TimeWindow` | `adGroupForecastSettings.forecastDurationInDays` | Int! | Optional | Remodelled in GraphQL—only when `adGroupForecastSettings` is supplied; days 1–180 on REST |
| `AverageBidCPMInAdvertiserCurrency` | `cpm.amount` / `adGroupForecastSettings.cpm.amount` | Decimal! | Optional | Remodelled in GraphQL—`cpm` is `MoneyModelInput` (`amount` + `currencyCode`), not a bare decimal |
| `CrossDeviceVendorId` | N/A | N/A | Optional | Not currently available in GraphQL |
| `UseMultipleCrossDeviceVendors` | N/A | N/A | Optional | Not currently available in GraphQL |
| `IsTargetKnownUsersEnabled` | `adGroupForecastSettings.targetAllKnowUsers` | Boolean! | Optional | Remodelled in GraphQL—inverted semantics; only when `adGroupForecastSettings` is supplied |
| `UseCrossDevice` | N/A | N/A | Optional | Not currently available in GraphQL |
| `UseCtvCrossDevice` | N/A | N/A | Optional | Not currently available in GraphQL |
| `AudienceId` | `adGroupForecastSettings.audienceId` | String | Optional | Remodelled in GraphQL—only when `adGroupForecastSettings` is supplied |
| `UniversalForecastingBidLists` | N/A | N/A | Optional | Not currently available in GraphQL; see NewBidList / BidLine nested types |
| `ExistingBidLists` | `adGroupForecastSettings.bidLists` | [AdGroupForecastBidListCreateInput!]! | Optional | Remodelled in GraphQL—references existing bid list IDs by `bidListId`, not inline bid-list creation |
| `ForecastingAudiences` | N/A | N/A | Optional | Not currently available in GraphQL |
| `PercentAboveBase` | N/A | N/A | Optional | Not currently available in GraphQL |
| `AllowOpenMarket` | N/A | N/A | Optional | Not currently available in GraphQL |
| `MockForecast` | N/A | N/A | Optional | Not currently available in GraphQL |
| `Demographic` | N/A | N/A | Optional | Not currently available in GraphQL |
| `UseTTDSegmentsOnly` | N/A | N/A | Optional | Not currently available in GraphQL |
| `UseSeparateDemoForecasts` | N/A | N/A | Optional | Not currently available in GraphQL |
| `IncludeExpectedValues` | N/A | N/A | Optional | Not currently available in GraphQL |
| `GenerateBudgetPoints` | N/A | N/A | Optional | Not currently available in GraphQL |
| `UseForecastScalingArrayApproach` | N/A | N/A | Optional | Not currently available in GraphQL |
| N/A | `name` | String! | Required | Create-only; human-readable forecast name |
| N/A | `forecastMode` | ForecastModeInput | Optional | Create-only (`STANDARD`, `LIVE_EVENTS`) |
| N/A | `reachType` | ReachType | Optional | Create-only (`DEVICE`, `PERSON`, `HOUSEHOLD`); deprecated in favour of `adGroupForecastSettings.reachType` when settings supplied |
| N/A | `liveEventsForecastSettings` | LiveEventsForecastSettingCreateInput | Optional | Create-only; for `forecastMode: LIVE_EVENTS` |
| N/A | `isArchived` | Boolean | Optional | Create-only |
| N/A | `isAsync` | Boolean | Optional | Create-only; when `true`, results populate asynchronously |

## Output field mapping

Output type: `PayloadWithErrorsOfForecast` → `data: Forecast`

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | `data.advertiser.id` | ID! | Not nullable | Via `advertiser` relationship |
| `LastCalculatedAt` | `data.adGroupLevelForecastResults.lastCalculatedAt` | DateTime! | Not nullable | Populated after forecast calculation completes |
| `TimeWindow` | `data.adGroupLevelForecastResults.durationInDays` | Int! | Not nullable | Echo of forecast duration |
| `MetricResults` | N/A | N/A | N/A | Not currently available in GraphQL |
| `PrivateContractMetricResults` | N/A | N/A | N/A | Not currently available in GraphQL |
| `PrivateContractGroupMetricResults` | N/A | N/A | N/A | Not currently available in GraphQL |
| `PrivateContractMetricGeoResults` | N/A | N/A | N/A | Not currently available in GraphQL |
| `AverageBidCPMInAdvertiserCurrency` | `data.cpm.amount` | Decimal | Nullable | Remodelled in GraphQL—`MoneyModel`; deprecated in favour of `adGroupForecastSettings.cpm` |
| `CrossDeviceVendorId` | N/A | N/A | N/A | Not currently available in GraphQL |
| `UseMultipleCrossDeviceVendors` | N/A | N/A | N/A | Not currently available in GraphQL |
| `TargetKnownUsers` | `data.adGroupForecastSettings.targetAllKnowUsers` | Boolean! | Not nullable | Remodelled in GraphQL—only when settings were supplied |
| `Audience` | `data.adGroupForecastSettings.audience` | Audience | Nullable | Remodelled in GraphQL—audience entity, not inline REST audience payload |
| `IncrementalForecast` | N/A | N/A | N/A | Not currently available in GraphQL |
| `ReachCurveData` | `data.adGroupLevelForecastResults.curves` | [ForecastingCurveDataPoint!]! | Not nullable | Remodelled in GraphQL—reach curve after calculation; fields include `budget`, `impressions`, `personsReach` (not REST `ReachCurveDataPoint` shape) |
| `ReachStrategySupported` | N/A | N/A | N/A | Not currently available in GraphQL |
| `ForecastingAudiencesToAdd` | N/A | N/A | N/A | Not currently available in GraphQL |
| `ForecastingLambdaRequest` | N/A | N/A | N/A | Not currently available in GraphQL |
| `BudgetMetrics` | N/A | N/A | N/A | Not currently available in GraphQL |
| N/A | `data.id` | ID! | Not nullable | Read-only forecast identifier |
| N/A | `data.name` | String! | Not nullable | Read-only |
| N/A | `data.status` | ForecastStatus | Nullable | Read-only (`QUEUED`, `RUNNING`, `COMPLETED`, `FAILED`, `TO_BE_SUBMITTED`) |
| N/A | `data.forecastMode` | ForecastMode! | Not nullable | Read-only |
| N/A | `data.isAsync` | Boolean! | Not nullable | Read-only |
| N/A | `data.isArchived` | Boolean! | Not nullable | Read-only |
| N/A | `data.adGroupLevelForecastResults.availsNumber` | Long! | Not nullable | Read-only |
| N/A | `data.adGroupLevelForecastResults.spend` | Long | Nullable | Read-only |
| N/A | `data.adGroupLevelForecastResults.valuesAtInputBudget` | BaseForecastingCurveDataPoint! | Not nullable | Read-only metrics at input budget |
| N/A | `userErrors` | [UserError!]! | Not nullable | Validation / business errors (`field`, `message`) |

## Endpoint-specific nested types and enums

Most inputs below are **Not currently available in GraphQL** on `forecastCreate`.

### BidLine (within NewBidList.BidLines)

REST `BidLine` objects on `UniversalForecastingBidLists` are **Not currently available in GraphQL** on `forecastCreate`. When creating bid lists through GraphQL bid-list mutations, use `BidLineCreateInput`.

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `BidAdjustment` | `bidAdjustment` | Decimal! | Required | On `BidLineCreateInput` |
| `AdFormatId` | `adFormatId` | ID | Optional | N/A |
| `DomainFragment` | `domainFragment` | String | Optional | N/A |
| `UniversalCategoryTaxonomyId` | `universalCategoryTaxonomyId` | ID | Optional | N/A |
| `Browser` | `browser` | Browser | Optional | On `BidLineCreateInput` |
| `Browser` | `browserId` | BrowserInput | Optional | On `BidLineCreateInput` |
| `CarrierId` | `carrierId` | ID | Optional | N/A |
| `DeviceModelId` | `deviceModelId` | ID | Optional | N/A |
| `DeviceType` | `deviceType` | DeviceType | Optional | N/A |
| `GeoSegmentId` | `geoSegmentId` | ID | Optional | N/A |
| `HourOfWeek` | `hourOfWeek` | Short | Optional | N/A |
| `LanguageId` | `languageId` | ID | Optional | N/A |
| `Os` | `osName` | String | Optional | N/A |
| `PrivateContractId` | `privateContractId` | ID | Optional | N/A |
| `RecencyWindowInMinutes` | `recencyWindowInMinutes` | RangeOfInt32Input | Optional | N/A |
| `RenderingContext` | `renderingContext` | RenderingContext | Optional | N/A |
| `SupplyVendorId` | `supplyVendorId` | ID | Optional | N/A |
| `MaxBid` | `maxBid` | Decimal | Optional | N/A |
| `BidLineId` | N/A | N/A | N/A | Not currently available in GraphQL |

### NewBidList

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `BidListId` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Name` | N/A | N/A | N/A | Not currently available in GraphQL |
| `BidListAdjustmentType` | N/A | N/A | N/A | Not currently available in GraphQL |
| `ResolutionType` | N/A | N/A | N/A | Not currently available in GraphQL |
| `BidListDimensions` | N/A | N/A | N/A | Read-only on create |
| `BidLines` | N/A | N/A | N/A | Not currently available in GraphQL; see BidLine above |
| `IsEnabled` | N/A | N/A | N/A | Not currently available in GraphQL |
| `IsDefaultForDimension` | N/A | N/A | N/A | Not currently available in GraphQL |

### ForecastingAudience

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | N/A | N/A | N/A | Not currently available in GraphQL |
| `AudienceId` | N/A | N/A | N/A | Read-only on create |
| `AudienceName` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Description` | N/A | N/A | N/A | Not currently available in GraphQL |
| `IncludedDataGroups` | N/A | N/A | N/A | Not currently available in GraphQL; nested object |
| `ExcludedDataGroups` | N/A | N/A | N/A | Not currently available in GraphQL; nested object |
| `IsAutoGenerated` | N/A | N/A | N/A | Read-only |

### DataGroup (within ForecastingAudience)

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | N/A | N/A | N/A | Not currently available in GraphQL |
| `DataGroupId` | N/A | N/A | N/A | Read-only on create |
| `DataGroupName` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Description` | N/A | N/A | N/A | Not currently available in GraphQL |
| `IsSharable` | N/A | N/A | N/A | Not currently available in GraphQL |
| `FirstPartyDataIds` | N/A | N/A | N/A | Not currently available in GraphQL |
| `ThirdPartyDataIds` | N/A | N/A | N/A | Not currently available in GraphQL |
| `SkipUnauthorizedThirdPartyData` | N/A | N/A | N/A | Not currently available in GraphQL |
| `GeoForCounts` | N/A | N/A | N/A | Not currently available in GraphQL |

### NielsenDemographicSettings

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `StartAge` | N/A | N/A | N/A | Not currently available in GraphQL |
| `EndAge` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Gender` | N/A | N/A | N/A | Not currently available in GraphQL |

### UniversalForecastingInsightMetricResult

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `InsightMetricType` | N/A | N/A | N/A | Not currently available in GraphQL |
| `RangeStart` | N/A | N/A | N/A | Not currently available in GraphQL |
| `RangeEnd` | N/A | N/A | N/A | Not currently available in GraphQL |
| `IsCurrency` | N/A | N/A | N/A | Not currently available in GraphQL |
| `ExpectedValue` | N/A | N/A | N/A | Not currently available in GraphQL |

### UniversalForecastInsightMetricType

`Impressions`, `Spend`, `FrequencyUsers`, `FrequencyPeople`, `FrequencyHousehold`, `ReachUsers`, `ReachPeople`, `ReachHousehold`, `Reach`, `Frequency`, `OTP`, `LinearTVReach`, `DigitalReach`, `UsDemographicPercentages`, `SambaUniqueUserCount`, and additional REST-only forecast metric fields. **Not currently available in GraphQL**.

### UniversalForecastingContractMetricResult

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `PrivateContractId` | N/A | N/A | N/A | Not currently available in GraphQL |
| `PrivateContractName` | N/A | N/A | N/A | Not currently available in GraphQL |
| `FloorPrice` | N/A | N/A | N/A | Not currently available in GraphQL |
| `LogoUrl` | N/A | N/A | N/A | Not currently available in GraphQL |
| `IsPremium` | N/A | N/A | N/A | Not currently available in GraphQL |
| `MetricResults` | N/A | N/A | N/A | Not currently available in GraphQL |

### UniversalForecastingContractGroupMetricResult

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `PrivateContractGroupId` | N/A | N/A | N/A | Not currently available in GraphQL |
| `GroupMetricResults` | N/A | N/A | N/A | Not currently available in GraphQL |
| `SubPrivateContractMetricResults` | N/A | N/A | N/A | Not currently available in GraphQL |

### UniversalForecastingContractGeoTypeMetricResult

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `GeoLocationType` | N/A | N/A | N/A | Not currently available in GraphQL |
| `MetricResults` | N/A | N/A | N/A | Not currently available in GraphQL |

### UniversalForecastingContractGeoMetricResult

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `GeoName` | N/A | N/A | N/A | Not currently available in GraphQL |
| `MetricResults` | N/A | N/A | N/A | Not currently available in GraphQL |

### GeoSegmentFilter

`CustomOnly`, `StandardOnly`, `All`, `Country`, `Region`, `City`, `Zip`, `Metro` (**Deprecated on REST**), `CongressionalDistrict`, `NielsenDma`. **Not currently available in GraphQL**.

### IncrementalForecast

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `ReachHh` | N/A | N/A | N/A | Not currently available in GraphQL |
| `ReachUsers` | N/A | N/A | N/A | Not currently available in GraphQL |
| `ReachPeople` | N/A | N/A | N/A | Not currently available in GraphQL |
| `FrequencyHh` | N/A | N/A | N/A | Not currently available in GraphQL |
| `FrequencyUsers` | N/A | N/A | N/A | Not currently available in GraphQL |
| `FrequencyPeople` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Spend` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Impressions` | N/A | N/A | N/A | Not currently available in GraphQL |
| `ImpressionsForAdGroup` | N/A | N/A | N/A | Not currently available in GraphQL |
| `CtvNotExposedImpressions` | N/A | N/A | N/A | Not currently available in GraphQL |
| `ReachPerChannel` | N/A | N/A | N/A | Not currently available in GraphQL |
| `USDemographicPercentage` | N/A | N/A | N/A | Not currently available in GraphQL |

### Range

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Min` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Max` | N/A | N/A | N/A | Not currently available in GraphQL |

### ReachPerChannel

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Ctv` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Both` | N/A | N/A | N/A | Not currently available in GraphQL |

### ReachCurveDataPoint

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Ratio` | N/A | N/A | N/A | Not currently available in GraphQL; GraphQL curves use `ForecastingCurveDataPoint` |
| `ReachRatio` | N/A | N/A | N/A | Not currently available in GraphQL |
| `SpendBudget` | N/A | N/A | N/A | Not currently available in GraphQL |
| `MinReach` | N/A | N/A | N/A | Not currently available in GraphQL |
| `MaxReach` | N/A | N/A | N/A | Not currently available in GraphQL |
| `MinFrequency` | N/A | N/A | N/A | Not currently available in GraphQL |
| `MaxFrequency` | N/A | N/A | N/A | Not currently available in GraphQL |
| `MinImpressions` | N/A | N/A | N/A | Not currently available in GraphQL |
| `MaxImpressions` | N/A | N/A | N/A | Not currently available in GraphQL |
| `AverageCpm` | N/A | N/A | N/A | Not currently available in GraphQL |
| `MinGrps` | N/A | N/A | N/A | Not currently available in GraphQL |
| `MaxGrps` | N/A | N/A | N/A | Not currently available in GraphQL |

### UniversalForecastingScaledFrequencyMapsResult

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `IsFCapped` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Max` | N/A | N/A | N/A | Not currently available in GraphQL |
| `ExpectedValue` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Min` | N/A | N/A | N/A | Not currently available in GraphQL |

### Audience (response nested object)

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | N/A | N/A | N/A | Not currently available in GraphQL; inline audience on generate response |
| `AudienceId` | N/A | N/A | N/A | Not currently available in GraphQL |
| `AudienceName` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Description` | N/A | N/A | N/A | Not currently available in GraphQL |
| `IncludedDataGroupIds` | N/A | N/A | N/A | Not currently available in GraphQL |
| `ExcludedDataGroupIds` | N/A | N/A | N/A | Not currently available in GraphQL |
| `LastUpdatedAtUTC` | N/A | N/A | N/A | Not currently available in GraphQL |
| `IsAutoGenerated` | N/A | N/A | N/A | Not currently available in GraphQL |
| `GeoForCounts` | N/A | N/A | N/A | Not currently available in GraphQL |
| `UniqueUserCount` | N/A | N/A | N/A | Not currently available in GraphQL |
| `WebCount` | N/A | N/A | N/A | Not currently available in GraphQL |
| `InAppCount` | N/A | N/A | N/A | Not currently available in GraphQL |
| `CtvCount` | N/A | N/A | N/A | Not currently available in GraphQL |
| `PersonsCount` | N/A | N/A | N/A | Not currently available in GraphQL |
| `HouseholdCount` | N/A | N/A | N/A | Not currently available in GraphQL |
| `ActiveIDsCountExpanded` | N/A | N/A | N/A | Not currently available in GraphQL |
| `SuccessfullyRetrievedCounts` | N/A | N/A | N/A | Not currently available in GraphQL |

## Code examples

### REST example

```
POST /v3/universalforecasting/generate HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserId": "adv-abc123",
  "TimeWindow": 30,
  "AverageBidCPMInAdvertiserCurrency": 5.50,
  "AudienceId": "aud-xyz789",
  "UseCrossDevice": true,
  "UseCtvCrossDevice": true,
  "GenerateBudgetPoints": true,
  "Demographic": {
    "StartAge": "TwentyFive",
    "EndAge": "FortyNine",
    "Gender": "All"
  }
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation CreateForecast($input: ForecastCreateInput!) {
  forecastCreate(input: $input) {
    data {
      id
      name
      status
      isAsync
      advertiser {
        id
      }
      adGroupLevelForecastResults {
        lastCalculatedAt
        durationInDays
        availsNumber
        spend
        curves {
          budget
          impressions
          personsReach
          averageFrequency
        }
        valuesAtInputBudget {
          impressions
          personsReach
          averageFrequency
          relevance
        }
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

Variables:

```
{
  "input": {
    "name": "Q3 reach forecast",
    "advertiserId": "adv-abc123",
    "forecastMode": "STANDARD",
    "reachType": "PERSON",
    "cpm": {
      "amount": 5.50,
      "currencyCode": "USD"
    },
    "isAsync": true
  }
}
```
