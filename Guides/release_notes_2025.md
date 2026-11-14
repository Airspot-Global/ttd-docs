# 2025 Advertiser release notes

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserNews/news/doc/ReleaseNotes2025
- Retrieved: 2026-11-14
- Category: Guides

---

# 2025 Advertiser release notes

These release notes list all new features and updates that have been made to the Platform API in 2025. For announcements of new features and updates to the platform user interface (UI), see Knowledge Portal Release Notes. See also Upcoming changes and schedules.

### Campaign Trading Modes (closed beta)

##### December 12, 2025

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Starting **December 12, 2025**, The Trade Desk is introducing Trading Modes, a new campaign feature that defines how bidding, pacing, and optimization are managed. You can choose between two modes: - **Performance Mode** (recommended): An end-to-end AI powered buying solution that makes it easier to maximize outcomes with minimal campaign management. Automatically applies AI to optimize every decision by selecting the highest-value impressions based on your inputs and goals. - **Control Mode**: This mode enables you to manually select and configure each feature and adjust the campaign settings yourself. **NOTE**: This feature is available to select clients through a closed beta. For details, contact your Technical Account Manager. |
| **Action required** | To get started, we recommend creating new campaigns with Performance Mode. |

## Email notifications for deprecated REST endpoints and properties

##### October 3, 2025

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Starting **October 3, 2025**, if your integrations currently use deprecated REST endpoints and properties that have a scheduled expiration date, you will receive an email notification that includes the following: - A list of up to five endpoints and properties that are scheduled to expire within 180 days. These items are ordered by their potential risk to your integrations. - A link to the API dashboard where you can view the full list of deprecated endpoints and properties along with additional details and guidance. **IMPORTANT:** After their expiration dates, these endpoints and properties will no longer be available. |
| **Action required** | Use the API dashboard to review the deprecated endpoints and properties listed in the email. If you have questions about the level of impact on your integration or require additional guidance, contact your Technical Account Manager. |

## Ad group flight settings: Property deprecation

##### October 1, 2025

| What you need to know and do |  |
| --- | --- |
| **Change summary** | The GraphQL `AdGroupFlight.minimumSpendInAdvertiserCurrency` property, used to set the minimum spend for an ad group flight, has been fully deprecated and replaced with `AdGroupFlight.allocationInAdvertiserCurrency` in ad group workflows. |
| **Action required** | Remove the deprecated `AdGroupFlight.minimumSpendInAdvertiserCurrency` property from all ad group mutations and queries and replace it with the new `AdGroupFlight.allocationInAdvertiserCurrency` property. |

## Impression budgets: Upgraded pacing and prioritization

##### September 2, 2025

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Starting **September 2, 2025**, all newly created or upgraded Kokai campaigns with impression budgets will automatically use upgraded pacing that offers more control over average CPMs and waterfall-style budget allocation based on ad group priority. **NOTE**: This change does not affect existing campaigns or Kokai campaigns created by cloning an existing one. |
| **Action required** | No action is required. |

## Polygon-shaped geofence targeting

##### August 26, 2025

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Advertisers can now create polygon geofence segments to target custom-shaped areas with greater precision. Unlike standard circular or ZIP code-based targeting, polygon geofence segments enable you to define exact boundaries around locations such as malls, stadiums, or campuses. For details, see Geofence targeting. |
| **Action required** | No action is required. |

## Reclassification of the shopping industry category as sensitive

##### August 9, 2025

To classify advertisers and their ad groups by industry, our platform uses the IAB Tech Lab Content Taxonomy version 2.2. Each advertiser must be assigned an industry category during creation. For details, see Create advertisers.

To improve transparency around which categories require additional attention, we are updating the internal `IsSensitive` flag. This flag identifies specific industry and sub-industry categories as either "sensitive" or "not sensitive" based on company policy. While the flag does not enforce restrictions, it indicates which categories require special handling.

As part of this update, starting **August 9, 2025**, the **Shopping** category has been reclassified from non-sensitive to sensitive. This is due to the addition of a newly designated sensitive subcategory: **Lotteries and Scratch Cards**.

| What you need to know and do |  |
| --- | --- |
| **Change summary** | - Advertisers in the **Shopping** category must now include a valid subcategory when created or edited. - Attempts to create or edit advertisers in this category without specifying a subcategory will result in an error. - Existing advertisers that are not modified will not be affected. |
| **Action required** | Update your integration to specify a valid subcategory when creating or editing advertisers in the **Shopping** industry. Be sure to complete this update as soon as possible. If you have any questions, contact your Technical Account Manager. |

## Creative weights

##### July 28, 2025

| What you need to know and do |  |
| --- | --- |
| **Change summary** | For better control over which creatives are shown more frequently in an ad group, you can now adjust their creative weights—either manually or automatically. This helps you manage impression delivery across creatives without restructuring campaigns or splitting them into multiple ad groups. For details, see Creative weights. |
| **Action required** | No action is required. |

## Legacy external sandbox deprecation

##### July 7, 2025

| What you need to know and do |  |
| --- | --- |
| **Change summary** | On **July 7, 2025**, we deprecated our legacy External Sandbox environment (`https://desksb.thetradedesk.com/`). All API traffic directed to the legacy sandbox base URL `https://apisb.thetradedesk.com/v3/` is no longer supported. This change marks the official sunset of the External Sandbox in favor of our new Partner Sandbox. **NOTE**: No production data is affected by this change. The new Partner Sandbox environment offers major improvements, including the following: - Access to Kokai features - Improved performance - Weekly database refresh from production - Ongoing long-term support |
| **Action required** | To ensure uninterrupted support for your testing and development workflows, migrate to the new Partner Sandbox as soon as possible. |

## Bid lists: Update to direct publisher integration management

##### June 30, 2025

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Starting **June 30, 2025**, direct publisher integrations (OpenPath) will no longer be managed using the `SupplyVendorId` field. As a result, attempts to use the bid list APIs (REST and GraphQL) to manage direct publisher connections through supply vendor bid lists will return an error. The following actions are no longer supported: - Adding direct publisher connections - Excluding direct publisher connections - Adding or modifying bid factors for direct publisher connections - Retrieving direct publisher connections **NOTE**: This change affects only direct publisher integrations. For managing supply vendor or reseller relationships, integrations using the `SupplyVendorId` field remain unchanged. |
| **Action required** | Review your current bid list workflows to ensure that they do not rely on the `SupplyVendorId` field to manage your direct publisher connections (OpenPath). To manage direct publisher inventory, use publisher lists or site lists instead. If you need help transitioning or have advanced supply chain requirements, contact your Technical Account Manager. |

## Campaign pacing settings: IsValuePacing property deprecation

##### June 15, 2025

| What you need to know and do |  |
| --- | --- |
| **Change summary** | The GraphQL `CampaignPacingSettings.isValuePacing` property is now fully deprecated. |
| **Action required** | Remove the deprecated GraphQL `CampaignPacingSettings.isValuePacing` property from all campaign mutations as soon as possible. |

## General reporting settings: base bid property deprecation

##### June 9, 2025

| What you need to know and do |  |
| --- | --- |
| **Change summary** | The `baseBid` GraphQL query and mutation field, which determines the average starting price paid for an impression before any bid factors are applied, was deprecated for advertisers, campaigns, and ad groups. If you include this field in your workflows, it will not return an error, but it also won't return any meaningful data. |
| **Action required** | To set the average starting price for impressions, use the `adgroup.baseBidCPMInAdvertiserCurrency` field in your queries and mutations. Remove the `baseBid` field from your Budget allocation workflows. |

## Bulk operations: Mutations

##### May 30, 2025

Bulk mutation operations now provide a more efficient way to submit large-scale updates in a single asynchronous request. Instead of manually iterating over individual mutation calls, you can include multiple large input objects in one request—simplifying and accelerating the update process.

For details, see GraphQL bulk operations.

## Choose paths in Blue Lists

##### May 30, 2025

After creating a Blue List, an inventory management tool, you can now customize it by disabling automatic optimizations and setting supply path preferences for each publisher. Download an Excel file to choose path modes and resellers for each publisher. For details, see Supply path preferences.

To access this feature, contact your Technical Account Manager.

## Budget allocation settings: Allocation type

##### May 22, 2025

To give you more control and flexibility in managing campaign budgets, we've introduced a new GraphQL field: `allocationType`. This field enables you to define each ad group's budget allocation as either `FIXED` or `MINIMUM`, which determines how the platform allocates your overall campaign flight budget. You can also mix the two types within the same flight—reserving strict spend amounts for some ad groups while allowing optimization for others with unallocated budget.

For use case examples, FAQs, and other details, see Budget allocation.

## Ad group settings: campaign stack rank property deprecation

##### May 22, 2025

| What you need to know and do |  |
| --- | --- |
| **Change summary** | The GraphQL `adGroup.campaignStackRank` query field, which determines how the remaining budget is weighted across ad groups after assigned allocations are met, typically in partially fluid budgets, was fully deprecated on **May 15, 2025**. |
| **Action required** | To view how the remaining budget is weighted across ad groups, include the GraphQL `adGroup.budget.spendPriority` query field. Remove the deprecated `adGroup.campaignStackRank` field from your Budget allocation workflows by **November 15, 2025**. |

## Advertiser settings: AudienceBoosterEnabled property deprecation

##### April 28, 2025

| What you need to know and do |  |
| --- | --- |
| **Change summary** | The `AdvertiserAudienceSettings.AudienceBoosterEnabled` property, which allows you to configure ad group data settings at the advertiser level, was fully deprecated on **April 28, 2025**. |
| **Action required** | To enable the platform to add highly relevant segments to your audience when there is confidence they will improve your targeting and boost performance, continue using the `RTBAttributes.AudienceTargeting.AudienceBoosterEnabled` property in the ad group workflows. Remove the deprecated `AdvertiserAudienceSettings.AudienceBoosterEnabled` property from your advertiser workflows by **April 28, 2025**. |

## Use REST for budget allocation in Kokai—no code updates required

##### April 4, 2025

| What you need to know and do |  |
| --- | --- |
| **Change summary** | You can now transition to Kokai and continue using REST alongside GraphQL to create and manage Kokai campaigns and their budgets. Additionally, the new optional read-only `AllocationType` property helps distinguish between maximum- and minimum-based ad group budget allocation, ensuring backward compatibility with Solimar. |
| **Action required** | No code changes are required for your existing REST and GraphQL campaign or ad group workflows—you can continue using them as is. Our Budget allocation (Kokai) and other related articles are being updated. For details and FAQs on the `AllocationType` property, see REST API: Ad group budget allocation for Kokai campaigns. |

## Advertiser consent for sharing partner costs with retailers

##### April 1, 2025

To help retailers understand how much of your spend is tied to impressions that use their audience data, you can now share monthly reports of the partner costs with them. This visibility allows retailers to better assess your progress toward meeting commitments and confirm when those commitments have been fulfilled.

## New reporting field for enhanced performance tracking

##### February 25, 2025

To help you track key performance metrics like costs, bidding, and media quality, we've added a new `reporting` field to the advertiser, campaign, and ad group GraphQL queries. Retrieve lifetime data or break it down by day or hour to analyze trends, optimize bids, and measure engagement. Available at the advertiser, campaign, and ad group levels, this field enables you to evaluate media efficiency and refine bidding strategies with data-driven insights.

## Private contracts as part of upfront agreements

##### January 7, 2025

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Starting **January 7, 2025**, the currently optional (`IsUpfront`) field will be required when creating or updating private contracts to indicate whether that the contract is part of an upfront agreement. |
| **Action required** | Update your contract workflows to include the `IsUpfront` property. |

## Country code requirement for advertisers

##### January 1, 2025

| What you need to know and do |  |
| --- | --- |
| **Change summary** | Starting **January 1, 2025**, all advertisers must have the country code of the country in which they are advertising. The country code determines the relevant policies and regulations to be applied to the advertiser. |
| **Action required** | When creating an advertiser in the platform, set the `Country` property by using the POST /v3/advertiser endpoint. For details, see Create an advertiser. For existing advertisers, no action is required. If they are missing their country code, The Trade Desk will automatically set it for them. |
