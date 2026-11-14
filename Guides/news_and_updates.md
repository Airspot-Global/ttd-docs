# Platform API Release Notes

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserNews/news/doc/ReleaseNotes
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/doc/ReleaseNotes (retired)
- Retrieved: 2026-11-14
- Category: Guides

---

# Advertiser release notes

These release notes list all new features and updates that have been made to The Trade Desk APIs for advertisers. For announcements of new features and updates to the platform user interface (UI), see Knowledge Portal Release Notes. See also Upcoming API changes for advertisers.

## Product Catalog itemset input types: field deprecation

##### November 9, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **November 9, 2026**, the following GraphQL input fields have been deprecated: - `ItemsetProductFilterInput.searchText`: use `searchCriteria` instead. - `StaticItemsetCreateInput.itemsToAdd`: use `itemsToAddFilter` instead. - `StaticItemsetUpdateInput.itemsToAdd`: use `itemsToAddFilter` instead. - `StaticItemsetUpdateInput.itemsToRemove`: use `itemsToRemoveFilter` instead. **NOTE**: If a request provides both a legacy field and its replacement, the replacement (`*Filter`) field takes precedence. |
| **Action required** | Update any code that references the fields listed above. |

## Timestamp validation

##### October 30, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **October 30, 2026**, data submitted to the `/data/advertiser` and `/data/thirdparty` endpoints with an invalid `TimestampUtc` value is now rejected and returned as a failed line under a new error code, `InvalidTimestampUtc`. Data is considered invalid when it is either: - A timestamp whose expiration (`TimestampUtc` + `TTLInMinutes`) is more than 1 hour in the past. - A timestamp more than 1 hour in the future. |
| **Action required** | To avoid dropped records, make sure the timestamp in UTC on submitted data reflects a current, non-expired value. For details, see Timestamp in UTC |

## TargetingDataSegment GraphQL type: field deprecation

##### October 30, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **October 30, 2026**, the `targetingDataCounts` and `daysUntilLargeExpiration` fields on the `TargetingDataSegment` GraphQL type have been deprecated. Use the newer `targetingDataInsights` field instead, which includes an equivalent `daysUntilLargeExpiration` field alongside additional counts data. |
| **Action required** | Update any code that references the `targetingDataCounts` and `daysUntilLargeExpiration` fields on the `TargetingDataSegment` type. Use `targetingDataInsights` instead. For details, see the following examples. |

The following are example deprecated and new queries that show the update.

This query is **deprecated**—it queries `targetingDataCounts` and `daysUntilLargeExpiration` directly on the `TargetingDataSegment` type:

```
query GetAdvertiserTargetingDataExampleDeprecated($advertiserId: ID!, $targetingDataFilterInput: TargetingDataFilterInput!) {
  advertiser(id: $advertiserId) {
    targetingDataSegments(where: $targetingDataFilterInput) {
      nodes {
        targetingDataCounts {
          activeCounts
          receivedCounts
          lastUpdatedAtUTC
        }
        daysUntilLargeExpiration
      }
    }
  }
}
```

Use this **new** query instead, scoped through `targetingDataInsights`.

> **NOTE**: The `daysUntilLargeExpiration` field now lives inside the `targetingDataInsights` object rather than at the `TargetingDataSegment` level.

```
query GetAdvertiserTargetingDataExampleNew($advertiserId: ID!, $targetingDataFilterInput: TargetingDataFilterInput!) {
  advertiser(id: $advertiserId) {
    targetingDataSegments(where: $targetingDataFilterInput) {
      nodes {
        targetingDataInsights {
          activeCounts {
            devices
          }
          receivedCounts {
            totalUserIdCount
          }
          lastUpdatedAtUTC
          daysUntilLargeExpiration
        }
      }
    }
  }
}
```

## Product catalog guides for travel and automotive data providers

##### October 29, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | If you're a travel or automotive data provider, you can now follow industry-specific guidance to structure your product catalog and connect catalog items to event data. To help you get started, we've published the following guides: - Product catalog for travel data providers: For airlines, hotel companies, and online travel agencies (OTAs). Explains how to define stable item IDs for travel products, map travel attributes to catalog fields, and capture booking-specific details, such as travel dates and party size, with each event. - Product catalog for automotive data providers: For original equipment manufacturers (OEMs), dealer groups, and automotive marketplaces. Explains how to model both build-to-order model lineups and vehicle-level inventory, map vehicle attributes to catalog fields, and connect vehicles to shopping events, such as configuring a vehicle or booking a test drive. |
| **Action required** | None. |

## City GraphQL type: field deprecation

##### October 20, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **October 20, 2026**, the `metro` field has been deprecated on the `City` GraphQL type. Use the `NIELSEN_DMA` field instead. |
| **Action required** | Update any code that references the `metro` field on the `City` type. Use the `NIELSEN_DMA` field instead. |

## GeoSegmentType GraphQL type: enum value deprecation

##### October 20, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **October 20, 2026**, the `METRO` field has been deprecated as an enum value used in queries on the `GeoSegmentType` GraphQL type. |
| **Action required** | Update any code that references the `METRO` enum value on the `GeoSegmentType` type. |

## AdGroupFlightForecast GraphQL type: field deprecation

##### October 20, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **October 20, 2026**, the following five fields on the `AdGroupFlightForecast` GraphQL type have been deprecated: - `decisionPower`: use the `forecastedDecisionPower.decisionPower` field instead. - `lastUpdated`: use the `forecastedSpend.lastUpdated` field instead. - `projectedImpressions`: use the `forecastedSpend.forecastedSpendInImpressions` field instead. - `projectedSpend`: use the `forecastedSpend.forecastedSpendInAdvertiserCurrency` field instead. - `relevance`: use the `forecastedRelevance.relevance` field instead. |
| **Action required** | Update any code that references the five fields on the `AdGroupFlightForecast` type. |

## AdvertiserDataRate and ProviderDataRate GraphQL types: field deprecation

##### October 20, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **October 20, 2026**, the `cost` field has been deprecated on both `AdvertiserDataRate` and `ProviderDataRate` GraphQL types. Use the more type-safe `DataRateCost` entities (such as `HybridDataRateCost`) at `DataRateBasicInfo.DataRateCost` instead. |
| **Action required** | Update any code that references the `cost` field on the `AdvertiserDataRate` and `ProviderDataRate` types. Use the more type-safe `DataRateCost` entities (such as `HybridDataRateCost`) at `DataRateBasicInfo.DataRateCost` instead. |

## CampaignFlightForecast GraphQL type: field deprecation

##### October 20, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **October 20, 2026**, the following eight fields on the `CampaignFlightForecast` GraphQL type have been deprecated: - `decisionPower`: use the `forecastedDecisionPower.decisionPower` field instead. - `forecastedImpressionsTomorrow`: use the `forecastedSpend.forecastedSpendInImpressionsTomorrow` field instead. - `forecastedSpendTomorrow`: use the `forecastedSpend.forecastedSpendInAdvertiserCurrencyTomorrow` field instead. - `lastUpdated`: use the `forecastedSpend.lastUpdated` field instead. - `neededSpendToday`: use the `forecastedSpend.neededSpendToday` field instead. - `projectedImpressions`: use the `forecastedSpend.forecastedSpendInImpressions` field instead. - `projectedSpend`: use the `forecastedSpend.forecastedSpendInAdvertiserCurrency` field instead. - `relevance`: use the `forecastedRelevance.relevance` field instead. |
| **Action required** | Update any code that references the eight fields on the `CampaignFlightForecast` type. |

## Creative GraphQL types: field deprecation

##### October 20, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **October 20, 2026**, the following 5 fields on all Creative-related GraphQL types (`Creative`, `DeprecatedCreative`, `BroadcasterHostedVideoCreative`, `HostedAudioCreative`, `HostedDisplayCreative`, `HostedHtml5Creative`, `HostedNativeCreative`, `HostedNativeVideoCreative`, `HostedVideoCreative`) have been deprecated: - `flightEndDateUTC`: use the `flightEnd` field instead. - `flightStartDateUTC`: use the `flightStart` field instead. - `interstitialSupportId`—this field is deprecated as it is no longer in use (no replacement) - `tagType`: use the `type` field instead. - `tagTypeEnum`: use the `type` field instead. |
| **Action required** | Update any code that references the five fields on the Creative types listed above. |

## FrequencyDistributionMetrics GraphQL type: field deprecation

##### October 20, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **October 20, 2026**, the `frequency` field has been deprecated on the `FrequencyDistributionMetrics` GraphQL type. Use `Frequency` in dimensions instead. |
| **Action required** | Update any code that references the `frequency` field on the `FrequencyDistributionMetrics` type. Use `Frequency` in dimensions instead. |

## GeoReportingMetro GraphQL type: field deprecation

##### October 20, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **October 20, 2026**, the following four fields on the `GeoReportingMetro` GraphQL type have been deprecated: - `countryName`: use `GeoReportingNielsenDma` instead. - `geoSegment`: use `GeoReportingNielsenDma` instead. - `geoSegmentId`: use `GeoReportingNielsenDma` instead. - `metroCode`: use `GeoReportingNielsenDma` instead. |
| **Action required** | Update any code that references the four fields on the `GeoReportingMetro` type. Use `GeoReportingNielsenDma` instead. |

## GeoTarget GraphQL type: field deprecation

##### October 20, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **October 20, 2026**, the `polygonFileDownloadUrl` field has been deprecated on the `GeoTarget` GraphQL type. Use the `CustomGeofence.fileDownloadUrl` field instead. |
| **Action required** | Update any code that references the `polygonFileDownloadUrl` field on the `GeoTarget` type. Use the `CustomGeofence.fileDownloadUrl` field instead. |

## CreativeAdGroupAssociatePayload GraphQL type: field deprecation

##### October 20, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **October 20, 2026**, the `creative` field has been deprecated on the `CreativeAdGroupAssociatePayload` GraphQL type. Use `data` instead. |
| **Action required** | Update any code that references the `creative` field on the `CreativeAdGroupAssociatePayload` type. Use `data` instead. |

## AdGroupBidFactorWorkflowInput GraphQL type: enum value deprecation

##### October 17, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **October 17, 2026**, the `AD_GROUP_UPDATE_INTEGRAL_VIEWABILITY` value has been deprecated as an enum value used in the `steps.mutationName` field of the `adGroupBidFactorWorkflow` mutation (`AdGroupBidFactorWorkflowInput` type). Use `AD_GROUP_UPDATE` instead. This is a semantic-only change—there is no difference in behavior between the two enum values. |
| **Action required** | Update any code that references the `AD_GROUP_UPDATE_INTEGRAL_VIEWABILITY` enum value on the `AdGroupBidFactorWorkflowInput` type. Use `AD_GROUP_UPDATE` instead. For details, see the following examples. |

The following are example deprecated and new mutations that show the update.

> **NOTE**: Only the `mutationName` step value changes; the mutation shape itself is identical.

This mutation is **deprecated**—it sets the `mutationName` step to `AD_GROUP_UPDATE_INTEGRAL_VIEWABILITY`:

```
mutation AdGroupBidFactorWorkflowExampleDeprecated($input: AdGroupBidFactorWorkflowInput!) {
  adGroupBidFactorWorkflow(input: $input) {
    data {
      id
      name
    }
    errors {
      ... on AdGroupBidFactorWorkflowError {
        message
        field
        failedMutationName
        succeededMutationNames
      }
      ... on AdGroupWorkflowAuthError {
        message
        field
      }
    }
  }
}
```

```
{
  "input": {
    "adGroupId": "abujmf1",
    "steps": [
      {
        "mutationName": "AD_GROUP_UPDATE_INTEGRAL_VIEWABILITY",
        "mutationVariables": {
          "input": {
            "id": "abujmf1",
            "isQualityAllianceSuiteEnabled": true
          }
        }
      }
    ]
  }
}
```

Use this **new** mutation instead, with the `mutationName` step set to `AD_GROUP_UPDATE`:

```
mutation AdGroupBidFactorWorkflowExampleNew($input: AdGroupBidFactorWorkflowInput!) {
  adGroupBidFactorWorkflow(input: $input) {
    data {
      id
      name
    }
    errors {
      ... on AdGroupBidFactorWorkflowError {
        message
        field
        failedMutationName
        succeededMutationNames
      }
      ... on AdGroupWorkflowAuthError {
        message
        field
      }
    }
  }
}
```

```
{
  "input": {
    "adGroupId": "abujmf1",
    "steps": [
      {
        "mutationName": "AD_GROUP_UPDATE",
        "mutationVariables": {
          "input": {
            "id": "abujmf1",
            "isQualityAllianceSuiteEnabled": true
          }
        }
      }
    ]
  }
}
```

## Data API version 2 with improved error handling and response format

##### October 13, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **October 13, 2026**, version 2 of the Data API became the default, with standardized and improved error responses. Changes include: - JSON API error responses with `ErrorCode` and `Message` fields - Corrected HTTP status codes - Consistent error messages across endpoints - Per-item serialization errors surfacing in `FailedLines` instead of the entire request failing - New `FailedLines` error codes |
| **Action required** | These changes include breaking changes to existing error response formats. Instructions for using the new version are in the documentation for each Data API endpoint; for example, Using the custom header. Be sure to review the full documentation for the Data API endpoint you're using, and update your integration to use version 2 of the API. |

## Legacy CRM Data REST API: new PiiTypes array in drop-status responses

##### October 4, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **October 4, 2026**, the `PiiType` property has been deprecated in the `DropInfo` and `LatestActivatedDrop` response objects of the get /v3/crmdata/{segmentType}/segment/{advertiserId}/{crmDataId}/{referenceId} endpoint. It is replaced by `PiiTypes`, an array that lists all PII types declared on a drop. Unlike the `PiiType` property, which reflects only the first declared type, the `PiiTypes` array is accurate for drops that declare multiple types. For a response example, see CRM data integration (legacy REST API). |
| **Action required** | If you use the legacy CRM Data REST API, find any code that reads the `PiiType` values from the `DropInfo` or `LatestActivatedDrop` response objects and update it to use the `PiiTypes` array instead. |

## BidFactorDimension and BidLine GraphQL types: field deprecation

##### October 1, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **October 1, 2026**, the following 2 fields on both `BidFactorDimension` and `BidLine` GraphQL types have been deprecated: - `extendedZipCodeGroupSegment` - `geoFenceThirdPartyDataAndBrand` |
| **Action required** | Update any code that references the two fields on the `BidFactorDimension` and `BidLine` types. |

## GraphQL inventoryCommitmentAccept: field query deprecation

##### October 1, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **October 1, 2026**, the `inventoryCommitmentAccept` field query has been deprecated on the `Mutation` GraphQL type. |
| **Action required** | Update any code that references the `inventoryCommitmentAccept` field on the `Mutation` type. |

## Third-party data insights: TargetingDataStatus field deprecation

##### September 11, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | For more consistent data modeling, we've replaced the `TargetingDataStatus` field (queried through the `TargetingData` entity) with the new `TargetingDataInsights` field, now queried through the `TargetingDataSegment` entity. Unlike `TargetingDataStatus`, the new field does not have a `state` subfield with enum values. For details and an updated query example, see Third-party data insights. |
| **Action required** | None. |

## User-defined report schedules: conversion pixel column name change

##### September 3, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **June 1, 2026**, the conversion pixel column name has changed in user-defined report schedules (formerly My Reports) to include the tracking tag ID. Here are the formats of the new column name and the old name for comparison: - **New name**: `[Conversion Data Source Name] - [Tracking Tag ID] - [Graph Selection] - [Metric Name]` - **Old name**: `[Conversion Data Source Name] - [Graph Selection] - [Metric Name]` Report schedules created before **June 1, 2026** will continue to return the old column name. If you update an existing schedule, or create a new schedule, you will receive reports with the new column name. **NOTE**: The data within that column is unaffected by this update. |
| **Action required** | If you have report schedules created before **June 1, 2026** and have a dashboard, script, or ingestion process that reads a conversion pixel column by its name, update it to read the new name before you edit any existing report schedule. |

## Documentation updates: API changes page

##### August 31, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | We've added a new page describing how we classify and communicate API changes, covering our four change categories (additions, behavior changes, new requirements, removals and replacements) and our standard notice periods. For details, see API Changes. |
| **Action required** | None. This isn't tied to a specific product release. It's new reference content to help you plan around future API changes. |

## Bid lists: geotargeting home location

##### August 31, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | We've added a new field, `locationContextType`, to the `bidListCreate` mutation for creating a bid list that targets or blocks users based on home location instead of real-time location. This enables you to include users who reside in the locations you want to target instead of users who are visiting or just passing through those locations. For details, see Target home locations. |
| **Action required** | None. |

## Geofence status, type, and shape performance reports

##### August 31, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | You can now create a geofence performance report that includes individual shapes instead of viewing a report of the entire segment. To do this, you must include the shape ID and shape name in your coordinates. We've also added the following new fields to the `advertiser.customGeofence` query: the `status` field that returns processing progress and errors, and the `type` field that indicates if you, a third-party, or The Trade Desk owns a segment. For details, see Geofence targeting. |
| **Action required** | None. |

## Get started for real-time ID tag

##### August 28, 2026

| What you need to know and do |  |
| --- | --- |
| **Change Summary** | The Trade Desk has published a new guide for the real-time ID tag, which initiates cookie mapping between websites and TDIDs used by the Real-Time Conversion Events API. If you use real-time conversions, this is the recommended cookie mapping option because it supports real-time targeting and measurement while requiring less infrastructure than the match tag solution. |
| **Action Required** | None. To enable this feature, contact your Account Manager or Technical Account Manager. For details, see Real-Time ID Tag. |

## Impression cost deprecation

##### August 19, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **August 19, 2026**, the impression cost metric has been deprecated. |
| **Action required** | None. If a campaign was opted into the Trading Modes beta and used Performance Mode, review any integrations or reports that use impression cost fields, which include the following: - `ImpressionCostInUSDollars` in REDS. - `Impression Cost` and `Impression CPM` in user-defined reports. - `impressionCost` and `impressionCpm` in GraphQL queries. After a campaign reverts to its default behavior, these fields stop returning values. In REDS, the fields remain available but are unpopulated. If your campaign was in Control Mode, no action is required. |

## REST to GraphQL mappings and migration guide

##### August 17, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | We've published a complete field-level reference that maps between every REST endpoint in the Platform API and its GraphQL equivalent. The accompanying migration guide documents exactly how each REST operation, field, and pattern translates to GraphQL, including field naming, identifiers, pagination, error handling, timestamps, and structural differences between response types. Each domain page summarizes its endpoints and shared types, and links to endpoint detail pages with field-by-field input and output mappings as well as before and after code examples. Use the guide to migrate an existing REST integration or to choose GraphQL for new functionality with a clear, mechanical path from REST to GraphQL. |
| **Action required** | None. For details, see REST to GraphQL migration guide and the relevant domain and endpoint reference pages. |

## Trading Modes closed beta has ended

##### August 14, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **August 17, 2026**, the Trading Modes closed beta has ended. You can no longer assign a trading mode to any new or existing campaigns. Here's what this means for your campaigns: - Campaigns using Control Mode continue to function as-is. Control Mode functions as the standard campaign behavior. - Campaigns using Performance Mode are automatically reverted to the standard campaign behavior. - All premium features that were turned on with Performance Mode, such as Predictive Clearing, Identity Alliance, Prism, Audience Unlimited, and Quality Alliance, remain on and become individually configurable. |
| **Action required** | None. |

## Audience Unlimited decoupled from Trading Modes

##### August 14, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **August 17, 2026**, Audience Unlimited entered open beta and now operates independently from Trading Modes. This change follows the end of the [Trading Modes closed beta](#trading-modes-closed-beta-ends). |
| **Action required** | None. To request access to Audience Unlimited, contact your Technical Account Manager. For configuration instructions and details on each tier, see [Audience Unlimited](/doc/AudienceUnlimited). |

## Open Agentic Kit available in private beta

##### August 10, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **August 10, 2026**, Open Agentic Kit (OAK) is available in private beta. OAK is The Trade Desk's MCP-based access to Ask Koa, which brings The Trade Desk platform data and actions directly into the AI tools your traders and operations teams already use. For details on what's available today and what's coming later this year, see Open Agentic Kit overview. |
| **Action required** | None. OAK access is currently available to select partners in private beta. To register your interest, contact your account representative at The Trade Desk. To connect after you're approved, see Get started with Open Agentic Kit. |

## Enhancements to Koa Optimizations

> **IMPORTANT**: This documentation is for the latest version of Koa. For an earlier version, see Koa Optimizations.

##### August 10, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | We've updated Koa Optimizations with an expanded dimension list. This gives Koa more signals to evaluate at bid time, enabling smarter decisions across a broader range of inventory. The new Koa exposes the system's evaluation logic at the grain level through bid factors, so you can see exactly how each impression is being assessed and better understand what's driving campaign behavior. For details, see Koa Optimizations. |
| **Action required** | None. The latest version will be gradually deployed on all eligible campaigns by batch. Ad group owned bid lists are used as the system override. |

## Enabled value-added providers property deprecation

##### August 3, 2026

| What you need to know and do |  |
| --- | --- |
| **Change Summary** | Effective **August 3, 2026**, as part of The Trade Desk's broad shift to ID-based fields, the `EnabledValueAddedProviders` field for campaigns and ad groups was fully deprecated and replaced with the `EnabledValueAddedProviderIds` field. Instead of an array of provider name strings, the new field accepts an array of provider ID integers. Using the `EnabledValueAddedProviders` field will return errors. |
| **Action Required** | Update your integration to use the `EnabledValueAddedProviderIds` field. |

## Report download link now requires authentication

##### July 24, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **June 17, 2026**, download links returned in the `downloadLink` value for scheduled reports and predefined reports require an API token to access and download the report. |
| **Action required** | Whether action is required depends on how your integration uses the download link: - If your integration already attaches an authentication token when requesting the link, no action is required. - If your integration opens the link directly without authentication, either include a token, or create a new report schedule that sends the report to an email address to receive a browser-accessible link instead. For details, see Retrieve report and schedule details. |

## Impression placement ID update

##### July 13, 2026

| What you need to know and do |  |
| --- | --- |
| **Change Summary** | Effective **July 13, 2026**, `ImpressionPlacementId` values in bid lists were updated to exactly match values provided by the publishers. The Trade Desk longer applies custom updates to these IDs. For example, most placement prefixes will be restored, and some generic values will change to publisher-specific paths with unique site IDs. |
| **Action Required** | Review the `ImpressionPlacementId` entries in your target or optimized lists and update any affected values as soon as possible. If you need help identifying affected values or confirming updates, contact your Technical Account Manager. For example, you can request a list of affected values and their updated equivalents. Your Technical Account Manager also proactively reached out if your account is affected. |

## Creating circle geofence segments with GraphQL

##### July 8, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | You can now use GraphQL to create circle geofence segments, also known as radius targeting, by defining one or more circles with center point coordinates and a radius. You can provide your coordinates directly in the mutation or upload them in a file, and set either a uniform radius for all circles or a different radius for each one. For details, see Geofence targeting. |
| **Action required** | None. This is a new feature. |

## Hit counts: a new ID counting methodology

##### July 6, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Hit counts are now available for web and app pixel data. Hit counts report the number of IDs ingested into a segment during a given time period, without deduplication. Unlike received counts, which count each unique ID once, hit counts count every ingestion, so you can use them to confirm how much data you've sent and troubleshoot ingestion issues. Active counts are not affected by this change. For details, see ID counting methodologies. **NOTE**: Received counts are scheduled to be deprecated and replaced by hit counts on **October 13, 2026**. For details, see Upcoming API changes for advertisers. |
| **Action required** | None. |

## Adbug page quality fields deprecation

##### July 1, 2026

| What you need to know and do |  |
| --- | --- |
| **Change Summary** | Effective **July 1, 2026**, The Trade Desk deprecated Adbug page quality bid list fields. Adbug is a China-specific fraud verification vendor that's no longer operational and is not supported in Kokai. The following **GraphQL** fields were removed: - `/BidLine/adBugPageQualityCategory` - `/BidLine/adBugVideoPageQualityCategory` - `/BidListDimension/HAS_AD_BUG_PAGE_QUALITY_CATEGORY_ID` The following **REST** properties were removed: - `AdBugPageQualityCategoryId` - `AdBugVideoPageQualityCategoryId` Requests that include these fields will return an error. |
| **Action Required** | Update your bid list workflows to remove the deprecated fields from `BidLines` objects as soon as possible. For details, contact your Technical Account Manager. |

## Data API SDK

##### June 24, 2026

| What you need to know and do |  |
| --- | --- |
| **Change Summary** | The new Data API SDK provides a comprehensive, unified interface for onboarding and managing data within the platform. Its primary features include: - Onboarding of the following types of data to The Trade Desk: conversions, first-party segments, and third-party segments. You can also manage optouts and deletions. - Built-in conversion to UID2s or EUIDs - Built-in secure authentication |
| **Action Required** | None. This is a new feature. For details, see Data API SDK. |

## Koa bidding strategy

##### June 11, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | You can now control how Koa balances performance and spend across your campaign with the new Koa bidding strategy feature. By default, Koa prioritizes performance and full budget delivery. If your campaign has different spending goals, you can switch to CPM efficiency or waterfall allocation instead. |
| **Action required** | None. For details, see Koa bidding strategy. |

## Impression cost reporting updates

##### May 27, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | The Trade Desk has updated impression cost calculations, and these changes apply across user-defined reports (formerly MyReports), UI-based reports such as Portfolio View and Reports Dashboard, and GraphQL queries. **NOTE**: These updates are not backfilled and apply only from this date moving forward. |
| **Action required** | None. If you don't have permission to view user-defined reports, contact your Technical Account Manager. |

## Realytics measurement deprecation

##### May 22, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **May 24, 2026**, Realytics will cease all operations. The Trade Desk will remove Realytics incremental reach measurement services from the platform, and any workflows that include these services will no longer function. |
| **Action required** | Choose an alternative incremental reach measurement provider as soon as possible. For details and guidance on alternative solutions, contact your Technical Account Manager. |

## Report templates query and field changes

##### May 22, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | We've renamed the following query and field names for report templates. Your existing integration will continue to work, but we recommend planning a migration to `reportingTemplates` at your convenience. Type · Old name · New name<br>Query · `myReportsReportTemplates` · `reportingTemplates`<br>Field · `derivedReportTemplate.isDerived` · `derivedReportTemplate.partialAccess` |
| **Action required** | None. Note that the new query behaves slightly differently, so review the updated documentation before migrating. For details, see User-defined report templates. |

## REDS updates

##### May 20, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | As The Trade Desk introduces new features and enhancements, our objective is to ensure REDS delivers more comprehensive data and insights. An updated version of the schema is being provided alongside your existing schema. Both versions are available concurrently until the legacy schema is deprecated. New REDS clients will be onboarded directly onto the enhanced platform. The improved REDS version incorporates the following modifications: - **Data retention**: Data retention are updated to 99 days to better comply with privacy standards, compared to the previous retention period of one year plus 99 days. - **Fields**: New fields are introduced. Some existing fields are renamed, and others are deprecated or removed. For the most up-to-date field specifications, see Impressions, Conversions, Clicks, and Video events. - **Amazon S3**: - File paths and names are revised to follow new naming conventions. - All files feature headers. - **Snowflake**: New views are provided within your existing secure share. |
| **Timeline** | Upgraded versions of the product features will be available on **May 25, 2026**. Existing versions will be discontinued on **September 30, 2026**, except for Snowflake for Viewability Metrics, which will be discontinued in **October 2026**. These dates are subject to change, and you will receive a minimum notice of 90 days. |
| **Action required** | Update your REDS integration before the discontinued date for each feed. Both current and upgraded REDS are available until then. If you complete your updates early or have questions, contact your Technical Account Manager. |

For specific updates, see the following REDS product features.

| Product Feature | Feed Type |
| --- | --- |
| Nielsen DMA | Impressions |
| Trading Modes and Audience Unlimited | Impressions |
| Viewability metrics | Video Events |
| Inventory reporting | Impressions |
| Fold placement property deprecation | Impressions |
| Legacy identifier REDS schema | Impressions, conversions, clicks |
| Previously announced field updates | Impressions |

### Metro field update

| What you need to know and do |  |
| --- | --- |
| **Change summary** | The Trade Desk has renamed the `Metro` geography in REDS to standardize our naming conventions with Nielsen designated market areas (DMA) geographies. The `Metro` field in REDS impression feeds is deprecated and replaced with `Nielsen DMA`. |
| **Action required** | We recommend updating your Nielsen DMA schema as soon as possible. The earlier you adopt the new field, the easier it will be to ensure you continue receiving Nielsen DMA values in your REDS integrations. |

* © 2026, The Nielsen Company (US), LLC. The DMA® data is used pursuant to a license from The Nielsen Company (US), LLC. Any use and/or reproduction of these materials without the express written consent of The Nielsen Company (US), LLC, is strictly prohibited. DMA® data is valid for the period 2025 - 2026. DMA® is a registered service mark of The Nielsen Company (US), LLC and is used pursuant to license.

### REDS viewability and post-events feed updates

| What you need to know and do |  |
| --- | --- |
| **Change summary** | We updated the REDS viewability and post-events feed with enhanced fields and improved features. These updates provide advanced metrics in The Trade Desk post-bid marketplace. If you're using DoubleVerify or Quality Alliance and the REDS feeds, the changes include the following: - All viewability-related fields are available only in the REDS viewability and post-events feed. - The `IsTrackable` and `IsViewable` fields in the Viewability feed are deprecated. Data ingestion timing depends on how you receive REDS: - **Amazon S3**: Available for immediate ingestion. - **Snowflake**: Ingestion begins in October 2026. |
| **Action required** | No action is required, as the feed is added through bulk enablement. To opt out of bulk enablement, manually enable the feed. **IMPORTANT**: If you use Integral Ad Science (IAS) post-bid viewability in REDS, make sure you're using this feed, as the data isn't available in the video events feed. For details, contact your Technical Account Manager. |

### Inventory reporting field updates

| What you need to know and do |  |
| --- | --- |
| **Change summary** | To improve supply chain clarity, we updated our supply vendor fields for OpenPath and introducing new selling party fields for all inventory. Here's a summary of the changes: - Supply vendor field changes for OpenPath connections: - The `SupplyVendor` field is an empty string. This field is a text-based representation of the supply vendor (for example, `freewheel`). - The `SupplyVendorName` field is an empty string. This field is a user-friendly representation of the supply vendor. - The `SupplyVendorId` field is `0`. This is an integer-based ID of the supply vendor. - New selling party fields to help you understand the origin of the inventory being purchased. They include the following: - The `SellingPartyName` field for the name of the seller, publisher, or intermediary. - The `SellingPartyType` field for the type of selling party (seller, publisher, or intermediary). - The `SellingPartyId` field for the known agent ID of the selling party. The following user-defined reports are impacted: - Report type - Ad server reporting - Additional fees report - Aggregated retail performance report - Aggregated retail sales report - Available bid request reporting - Category element - Content signals report - Data element - DCO server report - Deal reconciliation reporting - Inventory contract delivery report - Performance (100 days, all metrics) - Performance (lifetime, fewer metrics) - Unique reach geo reporting |
| **Action required** | No action is required. If you have questions, contact your Technical Account Manager. |

### Fold placement property deprecation

| What you need to know and do |  |
| --- | --- |
| **Change summary** | The Trade Desk is deprecating the following: - `PlacementPositionRelativeToFold` bid dimension - `Fold` field in user-generated reports (formerly My Reports) - `MatchedFoldPosition` field in REDS Impressions feeds - `MatchedFoldPositionName` field in REDS Impressions feeds This deprecation improves campaign performance by focusing on more reliable and effective optimization signals. |
| **Action required** | Remove all fold placement bid lists from your ad groups as soon as possible. The earlier you begin, the easier it will be to collaborate with your Technical Account Manager and transition to alternative strategies. For instructions on querying and removing bid lists, see the following: - Create and manage bid lists in GraphQL - Create and manage bid lists in REST For more information, contact your Technical Account Manager. **TIP**: To optimize viewability, we recommend using the Quality Alliance Viewability Suite within the platform UI. This advanced solution leverages actual measurement data to score every impression and dynamically adjust bids without limiting your campaign's scale. |

## Report column deprecation

##### May 6, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | The `White Ops SIVT Bids Avoided` report column in user-defined reports has been deprecated. It will now always return `0` and no longer reports fraud detection counts. |
| **Action required** | Remove the `White Ops SIVT Bids Avoided` column from all scheduled reports. |

## Field renamed for DMA geotargeting

##### April 27, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | The Trade Desk is replacing the `Metro` field with a new `NielsenDMA` field for metropolitan area geotargeting and reporting. Nielsen designated market areas (DMAs) are a free geotargeting and reporting dimension. Both field names are supported until **July 6, 2026**, after which the `Metro` field will be deprecated and references to it will return errors. |
| **Action required** | Before **July 6, 2026**, update any references to `Metro` in your reporting workflows and targeting configurations (such as in bid lists) to use the `NielsenDMA` field instead. **NOTE**: The `NielsenDMA` field returns values _only_ for DMAs that are explicitly targeted. If your reporting requires complete DMA coverage, make sure all 210 Nielsen DMAs are intentionally targeted. |

* © 2026, The Nielsen Company (US), LLC. The DMA® data is used pursuant to a license from The Nielsen Company (US), LLC. Any use and/or reproduction of these materials without the express written consent of The Nielsen Company (US), LLC, is strictly prohibited. DMA® data is valid for the period 2025 - 2026. DMA® is a registered service mark of The Nielsen Company (US), LLC and is used pursuant to license.

## Contextual targeting with entities and groups

##### May 4, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | You can now create and manage contextual targeting strategies using contextual entities instead of bid lists. A contextual entity consists of groups of categories to target or block and is configured with a shared tactic. You then assign the entity to your ad groups. Unlike setting up contextual targeting in bid lists, contextual entities enable you to combine categories from multiple providers into a single strategy and reuse it across multiple ad groups. |
| **Action required** | None. For details, see Contextual category configuration. |

## Tracking full-site events in Shopify

##### April 22, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | You can now track conversion data from five key events with a direct Shopify integration. Events include site visit, product page view, add to cart, checkout, and purchase, with SKU-level data for the last four. |
| **Action required** | None. For details, see Tracking full-site events in Shopify. |

## The Trade Desk conversion lift studies (closed beta)

##### April 17, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | You can now create and manage The Trade Desk conversion lift studies that enable you to measure the incremental impact of your campaigns by comparing conversion rates between users who were exposed to your ads and a control group that wasn't. |
| **Action required** | None. For details, see The Trade Desk conversion lift studies. **NOTE**: This feature is available to select clients through a closed beta. For details, contact your Technical Account Manager. |

## Databricks connector solutions

##### April 6, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | The Trade Desk now provides a Databricks connector that enable you to securely onboard conversion and segment data from your Databricks account and access log‑level data within The Trade Desk. |
| **Action required** | None. For details, see Databricks connector. |

## New reporting solution: on-demand reporting queries

##### April 3, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | We've introduced on-demand reporting queries, a new way to retrieve aggregated reporting data directly in the API response. Unlike scheduled reports, these queries return results on demand, enabling you to select the metrics and dimensions you want, and retrieve data immediately without generating or downloading a file. These queries cover the most frequently used reporting metrics, which includes metrics used in over 70% of scheduled reporting use cases. |
| **Action required** | None. For details, see On-demand reporting queries. |

## New brand-agency organization model for UMP

##### March 23, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | To provide true shared access without transferring ownership or control, we've updated the User Management Platform (UMP) organization model and shared administrative access, which helps clarify the relationship between brands and agencies within the UMP. For details, see User Management Platform. |
| **Action required** | None. If you are a UMP admin for a brand or agency, review the access granted to user admins and update it as needed. |

## Snowflake Native App tracking tags feature

##### March 20, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | In The Trade Desk connector Snowflake Native App we've added a Tracking Tags page—a handy facility for customers who are uploading offline conversion data, where you can look up offline tracking tags that are valid in the context of the current activity. |
| **Action required** | None. For details, see The Trade Desk connector native app: Tracking tags. |

## Forecasting

##### March 17, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | We’ve updated forecasting with expanded GraphQL support, making it easier for you to programmatically estimate spend, reach, and delivery across campaign configurations. You can now generate and manage forecasts through the API with greater flexibility, alongside existing UI workflows. |
| **Action required** | None. For details on how to use GraphQL to manage forecasts, see Forecasting. |

## New GraphQL API for uploading creatives (closed beta)

##### March 2, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | We've streamlined how you upload creatives for ad groups by introducing a GraphQL API. This expands our GraphQL support for creatives and improves upon the REST API by enabling you to choose whether eligible creatives are approved automatically. Automatically approved creatives don't require manual review or encoding workflows after upload. |
| **Action required** | None. For details about the GraphQL option, see Creatives. To learn more about automatic approval, see Enable automatic approval. **NOTE**: This feature is available to select clients through a closed beta. Ask your Technical Account Manager for access permission to the API. |

## First-Party Data Uploader

##### March 2, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | We’ve introduced the First-Party Data Uploader, an upgraded and expanded replacement for the legacy CRM Data API. This new GraphQL‑based tool supports all ID types without requiring UID agreements for anonymous identifiers. It’s also our most efficient and flexible method yet for ingesting first‑party data at scale. **NOTE**: Directly identifiable IDs are still available only to advertisers and partners who have signed the UID agreement. |
| **Action required** | None. To see how the new tool compares to the available direct-upload methods, see ID-based first-party data. |

## Snowflake Native App optout/deletion pages

##### February 25, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | In The Trade Desk connector Snowflake Native App, you can now submit requests to opt out or delete user IDs across all data segments associated with your partner account, or any account you are authorized to act on behalf of. Three data opt‑out and deletion workflows are available: for first-party data, third-party data, and merchants managing data. |
| **Action required** | None. For details, see Snowflake connector. |

## Trading Modes: default mode update (closed beta)

##### February 20, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Starting **February 20, 2026**, the default trading mode for newly created and cloned Kokai campaigns is Control Mode. Audience Unlimited is disabled by default, but complimentary access remains available. Trading Modes defines how bidding, pacing, and optimization are managed. You can choose between two modes: - **Performance Mode** (recommended): Automatically turns on premium performance features and relies on Koa, the AI that powers the platform, to prioritize the highest-value impressions and optimize bidding, pacing, and other campaign decisions based on your inputs and goals, which minimizes the need for manual adjustments and while maximizing campaign performance. - **Control Mode** (default): This mode enables you to manually select and configure individual features and campaign settings manually, while still giving you the option to use AI-powered optimizations. **NOTE**: This feature is available to select clients through a closed beta. For details, contact your Technical Account Manager. |
| **Action required** | None. |

## Campaign pacing stability improvements

##### February 6, 2026

| What you need to know and do |  |
| --- | --- |
| **Change summary** | We improved the pacing system to increase stability and reduce instances of overpacing during sudden shifts in market dynamics. This improvement helps the platform respond more effectively to large changes in available inventory, resulting in more consistent delivery and spend behavior. |
| **Action required** | No action is required. |
