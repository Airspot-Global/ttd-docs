# POST /v3/adgroup → adGroupCreate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-adgroup
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/adgroup → adGroupCreate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/adgroup` |
| GraphQL operation | `adGroupCreate` |
| Input type | `AdGroupCreateInput` |
| Output type | `PayloadWithErrorsOfAdGroup` (`data: AdGroup`, `userErrors: [UserError!]!`) |

## Multi-step operations

| REST-only behavior | GraphQL target |
| --- | --- |
| `AssociatedBidLists`, `NewBidLists` on create | `bidListCreate` + `adGroupAssociateBidList` or `adGroupAssociateBidListBatch` after create |
| Full `RTBAttributes` nested tree (budget flights, audience targeting, dimensional bidding, site quality, etc.) | Partial overlap (`baseBidCPMInAdvertiserCurrency`, `maxBidCPMInAdvertiserCurrency`, `roiGoal`, `nielsenSettings`, `comscoreSettings`, `koaOptimizationSettings`, `cookielessTargetingUserSettingEnabled`, `supplyVendorDeclaredViewabilityBidType`, `miaozhenSettings`); remaining RTB settings require other GraphQL updates or remain REST-only |
| `IncludeDefaultsFromCampaign`, `Availability` | Not currently available in GraphQL |

## Input field mapping

Input type: `AdGroupCreateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `CampaignId` | `campaignId` | ID! | Required | Required on create |
| `AdGroupName` | `name` | String! | Required | N/A |
| `Description` | `description` | String | Optional | N/A |
| `IsEnabled` | `isEnabled` | Boolean | Optional | Defaults to disabled if omitted on REST; same on GraphQL when omitted |
| `IsHighFillRate` | N/A | N/A | Optional | High-fill create is indicated by setting `programmaticGuaranteedPrivateContractId` |
| `IndustryCategoryId` | `industryCategoryId` | Long | Optional | Deprecated on REST—use `AdGroupCategory.CategoryId` |
| `AdGroupCategory` | `industryCategoryId` | Long | Optional | Map `CategoryId` when present |
| `AdGroupCategory.CategoryId` | `industryCategoryId` | Long | Optional | Nested category ID |
| `RTBAttributes` | N/A | N/A | Optional | Not currently available in GraphQL |
| `RTBAttributes.BaseBidCPM` | `baseBidCPMInAdvertiserCurrency` | Decimal | Optional | REST money amount maps to advertiser-currency decimal |
| `RTBAttributes.MaxBidCPM` | `maxBidCPMInAdvertiserCurrency` | Decimal | Optional | REST money amount maps to advertiser-currency decimal |
| `RTBAttributes.ROIGoal` | `roiGoal` | AdGroupCreateROIGoalInput | Optional | GraphQL ROI goal input shape |
| `RTBAttributes.NielsenSettings` | `nielsenSettings` | NielsenSettingsCreateInput | Optional | N/A |
| `RTBAttributes.ComscoreSettings` | `comscoreSettings` | ComscoreSettingsInput | Optional | N/A |
| `RTBAttributes.IsUseClicksAsConversionsEnabled` | `isUseClicksAsConversionsEnabled` | Boolean | Optional | N/A |
| `RTBAttributes.IsUseSecondaryConversionsEnabled` | `isUseSecondaryConversionsEnabled` | Boolean | Optional | N/A |
| `RTBAttributes.KoaOptimizationSettings` | `koaOptimizationSettings` | AdGroupCreateKoaOptimizationSettingsInput | Optional | N/A |
| `HighFillAttributes` | `programmaticGuaranteedPrivateContractId` | String | Optional | Set from `HighFillAttributes.GuaranteedPrivateContractId` for PG create |
| `HighFillAttributes.GuaranteedPrivateContractId` | `programmaticGuaranteedPrivateContractId` | String | Optional | Programmatic guaranteed (high-fill) ad group |
| `IsBuildInProgress` | N/A | N/A | Optional | Not currently available in GraphQL |
| `MerchantInformation` | N/A | N/A | Optional | Deprecated on REST |
| `SmbAttributionInformation` | N/A | N/A | Optional | Deprecated on REST |
| `UseIdentityAlliance` | N/A | N/A | Optional | Deprecated on REST; use cross-device settings on audience updates |
| `Availability` | N/A | N/A | Optional | Create: REST allows only `Available`; no GraphQL input |
| `AssociatedBidLists` | N/A | N/A | Optional | Use `adGroupAssociateBidList` / batch after create |
| `IncludeDefaultsFromCampaign` | N/A | N/A | Optional | Create-only |
| `NewBidLists` | N/A | N/A | Optional | Use `bidListCreate` + association mutations |
| `CustomLabels` | `customLabels` | [String!] | Optional | GraphQL accepts label names, not full assigned-label objects |
| `AreFutureKoaFeaturesEnabled` | `koaOptimizationSettings.areFutureKoaFeaturesEnabled` | Boolean | Optional | Deprecated—no longer actionable |
| `FunnelLocation` | `funnelLocation` | AdGroupFunnelLocationType! | Required | Required on GraphQL create |
| `PredictiveClearingEnabled` | `predictiveClearingEnabled` | Boolean | Optional | N/A |
| `BidderServiceId` | `bidderServiceId` | String | Optional | Custom bidder service ID |
| `Increments` | `increments` | [ID!] | Optional | Frequency counter IDs |
| `NewFrequencyConfigs` | `newFrequencyConfigs` | [AdGroupNewFrequencyConfigInput!] | Optional | Creates counters and increments them on this ad group; see nested table |
| `ChannelId` | `channel` | AdGroupChannelType! | Required | Required on GraphQL create |
| `EnabledValueAddedProviderIds` | `enabledValueAddedProviderIds` | [ID!] | Optional | N/A |
| `MarketplaceOptOut` | `marketType` | MarketType | Optional | REST opt-out maps to GraphQL marketplace selection (`marketType`) |
| `AdBrainHouseholdCrossDeviceEnabled` | N/A | N/A | Optional | Not currently available in GraphQL |
| `IndustryCategoryTaxonomyId` | N/A | N/A | Optional | Category taxonomy is resolved via `industryCategoryId` / read-side `industryCategory` |
| `IndustryCategoryMapping` | N/A | N/A | Optional | Not currently available in GraphQL |

### GraphQL-only input fields (no REST equivalent)

| GraphQL field | GraphQL type | Description |
| --- | --- | --- |
| `isNewsNavigatorEnabled` | Boolean |  |
| `isQualityAllianceSuiteEnabled` | Boolean |  |
| `qualityAllianceViewabilityProfile` | QualityAllianceViewabilityProfileTypeInput |  |
| `displayViewabilityStandardIntegralType` | ViewabilityStandardTypeInput |  |
| `videoViewabilityStandardIntegral` | ViewabilityStandardTypeInput |  |
| `valueAddedProviders` | [ValueAddedProvider!] | Deprecated—use `enabledValueAddedProviderIds` |
| `advertiserId` | ID | Deprecated—does not do anything |
| `advertiserDomainOverride` | String | Advertiser domain address including `http://` or `https://` |
| `callerSource` | String | Leave unset unless you know that you require this |

## Output field mapping

Output type: `AdGroup` (returned as `data` on `PayloadWithErrorsOfAdGroup`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdGroupId` | `id` | ID! | Not nullable | Assigned by the platform on create |
| `CampaignId` | `campaign.id` | ID! | Not nullable | N/A |
| `AdGroupName` | `name` | String! | Not nullable | N/A |
| `Description` | `description` | String | Nullable | N/A |
| `IsEnabled` | `isEnabled` | Boolean! | Not nullable | N/A |
| `IsHighFillRate` | `isHighFillRate` | Boolean! | Not nullable | Also exposed as `isProgrammaticGuaranteed` |
| `IndustryCategoryId` | `industryCategoryId` | ID | Nullable | N/A |
| `AdGroupCategory` | `industryCategory` | IndustryCategory | Nullable | Nested category object |
| `RTBAttributes` | N/A | N/A | N/A | GraphQL exposes budget, bids, and settings across multiple `AdGroup` fields—not a single `RTBAttributes` object |
| `HighFillAttributes` | N/A | N/A | N/A | PG contract surfaced via `isProgrammaticGuaranteed` and related fields |
| `AssociatedBidLists` | `associatedBidLists` | AdGroupAssociatedBidListsConnection | Nullable | Connection—use `nodes { … }` |
| `CreatedAtUTC` | `createdAt` | DateTime! | Not nullable | Read-only |
| `IsBuildInProgress` | N/A | N/A | N/A | Not currently available in GraphQL |
| `ChannelId` | `channel` | AdGroupChannelType! | Not nullable | N/A |
| `FunnelLocation` | `funnelLocation` | AdGroupFunnelLocationType! | Not nullable | N/A |
| `PredictiveClearingEnabled` | `predictiveClearingEnabled` | Boolean! | Not nullable | N/A |
| `CustomLabels` | `customLabels` | CustomLabelsConnection | Nullable | Connection on `AdGroup` |
| `MarketplaceOptOut` | `marketType` | MarketType! | Not nullable | REST boolean opt-out maps to GraphQL marketplace type |
| `Availability` | `status` | AdGroupStatus! | Not nullable | REST `Availability` enum → `status` |
| `LastUpdatedAtUTC` | `lastUpdated` | DateTime! | Not nullable | Read-only; REST field deprecated |
| `AvailableRecommendations` | N/A | N/A | N/A | Not currently available in GraphQL |
| `AreFutureKoaFeaturesEnabled` | `koaSettings.areFutureFeaturesEnabled` | Boolean! | Not nullable | N/A |
| `UseIdentityAlliance` | N/A | N/A | N/A | Deprecated on REST |
| `CurrentAndFutureAdditionalFeeCards` | N/A | N/A | N/A | Read-only |
| `AdBrainHouseholdCrossDeviceEnabled` | N/A | N/A | N/A | Deprecated on REST |
| `BidderServiceId` | `Query.bidderService(id:)` | BidderService | N/A | Remodelled in GraphQL |
| `Increments` | N/A | N/A | N/A | Write-only |
| `NewFrequencyConfigs` | `frequencyConfigs` | AdGroupFrequencyConfigsConnection | Nullable | Echoed in create response only when included in request |
| `EnabledValueAddedProviders` | `enabledValueAddedProviders` | [ValueAddedProviderInfo!]! | Not nullable | Deprecated on REST |
| `EnabledValueAddedProviderIds` | `enabledValueAddedProviders[].id` | ID! | Not nullable | Derive IDs from nested `enabledValueAddedProviders` |
| `IndustryCategoryTaxonomyId` | `industryCategory.taxonomy.id` | ID! | Not nullable | Use `industryCategory.taxonomy.id` instead |
| `IndustryCategoryMapping` | N/A | N/A | N/A | Use `industryCategory.mappings` instead |
| `MerchantInformation` | N/A | N/A | N/A | Deprecated on REST |
| `SmbAttributionInformation` | N/A | N/A | N/A | Deprecated on REST |
| `NewBidLists` | N/A | N/A | N/A | Input-only on create; use bid-list mutations |

## Endpoint-specific nested types and enums

### AdGroupCreateROIGoalInput (create and update ROI goal)

| REST field (under `RTBAttributes.ROIGoal`) | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `MaximizeReach` | `maximizeReach` | Boolean | Optional | Mutually exclusive goal metrics—only one property per request |
| `MaximizeLtvIncrementalReach` | `maximizeLtvIncrementalReach` | Boolean | Optional | N/A |
| `CPCInAdvertiserCurrency.Amount` | `cpcInAdvertiserCurrency` | Decimal | Optional | REST Money amount → decimal |
| `CTRInPercent` | `ctrInPercent` | Decimal | Optional | N/A |
| `NielsenOTPInPercent` | `nielsenOTPInPercent` | Decimal | Optional | N/A |
| `CPAInAdvertiserCurrency.Amount` | `cpaInAdvertiserCurrency` | Decimal | Optional | REST Money amount → decimal |
| `MaximizeConversionRevenue` | N/A | N/A | Optional | Deprecated on REST—use `returnOnAdSpendPercent` |
| `ReturnOnAdSpendPercent` | `returnOnAdSpendPercent` | Decimal | Optional | N/A |
| `VCRInPercent` | `vcrInPercent` | Decimal | Optional | N/A |
| `ViewabilityInPercent` | `viewabilityInPercent` | Decimal | Optional | N/A |
| `VCPMInAdvertiserCurrency.Amount` | `vcpmInAdvertiserCurrency` | Decimal | Optional | REST Money amount → decimal |
| `CPCVInAdvertiserCurrency.Amount` | `cpcvInAdvertiserCurrency` | Decimal | Optional | REST Money amount → decimal |
| `MiaozhenOTPInPercent` | `miaozhenOTPInPercent` | Decimal | Optional | N/A |
| `NewBuyerTargetValue` | `newBuyerTargetValue` | Int | Optional | REST enum → GraphQL int (`0` Featured, `1` Total) |

### NielsenSettingsCreateInput (create)

| REST field (under `RTBAttributes.NielsenSettings`) | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `Fee` | N/A | N/A | N/A | Read-only |
| `NielsenTrackingAttributes` | N/A | N/A | Optional | Parent object on REST |
| `NielsenTrackingAttributes.Gender` | `genderInput` | TargetingGenderInput | Optional | N/A |
| `NielsenTrackingAttributes.StartAge` | `startAgeInput` | TargetingStartAgeInput | Optional | N/A |
| `NielsenTrackingAttributes.EndAge` | `endAgeInput` | TargetingEndAgeInput | Optional | N/A |
| `NielsenTrackingAttributes.Countries` | `countries` | [String!] | Optional | N/A |
| `NielsenTrackingAttributes.EnhancedReportingOption` | `enhancedNielsenReportingOptionsInput` | EnhancedNielsenReportingOptionsInput | Optional | N/A |
| `NielsenTrackingAttributes.LinearTvTrackingBrandCode` | N/A | N/A | Optional | Not currently available in GraphQL |
| (enable flag) | `isEnabled` | Boolean! | Required | Required when `nielsenSettings` object is supplied |

### NielsenSettingsUpdateInput (update)

| REST field (under `RTBAttributes.NielsenSettings`) | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `Fee` | N/A | N/A | N/A | Create-only |
| `NielsenTrackingAttributes.Gender` | `genderInput` | TargetingGenderInput | Optional | N/A |
| `NielsenTrackingAttributes.StartAge` | `startAgeInput` | TargetingStartAgeInput | Optional | N/A |
| `NielsenTrackingAttributes.EndAge` | `endAgeInput` | TargetingEndAgeInput | Optional | N/A |
| `NielsenTrackingAttributes.Countries` | `countries` | [String!] | Optional | N/A |
| `NielsenTrackingAttributes.EnhancedReportingOption` | `enhancedNielsenReportingOptionsInput` | EnhancedNielsenReportingOptionsInput | Optional | N/A |
| `NielsenTrackingAttributes.LinearTvTrackingBrandCode` | N/A | N/A | Optional | Not currently available in GraphQL |
| (enable flag) | `isEnabled` | Boolean | Optional | N/A |

### ComscoreSettingsInput (create and update)

| REST field (under `RTBAttributes.ComscoreSettings`) | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `Fee` | N/A | N/A | N/A | Read-only |
| `Enabled` | `enableComscoreTracking` | Boolean! | Required | Required when `comscoreSettings` object is supplied |
| `PopulationId` | `populationId` | Int! | Required | Required when Comscore tracking is enabled |
| `DemographicMemberIds` | `desktopDemographicMembers` | [Int!]! | Required | REST desktop demo IDs |
| `MobileDemographicMemberIds` | `mobileDemographicMembers` | [Int!]! | Required | REST mobile demo IDs |

### AdGroupCreateKoaOptimizationSettingsInput (create)

| REST field (under `RTBAttributes.KoaOptimizationSettings`) | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `IsEnabled` | `isEnabled` | Boolean | Optional | N/A |
| `OptionalDimensions` | `optionalDimensions` | [KoaOptionalDimensionDescriptor!] | Optional | Solimar optional dimensions (`HasAdFormatId`, `HasGeoSegmentId`) |
| `KoaDimensions` | N/A | N/A | Optional | Not currently available in GraphQL |
| `KpiOverBudgetEnabled` | `kpiOverBudgetEnabled` | Boolean | Optional | Requires `isEnabled: true` when supplied |
| `IsBiddingUpEnabled` | `isBiddingUpEnabled` | Boolean | Optional | N/A |
| `ClickOnlyRoasEnabled` | `clickOnlyRoasEnabled` | Boolean | Optional | Requires `isEnabled: true` when supplied |
| `AreFutureKoaFeaturesEnabled` (top-level) | `areFutureKoaFeaturesEnabled` | Boolean | Optional | Also available on this nested input; deprecated—no longer actionable |

### AdGroupNewFrequencyConfigInput (create)

| REST field (under `NewFrequencyConfigs[]`) | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `CounterName` | `counterName` | String! | Required | Alphanumeric and whitespace only |
| `FrequencyCap` | `frequencyCap` | Int | Optional | Must be greater than 0 when set |
| `FrequencyGoal` | `frequencyGoal` | Int | Optional | Must be greater than 0; cannot exceed `frequencyCap`; requires `resetIntervalInMinutes` ≥ 1440 |
| `ResetIntervalInMinutes` | `resetIntervalInMinutes` | Int! | Required | Must be at least 1 |
| `CounterId` | N/A | N/A | Optional | Ignored on REST create; GraphQL always creates a new counter |
| `OwnedByPartner` | N/A | N/A | Optional | Not currently available in GraphQL |

### AdGroupMiaozhenSettingsInput (create and update)

REST nests these under `MiaozhenSettings.MiaozhenTrackingAttributes`. GraphQL flattens them onto `miaozhenSettings`. China-signed partners with an advertiser corporation ID only. On update, pass `null` to disable Miaozhen tracking.

| REST field (under `RTBAttributes.MiaozhenSettings.MiaozhenTrackingAttributes`) | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `MiaozhenTrackingEnabled` | `miaozhenTrackingEnabled` | Boolean! | Required | Required when `miaozhenSettings` is supplied |
| `MiaozhenMonitoringProduct` | `monitoringProduct` | MiaozhenMonitoringProductInput! | Required | N/A |
| `Gender` | `gender` | MiaozhenTargetingGenderInput! | Required | N/A |
| `StartAge` | `startAge` | MiaozhenTargetingStartAgeInput! | Required | Must not exceed `endAge` |
| `EndAge` | `endAge` | MiaozhenTargetingEndAgeInput! | Required | N/A |
| `MiaozhenTargetingType` | `targetingType` | MiaozhenTargetingTypeInput! | Required | N/A |
| `MiaozhenReportingMarket` | `reportingMarket` | MiaozhenReportingMarketInput! | Required | N/A |
| `Fee` (on `MiaozhenSettings`) | N/A | N/A | N/A | Read-only |

### AdGroupUpdateKoaOptimizationSettingsInput (update)

| REST field (under `RTBAttributes.KoaOptimizationSettings`) | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `KoaOptimizationSettings` | `koaOptimizationSettings` | AdGroupUpdateKoaOptimizationSettingsInput | Optional | Parent on `AdGroupUpdateInput` |
| `KoaOptimizationSettings.PredictiveClearingEnabled` | `predictiveClearingEnabled` | Boolean | Optional | Only field on update Koa input; other Koa settings use top-level update fields |

### AdGroupUpdateAudienceInput (update audience)

| REST field (under `RTBAttributes.AudienceTargeting`) | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AudienceId` | `audienceId` | ID | Optional | Omit or pass `null` to target everyone with non-trackable users |

### RTBAttributes → direct children (create input)

| REST field (under `RTBAttributes`) | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `BudgetSettings` | N/A | N/A | Optional | Not currently available in GraphQL |
| `BaseBidCPM` | `baseBidCPMInAdvertiserCurrency` | Decimal | Optional | REST Money amount → decimal |
| `MaxBidCPM` | `maxBidCPMInAdvertiserCurrency` | Decimal | Optional | REST Money amount → decimal |
| `AudienceTargeting` | N/A | N/A | Optional | Create: no audience input—assign after create via update. Audience updates are in open beta; clients who opted out must wait for general availability or contact their TAM for access. See AdGroupUpdateAudienceInput. |
| `ROIGoal` | `roiGoal` | AdGroupCreateROIGoalInput | Optional | See nested table |
| `FrequencySettings` | N/A | N/A | Optional | Not currently available in GraphQL |
| `CreativeIds` | N/A | N/A | Optional | Not currently available in GraphQL |
| `AdFormatAdjustments` | N/A | N/A | Optional | Use bid-list mutations |
| `GeoSegmentAdjustments` | N/A | N/A | Optional | Use bid-list mutations |
| `UserTimeTargeting` | N/A | N/A | Optional | Use bid-list mutations |
| `SiteTargeting` | N/A | N/A | Optional | Use bid-list mutations |
| `SupplyVendorAdjustments` | N/A | N/A | Optional | Use bid-list mutations |
| `MobileCarrierAdjustments` | N/A | N/A | Optional | Use bid-list mutations |
| `BrowserAdjustments` | N/A | N/A | Optional | Use bid-list mutations |
| `OSFamilyAndVersionAdjustments` | N/A | N/A | Optional | Use bid-list mutations |
| `DeviceTypeAdjustments` | N/A | N/A | Optional | Use bid-list mutations |
| `DeviceMakeModelAdjustments` | N/A | N/A | Optional | Use bid-list mutations |
| `RenderingContextAdjustments` | N/A | N/A | Optional | Use bid-list mutations |
| `AdsTxtSellerTypeAdjustments` | N/A | N/A | Optional | Use bid-list mutations |
| `AutoOptimizationSettings` | N/A | N/A | Optional | Not currently available in GraphQL |
| `IsUseClicksAsConversionsEnabled` | `isUseClicksAsConversionsEnabled` | Boolean | Optional | N/A |
| `IsUseSecondaryConversionsEnabled` | `isUseSecondaryConversionsEnabled` | Boolean | Optional | N/A |
| `DimensionalBiddingAutoOptimizationSettings` | N/A | N/A | Optional | Not currently available in GraphQL |
| `KoaOptimizationSettings` | `koaOptimizationSettings` | AdGroupCreateKoaOptimizationSettingsInput | Optional | See nested table |
| `KoaOptimizationsVersion` | N/A | N/A | N/A | Read-only |
| `KoaOptimizationsMinorVersion` | N/A | N/A | N/A | Read-only |
| `CookielessTargetingUserSettingEnabled` | `cookielessTargetingUserSettingEnabled` | Boolean | Optional | N/A |
| `ContractTargeting` | N/A | N/A | Optional | Use bid-list mutations |
| `VideoTargeting` | N/A | N/A | Optional | Use bid-list mutations |
| `SiteQualitySettings` | N/A | N/A | Optional | Use bid-list / contextual entity mutations |
| `NielsenSettings` | `nielsenSettings` | NielsenSettingsCreateInput | Optional | See nested table |
| `ComscoreSettings` | `comscoreSettings` | ComscoreSettingsInput | Optional | See nested table |
| `LanguageTargeting` | N/A | N/A | Optional | Use bid-list mutations |
| `LogisticRegressionBidCalculationSettings` | N/A | N/A | Optional | Not currently available in GraphQL |
| `QualityAllianceViewabilityTargeting` | N/A | N/A | Optional | Use `isQualityAllianceSuiteEnabled` and bid-list mutations |
| `QualityAllianceVideoCompletionRateTargeting` | N/A | N/A | Optional | Use bid-list mutations |
| `SupplyVendorDeclaredViewabilityTargeting` | `supplyVendorDeclaredViewabilityBidType` | GuaranteedViewableBidTypeInput | Optional | REST nested `GuaranteedViewableBidType` flattens to this enum |
| `AdGroupLifetimeFrequencyCap` | N/A | N/A | Optional | Create: not on `AdGroupCreateInput`; use `adGroupUpdate` |
| `MiaozhenSettings` | `miaozhenSettings` | AdGroupMiaozhenSettingsInput | Optional | See nested table |
| `QualityAllianceViewabilityProfile` | `qualityAllianceViewabilityProfile` | QualityAllianceViewabilityProfileTypeInput | Optional | N/A |
| `DisplayViewabilityStandardIntegral` | `displayViewabilityStandardIntegralType` | ViewabilityStandardTypeInput | Optional | N/A |
| `VideoViewabilityStandardIntegral` | `videoViewabilityStandardIntegral` | ViewabilityStandardTypeInput | Optional | N/A |

### HighFillAttributes (create input)

| REST field (under `HighFillAttributes`) | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `GuaranteedPrivateContractId` | `programmaticGuaranteedPrivateContractId` | String | Optional | Programmatic guaranteed (high-fill) ad group |
| `BudgetSettings` | N/A | N/A | Optional | Not currently available in GraphQL |
| `BudgetSettings.Budget.Amount` | N/A | N/A | Optional | Not currently available in GraphQL |
| `BudgetSettings.BudgetInImpressions` | N/A | N/A | Optional | Not currently available in GraphQL |
| `BudgetSettings.DailyBudget.Amount` | N/A | N/A | Optional | Not currently available in GraphQL |
| `BudgetSettings.DailyBudgetInImpressions` | N/A | N/A | Optional | Not currently available in GraphQL |
| `BudgetSettings.AdGroupFlights[]` | N/A | N/A | Optional | Not currently available in GraphQL |
| `CreativeIds` | N/A | N/A | Optional | Not currently available in GraphQL |
| `BaseBidCPM` | N/A | N/A | N/A | Read-only; contract floor price |
| `MaxBidCPM` | N/A | N/A | N/A | Read-only; contract floor price |

### RTBAttributes → response fields (create/update response)

`AdGroup` flattens RTB data to top-level fields and connections—there is no `rTBAttributes` parent on the response. See nested tables below for leaf mappings.

### AdGroupCategory → industryCategory

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CategoryId` | `industryCategory.id` | ID | Nullable | N/A |
| `CategoryName` | `industryCategory.name` | String! | Not nullable | N/A |
| `CategoryTaxonomyId` | `industryCategory.taxonomy.id` | ID! | Not nullable | N/A |
| `CategoryTaxonomyName` | `industryCategory.taxonomy.name` | String! | Not nullable | N/A |
| `CategoryTaxonomyVersion` | `industryCategory.taxonomy.version` | String! | Not nullable | N/A |
| `Mappings` | `industryCategory.mappings` | [CategoryMapping!] | Nullable | REST `Mappings` → `mappings` (`categoryId`, `externalId`, `taxonomyId`). |

### RTBAttributes → Budget & pacing

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `BudgetSettings.Budget.Amount` | `budgetInAdvertiserCurrency` or `budget.total` | Decimal! | Not nullable | REST Money amount → advertiser-currency budget scalar or `AdGroupBudget.total`. |
| `BudgetSettings.BudgetInImpressions` | `budgetInImpressions` | Decimal | Nullable | N/A |
| `BudgetSettings.DailyBudget.Amount` | `currentFlight.dailyTargetInAdvertiserCurrency` | Decimal | Nullable | Daily targets live on the active flight, not a top-level daily-budget object. |
| `BudgetSettings.DailyBudgetInImpressions` | `currentFlight.dailyTargetInImpressions` | Long | Nullable | N/A |
| `BudgetSettings.AdGroupFlights[]` | `adGroupFlights` | AdGroupFlightsConnection | Nullable | Access via `adGroupFlights.nodes`. Also see `currentFlight` / `currentOrNextFlight`. |
| `BudgetSettings.AdGroupFlights[].AdGroupId` | `adGroupFlights.nodes[].adGroupId` | String! | Not nullable | N/A |
| `BudgetSettings.AdGroupFlights[].CampaignFlightId` | `adGroupFlights.nodes[].campaignFlightId` | Long! | Not nullable | N/A |
| `BudgetSettings.AdGroupFlights[].BudgetInAdvertiserCurrency` | `adGroupFlights.nodes[].budgetInAdvertiserCurrency` | Decimal! | Not nullable | N/A |
| `BudgetSettings.AdGroupFlights[].BudgetInImpressions` | `adGroupFlights.nodes[].budgetInImpressions` | Long | Nullable | N/A |
| `BudgetSettings.AdGroupFlights[].DailyTargetInAdvertiserCurrency` | `adGroupFlights.nodes[].dailyTargetInAdvertiserCurrency` | Decimal | Nullable | N/A |
| `BudgetSettings.AdGroupFlights[].DailyTargetInImpressions` | `adGroupFlights.nodes[].dailyTargetInImpressions` | Long | Nullable | N/A |
| `BudgetSettings.AdGroupFlights[].AllocationType` | `adGroupFlights.nodes[].allocationType` | AdGroupBudgetAllocationType! | Not nullable | N/A |
| `BudgetSettings.PacingMode` | N/A | N/A | N/A | Not currently available in GraphQL |
| `BudgetSettings.AutoAllocatorPriority` | `budget.spendPriority` | Int | Nullable | N/A |
| `BudgetSettings.AllocationType` | `adGroupFlights.nodes[].allocationType` | AdGroupBudgetAllocationType! | Not nullable | Same field as per-flight allocation type. |

### RTBAttributes → Bids

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `BaseBidCPM.Amount` | `baseBidCPMInAdvertiserCurrency` | Decimal | Nullable | REST Money → advertiser-currency decimal. |
| `MaxBidCPM.Amount` | `maxBidCPMInAdvertiserCurrency` | Decimal | Nullable | N/A |
| `LogisticRegressionBidCalculationSettings` | N/A | N/A | N/A | Not currently available in GraphQL |

### RTBAttributes → Audience targeting

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AudienceTargeting.AudienceId` | `audience.id` | String | Nullable | N/A |
| `AudienceTargeting.RecencyExclusionWindowInMinutes` | `audienceSettings.recencyExclusionWindowInMinutes` | Int! | Not nullable | N/A |
| `AudienceTargeting.AudienceBoosterEnabled` | `dataSettings.audienceBooster.isEnabled` | Boolean! | Not nullable | N/A |
| `AudienceTargeting.AudiencePredictorEnabled` | `dataSettings.audienceAssistant.isEnabled` | Boolean! | Not nullable | Audience Assistant maps to `dataSettings.audienceAssistant.isEnabled`. |
| `AudienceTargeting.AudienceExcluderEnabled` | `excludeLowValueUsers` | Boolean! | Not nullable | N/A |
| `AudienceTargeting.AudienceRetargetingEnabled` | `audienceSettings.strategy` | AudienceStrategy! | Not nullable | Use `RETARGETING` / `AUTOMATED_RETARGETING` strategy values. |
| `AudienceTargeting.TargetTrackableUsersEnabled` | `targetHighValueUsers` | Boolean! | Not nullable | N/A |
| `AudienceTargeting.TargetDemographicSettingsEnabled` | `audienceSettings.strategy` | AudienceStrategy! | Not nullable | Use `DEMOGRAPHIC_TARGETING` when enabled. |
| `AudienceTargeting.TargetInterestSettingsEnabled` | `audienceSettings.strategy` | AudienceStrategy! | Not nullable | Use `INTEREST_TARGETING` when enabled. |
| `AudienceTargeting.TargetDemographicSettings` | N/A | N/A | N/A | Detail lives on `audience` / strategy, not a flat REST-shaped object on read. |
| `AudienceTargeting.TargetInterestSettings` | N/A | N/A | N/A | Detail lives on `audience` / strategy, not a flat REST-shaped object on read. |
| `AudienceTargeting.CrossDeviceVendorListForAudience[]` | `dataSettings.crossDevice` / `dataSettings.crossDeviceV2` | CrossDeviceDataSetting! | Not nullable | Vendor list is modeled as data settings, not a REST-style array on read. |
| `AudienceTargeting.RecencyAdjustments[]` | N/A | N/A | N/A | Not currently available in GraphQL |
| AudienceTargeting._Fee._ | N/A | N/A | N/A | Not currently available in GraphQL |
| `AudienceTargeting.AudienceRetargetingSettings` | N/A | N/A | N/A | Retargeting detail is on `audience` / data groups, not a flat REST-shaped object on read. |
| `AudienceTargeting.AdGroupAudiencePredictorTargetingDataSourceSettings` | N/A | N/A | N/A | Not currently available in GraphQL |
| `AudienceTargeting.UseMcIdAsPrimary` | N/A | N/A | N/A | Not currently available in GraphQL |

### RTBAttributes → ROI goal

REST exposes a discriminated `ROIGoal` object with many optional metric fields. GraphQL models goals uniformly:

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| ROIGoal (envelope) | `roiGoal` / `goal` | Goal! | Not nullable | Also see `campaignPrimaryGoal` for the campaign's primary goal. |
| `ROIGoal.CPCInAdvertiserCurrency.Amount` | `roiGoal.type` | ROIGoalType! | Not nullable | Select the `ROIGoalType` matching the REST metric; `target` holds the goal value. |
| `ROIGoal.CPCInAdvertiserCurrency.Amount` | `roiGoal.target` | Decimal | Nullable | Select the `ROIGoalType` matching the REST metric; `target` holds the goal value. |
| `ROIGoal.CTRInPercent` | `roiGoal.type` | ROIGoalType! | Not nullable | Same pattern as other ROI metrics. |
| `ROIGoal.CTRInPercent` | `roiGoal.target` | Decimal | Nullable | Same pattern as other ROI metrics. |
| `ROIGoal.CPAInAdvertiserCurrency.Amount` | `roiGoal.type` | ROIGoalType! | Not nullable | N/A |
| `ROIGoal.CPAInAdvertiserCurrency.Amount` | `roiGoal.target` | Decimal | Nullable | N/A |
| `ROIGoal.ReturnOnAdSpendPercent` | `roiGoal.type` | ROIGoalType! | Not nullable | N/A |
| `ROIGoal.ReturnOnAdSpendPercent` | `roiGoal.target` | Decimal | Nullable | N/A |
| `ROIGoal.ViewabilityInPercent` | `roiGoal.type` | ROIGoalType! | Not nullable | N/A |
| `ROIGoal.ViewabilityInPercent` | `roiGoal.target` | Decimal | Nullable | N/A |
| `ROIGoal.MaximizeReach` | `roiGoal.type` | ROIGoalType! | Not nullable | Boolean REST flags become a `ROIGoalType` enum value. |
| `ROIGoal.MaximizeLtvIncrementalReach` | `roiGoal.type` | ROIGoalType! | Not nullable | N/A |
| `ROIGoal.MaximizeConversionRevenue` | `roiGoal.type` | ROIGoalType! | Not nullable | N/A |
| `ROIGoal.NewBuyerTargetValue` | N/A | N/A | N/A | Not currently available in GraphQL |

### RTBAttributes → Frequency

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `FrequencySettings.FrequencyCap` | `frequencyConfigs` / `impressionFrequencyCounters` | Connection | Nullable | REST inline caps map to `frequencyConfigs` / `impressionFrequencyCounters` connections. |
| `FrequencySettings.FrequencyPeriodInMinutes` | `frequencyConfigs` / `impressionFrequencyCounters` | Connection | Nullable | N/A |
| `FrequencySettings.FrequencyPricingSlopeCPM.Amount` | N/A | N/A | N/A | Not currently available in GraphQL |
| `AdGroupLifetimeFrequencyCap` | N/A | N/A | N/A | Not currently available in GraphQL |

### RTBAttributes → Creatives

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CreativeIds` | `creatives` | AdGroupCreativesConnection | Nullable | Prefer `creatives.nodes[].id` or `allCreativeIdVersionPairs[].creativeId`. |
| `CreativeIds` | `creatives.nodes[].id` | [CreativeIdVersionPair!]! | Not nullable | Prefer `creatives.nodes[].id` or `allCreativeIdVersionPairs[].creativeId`. |

### RTBAttributes → Dimension bid adjustments

REST inlines dimension adjustments (geo, browser, device, video, language, etc.) under `RTBAttributes`. GraphQL models these through bid lists and bid factors instead of a flat adjustment object on `AdGroup`.

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `GeoSegmentAdjustments` | `bidFactors` / `associatedBidLists` / `appliedBidLists` | varies | Nullable | Query bid lists and `bidFactors(dimensions: [...])` for dimension adjustments. |
| `BrowserAdjustments` | `bidFactors` / bid-list connections | varies | Nullable | N/A |
| `MobileCarrierAdjustments` | `bidFactors` / bid-list connections | varies | Nullable | N/A |
| `OSFamilyAndVersionAdjustments` | `bidFactors` / bid-list connections | varies | Nullable | N/A |
| `DeviceTypeAdjustments` | `bidFactors` / bid-list connections | varies | Nullable | N/A |
| `DeviceMakeModelAdjustments` | `bidFactors` / bid-list connections | varies | Nullable | N/A |
| `RenderingContextAdjustments` | `bidFactors` / bid-list connections | varies | Nullable | N/A |
| `AdsTxtSellerTypeAdjustments` | `bidFactors` / bid-list connections | varies | Nullable | N/A |
| `SupplyVendorAdjustments` | `bidFactors` / bid-list connections | varies | Nullable | N/A |
| VideoTargeting.*Adjustments | `bidFactors` / bid-list connections | varies | Nullable | N/A |
| LanguageTargeting.* | `bidFactors` / bid-list connections | varies | Nullable | N/A |
| `AdFormatAdjustments` | `bidFactors` / bid-list connections | varies | Nullable | N/A |
| `UserTimeTargeting.UserHourOfWeekUnknownAdjustment` | `userHourOfWeekUnknownAdjustment` | Decimal! | Not nullable | One of the few hour-of-week scalars exposed directly. |
| `UserTimeTargeting.UserHourOfWeekAdjustments` | `bidFactors` / bid-list connections | varies | Nullable | N/A |
| `SiteTargeting.SiteListIds` | `bidFactors` / bid-list connections | varies | Nullable | N/A |

### RTBAttributes → Auto-optimization & KOA

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AutoOptimizationSettings.IsUseClicksAsConversionsEnabled` | `autoOptimizationSettings.isUseClicksAsConversionsEnabled` | Boolean! | Not nullable | N/A |
| `AutoOptimizationSettings.IsUseSecondaryConversionsEnabled` | `autoOptimizationSettings.isUseSecondaryConversionsEnabled` | Boolean! | Not nullable | N/A |
| `IsUseClicksAsConversionsEnabled` | `autoOptimizationSettings.isUseClicksAsConversionsEnabled` | Boolean! | Not nullable | Duplicate REST surface; same field on `AdGroup`. |
| `IsUseSecondaryConversionsEnabled` | `autoOptimizationSettings.isUseSecondaryConversionsEnabled` | Boolean! | Not nullable | N/A |
| `AutoOptimizationSettings.IsBaseBidAutoOptimizationEnabled` | N/A | N/A | N/A | Not currently available in GraphQL |
| `AutoOptimizationSettings.IsAudienceAutoOptimizationEnabled` | N/A | N/A | N/A | Not currently available in GraphQL |
| `AutoOptimizationSettings.IsSiteAutoOptimizationEnabled` | N/A | N/A | N/A | Not currently available in GraphQL |
| `AutoOptimizationSettings.IsCreativeAutoOptimizationEnabled` | N/A | N/A | N/A | Not currently available in GraphQL |
| `AutoOptimizationSettings.IsSupplyVendorAutoOptimizationEnabled` | N/A | N/A | N/A | Not currently available in GraphQL |
| `AutoOptimizationSettings.IsVideoAutoOptimizationEnabled` | N/A | N/A | N/A | Not currently available in GraphQL |
| `DimensionalBiddingAutoOptimizationSettings` | N/A | N/A | N/A | Not currently available in GraphQL |
| `KoaOptimizationSettings.IsEnabled` | `koaSettings` | AdGroupKoaSettings! | Not nullable | See `koaSettings` child fields for dimensions and versions. |
| KoaOptimizationSettings.KoaDimensions.* | `koaSettings.koaDimensions.*` | Boolean! | Not nullable | N/A |
| `KoaOptimizationSettings.KpiOverBudgetEnabled` | N/A | N/A | N/A | Not currently available in GraphQL |
| `KoaOptimizationSettings.IsBiddingUpEnabled` | `koaSettings.koaDimensions.koaCanBidUp` | Boolean! | Not nullable | N/A |
| `KoaOptimizationSettings.ClickOnlyRoasEnabled` | N/A | N/A | N/A | Not currently available in GraphQL |
| `KoaOptimizationsVersion` | `koaSettings.optimizationsVersion` | KoaOptimizationsVersion! | Not nullable | N/A |
| `KoaOptimizationsMinorVersion` | `koaSettings.minorVersion` | String! | Not nullable | N/A |
| `CookielessTargetingUserSettingEnabled` | N/A | N/A | N/A | Not currently available in GraphQL |

### RTBAttributes → Contract / private marketplace targeting

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `ContractTargeting.ContractIds` | `bidFactors` / bid-list connections | varies | Nullable | Contract targeting is bid-list backed on read. |
| `ContractTargeting.ContractGroupIds` | `bidFactors` / bid-list connections | varies | Nullable | N/A |
| `ContractTargeting.ContractAdjustments` | `bidFactors` / bid-list connections | varies | Nullable | N/A |
| `ContractTargeting.DeliveryProfileAdjustments` | `bidFactors` / bid-list connections | varies | Nullable | N/A |
| `ContractTargeting.UseContractFloorPriceAsBaseBid` | N/A | N/A | N/A | Not currently available in GraphQL |
| `ContractTargeting.ContractFloorPriceAsBaseBidAdjustment` | `contractFloorPriceAsBaseBidAdjustment` | Decimal | Nullable | N/A |
| `ContractTargeting.ContractFloorPricePercentageIncrease` | N/A | N/A | N/A | Not currently available in GraphQL |
| `ContractTargeting.AllowOpenMarketBiddingWhenTargetingContracts` | N/A | N/A | N/A | Not currently available in GraphQL |

### RTBAttributes → Viewability

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `QualityAllianceViewabilityProfile` | `qualityAllianceViewabilityProfile` | QualityAllianceViewabilityProfileType! | Not nullable | N/A |
| `DisplayViewabilityStandardIntegral` | `displayViewabilityStandardIntegral` | ViewabilityStandardType! | Not nullable | N/A |
| `VideoViewabilityStandardIntegral` | `videoViewabilityStandardIntegral` | ViewabilityStandardType! | Not nullable | N/A |
| QualityAllianceViewabilityTargeting.* | `isQualityAllianceSuiteEnabled` / bid-list connections | varies | Nullable | QA suite toggle plus bid-list-backed targeting detail. |
| `QualityAllianceVideoCompletionRateTargeting` | `bidFactors` / bid-list connections | varies | Nullable | VCR targeting is bid-list backed on read; REST fee/percentage leaves are not flat `AdGroup` fields. |
| QualityAllianceVideoCompletionRateTargeting.Fee.* | N/A | N/A | N/A | Not currently available in GraphQL |
| `QualityAllianceVideoCompletionRateTargeting.QualityAllianceVideoCompletionRateMinimalPercentage` | `bidFactors` / bid-list connections | varies | Nullable | Query bid lists for VCR threshold detail. |
| `SupplyVendorDeclaredViewabilityTargeting` | N/A | N/A | N/A | Not currently available in GraphQL |

### RTBAttributes → Site quality providers (Integral / DoubleVerify / Peer39)

REST returns large provider-specific fee and rating trees inline. GraphQL does **not** mirror those trees on `AdGroup`; brand-safety, contextual, and viewability provider settings are bid-list and dimension backed.

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| SiteQualitySettings.* (all provider subtrees) | `bidFactors` / bid-list connections | varies | Nullable | Query associated/applied bid lists for provider category dimensions. Individual REST fee/rating leaves are not flat read fields. |

### RTBAttributes → Nielsen / Comscore / Miaozhen

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `NielsenSettings.NielsenTrackingAttributes.Gender` | `nielsenTrackingAttributes.gender` | TargetingGender! | Not nullable | N/A |
| `NielsenSettings.NielsenTrackingAttributes.StartAge` | `nielsenTrackingAttributes.startAge` | TargetingStartAge! | Not nullable | N/A |
| `NielsenSettings.NielsenTrackingAttributes.EndAge` | `nielsenTrackingAttributes.endAge` | TargetingEndAge! | Not nullable | N/A |
| `NielsenSettings.NielsenTrackingAttributes.Countries` | `nielsenTrackingAttributes.countries` | [String!]! | Not nullable | N/A |
| `NielsenSettings.NielsenTrackingAttributes.EnhancedReportingOption` | `nielsenTrackingAttributes.enhancedNielsenReportingOptions` | EnhancedNielsenReportingOptions! | Not nullable | N/A |
| `NielsenSettings.NielsenTrackingAttributes.LinearTvTrackingBrandCode` | N/A | N/A | N/A | Not currently available in GraphQL |
| NielsenSettings.Fee.* | N/A | N/A | N/A | Not currently available in GraphQL |
| `ComscoreSettings.Enabled` | `analyticsReport.comscoreEnabled` | Boolean! | Not nullable | See also `get-v3-adgroup-analyticsreport-adgroupid` for report metrics. |
| ComscoreSettings.PopulationId / DemographicMemberIds | `analyticsReport.comscoreAnalyticsReport` | ComscoreAnalyticsReport | Nullable | Report breakdown fields, not flat ID lists on `AdGroup`. |
| MiaozhenSettings.MiaozhenTrackingAttributes.* | `analyticsReport.miaozhenAnalyticsReport` | MiaozhenAnalyticsReport | Nullable | Tracking attributes are report-shaped on read. |
| ComscoreSettings.Fee.* / MiaozhenSettings.Fee.* | N/A | N/A | N/A | Not currently available in GraphQL |

### AssociatedBidLists

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `BidListId` | `associatedBidLists.nodes[].bidList.id` | ID! | Not nullable | N/A |
| `IsEnabled` | `associatedBidLists.nodes[].isEnabled` | Boolean! | Not nullable | N/A |
| `IsDefaultForDimension` | `associatedBidLists.nodes[].isDefaultForUI` | Boolean! | Not nullable | REST name → `isDefaultForUI`. |
| `BidListSource` | `associatedBidLists.nodes[].bidList.source` | BidListSource! | Not nullable | N/A |
| `BidListAdjustmentType` | `associatedBidLists.nodes[].bidList.adjustmentType` | BidListAdjustmentType! | Not nullable | N/A |
| `BidListDimensions` | `associatedBidLists.nodes[].bidList.dimensions` | [BidListDimension!]! | Not nullable | N/A |

### HighFillAttributes (REST-only envelope)

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `GuaranteedPrivateContractId` | N/A | N/A | N/A | Not currently available in GraphQL |
| BudgetSettings.* | `budget` / `currentFlight` / `adGroupFlights` | varies | Nullable | Same GraphQL budget fields as RTB budget settings. |
| `CreativeIds` | `creatives` | AdGroupCreativesConnection | Nullable | N/A |
| `CreativeIds` | `creatives.nodes[].id` | [CreativeIdVersionPair!]! | Not nullable | N/A |
| BaseBidCPM.Amount / MaxBidCPM.Amount | `baseBidCPMInAdvertiserCurrency` / `maxBidCPMInAdvertiserCurrency` | Decimal | Nullable | N/A |

## Code examples

### Example—create ad group (GraphQL subset)

### REST example

```
POST /v3/adgroup HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "CampaignId": "cmp123",
  "AdGroupName": "My RTB Ad Group",
  "IsEnabled": false,
  "ChannelId": "Display",
  "FunnelLocation": "Awareness",
  "RTBAttributes": {
    "BaseBidCPM": { "Amount": 1.50, "CurrencyCode": "USD" },
    "MaxBidCPM": { "Amount": 5.00, "CurrencyCode": "USD" }
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
mutation CreateAdGroup($input: AdGroupCreateInput!) {
  adGroupCreate(input: $input) {
    data {
      id
      name
      campaign { id }
      isEnabled
      channel
      funnelLocation
      baseBidCPMInAdvertiserCurrency
      maxBidCPMInAdvertiserCurrency
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
    "campaignId": "cmp123",
    "name": "My RTB Ad Group",
    "isEnabled": false,
    "channel": "DISPLAY",
    "funnelLocation": "AWARENESS",
    "baseBidCPMInAdvertiserCurrency": 1.50,
    "maxBidCPMInAdvertiserCurrency": 5.00
  }
}
```

The REST example includes RTB budget settings and other nested objects that are not all available on `AdGroupCreateInput`. Bid lists, campaign defaults, and full RTB targeting still require additional GraphQL mutations or remain REST-only.
