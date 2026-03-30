# Predictive Clearing: Win More Impressions with Lower CPMs

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/PredictiveClearing
- Category: Guides

---

# Predictive Clearing: Win More Impressions with Lower CPMs

Predictive Clearing enables you to win more impressions at a lower cost per mille (CPM) while optimizing ad spend and improving campaign performance. When you turn on Predictive Clearing, you enable Koa to analyze historical clearing prices to find a lower, optimal bid for each impression served in a first-price auction.

Here are some key terms that you need to be familiar with to understand the Predictive Clearing workflow.

| Term | Definition |
| First-price auction | An auction in which the winning bidder pays the bid amount, no matter how much higher it is than the second-highest bid. Compare with a second-price auction, in which the winning bidder pays the amount of the second-highest bid plus one cent. |
| Clearing price | The amount paid by the winning bidder. |
| Win rate | The percentage of impressions won, calculated using the following formula:  
`(Number of impressions won / Number of impressions bid on) x 100` |

Predictive Clearing enables Koa, The Trade Desk AI, to analyze historical clearing prices and win rates across first-price auctions to select the optimal bid for each impression. Koa analyzes historical data around SSPs, publishers, sites, ad format, and how much the inventory is worth to other advertisers. This ensures that you (the advertiser) continue to win bids, but at the lowest price needed to win.

For example, you make an original bid of $5.50. Koa analyzes historical data and adjusts your bid to $3.50 before it is submitted. You win the auction and save $2.00 on the impression, which is over 36% of your original bid of $5.50.

![predictive clearing process illustration](/v3/content/docs/Images/predictive-clearing-map.svg)

## 

Turn on Predictive Clearing[](#turn-on-predictive-clearing)

To ensure that your winning bids in first-party auctions have the lowest possible CPM, turn on Predictive Clearing. Here's what you need to know:

*   Predictive Clearing optimizes your winning bids only in first-price auctions.
*   You turn on Predictive Clearing for ad groups.
*   In the platform API, the default value for `PredictiveClearingEnabled` is `false`. In the platform UI, Predictive Clearing is turned on automatically for all ad groups.
*   You can see how much you saved with Predictive Clearing only in platform UI. For details, see [View Predictive Clearing Reporting](https://desk.thetradedesk.com/knowledge-portal/en/koa-predictive-clearing.html#view-predictive-clearing-reporting) in the Knowledge Portal.

To turn on Predictive Clearing, in a [POST /v3/adgroup](/v3/portal/api/ref/post-adgroup) or [PUT /v3/adgroup](/v3/portal/api/ref/put-adgroup) call, set the `PredictiveClearingEnabled` property to `true` as shown in the following ad group code snippet. For a complete example with all required ad group properties, see [Create an Ad Group](/v3/portal/api/doc/AdGroup#createadgroups).

{

   "CampaignId": "t0ncimu",

   "AdGroupName": "Retargeting",

   "PredictiveClearingEnabled": true

}

## 

FAQs[](#faqs)

The following is a list of commonly asked questions about Predictive Clearing.

### 

Does Predictive Clearing work for second-price auctions?

No. Predictive Clearing optimizes bids only in first-price auctions.

### 

Can I see how much I saved from using Predictive Clearing?

Yes. You can run the report that has the Predictive Clearing metric in the platform UI. Be sure to select the Predictive Clearing metric. For details, see [View Predictive Clearing Reporting](https://desk.thetradedesk.com/knowledge-portal/en/koa-predictive-clearing.html#view-predictive-clearing-reporting) in the Knowledge Portal.

### 

Can I run a report for Predictive Clearing savings in the API?

No. You can run the report that has the Predictive Clearing metric only in the platform UI. Be sure to select the Predictive Clearing metric. For details, see [View Predictive Clearing Reporting](https://desk.thetradedesk.com/knowledge-portal/en/koa-predictive-clearing.html#view-predictive-clearing-reporting) in the Knowledge Portal.

### 

Do I need to change my bid strategy if I turn on Predictive Clearing?

No. You can bid as usual, and after you win an auction, Predictive Clearing makes adjustments to see if you can still win the auction with a lower CPM than what you originally bid.

### 

Can Predictive Clearing lower my win rate?

Yes. Since Predictive Clearing lowers your original bid, it is possible for Predictive Clearing to also lower your win rate. However, even if you have a lower win rate, you still have a high chance of winning the auction.