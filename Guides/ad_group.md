# Ad Group (Solimar)

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/SolimarAdGroup
- Category: Guides

---

# Ad Group (Solimar)

> **IMPORTANT**: This guide is intended for Solimar users. To create or manage ad groups in Kokai, see [Ad Groups](/v3/portal/api/doc/AdGroup).

Ad groups are a container for assembling targeting specifics and strategies. Each campaign may contain multiple ad groups, and each ad group may contain various creative formats and sizes that support the strategy.

## 

Ad Group Elements[](#adgroupelements)

An ad group is made up of multiple elements that you can combine into a cohesive strategy.

### 

Audiences[](#adgroupaudience)

An audience is a container that holds included and excluded groups of data elements that represent specific users or segments of users. These segments are constructed from first-party pixels or third-party segments. For details, see [Audiences](/v3/portal/api/doc/Audience).

### 

Bid Lists[](#adgroupbidlists)

A bid list is a collection of dimensions and bid adjustments to target, block, or optimize against based on impression attributes. For details, see [Bid Lists](/v3/portal/api/doc/BidList). Here's what you need to know about associating bid lists with ad groups:

*   You can associate bid lists with ad groups directly when creating or updating them.
*   You can use the `IncludeDefaultsFromCampaign` property to have bid lists inherited from the parent campaign when creating ad groups. For detail, see [Default Bid Lists](/v3/portal/api/doc/BidListDefault).

### 

Budgets[](#adgroupbudgets)

Each ad group has budget settings. Here's what you need to know:

*   Ad group budgets allow you to break down your campaign budget by strategy.
*   For each ad group, be sure to specify a monetary budget or an impressions budget, which aligns with the campaign budget type.
*   If you are running a flighted campaign, the ad group must specify a budget for each campaign flight using `RTBAttributes.BudgetSettings.AdGroupFlights`.
*   **Flight Budget Exclusivity**: When `RTBAttributes.BudgetSettings.AdGroupFlights` is specified, top-level ad group budget fields (`Budget`, `BudgetInImpressions`, `DailyBudget`, `DailyBudgetInImpressions`, and `AllocationType`) must **not** be included in the request payload. Sending both flight details and top-level budget fields causes TTD to reject the request with `HTTP 400 Bad Request` (`"The request specifies both flight details and at least one of the budget attributes at the ad group budget level, which is not permitted."`).
*   **Deprecated Cross-Device Flags**: Legacy booleans `UseIdentityAlliance` and `AdBrainHouseholdCrossDeviceEnabled` are permanently retired and must be removed from all ad group payloads. Use `RTBAttributes.AudienceTargeting.CrossDeviceVendorListForAudience` instead.
*   If you are running a campaign that automatically allocates its budget, consider setting the ad group budget to be equal to the campaign budget. For details, see [Fluid Budgets for Ad Groups](/v3/portal/api/doc/SolimarCampaignBudget#fluid-budgeting).
*   If you want your ad group to receive a minimum daily spend from a campaign that automatically allocates its budget, set the `MinimumAdGroupSpendInAdvertiserCurrency` value to the amount you want the ad group to receive. For details, see [Minimum Ad Group Budget Spend](/v3/portal/api/doc/SolimarCampaignBudget#minimum-ad-group-budget-spend).

### 

Base and Max Bids[](#adgroupbasebidmaxbid)

Each ad group defines a base and max bids. Here's what you need to know:

*   CPM is used to define base and max bids.
*   The base bid is the starting bid for a single impression before applying bid adjustments specified through private contract settings and bid lists.
*   The max bid should be greater than or equal to the minimum base bid threshold for the partner. The max bid is the highest amount an ad group will bid on a single impression.

### 

Creatives[](#adgroupcreatives)

Here's what you need to know:

*   Ad groups require at least one approved creative to spend. An ad group with no creatives will not spend.
*   Be sure to upload your creatives before creating your ad group. For details, see [Creatives](/v3/portal/api/doc/Creative).

### 

Fee Cards[](#adgroupfees)

You can create fee cards for an ad group by using the [Additional Fees endpoints](/v3/portal/api/area/Additional%20Fees).

### 

Goals and KPIs[](#adgroupgoal)

The return on investment (ROI) goal is how this ad group defines success. Goals are also referred to as key performance indicators (KPIs). Here's what you need to know about them:

*   If you want your ad group to benefit from [Koa features](#ad-group-koa-features), you must add an ROI goal to the ad group.
*   An ad group may have its own goal or inherit them from its parent campaign.
*   A campaign can have up to three goals. In addition to inheriting goals from the parent, the campaign ad groups may also have goals of their own. Ad groups that have different goals than the campaign rely solely on Koa Optimizations to determine how it receives spend. See also [Campaign Budget Allocation](/v3/portal/api/doc/SolimarCampaignBudget).

## 

Recommended Performance-Enhancing Koa Features[](#ad-group-koa-features)

Koa is an AI engine that helps you discover the most efficient way to spend your budgets across channels, audiences, and inventory sources. Koa prioritizes best-performing and most relevant inventory based on your ad group's goals, and makes sure that you pay the right price on impressions. For the supported dimensions, goals, CPM handling, and other details, see [Koa Optimizations](/v3/portal/api/doc/SolimarKoaOptimizations).

The following table lists Koa features that you can turn on. The list indicates the ad group API settings for each feature and provides links to the Knowledge Portal pages and other resources where you can learn more.

Here's what you need to know:

*   To take advantage of the following performance-enhancing features, an [ROI goal](#adgroupgoal) is required for an ad group.
*   In the platform UI, [Prism](/v3/portal/api/doc/Prism), Predictive Clearing, and Cross Device are automatically turned on for all ad groups as part of the advertiser's Prism settings. For details, see [Prism](/v3/portal/api/doc/Prism).
*   In the platform API, to turn on a feature, set the corresponding property value to `true`. For an ad group example with several features turned on, see this [create request](#ad-group-create).
*   By default, the `AudienceExcluderEnabled` property (known as Prism) is enabled at the [advertiser](/v3/portal/api/doc/SolimarAdvertiser) level. To change this, do the following:
    *   For all new ad groups at the advertiser level, use the [advertiser endpoints](/v3/portal/api/area/Advertiser).
    *   For an existing ad group, set the ad group property to `true` or `false` in the request.
*   Some features, like Audience Booster, apply only to ad groups with certain KPIs. Other features are mutually exclusive as noted in the feature and property descriptions.
*   All feature properties, except Predictive Clearing, are part of the `RTBAttributes.AudienceTargeting` object.

| Feature | API Property | RTB Attribute? | Description | Fee-Based? |
| [Predictive Clearing](/v3/portal/api/doc/PredictiveClearing) | `PredictiveClearingEnabled` | No | Predictive Clearing is a cost-saving feature that helps you win more impressions at a lower CPM while optimizing ad spend and improving campaign performance. When you turn on Predictive Clearing, you enable Koa to analyze historical clearing prices to find a lower, optimal bid for each impression served in a first-price auction. | Yes |
| [Identity Alliance](/v3/portal/api/doc/CrossDeviceTargeting) | `CrossDeviceVendorListForAudience`  
Set `CrossDeviceVendorId` to `10` for Identity Alliance (person) or `11` for Identity Alliance (household) | RTB Attribute | Enables Koa to select the right option for a user across all cross-device vendors on an impression-by-impression basis. For details, see [Cross-Device Targeting](/v3/portal/api/doc/CrossDeviceTargeting). | Yes |
| [Prism](/v3/portal/api/doc/Prism) | `AudienceExcluderEnabled` | RTB Attribute | Creates a custom audience for the ad group by excluding data segments that are less relevant to the advertiser's target audience. In other words, this custom audience increases the value of a campaign by focusing on the most valuable impressions and excluding users who are less likely to benefit the campaign. Here's what you need to know about this property:

*   This property cannot be used in conjunction with Audience Predictor or Target Demographic Settings.
*   Advertisers in the following IAB categories may not use this functionality: Personal Finance, Careers, Real Estate.

 | Yes |
| [Audience Predictor](https://desk.thetradedesk.com/knowledge-portal/en/koa-audience-predictor.html) | `AudiencePredictorEnabled` | RTB Attribute | Enables Koa to use lookalike model data to create and continuously update an audience of users who are most likely to convert, and target them in your audience. Here's what you need to know about this functionality:

*   Enabling this functionality generates a custom audience, so you cannot use it in conjunction with Prism, Demographic or Interest Targeting.
*   Advertisers in the following IAB categories cannot use third-party data or custom modeling sources with Audience Predictor: Personal Finance, Careers, Real Estate.

 | Yes |
| [Demographic Targeting](https://desk.thetradedesk.com/knowledge-portal/en/koa-demographic-targeting.html) | `TargetDemographicSettingsEnabled`  
`TargetDemographicSettings` | RTB Attributes | Enables Koa to put together an audience that includes all data segments that align with your chosen age and gender demographics.  
**IMPORTANT**: You cannot use this feature in conjunction with Audience Predictor or Prism. | Yes |
| [Retargeting](https://desk.thetradedesk.com/knowledge-portal/en/koa-retargeting.html) | `AudienceRetargetingEnabled`  
`AudienceRetargetingSettings` | RTB Attributes | For ad groups with CPA as their primary goal, enables Koa to consolidate the retargeting strategy into one ad group and apply unique bids for each user. | No |
| [Interest Targeting](https://desk.thetradedesk.com/knowledge-portal/en/koa-interest-targeting.html) | `TargetInterestSettingsEnabled`  
`TargetInterestSettings` | RTB Attributes | Interest targeting helps you improve behavioral audience targeting while saving time through pre-built audience categories. Koa identifies the most relevant segments based on lookalike modeling and includes them in the audience.  
**IMPORTANT**: You cannot use this feature in conjunction with Audience Predictor or Prism. | Yes |

For an example of an ad group with some of the key performance-enhancing features turned on, see [Request Example](#ad-group-create).

## 

Create an Ad Group[](#createadgroups)

To create an ad group, use the [POST /v3/adgroup](/v3/portal/api/ref/post-adgroup) endpoint with a minimum of the required fields listed in the following table.

> **IMPORTANT**: To prioritize best-performing and most relevant inventory based on your ad group's goals, be sure to turn on the [recommended performance-enhancing settings](#ad-group-koa-features).

| Property Name | Required | Notes |
| `CampaignId` | Required | N/A |
| `AdGroupName` | Required | N/A |
| `AdGroupCategory` | Conditionally Required, Nullable | Required if the advertiser's industry category ID is not set. Here's what you need to know:

*   If set to `null`, defaults to the advertiser's `AdvertiserCategory`.
*   For industry categories, we use the IAB Tech Lab Content Taxonomy [version 2.2](https://iabtechlab.com/wp-content/uploads/2020/12/Implementation_Guide_for_Brand_Suitability_with_IABTechLab_Content_Taxonomy_2-2.pdf).

 |
| `RTBAttributes.BudgetSettings.AdGroupFlights.AdGroupId` | Required, Nullable | The request must include this property. When creating an ad group, set this to `null` because the ad group ID does not exist yet. |
| `RTBAttributes.BudgetSettings.AdGroupFlights.CampaignFlightId` | Required | The identifier of the campaign flight this ad group budget is associated to. You can look it up by using the [GET /v3/campaign/{campaignId}](/v3/portal/api/ref/get-campaign-campaignid) endpoint. |
| `RTBAttributes.BudgetSettings.AdGroupFlights.BudgetInAdvertiserCurrency`  
or  
`RTBAttributes.BudgetSettings.AdGroupFlights.BudgetInImpressions` | Required | Depending on what type of budgets are set for the campaign flight, specify a budget for this ad group for the ad group flight. |
| `RTBAttributes.BudgetSettings.PacingMode` | Required | N/A |
| `RTBAttributes.BaseBidCPM.Amount` | Required | N/A |
| `RTBAttributes.BaseBidCPM.CurrencyCode` | Required | N/A |
| `RTBAttributes.MaxBidCPM.Amount` | Required | N/A |
| `RTBAttributes.MaxBidCPM.CurrencyCode` | Required | N/A |
| `RTBAttributes.CreativeIds` | Required | A list of the `CreativeIds` that this ad group can serve. If the ad group does not have any creatives, it will not bid. |
| `AssociatedBidLists` | Recommended | A list of `BidListIds` to associate with this ad group. Set whether they are enabled or disabled with the `IsEnabled` property. |

### 

Request Example[](#ad-group-create)

The following is an example of a [POST /v3/adgroup](/v3/portal/api/ref/post-adgroup) request to create an ad group with CPA as its ROI goal. Aside from the required properties, to enhance the ad group's performance, the request also turns on several [Koa features](#ad-group-koa-features), such as Identity Alliance and Predictive Clearing.

{

   "CampaignId":"{campaignid}",

   "AdGroupName":"Strategy 1",

   "AdGroupCategory":{

      "CategoryId":8311

   },

   "PredictiveClearingEnabled":true,

   "RTBAttributes":{

      "ROIGoal":{

         "CPAInAdvertiserCurrency":{

            "Amount":0.2,

            "CurrencyCode":"USD"

         }

      },

      "AudienceTargeting":{

         "CrossDeviceVendorListForAudience":\[

            {

               "CrossDeviceVendorId":11,

               "CrossDeviceVendorName":"Identity Alliance"

            }

         \]

      },

      "BudgetSettings":{

         "PacingMode":"PaceToEndOfDay",

         "DailyBudget":{

            "Amount":1,

            "CurrencyCode":"USD"

         }

      },

      "BaseBidCPM":{

         "Amount":1.0,

         "CurrencyCode":"USD"

      },

      "MaxBidCPM":{

         "Amount":5.0,

         "CurrencyCode":"USD"

      },

      "CreativeIds":\[

      \]

   },

   "AssociatedBidLists":\[

   \]

}

## 

Look Up Ad Groups[](#lookupadgroups)

The following table lists the endpoints that you can use to search for ad groups.

| Task | Endpoint | Returns All Details? | Available Filters |
| Retrieve details for a specific ad group. | [GET /v3/adgroup/{adGroupId}](/v3/portal/api/ref/get-adgroup-adgroupid) | Yes | N/A |
| Retrieve a filtered, paged list of ad groups for a specific campaign ID. | [POST /v3/adgroup/query/campaign](/v3/portal/api/ref/post-adgroup-query-campaign) | Yes | `AdGroupId`  
`Availability`  
`CampaignId`  
`Description`  
`Name`  
`Type` |
| Retrieve a filtered, paged list of ad groups for a specific advertiser ID. | [POST /v3/adgroup/query/advertiser](/v3/portal/api/ref/post-adgroup-query-advertiser) | Yes | `AdGroupId`  
`Availability`  
`CampaignId`  
`Description`  
`Name`  
`Type` |
| Check the status (enabled or not) of a specific ad group. | [GET /v3/adgroup/status/{adGroupId}](/v3/portal/api/ref/get-adgroup-status-adgroupid) | No | N/A |
| Retrieve the name of a specific ad group based on its ID. | [GET /v3/adgroup/name/{adGroupId}](/v3/portal/api/ref/get-adgroup-name-adgroupid) | No | N/A |

## 

Update Ad Groups[](#updateadgroups)

The following table lists the endpoints that you can use to update ad group details or to turn them on or off.

| Task | Endpoint | Notes |
| Update the details of a specific ad group. | [PUT /v3/adgroup](/v3/portal/api/ref/put-adgroup) | When updating ad groups with list objects, such as `AssociatedBidLists` and `CreativeIds`, each list is replaced with the new content provided.  
**IMPORTANT**: To avoid overwriting any lists, retrieve the current state of these objects using the [GET /v3/adgroup/{adGroupId}](/v3/portal/api/ref/get-adgroup-adgroupid) endpoint and include the entire list, including changes, in the PUT request. |
| Enable or disable a specific ad group. | [PUT /v3/adgroup](/v3/portal/api/ref/put-adgroup) | To enable or disable an ad group, retrieve its state via GET and set the `IsEnabled` property to `true` or `false` in a `PUT /v3/adgroup` call. Legacy `PUT /v3/adgroup/status` was permanently sunset on May 11, 2026 (HTTP 410 Gone). |

## 

Troubleshooting Tips[](#troubleshootadgroups)

> **TIP**: If your ad group is not spending to your expectations, be sure to turn on [performance-enhancing features](#ad-group-koa-features) and let Koa help you.

To form a complete picture of all of the targeting, blocking, and optimizations applied to an ad group, look up the enabled bid lists for the ad group, campaign, advertiser, and partner.

| Task | Endpoint | Includes Bid Line Details? |
| Look up bid lists associated with and enabled for an ad group. | [GET /v3/adgroup/{adGroupId}](/v3/portal/api/ref/get-adgroup-adgroupid) | No |
| Look up bid lists associated with and enabled for the parent campaign. | [GET /v3/campaign/{campaignId}](/v3/portal/api/ref/get-campaign-campaignid) | No |
| Look up bid lists associated with and enabled for the parent advertiser. | [GET /v3/advertiser/{advertiserId}](/v3/portal/api/ref/get-advertiser-advertiserid) | No |
| Look up bid lists associated with and enabled for the parent partner. | [GET /v3/partner/{partnerId}](/v3/portal/api/ref/get-partner-partnerid) | No |
| Look up bid list details. | [GET /v3/bidlist/{bidListId}](/v3/portal/api/ref/get-bidlist-bidlistid) | Yes |

### 

Common Issues

The following table lists the common issues that prevent ad group spend and recommends possible solutions.

| Issue | Solution |
| The ad group does not have at least one bid list of type `TargetList` or `BlockList` associated and enabled. | Use [PUT /v3/adgroup](/v3/portal/api/ref/put-adgroup) and use the `AssociatedBidLists` property to associate and enable at least one bid list. |
| The ad group is disabled. | Use [PUT /v3/adgroup](/v3/portal/api/ref/put-adgroup) and set the `IsEnabled` property to `true`. Note: Legacy `PUT /v3/adgroup/status` was permanently sunset on May 11, 2026 (HTTP 410 Gone). |
| The ad group does not have creatives assigned. | Use [PUT /v3/adgroup](/v3/portal/api/ref/put-adgroup) to add at least one creative in the `CreativeIds` property. |
| The ad group is associated with a bid list of type `TargetList`, and the bid list does not contain bid lines. | Use [PUT /v3/adgroup](/v3/portal/api/ref/put-adgroup) to disassociate the bid list, or use [PUT /v3/bidlist](/v3/portal/api/ref/put-bidlist) to add bid lines to the bid list. |
| The ad group has additional flights after updating a campaign in the platform UI. | To remove flights from an ad group, you must use the platform UI.  
**NOTE**: You can remove only current flights from an ad group. |

## 

FAQs[](#faqs)

### 

Can I enable Prism for all ad groups?

Yes. For details, see [Prism](/v3/portal/api/doc/Prism).