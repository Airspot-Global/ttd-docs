# Create ad groups

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/AdGroupCreate
- Retrieved: 2026-11-14
- Category: Guides

---

# Create ad groups

This guide explains how to create a single ad group or multiple ad groups at once. Creating an ad group is one step in a larger process; for the full sequence from campaign setup through creative association and budget allocation, see Ad group creation workflows.

> **TIP**: If you want to update multiple ad groups at once, use bulk operations in GraphQL.

## GraphQL API

To create an ad group with the GraphQL API, use the `adGroupCreate` mutation.

The following mutation example creates an ad group targeting CTV ads for maximum reach in brand awareness. It also enables Predictive Clearing to enhance the ad group's performance.

```
mutation {
    adGroupCreate(
        input: {
            campaignId: "CAMPAIGN_ID_PLACEHOLDER"
            name: "AD_GROUP_NAME_PLACEHOLDER"
            description: "AD_GROUP_DESCRIPTION_PLACEHOLDER"
            isEnabled: true
            channel: DISPLAY
            funnelLocation: AWARENESS
            roiGoal: { maximizeReach: true }
            baseBidCPMInAdvertiserCurrency: 25
            maxBidCPMInAdvertiserCurrency: 40
            koaOptimizationSettings: { predictiveClearingEnabled: true }
            creativeIdsToAdd: ["CREATIVE_ID_PLACEHOLDER"]
        }
    ) {
        data {
            id
        }
        userErrors {
            message
            field
        }
    }
}
```

## REST API

To create an ad group with the REST API, use the POST /v3/adgroup endpoint with a minimum of the required fields listed in the following table. If you want to create multiple ad groups at once, use bulk operations in the GraphQL API.

> **TIP**: To prioritize best-performing and most relevant inventory based on your ad group's goals, consider turning on the performance-enhancing settings.

| Property Name | Required | RTB Attribute? | Notes |
| --- | --- | --- | --- |
| `CampaignId` | Required | No | The ID of the campaign associated with the ad group. |
| `AdGroupName` | Required | No | Specify a name that follows your naming conventions, if you have any. For example, include the audience, geographic location, and other details that will help you identify the ad group. |
| `AdGroupCategory` | Conditionally Required, Nullable | No | Required if the advertiser's industry category ID is not set. If set to `null`, the advertiser category will be used. **NOTE**: The Trade Desk uses the IAB Tech Lab Content Taxonomy version 2.2 for assigning industry categories to advertisers. If you want to see how version 1.0 maps to version 2.2, see IAB content taxonomy mapping: Version 1.0 to 2.2. |
| `FunnelLocation` | Required | No | For details, see Funnel location. |
| `Channel` | Required | No | Channels inform bidding behavior and provide recommendations and insights. For details, see Channels. |
| `BaseBidCPM` | Required | RTB Attribute | CPM is used to define base and max bids. The base bid is the starting bid for an impression before bid adjustments from private contracts, bid lists, and optimizations. By setting a higher base bid for a valuable segment, you indicate a willingness to pay more for those impressions, improving your chances of winning them. |
| `CreativeIds` | Required | RTB Attribute | A list of the creative IDs that this ad group serves. Here's what you need to know about this property: - Ad groups require at least one approved creative to spend. - An ad group with no creatives will not spend. - You can include an empty array but be sure to upload your creatives before enabling your ad group. |
| `MaxBidCPM.Amount` | Required | RTB Attribute | The max bid must be greater than or equal to the minimum base bid threshold for the partner. The max bid is the highest amount an ad group will bid on a single impression. |
| `ROIGoal` | Required | RTB Attribute | Goals, or KPIs, measure the success of the ad group while driving performance and delivering results. An ad group can have its own goal set directly or inherit it from its parent campaign. Otherwise, the default value is `Reach`. |
| `AssociatedBidLists` | Recommended | No | A list of IDs of the bid lists to associate with this ad group. Here's what you need to know about this property: - You can associate bid lists with ad groups directly when creating or updating them. - You can use the `IncludeDefaultsFromCampaign` property to have bid lists inherited from the parent campaign when creating ad groups. - To enable the bid lists, set the `IsEnabled` property to `true`. |

The following is an example of a POST request to create an ad group targeting display ads with CPA as its ROI goal. Aside from the required properties, to enhance the ad group's performance, the request also turns on several performance-enhancing features, such as Predictive Clearing and Identity Alliance.

```
{
   "CampaignId":"{CAMPAIGN_ID_PLACEHOLDER}",
   "AdGroupName":"Strategy 1",
   "AdGroupCategory":{
      "CategoryId":8311
   },
   "PredictiveClearingEnabled":true,
   "FunnelLocation": "Awareness",
   "RTBAttributes":{
      "ROIGoal":{
         "CPAInAdvertiserCurrency":{
            "Amount":0.2,
            "CurrencyCode":"USD"
         }
      },
      "AudienceTargeting":{
         "CrossDeviceVendorListForAudience":[
            {
               "CrossDeviceVendorId":11,
               "CrossDeviceVendorName":"Identity Alliance"
            }
         ]
      },
      "BaseBidCPM":{
         "Amount":1.0,
         "CurrencyCode":"USD"
      },
      "MaxBidCPM":{
         "Amount":5.0,
         "CurrencyCode":"USD"
      },
      "CreativeIds":[

      ]
   },
   "AssociatedBidLists":[

   ]
}
```

> **NOTE**: The provided request example does not include the `KoaOptimizationSettings.KoaDimensions` properties in the `RTBAttributes` object. With the exception of advertisers in certain industries, such as Careers, Medical Health, Personal Finance, and Real Estate, Koa Optimizations will be disabled for the newly created ad group. For details and instructions on how to enable it for certain dimensions, see Koa Optimizations. See also FAQs.
