# Create campaigns

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/CampaignCreate
- Retrieved: 2026-11-14
- Category: Guides

---

# Create campaigns

This guide explains how to create a single campaign from scratch, but, depending on your needs, you can also clone existing campaigns. See also Campaign creation workflows.

To define your advertising strategies in the platform, you need to create a campaign with a specialized seed, clear and precise goals, and a channel in which you want to advertise. Here's what you need to know about the campaign creation process:

- You can create a single campaign or multiple campaigns in one call.
- To create individual campaigns, you can use either API: GraphQL or REST.
- To create multiple campaigns in bulk, you must use GraphQL. This option is best suited for creating over 100 campaigns at once.
- The requirements are the same for creating single campaigns or multiple campaigns in bulk—regardless of which API you use.

## Campaign requirements

To send a successful create request, you must provide your advertiser ID, the name of your campaign, and set the campaign primary goal and channel. However, there are other factors and properties you need to consider to create a successful campaign and bid on the most valuable impressions. See also Campaign success checklist.

Here's what you need to know about creating campaigns:

- You can have your default seed automatically attached, or create a designated seed for your campaign (recommended) and attach it using the `SeedId` property in either API.
- For campaign goals, only the primary goal is required. Secondary and tertiary goals are optional and hierarchically interdependent.
- Each campaign requires at least one flight with a budget and a start date. For details on how to allocate the flight budget to its ad groups, see Budget allocation.
- The `ChannelId` value for each ad group in this campaign must match the campaign channel. The ad group creative type must match the selected channel.
- Political advertising, live events, and conversion-focused campaigns require additional properties to be set. For details, see Political advertising, Live event campaigns, and Conversion reporting columns.

> **TIP**: To save time and ensure consistency across ad groups, you can include the advertiser’s default bid lists in campaigns and further propagate them to ad groups. For details, see Default bid lists.

### Campaign goals

The primary campaign goal is the main KPI toward which the platform optimizes performance. Secondary and tertiary goals provide additional KPIs for measurement. In Solimar-budgeted campaigns, they also rank ad groups when AutoAllocator and Auto Prioritization are turned on.

Here’s what you need to know about campaign goals:

- You can set up to three goals for a campaign. The `PrimaryGoal` is required, while the `SecondaryGoal` and `TertiaryGoal` are optional.
- All three goals are hierarchically interdependent. For example, to set a tertiary goal, you must first set the secondary one.
- Ad groups initially inherit only the `PrimaryGoal` from their parent campaign and may have their own goals.
- All goal properties are mutually exclusive. In other words, in each goal object (`PrimaryGoal`, `SecondaryGoal`, and `TertiaryGoal`), you can include only _one_ goal (property).
- Some goals require a target set, which is the amount (in the advertiser's currency) or percentage.

For a complete list of goals that you can set in your campaign, see Goals and KPIs.

### Conversion reporting columns

A conversion reporting column is the mapping of conversion tracking tags, or conversion pixels, to reporting columns. Here's what you need to know about conversion reporting columns:

- If your campaign is _not_ conversion-focused, send the `CampaignConversionReportingColumns` object empty.
- You can include up to five reporting columns.
- You can always update your reporting columns later, but new reports will not contain retroactive metrics for these conversions. If you assign different conversions to a previously-used reporting column, your long-term roll-up reports could be misleading.

To add a conversion reporting column to your campaign, include the `CampaignConversionReportingColumns` property with at least the following two fields.

| Property | Notes |
| --- | --- |
| `TrackingTagId` | The tracking tag to which the ID belongs must have a type considered to be a conversion (for details, see the Tracking tag and Tracking tag type APIs). |
| `ReportingColumnId` | Metrics about this conversion will appear in reports under this reporting column. Only one tracking tag ID and cross-device attribution model ID may be mapped to each column within a campaign. For details, see Set up cross-device attribution for a conversion campaign. |

## GraphQL mutation example

The following `campaignCreate` GraphQL mutation illustrates how to create a Kokai campaign with a Kokai budget version.

```
mutation {
  campaignCreate(
    input: {
      advertiserId: "ADVERTISER_ID_PLACEHOLDER"
      primaryGoal: { maximizeReach: true }
      campaignConversionReportingColumns: {}
      flights: {
        budgetInAdvertiserCurrency: 1200000
        endDateExclusiveUTC: "2025-02-15T00:00:00"
        startDateInclusiveUTC: "2025-03-15T00:00:00"
      }
      name: "CAMPAIGN_NAME_PLACEHOLDER"
      primaryChannel: DISPLAY
      seedId: "SEED_ID_PLACEHOLDER"
    }
  ) {
    userErrors {
      field
      message
    }
    data {
      id
      name
      version
      budget {
        version
        total
      }
    }
  }
}
```

## REST request example

Here's what you need to know about using the REST API to create campaigns:

- You must set the `Version` property value to `Kokai`, otherwise you will create a Solimar campaign.
- If your campaign is not conversion-focused, send the `CampaignConversionReportingColumns` object array empty. For details, see Conversion reporting columns.

Here's an example of a POST /v3/campaign request body for a campaign that has multiple goals.

```
{
    "AdvertiserId": "ADVERTISER_ID_PLACEHOLDER",
    "CampaignName": "CAMPAIGN_NAME_PLACEHOLDER",
    "Version": "Kokai",
    "SeedId": "SEED_ID_PLACEHOLDER",
    "Budget": {
        "Amount": 1200000,
        "CurrencyCode": "USD"
    },
    "StartDate": "2024-09-15T00:00:00",
    "EndDate": "2024-08-15T00:00:00",
    "CampaignConversionReportingColumns": [],
    "PrimaryGoal": {
        "MaximizeReach": true
    },
    "SecondaryGoal": {
        "MaximizeLtvIncrementalReach": true
    },
    "TertiaryGoal": {
        "VCPMInAdvertiserCurrency": {
            "Amount": 28.00,
            "CurrencyCode": "USD"
        }
    },
    "PrimaryChannel": "Display",
    "IncludeDefaultsFromAdvertiser": true
}
```

## FAQs

The following is a list of frequently asked questions about creating campaigns.

### How do I update a campaign after I create it?

Use the GraphQL `campaignUpdate` operation.

### When creating a Kokai campaign, how do I set the budgeting version to Kokai?

In GraphQL, campaign and budget versions are set to `Kokai` by default. If you are using the REST API, just set the campaign `Version` property to `Kokai`, and the `BudgetingVersion` value is automatically set to `Kokai` and returned in the response.

### How are ad group KPIs set when there are multiple campaign goals?

The primary campaign goal becomes the default KPI for all ad groups in the campaign.

### How do I use the REST API to opt my campaign out of the Sellers and Publishers Marketplace 500+?

In a POST /v3/campaign call, set the `MarketplaceOptOut` value to `true`.
