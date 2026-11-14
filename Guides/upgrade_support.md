# Platform API Upgrade Support Archives

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserNews/news/doc/UpgradeSupportArchives
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/doc/UpgradeSupportArchives (retired)
- Retrieved: 2026-11-14
- Category: Guides

---

# Archived API changes for advertisers

This page provides archived upgrade schedules that document changes to The Trade Desk APIs for advertisers over the past two years. See also the archived release notes for the corresponding years.

> **NOTE**: For any upcoming upgrades, see the Upcoming API changes for advertisers page.

## July-September 2026

| Effective Date | Product/Feature | Update Type | Details |
| --- | --- | --- | --- |
| Jul 1, 2026 | Bid lists | Field deprecation | Adbug page quality fields deprecation |
| Jul 13, 2026 | Bid lists | Field update | Impression placement ID update |
| Aug 3, 2026 | Campaigns | Field deprecation | Enabled value-added providers field deprecation |
| Sep 30, 2026 | Solimar campaigns | Documentation archived | Solimar campaigns |
| Sep 30, 2026 | Solimar campaign budget allocation | Documentation archived | Solimar campaign budget allocation |

### Adbug page quality fields deprecation

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **July 1, 2026**, The Trade Desk will deprecate Adbug page quality bid list fields. Adbug is a China-specific fraud verification vendor that's no longer operational and is not supported in Kokai. The following **GraphQL** fields will be removed: - `/BidLine/adBugPageQualityCategory` - `/BidLine/adBugVideoPageQualityCategory` - `/BidListDimension/HAS_AD_BUG_PAGE_QUALITY_CATEGORY_ID` The following **REST** properties will be removed: - `AdBugPageQualityCategoryId` - `AdBugVideoPageQualityCategoryId` Requests that include these fields after this date will return an error. |
| **Action required** | Update your bid list workflows to remove the deprecated fields from `BidLines` objects by **July 1, 2026**. For details, contact your Technical Account Manager. |

### Impression placement ID update

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Effective **July 13, 2026**, `ImpressionPlacementId` values in bid lists will be updated to exactly match values provided by the publishers. The Trade Desk will no longer apply custom updates to these IDs. For example, most placement prefixes will be restored, and some generic values will change to publisher-specific paths with unique site IDs. |
| **Action required** | Review the `ImpressionPlacementId` entries in your target or optimized lists and update any affected values. If you need help identifying affected values or confirming updates, contact your Technical Account Manager. For example, you can request a list of affected values and their updated equivalents. Your Technical Account Manager will also proactively reach out if your account is affected. |

### Enabled value-added providers property deprecation

##### August 3, 2026

| What you need to know and do |  |
| --- | --- |
| **Change Summary** | Effective **August 3, 2026**, as part of The Trade Desk's broad shift to ID-based fields, the `EnabledValueAddedProviders` field for campaigns and ad groups will be fully deprecated and replaced with the `EnabledValueAddedProviderIds` field. Instead of an array of provider name strings, the new field accepts an array of provider ID integers. Using the `EnabledValueAddedProviders` field will return errors. |
| **Action Required** | Update your integration to use the `EnabledValueAddedProviderIds` field. |

## October-December 2025

| Effective Date | Product/Feature | Update Type | Details |
| --- | --- | --- | --- |
| Oct 1, 2025 | GraphQL property | Deprecation | Ad group flight settings: Property deprecation |
| Oct 3, 2025 | REST endpoints | Deprecation | Email notifications for deprecated REST endpoints and properties |
| Dec 12, 2025 | Advertiser | New Feature | Campaign Trading Modes (closed beta) |

### Ad group flight settings: Property deprecation

##### October 1, 2025

| What you need to know and do |  |
| --- | --- |
| **Change summary** | The GraphQL `AdGroupFlight.minimumSpendInAdvertiserCurrency` property, used to set the minimum spend for an ad group flight, has been fully deprecated and replaced with `AdGroupFlight.allocationInAdvertiserCurrency` in ad group workflows. |
| **Action required** | Remove the deprecated `AdGroupFlight.minimumSpendInAdvertiserCurrency` property from all ad group mutations and queries and replace it with the new `AdGroupFlight.allocationInAdvertiserCurrency` property. |

### Email notifications for deprecated REST endpoints and properties

##### October 3, 2025

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Starting **October 3, 2025**, if your integrations currently use deprecated REST endpoints and properties that have a scheduled expiration date, you will receive an email notification that includes the following: - A list of up to five endpoints and properties that are scheduled to expire within 180 days. These items are ordered by their potential risk to your integrations. - A link to the API dashboard where you can view the full list of deprecated endpoints and properties along with additional details and guidance. **IMPORTANT:** After their expiration dates, these endpoints and properties will no longer be available. |
| **Action required** | Use the API dashboard to review the deprecated endpoints and properties listed in the email. If you have questions about the level of impact on your integration or require additional guidance, contact your Technical Account Manager. |

### Campaign Trading Modes (closed beta)

##### December 12, 2025

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Starting **December 12, 2025**, The Trade Desk is introducing Trading Modes, a new campaign feature that defines how bidding, pacing, and optimization are managed. You can choose between two modes: - **Performance Mode** (recommended): An end-to-end AI powered buying solution that makes it easier to maximize outcomes with minimal campaign management. Automatically applies AI to optimize every decision by selecting the highest-value impressions based on your inputs and goals. - **Control Mode**: This mode enables you to manually select and configure each feature and adjust the campaign settings yourself. **NOTE**: This feature is available to select clients through a closed beta. For details, contact your Technical Account Manager. |
| **Action required** | To get started, we recommend creating new campaigns with Performance Mode. |

## July–September 2025

| Effective Date | Product/Feature | Update Type | Details |
| --- | --- | --- | --- |
| Jul 7, 2025 | Legacy sandbox | Deprecation | Legacy external sandbox deprecation |
| Aug 9, 2025 | Advertiser | Behavior change | Reclassification of the shopping industry category as sensitive |

### Legacy external sandbox deprecation

| What you need to know and do |  |
| --- | --- |
| **Change summary** | As of **July 7, 2025**, we will deprecate our legacy External Sandbox environment (`https://desksb.thetradedesk.com/`). All API traffic directed to the legacy sandbox base URL `https://apisb.thetradedesk.com/v3/` will no longer be supported. This change marks the official sunset of the External Sandbox in favor of our new Partner Sandbox, which is already available for use. **NOTE**: No production data is affected by this change. The new Partner Sandbox environment offers major improvements, including the following: - Access to Kokai features - Improved performance - Weekly database refresh from production - Ongoing long-term support |
| **Action required** | To ensure uninterrupted support for your testing and development workflows, migrate to the new Partner Sandbox as soon as possible. |

### Reclassification of the shopping industry category as sensitive

To classify advertisers and their ad groups by industry, our platform uses the IAB Tech Lab Content Taxonomy version 2.2. Each advertiser must be assigned an industry category during creation. For details, see Create advertisers.

To improve transparency around which categories require additional attention, we are updating the internal `IsSensitive` flag. This flag identifies specific industry and sub-industry categories as either "sensitive" or "not sensitive" based on company policy. While the flag does not enforce restrictions, it indicates which categories require special handling.

As part of this update, starting **August 9, 2025**, the **Shopping** category will be reclassified from non-sensitive to sensitive. This is due to the addition of a newly designated sensitive subcategory: **Lotteries and Scratch Cards**.

| What you need to know and do |  |
| --- | --- |
| **Change summary** | - Advertisers in the **Shopping** category must now include a valid subcategory when created or edited. - Attempts to create or edit advertisers in this category without specifying a subcategory will result in an error. - Existing advertisers that are not modified will not be affected. |
| **Action required** | Update your integration to specify a valid subcategory when creating or editing advertisers in the **Shopping** industry. Be sure to complete this update as soon as possible—and no later than **August 9, 2025**. If you have any questions, contact your Technical Account Manager. |

## April–June 2025

| Effective Date | Product/Feature | Update Type | Details |
| --- | --- | --- | --- |
| Apr 28, 2025 | Advertisers | Property deprecation | Advertiser settings: AudienceBoosterEnabled property deprecation |
| Jun 15, 2025 | Campaigns | Property deprecation | Campaign pacing settings: IsValuePacing property deprecation |
| Jun 30, 2025 | Bid lists | Behavior change | Bid lists: Update to direct publisher integration management |

### Advertiser settings: AudienceBoosterEnabled property deprecation

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Starting **November 13, 2024**, the `AdvertiserAudienceSettings.AudienceBoosterEnabled` property, which allows you to configure ad group data settings at the advertiser level, will be disregarded in advertiser workflows. This property will be fully deprecated on **April 28, 2025**. |
| **Action required** | To enable the platform to add highly relevant segments to your audience when there is confidence they will improve your targeting and boost performance, continue using the `RTBAttributes.AudienceTargeting.AudienceBoosterEnabled` property in the ad group workflows. Remove the deprecated `AdvertiserAudienceSettings.AudienceBoosterEnabled` property from your advertiser workflows by **April 28, 2025**. |

### Campaign pacing settings: IsValuePacing property deprecation

| What you need to know and do |  |
| --- | --- |
| **Change summary** | As of March 26, 2025, the GraphQL `CampaignPacingSettings.isValuePacing` property returns null in all campaign mutations and queries, regardless of its original value. This property is scheduled for full deprecation in the GraphQL schema on **June 15, 2025**. |
| **Action required** | Remove the deprecated GraphQL `CampaignPacingSettings.isValuePacing` property from all campaign mutations and queries by **June 15, 2025**. |

### Bid lists: Update to direct publisher integration management

| What you need to know and do |  |
| --- | --- |
| **Change summary** | As of **June 30, 2025**, direct publisher integrations (OpenPath) will no longer be managed using the `SupplyVendorId` field. As a result, attempts to use the bid list APIs (REST and GraphQL) to manage direct publisher connections through supply vendor bid lists will return an error. The following actions are no longer supported: - Adding direct publisher connections - Excluding direct publisher connections - Adding or modifying bid factors for direct publisher connections - Retrieving direct publisher connections **NOTE**: This change affects only direct publisher integrations. For managing supply vendor or reseller relationships, integrations using the `SupplyVendorId` field remain unchanged. |
| **Action required** | Review your current bid list workflows to ensure that they do not rely on the `SupplyVendorId` field to manage your direct publisher connections (OpenPath). To manage direct publisher inventory, use publisher lists or site lists instead. If you need help transitioning or have advanced supply chain requirements, contact your Technical Account Manager. |

## January–March 2025

| Effective Date | Product/Feature | Update Type | Details |
| --- | --- | --- | --- |
| Jan 7, 2025 | Private Contracts | Property update | Private contracts as part of upfront agreements |
| Mar 31, 2025 | Campaigns | New requirement | Campaign version check requirement |

### Private contracts as part of upfront agreements

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Starting **January 7, 2025**, the currently optional (`IsUpfront`) field will be required when creating or updating private contracts to indicate whether that the contract is part of an upfront agreement. |
| **Action required** | Update your contract workflows to include the `IsUpfront` property by **January 7, 2025**. |

### Campaign version check requirement

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Starting **March 31, 2025**, new features and updates will be available and function correctly only for specific campaign versions defined by the Version property. For example, to set the budget properly, you must know which version of the campaign you are manipulating, as Solimar and Kokai workflows differ. |
| **Action required** | Your code must check the campaign version and conditionally use features supported by that version when updating your campaign and related workflows. All REST endpoints are marked with compatibility labels, and the appropriate campaign version is provided in all user guides, giving you everything you need to do this work. To verify if the campaign `Version` property is set to `Kokai`, use the GET /v3/campaign/{campaignId} endpoint. See also Campaign upgrade process. |

## October–December 2024

| Effective Date | Product/Feature | Update Type | Details |
| --- | --- | --- | --- |
| Oct 1, 2024 | Ad Groups | `ChannelId` property updates | Ad group channel selection updates |
| Oct 29, 2024 | Audiences | Updates to existing functionality | Third-party data ID validation for bidding eligibility |

### Ad group channel selection updates

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Starting **October 1, 2024**, the `ChannelId` property will be required for all ad group workflows in Kokai, with the following supported values: `Display`, `Video`, `Audio`, `NativeDisplay`, `NativeVideo`, `TV`, `OutOfHome`. In Kokai, the ad group channel will be used to inform bidding behavior and provide recommendations and insights. For example, if you choose `Display`, we'll buy only display content for that ad group. If you choose `TV` for an ad group targeting display inventory, we won't bid. Here's what it means for your integration: - The ad group creative type must match the channel. - You cannot update the ad group channel after the flight starts. - Any deprecated values (`Other`, `Mixed`, `Native`, `TVPersonal`) included in create and update requests will result in a 400 (Bad Request) error. - If a Solimar ad group with its channel set to `Mixed` is upgraded to Kokai, channel filtering will be ignored. - `Mixed` will no longer be accepted as a `ChannelId` property value when cloning campaigns. For details, see Channels. |
| **Action required** | - Update all your ad group workflows to include the required `ChannelId` property and its updated values by **October 1, 2024**. - When cloning campaigns, update any ad groups with the `ChannelId` property set to `Mixed` to the appropriate value supported in Kokai. |

### Third-party data ID validation for bidding eligibility

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Starting **October 29, 2024**, all third-party data IDs in segments will be validated to check if they are biddable. Data group workflows will fail when non-biddable third-party data IDs are included in the `ThirdPartyDataIds` array. |
| **Action required** | Start using the POST /v3/dmp/thirdparty/advertiser endpoint to check if segments are buyable beforehand, then remove all third-party data IDs that are not listed from your POST and PUT data group workflows. |

## July–September 2024

| Effective Date | Area | Update Type | Details |
| --- | --- | --- | --- |
| Jul. 1, 2024 | Advertiser Ad group | Upgrade to new taxonomy version | Industry category taxonomy migration |
| Jul. 1, 2024 | Campaigns | New functionality | Live event campaigns |
| Sep. 30, 2024 | Ad group | Property value update | Video playback type value update |
| Sep. 30, 2024 | CRM Data | Property deprecation | RetentionEnabled property deprecation |
| Sep. 30, 2024 | Contextual and other categories | Oracle pre- and post-bid product deprecation | Grapeshot and Moat deprecation by Oracle |
| Sep. 30, 2024 | Cross-Device | Adbrain Household Graph selection | Household graph selection updates |

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
| **Change summary** | Starting **September 30, 2024**, the `RetentionEnabled` field will be removed from the POST /v3/crmdata/{segmentType}/segment/{advertiserId}/{crmDataId} and POST /v3/crmdata/segment/{advertiserId}/{crmDataId} endpoints. By default, all targeting segments will retain hashed email addresses and phone numbers for 90 days to refresh UIDs daily. **NOTE**: Update (March 2025): The retention period is now 180 days. This upgrade note reflects the policy at the time of release. |
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

## April–June 2024

| Area | Update Guidelines | Update Type | Description | Effective Date |
| --- | --- | --- | --- | --- |
| Kokai (Open Beta) | N/A | New platform experience | For details and guides, see Release notes for May 28, 2024. | May 28, 2024 |
| Campaigns | N/A | New functionality | To help optimize spending for campaigns with budgets dedicated to live sports and other events, we've launched a new pacing model. For details, see Live event campaigns. | June 15, 2024 (trial inventory access) |
| Ad group | N/A | Property deprecation | The `PacingEnabled` property in the ad group endpoints, which used to define the rate at which an ad group spends the allotted budget, will be _fully_ deprecated. | June 25, 2024 |

## January–March 2024

| Area | Update Guidelines | Update Type | Description | Effective Date |
| --- | --- | --- | --- | --- |
| Bid Lists | Unassociated Bid List Retention Policy Update | Retention policy change | To optimize and recycle storage for new bid lists, the system will permanently delete all unused, unassociated bid lists that meet our purging criteria on a monthly basis. | Jan 15, 2024 |
| Creatives | N/A | Property value deprecation | With creative approvals no longer submitted to Microsoft, BrightRoll, and Right Media. The `CreativeAuditStatuses` property in the creative endpoints will stop returning creative auditor IDs for these providers. **IMPORTANT**: Verify your creative approval API workflows to ensure that they do not rely on the deprecated creative auditor type values: `Microsoft`, `BrightRoll`, and `RightMedia`. | Feb 5, 2024 |
| Advertiser | New Advertiser Properties: Digital Services Act | New properties | If you are targeting anyone in the EU, review your advertiser properties and update your workflows to include the following new DSA properties: `AdvertiserNameDsa` and `PayerNameDsa`. **IMPORTANT**: It is your responsibility, as required under our Master Services Agreement, to ensure any information you provide to us is truthful and correct. If you fail to confirm the values, you agree to us using the default values. | Feb 17, 2024 |
| Ad group settings | N/A | Default value change | The Predictive Clearing and Cross Device default values will change during ad group creation. | Mar 15, 2024 |
| Advertiser-level Audience Settings | N/A | New endpoint | To achieve parity with the platform UI functionality, a new Audience Settings endpoint will allow you to set the default values for the `AudienceBoosterEnabled` and `AudienceExcluderEnabled` properties at ad group creation. The Audience Settings automatically modify your audience when it is likely to benefit your campaign. | Mar 15, 2024 |
