# Deal Quality

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/PlatformDealQuality
- Category: Guides

---

# Deal Quality

As a buying party, you have access to view how The Trade Desk monitors and tracks quality across your commitment and endeavor deals. Your deal quality score measurements follow a 100-point scale that reflects how your deal compares with the open market. The deal quality score considers many factors such as price competitiveness, inventory uniqueness, addressability, and signal fidelity. Afterward, it compares the quality to similar inventory across non-deal options, such as the open market or the Sellers and Publishers 500+ (SP500+).

You can use Deal Quality score to do the following:

*   Evaluate new proposals before accepting.
*   Decide which deals to prioritize.
*   Spot underperforming deals mid-flight and evaluate which deals are worth targeting.
*   Support deal terms renegotiation conversations.

> **TIP**: Deal Quality score is a useful metric to determine which deals to [prioritize](#priority).

## 

Quality Score[](#score)

The deal quality score represents how your deal compares to market averages. If your deal quality score is at 50, then it's equal to the open market. The following table shows a breakdown of each grade and range.

| Score Range | Grade | Description |
| Above 60 | Good | A score greater than 60 signifies a strong negotiation to buy this inventory. The deal scores well across quality metrics compared to similar inventory in the marketplace. |
| 40 to 60 | Average | A score between 40 and 60 represents an average deal. This deal performs similarly to what's already available through marketplace options. It may not offer meaningful added value. |
| Below 40 | Poor | A score less than 40 shows that this deal scores poorly across multiple quality metrics. It may be overpriced, offer less support for audience targeting or weaker signal fidelity, or overlap with inventory already available through marketplace options. |

> **NOTE**: Not all deals with a low deal quality score are underperforming. Sometimes, deals can perform well, but have a low deal quality score. For example, a deal that overprices inventory but brings a lot of audience value towards your KPIs.

### 

Quality Metrics[](#score-metrics)

Each component of Deal Quality score tells you something different about the deal’s value. Use the following table to evaluate whether a deal meets your expectations.

| Metric | Definition |
| Inventory exclusivity | Measures whether the inventory in the deal is only available through private deals, not the open market. High inventory exclusivity means the deal gives you access to inventory that isn't available through the open market. |
| Price competitiveness | Measures how the deal's CPM compares to what’s typically paid for similar inventory when bought through marketplace options. If you negotiated this deal for better pricing, this score shows whether it's delivering on that value. |
| Addressability | Shows what proportion of avails in the deal can be linked to a user or household ID in an identity graph. A deal with high addressibility supports targeting and ID-based measurement. |
| Signal fidelity | Shows how much detail this deal provides about the inventory sent. High signal fidelity means you'll be more likely to know exactly what you bought when reviewing reports, such as which site or show your ad ran on.  
**NOTE**: Having clearer signals can also improve targeting and help Koa optimize delivery. |
| Relevance | Shows how closely the users reachable through this deal match your ideal audience based on your campaign seed. High relevance means the deal is reaching users that match your seed or target audience. |
| Contribution to campaign performance | Records how your deal performs against your campaign KPIs compared to other inventory. A high contribution to campaign performance means the deal drives stronger results than your other inventory. |

### 

Deal Quality Scenarios[](#scenarios)

The Deal Quality score is a signal, not a rule. Here are some common situations you might encounter and how you might think about them in context.

| Scenario | Considerations | Possible Actions |
| The deal has 0% inventory exclusivity but is strong on other factors. | Unless exclusivity is the reason you agreed to the deal, you should continue the deal. | Examine the price competitiveness and addressability metrics to guide your decision. |
| The deal has high inventory exclusivity but you find it expensive. | You may be paying a premium for the exclusive inventory. If exclusivity was your goal, this could still make sense. | Look up the inventory exclusivity to confirm it's near 100%. If so, the deal can justify a lower Deal Quality score. |
| The deal has low price competitiveness but includes a seller-applied audience. | You're likely paying extra for the applied audience. | Check contribution to campaign performance and average relevance. If either metric is higher than your other inventory, the audience might be worth the premium price. If not, ask the seller to remove their audience to apply your own audience targeting. |
| The deal has a lower signal fidelity or addressability than marketplace options. | You lack some information to optimize or measure effectively through this deal. In some cases, intermediaries could be dropping the signals they receive from the publisher, so even if the source inventory is strong, those dropped details might not reach you. | If the same inventory is accessible through marketplace options, with stronger signals, you should consider targeting the open marketplace. |

### 

Calculation Methodology[](#calculate)

Deal Quality score is calculated by comparing the actual avails coming through a deal to other similar inventory available in the open marketplace.

The following table describes the Deal Quality score calculation process.

| Step | Task | Description |
| **1** | Analyze actual avails. | The system analyzes the actual avails coming through the deal (not just what the seller declared) to identify similar inventory in the open market. |
| **2** | Find comparable avails. | The system identifies "like-for-like" marketplace inventory based on dimensions like publisher, geo, skippability, placement type, and more. |
| **3** | Score each factor. | Each deal is evaluated across four core metrics: Inventory exclusivity, price competitiveness, addressability, and signal fidelity. For details, see [Quality Metrics](#score-metrics). |
| **4** | Combine the metrics into a final overall score. | The platform applies weighted averaging to calculate the final Deal Quality score ranging from 0–100. For details, see [Quality Score](#score). |

## 

Prioritize Deals[](#priority)

Deal prioritization enables you to allocate spend towards certain deals first, before spending on other deals. By prioritizing high-quality deals with a high Deal Quality score above 60, you can allocate spend towards more valuable audiences and improve overall campaign performance.

> **NOTE**: By default, deals with media spend goals use a dynamic prioritization system that automatically adjusts deal prioritization based on how it’s pacing. Underpacing deals follow more aggressive prioritization until pacing improves, while commitment deals have priority over endeavor deals.

To prioritize a deal, you can use the `inventoryDealsPrioritizationSet` or `inventoryDealPrioritizationAdvertiserOverrideSet` mutations, depending on the level of granularity you want. The following table outlines the differences.

| Mutation | Scope | Usage | Notes |
| `inventoryDealsPrioritizationSet` | Global (all advertisers in the deal) | Sets deal prioritization at the global level. | This is the default method. |
| `inventoryDealPrioritizationAdvertiserOverrideSet` | Advertiser-level | Sets prioritization for individual advertisers within a deal. | More granular control but more setup. You must set global prioritization off. |

By default, all ad groups follow the global prioritization setting to equally consider all advertisers. To prioritize deals by specific advertisers, you must first disable global deal prioritization. Then, add overrides for each advertiser.

When you use the `inventoryDealsPrioritizationSet` mutation, this modifies the global prioritization for all advertisers included in the deal. The following example shows how to disable global deal prioritization.

mutation {

  inventoryDealsPrioritizationSet(input: {

    inventoryDealsWithTargetingAssociated: \[

      {

        dealId: "DEAL\_ID\_PLACEHOLDER"

      }

    \],

    isPrioritized: false

  }) {

   userErrors {

      message

    }

  }

}

The following example shows how to override prioritization to add a specific advertiser.

mutation {

  inventoryDealPrioritizationAdvertiserOverrideSet(input: {

    advertiserId: "ADVERTISER\_ID\_PLACEHOLDER"

    dealId: "DEAL\_ID\_PLACEHOLDER"

    isPrioritized: true

  }) {

   userErrors {

      message

    }

  }

}