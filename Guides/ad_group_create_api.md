# Ad group creation workflows

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/AdGroupCreateAPI
- Retrieved: 2026-11-14
- Category: Guides

---

# Ad group creation workflows

This page outlines the options and steps you need to take to create, configure, and maintain ad groups. Unlike campaigns, ad groups have near-complete parity between the REST and GraphQL APIs, so most steps list both options. For a breakdown of what each API supports, see GraphQL and REST API comparison.

Here's what you need to know before you start:

- Every ad group must be associated with a campaign, and its `ChannelId` value must match the channel of the parent campaign.
- An ad group needs at least one approved creative before you can enable it. You can create an ad group with an empty `CreativeIds` array, but it will not spend.
- Budget allocation and pacing are set at the campaign level and require GraphQL. For details, see Budget allocation.

## Process overview

The following table outlines the process step by step and provides links to detailed user guides.

| Step |  | Description | Operation | User Guide | Notes |
| --- | --- | --- | --- | --- | --- |
| **1** |  | Confirm the parent campaign and its channel. | `campaign` query | Campaigns | The ad group creative type must match the campaign channel. If the channels are mismatched, only the ad group channel is used for bidding. |
| **2** |  | Choose how you want to create your ad groups. | N/A | N/A | The requirements are the same regardless of which option and API you choose. |
|  |  | - Create a single ad group. | `adGroupCreate` mutation POST /v3/adgroup | Create ad groups | Set the funnel location and goal explicitly, or the ad group inherits them from the campaign primary goal. |
|  |  | - Create multiple ad groups at once. | `createMutationBulk` mutation, wrapping `adGroupCreate` | GraphQL API bulk operations | GraphQL only. You can include up to 1000 `input` objects in a single bulk mutation. |
|  |  | - Create ad groups as copies of existing ones. | `campaignClonesCreate` mutation | Clone campaigns | You can clone ad groups only with their parent campaign. You can choose to clone all, none, or a selection of the ad groups. |
| **3** |  | Associate at least one approved creative. | `adGroupAssociateCreative` mutation PUT /v3/adgroup | Creatives | Required before you can enable the ad group. In REST, the `CreativeIds` list is replaced with the content you provide. |
| **4** |  | Associate and enable at least one bid list. | POST /v3/adgroup/bidlist PUT /v3/adgroup | Bid lists | To inherit the campaign bid lists instead, use the `IncludeDefaultsFromCampaign` property when you create the ad group. See also Default bid lists. |
| **5** |  | (Optional) Allocate flight budget to the ad group. | `campaignBudgetSettingsUpdate` mutation | Budget allocation | GraphQL only, and only after the ad group exists. By default, ad groups have zero allocation, which lets the platform algorithm allocate the flight budget to where it finds the most value. |
| **6** |  | (Optional) Review the new ad groups, their settings, and their performance. | `adGroup` and `adGroups` queries | Look up ad groups | With GraphQL, you can query one ad group or many with custom queries, including performance metrics by date range. |
| **7** |  | Update ad group settings, or enable and disable the ad group. | `adGroupUpdate` mutation PUT /v3/adgroup | Update ad groups | To update multiple ad groups at once, use bulk operations. |
| **8** |  | (Optional) Archive ad groups you no longer need. | `adGroupsArchive` mutation | Archive ad groups | GraphQL only. **IMPORTANT**: An ad group that is archived cannot be restored. |

> **TIP**: To prioritize the best-performing and most relevant inventory for your goals, turn on the performance-enhancing features available for ad groups, such as Predictive Clearing and Identity Alliance.
