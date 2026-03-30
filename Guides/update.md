# Update Campaigns

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/CampaignUpdate
- Category: Guides

---

# Update Campaigns

After you [clone](/v3/portal/api/doc/CampaignCloning) or [create](/v3/portal/api/doc/CampaignCreate) a campaign, you may need to make adjustments to maintain high effectiveness and relevance. This can include optimizing the settings for underperforming ad groups, creatives, or keywords. If you notice a shift in your target audience, you can adjust your targeting settings to help ensure your ads reach the right users. You can also reallocate your budget to focus on higher-performing segments or to accommodate new priorities. Additionally, modifying your campaign goals when conversion behavior changes can help keep your strategy aligned with performance trends. See also [Drive Your KPIs to Success](/v3/portal/api/doc/DriveKPIs).

Here's what you need to know about updating campaigns:

*   Updating a campaign has most of the same [requirements](/v3/portal/api/doc/CampaignCreate#requirements) and dependencies as [creating](/v3/portal/api/doc/CampaignCreateWorkflows) a campaign.
*   To update single campaigns, use the [REST API](#rest). For updating multiple campaigns in bulk, use the GraphQL [bulk operations](/v3/portal/api/doc/GqlBulkOperations).

This page explains how to update a single campaign. For details about updating [bid lists](/v3/portal/api/doc/BidList), [seeds](/v3/portal/api/doc/Seed), [ad groups](/v3/portal/api/doc/AdGroup), and other settings, see the respective guides.

## 

REST Request Example[](#rest)

To update a campaign, use the [PUT /v3/campaign](/v3/portal/api/ref/put-campaign) endpoint.

For example, to update the campaign goals in the example request, you can include the following [PUT /v3/campaign](/v3/portal/api/ref/put-campaign) request body:

{

   "CampaignId": "CAMPAIGN\_ID\_PLACEHOLDER",

   "PrimaryGoal": {

      "MaximizeReach": true

   },

   "SecondaryGoal": null

}

### 

Updating Campaign Goals

All three goals (primary, secondary, and tertiary) are hierarchically interdependent, for example, you cannot remove the secondary goal without removing the tertiary one. Here’s what you need to keep in mind about updating campaign goals:

*   You can update the campaign [goals](#goals), however you cannot remove any existing values, except the secondary and tertiary goals.
*   To keep the currently set goal when updating the campaign, exclude the goal object from the request or send it empty.
*   If you update the primary goal of a campaign, its existing ad groups will not be automatically updated. To align them with the updated primary campaign goal, you need to update the ad group goals manually.

The following table details how you can update and remove a goal from a campaign.

| Update Task | Notes |
| Update | To change a goal, set a different value for the corresponding property. This will automatically remove the previously set goal property.  
**IMPORTANT**: If you update the primary goal of a campaign, its existing ad groups will not be automatically updated. To align them with the updated primary campaign goal, you need to update the ad group goals manually. |
| Remove | To remove the secondary or tertiary goal, pass `null` or set the value to `false` for the `SecondaryGoal` or `TertiaryGoal` object. |

## 

FAQs[](#faqs)

### 

Can I use the GraphQL API to update campaigns?

Yes, you can use the [bulk operation](/v3/portal/api/doc/GqlBulkOperations) mutations to update a single campaign or multiple campaigns at once.

### 

Can I attach a different seed to a campaign I already created?

Yes. For details, see [Seeds](/v3/portal/api/doc/Seed).