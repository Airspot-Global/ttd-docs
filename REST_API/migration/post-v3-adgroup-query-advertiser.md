# POST /v3/adgroup/query/advertiser → Advertiser.adGroups

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-adgroup-query-advertiser
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/adgroup/query/advertiser → Advertiser.adGroups

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/adgroup/query/advertiser` |
| GraphQL query | `Advertiser.adGroups` |
| Return type | `AdGroupsWithAggregatesConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | N/A | N/A | Required | Parent entity ID—scope via Advertiser.`adGroups` parent, not a public arg |
| `IsTemplateAdGroups` | Advertiser.adGroups(where.isTemplate:) | BooleanOperationFilterInput | Required | `where: { isTemplate: { eq: ... } }` on `AdGroupForAdvertiserFilterInput` |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |
| `SearchTerms` | Advertiser.adGroups(where.name:) | StringOperationFilterInput | Optional | No `filter` arg—use `where: { name: { contains: ... } }` on `AdGroupForAdvertiserFilterInput` |
| `SortFields` | Advertiser.adGroups(order:) | [AdGroupForAdvertiserSortInput!] | Optional | REST SortFields → GraphQL order input |
| `Availabilities` | Advertiser.adGroups(where.status:) | AdGroupStatusOperationFilterInput | Optional | REST Availabilities → `where.status` on `AdGroupForAdvertiserFilterInput` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [AdGroup!] | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].CampaignId` | `campaign.id` | ID! | Not nullable | N/A |
| `Result[].AdGroupId` | `id` | ID! | Not nullable | Entity key. |
| `Result[].BidderServiceId` | `Query.bidderService(id:)` | BidderService | N/A | Remodelled in GraphQL |
| `Result[].AdGroupName` | `name` | String! | Not nullable | N/A |
| `Result[].Description` | `description` | String | Nullable | N/A |
| `Result[].IsEnabled` | `isEnabled` | Boolean! | Not nullable | N/A |
| `Result[].IsHighFillRate` | `isProgrammaticGuaranteed` | Boolean! | Not nullable | REST `IsHighFillRate` → `isProgrammaticGuaranteed`. |
| `Result[].IndustryCategoryId` | `industryCategoryId` | ID | Nullable | N/A |
| `Result[].AdGroupCategory` | `industryCategory` | IndustryCategory | Nullable | REST `AdGroupCategory` → `industryCategory`. See nested table. |
| `Result[].RTBAttributes` | N/A | N/A | N/A | REST nests bidding, budget, audience, and targeting config here. GraphQL `AdGroup` **flattens** this data to top-level fields and connections—there is no `rTBAttributes` parent. See nested tables below. |
| `Result[].HighFillAttributes` | N/A | N/A | N/A | Remodelled in GraphQL—Query `isProgrammaticGuaranteed`, `budget`, `baseBidCPMInAdvertiserCurrency`, and flight fields on `AdGroup` instead |
| `Result[].MerchantInformation` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Result[].SmbAttributionInformation` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Result[].Availability` | `status` | AdGroupStatus! | Not nullable | REST `Availability` enum → `status`. |
| `Result[].CreatedAtUTC` | `createdAt` | DateTime! | Not nullable | N/A |
| `Result[].LastUpdatedAtUTC` | `lastUpdated` | DateTime! | Not nullable | N/A |
| `Result[].AssociatedBidLists` | `associatedBidLists` | AdGroupAssociatedBidListsConnection | Nullable | See nested table. |
| `Result[].IncludeDefaultsFromCampaign` | N/A | N/A | N/A | Write-only |
| `Result[].AvailableRecommendations` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Result[].NewBidLists` | N/A | N/A | N/A | Write-only |
| `Result[].CustomLabels` | `customLabels` | CustomLabelsConnection | Nullable | `CustomLabelId` → `customLabels.nodes[].id`. |
| `Result[].IsClassic` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Result[].AreFutureKoaFeaturesEnabled` | `koaSettings.areFutureFeaturesEnabled` | Boolean! | Not nullable | N/A |
| `Result[].FunnelLocation` | `funnelLocation` | AdGroupFunnelLocationType! | Not nullable | N/A |
| `Result[].PredictiveClearingEnabled` | `predictiveClearingEnabled` | Boolean! | Not nullable | Also available via `dataSettings.predictiveClearing.isEnabled`. |
| `Result[].UseIdentityAlliance` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Result[].CurrentAndFutureAdditionalFeeCards` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Result[].IsBuildInProgress` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Result[].AdBrainHouseholdCrossDeviceEnabled` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Result[].Increments` | N/A | N/A | N/A | Write-only |
| `Result[].NewFrequencyConfigs` | N/A | N/A | N/A | Write-only |
| `Result[].ChannelId` | `channel` | AdGroupChannelType! | Not nullable | REST `ChannelId` → `channel`. |
| `Result[].EnabledValueAddedProviders` | `enabledValueAddedProviders` | [ValueAddedProviderInfo!]! | Not nullable | N/A |
| `Result[].EnabledValueAddedProviderIds` | `enabledValueAddedProviders[].id` | ID! | Not nullable | Derive IDs from nested `enabledValueAddedProviders`. |
| `Result[].IndustryCategoryTaxonomyId` | N/A | N/A | N/A | Use `industryCategory.taxonomy.id` instead. |
| `Result[].IndustryCategoryMapping` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Result[].MarketplaceOptOut` | N/A | N/A | N/A | Not currently available in GraphQL |

## Endpoint-specific nested types and enums

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

The following are examples of querying ad groups for an advertiser with REST and GraphQL.

Paged ad groups for an advertiser:

### REST example

```
POST /v3/adgroup/query/advertiser HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserId": "adv456",
  "IsTemplateAdGroups": false,
  "PageStartIndex": 0,
  "PageSize": 25
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query AdvertiserAdGroups($advertiserId: ID!) {
  advertiser(id: $advertiserId) {
    adGroups(first: 25, where: { isTemplate: { eq: false } }) {
      totalCount
      nodes {
        id
        name
        campaign { id }
        isEnabled
        description
        status
        channel
        funnelLocation
        industryCategory {
          id
          name
          taxonomy {
            id
            name
            version
          }
        }
        associatedBidLists {
          nodes {
            isEnabled
            isDefaultForUI
            bidList {
              id
              name
              source
              adjustmentType
              dimensions
            }
          }
        }
      }
    }
  }
}
```

Budget, bids, audience, and viewability (rTBAttributes equivalents):

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query AdvertiserAdGroupsTargeting($advertiserId: ID!) {
  advertiser(id: $advertiserId) {
    adGroups(first: 25, where: { isTemplate: { eq: false } }) {
      nodes {
        id
        budgetInAdvertiserCurrency
        budgetInImpressions
        budget {
          total
          spendPriority
        }
        currentFlight {
          dailyTargetInAdvertiserCurrency
          dailyTargetInImpressions
          budgetInAdvertiserCurrency
          allocationType
        }
        baseBidCPMInAdvertiserCurrency
        maxBidCPMInAdvertiserCurrency
        audience { id }
        targetHighValueUsers
        excludeLowValueUsers
        audienceSettings {
          recencyExclusionWindowInMinutes
          strategy
        }
        dataSettings {
          audienceBooster { isEnabled }
          audienceAssistant { isEnabled }
          crossDevice { isEnabled vendor { id name } }
        }
        roiGoal {
          type
          target
        }
        displayViewabilityStandardIntegral
        videoViewabilityStandardIntegral
        qualityAllianceViewabilityProfile
        nielsenTrackingAttributes {
          gender
          startAge
          endAge
          countries
          enhancedNielsenReportingOptions
        }
        analyticsReport {
          nielsenEnabled
          comscoreEnabled
        }
      }
    }
  }
}
```
