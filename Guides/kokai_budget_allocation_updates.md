# 2024 budget allocation updates (deprecated)

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserNews/news/doc/KokaiBudgetAllocationUpdates
- Retrieved: 2026-11-14
- Category: Guides

---

# 2024 budget allocation updates (deprecated)

> **IMPORTANT**: This article outlines the key differences and breaking changes in Kokai budget allocation as compared to Solimar for the May 28, 2024 release.

To distinguish between two different versions of campaign and ad group budgeting, a new `BudgetingVersion` property has been introduced in the REST API with two respective values: `Kokai` and `Solimar`.

The information provided in this article applies only to "Kokai-budgeted campaigns"—Kokai campaigns with the `BudgetingVersion` property value set to `Kokai`. To check the budgeting version, use the respective campaign and ad group GET endpoints and look for the `BudgetingVersion` property in the response. Only Kokai campaigns have this property present in their responses.

Here's what you need to know about budget allocation in Kokai:

- To manage budget allocation for Kokai campaigns, you must use the GraphQL API. For details, see Budget allocation.
- All Solimar campaign and ad group budget allocation properties have been fully deprecated in the REST API for Kokai-budgeted campaigns. If you include any of the deprecated properties in your requests for Kokai-budgeted campaigns using the REST endpoints, you will receive an error. None of the deprecated properties will be returned in response payloads.
- For Kokai-budgeted campaigns, most of the deprecated REST properties have been replaced with the equivalent properties in the GraphQL API.
- Kokai campaign budget allocation differs from Solimar and might include varying default values.
- For Kokai ad groups and campaigns, you can set the pacing options only at the campaign level.

## Budget types and ad group allocation

Budget allocation in Kokai is different from Solimar, both conceptually and in terms of implementation.

> **IMPORTANT**: In Solimar, ad group budgets function as _maximums_, which might lead to underspending if the flight budget is not fully allocated. In Kokai, ad group budget allocations act as _minimums_ and are optional. By default, ad groups have zero allocation, allowing the platform algorithm to allocate the flight budget to where it finds the most value.

The following table lists the differences between budget types and their definitions in Solimar and Kokai.

| Budget Type | Solimar | Kokai |
| --- | --- | --- |
| Fixed | The sum of unarchived ad group budgets is equal to the campaign budget. | The sum of ad group allocations in the campaign flight is equal to the campaign flight budget. |
| Fluid | Each unarchived ad group budget is equal to the campaign budget. | Each ad group allocation in the campaign flight is set to `0`. |
| Partially fluid | Unarchived ad group budgets in the campaign are neither fluid nor fixed. | The sum of ad group allocations in the campaign flight is less than the campaign flight budget. |

> **NOTE**: Any budget manually allocated to ad groups by using the `minimumSpendInAdvertiserCurrency` property is automatically reserved, regardless of whether the ad groups are active and able to spend (`isEnabled` property). For details and FAQs, see Budget allocation.

### Pacing options

There are four pacing mode options for campaigns (`PacingMode` property values):

- `PACE_AHEAD` (pace ahead to end of flight)
- `PACE_EVENLY` (pace evenly to end of flight)
- `PACE_TO_DAILY_CAP` (pace to daily spend cap)
- `PACE_AS_SOON_AS_POSSIBLE` (pace as soon as possible within minutes)

Here's what you need to know about pacing:

- All ad groups share the same pacing mode as the campaign.
- To set a campaign's pacing mode to `PACE_AS_SOON_AS_POSSIBLE`, it must contain at least one ad group.
- If you are migrating a campaign to Kokai, if all its ad groups have the same pacing mode, the campaign's pacing mode will match the ad groups. For example, if all ad groups are set to `PACE_AS_SOON_AS_POSSIBLE`, the campaign will also be set to this mode. Otherwise, if the ad groups have mixed pacing before migration, they will be set to the campaign's current pacing mode, which may impact spending.

For implementation details, see Budget allocation.

## Deprecated properties in Kokai

The following Solimar properties have been deprecated in the REST API only for Kokai-budgeted campaigns, while Solimar-budgeted campaigns retain these properties.

| Entity | Solimar Setting | Notes on Usage for Kokai-Budgeted Campaigns |
| --- | --- | --- |
| Ad group | `RTBAttributes.BudgetSettings` | The Solimar ad group budget settings (including `PacingMode` and `AdGroupFlights`) have been replaced with the ad group allocation in Kokai. Here's what you need to know: - Solimar ad group budgets that functioned as maximums now function as minimums in Kokai. - To manage your ad group flights in Kokai, use the GraphQL API. |
| Ad group | `RTBAttributes.BudgetSettings.AutoAllocatorPriority` | Fully deprecated in Kokai. |
| Campaign | `AutoAllocatorEnabled` | Fully deprecated in Kokai, this functionality is now automatically managed by the new AI-driven algorithms. |
| Campaign | `AutoPrioritizationEnabled` | Fully deprecated in Kokai, this functionality is now automatically managed by the new AI-driven algorithms. |
| Campaign | `MinimumAdGroupSpendInAdvertiserCurrency` | Fully deprecated in Kokai. |
| Campaign | `PacingMode` | Replaced with an equivalent property in the GraphQL API with a new option to pace as soon as possible. |

If you have any questions, consult with your Technical Account Manager before upgrading your workflows.

## FAQs

The following is a list of commonly asked questions about Kokai-budgeted campaigns.

### Are auto-allocation and auto-prioritization of campaign budgets not supported in Kokai?

Even though the `AutoAllocatorEnabled` and `AutoPrioritizationEnabled` properties are deprecated in Kokai, this functionality is still supported and automatically managed by new AI-driven algorithms.

### How do I recognize if I have a Kokai-budgeted campaign?

To check if a campaign is a Kokai-budgeted campaign, use the GET /v3/campaign/{campaignId} and look up the `BudgetingVersion`. Kokai-budgeted campaigns have the value `Kokai` in the property of `BudgetingVersion`.

### When creating a Kokai campaign, how do I set the budgeting version to Kokai?

If you set the `Version` property to `Kokai` when creating a campaign, its `BudgetingVersion` value will be automatically set to `Kokai` and returned in the response.

### How do I manage deprecated Solimar ad group properties in Kokai?

Kokai has incompatible budgeting settings between Solimar when you use REST for Kokai campaigns. To manage your ad group flights in Kokai, use the REST API in tandem with GraphQL.

### How do I retrieve my campaign and ad group budget settings in Kokai?

Use the GraphQL API. For a list of example queries for retrieving your campaign and ad group budget settings, see Budget allocation.
