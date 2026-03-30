# Platform API Upgrade Support Archives

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/UpgradeSupportArchives
- Category: Guides

---

# Platform API Upgrade Support Archives

This page provides archived upgrade schedules that document changes to the Platform API over the past two years. See also the archived release notes for the corresponding years.

> **NOTE**: For any upcoming upgrades, see the [Upcoming Changes](/v3/portal/api/doc/UpgradeSupport) page.

## 

October-December 2025[](#Q4-25)

| Effective Date | Product/Feature | Update Type | Details |
| Oct 1, 2025 | GraphQL property | Deprecation | [Ad Group Flight Settings: Property Deprecation](#minimumSpendInAdvertiserCurrency) |
| Oct 3, 2025 | REST endpoints | Deprecation | [Email Notifications for Deprecated REST Endpoints and Properties](#email-notifications) |
| Dec 12, 2025 | Advertiser | New Feature | [Campaign Trading Modes (Closed Beta)](#trading-modes) |

### 

Ad Group Flight Settings: Property Deprecation[](#minimumSpendInAdvertiserCurrency)

##### October 1, 2025

| What you need to know and do |
| **Change Summary** | 

The GraphQL `AdGroupFlight.minimumSpendInAdvertiserCurrency` property, used to set the minimum spend for an ad group flight, has been fully deprecated and replaced with `AdGroupFlight.allocationInAdvertiserCurrency` in ad group workflows.

 |
| **Action Required** | 

Remove the deprecated `AdGroupFlight.minimumSpendInAdvertiserCurrency` property from all ad group mutations and queries and replace it with the new `AdGroupFlight.allocationInAdvertiserCurrency` property.

 |

### 

Email Notifications for Deprecated REST Endpoints and Properties[](#email-notifications)

##### October 3, 2025

| What you need to know and do |
| **Change Summary** | 

Starting **October 3, 2025**, if your integrations currently use deprecated REST endpoints and properties that have a scheduled expiration date, you will receive an email notification that includes the following:

*   A list of up to five endpoints and properties that are scheduled to expire within 180 days. These items are ordered by their potential risk to your integrations.
*   A link to the [API dashboard](/v3/portal/dashboard/api) where you can view the full list of deprecated endpoints and properties along with additional details and guidance.

**IMPORTANT:** After their expiration dates, these endpoints and properties will no longer be available.

 |
| **Action Required** | 

Use the [API dashboard](/v3/portal/dashboard/api) to review the deprecated endpoints and properties listed in the email. If you have questions about the level of impact on your integration or require additional guidance, contact your Technical Account Manager.

 |

### 

Campaign Trading Modes (Closed Beta)[](#trading-modes)

##### December 12, 2025

| What you need to know and do |
| **Change Summary** | 

Starting **December 12, 2025**, The Trade Desk is introducing Trading Modes, a new campaign feature that defines how bidding, pacing, and optimization are managed. You can choose between two modes:

*   **Performance Mode** (recommended): An end-to-end AI powered buying solution that makes it easier to maximize outcomes with minimal campaign management. Automatically applies AI to optimize every decision by selecting the highest-value impressions based on your inputs and goals.
*   **Control Mode**: This mode enables you to manually select and configure each feature and adjust the campaign settings yourself.

**NOTE**: This feature is available to select clients through a closed beta. For details, contact your Technical Account Manager.

 |
| **Action Required** | 

To get started, we recommend creating new campaigns with Performance Mode. For details, see [Trading Modes](/v3/portal/api/doc/TradingModes).

 |

## 

July–September 2025[](#Q3-25)

| Effective Date | Product/Feature | Update Type | Details |
| Jul 7, 2025 | Legacy sandbox | Deprecation | [Legacy External Sandbox Deprecation](#legacy-sandbox) |
| Aug 9, 2025 | Advertiser | Behavior change | [Reclassification of the Shopping Industry Category as Sensitive](#shopping-sensitive-category) |

### 

Legacy External Sandbox Deprecation[](#legacy-sandbox)

| What you need to know and do |
| **Change Summary** | 

As of **July 7, 2025**, we will deprecate our legacy External Sandbox environment (`https://desksb.thetradedesk.com/`). All API traffic directed to the legacy sandbox base URL `https://apisb.thetradedesk.com/v3/` will no longer be supported. This change marks the official sunset of the External Sandbox in favor of our new [Partner Sandbox](/v3/portal/api/doc/PartnerSandbox), which is already available for use.  
**NOTE**: No production data is affected by this change.  
The new Partner Sandbox environment offers major improvements, including the following:

*   Access to Kokai features
*   Improved performance
*   Weekly database refresh from production
*   Ongoing long-term support

 |
| **Action Required** | 

To ensure uninterrupted support for your testing and development workflows, migrate to the new [Partner Sandbox](/v3/portal/api/doc/PartnerSandbox) as soon as possible.

 |

### 

Reclassification of the Shopping Industry Category as Sensitive[](#shopping-sensitive-category)

To classify advertisers and their ad groups by industry, our platform uses the IAB Tech Lab Content Taxonomy [version 2.2](https://iabtechlab.com/wp-content/uploads/2020/12/Implementation_Guide_for_Brand_Suitability_with_IABTechLab_Content_Taxonomy_2-2.pdf). Each advertiser must be assigned an industry category during creation. For details, see [Create Advertisers](/v3/portal/api/doc/AdvertiserCreate).

To improve transparency around which categories require additional attention, we are updating the internal `IsSensitive` flag. This flag identifies specific industry and sub-industry categories as either "sensitive" or "not sensitive" based on company policy. While the flag does not enforce restrictions, it indicates which categories require special handling.

As part of this update, starting **August 9, 2025**, the **Shopping** category will be reclassified from non-sensitive to sensitive. This is due to the addition of a newly designated sensitive subcategory: **Lotteries and Scratch Cards**.

| What you need to know and do |
| **Change Summary** | 

*   Advertisers in the **Shopping** category must now include a valid subcategory when created or edited.
*   Attempts to create or edit advertisers in this category without specifying a subcategory will result in an error.
*   Existing advertisers that are not modified will not be affected.

 |
| **Action Required** | 

Update your integration to specify a valid subcategory when creating or editing advertisers in the **Shopping** industry. Be sure to complete this update as soon as possible—and no later than **August 9, 2025**. If you have any questions, contact your Technical Account Manager.

 |

## 

April–June 2025[](#Q2-25)

| Effective Date | Product/Feature | Update Type | Details |
| Apr 28, 2025 | Advertisers | Property deprecation | [Advertiser Settings: AudienceBoosterEnabled Property Deprecation](#audience-booster) |
| Jun 15, 2025 | Campaigns | Property deprecation | [Campaign Pacing Settings: IsValuePacing Property Deprecation](#isvaluepacing) |
| Jun 30, 2025 | Bid lists | Behavior change | [Bid Lists: Update to Direct Publisher Integration Management](#supply-vendor) |

### 

Advertiser Settings: AudienceBoosterEnabled Property Deprecation[](#audience-booster)

| What you need to know and do |
| **Change Summary** | 

Starting **November 13, 2024**, the `AdvertiserAudienceSettings.AudienceBoosterEnabled` property, which allows you to configure ad group data settings at the advertiser level, will be disregarded in advertiser workflows. This property will be fully deprecated on **April 28, 2025**.

 |
| **Action Required** | 

To enable the platform to add highly relevant segments to your audience when there is confidence they will improve your targeting and boost performance, continue using the `RTBAttributes.AudienceTargeting.AudienceBoosterEnabled` property in the [ad group](/v3/portal/api/area/Ad%20Group) workflows. Remove the deprecated `AdvertiserAudienceSettings.AudienceBoosterEnabled` property from your [advertiser](/v3/portal/api/area/Advertiser) workflows by **April 28, 2025**.

 |

### 

Campaign Pacing Settings: IsValuePacing Property Deprecation[](#isvaluepacing)

| What you need to know and do |
| **Change Summary** | 

As of March 26, 2025, the GraphQL `CampaignPacingSettings.isValuePacing` property returns null in all campaign mutations and queries, regardless of its original value. This property is scheduled for full deprecation in the GraphQL schema on **June 15, 2025**.

 |
| **Action Required** | 

Remove the deprecated GraphQL `CampaignPacingSettings.isValuePacing` property from all campaign mutations and queries by **June 15, 2025**.

 |

### 

Bid Lists: Update to Direct Publisher Integration Management[](#supply-vendor)

| What you need to know and do |
| **Change Summary** | 

As of **June 30, 2025**, direct publisher integrations (OpenPath) will no longer be managed using the `SupplyVendorId` field. As a result, attempts to use the bid list APIs (REST and GraphQL) to manage direct publisher connections through supply vendor bid lists will return an error. The following actions are no longer supported:

*   Adding direct publisher connections
*   Excluding direct publisher connections
*   Adding or modifying bid factors for direct publisher connections
*   Retrieving direct publisher connections

**NOTE**: This change affects only direct publisher integrations. For managing supply vendor or reseller relationships, integrations using the `SupplyVendorId` field remain unchanged.

 |
| **Action Required** | 

Review your current bid list workflows to ensure that they do not rely on the `SupplyVendorId` field to manage your direct publisher connections (OpenPath). To manage direct publisher inventory, use publisher lists or site lists instead. If you need help transitioning or have advanced supply chain requirements, contact your Technical Account Manager.

 |

## 

January–March 2025[](#Q1-25)

| Effective Date | Product/Feature | Update Type | Details |
| Jan 7, 2025 | Private Contracts | Property update | [Private Contracts as Part of Upfront Agreements](#upfronts) |
| Mar 31, 2025 | Campaigns | New requirement | [Campaign Version Check Requirement](#version-check) |

### 

Private Contracts as Part of Upfront Agreements[](#upfronts)

| What you need to know and do |
| **Change Summary** | 

Starting **January 7, 2025**, the currently optional (`IsUpfront`) field will be required when creating or updating private contracts to indicate whether that the contract is part of an upfront agreement.

 |
| **Action Required** | 

Update your [contract](/v3/portal/api/area/Contract) workflows to include the `IsUpfront` property by **January 7, 2025**.

 |

### 

Campaign Version Check Requirement[](#version-check)

| What you need to know and do |
| **Change Summary** | 

Starting **March 31, 2025**, new features and updates will be available and function correctly only for specific campaign versions defined by the Version property. For example, to set the budget properly, you must know which version of the campaign you are manipulating, as Solimar and Kokai workflows differ.

 |
| **Action Required** | 

Your code must check the campaign version and conditionally use features supported by that version when updating your campaign and related workflows. All REST endpoints are marked with compatibility labels, and the appropriate campaign version is provided in all user guides, giving you everything you need to do this work.  
To verify if the campaign `Version` property is set to `Kokai`, use the [GET /v3/campaign/{campaignId}](/v3/portal/api/ref/get-campaign-campaignid) endpoint. See also [Campaign Upgrade Process](/v3/portal/api/doc/KokaiCampaignUpgrade#upgrade).

 |

## 

October–December 2024[](#Q4-24)

| Effective Date | Product/Feature | Update Type | Details |
| Oct 1, 2024 | Ad Groups | `ChannelId` property updates | [Ad Group Channel Selection Updates](#adgroup-channel) |
| Oct 29, 2024 | Audiences | Updates to existing functionality | [Third-Party Data ID Validation for Bidding Eligibility](#third-pd-validation) |

### 

Ad Group Channel Selection Updates[](#adgroup-channel)

| What you need to know and do |
| **Change Summary** | 

Starting **October 1, 2024**, the `ChannelId` property will be required for all ad group workflows in Kokai, with the following supported values: `Display`, `Video`, `Audio`, `NativeDisplay`, `NativeVideo`, `TV`, `OutOfHome`. In Kokai, the ad group channel will be used to inform bidding behavior and provide recommendations and insights. For example, if you choose `Display`, we'll buy only display content for that ad group. If you choose `TV` for an ad group targeting display inventory, we won't bid. Here's what it means for your integration:

*   The ad group creative type must match the channel.
*   You cannot update the ad group channel after the flight starts.
*   Any deprecated values (`Other`, `Mixed`, `Native`, `TVPersonal`) included in create and update requests will result in a 400 (Bad Request) error.
*   If a Solimar ad group with its channel set to `Mixed` is upgraded to Kokai, channel filtering will be ignored.
*   `Mixed` will no longer be accepted as a `ChannelId` property value when cloning campaigns.

For details, see [Channels](/v3/portal/api/doc/Channel).

 |
| **Action Required** | 

*   Update all your ad group workflows to include the required `ChannelId` property and its updated values by **October 1, 2024**.
*   When cloning campaigns, update any ad groups with the `ChannelId` property set to `Mixed` to the appropriate value supported in Kokai.

 |

### 

Third-Party Data ID Validation for Bidding Eligibility[](#third-pd-validation)

| What you need to know and do |
| **Change Summary** | 

Starting **October 29, 2024**, all third-party data IDs in segments will be validated to check if they are biddable. [Data group](/v3/portal/api/area/Data%20Group) workflows will fail when non-biddable third-party data IDs are included in the `ThirdPartyDataIds` array.

 |
| **Action Required** | 

Start using the [POST /v3/dmp/thirdparty/advertiser](/v3/portal/api/ref/post-dmp-thirdparty-advertiser) endpoint to check if segments are buyable beforehand, then remove all third-party data IDs that are not listed from your POST and PUT data group workflows.

 |

## 

July–September 2024[](#Q3-24)

| Effective Date | Area | Update Type | Details |
| Jul. 1, 2024 | Advertiser  
Ad group | Upgrade to new taxonomy version | [Industry Category Taxonomy Migration](/v3/portal/api/doc/UpgradeSupportCategoryTaxonomy) |
| Jul. 1, 2024 | Campaigns | New functionality | [Live Event Campaigns](/v3/portal/api/doc/CampaignLiveEvents) |
| Sep. 30, 2024 | Ad group | Property value update | [Video Playback Type Value Update](#playback-values) |
| Sep. 30, 2024 | CRM Data | Property deprecation | [RetentionEnabled Property Deprecation](#crm-data-retention) |
| Sep. 30, 2024 | Contextual and other categories | Oracle pre- and post-bid product deprecation | [Grapeshot and Moat Deprecation by Oracle](#oracle) |
| Sep. 30, 2024 | Cross-Device | Adbrain Household Graph selection | [Household Graph Selection Updates](#adbrain) |

### 

Video Playback Type Value Update[](#playback-values)

| What you need to know and do |
| **Change Summary** | 

Starting **September 30, 2024**, we'll no longer accept the `InBanner`, `InArticle`, `InFeed`, and `Outstream` values in the `VideoPlaybackType` property in the [ad group](/v3/portal/api/area/Ad%20Group) endpoints and will return a 400 (Bad Request) error.

 |
| **Action Required** | 

Update all your ad group workflows to use the new `AccompanyingContent` and `Standalone` values in the `VideoPlaybackType` property by **September 30, 2024**.

 |

To align with the evolving landscape of video content and provide much-needed clarity for both the sell side and buy side, the IAB Tech Lab is planning to deprecate the `video.placement` field. Instead, it will use only the `video.plcmt` field, which better differentiates between in-stream and out-stream inventory and reflects more accurately the different levels of user engagement provided by various video placements. For details, see [March 2023 Update To OpenRTB Is Now Ready For Implementation!](https://iabtechlab.com/march-2023-update-to-openrtb-is-now-ready-for-implementation/)

> **NOTE**: Any existing targeting settings with the video playback types will be updated using the [bid list endpoints](/v3/portal/api/area/Bid%20List).

### 

RetentionEnabled Property Deprecation[](#crm-data-retention)

| What you need to know and do |
| **Change Summary** | 

Starting **September 30, 2024**, the `RetentionEnabled` field will be removed from the [POST /v3/crmdata/{segmentType}/segment/{advertiserId}/{crmDataId}](/v3/portal/api/ref/post-crmdata-segmenttype-segment-advertiserid-crmdataid) and [POST /v3/crmdata/segment/{advertiserId}/{crmDataId}](/v3/portal/api/ref/post-crmdata-segment-advertiserid-crmdataid) endpoints. By default, all targeting segments will retain hashed email addresses and phone numbers for 90 days to refresh UIDs daily.  
**NOTE**: Update (March 2025): The retention period is now 180 days. This upgrade note reflects the policy at the time of release.

 |
| **Action Required** | 

Update your workflows to remove the deprecated field by **September 30, 2024**.

 |

### 

Grapeshot and Moat Deprecation by Oracle[](#oracle)

| What you need to know and do |
| **Change Summary** | 

As Oracle Advertising is sunsetting their pre- and post-bid products, Grapeshot and Moat, any targeting strategies that depend on these Oracle products will not function after **September 30, 2024**. All workflows using Moat Reporting will be automatically migrated to our new white-labeled product unless you choose to opt out.

 |
| **Action Required** | 

Choose an alternative product as _soon as possible_.

*   For Grapeshot standard and custom contextual categories, we recommend considering The Trade Desk [contextual categories](/v3/portal/api/doc/ContextualCategories).
*   For other Oracle features—such as Grapeshot Content Affinity, Grapeshot Predicts, Moat Viewability, Grapeshot Language, Grapeshot Brand Safety, and Moat Invalid Traffic—contact your Account Manager for guidance on alternative solutions.
*   If you prefer to use an alternate provider for Moat Reporting, request the necessary form from your Account Manager and opt out of the default migration by **September 23, 2024**. Be sure to update your advertiser or partner settings with the new provider by **September 30, 2024**.

 |

### 

Household Graph Selection Changes[](#adbrain)

| What you need to know and do |
| **Change Summary** | 

We are removing Adbrain Household as a selection for our API users. Starting **September 30, 2024**, we'll automatically redirect all API calls with Adbrain Household (Cross-Device Vendor ID `8`) to Identity Alliance Household (Cross-Device Vendor ID `11`).

 |
| **Action Required** | 

Update all your campaigns and ad group workflows currently leveraging Adbrain Household (Cross-Device Vendor ID `8`) to use the Identity Alliance Household Graph (Cross-Device Vendor ID `11`).

 |

## 

April–June 2024[](#Q2-24)

| Area | Update Guidelines | Update Type | Description | Effective Date |
| Kokai (Open Beta) | N/A | New platform experience | For details and guides, see [Release Notes](/v3/portal/api/doc/ReleaseNotes#december-1-2023) for May 28, 2024. | May 28, 2024 |
| Campaigns | N/A | New functionality | To help optimize spending for campaigns with budgets dedicated to live sports and other events, we've launched a new pacing model. For details, see [Live Event Campaigns](/v3/portal/api/doc/CampaignLiveEvents). | June 15, 2024 (trial inventory access) |
| Ad group | N/A | Property deprecation | The `PacingEnabled` property in the [ad group](/v3/portal/api/area/Ad%20Group) endpoints, which used to define the rate at which an ad group spends the allotted budget, will be _fully_ deprecated. For details on required actions and impact on your integration, see [Release Notes](/v3/portal/api/doc/ReleaseNotes#december-1-2023) for December 1, 2023. | June 25, 2024 |

## 

January–March 2024[](#Q1-24)

| Area | Update Guidelines | Update Type | Description | Effective Date |
| Bid Lists | [Unassociated Bid List Retention Policy Update](#retention-policy) | Retention policy change | To optimize and recycle storage for new bid lists, the system will permanently delete all unused, unassociated bid lists that meet our purging criteria on a monthly basis. | Jan 15, 2024 |
| Creatives | N/A | Property value deprecation | With creative approvals no longer submitted to Microsoft, BrightRoll, and Right Media. The `CreativeAuditStatuses` property in the [creative endpoints](/v3/portal/api/area/Creative) will stop returning creative auditor IDs for these providers.  
**IMPORTANT**: Verify your creative approval API workflows to ensure that they do not rely on the deprecated creative auditor type values: `Microsoft`, `BrightRoll`, and `RightMedia`. | Feb 5, 2024 |
| Advertiser | [New Advertiser Properties: Digital Services Act](#dsa) | New properties | If you are targeting anyone in the EU, review your advertiser properties and update your workflows to include the following new DSA properties: `AdvertiserNameDsa` and `PayerNameDsa`.  
**IMPORTANT**: It is your responsibility, as required under our Master Services Agreement, to ensure any information you provide to us is truthful and correct. If you fail to confirm the values, you agree to us using the default values. | Feb 17, 2024 |
| Ad group settings | N/A | Default value change | The Predictive Clearing and Cross Device default values will change during ad group creation. For details, required actions, and impact on your integration, see [Release Notes](/v3/portal/api/doc/ReleaseNotes#september-20-2023) for September 20, 2023. | Mar 15, 2024 |
| Advertiser-level Audience Settings | N/A | New endpoint | To achieve parity with the platform UI functionality, a new Audience Settings endpoint will allow you to set the default values for the `AudienceBoosterEnabled` and `AudienceExcluderEnabled` properties at ad group creation. The Audience Settings automatically modify your audience when it is likely to benefit your campaign. For details, required actions, and impact on your integration, see [Release Notes](/v3/portal/api/doc/ReleaseNotes#september-20-2023) for September 20, 2023. | Mar 15, 2024 |