# Upcoming API changes for advertisers

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserNews/news/doc/UpgradeSupport
- Retrieved: 2026-11-14
- Category: Guides

---

# Upcoming API changes for advertisers

This page outlines the timeline for upcoming changes to The Trade Desk APIs for advertisers and offers support guidelines to help you upgrade to new features or adapt to API updates that require code changes on your part. For details on how The Trade Desk introduces and manages changes to the API, see API changes.

> **TIP**: For any past upgrades and guidelines, see the Archived API changes for advertisers page.

The following sections summarize the upcoming updates by quarter.

## October-December 2026

| Effective Date | Product/Feature | Update Type | Details |
| --- | --- | --- | --- |
| Nov 15, 2026 | GraphQL: GeneralReportingMetrics | Field deprecation | GeneralReportingMetrics GraphQL type: field deprecation |
| Dec 1, 2026 | GraphQL: Query | Endpoint deprecation | Query GraphQL type: endpoint deprecation |
| Dec 1, 2026 | GraphQL: AdGroup | Field deprecation | AdGroup GraphQL type: field deprecation |
| Dec 11, 2026 | GraphQL: AdGroupUpdateInput | Field deprecation | AdGroupUpdateInput GraphQL type: field deprecation |
| Dec 16, 2026 | GraphQL: Marketplace | Field deprecation | Marketplace GraphQL type: field deprecation |
| Dec 31, 2026 | GraphQL: PharmaHcpFrequencyWindowInput | Enum value deprecation | PharmaHcpFrequencyWindowInput GraphQL type: enum value deprecation |
| Dec 31, 2026 | GraphQL: MyReportsReportSchedule | Field deprecation | MyReportsReportSchedule GraphQL type: field deprecation |

### GeneralReportingMetrics GraphQL type: field deprecation

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **November 15, 2026**, the following 2 fields on the `GeneralReportingMetrics` GraphQL type will be deprecated: - `nielsenOtp` - `roasAggregate` |
| **Action required** | Update any code that references the two fields on the `GeneralReportingMetrics` type by **November 15, 2026**. |

### Query GraphQL type: endpoint deprecation

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **December 1, 2026**, the following 2 fields on the `Query` GraphQL type will be deprecated: - `thirdPartyData` - `thirdPartyDatas` |
| **Action required** | Update any code that references the two fields on the `Query` type by **December 1, 2026**. |

### AdGroup GraphQL type: field deprecation

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **December 1, 2026**, the following four fields on the `AdGroup` GraphQL type will be removed: - `displayViewabilityStandardIntegral`—use `displayViewabilityStandardIntegralType` instead. - `videoViewabilityStandardIntegral`—use `videoViewabilityStandardIntegralType` instead. - `isNewsNavigatorEnabled`—use `isNewsNavigatorEnabledState` instead. - `isUsingLiveEventSchedule`—use `isUsingLiveEventScheduleState` instead. |
| **Action required** | Update any code that references the four fields on the `AdGroup` type by **December 1, 2026**. See the replacement properties listed above. |

### AdGroupUpdateInput GraphQL type: field deprecation

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **December 11, 2026**, the `dataSettings` field will be deprecated on the `AdGroupUpdateInput` GraphQL type. |
| **Action required** | Update any code that references the `dataSettings` field on the `AdGroupUpdateInput` type by **December 11, 2026**. |

### Marketplace GraphQL type: field deprecation

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **December 16, 2026**, the following three fields on the `Marketplace` GraphQL type will be deprecated: - `isEnabled` - `isPublished` - `isUsingManualSupplyPathConfiguration` |
| **Action required** | Update any code that references the three fields on the `Marketplace` type by **December 16, 2026**. |

### PharmaHcpFrequencyWindowInput GraphQL type: enum value deprecation

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **December 31, 2026**, the `SEVEN_DAYS` field will be deprecated as an enum value used in queries on the `PharmaHcpFrequencyWindowInput` GraphQL type. |
| **Action required** | Update any code that references the `SEVEN_DAYS` enum value on the `PharmaHcpFrequencyWindowInput` type by **December 31, 2026**. |

### MyReportsReportSchedule GraphQL type: field deprecation

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **December 31, 2026**, the `createdBy` field on the `MyReportsReportSchedule` GraphQL type will be deprecated in favor of `createdByUser`. Both fields identify who created a scheduled report, but if the caller lacks visibility over the creator, `createdBy` returns a permission-gated `User` object that comes back `null` with a per-row GraphQL error. The `createdByUser` field returns a `UserBasicInfo` object that always resolves, returning `[REDACTED]` name and email instead of an error when visibility is restricted. This deprecation applies only to `MyReportsReportSchedule.createdBy` (a report _schedule_). It does not affect the unrelated, non-deprecated `createdBy` field on `MyReportsTemplate` (a report _template_). |
| **Action required** | Update any code that references `MyReportsReportSchedule.createdBy` to use `createdByUser` instead, by **December 31, 2026**. |

## January-March 2027

| Effective Date | Product/Feature | Update Type | Details |
| --- | --- | --- | --- |
| Jan 1, 2027 | GraphQL: TradingMode types | Field deprecation | TradingMode GraphQL types: field deprecation |
| Jan 2, 2027 | GraphQL: Query (audiences) | Field deprecation | Query GraphQL type: root-level audiences field deprecation |
| Jan 2, 2027 | GraphQL: TargetingData and TargetingDataSegment | Field deprecation | TargetingData and TargetingDataSegment GraphQL types: field deprecation |
| Jan 11, 2027 | Contextual targeting | New requirement (breaking change) | Contextual targeting for new campaigns and ad groups: contextual entities required |
| Jan 28, 2027 | GraphQL: Ad group targeting disallowed reasons | Field deprecation | Deal targeting disallowed reason GraphQL types: field deprecation |
| Feb 1, 2027 | GraphQL: valueAddedProviders | Field deprecation | Value-added provider fields deprecation: GraphQL fields |
| Feb 1, 2027 | Rest API: iptargetinglist | Behavioral change | IP targeting list REST API: unique name required for new segments |
| Feb 8, 2027 | GraphQL: BidLine and BidListDimension | Field deprecation | Contextual bid list deprecation: GraphQL fields |
| Feb 8, 2027 | Bid lists REST API | Property deprecation | Contextual bid list deprecation: REST properties |
| Feb 28, 2027 | REST API: universalforecasting | Endpoint deprecation | Universal Forecasting REST API: endpoint deprecation |
| Q1 2027 | REDS: DoubleVerify viewability feed | Integration upgrade | DoubleVerify viewability: enhanced integration migration |

### TradingMode GraphQL types: field deprecation

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **January 1, 2027**, as part of the Trading Modes closed beta sunset, the `audienceUnlimitedTier` field will be deprecated on the following GraphQL types: - `CampaignTradingModeDetails`—use the `campaign.audienceUnlimitedSettings` field instead. - `TradingModeSettings`—use the `advertiser.audienceUnlimitedSettings` field instead. - `CampaignCreateTradingModeSettingsInput`—use the `audienceUnlimitedSettings` field instead. - `CampaignCloneTradingModeSettingsInput`—use the `audienceUnlimitedSettings` field instead. - `CampaignUpdateTradingModeSettingsInput`—use the `audienceUnlimitedSettings` field instead. Both the deprecated and new fields will be exposed during the transition period; requests that submit an invalid combination of old and new field values will return an error. |
| **Action required** | Update any code that references the `audienceUnlimitedTier` field on the types listed above by **January 1, 2027**. |

### Query GraphQL type: root-level audiences field deprecation

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **January 2, 2027**, the root-level `audiences` query on the `Query` GraphQL type will be deprecated. Use the scoped `advertiser.audiences` or `partner.audiences` query instead, which is consistent with how other entities are scoped through their owning entity. |
| **Action required** | Update any code that queries `audiences` at the root level to instead query it through `advertiser(id: ...) { audiences }` or `partner(id: ...) { audiences }` by **January 2, 2027**. For details, see the following examples. |

The following are example deprecated and new queries that show the updates.

This query is **deprecated**—it queries the `audiences` type at the root level:

```
query GetAudiencesExampleDeprecated($advertiserId: String) {
  audiences(where: {advertiserId: {eq: $advertiserId}}) {
    nodes {
      audienceId: id
      audienceName: name
    }
  }
}
```

Use this **new** query instead, scoped through the `advertiser` type:

```
query GetAudiencesForAdvertiserExampleNew($advertiserId: ID!) {
  advertiser(id: $advertiserId) {
    audiences {
      nodes {
        audienceId: id
        audienceName: name
      }
    }
  }
}
```

To query audiences at the partner level, use this **new** query instead, scoped through the `partner` type:

```
query GetAudiencesForPartnerExampleNew($partnerId: ID!) {
  partner(id: $partnerId) {
    audiences {
      nodes {
        audienceId: id
        audienceName: name
      }
    }
  }
}
```

### TargetingData and TargetingDataSegment GraphQL types: field deprecation

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **January 2, 2027**, the `targetingDataStatus` field on the `TargetingData` GraphQL type will be deprecated. Use the `targetingDataInsights` field on the `TargetingDataSegment` GraphQL type instead, available starting mid-October 2026. Note that the `state` field is not carried over to `targetingDataInsights`. The `receivedCounts` field remains available for now but will eventually become internal-only. |
| **Action required** | Update any code that references `targetingDataStatus` (under `TargetingData`) to instead use `targetingDataInsights` (under `TargetingDataSegment`) by **January 2, 2027**. |

### Contextual targeting on new campaigns and ad groups: contextual entities required

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **January 11, 2027**, contextual entities become the default experience for contextual targeting for new campaigns and ad groups. - Contextual bid lists will no longer be created on net-new campaigns or ad groups, in the UI or using the Platform REST API. - Contextual targeting on net-new campaigns and ad groups will be available only through GraphQL, using contextual entities. For details, see Contextual category configuration. - This update does not affect existing campaigns and ad groups already using contextual bid lists. They will continue to work as-is until contextual bid lists are fully deprecated. - Cloning an existing bid list campaign also remains supported in the UI and API until that full deprecation. |
| **Action required** | If you use the Platform REST API to create contextual bid lists on new campaigns or ad groups, migrate to using contextual entities via GraphQL before **January 11, 2027**. No action is required for existing campaigns or ad groups. |

### Deal targeting disallowed reason GraphQL types: field deprecation

| What you need to know and do |  |
| --- | --- |
| **Change summary** | As part of a broader effort to improve the performance of ad group targetable inventory queries, effective **January 28, 2027**, the `targetedAtPartnerLevel`, `targetedAtAdvertiserLevel` and `targetedAtCampaignLevel` fields will be deprecated in favor of a single new field, `targetedAtHigherLevel`, on the following GraphQL types: - `DealTargetingDisallowedReason` - `CommitmentTargetingDisallowedReason` - `EndeavorTargetingDisallowedReason` Here's what you need to know: - The `targetedAtHigherLevel` value is `true` when any of the three deprecated fields would have been set to `true`. - You can reach these types through the `isTargetingChangeAllowed.reason` field on the edges of the `adGroup.targetableDeals`, `adGroup.targetableCommitments` and `adGroup.targetableEndeavors` fields. - The `targetedAtHigherLevel` field doesn't distinguish between partner-, advertiser- and campaign-owned bid lists. If that distinction matters to you, retrieve the higher-level bid list and its owning level through the Platform API. |
| **Action required** | Update any code that references the `targetedAtPartnerLevel`, `targetedAtAdvertiserLevel` and `targetedAtCampaignLevel` fields on the three types listed above to use `targetedAtHigherLevel` instead, by **January 28, 2027**. For details, see the following examples. |

The following are example deprecated and new queries that show the update.

> **NOTE**: The same change applies to the `targetableCommitments` and `targetableEndeavors` deprecated fields.

This query is **deprecated**—it queries the three per-level fields directly on the `reason` value:

```
query AdGroupTargetableDealsExampleDeprecated($adGroupId: ID!) {
  adGroup(id: $adGroupId) {
    targetableDeals {
      edges {
        isTargetingChangeAllowed {
          isAllowed
          reason {
            targetedAtPartnerLevel
            targetedAtAdvertiserLevel
            targetedAtCampaignLevel
          }
        }
      }
    }
  }
}
```

Use this **new** query instead, with the single `targetedAtHigherLevel` field:

```
query AdGroupTargetableDealsExampleNew($adGroupId: ID!) {
  adGroup(id: $adGroupId) {
    targetableDeals {
      edges {
        isTargetingChangeAllowed {
          isAllowed
          reason {
            targetedAtHigherLevel
          }
        }
      }
    }
  }
}
```

### Value-added provider fields deprecation: GraphQL fields

| What you need to know and do |  |
| --- | --- |
| **Change summary** | The following GraphQL value-added provider fields are deprecated. Their replacements identify providers by ID instead of enum value, consistent with the REST API change. Deprecated endpoints will be removed on **February 1, 2027**. - **Query fields:** - `Adgroup.valueAddedProviders`— use the `Adgroup.valueAddedProviderInfo` field instead. - `Campaign.valueAddedProviders`— use the `Campaign.valueAddedProviderInfo` field instead. The replacement fields return a `ValueAddedProviderInfo` object with `id`, `name`, and `description` properties. You can filter by the `id` and `name` fields. - **Mutation input fields:** - `AdGroupCreateInput.valueAddedProviders`— use the `AdGroupCreateInput.enabledValueAddedProviderIds` field instead. - `AdgroupUpdateInput.valueAddedProviders`— use the `AdgroupUpdateInput.enabledValueAddedProviderIds` field instead. The replacement fields accept an array of integer provider IDs. |
| **Action required** | Update your campaign and ad group queries to use the `valueAddedProviderInfo` field and your ad group create and update mutations to pass provider IDs in the `enabledValueAddedProviderIds` field by **February 1, 2027**. |

### IP targeting list REST API: unique name required for new segments

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **February 1, 2027**, the POST /iptargetinglist endpoint requires a unique IP targeting data name. Previously, clients could call the endpoint repeatedly with the same IP targeting data name; each call succeeded and was assigned the same targeting data ID but a different IP targeting data name, resulting in duplicate IP target lists in your account. Going forward, a request that reuses an existing IP targeting data name for a new segment will return an error. To edit an existing IP list, continue using the PUT /iptargetinglist endpoint. |
| **Action required** | Before **February 1, 2027**, review any automation that calls POST /iptargetinglist. If it relies on reusing an existing IP targeting data name value to create new segments, update it to supply a unique name per new segment, or switch to the PUT /iptargetinglist endpoint if the intent is to edit an existing list. |

### Contextual bid list deprecation: GraphQL fields

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **February 8, 2027**, contextual bid lists will be deprecated. To use contextual categories in your campaigns, you must first organize them into contextual groups and entities, then assign those entities to your ad groups. For details, see Contextual category configuration. The following **GraphQL** fields will be removed: - **BidLine** - `doubleVerifyBrandSafetyCategory` - `integralBrandSafetyCategory` - `integralVideoBrandSafetyCategory` - `peer39BrandSafetyCategory` - `preBidContextualCategory` - **BidListDimension** - `HAS_DOUBLE_VERIFY_BRAND_SAFETY_CATEGORY_ID` - `HAS_INTEGRAL_BRAND_SAFETY_CATEGORY_ID` - `HAS_INTEGRAL_VIDEO_BRAND_SAFETY_CATEGORY_ID` - `HAS_PEER39_BRAND_SAFETY_CATEGORY_ID` - `HAS_PRE_BID_CONTEXTUAL_CATEGORY_ID` Requests that include these fields after this date will return an error. |
| **Action required** | Update any code that references the fields listed above on the `BidLine` and `BidListDimension` GraphQL types by **February 8, 2027**. For details, see Migrate bid lists to contextual entities. |

### Contextual bid list deprecation: REST properties

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **February 8, 2027**, contextual bid lists will be deprecated. To use contextual categories in your campaigns, you must first organize them into contextual groups and entities, then assign those entities to your ad groups. For details, see Contextual category configuration. The following **REST** properties will be removed: - **POST /v3/adgroup** - `AssociatedBidLists.BidListDimensions.HasDoubleVerifyBrandSafetyCategoryId` - `AssociatedBidLists.BidListDimensions.HasIntegralBrandSafetyCategoryId` - `AssociatedBidLists.BidListDimensions.HasIntegralContextualCategoryId` - `AssociatedBidLists.BidListDimensions.HasIntegralVideoBrandSafetyCategoryId` - `NewBidLists.BidLines.DoubleVerifyBrandSafetyCategoryId` - `NewBidLists.BidLines.IntegralBrandSafetyCategoryId` - `NewBidLists.BidLines.IntegralVideoBrandSafetyCategoryId` - `NewBidLists.BidLines.TTDContextualCategoryId` - `NewBidLists.BidListDimensions.HasDoubleVerifyBrandSafetyCategoryId` - **PUT /v3/adgroup** - `AssociatedBidLists.BidListDimensions.HasDoubleVerifyBrandSafetyCategoryId` - `AssociatedBidLists.BidListDimensions.HasDoubleVerifyContextualCategoryId` - `AssociatedBidLists.BidListDimensions.HasIntegralBrandSafetyCategoryId` - `AssociatedBidLists.BidListDimensions.HasIntegralContextualCategoryId` - `AssociatedBidLists.BidListDimensions.HasIntegralVideoBrandSafetyCategoryId` - `AssociatedBidLists.BidListDimensions.HasPeer39BrandSafetyCategoryId` - `AssociatedBidLists.BidListDimensions.HasPeer39ContextualCategoryId` - `AssociatedBidLists.BidListDimensions.HasPreBidContextualCategoryId` - `AssociatedBidLists.BidListDimensions.HasSemasioContextualCategoryId` - `AssociatedBidLists.BidListDimensions.HasTTDContextualCategoryId` - `NewBidLists.BidLines.AudigentContextualCategoryId` - `NewBidLists.BidLines.DoubleVerifyBrandSafetyCategoryId` - `NewBidLists.BidLines.IntegralBrandSafetyCategoryId` - `NewBidLists.BidLines.IntegralVideoBrandSafetyCategoryId` - `NewBidLists.BidLines.Peer39BrandSafetyCategoryId` - `NewBidLists.BidLines.TTDContextualCategoryId` - `NewBidLists.BidListDimensions.HasDoubleVerifyBrandSafetyCategoryId` - `NewBidLists.BidListDimensions.HasIntegralBrandSafetyCategoryId` - `NewBidLists.BidListDimensions.HasIntegralVideoBrandSafetyCategoryId` - **POST /v3/bidlist** - `BidLines.AdFontesContextualCategoryId` - `BidLines.AudigentContextualCategoryId` - `BidLines.ComscoreContextualCategoryId` - `BidLines.DoubleVerifyBrandSafetyCategoryId` - `BidLines.DoubleVerifyContextualCategoryId` - `BidLines.FourDContextualCategoryId` - `BidLines.IntegralBrandSafetyCategoryId` - `BidLines.IntegralContextualCategoryId` - `BidLines.IntegralVideoBrandSafetyCategoryId` - `BidLines.Peer39BrandSafetyCategoryId` - `BidLines.Peer39ContextualCategoryId` - `BidLines.TTDContextualCategoryId` - `BidLines.hyScoreContextualCategoryId` - **PUT /v3/bidlist** - `BidLines.ComscoreContextualCategoryId` - `BidLines.DoubleVerifyBrandSafetyCategoryId` - `BidLines.DoubleVerifyContextualCategoryId` - `BidLines.IntegralContextualCategoryId` - `BidLines.TTDContextualCategoryId` - **POST /v3/bidlist/batch** - `BidLines.AudigentContextualCategoryId` - `BidLines.DoubleVerifyBrandSafetyCategoryId` - `BidLines.IntegralBrandSafetyCategoryId` - `BidLines.IntegralContextualCategoryId` - `BidLines.IntegralVideoBrandSafetyCategoryId` - `BidLines.TTDContextualCategoryId` - **PUT /v3/bidlist/batch** - `BidLines.DoubleVerifyBrandSafetyCategoryId` - `BidLines.IntegralBrandSafetyCategoryId` - `BidLines.IntegralVideoBrandSafetyCategoryId` - **PUT /v3/campaign** - `AssociatedBidLists.BidListDimensions.HasDoubleVerifyBrandSafetyCategoryId` - `AssociatedBidLists.BidListDimensions.HasDoubleVerifyContextualCategoryId` - `AssociatedBidLists.BidListDimensions.HasPreBidContextualCategoryId` - **POST /v3/universalforecasting/generate** - `UniversalForecastingBidLists.BidLines.DoubleVerifyBrandSafetyCategoryId` Requests that include these properties after this date will return an error. |
| **Action required** | Update any code that references the properties listed above across these REST endpoints by **February 8, 2027**. For details, see Migrate bid lists to contextual entities. |

### Universal Forecasting REST API: endpoint deprecation

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **February 28, 2027**, the POST /v3/universalforecasting/generate endpoint will be removed. Use the `forecastCreate` mutation in GraphQL instead. **NOTE**: Migration isn't one-to-one. The `forecastCreate` mutation creates a persisted forecast, while this endpoint returns temporary forecast metrics in a single call. Requests to this endpoint after this date will return an error. Separately, effective **February 8, 2027**, the `UniversalForecastingBidLists.BidLines.DoubleVerifyBrandSafetyCategoryId` property will be removed from this endpoint as part of the contextual bid list deprecation. See Contextual bid list deprecation: REST properties. |
| **Action required** | Update any code that calls the `POST /v3/universalforecasting/generate` endpoint to use the `forecastCreate` GraphQL mutation by **February 28, 2027**. To receive forecast results immediately, include the `adGroupLevelForecastResults` field in your `forecastCreate` request. For details, see Forecasting. |

### DoubleVerify viewability: enhanced integration migration

| What you need to know and do |  |
| --- | --- |
| **Change summary** | The Trade Desk now supports DoubleVerify's enhanced viewability integration, which adds metrics such as whether the ad was audible and the actual video player size. In **Q1 2027**, all advertisers who use DoubleVerify for post-bid viewability reporting will be migrated to the enhanced integration automatically. Here's what you need to know: - DoubleVerify takes longer to process the enhanced metrics, so viewability data can be delayed by up to 24 hours. - To migrate before Q1 2027, contact your Technical Account Manager. For column details, see REDS viewability and post-events feeds. |
| **Action required** | No action is required to migrate. If you process the REDS viewability feed, review the new DoubleVerify columns and account for the delay of up to 24 hours before **Q1 2027**. |

## April-June 2027

| Effective Date | Product/Feature | Update Type | Details |
| --- | --- | --- | --- |
| Apr 1, 2027 | GraphQL: Advertiser and ConversionLiftProvider | Field deprecation | Advertiser and ConversionLiftProvider GraphQL types: field deprecation |
| Apr 1, 2027 | GraphQL: Mutation | Endpoint deprecation | Mutation GraphQL type: endpoint deprecation |
| Apr 1, 2027 | GraphQL: Query | Endpoint deprecation | Query GraphQL type: endpoint deprecation |
| Apr 1, 2027 | Reports | Download URL update | Scheduled reports: new download URL format |

### Advertiser and ConversionLiftProvider GraphQL types: field deprecation

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **April 1, 2027**, the `conversionLiftExperiments` field will be deprecated on both `Advertiser` and `ConversionLiftProvider` GraphQL types. |
| **Action required** | Update any code that references the `conversionLiftExperiments` field on the `Advertiser` and `ConversionLiftProvider` types by **April 1, 2027**. |

### Mutation GraphQL type: endpoint deprecation

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **April 1, 2027**, the `conversionLiftExperimentUpdate` field query will be deprecated on the `Mutation` GraphQL type. |
| **Action required** | Update any code that references the `conversionLiftExperimentUpdate` field on the `Mutation` type by **April 1, 2027**. |

### Query GraphQL type: endpoint deprecation

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **April 1, 2027**, the following two fields on the `Query` GraphQL type will be deprecated: - `conversionLiftExperiment` - `conversionLiftExperimentDelta` |
| **Action required** | Update any code that references the two fields on the `Query` type by **April 1, 2027**. |

### Scheduled reports: new download URL format

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **April 1, 2027**, the `DownloadURL` field returned by the scheduled reports API will use a new format. The legacy format will remain valid for 30 days after the change takes effect. Here's the new format, with placeholders in curly braces: ``` api.thetradedesk.com/v3/reports/download/{EXECUTION_ID}/{DELIVERY_ID}?t={TIMESTAMP}&s={SIGNATURE}&src={SOURCE}``` |
| **Action required** | Whether action is required depends on how your integration uses the `DownloadURL` value: - If your integration uses the `DownloadURL` value returned directly by the API without modification, no action is required. - If you hardcode the download URL or parse and reassemble it, update your integration to use the new format. |
