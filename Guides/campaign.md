# Campaign (Solimar)

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/SolimarCampaign
- Category: Guides

---

# Campaign (Solimar)

> **IMPORTANT**: This guide is intended for Solimar users. To create and manage campaigns in Kokai, see [Campaigns](/v3/portal/api/doc/Campaigns).

A campaign is a group of strategies with the same budget, flight dates, and conversion events. Campaigns in The Trade Desk platform are focused on and driven by goals, or key performance indicators (KPIs). That’s why multi-level goal setting—where you can input a high-level business objective and tie it back to multiple KPIs—is so important. Setting multi-level goals enables Koa, The Trade Desk AI, to optimize your campaign to drive performance more effectively. With your goals as the guide, and unlimited expressiveness, you can be confident that every ad impression you’re buying is the right one, at the right price. This could mean running campaigns in channels you had not previously considered, resulting in multiple campaigns being created to best achieve your goals.

Here’s what you need to know about campaigns:

*   A campaign must include a name, advertiser ID, budget, and the following:
    *   A broad [objective](#campaign-objective) that identifies what you want people to do when they see your ads.
    *   The [channel](#primary-channel) through which ads are served.
    *   At least one [campaign goal](#campaign-goals) (required) and up to two additional goals (optional). Campaign goals are also known as KPIs.
    *   [Conversion reporting columns](#conversion-columns) which are the mappings of conversion tracking tags, or conversion pixels, to reporting columns.
*   Campaign objective, primary goal, and channel property values are required for all new campaigns on [create](#create-campaign). You can [update](#update-campaign) these values at any time.
*   For legacy campaigns with no objective, primary goal, and channel properties set, these values are optional when [updating](#update-campaign) and [cloning](#clone-campaign) them. For details, see [Manage Campaigns](#manage-campaigns).
*   The [Koa Optimizations](/v3/portal/api/doc/SolimarKoaOptimizations) feature automatically optimizes your campaign performance based on the objective and goals you select. It is always on by default.
*   To [automatically allocate](/v3/portal/api/doc/SolimarCampaignBudget) the campaign budget, be sure to turn on Auto Allocator and Auto Prioritization.
*   To save time and ensure consistency across ad groups, you can include advertiser’s default bid lists in campaigns and further propagate them to ad groups. For details, see [Default Bid Lists](/v3/portal/api/doc/BidListDefault).
*   To create a campaign, you'll need to assign at least one [creative](/v3/portal/api/doc/Creative), but you don't need to have creatives available.

For details on budgets, flights, pacing options, and other important concepts, see [Campaigns](https://desk.thetradedesk.com/knowledge-portal/en/campaigns.html) in the Knowledge Portal.

## 

Campaign Objective[](#campaign-objective)

To measure the success of your campaigns effectively, be sure to choose the appropriate objective. The campaign objective identifies the focus of your campaign (awareness, consideration, and conversion), and the platform will automatically optimize campaign performance accordingly. For example, you may want to focus on getting people to consider your business, encourage them to make a purchase, or sign up for an event.

You can choose _one_ of the following three broad objectives for your campaign:

| Objective | Description |
| Awareness | Generate interest in your brand. Discover qualified leads to increase brand knowledge and reach as many people as possible in your target audience. Increasing brand awareness is about telling people what makes your business valuable. |
| Consideration | Get people to think about your business and seek more information. Reach new customers and influence them to become prospective customers. |
| Conversion | Encourage prospective customers who are already interested in your business to take a specific action. |

To set a campaign objective, you must also specify the channel for the campaign and at least the primary goal. For details, see [Create Campaigns](#create-campaign).

## 

Campaign Channel[](#primary-channel)

A channel is the medium through which ads are served. With the advent of digital advertising, the number of channels available for advertising has grown. Setting the channel for your campaign allows the platform to provide specific recommendations and automatically optimize toward reaching your goals. Depending on their creatives and bid lists, ad groups within the campaign, however, may subsequently target more than the campaign channel.

You can choose one of the following channels to set as the channel for your campaign:

*   `Display`
*   `Video`
*   `Audio`
*   `TV`
*   `NativeDisplay`
*   `NativeVideo`
*   `DigitalOutOfHome` (DOOH)—primarily outdoor digital ad placements, such as digital billboards and signs in a variety of places including gas stations, airports, freeways, the sides of buildings, and so on. If you want to set DOOH as your channel but this option isn't available, contact your Technical Account Manager.

For details, examples, and specifications for each channel, see [Channels](https://desk.thetradedesk.com/knowledge-portal/en/channels-intro.html) in the Knowledge Portal.

## 

Campaign Goals[](#campaign-goals)

Campaign goals are the main KPIs toward which Koa automatically optimizes performance.

Here’s what you need to know about campaign goals:

*   You can set up to three goals for a campaign. The `PrimaryGoal` is required, while the `SecondaryGoal` and `TertiaryGoal` are optional.
*   All three goals are hierarchically interdependent. For example, to set a tertiary goal, you must first set the secondary one.
*   Ad groups initially inherit only the `PrimaryGoal` from their parent campaign and may have their own goals.
*   All goal properties are mutually exclusive. In other words, in each goal object (`PrimaryGoal`, `SecondaryGoal`, and `TertiaryGoal`), you can select only _one_ of the goals (properties) listed in the table below.
*   Some goals require a target set, which is the amount (in the advertiser's currency) or percentage. The following table lists the available goals that you can choose as KPIs.

| Goal | Has Target? | Description | Goal Object Property | Supported by Koa Optimizations? |
| Reach | No | This is a broad goal without any specific metrics used as primary benchmarks. Choose this goal if you want to reach as many unique users as possible in your intended audience given your specified base bid, max bid, and any bid adjustments. | `MaximizeReach` | Yes |
| Incremental Reach | No | Maximize the number of unique viewers beyond those who have already been reached through linear TV.  
This goal prioritizes spend toward CTV PMP deals that improve unique or incremental reach of the ad group and deprioritize spends toward PMP deals that do the opposite. | `MaximizeLtvIncrementalReach` | Yes |
| CPC | Yes, currency amount | _Cost per click_. The amount the advertiser pays every time an ad is clicked. If your primary engagement metric is clicks, you may want to choose CPC as your goal. See also the CTR goal. | `CPCInAdvertiserCurrency` | Yes |
| CPA | Yes, currency amount | _Cost Per Acquisition_. The amount the advertiser pays based on the number of "acquisitions" (conversions) made.  
If your goal is a specific action like a purchase or a newsletter sign up, you may want to choose CPA as your goal. | `CPAInAdvertiserCurrency` | Yes |
| vCPM | Yes, currency amount | (Estimated) _Viewable Cost Per Mille_ (thousand). Setting this goal optimizes based on the cost of _viewable_ inventory. vCPM is calculated by dividing eCPM by the in-view rate (vCPM = eCPM / in-view rate).  
Unlike the Viewability goal, which optimizes toward an entered in-view target percentage, vCPM optimizes to inventory that is effective in terms of its viewable cost. | `VCPMInAdvertiserCurrency` | Yes |
| CPCV | Yes, currency amount | _Cost Per Completed View_. The amount the advertiser pays after a video has been viewed all the way through. Set this goal if your campaign is using video creatives and you want to encourage immediate engagement. This is a great option for brand-focused advertisers. | `CPCVInAdvertiserCurrency` | Yes |
| ROAS | Yes, percentage | _Return On Ad Spend_. The ratio of total revenue compared to total spend. Set this ROI-type of goal when you can pass specific revenue amounts to the platform in your conversion pixel. | `ReturnOnAdSpendPercent` | Yes |
| CTR | Yes, percentage | _Click Through Rate_. It is calculated by dividing the number of clicks by the number of impressions. A high CTR indicates a more successful campaign.  
This alternative to CPC does not consider the cost of the media, but only how often a user clicks an ad. | `CTRInPercent` | Yes |
| VCR | Yes, percentage | _Video Completion Rate_. This goal allows optimization toward inventory where ads are viewed or heard to completion. | `VCRInPercent` | Yes |
| Viewability | Yes, percentage | Viewability is a metric that measures whether an ad impression has been viewed by a website user rather than simply being displayed.  
Unlike the vCPM goal, which optimizes based on the cost of viewable inventory, Viewability optimizes toward an entered in-view target percentage. | `ViewabilityInPercent` | No |
| Nielsen OTP | Yes, percentage | Nielsen _On Target Percentage_. Setting this goal helps you optimize toward a percentage of impressions delivered to a chosen demographic (out of the total number of impressions served during your campaign).  
Nielsen sets different percentage benchmarks for different demographics and different regions. Nielsen's suggested benchmarks can be found on their website. You can also contact your Account Manager to get a better sense of what your percentage should be.  
When set, the demographic must be provided in the form of `NielsenTrackingAttributes` or you must set `TargetDemographicSettingsEnabled` to `true`.  
If you select this goal, fees for Nielsen reporting may apply. | `NielsenOTPInPercent` | No |
| Miaozhen OTP | Yes, percentage | Miaozhen _On Target Percentage_. Setting this goal will help you optimize toward a percentage of impressions delivered to a chosen demographic (out of the total number of impressions served during your campaign).  
When set, the demographic must be provided in `MiaozhenTrackingAttributes`.  
If you select this goal, reporting fees may apply. | `MiaozhenOTPInPercent` | No |

> **NOTE**: Some goals may require special permissions. If needed, please contact your Account Manager for appropriate access.

## 

Conversion Reporting Columns[](#conversion-columns)

A conversion reporting column is the mapping of conversion tracking tags, or conversion pixels, to reporting columns.

Here's what you need to know about conversion reporting columns:

*   If your campaign is not conversion-focused, send the `CampaignConversionReportingColumns` object array empty.
*   To add a conversion reporting column to your campaign, you must include at least the following `CampaignConversionReportingColumns` parameters:
    *   `TrackingTagId`  
        The tracking tag to which the ID belongs must have a type considered to be a conversion (for details, see the [Tracking Tags](/v3/portal/api/ref/post-trackingtag) and [Tracking Tag Type](/v3/portal/api/ref/get-trackingtag-query-facets) APIs).
    *   `ReportingColumnId`  
        Metrics about this conversion will appear in reports under this reporting column. Only one tracking tag ID and cross-device attribution model ID may be mapped to each column within a campaign. For details, see [Set Up Cross-Device Attribution for a Conversion Campaign](/v3/portal/api/doc/CrossDeviceTargeting#attribution).
*   You can include up to five reporting columns.
*   You can always update your reporting columns later, but new reports will not contain retroactive metrics for these conversions. If you assign different conversions to a previously-used reporting column, your long-term roll-up reports could be misleading.

## 

Manage Campaigns[](#manage-campaigns)

The following table lists the high-level campaign tasks and summarizes the objective, goal, and channel property value requirements for managing Solimar campaigns and any Legacy campaigns that do not have these properties set.

| Task | Endpoint | Objective, Primary Goal, Channel |
| Solimar Campaigns | Legacy Campaigns |
| [Create](#create-campaign) a campaign. | [POST /v3/campaign](/v3/portal/api/ref/post-campaign) | Required | N/A |
| [Update](#update-campaign) a campaign. | [PUT /v3/campaign](/v3/portal/api/ref/put-campaign) | Required  
Can be changed | Optional  
May be added |
| [Clone](#clone-campaign) a campaign. | [POST /v3/campaign/clone](/v3/portal/api/ref/post-campaign-clone) | Copied automatically  
May not be changed | Optional  
May be added |

## 

Create a Campaign[](#create-campaign)

To create a campaign, use the [POST /v3/campaign](/v3/portal/api/ref/post-campaign) endpoint.

Here’s what you need to know about creating campaigns:

*   The following properties are required:
    *   Advertiser ID
    *   Campaign name
    *   [Objective](#campaign-objective)
    *   [Goal](#campaign-goals)
    *   [Channel](#primary-channel)
    *   [Conversion reporting columns](#conversion-columns)
    *   Budget (especially if the pacing mode is not set to pace ahead or evenly)
*   For campaign goals, only the primary goal is required. Secondary and tertiary goals are optional and hierarchically interdependent. For details, see [Campaign Goals](#campaign-goals).
*   To [automatically allocate](/v3/portal/api/doc/SolimarCampaignBudget) the campaign budget to multiple ad groups, be sure to turn on the Auto Allocator and Auto Prioritization options.
*   If your campaign is not conversion-focused, send the `CampaignConversionReportingColumns` object array empty. For details, see [Conversion Reporting Columns](#conversion-columns).
*   If pacing mode is off or not included in the request, be sure to include a budget.
*   To save time and ensure consistency across ad groups, you can include advertiser’s default bid lists in campaigns and further propagate them to ad groups. For details, see [Default Bid Lists](/v3/portal/api/doc/BidListDefault).
*   After campaign creation, you can [update](#update-campaign) parameter values as needed. You cannot remove the primary goal, but you can remove the secondary and tertiary goals.

### 

Example Request[](#create-response)

Here's an example of a [POST /v3/campaign](/v3/portal/api/ref/post-campaign) request body for a campaign that has multiple goals.

{

    "AdvertiserId": "{advertiserid}",

    "CampaignName": "New Campaign XYZ",

    "Budget": {

        "Amount": 1200000,

        "CurrencyCode": "USD"

    },

    "StartDate": "2022-11-01T00:00:00",

    "EndDate": "2022-12-31T23:59:00",

    "PacingMode": "PaceAhead",

    "CampaignConversionReportingColumns": \[\],

    "Objective": "Awareness",

    "PrimaryGoal": {

        "MaximizeReach": true

    },

    "SecondaryGoal": {

        "MaximizeLtvIncrementalReach": true

    },

    "TertiaryGoal": {

        "VCPMInAdvertiserCurrency": {

            "Amount": 28.00,

            "CurrencyCode": "USD"

        }

    },

    "PrimaryChannel": "Video",

    "AutoAllocatorEnabled": true,

    "AutoPrioritizationEnabled": true,

    "IncludeDefaultsFromAdvertiser": true

}

### 

Example Response

Here's an example of a [POST /v3/campaign](/v3/portal/api/ref/post-campaign) response body with multiple optional properties in addition to the required ones.

{

    "AdvertiserId": "{advertiserid}",    

    "CampaignId": "{campaign}",

    "CampaignName": "New Campaign XYZ",    

    "Budget": {

        "Amount": 1200000.000000,

        "CurrencyCode": "USD"

    },

    "BudgetInImpressions": null,

    "DailyBudget": null,

    "DailyBudgetInImpressions": null,

    "StartDate": "2022-11-01T00:00:00",

    "EndDate": "2022-12-31T23:59:00",

    "AutoAllocatorEnabled": true,

    "AutoPrioritizationEnabled": true,

    "MinimumAdGroupSpendInAdvertiserCurrency": 0.000000,

    "PacingMode": "PaceAhead",

    "CampaignFlights": \[

        {

            "CampaignFlightId": 4250052,

            "CampaignId": "8we6afv",

            "StartDateInclusiveUTC": "2022-11-01T00:00:00",

            "EndDateExclusiveUTC": "2022-12-31T23:59:00",

            "BudgetInAdvertiserCurrency": 1200000.000000,

            "BudgetInImpressions": null,

            "DailyTargetInAdvertiserCurrency": 50000.000000,

            "DailyTargetInImpressions": null

        }

    \],

    "CustomLabels": \[\],

    "CustomCPAType": "Disabled",

    "CustomCPAClickWeight": null,

    "CustomCPAViewthroughWeight": null,

    "CustomROASType": "Disabled",

    "AssociatedBidLists": \[\],

    "CurrentAndFutureAdditionalFeeCards": \[

        {

            "StartDateUtc": "2022-10-31T23:59:59",

            "Fees": \[

                {

                    "Description": "Cost Percentage Fee",

                    "Amount": 15.000000,

                    "FeeType": "PartnerCostPercentage"

                },

                {

                    "Description": "CPM Fee",

                    "Amount": 0.500000,

                    "FeeType": "FeeCPM"

                }

            \],

            "OwnerId": "8we6afv",

            "OwnerType": "campaign"

        }

    \],

    "CampaignType": "Standard",

    "DeprecateHouseholdTargetingAndAttribution": true,

    "IsBallotMeasure": false,

    "Increments": \[\],

    "Objective": "Awareness",

    "PrimaryGoal": {

        "MaximizeReach": true

    },

    "SecondaryGoal": {

        "MaximizeLtvIncrementalReach": true

    },

    "TertiaryGoal": {

        "VCPMInAdvertiserCurrency": {

            "Amount": 28.000000,

            "CurrencyCode": "USD"

        }

    },

    "PrimaryChannel": "Video",   

    "Description": null,

    "PartnerCostPercentageFee": 0.000000,

    "PartnerCPMFee": {

        "Amount": 0.000000,

        "CurrencyCode": "USD"

    },

    "PartnerCPCFee": {

        "Amount": 0.000000,

        "CurrencyCode": "USD"

    },

    "CampaignConversionReportingColumns": \[\],

    "DefaultBidLists": \[

        {

            "BidListId": "134dfgou"

        },

        {

            "BidListId": "097sdfi3"

        }

    \],

    "Availability": "Available",

    "CtvTargetingAndAttribution": false,

    "CreatedAtUTC": "2022-11-22T02:18:42.173",

    "LastUpdatedAtUTC": "2022-11-22T02:18:42.173",

    "FrequencySettings": {

        "LifetimeFrequencyCap": null,

        "FrequencyCap": null,

        "FrequencyPeriodInMinutes": 44640

    },

    "PurchaseOrderNumber": null,

    "TimeZone": "Etc/GMT"

}

## 

Update a Campaign[](#update-campaign)

To update a campaign, use the [PUT/campaign](/v3/portal/api/ref/put-campaign) endpoint.

Here’s what you need to keep in mind about updating campaigns and their KPIs:

*   You can update the campaign [objective](#campaign-objective), [goals](#campaign-goals), and [channel](#primary-channel), but you cannot remove any values, except the secondary and tertiary goals.
*   For legacy campaigns with none of these properties set, all of these properties are optional on update. If you set one of them, however, the rest of them become required. For example, if you set the channel, you must add the objective and at least the primary goal.
*   To change a goal, set a value for the corresponding property. This will automatically remove the previously set goal property.
*   All three goals are hierarchically interdependent, for example, you cannot remove the secondary goal without removing the tertiary one.
*   To remove the secondary or tertiary goal, pass `null` for the `SecondaryGoal` or `TertiaryGoal` object.
*   Setting a Boolean goal value to `false` removes the goal from the campaign.
*   To keep the currently set goal when updating the campaign, exclude the goal object from the request or send it empty.
*   If you update the primary goal of a campaign, its existing ad groups will not be automatically updated. To align them with the updated primary campaign goal, you need to update the ad group goals manually.

### 

Example Request

For example, to update the campaign goals in the [example request](#create-response), you can include the following [PUT/campaign](/v3/portal/api/ref/put-campaign) request body:

{

   "CampaignId": "{campaignid}",

   "CampaignName": "New Campaign XYZ",

   "Objective": "Awareness",

   "PrimaryGoal": {

      "MaximizeReach": true

   },

   "SecondaryGoal": null,

   "PrimaryChannel": "NativeDisplay"

}

## 

Clone a Campaign[](#clone-campaign)

If you want to run a campaign with the same channel and strategies as one that you have already created, you can clone the existing campaign instead of creating new campaigns from scratch. To clone a campaign, use the [POST /v3/campaign/clone](/v3/portal/api/ref/post-campaign-clone) endpoint.

Here’s what you need to know about cloning campaigns:

*   You can clone only one campaign at a time, with up to 500 ad groups.
    
*   To clone ad group budgets and or campaign flights, you must provide campaign flight IDs in the `CampaignFlights` object.
    
*   If the original campaign that you want to clone has an [objective](#campaign-objective), the [channel](#primary-channel), and at least one [goal](#campaign-goals) set, they are copied automatically. Otherwise, they are optional.
    
*   If the original campaign that you want to clone has advanced frequency settings configured, they will not be cloned.
    
    > **IMPORTANT**: To avoid unintentional spend, be sure to update frequency settings in your cloned campaign.
    
*   You may not change the campaign objective, goals, or channel when you clone campaigns. For details on making changes, see [Update a Campaign](#update-campaign).
    
*   The [POST /v3/campaign/clone](/v3/portal/api/ref/post-campaign-clone) endpoint only submits a job to clone a campaign and returns a reference ID. You can use the reference ID to check the job status by calling the [GET /v3/campaign/clone/status/{referenceId}](/v3/portal/api/ref/get-campaign-clone-status-referenceid) endpoint.
    

### 

Example Requests

Here’s an example of a [POST /v3/campaign/clone](/v3/portal/api/ref/post-campaign-clone) request body for cloning a campaign with the objective, goals, and other properties already set. This request clones all ad groups and budgets for the specified flight.

{

    "CampaignId": "{campaignid}",

    "CampaignName": "Cloned Campaign XYZ"

}

Here’s an example of a [POST /v3/campaign/clone](/v3/portal/api/ref/post-campaign-clone) request body for cloning a campaign that does not have the objective, goals, and channel properties set.

{

    "CampaignId": "{campaignid}",

    "CampaignName": "Cloned Campaign XYZ",

    "Objective": "Awareness",

    "PrimaryGoal": {

        "MaximizeReach": true

    },

    "PrimaryChannel": "Video"

}

## 

FAQs[](#faqs)

The following is a list of frequently asked questions about campaign and ad group goal management. See also [Campaign Budget Allocation (Solimar)](/v3/portal/api/doc/SolimarCampaignBudget).

### 

Do I have to update Legacy campaigns that do not have objectives, goals, and channels set?

No. All Legacy campaigns previously created through the UI or API that are missing campaign KPI data will continue to function as is and will not require this data if you update them via the API. For details, see [Manage Campaigns](#manage-campaigns).

### 

Do I have to specify objectives, goals, and channels when cloning campaigns?

If the campaign that you are trying to clone already has these properties set, they will be automatically copied. For Legacy campaigns, these properties are optional.

### 

Can I change objectives, goals, and channels when cloning campaigns?

No. If the campaign you are trying to clone already has these properties set, you may not change them. You can clone the campaign and then use the [PUT/campaign](/v3/portal/api/ref/put-campaign) endpoint to make the updates you want. For details, see [Update Campaigns](#update-campaign).

### 

How are ad group KPIs set when there are multiple campaign goals?

The primary campaign goal becomes the default KPI for all ad groups in the campaign.

### 

What happens if no ad groups meet their KPI targets?

The secondary and tertiary campaign goals are ignored by the Auto-Prioritized AutoAllocator until at least one ad group reaches the primary goal.

### 

How often are rankings/priorities updated?

Every other day (after a 24-hour data collection cycle).

### 

What happens if the campaign has only one (primary) goal inherited by its ad groups?

They are managed the way they were before the Solimar release.

### 

Can I update my campaign in the platform UI?

If you create a campaign in platform API, be sure to make changes only in the platform API. The platform UI may update your campaigns differently from the API. For example, if you update your campaign flight in the platform UI, it will add the flight to all of ad groups associated with that campaign.