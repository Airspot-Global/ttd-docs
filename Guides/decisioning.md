# Deal Decisioning

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/PlatformDealNonDecisioned
- Category: Guides

---

# Deal Decisioning

Deals can have two modes with decisioning and without decisioning. By default, all deals start in the decisioning mode which adds Kokai features to support and manage the deal. After you have accepted a deal as a buying party, all newly created ad groups are set to decisioned mode and support Koa features such as audience targeting and other optimizations.

> **NOTE**: Non-decisioning disables certain features and is only available to fixed-price commitment deals. For details, see [Run Fixed-Price Commitment Deals](#pg).

The following table compares the two decisioning modes, Decisioned Mode and Non-Decisioned Mode.

| Comparison Aspect | Decisioned Mode (Optimized) | Non-Decisioned Mode (Traditional PG) |
| Definition | Run fixed-price commitments with audience targeting, bid factors, and Koa optimizations. The Trade Desk selects the best impressions to meet committed spend. | Run fixed-price commitments without decisioning. Every impression is purchased at a fixed price, with no optimization applied. |
| Deal types supported | Commitment and endeavor deals. | Fixed-price commitment deals only. |
| Default? | Yes, all new deals and ad groups start in decisioned mode. | No, must be switched manually. For details, see [Run Fixed Price Commitment Deals](#pg). |
| Benefits | Smarter delivery, better performance, access to optimization levers | Lower platform fee (no standard decisioning fee) |
| Requirements | Audience targeting, bid factors, or other optimization features must be enabled. | No targeting, bid factors, or optimization features can be applied. |
| Downsides | A decisioning fee applies per feature. | No access to Koa features (audience targeting, optimizations, reporting enhancements) |

## 

Run Fixed-Price Commitment Deals[](#pg)

Decisioning is part of most deals, and can only be turned off if you have a fixed-price commitment deal. If you choose to not apply decisioning, all Koa related features are automatically off.

> **IMPORTANT**: A calculated minimum bid rate determines the eligibility. Non-decisioned deals must have a minimum bid rate greater than 90%. For details, see [FAQs](#faqs).

To run a fixed-price commitment deal exclusively, configure the following inventory controls:

Disable open marketplace sources (SP500+ or Blue List) by setting the market type to private.  
Opt-out of default-on deals. For details, see [Default-On Deals](#default-deals).  
Mark your commitment deal as non-decisioned.  
Add your ad group to use non-decisioned deals.  

### 

Disable Open Marketplace Sources[](#pg-private)

To disable markplace sources, allowing only private marketplace deals, use the `adGroupUpdate` mutation to change the marketplace type to `PRIVATE`. The following example updates an ad group to only accept private marketplace sources, which disables SP500+ and Blue List sources.

mutation {

  adGroupUpdate(input: { adGroupId: "AD\_GROUP\_ID\_PLACEHOLDER", marketType: PRIVATE 

  }) {

    data {

      marketType

    }

    userErrors {

      field

      message

    }

  }

}

### 

Set a Deal as Non-Decisioned[](#pg-mark)

To enable non-decisioning on a fixed-price commitment deal, you must use the `inventoryCommitmentSetNonDecisionedEligibility` mutation and set the `isEligibleForNonDecisioned` value to `true`. The following example shows how to set a deal as non-decisioned. After you have marked a deal as eligible, it disables Koa features for targeting and optimizations until this value is set to `false`.

  mutation {

    inventoryCommitmentSetNonDecisionedEligibility(input: {

    commitmentId: "COMMITMENT\_DEAL\_ID\_PLACEHOLDER"

    isEligibleForNonDecisioned: true

  }) {

    userErrors {

      field

      message

    }   

  }

}

> **NOTE**: A fixed-price commitment deal that contains any marketplace sources or default-on deals is ineligible for non-decisioned mode and returns an error.

### 

Set a Non-Decisioned Ad Group[](#pg-adgroup)

To target a non-decisioned deal in an ad group, the ad group must first support non-decisioned deals. Use the `adGroupSetIsNonDecisioned` muation and set the `isNonDecisioned` value to `true`. The following example shows how to set an ad group to allow targeting for non-decisioned deals.

mutation {

  adGroupSetIsNonDecisioned(input: {

    adGroupId: "AD\_GROUP\_ID\_PLACEHOLDER"

    isNonDecisioned: true

  }) {

    userErrors {

      message

    }

  }

}

### 

Target a Non-Decisioned Ad Group[](#pg-target)

After the ad group is set for non-decisioned deals, you can target it with the `adGroupSetCommitmentTargeting` mutation. The following example shows how to add or remove commitments from deal targeting.

mutation {

  adGroupSetCommitmentTargeting(input: {

    adGroupId: "AD\_GROUP\_ID\_PLACEHOLDER"

    commitmentIdsToAdd: \[

      "COMMITMENT\_DEAL\_ID\_PLACEHOLDER"

    \]

    commitmentIdsToRemove: \[\]

  }) {

    userErrors {

      field

      message

    }

  }

}

## 

FAQs[](#faqs)

The following is a list of commonly asked questions about decisioned and non-decisioned deals.

### 

When should I use decisioning?

By default, all deals have decisioning enabled to take advantage of AI, using Koa to manage your deals. Only fixed-price commitment deals can run without decisioning.

### 

What's a fixed-price commitment deal?

A fixed-price commitment deal follows a fixed-price auction, where each impression has a set flat price. These specific deals replace Programmatic Guaranteed (PG) deals in Solimar and can created with or without decisioning.

### 

Why is my deal not spending after I've targeted it?

A common reason for a deal to not spend after being targeted is when the max bid price is lower than the deal's floor price. To fix this, adjust your max bid prices to be greater than the floor price.

### 

How is the minimum bid rate calculated?

The minimum bid rate is a calculated variable that shows how likely the buying party bids, it can also represent how reasonable a commitment deal is. This value is calculated by the following equation:

The spend goal times 1000 divided by the product of the minimum avails, flight duration, minimum win rate, and floor price.

![PDP API Bid Rate Calculation](/v3/content/docs/Images/pdp-bid-rate-calculation.png)