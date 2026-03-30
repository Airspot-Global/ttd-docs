# Budget Allocation

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/CampaignBudgets
- Category: Guides

---

# Budget Allocation

In The Trade Desk platform, campaign budget allocation determines how advertising spend is distributed across campaigns and their ad groups. Efficient allocation helps direct your budget toward placements and audiences that offer the most value. This page explains how the default budget allocation settings in Kokai can drive your KPIs by allocating your spend to ad groups that demonstrate optimal relevance and better value. It also covers how to apply manual controls to fine-tune allocation, manage pacing, and ensure that some budget is reserved for value-based buying.

Here's what you need to know about budget allocation in Kokai:

*   You can let the platform automatically allocate your budget based on value (default and recommended), or manually assign some or all of your budget to specific ad groups, as needed.
*   You can use either the REST API or the GraphQL API (recommended).
*   If you have access to impression budgeting, you can choose to target a specific number of impressions against your flight budget amount. This feature is subject to limited availability. To request access, contact your Technical Account Manager.

## 

Pacing Options[](#pacing)

The campaign pacing mode determines how a campaign flight budget is spent over time, balancing delivery speed with KPIs. Selecting the right pacing mode helps ensure that your ads are served optimally throughout the campaign duration. During or after campaign creation, you can set the pacing mode by using the `PacingMode` property.

> **NOTE**: All ad groups share the same pacing mode as the campaign.

The following table lists the four `PacingMode` values you can set for campaigns.

| Value | Description |
| `PACE_AHEAD` (Default) | Aims to spend approximately 60% of your budget by the midway point of your campaign flight. This is the recommended option in most cases, since front-loading your spend in the first half of the flight can help reduce any effect that market conditions in the last half of your flight might have on your ability to spend your full budget. |
| `PACE_EVENLY` | Aims to spend approximately 50% of your budget by the midway point of your campaign flight. |
| `PACE_TO_DAILY_CAP` | When pacing to a daily spend cap, the platform roughly matches the currently available volume and pricing, spreading your daily cap across the day or across your specified time-of-day targeting. |
| `PACE_AS_SOON_AS_POSSIBLE` | When pacing ASAP, the platform tries to spend up to your specified daily cap as soon as possible, without regard for current available volume or pricing.  
**IMPORTANT**: This option is available only for campaigns that have at least one ad group. |

## 

Budget Allocation Settings[](#settings)

Kokai supports flexible budget allocation strategies across campaign flights and ad groups. The following approaches aren't defined by a schema field but are widely used to describe how the platform handles spend:

*   **Auto allocation** (allocation type: `MINIMUM`)
    *   All ad groups have zero allocated budgets.
    *   The platform automatically distributes spend to the highest-performing (most valuable) ad groups.
    *   Spend priority (if used) influences allocation as a value weight, not as a strict rule. It does not create waterfall-style allocation.
    *   This is the default and most performant approach that drives KPIs and other indicators. It's often informally referred to as "fully fluid" or "value-driven" budget allocation.
*   **Manual allocation** (allocation type: `FIXED` and/or `MINIMUM`)
    *   You assign spend amounts to one or more ad groups.
    *   If `FIXED`, the platform spends the exact amounts assigned to each ad group, regardless of performance.
    *   If `MINIMUM`, the platform ensures the assigned amounts are spent, then distributes any remaining budget based on value.
    *   Spend priority (if used) might still influence fluid portions, but it does not override fixed budgets.
    *   This method is useful when you want stricter budget control or predictability. Depending on the use case, it’s sometimes informally referred to as "partially fluid," "mixed-allocation," or "fixed" budget allocation.

For mutation examples and instructions, see [Automatically Allocate the Budget](#automatic) and [Manually Allocate the Budget](#manual). For sample configurations using different combinations of these settings, see [Use Cases](#use-cases).

The following table lists the key campaign and ad group flight settings that control budget allocation in Kokai.

| Setting | Default Value | Description | Notes |
| `allocationType` | `MINIMUM` | How the campaign flight budget is allocated to the ad group. Possible values include the following:

*   `MINIMUM`—ensures that the ad group receives at least the specified spend amount, with the possibility of receiving more of the budget if the ad group has the most valuable impressions.
*   `FIXED`—ensures that the ad group receives exactly the specified spend amount—no more, no less.

 | 

*   If you choose fixed allocation for all ad groups, and the sum is less than the campaign flight budget, your campaign will underspend. If the sum exceeds the campaign flight budget, you'll get an error.
*   To take advantage of value-driven spending and improve your outcomes whenever possible, The Trade Desk recommends leaving at least 25% of your budget fluid.

 |
| `allocationInAdvertiserCurrency` | `0` | The amount of the campaign flight budget you want to allocate to the ad group. | This amount will be automatically reserved, regardless of whether the ad group is live and able to spend (`isEnabled` property set to `true`). |
| `spendPriority` | `1` | A budget allocation setting that determines how the remaining budget is weighted across ad groups after assigned allocations are met, typically in partially fluid budgets. | Spend priority acts as a value weight rather than a strict spending order. It guides the system to favor certain impressions, but it does not create waterfall-style allocation. Instead, priorities provide a directional nudge to influence how impressions are valued. For details, see [Spend Priority](#priority). |

If you choose to [manually allocate](#manual) some or all of your budget to specific ad groups, use the same settings but with updated values.

> **TIP**: For performance and flexibility, use a fluid, value-driven budget so our AI can help you regularly and rapidly improve value and relevance.

### 

Use Cases[](#use-cases)

Let’s consider a simple scenario with two ad groups—A and B—and a campaign flight budget of $1000. The following table outlines common budget allocation use cases, showing how different settings influence the platform's distribution of spend between the two ad groups, regardless of which one ultimately delivers more value.

| Ad Group A | Ad Group B | Chances of Conversions | Underspend Risk Level | Notes |
| `allocationType` = `MINIMUM`  
`allocationInAdvertiserCurrency` = `0` | `allocationType` = `MINIMUM`  
`allocationInAdvertiserCurrency` = `0` | Highest | Very low | 

*   This is a fully fluid, value-driven budget.
*   This is the default and recommended spending method.

 |
| `allocationType` = `MINIMUM`  
`allocationInAdvertiserCurrency` = `300` | `allocationType` = `MINIMUM`  
`allocationInAdvertiserCurrency` = `300` | Medium | Low | 

*   This is a partially fluid, value-driven budget.
*   Both ad groups receive $300 each.
*   The platform automatically directs the remaining $400 to the ad group that delivers the most valuable impressions.

 |
| `allocationType` = `MINIMUM`  
`allocationInAdvertiserCurrency` = `300`  
`spendPriority` = `2` | `allocationType` = `MINIMUM`  
`allocationInAdvertiserCurrency` = `300`  
`spendPriority` = `1` | Medium | Medium to low | 

*   This is a partially fluid, priority-weighted budget.
*   Both ad groups receive $300 each.
*   The higher priority nudges the platform to favor ad group B to direct the remaining $400. However, if ad group A has more valuable impressions, it might still get more spend.

 |
| `allocationType` = `MINIMUM`  
`allocationInAdvertiserCurrency` = `300` | `allocationType` = `FIXED`  
`allocationInAdvertiserCurrency` = `300` | Medium | Medium to low | 

*   This is a mixed-allocation budget.
*   Both ad groups receive $300 each.
*   The remaining $400 of the flight budget is automatically directed to ad group A, even if those impressions might not be the most valuable.

 |
| `allocationType` = `FIXED`  
`allocationInAdvertiserCurrency` = `300` | `allocationType` = `FIXED`  
`allocationInAdvertiserCurrency` = `700` | Medium | Very low | 

*   This is a fixed budget.
*   Each ad group receives the allocated amount.

 |
| `allocationType` = `FIXED`  
`allocationInAdvertiserCurrency` = `300` | `allocationType` = `FIXED`  
`allocationInAdvertiserCurrency` = `300` | Low | High | 

*   This is a fixed budget.
*   Both ad groups receive $300 each.
*   Since both ad groups are fixed, the platform stops spending after both ad groups reach their fixed amount.
*   **IMPORTANT**: The remaining $400 of the flight budget remains unspent.
*   In this situation, consider changing the allocation type to `MINIMUM`.

 |

### 

Automatically Allocate the Budget[](#automatic)

When you select a value-driven budget with the auto allocation option, the platform employs data-driven insights on performance to dynamically direct your flight budget to impressions with optimal relevance and better value. Using a value-driven budget reduces the need to move the budget mid-flight based on ad group performance. See also [Drive Your KPIs to Success](/v3/portal/api/doc/DriveKPIs).

To achieve this, all ad groups in a campaign have zero allocation (are fully fluid) by default.

The following GraphQL `campaignBudgetSettingsUpdate` mutation example illustrates the default allocation settings for two ad groups.

mutation {

  campaignBudgetSettingsUpdate(

    input: {

      campaignId: "CAMPAIGN\_ID\_PLACEHOLDER"

      campaignFlights: \[

        {

          campaignFlightId: "CAMPAIGN\_FLIGHT\_ID\_PLACEHOLDER"

          budgetInAdvertiserCurrency: 1000

          adGroupFlights: \[

            {

              adGroupId: "AD\_GROUP\_ID\_A\_PLACEHOLDER"

              campaignFlightId: "CAMPAIGN\_FLIGHT\_ID\_PLACEHOLDER"

              allocationInAdvertiserCurrency: 0

              allocationType: MINIMUM

            }

            {

              adGroupId: "AD\_GROUP\_ID\_B\_PLACEHOLDER"

              campaignFlightId: "CAMPAIGN\_FLIGHT\_ID\_PLACEHOLDER"

              allocationInAdvertiserCurrency: 0

              allocationType: MINIMUM

            }

          \]

        }

      \]

    }

  ) {

    data {

      campaign {

        flights {

          edges {

            node {

              budgetInAdvertiserCurrency

              startDateInclusiveUTC

              endDateExclusiveUTC

              id

              adGroupFlights {

                edges {

                  node {

                    adGroupId

                    allocationInAdvertiserCurrency

                    allocationType

                  }

                }

              }

            }

          }

        }

      }

    }

    userErrors {

      field

      message

    }

  }

}

### 

Manually Allocate the Budget[](#manual)

The platform’s default and recommended approach is to let the system automatically allocate your budget based on value, directing spend to the ad groups most likely to deliver strong performance. This fully fluid, value-driven method typically yields the best results by maximizing efficiency and outcome.

However, if you prefer more control, you can manually allocate any or all of your campaign budget to specific ad groups.

> **IMPORTANT**: Before getting started, be sure to review the [budget allocation settings](#settings) and various [use cases](#use-cases) to ensure your setup aligns with your campaign goals.

Here's what you need to know about manual budget allocation:

*   You can change budget allocations at any time for current and future flights, as long as the amount is not less than what has already been spent.
*   If the total of your `FIXED` or `MINIMUM` allocations is less than the campaign flight budget, the platform spends those allocations first, then distributes the remaining budget to high-performing ad groups based on value. This mixed-allocation approach is recommended when you want both control and optimization. To maximize value-driven performance, try to leave at least 25% of your budget unallocated.
*   Spend priority (if used) might still influence fluid portions, but it does not override fixed budgets. Nor does it create waterfall allocation. For details, see [Spend Priority](#priority).
*   The value-driven portion of a mixed-allocation budget won't compensate for an underspending ad group. Any unspent portion of a fixed or minimum allocation is not redistributed elsewhere.
*   Manual allocations reserve the specified budget amount exclusively for the assigned ad group. If you turn off that ad group, its budget will remain unused unless you either re-enable the ad group or reallocate its funds.
*   If the total allocation amount across all ad groups exceeds the campaign flight budget, the system will return an error.

The following GraphQL `campaignBudgetSettingsUpdate` mutation example illustrates how you can set up a mixed-allocation budget for two ad groups—A and B—for one of the [use cases](#use-cases). Both ad groups will receive $300 each, and the remaining $400 of the flight budget will be automatically directed to ad group A.

> **NOTE**: If an ad group starts to show significant projected underspend, consider reallocating its budget to value-driven to help spend your budget in full. Setting the allocation type to `MINIMUM` will have more room for value-driven allocation, with the same specified amounts spent for each ad group.

mutation {

  campaignBudgetSettingsUpdate(

    input: {

      campaignId: "CAMPAIGN\_ID\_PLACEHOLDER"

      pacingMode: PACE\_AS\_SOON\_AS\_POSSIBLE

      campaignFlights: \[

        {

          campaignFlightId: "CAMPAIGN\_FLIGHT\_ID\_PLACEHOLDER"

          budgetInAdvertiserCurrency: 1000

          adGroupFlights: \[

            {

              adGroupId: "AD\_GROUP\_ID\_A\_PLACEHOLDER"

              campaignFlightId: "CAMPAIGN\_FLIGHT\_ID\_PLACEHOLDER"

              allocationInAdvertiserCurrency: 200

              allocationType: FIXED

            }

            {

              adGroupId: "AD\_GROUP\_ID\_B\_PLACEHOLDER"

              campaignFlightId: "CAMPAIGN\_FLIGHT\_ID\_PLACEHOLDER"

              allocationInAdvertiserCurrency: 300

              allocationType: MINIMUM

            }

          \]

        }

      \]

    }

  ) {

    data {

      campaign {

        flights {

          edges {

            node {

              budgetInAdvertiserCurrency

              dailyTargetInAdvertiserCurrency

              startDateInclusiveUTC

              endDateExclusiveUTC

              id

              adGroupFlights {

                edges {

                  node {

                    adGroupId

                    dailyTargetInAdvertiserCurrency

                    allocationInAdvertiserCurrency

                  }

                }

              }

            }

          }

        }

      }

    }

    userErrors {

      field

      message

    }

  }

}

You can also use the `campaignBudgetSettingsUpdate` mutation to upgrade the budget version to Kokai and update the campaign [pacing mode](#pacing), flight dates, time zone, and so on for multiple flights in one call.

### 

Spend Priority[](#priority)

If needed, you can set priorities among your ad groups to influence how the platform calculates the value of each impression your campaign might bid on. Priorities enable you to express what strategies you find more valuable compared to others.

> **IMPORTANT**: In the platform, spend priority acts as a value weight rather than a strict spending order. It guides the system to favor certain impressions, but it does _not_ create waterfall-style allocation. Instead, priorities provide a directional nudge to influence how impressions are valued.

Here's what you need to know about setting a spend priority for your ad groups:

*   Fixed budgets are always honored, regardless of priority. Priority only influences how the remaining fluid budget is distributed, if there is any.
*   Ad groups with a higher priority (lower number) are more likely to receive a larger share of the fluid budget, assuming similar performance and scale. However, this doesn’t mean they spend first; rather, they receive more consideration during allocation.
*   If you assign the same value to multiple ad groups, then the platform will either prioritize the ad group with the fixed budget or, if both ad groups have the minimum allocation type, the platform will prioritize the ad group that has the most valuable impressions.
*   You can assign only a priority value that's between `1` and `10`.

The following GraphQL `adGroupSpendPrioritizationUpdate` mutation example illustrates five ad groups (A-E) that each have different spend priorities with the exception of ad groups B and C that have the same priority. In this example, ad group A will be prioritized above the other ad groups. Since ad groups B and C have the same priority, the ad group that has the most valuable impressions will be prioritized.

mutation {

  adGroupSpendPrioritizationUpdate(

    input: {

      campaignId: "CAMPAIGN\_ID\_PLACEHOLDER"

      spendPriorities: \[

        { adGroupId: "AD\_GROUP\_ID\_A\_PLACEHOLDER", spendPriority: 1 }

        { adGroupId: "AD\_GROUP\_ID\_B\_PLACEHOLDER", spendPriority: 2 }

        { adGroupId: "AD\_GROUP\_ID\_C\_PLACEHOLDER", spendPriority: 2 }

        { adGroupId: "AD\_GROUP\_ID\_D\_PLACEHOLDER", spendPriority: 3 }

        { adGroupId: "AD\_GROUP\_ID\_E\_PLACEHOLDER", spendPriority: 4 }

      \]

    }

  ) {

    errors {

      ... on MutationError {

        message

        field

      }

    }

  }

}

## 

Impression Budgets[](#impression-budget)

> **NOTE**: This feature requires permissions. To request access, contact your Technical Account Manager.

Impression budgeting enables you to target a specific number of impressions against your flight budget amount. Here's what you need to know about impression budgets:

*   The pacing model uses a combination of base bids and bid factors, which offers more control over average CPMs.
*   Ad group spend is prioritized using waterfall-style budget allocation.

The following table provides additional details.

| Feature | Description |
| Bid Price | The price of each impression is determined by a combination of the impression value and the calculation of the base bid x bid factors. |
| Base Bid CPM | The base bid represents your target average CPM for the ad group. Your bid prices may fluctuate above or below this amount depending on the value of the impression, but by the end of the flight, the average CPM will normalize to the base bid you set. |
| Bid Factors | If your ad group includes bid factors, the average CPM will be based on base bid × bid factors. If the ad group doesn't have bid factors, then the platform uses only the base bid as the average CPM. |
| Prioritization | Ad group priorities follow a strict waterfall spending order. Higher-priority ad groups will spend their budget first while lower-priority ones will only receive budget once higher ones are exhausted.  
**NOTE**: If an ad group also has a monetary minimum budget, then that ad group takes priority regardless of what you set. |

The following GraphQL `campaignBudgetSettingsUpdate` mutation example illustrates an ad group that has a budget of one million impressions specified in the `budgetInImpressions` field.

mutation {

  campaignBudgetSettingsUpdate(

    input: {

      campaignId: "CAMPAIGN\_ID\_PLACEHOLDER"

      campaignFlights: \[

        {

          campaignFlightId: "CAMPAIGN\_FLIGHT\_ID\_PLACEHOLDER"

          adGroupFlights: \[

            {

              adGroupId: "AD\_GROUP\_ID\_A\_PLACEHOLDER"

              campaignFlightId: "CAMPAIGN\_FLIGHT\_ID\_PLACEHOLDER"

              budgetInImpressions: 1000000

            }

          \]

        }

      \]

    }

  ) {

    userErrors {

      field

      message

    }

  }

}

## 

Query Examples[](#queries)

The following are some commonly used GraphQL query examples that illustrate how you can look up budget and flight information for a given campaign and its ad groups.

### 

Look Up Campaign and Ad Group Flight and Budget Settings[](#queries-flights)

The following GraphQL `campaign` query retrieves campaign and ad group flight and budget settings for a given campaign ID.

query GetCampaignAndAdGroupFlightsExample {

  campaign(id: $campaignId) {

    id

    budget {

      allocationMode

      total

      pacingMode

      usesImpressionBudgets

      version

    }

    flights {

      edges {

        node {

          id

          budgetAllocationMode

          usesImpressionBudgets

          budgetInAdvertiserCurrency

          startDateInclusiveUTC

          endDateExclusiveUTC

          isCurrent

          adGroupFlights {

            edges {

              node {

                adGroupId

                allocationInAdvertiserCurrency

                allocationType

                adGroup {

                  budget {

                    isFluid

                    spendPriority

                  }

                }

              }

            }

          }

        }

      }

    }

  }

}

### 

Look Up Flight IDs in a Campaign[](#queries-flight-IDs)

The following GraphQL `campaign` query retrieves campaign flight IDs and the maximum amount each flight may spend.

query GetFlightIDsExample {

  campaign(id: "CAMPAIGN\_ID\_PLACEHOLDER"){

    id

    name

    flights(where: {id: {in: \["FLIGHT\_ID\_1", "FLIGHT\_ID\_2"\]}}){

      nodes{

        id

        budgetInAdvertiserCurrency

      }

    }

  }

}

> **TIP**: You can also retrieve performance metrics that provide more granular data to help analyze trends, optimize bids, and measure engagement effectively. For details, see [Campaign Performance Reporting Queries](/v3/portal/api/doc/CampaignQueryExamplesGQL#reporting).

## 

Campaign Flight Mutation Examples[](#mutations)

The following are some commonly used GraphQL mutation examples that illustrate how you can update budget and flight information for a given campaign and its ad groups.

### 

Create a Campaign Flight[](#mutations-flight-create)

The following GraphQL `campaignFlightCreate` mutation example illustrates how you can create a campaign flight for a given campaign.

> **NOTE**: When you create a new campaign flight, default ad group flights will be automatically created.

mutation {

  campaignFlightCreate(

    input: {

      campaignId: "abc123"

      budgetInAdvertiserCurrency: 1000

      startDateInclusiveUTC: "2024-07-01T00:00:00.000Z"

      endDateExclusiveUTC: "2024-07-30T23:59:00.000Z"

    }

  ) {

    data {

      id

      budgetInAdvertiserCurrency

      dailyTargetInAdvertiserCurrency

      startDateInclusiveUTC

      endDateExclusiveUTC

      adGroupFlights {

        edges {

          node {

            adGroupId

            allocationInAdvertiserCurrency

          }

        }

      }

    }

    userErrors {

      field

      message

    }

  }

}

### 

Update a Campaign Flight[](#update-flight)

To update a campaign flight, use the `campaignFlightUpdate` mutation. Here's what you need to know about updating a campaign flight:

*   You can update only one campaign flight in a single `campaignFlightUpdate` mutation call. To update multiple flights in a campaign, use the `campaignBudgetSettingsUpdate` mutation. For details, see [Allocate the Budget](#mutations-budget-settings).
*   You can update only ad group flights that are associated with the same campaign flight. In other words, you must specify the same campaign flight ID for each ad group flight.

The following GraphQL `campaignFlightUpdate` mutation example illustrates how you can update the budget, daily target, and ad group flights of a given campaign flight by its ID.

mutation {

  campaignFlightUpdate(

    input: {

      campaignFlightId: "CAMPAIGN\_FLIGHT\_ID\_PLACEHOLDER"

      budgetInAdvertiserCurrency: 1000

      dailyTargetInAdvertiserCurrency: 15

      adGroupFlights: \[

        {

          adGroupId: "AD\_GROUP\_ID\_A\_PLACEHOLDER"

          campaignFlightId: "CAMPAIGN\_FLIGHT\_ID\_PLACEHOLDER"

          dailyTargetInAdvertiserCurrency: 50

          allocationInAdvertiserCurrency: 0

        }

        {

          adGroupId: "AD\_GROUP\_ID\_B\_PLACEHOLDER"

          campaignFlightId: "CAMPAIGN\_FLIGHT\_ID\_PLACEHOLDER"

          dailyTargetInAdvertiserCurrency: 50

          allocationInAdvertiserCurrency: 0

        }

      \]

    }

  ) {

    data {

      id

      budgetInAdvertiserCurrency

      dailyTargetInAdvertiserCurrency

      adGroupFlights {

        edges {

          node {

            adGroupId

            dailyTargetInAdvertiserCurrency

            allocationInAdvertiserCurrency

          }

        }

      }

    }

    userErrors {

      field

      message

    }

  }

}

### 

Delete a Campaign Flight[](#delete-flight)

The following GraphQL `CampaignFlightDelete` mutation example illustrates how you can delete a campaign flight by its ID.

mutation {

  campaignFlightDelete(input: { campaignFlightId: 123456 }) {

    data {

      wasSuccessfullyDeleted

    }

    userErrors {

      field

      message

    }

  }

}

## 

FAQs[](#faqs)

The following are frequently asked questions about campaign and ad group budget allocation.

### 

Can I assign a maximum allocation to an ad group?

No. You can, however, assign a fixed allocation that enables the platform to spend exactly the specified amounts. This method acts as both a minimum and a maximum allocation.

### 

Can I set a budget based on impressions?

You can use impression budgets only if you have the appropriate permissions. For details, contact your Technical Account Manager.

### 

Do all ad groups have to have the same allocation type?

No. You can assign a different allocation type to each ad group. You can make some ad group budgets fixed and leave others fluid. The platform honors fixed budgets first, then allocates the rest based on value. For details, see [Use Cases](#use-cases).

### 

What does "value-driven" mean in Kokai?

It means the platform automatically allocates budget to the ad groups that generate the most valuable impressions without requiring any predefined ad group budgets.

### 

What happens if the sum of my ad group minimum spend allocations exceed the campaign flight budget?

You will receive an error. The sum of ad group minimum spend allocations must never exceed the campaign budget.

### 

How are priorities different in Kokai?

In Kokai, priorities acts as a value weight, not a strict order of spend as it was in Solimar. For details, see [Spend Priority](#priority).

### 

Can I allocate the budget during ad group creation?

No. You can use only the `campaignBudgetSettingsUpdate` mutation to allocate the budget, and only after you have created the ad group. For details, see [Budget Allocation Settings](#settings).

### 

Can I use the campaignBudgetSettingsUpdate mutation to update budget and allocation settings for multiple campaigns?

No. This mutation enables you to update multiple flight budgets and allocations within a single campaign only.

### 

Can I use bulk operations to update my budget and allocation settings?

Yes. To update campaign and ad group flight settings, you can use the `bulkUpdateCampaignFlights` mutation.

### 

How do I reserve some of the budget for an ad group?

Any budget allocated to ad groups is automatically reserved, regardless of whether the ad groups are live and able to spend (`isEnabled` property).

### 

If the allocated budget is reserved for ad groups regardless of their status, is it also reserved for archived ad groups?

No. Budget is reserved only for non-archived ad groups (`isArchived` property set to `false`). Ad group budgets are automatically reserved regardless of whether ad groups are live and able to spend (`isEnabled` property set to `true`).

### 

What budgeting versions do Kokai campaigns support?

Kokai campaigns currently support two budgeting versions (Kokai and Solimar) for campaigns and ad groups, which are indicated by the `budget.version` field in GraphQL and `BudgetingVersion` property in REST.

### 

When creating a Kokai campaign, how do I set the budgeting version to Kokai?

You do not need to set the budgeting version if you created a campaign in Kokai. Every campaign created in Kokai will always have a `Kokai` budgeting version.

### 

How do I query for flight IDs in a specific campaign?

Use a `flights` filter in a GraphQL query to retrieve campaign flight IDs and the maximum amount each flight may spend. To learn more about using filters, see [GraphQL API Queries](/v3/portal/resources/doc/GqlApiQueries#filters) in our GraphQL Resource Hub.

query GetFlightIDsExample {

  campaign(id: "CAMPAIGN\_ID\_PLACEHOLDER"){

    id

    name

    flights(where: {id: {in: \["FLIGHT\_ID\_1", "FLIGHT\_ID\_2"\]}}){

      nodes{

        id

        budgetInAdvertiserCurrency

      }

    }

  }

}

### 

How is pacing mode different in Kokai?

In Solimar, campaigns have three pacing modes, and ad groups have four pacing modes. You can adjust the pacing mode at both the campaign and ad group level.

In Kokai, both campaigns and ad groups have four pacing modes since ad groups inherit the pacing mode from the campaign. The pacing mode on the campaign level is shared by all ad groups under it.

The following table lists equivalent values for the `PacingMode` property in Kokai versus Solimar.

| Kokai | Solimar (Campaign) | Solimar (Ad Group) |
| `PACE_AS_SOON_AS_POSSIBLE` | N/A | `Off` |
| `PACE_EVENLY` | `PaceToEndOfFlight` | `PaceToEndOfFlight` |
| `PACE_TO_DAILY_CAP` | `Off` | `PaceToEndOfDay` |
| `PACE_AHEAD` | `PaceAhead`  
**NOTE**: The logic for pace ahead is `PaceToEndOfFlight` + 1.2 \* `DailyBudget`. | `PaceAhead` |

> **NOTE**: These property names and values apply to only the `CampaignBudget` mutations. The pacing mode in other mutations and REST may use a different name or set of values. For example, in a campaign [bulk operation](/v3/portal/api/doc/GqlBulkOperations), the value for pacing evenly is `PaceEvenly`.