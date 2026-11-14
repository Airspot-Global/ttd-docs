# Creative weights

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/CreativeWeights
- Retrieved: 2026-11-14
- Category: Guides

---

# Creative weights

Creative weights are numerical values (ranging from 0-10) that give you more control over which creatives are shown more or less frequently within an ad group—based on performance insights, testing strategies, or messaging priorities. This lets you manage delivery without restructuring your campaigns or splitting creatives across multiple ad groups.

You can assign creative weights manually or let Koa automate the process. If you use Koa-optimized weights, the platform automatically reviews creative performance daily and adjusts weights to improve delivery. If you prefer to set weights manually, be sure to follow recommended best practices.

The following sections explain the creative weight values and provide GraphQL examples for looking up details and updating the weights.

## Applying creative weights

To apply creative weights, use the `adGroupCreativeSettingsUpdate` mutation with either of the following options specified in the `areKoaCreativeWeightsEnabled` field.

| Description | Field Value | Usage Details |
| --- | --- | --- |
| Enable Koa-optimized weights. | `true` | None. |
| Assign weights manually. | `false` (default) | Assign your preferred values to the `manualWeight` field for each creative. |

For a mutation example, see Update creative weights manually.

### Best practices for manual assignment

If you choose to apply creative weights manually, here are some best practices you can follow:

- Test creative variations at different weights and boost the delivery of top performers.
- Prioritize messaging (for example, highlight a specific product or seasonal offer) by increasing weights.
- Roll out new creatives at lower weights to evaluate performance before scaling.

### Creative weight values

Creative weights are grouped by ad format and use a `0`-`10` decimal scale to indicate the desired ratio for delivery. Higher weights increase the likelihood that a creative will be shown for each impression. The following table describes what the values represent.

| Weight Value | Behavior |
| --- | --- |
| `0` | Creative is excluded from bidding and will not be served. |
| `1` | By default, all creatives in an ad group are evenly weighted at `1`, giving each an equal chance of being shown (unless optimized by Koa). In a custom mix, the weight of `1` is proportional to the total, and delivery reflects the share of each creative in a group sharing the _same ad format and duration_. |
| Custom mix (`1` to `10`) | Impression share is based on the ratio of a creative weight to the total weight of all creatives in a group sharing the _same ad format and duration_. For example, weights of `2`, `2`, and `3` result in selection probabilities of approximately 28.6%, 28.6%, and 42.9%. Formula: `(Individual weight/sum of all weights)`. Using the same example, `3/(2+2+3)=42.9%`. |

## Look up creative weights

The following `adGroup` query retrieves creative weight details as part of bidding information for an ad group:

```
query GetAdGroupCreativeWeightsExample {
  adGroup(id: "AD_GROUP_ID_PLACEHOLDER") {
    koaSettings {
      areKoaCreativeWeightsEnabled
      optimizationsVersion
      minorVersion
    }
    creatives {
      edges {
        node {
          id
        }
        biddingInfo {
          manualWeight {
            weight
            selectionProbability
          }
          koaWeight {
            weight
            selectionProbability
          }
        }
      }
    }
  }
}
```

Here's a sample response that shows how manual weights are assigned when Koa-optimized creative weights are disabled. Note that it returns both the manual and Koa-optimized weights for four creatives for comparison. However, it calculates weights only for the first two creatives because the others have different ad formats (based on content duration).

```
{
  "data": {
    "adGroup": {
      "koaSettings": {
        "areKoaCreativeWeightsEnabled": false,
        "optimizationsVersion": "V3",
        "minorVersion": "5"
      },
      "creatives": {
        "edges": [
          {
            "node": {
              "id": "CREATIVE_ID_PLACEHOLDER_01"
            },
            "biddingInfo": {
              "manualWeight": {
                "weight": 3,
                "selectionProbability": 0.42857142857142855
              },
              "koaWeight": {
                "weight": 1,
                "selectionProbability": 0.5
              }
            }
          },
          {
            "node": {
              "id": "CREATIVE_ID_PLACEHOLDER_02"
            },
            "biddingInfo": {
              "manualWeight": {
                "weight": 4,
                "selectionProbability": 0.5714285714285714
              },
              "koaWeight": {
                "weight": 1,
                "selectionProbability": 0.5
              }
            }
          },
          {
            "node": {
              "id": "CREATIVE_ID_PLACEHOLDER_03"
            },
            "biddingInfo": {
              "manualWeight": {
                "weight": 5,
                "selectionProbability": 1
              },
              "koaWeight": {
                "weight": 1,
                "selectionProbability": 1
              }
            }
          },
          {
            "node": {
              "id": "CREATIVE_ID_PLACEHOLDER_04"
            },
            "biddingInfo": {
              "manualWeight": {
                "weight": 2,
                "selectionProbability": 1
              },
              "koaWeight": {
                "weight": 1,
                "selectionProbability": 1
              }
            }
          }
        ]
      }
    }
  }
}
```

## Assign creative weights manually

To assign creative weights and update their values, use the `adGroupCreativeSettingsUpdate` mutation. The following example mutation shows how to disable Koa for creative weights and assign a manual weight of `4` to a creative.

```
mutation {
  adGroupCreativeSettingsUpdate(input: {
    adGroup: "AD_GROUP_ID_PLACEHOLDER"
    arekoaCreativeWeightEnabled: false
    creativeManualWeights: [
    {
      creativeId: "CREATIVE_ID_PLACEHOLDER"
      manualWeight: 4
    }
    ]
  }) {
    data {
      id
    }
    errors {
      __typename
      ... on MutationError {
        field
        message
      }
    }
  }
}
```

## FAQs

The following is a list of commonly asked questions about creative weights.

### Can I adjust creative weights mid-flight?

Yes. You can modify weights at any time during a campaign to respond to changing performance insights or an evolving strategy.

### Do creative weights work across different ad formats in the same ad group?

No. Creative weights only apply to creatives within a group sharing the _same ad format and duration_. Applying weights across different ad formats in an ad group is not supported.

> **NOTE**: If you want to prioritize ad formats rather than individual creatives, consider using bid factors.

### Can I use a combination of Koa-optimized and manual weights in the same group of creatives?

No. You can either automate creative weights through Koa or adjust them manually, but not both.

### Can I bulk edit creative weights for multiple ad groups at once?

No. You can only edit one or more weights in a single call for each ad group.

### Do creative weights work in Solimar?

No. Creative weights only work with Kokai (Koa v3.5). Using the creative weights mutation in Solimar produces an error.

### What's the likelihood of a creative being shown based on its weight assignment?

The likelihood, also known as selection probability, is determined using the following formula: `(Individual weight/sum of all weights)`. For example, if the creative weights within a group sharing the _same ad format and duration_ are `2`, `2`, and `3`, the creative with the weight of `3` has a selection probability of 42.9% (calculated as `3/(2+2+3)=42.9%`).

You can also run an `adGroup` query and look up the `selectionProbability` value for the creative. For details, see Look up creative weights.

### Can I use fractional values instead of whole numbers when assigning weights to creatives?

Yes. You can assign weights to creatives using fractional values expressed as decimals greater than `0` and less than `10`.

### If Creative A, which has a creative weight of 9.5, becomes unavailable due to an error, will Creative B, with a lower weight of 0.5, use the entire budget despite its smaller share?

Yes. Creative B will use the entire budget because The Trade Desk uses only eligible creatives. Creative weights affect bidding ratios, not spending. Spending is aligned with the ad group budget.

### Do creative weights behave differently between programmatic guaranteed (PG) and non‑PG campaigns?

No. Both PG and non‑PG (including non‑decisioned) campaigns follow the user‑entered creative weights, and there is no special handling between them.
