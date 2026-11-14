# Ad Groups

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/AdGroup
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/doc/AdGroup (retired)
- Retrieved: 2026-11-14
- Category: Guides

---

# Ad groups

An ad group is a strategy that falls within a particular campaign and enables you to assemble targeting strategies to specify when, where, and how to serve ads. You can manage budgets, goals, creatives, site lists, inventory, and viewability, as well as targeting options for audiences, devices, locations, languages, times of day, and video adjustments across ad groups.

This guide covers the settings that apply to every ad group, such as funnel location, goals, and performance-enhancing features. For the end-to-end process (creating, associating creatives and bid lists, allocating budget, and updating), see Ad group creation workflows.

Here's what you need to know about ad groups:

- You can use both the GraphQL and REST API to create and manage your ad groups. For details on what each API supports, see GraphQL and REST API comparison.
- To create or update multiple ad groups at once, you must use GraphQL API bulk operations.
- To enable an ad group, it must be associated with a campaign and have at least one approved creative. While you can create an ad group with an empty `CreativeIds` array, you cannot enable it until you upload a creative.
- Ad group budget allocation and pacing are set at the campaign level, and only in GraphQL. For details, see Budget allocation.
- If a campaign is in Kokai and has the Sellers and Publishers 500+ (SP500+) marketplace enabled, any ad group you create in that campaign automatically inherits SP500+ access.

## Setup and optimization

The following table lists the properties you must include in all ad groups.

| Property | Notes |
| --- | --- |
| Funnel location | - The funnel location (awareness, consideration, conversion) helps measure the success of your ad groups effectively. - If not explicitly set, it's automatically set based on the originating campaign's primary goal. |
| Goal or KPI | - If not explicitly set, the goal or KPI is automatically set based on the originating campaign's primary goal. - Ad groups must also have them either set directly or inherited from their parent campaign. - The default KPI is "Reach". |

You can further optimize ad groups using performance-enhancing features such as Predictive Clearing and Identity Alliance. Here's what else you need to know about setting up ad groups:

- To configure and manage ad group budgets, you must use GraphQL. For details on budget types and pacing options, see Budget allocation.
- By default, ad groups have no budget allocation, allowing the platform algorithm to distribute flight budget wherever it identifies the greatest value.
- Any budget manually allocated to ad groups through the `minimumSpendInAdvertiserCurrency` flight property is automatically reserved, regardless of whether the ad groups are enabled and eligible to spend (`isEnabled` property).

## GraphQL and REST API comparison

To create, update, or query ad groups, you can use the GraphQL and REST API. The following table lists the differences between the GraphQL and REST API and how many ad groups you can create, update, and query per call.

> **NOTE**: The update and create mutations for individual ad groups are not fully featured yet. Check for updates as we roll out new features and enhancements.

| Operation | GraphQL API | REST API | Notes |
| --- | --- | --- | --- |
| Create | Individually or in bulk, using a simplified set of fields | Only one ad group | For details, see Create ad groups and GraphQL API bulk operations. |
| Clone | Only with the parent campaign | N/A | You can choose to clone all, none, or a selection of ad groups with the parent campaign. For details, see Clone campaigns. |
| Read (query) | Individually or in bulk, using custom queries | Only one ad group | For details, see Look up ad groups. |
| Update | In bulk, using a simplified set of fields | Only one ad group | For details, see Update ad groups and GraphQL API bulk operations. |
| Manage budget allocation and pacing | In bulk and per campaign | N/A | For details, see Budget allocation. |

> **TIP**: For comprehensive steps from creating an ad group through associating creatives, bid lists, and budget, see Ad group creation workflows.

## Funnel location

An ad group funnel location identifies the focus or objective of your ad group (awareness, consideration, and conversion). For example, you may want to focus on getting people to consider your business, encourage them to make a purchase, or sign up for an event.

To measure the success of your ad groups effectively, you must set the `FunnelLocation` value when you create your ad group:

| Funnel Location | Value | Description |
| --- | --- | --- |
| Awareness | `AWARENESS` | Generate interest in your brand. Discover qualified leads to increase brand knowledge and reach as many people as possible in your target audience. Increasing brand awareness is about telling people what makes your business valuable. |
| Consideration | `CONSIDERATION` | Get people to think about your business and seek more information. Reach new customers and influence them to become prospective customers. |
| Conversion | `CONVERSION` | Encourage prospective customers who are already interested in your business to take a specific action. |

## Performance-enhancing features

Here's what you need to know about performance-enhancing features for ad groups:

- To enable a feature, set the corresponding property value to `true`. For an example of an ad group with some of the key performance-enhancing features turned on, see the REST API request example.
- All feature properties, except Predictive Clearing and Koa Optimizations, are part of the `RTBAttributes.AudienceTargeting` object.
- Some features, like Audience Booster, apply only to ad groups with certain KPIs. Other features are mutually exclusive as noted in the feature and property descriptions.

The following table lists performance-enhancing features available for ad groups. The list indicates the ad group API settings for each feature and provides links to the Knowledge Portal pages and other resources where you can learn more.

| Feature | API Property | Description | Fee-Based? |  |
| --- | --- | --- | --- | --- |
| Predictive Clearing | `PredictiveClearingEnabled` | Predictive Clearing is a cost-saving feature that helps you win more impressions at a lower CPM while optimizing ad spend and improving campaign performance. When you turn on Predictive Clearing, it analyzes historical clearing prices to find a lower, optimal bid for each impression served in a first-price auction. | Yes |  |
| Koa Optimizations | `KoaDimensions` | Koa Optimizations is on by default, except in some special cases. When turned on, it enables Koa, the artificial intelligence that powers The Trade Desk platform, to automatically generate optimizations for the ad group dimensions that you specify. | No |  |
| Identity Alliance | `CrossDeviceVendorListForAudience` | Enables the platform to select the right option for a user across all cross-device vendors on an impression-by-impression basis. Set `CrossDeviceVendorId` to `10` for Identity Alliance (person) or `11` for Identity Alliance (household). For details, see Cross-device targeting. | Yes |  |
| Prism | `AudienceExcluderEnabled` | Creates a custom audience for the ad group by excluding data segments that are less relevant to the advertiser's target audience. In other words, this custom audience increases the value of a campaign by focusing on the most valuable impressions and excluding users who are less likely to benefit the campaign. Here's what you need to know about this property: - This property cannot be used in conjunction with Audience Predictor. - Advertisers in the following IAB categories may not use this functionality: Personal Finance, Careers, Real Estate. . | Yes |  |
| Audience Predictor | `AudiencePredictorEnabled` | Enables the platform to use the lookalike model data to create and continuously update an audience of users who are most likely to convert, and target them in your audience. Here's what you need to know about this functionality: - Enabling this functionality generates a custom audience. - Advertisers in the following IAB categories cannot use third-party data or custom modeling sources with Audience Predictor: Personal Finance, Careers, Real Estate. | Yes |  |
| Adding Segments Resembling Your Target Customer | `AudienceBoosterEnabled` | A performance-enhancing functionality for conversion-based campaigns that have cost per acquisition (CPA) or return on ad spend (ROAS) as the primary goal. This functionality adds high-performing data segments that are similar to the advertiser's target audience. In other words, ads will be served only to users who benefit from the campaign and are most likely to convert. By default, it is set to `false`. **IMPORTANT**: This feature applies only to ad groups that have CPA or ROAS goals. | No |  |
| News Navigator | `isNewsNavigatorEnabled` | Prioritizes reliable and objective news as scored by third-party news rating partners. Available through GraphQL only. By default, it is set to `true`. | No | 0 0 |

> **TIP**: For an example of an ad group with some of the key performance-enhancing features turned on, see Request example.

## Look up ad groups

You can retrieve ad group details using GraphQL. The following sections provide a list of sample queries that retrieve ad group information.

- Look up ad groups by name
- Look up campaign data for an ad group
- Look up ad group performance metrics by date range
- Look up ad groups for multiple advertiser IDs
- Look up invisible or disabled ad groups
- Look up ad group settings
- Look up ad group Prism setting
- Look up ad group metadata

> **TIP**: You can also run multiple queries at once. For details, see GraphQL bulk operations: Queries.

#### Look up ad groups by name

The following GraphQL query retrieves ad groups by name. You can configure the query to reduce or change the types of data returned. Other options include omitting the partner ID, searching across multiple advertisers, and combining search terms using the "and" operator.

If you have more than 100 items in your search results, use pagination to return them.

```
query GetAdGroupsByNameExample {
    adGroups(
        first: 100
        where: {
            partnerId: { eq: "PARTNER_ID_PLACEHOLDER" }
            advertiserId: { eq: "ADVERTISER_ID_PLACEHOLDER" }
            name: { contains: "SEARCH_TERM_PLACEHOLDER" }
        }
    ) {
        nodes {
            id
            name
            isArchived
            budget {
                currentFlightBudget
                isFluid
                total
            }
            adGroupFlights {
                nodes {
                    campaignFlightId
                    budgetInImpressions
                    dailyTargetInAdvertiserCurrency
                    dailyTargetInImpressions
                    historicalProjectedSpendInAdvertiserCurrency
                    minimumSpendInAdvertiserCurrency
                    totalSpendSoFarInAdvertiserCurrency
                    yesterdayImpressions
                    yesterdaysPotentialSpendInAdvertiserCurrency
                    yesterdaysSpendInAdvertiserCurrency
                }
            }
        }
    }
}
```

#### Look up campaign data for an ad group

The following GraphQL query retrieves campaign-level data for an ad group.

```
query GetCampaignKeyMetricDataForAdGroupExample {
    adGroup(id: "abc1234") {
        adGroupFlights {
            totalCount
            nodes {
                adGroupId
                forecast {
                    projectedSpend
                    relevance
                    confidence
                    lastUpdated
                }
            }
        }
        spend {
            spend
        }
    }
}
```

#### Look up ad group performance metrics by date range

With the GraphQL API, you can create and customize `adGroup` queries and include `reporting` fields that provide key performance metrics for tracking KPIs, cost and bidding, media quality, and overall effectiveness. You can either retrieve lifetime data or organize it by day or hour to help analyze trends, optimize bids, and measure engagement effectively. Whether you're evaluating media efficiency or optimizing your bidding strategy, these detailed performance metrics can help you make informed, data-driven decisions.

> **TIP**: You can also use the `reporting` field to retrieve performance metrics at the advertiser and campaign level.

Here's what you need to know about looking up ad group performance metrics by date range:

- You can filter the metrics only by date.
- If you don't include a date range in the `where` filter, the query returns the ad group's lifetime metrics.
- You can retrieve metrics at the following time intervals, specified in the `dimensions` field:

  - Hourly (last 30 days)
  - Daily (last year)

- If you don’t include the `dimensions` field, the query returns aggregated totals for each metric without grouping data by time interval.

The following `adGroup` GraphQL query retrieves all metrics you can use to optimize campaign performance, manage spend and bidding, and so on. The date range is specified using `gte` (start, inclusive) and `lt` (end, exclusive) for the reporting period.

```
query GetAdGroupPerformanceMetricsbyDateRangeExample($adGroupId: ID!) {
  adGroup(id: $adGroupId) {
    reporting {
      generalReporting(
        where: { date: { gte: "2025-02-01", lt: "2025-03-01" } }
      ) {
        nodes {
          dimensions {
            time {
              day
            }
          }
          metrics {
            adPlays
            bids
            clicks
            conversions
            cpa {
              advertiserCurrency
            }
            cpc {
              advertiserCurrency
            }
            cpcv {
              advertiserCurrency
            }
            cpm {
              advertiserCurrency
            }
            ctr
            customCpa {
              advertiserCurrency
            }
            customRoas {
              advertiserCurrency
            }
            impressions
            revenue
            roas {
              advertiserCurrency
            }
            spend {
              advertiserCurrency
            }
            tvQualityCpm {
              advertiserCurrency
            }
            tvQualityIndex
            vCpm {
              advertiserCurrency
            }
            videoCompletionRate
            viewability
            winRate
          }
        }
      }
    }
  }
}
```

#### Look up ad groups for multiple advertiser IDs

The following GraphQL query retrieves the name and ID for ad groups across three advertisers.

```
query GetAdGroupForMultipleAdvertiserIdsExample {
  adGroups(where: { advertiserId: { in: ["ADVERTISER_ID__PLACEHOLDER_1", "ADVERTISER_ID__PLACEHOLDER_2", "ADVERTISER_ID__PLACEHOLDER_3"] } }) {
    nodes {
      id
      name
    }
  }
}
```

#### Look up invisible or disabled ad groups

The following GraphQL query retrieves the names, IDs, visibility, and statuses of ad groups that are either disabled or invisible across three different advertisers.

```
query GetInvisibleOrDisabledAdGroupsExample {
  adGroups(
    where: {
      and: {
        advertiserId: {
          in: ["ADVERTISER_ID__PLACEHOLDER_1", "ADVERTISER_ID__PLACEHOLDER_2", "ADVERTISER_ID__PLACEHOLDER_3"]
        }
        or: { isEnabled: { eq: false }, isVisible: { eq: false } }
      }
    }
  ) {
    edges {
      cursor
      node {
        id
        name
        isVisible
        isEnabled
      }
    }
    pageInfo {
      endCursor
      hasNextPage
      hasPreviousPage
      startCursor
    }
  }
}
```

#### Look up ad group settings

The following GraphQL query retrieves the ad group settings.

```
query GetAdGroupSettingsExample($adGroupId: ID!) {
  adGroup(id: $adGroupId) {
    id
    name
    KoaSettings {
      areFutureFeaturesEnabled
      areFutureFeaturesEnabledForPartner
      optimizationsVersion
    }
    industryCategory {
      id
      name
      parentCategoryId
      isDefault
      isSensitive
    }
    availableIndustryCategories {
      id
      name
      parentCategoryId
      isDefault
      isSensitive
    }
  }
}
```

#### Look up ad group Prism setting

The following GraphQL query checks whether Prism is available and enabled for an ad group.

```
query GetAdGroupPrism ($adGroupId: ID!) {
  adGroup(id: $adGroupId) {
    audienceSettings {
        dataSettings {
            prism {
                isEnabled
            }
        }
    }
  }
}
```

#### Look up ad group metadata

The following GraphQL query retrieves Ad Group (**Ag**) tile metadata from the UI programmatic table.

```
query GetAdGroupTileMetadataExample ($adGroupId: ID!) {
  adGroup(id: $adGroupId) {
    id
    name
    programmaticTiles {
      isUserOptimized
      metadataSummaries
      type
    }
  }
}
```

## Common issues

The following table lists the common issues that prevent ad group spend and recommends possible solutions.

| Issue | Solution |
| --- | --- |
| The ad group does not have at least one bid list of type `TargetList` or `BlockList` associated and enabled. | Use PUT /v3/adgroup and use the `AssociatedBidLists` property to associate and enable at least one bid list. |
| The ad group is disabled. | Use the adGroupUpdate mutation and set the `IsEnabled` property to `true`. |
| The ad group does not have creatives assigned. | Use PUT /v3/adgroup or the adGroupAssociateCreative mutation to add at least one creative in the `CreativeIds` property. |
| The ad group is associated with a bid list of type `TargetList` but the bid list is missing bid lines. | Use PUT /v3/adgroup to disassociate the bid list, or use PUT /v3/bidlist to add bid lines to the bid list. |
| The ad group cannot have additional flights when updating a campaign through the platform UI. | To remove flights from an ad group, you must use the platform UI. **NOTE**: You can remove only current flights from an ad group. |
| An ad group needs to be created and opted out of SP500+. | Set the `MarketplaceOptOut` parameter to `true`. |

## FAQs

### How can I improve the user experience using the ad group endpoints?

For an improved user experience, integrate our API endpoints with your client-based UI. For example, you can clone and manage campaigns and ad groups in the backend, and then use our API endpoints for adjusting budgets and bid lists on a daily basis within your UI.

### How can I automatically opt cloned ad groups into my current marketplace?

In GraphQL, use the `DefaultUseInventoryMarketPlace` property. It enables campaigns to automatically opt cloned ad groups into your current marketplace. For details, see Automatically opt cloned ad groups into marketplace.

### What happens if I don't set my ad group KPIs in a campaign that has multiple goals?

The primary campaign goal becomes the default KPI for all ad groups in the campaign.

### What happens if the channels in the ad group and campaign do not match?

When ad group and campaign channels are mismatched, only the ad group's channel is used for bidding.

For best practices, be sure ad groups have the same value in their `ChannelId` properties as the channel of the parent campaign. To target multiple channels and use the same campaign settings, clone the campaign and update the channel for the new copy of the campaign. For details, see Channels.

### Can I allocate the budget during ad group creation?

No. You can use only the `campaignBudgetSettingsUpdate` mutation to allocate the budget, and only after you have created the ad group. For details, see Update campaign budget and other settings.

### How do I use GraphQL to associate an ad group to a new campaign flight?

Use the `campaignFlightUpdate` mutation. For an example, see Update a campaign flight.

### Can I enable Prism for all ad groups?

Yes. For details, see Prism.
