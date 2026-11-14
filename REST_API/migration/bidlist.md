# Bid list: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/bidlist-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Bid list: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/bidlist/{bidListId}` | `Query.bidList(id:)` | N/A |
| `POST /v3/bidlist/batch/get` | `Query.bidList(id:)` (multiple) | Use multiple selections; REST per-ID error envelope not preserved |
| `POST /v3/bidlistsummary/query/adgroup/available` | `AdGroup.availableBidLists` | N/A |
| `POST /v3/bidlistsummary/query/campaign/available` | `Campaign.availableBidLists` | **IMPORTANT**: `Campaign.availableBidLists` is deprecated. Use `Campaign.associatedBidLists` for associated bid lists and `Campaign.ownedBidLists` for owned bid lists. |
| `POST /v3/bidlistsummary/query/advertiser/available` | `Advertiser.availableBidLists` | **IMPORTANT**: `Advertiser.availableBidLists` is deprecated. Use `Advertiser.associatedBidLists` for associated bid lists and `Advertiser.ownedBidLists` for owned bid lists. |
| `POST /v3/bidlistsummary/query/partner/available` | `Partner.availableBidLists` | **IMPORTANT**: `Partner.availableBidLists` is deprecated. Use `Partner.associatedBidLists` for associated bid lists and `Partner.ownedBidLists` for owned bid lists. |
| `POST /v3/bidlistsummary/query/global` | `Query.globalBidLists` | N/A |
| `POST /v3/bidlist/query/unassociated` | N/A | Not currently available in GraphQL |
| `POST /v3/bidlist` | `bidListCreate` | N/A |
| `POST /v3/bidlist/batch` | `bidListCreate` | One mutation per list element; REST batch deprecated |
| `PUT /v3/bidlist` | `bidListSet` or `bidListUpdate` | Full replace vs partial line edits |
| `PUT /v3/bidlist/batch` | `bidListSetBatch` | N/A |
| `DELETE /v3/bidlist/{bidListId}` | `bidListDelete` | N/A |

## Shared nested types and enums

### IBidList (bid list body)

The bid list payload returned by `Query.bidList(id:)`, as connection nodes on `AdGroup.availableBidLists`, `Campaign.availableBidLists`, `Advertiser.availableBidLists` and `Partner.availableBidLists`, and on `Query.globalBidLists`. Concrete type `BidList` implements this interface.

| GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- |
| `id` | `ID!` | Not nullable | N/A |
| `name` | `String!` | Not nullable | N/A |
| `source` | `BidListSource!` | Not nullable | N/A |
| `adjustmentType` | `BidListAdjustmentType!` | Not nullable | N/A |
| `resolutionType` | `MultipleMatchResolutionType!` | Not nullable | N/A |
| `dimensions` | `[BidListDimension!]!` | Not nullable | N/A |
| `bidLines` | `[BidLine!]!` | Not nullable | Plain list, not a connection |
| `bidLinesCount` | `Int!` | Not nullable | N/A |
| `ownerType` | `BidListOwnerType!` | Not nullable | N/A |
| `owner` | `BidListOwner` | Nullable | Union of `AdGroup`, `Advertiser`, `Campaign`, `Forecast`, `Partner` |
| `isAvailableForLibraryUse` | `Boolean!` | Not nullable | N/A |
| `volumeControlOnly` | `Boolean!` | Not nullable | N/A |
| `dimensionDescriptorId` | `Long!` | Not nullable | N/A |
| `activeBidLineBatchId` | `Long` | Nullable | N/A |
| `lastUpdateDate` | `DateTime` | Nullable | N/A |

### BidListDimension (dimension enum)

Used by `dimensions` on the bid list body and by the `dimensions` filter on every available-bid-lists query.

REST `DimensionDescriptor` has 90 values; GraphQL `BidListDimension` has 88. Verify dimension values before migrating a dimension filter:

| Difference | Detail |
| --- | --- |
| REST-only value | **Not currently available in GraphQL**—`UnknownDimension` has no GraphQL member. |
| Renamed values | Several carry an `_ID` suffix or a shortened stem, for example `HasThirdPartyData` becomes `HAS_THIRD_PARTY_DATA_ID` and `HasContentGenre` becomes `HAS_GENRE_ID` |
| Case convention | REST uses PascalCase, GraphQL uses SCREAMING_SNAKE_CASE |

### Available-bid-list associated-entity unions

Each available-bid-lists query exposes `associatedEntity` on its edge type, and the union members narrow as the scope narrows. Select the members that apply to the target scope:

| Query | Edge union | Members |
| --- | --- | --- |
| `AdGroup.availableBidLists` | `AdGroupAvailableBidListEdge.associatedEntity` | `AdGroup`, `Advertiser`, `Campaign`, `Partner` |
| `Campaign.availableBidLists` | `CampaignAvailableBidListEdge.associatedEntity` | `Advertiser`, `Campaign`, `Partner` |
| `Advertiser.availableBidLists` | `AdvertiserAvailableBidListEdge.associatedEntity` | `Advertiser`, `Partner` |
| `Partner.availableBidLists` | `PartnerAvailableBidListEdge.associatedEntity` | `Partner` |

`Query.globalBidLists` returns no association metadata, so it has no `associatedEntity` field.

### BidListOwnerInput (create / batch create)

REST sends owner as `BidListOwner` enum plus `BidListOwnerId`. GraphQL uses a single `BidListOwnerInput` where exactly one ID field (or `isGlobal`) is set.

| REST combination | GraphQL owner object |
| --- | --- |
| BidListOwner: AdGroup + BidListOwnerId: "ag123" | { `adGroupId`: "ag123" } |
| BidListOwner: Advertiser + BidListOwnerId: "adv123" | { `advertiserId`: "adv123" } |
| BidListOwner: Campaign + BidListOwnerId: "cmp123" | { `campaignId`: "cmp123" } |
| BidListOwner: Partner + BidListOwnerId: "prt123" | { `partnerId`: "prt123" } |
| BidListOwner: Global | { `isGlobal`: true } |

### BidLineCreateInput

Used when setting `bidLines`, `bidLinesToAdd`, or nested bid line arrays on create and update mutations.

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `BidLineId` | N/A | N/A | N/A | Read-only |
| `BidAdjustment` | `bidAdjustment` | Decimal! | Required | N/A |
| `AdFormatId` | `adFormatId` | ID | Optional | N/A |
| `DomainFragment` | `domainFragment` | String | Optional | N/A |
| `UniversalCategoryTaxonomyId` | `universalCategoryTaxonomyId` | ID | Optional | N/A |
| `Browser` | `browserId` | BrowserInput | Optional | Use BrowserInput; `browser` is deprecated |
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
| `TemperatureRangeInCelsius` | `temperatureBucketInCelsius` | RangeOfDecimalInput | Optional | N/A |
| `WeatherConditionId` | `weatherCondition` | WeatherCondition | Optional | N/A |
| `ThirdPartyData` | `geofenceThirdPartyDataAndBrand` | GeofenceThirdPartyDataAndBrandInput | Optional | REST ThirdPartyData {ThirdPartyDataBrandId, ThirdPartyDataId} maps to GeofenceThirdPartyDataAndBrandInput {`brandId`, `dataId`} |
| `AdvertiserTargetingDataId` | N/A | N/A | N/A | Not currently available in GraphQL |
| `AdsTxtSellerType` | `adsTxtSellerType` | AdsTxtSellerType | Optional | N/A |
| `VideoMutedState` | `videoMutedState` | VideoMutedState | Optional | N/A |
| `VideoPlaybackType` | `videoPlaybackType` | VideoPlaybackType | Optional | N/A |
| `VideoPlayerSize` | `videoPlayerSize` | VideoPlayerSize | Optional | N/A |
| `VideoQuality` | `videoQuality` | VideoQuality | Optional | N/A |
| `VideoSkippability` | `videoSkippability` | VideoSkippability | Optional | N/A |
| `FactualProximityTarget` | `factualProximityTarget` | FactualProximityTargetInput | Optional | N/A |
| `VideoTruthScoreRange` | `videoTruthScoreRange` | RangeOfDecimalInput | Optional | N/A |
| `VideoViewabilityScoreRange` | `videoViewabilityScoreRange` | RangeOfDecimalInput | Optional | N/A |
| `DisplayViewabilityScoreRange` | `displayViewabilityScoreRange` | RangeOfDecimalInput | Optional | N/A |
| `VideoCompletionRateScoreRange` | `videoCompletionRateScoreRange` | RangeOfDecimalInput | Optional | N/A |
| `FactualGeoTargetingId` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Peer39LanguageId` | `peer39LanguageId` | ID | Optional | N/A |
| `IntegralContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `Peer39ContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `DoubleVerifyContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `TTDContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `IntegralBrandSafetyCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `IntegralVideoBrandSafetyCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `Peer39BrandSafetyCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `DoubleVerifyBrandSafetyCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `ContextualAppCategoryId` | `contextualAppCategoryId` | ID | Optional | N/A |
| `PublisherId` | `publisherId` | ID | Optional | N/A |
| `IntegralViewabilityCategoryId` | `integralViewabilityCategory` | IntegralViewabilityInput | Optional | Prefer `integralViewabilityCategory`; `integralViewabilityCategoryId` is deprecated |
| `IntegralVideoViewabilityCategoryId` | `integralVideoViewabilityCategory` | IntegralVideoViewabilityInput | Optional | Prefer `integralVideoViewabilityCategory`; `integralVideoViewabilityCategoryId` is deprecated |
| `DoubleVerifyViewabilityCategoryId` | `doubleVerifyViewabilityCategory` | DoubleVerifyDisplayViewability | Optional | N/A |
| `DoubleVerifyVideoViewabilityCategoryId` | `doubleVerifyVideoViewabilityCategory` | DoubleVerifyVideoViewability | Optional | N/A |
| `Peer39ViewabilityCategoryId` | `peer39ViewabilityCategory` | Peer39ViewabilityInput | Optional | Prefer `peer39ViewabilityCategory`; `peer39ViewabilityCategoryId` is deprecated |
| `IntegralPageQualityCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `IntegralVideoPageQualityCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `Peer39PageQualityCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `DoubleVerifyBotAvoidanceCategoryId` | `doubleVerifyBotAvoidanceCategory` | DoubleVerifyBotAvoidance | Optional | N/A |
| `TencentPageQualityCategoryId` | `tencentPageQualityCategory` | TencentPageQualityInput | Optional | N/A |
| `FrequencyTarget` | N/A | N/A | N/A | Deprecated on REST |
| `ImpressionPlacementValue` | `impressionPlacementValue` | String | Optional | N/A |
| `VolumeControlPriority` | `volumeControlPriority` | VolumeControlPriority! | Required | N/A |
| `InternetConnectionType` | `internetConnectionTypeId` | InternetConnectionTypeInput | Optional | N/A |
| `RTBAsiaPageQualityCategoryId` | `rtbAsiaPageQualityCategory` | RTBAsiaViewability | Optional | N/A |
| `RTBAsiaVideoPageQualityCategoryId` | `rtbAsiaVideoPageQualityCategory` | RTBAsiaViewability | Optional | N/A |
| `MaxBid` | `maxBid` | Decimal | Optional | N/A |
| `SupplyPathOptimizationListId` | `supplyPathOptimizationListId` | ID | Optional | N/A |
| `MarketType` | `marketType` | MarketTypeBidList | Optional | N/A |
| `ContextualSupplyVendorGenreId` | N/A | N/A | N/A | Not currently available in GraphQL |
| `ContextualSupplyVendorCategoryId` | N/A | N/A | N/A | Not currently available in GraphQL |
| `FrequencyRange` | `frequencyAdjustment` | FrequencyAdjustmentInput | Optional | REST FrequencyRange maps to FrequencyAdjustmentInput |
| `SemasioContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `SellerDomain` | `sellerDomain` | String | Optional | N/A |
| `DigitalOutOfHomeVenueTypeId` | `digitalOutOfHomeVenueTypeId` | ID | Optional | N/A |
| `NativePlacementType` | `nativePlacementType` | NativePlacementType | Optional | N/A |
| `TTDNativeContextType` | `nativeContextType` | NativeContextType | Optional | N/A |
| `GeofenceThirdPartyDataAndBrand` | `geofenceThirdPartyDataAndBrand` | GeofenceThirdPartyDataAndBrandInput | Optional | REST ThirdPartyData {ThirdPartyDataBrandId, ThirdPartyDataId} maps to GeofenceThirdPartyDataAndBrandInput {`brandId`, `dataId`} |
| `EmetriqContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `ComscoreContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `CaptifyContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `AdFontesContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `GumGumContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `NewsGuardContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `IllumaContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `AudigentContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `ShareThisContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `WeboramaContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `DstilleryContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `Scope3ContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `OSDSContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `CrossPixelContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `LumenContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `AdelaideContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `QwarryContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `BarometerContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `SirdataContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `MobianContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `SilverpushContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `FourDContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `AeternaLabsContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `XplnContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `AblidaContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `hyScoreContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `TrueRelevanceContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `NanoInteractiveContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `RaasLabContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `AnokiIncContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `TVQualityIndexRange` | `qualityScoreRange` | RangeOfDecimalInput | Optional | N/A |
| `ContentGenre` | `genreId` | ID | Optional | N/A |
| `ContentLivestream` | `livestream` | Livestream | Optional | N/A |
| `ContentProductionQuality` | `productionQualityId` | ProductionQualityInput | Optional | Prefer `productionQualityId`; `productionQuality` is deprecated |
| `ContentRating` | `contentRatingId` | ID | Optional | N/A |
| `ContentDuration` | `contentDuration` | ContentDuration | Optional | N/A |
| `AtmosphericCondition` | `atmosphericCondition` | AtmosphericCondition | Optional | N/A |
| `AudienceReachPercentageTier` | `audienceReachPercentageTier` | AudienceReachPercentageTier | Optional | N/A |
| `Rewarded` | `rewarded` | Rewarded | Optional | N/A |
| `SellerRelationshipTypeId` | N/A | N/A | N/A | Not currently available in GraphQL |
| `AdToContentRatioRange` | `adToContentRatioRange` | RangeOfDecimalInput | Optional | N/A |
| `AdsInViewRange` | `adsInViewRange` | RangeOfDecimalInput | Optional | N/A |
| `ExtendedZipCodeGroupSegmentThirdPartyDataId` | `extendedZipCodeGroupSegmentThirdPartyDataId` | ID | Optional | N/A |

### BidLine (response)

REST `BidLine` objects returned inside `bidLines` on write mutations and on `IBidList.bidLines`. Collection-element field mapping:

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `BidLineId` | `bidDimensionId` | ID! | Not nullable | N/A |
| `BidAdjustment` | `bidAdjustment` | Decimal! | Not nullable | N/A |
| `AdFormatId` | `adFormat.id` | AdFormat | Nullable | Prefer `adFormat { id }`; `adFormatId` is deprecated |
| `DomainFragment` | `domainFragment` | String | Nullable | N/A |
| `UniversalCategoryTaxonomyId` | `universalCategoryTaxonomy.id` | UniversalCategoryTaxonomy | Nullable | N/A |
| `Browser` | `browser` | Browser | Nullable | N/A |
| `CarrierId` | `carrier.id` | Carrier | Nullable | N/A |
| `DeviceModelId` | `deviceModel.id` | DeviceModel | Nullable | N/A |
| `DeviceType` | `deviceType` | DeviceType | Nullable | N/A |
| `GeoSegmentId` | `geoSegment.id` | GeoSegment | Nullable | N/A |
| `HourOfWeek` | `hourOfWeek` | Short | Nullable | N/A |
| `LanguageId` | `ttdLanguage.id` | TTDLanguage | Nullable | N/A |
| `Os` | `os` | OperatingSystemType | Nullable | N/A |
| `PrivateContractId` | `privateContract.id` | PrivateContract | Nullable | N/A |
| `RecencyWindowInMinutes` | `recencyWindowInMinutes` | RangeOfInt32 | Nullable | N/A |
| `RenderingContext` | `renderingContext` | RenderingContext | Nullable | N/A |
| `SupplyVendorId` | `supplyVendor.id` | SupplyVendor | Nullable | N/A |
| `TemperatureRangeInCelsius` | `temperatureBucketInCelsius` | RangeOfDecimal | Nullable | N/A |
| `WeatherConditionId` | `weatherCondition` | WeatherCondition | Nullable | N/A |
| `ThirdPartyData` | `geoFenceThirdPartyDataAndBrand` | ThirdPartyDataAndBrand | Nullable | REST ThirdPartyData maps to `geoFenceThirdPartyDataAndBrand` |
| `AdvertiserTargetingDataId` | `firstPartyData.id` | FirstPartyData | Nullable | N/A |
| `AdsTxtSellerType` | `adsTxtSellerType` | AdsTxtSellerType | Nullable | N/A |
| `VideoMutedState` | `videoMutedState` | VideoMutedState | Nullable | N/A |
| `VideoPlaybackType` | `videoPlaybackType` | VideoPlaybackType | Nullable | N/A |
| `VideoPlayerSize` | `videoPlayerSize` | VideoPlayerSize | Nullable | N/A |
| `VideoQuality` | `videoQuality` | VideoQuality | Nullable | N/A |
| `VideoSkippability` | `videoSkippability` | VideoSkippability | Nullable | N/A |
| `FactualProximityTarget` | `factualProximityTarget` | FactualProximityTarget | Nullable | N/A |
| `VideoTruthScoreRange` | `videoTruthScoreRange` | RangeOfDecimal | Nullable | N/A |
| `VideoViewabilityScoreRange` | `videoViewabilityScoreRange` | RangeOfDecimal | Nullable | N/A |
| `DisplayViewabilityScoreRange` | `displayViewabilityScoreRange` | RangeOfDecimal | Nullable | N/A |
| `VideoCompletionRateScoreRange` | `videoCompletionRateScoreRange` | RangeOfDecimal | Nullable | N/A |
| `FactualGeoTargetingId` | N/A | N/A | N/A | Not currently available in GraphQL |
| `Peer39LanguageId` | `peer39Language.id` | Peer39Language | Nullable | N/A |
| `IntegralContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `Peer39ContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `DoubleVerifyContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `TTDContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `IntegralBrandSafetyCategoryId` | `integralBrandSafetyCategory.id` | IntegralBrandSafetyCategory | Nullable | Deprecated on GraphQL |
| `IntegralVideoBrandSafetyCategoryId` | `integralVideoBrandSafetyCategory.id` | IntegralVideoBrandSafetyCategory | Nullable | Deprecated on GraphQL |
| `Peer39BrandSafetyCategoryId` | `peer39BrandSafetyCategory.id` | Peer39BrandSafetyCategory | Nullable | Deprecated on GraphQL |
| `DoubleVerifyBrandSafetyCategoryId` | `doubleVerifyBrandSafetyCategory.id` | DoubleVerifyBrandSafetyCategory | Nullable | Deprecated on GraphQL |
| `ContextualAppCategoryId` | `contextualAppCategory.id` | ContextualAppCategory | Nullable | N/A |
| `PublisherId` | `seller.id` | Publisher | Nullable | Prefer `seller { id }`; `publisher` is deprecated |
| `IntegralViewabilityCategoryId` | `integralViewabilityCategory` | IntegralViewabilityCategory | Nullable | N/A |
| `IntegralVideoViewabilityCategoryId` | `integralVideoViewabilityCategory` | IntegralVideoViewabilityCategory | Nullable | N/A |
| `DoubleVerifyViewabilityCategoryId` | `doubleVerifyViewabilityCategory` | DoubleVerifyDisplayViewability | Nullable | N/A |
| `DoubleVerifyVideoViewabilityCategoryId` | `doubleVerifyVideoViewabilityCategory` | DoubleVerifyVideoViewability | Nullable | N/A |
| `Peer39ViewabilityCategoryId` | `peer39ViewabilityCategory` | Peer39ViewabilityCategory | Nullable | N/A |
| `IntegralPageQualityCategoryId` | `integralPageQualityCategory.id` | IntegralPageQualityCategory | Nullable | N/A |
| `IntegralVideoPageQualityCategoryId` | `integralVideoPageQualityCategory.id` | IntegralVideoPageQualityCategory | Nullable | N/A |
| `Peer39PageQualityCategoryId` | `peer39PageQualityCategory.id` | Peer39PageQualityCategory | Nullable | N/A |
| `DoubleVerifyBotAvoidanceCategoryId` | `doubleVerifyBotAvoidanceCategory` | DoubleVerifyBotAvoidance | Nullable | N/A |
| `TencentPageQualityCategoryId` | `tencentPageQualityCategory` | TencentPageQuality | Nullable | N/A |
| `FrequencyTarget` | `frequencyLegacyAdjustment` | FrequencyLegacyAdjustment | Nullable | Legacy frequency v1 |
| `ImpressionPlacementValue` | N/A | N/A | N/A | Not currently available in GraphQL |
| `VolumeControlPriority` | `volumeControlPriority` | VolumeControlPriority! | Not nullable | N/A |
| `InternetConnectionType` | `internetConnectionType` | InternetConnectionType | Nullable | N/A |
| `RTBAsiaPageQualityCategoryId` | `rtbAsiaPageQualityCategory` | RTBAsiaViewability | Nullable | N/A |
| `RTBAsiaVideoPageQualityCategoryId` | `rtbAsiaVideoPageQualityCategory` | RTBAsiaViewability | Nullable | N/A |
| `MaxBid` | `maxBid` | Decimal | Nullable | N/A |
| `SupplyPathOptimizationListId` | `supplyPathOptimizationList.id` | SupplyPathOptimizationList | Nullable | N/A |
| `MarketType` | `marketType` | MarketTypeBidList | Nullable | N/A |
| `ContextualSupplyVendorGenreId` | `contextualSupplyVendorGenre.id` | ContextualSupplyVendorGenre | Nullable | N/A |
| `ContextualSupplyVendorCategoryId` | `contextualSupplyVendorCategory.id` | ContextualSupplyVendorCategory | Nullable | N/A |
| `FrequencyRange` | `frequencyAdjustment` | FrequencyAdjustment | Nullable | REST FrequencyRange maps to `frequencyAdjustment` |
| `SemasioContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `SellerDomain` | `seller.domain` | Publisher | Nullable | Resolve via seller relationship |
| `DigitalOutOfHomeVenueTypeId` | `digitalOutOfHomeVenueType.id` | DigitalOutOfHomeVenueType | Nullable | N/A |
| `NativePlacementType` | `nativePlacementType` | NativePlacementType | Nullable | N/A |
| `TTDNativeContextType` | `nativeContextType` | NativeContextType | Nullable | N/A |
| `GeofenceThirdPartyDataAndBrand` | `geoFenceThirdPartyDataAndBrand` | ThirdPartyDataAndBrand | Nullable | N/A |
| `EmetriqContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `ComscoreContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `CaptifyContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `AdFontesContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `GumGumContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `NewsGuardContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `IllumaContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `AudigentContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `ShareThisContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `WeboramaContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `DstilleryContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `Scope3ContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `OSDSContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `CrossPixelContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `LumenContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `AdelaideContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `QwarryContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `BarometerContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `SirdataContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `MobianContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `SilverpushContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `FourDContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `AeternaLabsContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `XplnContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `AblidaContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `hyScoreContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `TrueRelevanceContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `NanoInteractiveContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `RaasLabContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `AnokiIncContextualCategoryId` | N/A | N/A | N/A | Deprecated on REST |
| `TVQualityIndexRange` | `qualityScoreRange` | RangeOfDecimal | Nullable | N/A |
| `ContentGenre` | `genre.id` | Genre | Nullable | N/A |
| `ContentLivestream` | `livestream` | Livestream | Nullable | N/A |
| `ContentProductionQuality` | `productionQuality` | ProductionQuality | Nullable | N/A |
| `ContentRating` | `contentRating.id` | ContentRating | Nullable | N/A |
| `ContentDuration` | `contentDuration` | ContentDuration | Nullable | N/A |
| `AtmosphericCondition` | `atmosphericCondition` | AtmosphericCondition | Nullable | N/A |
| `AudienceReachPercentageTier` | `audienceReachPercentageTier` | AudienceReachPercentageTier | Nullable | N/A |
| `Rewarded` | `rewarded` | Rewarded | Nullable | N/A |
| `SellerRelationshipTypeId` | `sellerRelationshipTypeId` | SellerRelationshipType | Nullable | N/A |
| `AdToContentRatioRange` | `adToContentRatioRange` | RangeOfDecimal | Nullable | N/A |
| `AdsInViewRange` | `adsInViewRange` | RangeOfDecimal | Nullable | N/A |
| `ExtendedZipCodeGroupSegmentThirdPartyDataId` | `extendedZipCodeGroupThirdPartyTargetingDataSegment.id` | ThirdPartyTargetingDataSegment | Nullable | N/A |
