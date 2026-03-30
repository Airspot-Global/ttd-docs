# Trading Modes (Closed Beta)

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/TradingModes
- Category: Guides

---

# Trading Modes (Closed Beta)

> **IMPORTANT**: This feature is in closed beta and subject to change as we improve its performance. For details about participating in the closed beta, contact your Technical Account Manager.

Trading Modes determine how bidding, pacing, and optimization are managed between manual user controls and AI-powered automation. You can choose between the following two modes:

*   **Performance Mode** (recommended): Automatically turns on premium performance [features](#features) and relies on Koa, the AI that powers the platform, to prioritize the highest-value impressions and optimize bidding, pacing, and other campaign decisions based on your inputs and goals, which minimizes the need for manual adjustments and while maximizing campaign performance.
*   **Control Mode**: This mode enables you to manually select and configure individual features and campaign settings manually, while still giving you the option to use AI-powered optimizations.

Here's what you need to know about Trading Modes:

*   Most KPI-driving features are enabled by default.
*   Trading Modes doesn't affect budget allocation settings during closed beta, although we recommend using a fully fluid budget for best results.
*   To get started, we recommend [creating](#create) new campaigns with Performance Mode.
*   Performance Mode combines the costs of media, data, and fee-based features into a single impression cost metric, making it the most cost-efficient option for high-performance campaigns. For details, see [Reporting for Trading Modes](/v3/portal/api/doc/TradingModesREDS).

## 

Prerequisites[](#prereqs)

To be able to use Performance Mode, the following prerequisites must be met:

 The Terms of Service is accepted in the platform UI.  
 [Audience Unlimited](/v3/portal/api/doc/AudienceUnlimited) is enabled.  

Here's what you need to know about these prerequisites:

*   If any of these prerequisites are not met, the default trading mode will be Control Mode.
*   As part of the closed beta, you have complimentary access to Audience Unlimited for one year, so you can start using Performance Mode right away.

## 

Features Controlled by Trading Modes[](#features)

Here's what you need to know about the features controlled by Trading Modes:

*   In Performance Mode, all KPI-driving features are always on, giving you the highest level of automation and efficiency.
*   Control Mode is available if you need to fine-tune individual settings for goals beyond pure performance.
*   The cost of premium fee-based features like Audience Unlimited, Predictive Clearing, Quality Alliance, and Prism, is consolidated into a single reporting impression cost metric in Performance Mode. For details, see [Reporting for Trading Modes](/v3/portal/api/doc/TradingModesREDS). In Control Mode, these fee-based features have their own separate reporting cost metrics.

The following table lists the features affected by Trading Modes and how they are applied under each mode.

| Feature | Description | Performance Mode | Control Mode | Notes |
| [Audience Unlimited](/v3/portal/api/doc/AudienceUnlimited) | Accesses premium data segments at a predictable cost to simplify planning and boost performance. | Always on (Full tier) | Configurable, available options include the following:  

*   `FULL` (default)
*   `LITE`
*   `NONE`

 | 

*   This fee-based feature (complimentary for 12 months in the closed beta) is required for Performance Mode.
*   In Control Mode, additional platform rate fees apply (3.3% or 4.4% of spend). For details, see [Audience Unlimited Tiers](/v3/portal/api/doc/AudienceUnlimited#au-tiers).
*   Measurement is included with Audience Unlimited with participating data providers.

 |
| [Predictive Clearing](/v3/portal/api/doc/PredictiveClearing) | Adjusts bids in real time to market conditions, lowering CPMs while maintaining results. | Always on | On by default, configurable | This is a fee-based feature. |
| [Prism](/v3/portal/api/doc/Prism) | Filters out low-value impressions to avoid wasteful bidding. | Always on | On by default, configurable | Prism might not be available for advertisers working with sensitive categories (unless Prism appears for them as an option in the platform UI). |
| [Identity Alliance](/v3/portal/api/doc/CrossDeviceTargeting) | Enhances cross-device targeting and measurement, improving campaign efficiency and performance. | Always on | On by default, configurable | This is a fee-based feature. |
| Quality Alliance | Prioritizes high-quality impressions to improve viewability and completion rates. | Always on | On by default, configurable | This is a fee-based feature. |
| [Koa Optimizations](/v3/portal/api/doc/KoaOptimizationsTM) | Uses AI to optimize bids and budgets for stronger results with less manual effort. | Always on (all dimensions) | Always on for the `Geography` and `Publisher` dimensions, configurable for all other dimensions | The `Publisher` dimension replaced `Site`. |
| [Price Optimizations](#price-optimizations) | Affects how Koa manages bid prices, volume control, and pacing for your campaigns. | Always on (`PERFORMANCE_DRIVEN`) | Configurable, available options include the following:

*   `PERFORMANCE_DRIVEN` (default)
*   `PRICE_DRIVEN`
*   `PRIORITY_DRIVEN`

 | By default, this feature automatically optimizes bidding and pacing. |

## 

Price Optimization Options[](#price-optimizations)

The price optimization setting affects how Koa manages bid prices, volume control, and pacing for your campaigns. The following table lists the available price optimization options.

| Price Optimization Option | Trading Mode | Use Case | Description |
| `PERFORMANCE_DRIVEN` (default) | Performance Mode, Control Mode | Hands-free optimization and full automation. | The system automatically does the following:

*   Optimizes bidding and pacing adjustments.
*   Adjusts CPMs to maximize performance, automatically lowering bids when inventory is plentiful and raising them to avoid underdelivery.

This is the default and recommended option. No manual setup or monitoring is required. |
| `PRICE_DRIVEN` | Control Mode | Efficient CPMs with a cautious bidding strategy. | The system won’t exceed the total bid calculated from your base bid multiplied by your applicable bid factors.  
**IMPORTANT**: This option might limit your ability to deliver in full when scale is limited. |
| `PRIORITY_DRIVEN` | Control Mode | Waterfall-style ad group spend allocation. | You set spend priorities for your ad groups, and the system directs more spend toward the high-priority groups before others. Your base bid and bid factors determine the final average CPM.  
**IMPORTANT**: This option might limit your ability to deliver in full when scale is limited. |

## 

Get Started with Trading Modes[](#upgrade)

> **IMPORTANT**: Make sure the `TTD-Gql-Beta` header includes `kokai-campaign-trading-mode` before making calls.

To get started with Trading Modes, create a new campaign and set the trading mode to either Performance Mode or Control Mode. Here's what you need to know about Trading Modes for campaigns:

*   You cannot change the trading mode of an existing campaign.
*   The default trading mode for creating and cloning campaigns is Performance Mode.
*   If you create a campaign and do not have Audience Unlimited, the default trading mode is Control Mode.

The following table lists all tasks related to Trading Modes.

| Task | Operation |
| [Create](#create) a new campaign that uses Trading Modes. | `campaignCreate` mutation |
| [Retrieve](#retrieve) the trading mode of an existing campaign. | `campaign` query |
| [Clone](#clone) an existing campaign. | `campaignClonesCreate` mutation |
| Set the [price optimization](#set-price-optimizations) option for a campaign. | `campaignBudgetSettingsUpdate` mutation |

### 

Create a New Campaign and Set the Trading Mode[](#create)

To set the trading mode for a new campaign you create, use the GraphQL `campaignCreate` mutation and set the `tradingModeSettingsInput` field to either `PERFORMANCE` (recommended) or `CONTROL`. For full details and examples, see [Campaign Create](/v3/portal/api/doc/CampaignCreate).

mutation {

  campaignCreate(

    input: {

      tradingModeSettingsInput: { mode: PERFORMANCE }

      advertiserId: "ADVERTISER\_ID\_PLACEHOLDER"

      primaryGoal: { maximizeReach: true }

      flights: \[

        {

          budgetInAdvertiserCurrency: 1200000

          endDateExclusiveUTC: "2025-12-15T00:00:00"

          startDateInclusiveUTC: "2026-01-15T00:00:00"

        }

      \]

      name: "CAMPAIGN\_NAME\_PLACEHOLDER"

      primaryChannel: DISPLAY

      seedId: "SEED\_ID\_PLACEHOLDER"

    }

  ) {

    userErrors {

      field

      message

    }

    data {

      id

      name

      budget {

        total

      }

    }

  }

}

### 

Retrieve the Trading Mode of a Campaign[](#retrieve)

To retrieve the trading mode of a campaign, in a GraphQL `campaign` query, include the `tradingModeDetails.mode` field.

query GetCampaignTradingMode {

  campaign(id: "CAMPAIGN\_ID\_PLACEHOLDER") {

    tradingModeDetails {

      mode

      audienceUnlimitedTier

      isEligibleForPerformanceTradingMode

    }

  }

}

### 

Set the Price Optimization Setting for a Campaign[](#set-price-optimizations)

To set the price optimization, use the GraphQL `campaignBudgetSettingsUpdate` mutation and set the `priceOptimizationType` field to `PERFORMANCE_DRIVEN` (recommended) or any other [option](#price-optimizations) you want to use.

mutation {

  campaignBudgetSettingsUpdate(

    input: {

        campaignId: "CAMPAIGN\_ID\_PLACEHOLDER"

        priceOptimizationType: PERFORMANCE\_DRIVEN

    }

  ) {

    data {

      campaign {

        id            

        priceOptimizationType

      }

    }

    userErrors {

      field

      message

    }

  }

}

### 

Clone an Existing Campaign and Set the Trading Mode[](#clone)

Here's what you need to know about Trading Modes during the campaign cloning process:

*   You can set the trading mode during the campaign [cloning process](/v3/portal/api/doc/CampaignCloning).
*   If you don't set the trading during the campaign cloning process, the trading mode of the campaign clone is set to Performance.
*   If you clone a campaign that does not have a trading mode, the new campaign trading mode is set to Performance.

To clone an existing campaign and set the trading mode, use the `campaignClonesCreate` mutation. This submits a job that starts the cloning process. For details, see [Clone Campaigns](/v3/portal/api/doc/CampaignCloning).

mutation {

  campaignClonesCreate(

    input: {

      campaignCloneData: \[

        {

          campaignId: "CAMPAIGN\_ID\_A\_PLACEHOLDER"

          numberOfClones: 1

          defaultUseInventoryMarketPlace: true

          tradingModeSettingsInput: { mode: PERFORMANCE }

          cloneNames: \["CAMPAIGN\_A\_CLONE\_PLACEHOLDER"\]

        }

      \]

    }

  ) {

    data {

      id

    }

    userErrors {

      message

      field

    }

  }

}

## 

FAQs[](#faqs)

The following are frequently asked questions about Trading Modes.

### 

Which trading mode should I start with?

Try Performance Mode first. It's ideal for advertisers who want to enhance their current strategy with AI and drive stronger outcomes without the need to manage every campaign detail.

### 

How does Trading Modes affect my budget?

Trading Modes does not affect how you allocate your budgets to your campaigns.

For the best results in Performance Mode, The Trade Desk recommends setting up a fully fluid budget. This enables the platform to automatically direct spend to the best-performing ad groups and bid on the most valuable impressions. With this setup, you’ll have the best chance to spend your full budget and achieve your campaign goals and KPIs. For details about fluid budgets, see the [Budget Allocation](/v3/portal/api/doc/CampaignBudgets).

If you set the [price optimization option](#price-optimizations) to `PRIORITY_DRIVEN`, ad group spend priorities use waterfall allocation.

### 

What happens if I clone an existing campaign that never had a Trading Mode?

The trading mode of your new campaign will be set to Control Mode.

### 

What happens if I clone an existing campaign in Performance Mode and no longer have Audience Unlimited?

The trading mode for your campaign will be set to Control Mode with all other applicable default settings turned on.

### 

What happens when I apply my own bid factors in campaigns with a trading mode?

If you apply a bid factor to a specific dimension, the platform applies only the bid factor you set and does not apply a Koa bid factor. For details about bid factors, see [Bid Lists](/v3/portal/api/doc/BidList).

### 

Does Performance Mode turn on Quality Alliance?

Not during the closed beta. In future releases, however, Quality Alliance will be turned on after you set a campaign to Performance Mode. Stay tuned for [future announcements](/v3/portal/api/doc/ReleaseNotes)!

### 

Are Trading Modes available in legacy versions of the platform?

No. Trading Modes is available only for Kokai campaigns.

### 

Can I set the trading mode for an existing campaign?

Yes, however, you can set the trading mode of existing campaigns only to Control Mode. If an existing campaign has a Trading Mode, you cannot set a different Trading Mode.

To set the trading mode for an existing campaign, use the GraphQL `campaignUpdate` mutation and set the `tradingModeSettingsInput` field to `CONTROL`.

> **TIP**: You can set the trading mode for multiple campaigns at once by running the `campaignUpdate` mutation as a [bulk operation](/v3/portal/api/doc/GqlBulkOperations).

mutation {

  campaignUpdate(

    input: {

      id: "CAMPAIGN\_ID\_PLACEHOLDER"

      tradingModeSettingsInput: { mode: CONTROL }

    }

  ) {

    data {

      tradingModeDetails {

        audienceUnlimitedTier

        mode

      }

    }

    errors {

      ... on MutationError {

        \_\_typename

        message

        field

      }

    }

  }

}