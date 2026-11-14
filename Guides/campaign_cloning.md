# Clone campaigns

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/CampaignCloning
- Retrieved: 2026-11-14
- Category: Guides

---

# Clone campaigns

Campaign cloning is the process of duplicating an existing campaign to create a new one with identical channels, strategies, budgets, and ad groups. Unlike creating campaigns from scratch individually or in bulk, cloning a campaign enables you to efficiently recreate successful campaigns for various purposes, such as targeting different audience segments while maintaining consistency in approach and resource allocation. This streamlined method ensures that proven strategies can be easily adapted and deployed, optimizing campaign management and maximizing results across diverse demographics and markets.

Here’s what you need to know about cloning campaigns:

- Campaign cloning is a two-step asynchronous process where you submit a job for processing and check its progress.
- You can use either the REST API or GraphQL API, both of which offer different options for cloning campaigns.
- You can clone up to 50 different campaigns in a single call.
- You can create up to 1000 campaign copies in a single call regardless of how many different campaigns you're cloning.
- You can clone campaigns with up to 500 ad groups.
- You can specify which ad groups you want to clone and modify some campaign settings.

## Campaign settings you can copy and modify

Here’s what you need to know about which campaign settings you can clone and modify:

- When you clone a campaign to create a copy of it, most settings are copied to the new campaign.
- You can modify certain campaign settings for the copy, but not all.

The following table lists the campaign settings that are copied and which settings you can modify for the new copy.

| Settings | Copied from the source campaign? | Modifiable during the cloning process? | Notes |
| --- | --- | --- | --- |
| Name | Not copied | Modifiable | You must provide the name for the new copy of the campaign. |
| Flights | Copied only if the flight ID is provided | Modifiable | None. |
| Channel | Copied | Modifiable | You can change the campaign channel but you cannot modify the ad group channels during the cloning process. To change ad group channels, update the cloned ad groups. |
| Goals | Copied | Modifiable | None. |
| Targeting | Copied | Modifiable | None. |
| Budget | Copied | Modifiable | If you clone campaigns using GraphQL or use REST with the `version` property set to `Kokai`, budgets for all new campaigns are automatically updated to use the Kokai budgeting version and settings. No additional updates are required. |
| Seed | Copied | Modifiable | None. |
| Frequency settings | Copied | Not modifiable | None. |
| Advanced frequency settings | Not copied | Not modifiable | The frequency settings set in the source campaign through the API. **IMPORTANT**: To avoid unintentional spend, be sure to update frequency settings in the campaign copy. |
| Ad groups | Copied | Modifiable only with GraphQL | You can copy all, none, or specific ad groups from the source campaign by doing the following with both REST and GraphQL: - To clone all ad groups, set the ad group array to `null`. - To clone no ad groups, include an empty ad group array. For details about which ad group settings you can modify in GraphQL for the copies, see Ad group settings. |
| Audiences | Copied only if an associated ad group has Prism enabled | Not modifiable | Copied with the `- Copy` suffix appended to the segment name, such as `AUDIENCE_NAME_PLACEHOLDER - Copy`. |
| Bid lists | Copied | Not modifiable | To modify the cloned bid list, use the bidListClone mutation. |
| All other settings | Copied | Not modifiable | None. |

### Ad group settings

Here's what you need to know about ad groups when cloning campaigns:

- You cannot modify ad group settings using REST.
- You can modify the following ad group settings using GraphQL:

  - Base and max bid
  - Funnel location
  - Inventory marketplace usage

- `Mixed` is only accepted as a `ChannelId` property value if you do not designate a channel ID in your API POST calls. When cloning campaigns, update any ad groups with the `ChannelId` property set to `Mixed` to the appropriate value supported in Kokai.
- When cloning a campaign, the platform also clones the audience associated with each ad group that has Prism enabled. The cloned audience has the `- Copy` suffix appended to its name, such as `AUDIENCE_NAME_PLACEHOLDER - Copy`. This duplication ensures Prism is optimized for each ad group.

## Process overview

To clone a campaign, use either the REST API or GraphQL API to complete the following steps:

1. Specify which campaign you want to clone and submit a job that starts the cloning process.
2. (Optional) Check the status of the job.

> **NOTE**: Depending on the amount of data in a campaign, it may take from a few seconds to a few minutes to process.

The following table lists the differences between REST and GraphQL for cloning campaigns.

| Comparison | REST | GraphQL |
| --- | --- | --- |
| Number of campaigns you can clone | One campaign | Up to 50 different campaigns |
| Number of copies or clones you can create | One copy | Up to 1000 copies |
| Request Processing | 2-step, asynchronous | 2-step, asynchronous |

> **TIP**: For optimized audience-based buying, The Trade Desk has curated a pool of thousands of vetted, trusted sellers and publishers at no cost to you. Explore the Sellers and Publishers 500+ marketplace to take advantage of this opportunity.

### Clone campaigns with the GraphQL API

To clone a campaign in GraphQL, complete the following steps.

| Step | Task | Operation Type | Operation Name | Notes |
| --- | --- | --- | --- | --- |
| 1 | Submit the cloning job. | Mutation | `campaignClonesCreate` | A successful response returns an ID that you can use to check the status of the job. |
| 2 | (Optional) Check the status of the job. | Query | `campaignCloneJobsProgress` | Include the job progress ID returned after you submitted the job. |

> **NOTE**: You can clone up to 50 campaigns at once and create up to 1000 campaign copies at a time.

To submit a job to clone a campaign in GraphQL, in a `campaignClonesCreate` mutation, specify at least the following for each campaign you want to clone:

- The ID of the campaign you want to clone.
- The number of campaign copies you want to create.
- A list of names for each copy.
- The campaign flight and other required information.

The following example illustrates how to clone two campaigns and make multiple copies of each campaign. One campaign creates copies of only specific ad groups assigned to it, while the other creates copies of all assigned ad groups.

```
mutation {
  campaignClonesCreate(
    input: {
      campaignCloneData: [
        {
          campaignId: "CAMPAIGN_ID_A_PLACEHOLDER"
          numberOfClones: 1
          defaultUseInventoryMarketPlace: true
          cloneNames: ["CAMPAIGN_A_CLONE_PLACEHOLDER_01"]
          campaignFlights: [
            {
              startDateInclusive: "2024-05-06T20:26:20.077Z",
              budgetInAdvertiserCurrency: 12000000.00
            }
          ]
          selectedAdGroups: [
            { adGroupId: "AD_GROUP_ID_PLACEHOLDER_01", useInventoryMarketPlace: false },
            { adGroupId: "AD_GROUP_ID_PLACEHOLDER_02" },
            { adGroupId: "AD_GROUP_ID_PLACEHOLDER_03" }
          ]
        }
        {
          campaignId: "CAMPAIGN_ID_B_PLACEHOLDER"
          numberOfClones: 2
          cloneNames: ["CAMPAIGN_B_CLONE_PLACEHOLDER_01", "CAMPAIGN_B_CLONE_PLACEHOLDER_02"]
          campaignFlights: [
            {
              startDateInclusive: "2024-06-05T20:26:20.077Z",
              budgetInAdvertiserCurrency: 23000000.00
            }
          ]
        }
      ]
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

A successful response returns an ID (or list of IDs) that you can use to check the status of the cloning job.

```
{
  "data": {
    "campaignClonesCreate": {
      "data": [
        {
          "id": 21
        },
        {
          "id": 22
        }
      ],
      "userErrors": []
    }
  }
}

```

> **NOTE**: If you are cloning multiple campaigns, you will have multiple job IDs, one for each campaign being cloned.

To check the status of your campaign cloning jobs in GraphQL, use the `campaignCloneJobsProgress` query and include the job ID returned when you submitted the job. The following example demonstrates how you can retrieve the status of four jobs and, for each job, information about the source and the copies of the ad groups and campaigns that you are cloning.

```
query GetCampaignCloningStatusExample {
  campaignCloneProgresses(where: { id: { in: [21, 22] } }) {
    nodes {
      id
      status
      cloneCount
      sourceCampaign {
        id
      }
      jobs {
        totalCount
        nodes {
          id
          status
          progressPercentage
          cloneReport
          failureMessage
          cloneInfo {
            campaignClone {
              id
            }
            adGroupCloneMap {
              originalAdGroup {
                id
              }
              clonedAdGroup {
                id
              }
            }
          }
          failedAdGroups {
            adGroup {
              id
            }
            failureMessage
          }
        }
      }
    }
  }
}

```

### Clone a campaign with the REST API

To clone a campaign using the platform REST API, complete the following steps.

| Step | Task | Endpoint | Notes |
| --- | --- | --- | --- |
| 1 | Submit the cloning job. | POST /v3/campaign/clone | A successful response returns a reference ID that you can use to check the job progress. |
| 2 | (Optional) Check the status of the job. | GET /v3/campaign/clone/status/{referenceId} | Include the reference ID returned in the response after you submitted the job. |

To clone a campaign with the REST API, in a POST /v3/campaign/clone call, include the following:

1. The ID of the campaign you want to clone.
2. The name of the new campaign.
3. Set the `Version` value to `Kokai` if you're cloning a campaign in Solimar.

This request clones a campaign with all its data, including ad groups and flight information, but not its frequency settings. If you want to make any changes to the other settings, be sure to include them in your request.

```
{
  "CampaignId": "SOURCE_CAMPAIGN_ID_PLACEHOLDER",
  "CampaignName": "CLONED_CAMPAIGN_NAME_PLACEHOLDER",
  "Version": "Kokai"
}
```

A successful response returns a reference ID that you can use in a GET /v3/campaign/clone/status/{referenceId} call to check the status of the job.

#### Automatically opt cloned ad groups into marketplace

Cloning a campaign does not automatically opt in the cloned ad groups into the current inventory marketplace unless you set the `DefaultUseInventoryMarketPlace` property to `true`. This applies to all selected ad groups unless specified otherwise.

Here's what you need to know:

- Ad groups must be eligible to join the marketplace. For example, an ad group is ineligible if it's configured for the private market only.
- If you want to prevent an ad group from being automatically opted in, set its `useInventoryMarketPlace` property to `false` in the `selectedAdGroups` property.
- If no value is set for the `DefaultUseInventoryMarketPlace` property, the mutation defaults to the `isMarketplaceEnabledByDefault` property.

The following is a snippet of the `campaignClonesCreate` mutation shown in Clone campaigns with the GraphQL API. It illustrates how the first ad group will not be automatically opted into the marketplace because its `useInventoryMarketPlace` property is set to `false`. The other ad groups will be automatically opted in.

```
mutation {
  ...
        defaultUseInventoryMarketPlace: true
        selectedAdGroups: [
          {
            adGroupId: "ADGROUP_ID_PLACEHOLDER_01",
            useInventoryMarketPlace: false // This ad group will not be automatically opted into the marketplace.
          },
          {
            adGroupId: "ADGROUP_ID_PLACEHOLDER_02"
          },
          {
            adGroupId: "AD_GROUP_ID_PLACEHOLDER_03"
          }
        ]
      }
```

## FAQs

The following is a list of frequently asked questions about campaign cloning.

### Can I add new ad groups to campaign copies when cloning a campaign?

No. You can add ad groups only after the campaign copies are created.

### Are cloned ad groups automatically opted into my current marketplace?

No. Cloning a campaign does not automatically opt in the cloned ad groups into the current inventory marketplace unless you set the `DefaultUseInventoryMarketPlace` property to `true`. This applies to all selected ad groups unless specified otherwise. For details, see Automatically opt cloned ad groups into marketplace.

### Can I clone multiple campaigns?

Yes, but using only the GraphQL API. For details, see Clone campaigns with the GraphQL API.

### Can I make multiple copies of the same campaign?

Yes, but using only the GraphQL API. You can specify how many copies of a campaign you want to create. For details, see Clone campaigns with the GraphQL API.

### How long does it take to process a cloning job?

On average, the processing time for cloning a single campaign is 10 seconds. This also depends on the amount of data in the campaign being cloned. For example, the amount of ad groups, bid lists, bid lines, and so on can increase the processing time.

### Can I change the settings of the source campaign during the cloning process?

No. To make changes to an existing campaign that you cloned, use the `campaignUpdate` operation.

### Can I make changes to the campaign clones during the campaign cloning process?

Yes. However, there's a limit to the type of settings you can change. For details, see Campaign settings you can copy and modify.

### How do I make changes to all of the campaign clones at once?

Use the bulk campaign update operation. For details, see GraphQL API bulk operations.

### Is there a limit to how many campaigns I can clone?

You can clone up to 50 campaigns at once and create up to 1000 campaign copies at a time.

### Do I have to specify goals and channels when cloning campaigns?

No. If the campaign that you are trying to clone already has these properties set, they will be automatically copied.

### Can I change goals and channels when cloning campaigns?

Yes. To apply a different primary goal and channel when cloning campaigns, in a `campaignClonesCreate` mutation, include the `channel` and `primaryGoal` fields.

### Do I need to update budget settings for cloned Kokai campaigns?

All budgets are automatically updated to use the Kokai budgeting version and settings if you do either of the following:

- If you cloned your campaigns using GraphQL.
- If you cloned your campaigns using REST and set the `version` property to `Kokai`.

In these use cases, you do not need to run the `campaignBudgetSettingsUpdate` mutation to update the budget settings for the cloned campaigns. To upgrade campaigns with Solimar budgets, see Budget allocation.

### How do I add a new fee card to a new campaign clone?

Use the POST /v3/additionalfees endpoint.

### I see a duplicate audience with "- Copy" in its name. Where did it come from?

When cloning a campaign, the platform also clones the audience associated with each ad group that has Prism enabled. The cloned audience has the `- Copy` suffix appended to its name, such as `AUDIENCE_NAME_PLACEHOLDER - Copy`. This duplication ensures Prism is optimized for each ad group.
