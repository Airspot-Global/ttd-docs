# Koa bidding strategy

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/KoaBiddingStrategy
- Retrieved: 2026-11-14
- Category: Guides

---

# Koa bidding strategy

Koa bidding strategy operates at the campaign level and determines how Koa balances performance and spend across your ad groups. By default, Koa maximizes performance while prioritizing full budget delivery. If your campaign has different spending goals, you can switch to CPM efficiency or waterfall allocation instead.

> **NOTE**: After you create your campaign, you can decide whether to change your bidding strategy or keep the default `PERFORMANCE` value. If you keep the default value, proceed to the next steps.

## Koa bidding strategy types

The following table describes the available Koa bidding strategies (the `koaBiddingStrategy.type` values), including the use case, bidding behavior, and tradeoffs for each strategy.

| Value | Best for | Description | Notes |
| --- | --- | --- | --- |
| `PERFORMANCE` (default, recommended) | Hands-free optimization with full budget delivery as the priority. | Koa dynamically adjusts bids to maximize performance while keeping the campaign on track to deliver its full budget. If inventory is scarce, Koa might bid CPMs closer to your max bid to improve win rates and secure enough impressions. | Average CPMs might rise to meet delivery targets, especially in ad groups with limited inventory. |
| `EFFICIENCY` | CPM efficiency with a conservative bidding approach. | Koa finds high-value inventory and optimizes toward it, but caps bid prices at the base bid price multiplied by the bid factor. | - Do not use this strategy if full budget delivery is a priority. - If the base bid or bid factors are set too low, the campaign might underspend. To maintain budget delivery, consider increasing bid pricing. |
| `PRIORITY` | Waterfall-style spend allocation across ad groups. | Instead of using value weights, you assign strict spend priorities to your ad groups, and Koa prioritizes spend accordingly. When a higher-priority ad group can no longer spend, spend flows to the next group in priority order. Your base bid and bid factors determine the final average CPM. | - Koa dynamically adjusts bids based on value, but is constrained to maintain the average CPM at the base bid multiplied by bid factors. - This changes the behavior of the spend priority setting from a value weight to a strict spending order. - If the base bid or bid factors are set too low, the campaign might underspend. To maintain budget delivery, consider increasing bid pricing. |

## Manage your Koa bidding strategy

> **NOTE**: Accounts that participated in a closed beta with similar features might have an earlier version of Koa bidding strategy. To check your version and update it, see Update your Koa bidding strategy version after closed beta.

The following table lists the tasks for retrieving and updating your bidding strategy.

| Task | Operation | Notes |
| --- | --- | --- |
| Check the current bidding strategy for a campaign. | `campaign` query | None. |
| Update or change the bidding strategy for a campaign. | `campaignKoaBiddingStrategyUpdate` mutation | - You can change the bidding strategy at any time after campaign creation. - If you change the bidding strategy during an active campaign flight, allow up to 24 hours for Koa to generate new bid factors. |

### Check the Koa bidding strategy for a campaign

Before adjusting mid-flight settings, you might want to confirm which bidding strategy your campaign is currently using. To check the bidding strategy for a campaign, use the `campaign` query and include the `koaBiddingStrategy.type` field.

The following `campaign` query example shows how to check the current bidding strategy for a campaign.

```
query GetCampaignBiddingStrategyExample {
  campaign(id: "CAMPAIGN_ID_PLACEHOLDER") {
    koaBiddingStrategy {
      type
    }
  }
}
```

A successful response returns the bidding strategy as the `type` value.

### Update the Koa bidding strategy for a campaign

The recommended Koa bidding strategy is `PERFORMANCE`, which prioritizes budget delivery. If you have different spending goals and want to prioritize CPM efficiency or use the waterfall allocation method, you can change the bidding strategy type. For details on the different strategies and `type` values, see Koa bidding strategy types.

To set or change the bidding strategy for a campaign, use the `campaignKoaBiddingStrategyUpdate` mutation and specify the strategy `type` field.

> **IMPORTANT**: If you change the bidding strategy during an active campaign flight, allow up to 24 hours for Koa to generate new bid factors.

The following `campaignKoaBiddingStrategyUpdate` mutation example shows how to change the bidding strategy for a campaign.

```
mutation {
  campaignKoaBiddingStrategyUpdate(
    input: {
      campaignId: "CAMPAIGN_ID_PLACEHOLDER"
      type: PERFORMANCE
    }
  ) {
    data {
      koaBiddingStrategy {
        type
      }
    }
    errors {
      ... on MutationError {
        field
        message
      }
    }
  }
}
```

A successful response returns the updated `koaBiddingStrategy` object with the new `type` value.

## Update your Koa bidding strategy version after closed beta

If you participated in a closed beta that relates to price optimizations or spend allocations, you might need to update the Koa bidding strategy to the current available version. Here's what you need to know about updating legacy Koa bidding strategy versions:

- Different campaigns can have different versions depending on which campaigns were opted into the beta features.
- New campaigns you create automatically use the current version and release state.
- If your campaign was using a version that is no longer available, the system automatically migrated it to use the latest version and release state.
- If you have multiple campaigns with different versions and release states, you can migrate them in bulk using bulk operations.

The following table lists the tasks for retrieving the latest version and release state of Koa bidding strategies and updating your campaign to the latest version.

| Task | Operation |
| --- | --- |
| Get the available bidding strategies, their release state, and version number for an advertiser. | `advertiser` query |
| Check the current release state and version number of the bidding strategy for a campaign. | `campaign` query |
| Update the bidding strategy to the latest version. | `campaignKoaBiddingStrategyUpdate` mutation |

### Get available bidding strategies

If your campaign used a previous spend allocation method that was in closed beta, you can check to see which Koa bidding strategy release state and version number your campaign is currently using.

> **TIP**: To check multiple campaigns at once, use bulk operations.

To get the list of bidding strategies available for your advertiser, use the `advertiser` query and include the `availableOptions` field.

The following `advertiser` query example shows how to get all bidding strategies available for your advertiser.

```
query GetAvailableBiddingStrategiesExample {
  advertiser(id: "ADVERTISER_ID_PLACEHOLDER") {
    koaBiddingStrategy {
      availableOptions {
        type
        releaseState
        version
      }
    }
  }
}
```

A successful response returns the current release state and version number for Koa bidding strategy. Make sure your campaigns are using the current release state and version of the bidding strategy. For details, see Check the Koa bidding strategy version and release state for a campaign.

### Check the Koa bidding strategy version and release state for a campaign

After you get the current release state and version for Koa bidding strategy, you might need to check to see which campaigns have the latest version and release. To check the current bidding strategy for a campaign, use the `campaign` query and include the release state and version number.

The following `campaign` query example shows how to check the current bidding strategy for a campaign.

```
query GetCampaignBiddingStrategyExample {
  campaign(id: "CAMPAIGN_ID_PLACEHOLDER") {
    koaBiddingStrategy {
      type
      releaseState
      version
    }
  }
}
```

If the response returns a release state and version number that isn't up-to-date, use the `campaignKoaBiddingStrategyUpdate` mutation to update the bidding strategy for a campaign.

### Update the bidding strategy version for a campaign

If a campaign has a legacy version of the Koa bidding strategy, you might need to change the release state and version number to use the current available version. To set or change the bidding strategy for a campaign, use the `campaignKoaBiddingStrategyUpdate` mutation and specify the strategy `type` field.

> **IMPORTANT**: If you change the bidding strategy during an active campaign flight, allow up to 24 hours for Koa to generate new bid factors.

The following `campaignKoaBiddingStrategyUpdate` mutation example shows how to set the bidding strategy for a campaign.

```
mutation {
  campaignKoaBiddingStrategyUpdate(
    input: {
      campaignId: "CAMPAIGN_ID_PLACEHOLDER"
      type: PERFORMANCE
      releaseState: GA
      version: VERSION_NUMBER_PLACEHOLDER
    }
  ) {
    data {
      koaBiddingStrategy {
        type
      }
    }
    errors {
      ... on MutationError {
        field
        message
      }
    }
  }
}
```

## Next steps

After you decide which bidding strategy you want to use for your campaign, do either of the following:

- If you haven't finished setting up your campaign, proceed to Campaigns.
- If your campaign setup is complete, you can either set up your targeting settings or ad groups.

## FAQs

The following is a list of commonly asked questions about Koa bidding strategy.

### Can I change the bidding strategy after the campaign starts?

Yes. You can change the bidding strategy at any time. Be sure to allow up to 24 hours for Koa to generate new bid factors.

### How does the priority strategy affect my spend priority setting in budget allocation?

If you set the Koa bidding strategy to `PRIORITY`, the spend priority setting in budget allocation changes from a value weight to a strict spending order. A value weight influences how the platform values impressions, while a strict spending order creates waterfall allocation where higher-priority ad groups spend before lower-priority ones.

### What's the difference between Koa bidding strategy and Koa Optimizations?

Koa bidding strategy operates at the campaign level while Koa Optimizations works at the ad group level. Koa bidding strategy specifies how Koa balances performance, delivery, and CPM efficiency across your campaign. Koa Optimizations is the bid factors that Koa automatically generates based on the bidding strategy you set, the decision power score, the inventory you're targeting, and other campaign signals.

### Can I use bidding strategy with impression budget campaigns?

Yes. Impression budget campaigns are compatible with all bidding strategies. New impression budget campaigns default to `PERFORMANCE`. To prioritize stable CPMs over full budget delivery, use the `PRIORITY` bidding strategy. This strategy enables the platform to calculate CPMs through your base bid and bid factors, which often produce more predictable results for impression budget campaigns.
