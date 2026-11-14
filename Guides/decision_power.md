# Decision Power

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/DecisionPower
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/doc/DecisionPower (retired)
- Retrieved: 2026-11-14
- Category: Guides

---

# Decision Power

Decision Power is a forward-looking metric (scored from 0 to 100) that helps you evaluate your campaign’s potential for success by showing when you’ve got the scale needed to be discerning in finding and capturing the most relevant impressions for you. It is one of the key performance indicators (KPIs) in the audience-based buying philosophy of Kokai.

Here’s how the Decision Power Score (DPS) is calculated:

1. The platform determines the consideration circle ratio for your ad group.
 This ratio compares the forecasted available impressions to the forecasted number of impressions needed to spend your budget, given your campaign settings.
2. The ratio is then converted into an index to produce a single, easy-to-read number shown as the Decision Power Score.

In general, higher scores give you more flexibility to optimize toward your goals. For example, at or above 80 means that the platform has plenty of inventory to look for and find the best impressions for you based on information you’ve provided like your seed and goals. In most cases, 80 or above makes for a healthy spread of options to choose from when looking for performant impressions.

Lower DPS indicates that you have less power to apply decisioning. As scores decline, it becomes more and more necessary to buy any impression to hit your budget rather than reach your goals. This lack of decisioning power typically leads to degraded campaign performance. Some campaign types, such as lower-funnel retargeting campaigns, naturally have lower DPS due to the nature of the campaign’s mechanics and may not benefit from a higher score.

## Optimize Decision Power

When your DPS is low, consider making some adjustments. The following table provides guidance by score range.

| Score Range | Status | Description | Recommended Action |
| --- | --- | --- | --- |
| `1` - `79` | Constrained | Your consideration circle is small and our tools don’t have enough room to work to find you more value given your ad group setup. | Expand your inventory and/or apply less restrictive controls to your ad group like loosening frequency caps, increasing base and max bids, and modifying other targeting rails. |
| `80`+ | Ideal | Your score is in an ideal range for the platform to find the best impressions for your ad group setup. | Increase your expressiveness with bid factors. You’ve given the platform room to look for valuable impressions. So make sure you’ve made it clear what’s most valuable to you and your brand. |

## Retrieve the Decision Power score

You can retrieve DPS at the flight level by including the `forecast.forecastedDecisionPower` field in the `advertiser`, `campaign`, or `adGroup` GraphQl queries. The following sections provide examples for each entity (advertiser, campaign, ad group).

### Multiple campaigns

The following `advertiser` GraphQL query example uses the `forecast.forecastedDecisionPower` field to retrieve the DPS for the current flight of one or more campaigns for the specified advertiser.

```
query GetAdvertiserDecisionPowerExample {
  advertiser(id: "ADVERTISER_ID_PLACEHOLDER") {
    campaigns {
      aggregates {
        currentFlight {
          forecast {
            forecastedDecisionPower {
              decisionPower
            }
          }
        }
      }
    }
  }
}
```

### Single ad group

The following `adGroup` GraphQL query example uses the `forecast.forecastedDecisionPower` field to retrieve the DPS for the current flight of one ad group.

```
query GetAdGroupDecisionPowerExample {
  adGroup(id: "AD_GROUP_ID_PLACEHOLDER") {
    currentFlight {
      forecast {
        forecastedDecisionPower {
          calculationStatus
          decisionPower
        }
      }
    }
  }
}
```

### Multiple ad groups

The following `campaign` GraphQL query example uses the `forecast.forecastedDecisionPower` field to retrieve the DPS for the current flight of one or more ad groups for the specified campaign.

```
query GetCampaignAdGroupsDecisionPowerExample {
  campaign(id: "CAMPAIGN_ID_PLACEHOLDER") {
    adGroups {
      nodes {
        id
        currentFlight {
          forecast {
            forecastedDecisionPower {
              calculationStatus
              decisionPower
            }
          }
        }
      }
    }
  }
}
```

### Single campaign flight

The following `campaign` GraphQL query example uses the `forecast.forecastedDecisionPower` field to retrieve the DPS for the current flight of one campaign.

```
query GetCampaignDecisionPowerExample {
  campaign(id: "CAMPAIGN_ID_PLACEHOLDER") {
    id
    currentFlight {
      forecast {
        forecastedDecisionPower {
          calculationStatus
          decisionPower
        }
      }
    }
  }
}
```
