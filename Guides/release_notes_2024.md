# 2024 Advertiser release notes

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserNews/news/doc/ReleaseNotes2024
- Retrieved: 2026-11-14
- Category: Guides

---

# 2024 Advertiser release notes

These release notes list all new features and updates that have been made to the Platform API in 2024. For announcements of new features and updates to the platform user interface (UI), see Knowledge Portal Release Notes. See also Upcoming changes and schedules.

## November 27, 2024

### Geofence targeting update

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Starting **December 1, 2024**, Nevada will join Connecticut, Washington, and New York, as the list of US states that require a minimum radius of 3,000 feet (914 meters) per point in a geofence segment. To comply with local laws, existing geofence segments that contain points in Nevada with a radius of less than 914 meters will have their points be deleted. |
| **Action required** | If you have any geofence targeting points in Nevada with a radius of less than 914 meters, you must create a new geofence segment with your previous points that complies with this change by **December 1, 2024**. Third-party geofence data providers are advised to update their points to comply with the policy changes. |

## November 20, 2024

### Auto-reservation for ad group budgets

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Budgets allocated to ad groups using the `minimumSpendInAdvertiserCurrency` property are now automatically reserved, regardless of whether the ad groups are active or enabled to spend (`isEnabled` property). For more details and FAQs, see Budget allocation. |
| **Action required** | No action is required. |

## November 13, 2024

### Audience Excluder upgraded to Prism

| What you need to know and do |  |
| --- | --- |
| **Change summary** | The Audience Excluder has been renamed to Prism and enhanced to focus on the most valuable impressions by excluding irrelevant user-based and non-user-based signals that are unlikely to benefit a campaign. To ensure exclusions happen without compromising campaign delivery, it now works in real time with the pacing algorithm, which eliminates the previous four-day refresh cycle. Here's what it means for your campaigns: - At the advertiser and ad group levels in REST API, Prism settings are controlled by the existing `AudienceExcluderEnabled` property. Its use remains unchanged. - In GraphQL API, Prism is controlled by the new `prism` property, currently available only at the advertiser level. - By default, Prism is disabled. However, any existing ad groups that have Audience Excluder enabled will have Prism automatically turned on. - You can turn Prism on for all ad groups at the advertiser level unless you are advertising in the following IAB categories: Personal Finance, Careers, Real Estate. For details, see Prism. |
| **Action required** | No action is required. |

### Advertiser settings: AudienceBoosterEnabled property updated

| What you need to know and do |  |
| --- | --- |
| **Change summary** | The `AdvertiserAudienceSettings.AudienceBoosterEnabled` property, which allows you to configure ad group data settings at the advertiser level, is now disregarded in advertiser workflows and will be fully deprecated in **Q2 2025**. |
| **Action required** | To enable the platform to add highly relevant segments to your audience when there is confidence they will improve your targeting and boost performance, continue using the `RTBAttributes.AudienceTargeting.AudienceBoosterEnabled` property in the ad group workflows. Remove the deprecated `AdvertiserAudienceSettings.AudienceBoosterEnabled` property from your advertiser workflows by **Q2 2025**. |

## October 29, 2024

### Third-party data ID validation for bidding eligibility

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Starting **October 29, 2024**, all third-party data IDs in segments are validated to check if they are biddable. Data group workflows will fail when non-biddable third-party data IDs are included in the `ThirdPartyDataIds` array. |
| **Action required** | Start using the POST /v3/dmp/thirdparty/advertiser endpoint to check if segments are buyable beforehand, then remove all third-party data IDs that are not listed from your POST and PUT data group workflows. |

## October 1, 2024

### Ad group channel selection updates

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Starting **October 1, 2024**, the `ChannelId` property is required for all ad group workflows in Kokai, with the following supported values: `Display`, `Video`, `Audio`, `NativeDisplay`, `NativeVideo`, `TV`, and `OutOfHome`. In Kokai, the ad group channel will be used to inform bidding behavior and provide recommendations and insights. For example, if you choose `Display`, we'll buy only display content for that ad group. If you choose `TV` for an ad group targeting display inventory, we won't bid. Here's what it means for your integration: - The ad group creative type must match the channel. - You cannot update the ad group channel after the flight starts. - Any deprecated values (`Other`, `Mixed`, `Native`, `TVPersonal`) included in create and update requests will result in a 400 (Bad Request) error. - If a Solimar ad group with its channel set to `Mixed` is upgraded to Kokai, channel filtering is now ignored. - `Mixed` is no longer be accepted as a `ChannelId` property value when cloning campaigns. For details, see Channels. |
| **Action required** | - Update all your ad group workflows to include the required `ChannelId` property and its updated values by **October 1, 2024**. - When cloning campaigns, update any ad groups with the `ChannelId` property set to `Mixed` to the appropriate value supported in Kokai. |

## September 30, 2024

### Video playback type value update

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Starting **September 30, 2024**, we'll no longer accept the `InBanner`, `InArticle`, `InFeed`, and `Outstream` values in the `VideoPlaybackType` property in the ad group endpoints and will return a 400 (Bad Request) error. |
| **Action required** | Update all your ad group workflows to use the new `AccompanyingContent` and `Standalone` values in the `VideoPlaybackType` property by **September 30, 2024**. |

To align with the evolving landscape of video content and provide much-needed clarity for both the sell side and buy side, the IAB Tech Lab is planning to deprecate the `video.placement` field. Instead, it will use only the `video.plcmt` field, which better differentiates between in-stream and out-stream inventory and reflects more accurately the different levels of user engagement provided by various video placements. For details, see March 2023 Update To OpenRTB Is Now Ready For Implementation!

> **NOTE**: Any existing targeting settings with the video playback types will be updated using the bid list endpoints.

### RetentionEnabled property deprecation

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Starting **September 30, 2024**, the `RetentionEnabled` field will be removed from the POST /v3/crmdata/{segmentType}/segment/{advertiserId}/{crmDataId} and POST /v3/crmdata/segment/{advertiserId}/{crmDataId} endpoints. By default, all targeting segments will retain hashed email addresses and phone numbers for 90 days to refresh UIDs daily. **NOTE**: Update (March 2025): The retention period is now 180 days. This release note reflects the policy at the time of release. |
| **Action required** | Update your workflows to remove the deprecated field by **September 30, 2024**. |

### Grapeshot and Moat deprecation by Oracle

| What you need to know and do |  |
| --- | --- |
| **Change summary** | As Oracle Advertising is sunsetting their pre- and post-bid products, Grapeshot and Moat, any targeting strategies that depend on these Oracle products will not function after **September 30, 2024**. All workflows using Moat Reporting will be automatically migrated to our new white-labeled product unless you choose to opt out. |
| **Action required** | Choose an alternative product as _soon as possible_. - For Grapeshot standard and custom contextual categories, we recommend considering The Trade Desk Contextual categories. - For other Oracle features—such as Grapeshot Content Affinity, Grapeshot Predicts, Moat Viewability, Grapeshot Language, Grapeshot Brand Safety, and Moat Invalid Traffic—contact your Account Manager for guidance on alternative solutions. - If you prefer to use an alternate provider for Moat Reporting, request the necessary form from your Account Manager and opt out of the default migration by **September 23, 2024**. Be sure to update your advertiser or partner settings with the new provider by **September 30, 2024**. |

### Household graph selection changes

| What you need to know and do |  |
| --- | --- |
| **Change summary** | We are removing Adbrain Household as a selection for our API users. Starting **September 30, 2024**, we'll automatically redirect all API calls with Adbrain Household (Cross-Device Vendor ID `8`) to Identity Alliance Household (Cross-Device Vendor ID `11`). |
| **Action required** | Update all your campaigns and ad group workflows currently leveraging Adbrain Household (Cross-Device Vendor ID `8`) to use the Identity Alliance Household Graph (Cross-Device Vendor ID `11`). |

## August 14, 2024

### Koa v3.5 and Koa Optimizations for Kokai

We are excited to announce the release of Koa v3.5, featuring enhanced Koa Optimizations that leverages advanced machine-learning algorithms to offer you greater confidence, control, and flexibility in managing your ad groups.

Here's a quick overview of the key Koa v3.5 features:

-

**Dimension-Level Granularity:** In Kokai, Koa Optimizations is off by default. By turning on Koa Optimizations for specific bid dimensions, you can now ensure your budget is allocated to the highest-performing impressions available.

-

**Seamless Integration:** With Koa v3.5, you can easily manage optimizations using the new `KoaDimensions` object, which simplifies the integration process and enhances your overall experience.

-

**Backward Compatibility:** For backward compatibility, all responses include the Koa v3 (Solimar) properties.

The following table lists the properties that are intended to be used only for the respective experience (Solimar or Kokai).

| Solimar (Koa v3) Properties | Kokai (Koa v3.5) Properties |
| --- | --- |
| `IsEnabled` `OptionalDimensions` `IsBiddingUpEnabled` | `KoaDimensions` `KoaOptimizationsMinorVersion` |

> **IMPORTANT**: You must use only the new Koa v3.5 properties to manage Koa Optimizations in Kokai. Using the old Koa v3 properties can lead to a more complex integration and a degraded user experience.

For details, see Koa Optimizations.

### New GraphQL mutation: Create campaign

We've added a new option for creating campaigns using GraphQL API. With the `createCampaign` mutation, you can create a single campaign in a single call.

For details, see Create campaigns.

## August 12, 2024

### GraphQL Schema Explorer

To provide deeper insight into the structure of The Trade Desk GraphQL schema, we've launched the GraphQL Schema Explorer. It's an interactive tool for building and testing queries and mutations. Feel free to experiment and explore!

## August 8, 2024

### Additional ad group property deprecations in Kokai

The following ad group `RTBAttributes` properties for performance-enhancing features have been deprecated in Kokai:

- `AudienceTargeting.AudienceRetargetingEnabled`
- `AudienceTargeting.AudienceRetargetingSettings`
- `AudienceTargeting.TargetDemographicSettings`
- `AudienceTargeting.TargetDemographicSettingsEnabled`
- `AudienceTargeting.TargetInterestSettings`
- `AudienceTargeting.TargetInterestSettingsEnabled`
- `ContractTargeting.UseContractFloorPriceAsBaseBid` (the **Help me reach floor price** feature in the UI)

This change applies only to Kokai ad groups; Solimar ad groups retain these properties.

## August 02, 2024

### Oracle cross-device vendor removal

Starting **August 02, 2024**, Oracle is no longer a cross-device graph vendor.

The removal applies to the following in The Trade Desk platform:

| Feature | Vendor Name | Vendor ID | Impact | Action required |
| --- | --- | --- | --- | --- |
| Cross-Device | `Oracle Cross Device` | `2` | Ad group workflows using Oracle as the Cross-Device vendor in the `RTBAttributes.AudienceTargeting.CrossDeviceVendorListForAudience` property will no longer function. | To continue using cross-device graphs, update your Cross-Device settings with an alternative vendor. |

## June 4, 2024

### Property deprecation in Kokai: Campaign objective

The `Objective` property in the campaign endpoints which used to define a high-level objective for a campaign (awareness, consideration, conversion), has been deprecated and replaced by the `FunnelLocation` property in the ad group endpoints. This change applies only to Kokai campaigns; Solimar campaigns retain the property.

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Solimar campaigns are not affected. In Kokai, if an ad group has no funnel location specified, it is automatically assigned based on the campaign's primary goal. The campaign's objective is ignored. |
| **Action required** | For all ad groups, set the `FunnelLocation` value to the high-level objective that you want to assign to the ad group. For details, see Funnel location. |

## May 28, 2024

### Kokai (open beta): The new platform experience at The Trade Desk

Kokai is our new approach to digital advertising innovation that incorporates major advances in distributed artificial intelligence (AI), measurement, partner integrations, and a revolutionary, intuitive user experience. With these innovations, Kokai ensures that marketers at all levels can easily benefit from the full power and sophistication of programmatic advertising.

The following sections outline feature updates and recommended actions:

- Updates
- Recommended actions
- Coming soon

See also Budget allocation updates and Campaign upgrade to Kokai.

#### Updates

> **IMPORTANT**: Most of the listed updates are driven by and apply to "Kokai campaigns"—campaigns created in Kokai or upgraded to leverage Kokai enhancements. Before making calls, be sure to use the GET /v3/campaign/{campaignId} endpoint to look up the version of the campaign. All Kokai campaigns are indicated by the `Version` property value set to `Kokai`. See also Recommended actions.

The following table outlines the key new features, updates, and functionalities in Kokai.

| Feature | Description | API Usage Notes | Further Reference |
| --- | --- | --- | --- |
| Campaign workflows | You can use the REST API or GraphQL API to create, clone, and manage campaigns, including managing campaigns and their flights in bulk. With the GraphQL API, you can now clone multiple campaigns at once, make multiple copies of each campaign, and set new properties as needed. | Additive, non-breaking change, with more cloning options and bulk operations, with a new `Version` property set to `Kokai` in both APIs. | - Upgrade Solimar campaigns to Kokai - Campaigns - Clone campaigns |
| Seeds | Seeds are at the core of Kokai. By creating a seed representing your ideal customer and attaching it to your campaigns, you unlock relevance—our metric gauging alignment between your campaign targeting and your seed. The higher the relevance, the more the audience you are targeting shares traits and behaviors with your seed. Seeds power various parts of the buying experience, including Koa, lookalike modeling, segment recommendations, automated targeting strategies, measuring relevant reach, and fractional pricing. | Non-breaking change. As a new entity, seeds are created and managed in GraphQL, with a new optional `SeedId` property added to REST campaign endpoints. | Seeds |
| Budget Allocation | You can automatically optimize your budget by allocating it to ad groups that demonstrate optimal relevance and better value. We recommend using fluid, value-driven budgets and implementing other elements of your IO and strategy. For example, you can set your base and max bids and specify bid factors, thus, gaining control over placements and pricing and allow our tools to make sure you're getting the best value and relevance. | Breaking change. You must use the GraphQL API to manage Kokai-budgeted campaigns. **UPDATE**: Starting **April, 4, 2025**, budget allocation is no longer a breaking change in Kokai. For details, see Release notes. | Budget allocation updates |
| Funnel location | This is a new foundational component for each ad group that helps you measure performance across a campaign and across the advertiser at each level of the funnel. The goal is to help you set campaigns up for success with a full-funnel approach to drive greater performance and conversion rates. | Non-breaking change, with a new `FunnelLocation` property. | Ad groups |
| More control over inventory quality and delivery at scale | We have introduced Sellers and Publishers 500+, a new inventory buying option that represents the easiest and most efficient way to buy the best of the open internet. Comprised of high-quality inventory from the top 500+ inventory properties across the open internet, the SP500+ eliminates unnecessary complexity and fragmentation while enforcing the highest inventory standards. Each seller and publisher was included because they have a proven track record of providing quality inventory that delivers performance for advertisers. | Non-breaking change, with the new `MarketType` property that you can set to `MARKETPLACE` at the ad group level. | Sellers and Publishers 500+ marketplace |
| Bulk operations | With the GraphQL API, you can now export, create, or update multiple ad groups, campaigns, campaign sets, and campaign flights with a single request without throttling. | Additive, non-breaking change. | GraphQL API bulk operations |
| Custom queries | The GraphQL API enables you to construct and execute queries by specifying fields across multiple entities. This flexibility empowers you to precisely define the data structure you need, ensuring that you only retrieve the desired information. | Additive, non-breaking change. | GraphQL API queries Examples: - Advertiser - Campaign - Ad group |
| My Reports | We have introduced new templates and improved reporting to reduce the time it takes to generate reports. In addition, you can now generate these reports from specific tiles in the UI. | Non-breaking change. | N/A |
| Key metric metadata | We've introduced a number of new optional properties, such as `projectedSpend`, `relevance`, and `confidence`, that you can use in your queries to understand the potential implications of your decisions. | Additive, non-breaking change. | Query examples: - Campaign - Ad group |

For more details and FAQs, see Introducing Kokai and the respective pages listed in the preceding table.

#### Recommended actions

Here's what you need to know and do to get started with Kokai:

- Updates to campaign and ad group budgets include breaking changes. For more information, see Budget allocation updates.
- All other updates are backward compatible, contain no breaking changes, and serve as enhancements that enable you to take advantage of Kokai without making immediate updates to your current workflows.
- To ensure your workflows are running smoothly before implementing any changes in production, be sure to test and verify your workflows in our new Partner Sandbox at `https://ext-api.sb.thetradedesk.com/v3`.

  - This sandbox has the same data and users as our production environment and is wiped clean weekly. This allows you to experiment freely, knowing that your production data will be fully restored the following week.
  - To access this sandbox environment, you can use your production Public API keys.
  - No need to change anything in your code except the URL to test everything.

- To check if a campaign can take advantage of the Kokai enhancements and to update your workflow accordingly, use the GET /v3/campaign/{campaignId} look up the `Version` property of the campaign. All campaigns created in or upgraded to Kokai are indicated by the `Version` property set to `Kokai`.

#### Coming soon

This is our Open Beta release of Kokai. Stay tuned for more updates and documentation for Koa Optimizations, publisher lists, and other features!

## May 15, 2024

### Live events

To help optimize spending for campaigns with budgets dedicated to live sports and other events, we've launched a new pacing model. For details, see Live event campaigns.

## April 2, 2024

### GraphQL API (alpha)

Introducing a new paradigm of sending and receiving data in Kokai—GraphQL API. Follow object relationships, request explicit fields, perform bulk operations, and reduce round trips to the network with the new API. GraphQL offers you a single endpoint to call for all data needed in one request.

> **NOTE**: GraphQL API is currently in its early-access alpha release with limited features. It's not a replacement for our REST API but rather an augmentative feature within the Platform API infrastructure.

For details, see Platform API: REST and GraphQL.

## March 19, 2024

### Industry category taxonomy migration update

As we continue our migration of industry categories from IAB 1.0 Content Taxonomy to IAB 2.2 Content Taxonomy, starting **March 19, 2024**, all responses to the following calls will automatically return a list of category mappings in the `AdvertiserCategory` and `AdGroupCategory` properties, respectively.

- POST, PUT, and GET advertiser endpoints
- POST, PUT, and GET ad group endpoints
- Advertiser and ad group overview and bulk-editing endpoints

For details, see New properties in advertiser and ad group endpoint and Update advertiser and ad group workflows.

## March 18, 2024

### Video playback type value update

To align with the evolving landscape of video content and provide much-needed clarity for both the sell side and buy side, the IAB Tech Lab is planning to deprecate the `video.placement` field. Instead, it will use only the `video.plcmt` field, which better differentiates between in-stream and out-stream inventory and reflects more accurately the different levels of user engagement provided by various video placements. For details, see March 2023 Update To OpenRTB Is Now Ready For Implementation!

As a result, we'll be deprecating the `InBanner`, `InArticle`, `InFeed`, and `Outstream` values in the `VideoPlaybackType` property in the ad group, and replace them with the new `AccompanyingContent` and `Standalone` values.

Here's what you need to know and do going forward.

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Starting **September 30, 2024**, we'll no longer accept the `InBanner`, `InArticle`, `InFeed`, and `Outstream` values in the `VideoPlaybackType` property and will return a 400 (Bad Request) error. |
| **Action required** | Update all your ad group workflows to use the new `AccompanyingContent` and `Standalone` values in the `VideoPlaybackType` property by **September 30, 2024**. |

> **NOTE**: Any existing targeting settings with the video playback types will be updated using the bid list endpoints.

## March 5, 2024

### Industry category taxonomy migration deadline update

The deadline announced in the _2023 Release Notes_ for the migration of industry categories from IAB 1.0 Content Taxonomy to IAB 2.2 Content Taxonomy has been extended to **July 1, 2024**, when advertiser entities will be required to declare IAB 2.2 category taxonomy IDs instead of the legacy 1.0 taxonomy IDs. For details on the new endpoints, properties, and required actions, see Industry category taxonomy migration.

## February 5, 2024

### Deprecated creative auditor IDs

Creative approvals are no longer submitted to the following creative auditors:

- Microsoft
- BrightRoll
- Right Media

The `CreativeAuditStatuses` property in the creative endpoints no longer returns creative auditor IDs for these providers.

## January 15, 2024

### Unassociated bid list retention policy update

To optimize and recycle storage for new bid lists, the system now permanently deletes all unused, unassociated bid lists that meet our purging criteria on a monthly basis. For details on the purging criteria, cadence, and required actions, see Unassociated Bid List Retention Policy Update.
