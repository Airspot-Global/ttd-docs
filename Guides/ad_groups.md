# Ad Groups

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/AdGroup
- Category: Guides

---

# Ad Groups

An ad group is a strategy that falls within a particular [campaign](/v3/portal/api/doc/Campaigns) and enables you to assemble targeting strategies to specify when, where, and how to serve ads. You can manage budgets, goals, creatives, site lists, inventory, and viewability, as well as targeting options for audiences, devices, locations, languages, times of day, and video adjustments across ad groups.

The Trade Desk offers flexible options for creating and managing ad groups. Here's what you need to know:

*   You can use both the REST API and the GraphQL API to create and manage your ad groups, except for budget allocation and pacing, for which you must use GraphQL. For details, see [REST and GraphQL API Comparison](#gql-rest).
*   If you want to create or update multiple ad groups at once, you must use the GraphQL API for [GraphQL API Bulk Operations](/v3/portal/api/doc/GqlBulkOperations).
*   To enable an ad group, it must be associated with a campaign and have at least one approved creative. While you can create an ad group with an empty `CreativeIds` array, you cannot enable it until you upload a creative for the ad group.
*   By default, ad groups have zero allocation, allowing the platform algorithm to allocate the flight budget to where it finds the most value.
*   Any budget manually allocated to ad groups by using the `minimumSpendInAdvertiserCurrency` ad group flight property is automatically reserved, regardless of whether the ad groups are active and able to spend (`isEnabled` property).
*   You can set ad group pacing only at the campaign level.
*   If a campaign is in Kokai and has the [Sellers and Publishers 500+ (SP500+) Marketplace](/v3/portal/api/doc/SP500) enabled, any ad group you create that is associated with that campaign will automatically inherit SP500+ access.

## 

Setup and Optimization[](#features)

The following table lists the properties you must include in all ad groups.

| Property | Notes |
| [Funnel Location](#funnel-location) | 

*   The funnel location (awareness, consideration, conversion) helps measure the success of your ad groups effectively.
*   If not explicitly set, it's automatically set based on the originating campaign's primary goal.

 |
| [Goal](/v3/portal/api/doc/GoalsKPIs) or KPI | 

*   If not explicitly set, the goal or KPI is automatically set based on the originating campaign's primary goal.
*   Ad groups must also have them either set directly or inherited from their parent campaign.
*   The default KPI is "Reach".

 |

You can also optimize ad groups by taking advantage of [performance-enhancing features](#ad-group-koa-features), such as Predictive Clearing and Identity Alliance.

> **IMPORTANT**: To set up and manage ad group budgets, you must use GraphQL. For details on budget types and pacing options, see [Budget Allocation](/v3/portal/api/doc/CampaignBudgets).

## 

REST and GraphQL API Comparison[](#gql-rest)

To create, update, or query ad groups, you can use the REST and the GraphQL API. The following table lists the differences between the GraphQL and REST APIs and how many ad groups you can create, update, and query per call.

> **NOTE**: The update and create mutations for individual ad groups are not fully featured yet. Check for [updates](/v3/portal/api/doc/ReleaseNotes) as we roll out new features and enhancements.

| Operation | REST API | GraphQL API | Notes |
| Create | Only one ad group | Individually or in bulk, using a simplified set of fields | For details, see [Create an Ad Group](#createadgroups) and [GraphQL API Bulk Operations](/v3/portal/api/doc/GqlBulkOperations). |
| Clone | N/A | Only with the parent campaign | You can choose to clone all, none, or a selection of ad groups with the parent campaign. For details, see [Clone Campaigns](/v3/portal/api/doc/CampaignCloning). |
| Read (query) | Only one ad group | Individually or in bulk, using custom queries | For details, see [Look Up Ad Groups](#lookupadgroups). |
| Update | Only one ad group | In bulk, using a simplified set of fields | For details, see [Update an Ad Group](#updateadgroups) and [GraphQL API Bulk Operations](/v3/portal/api/doc/GqlBulkOperations). |
| Manage budget allocation and pacing | N/A | In bulk and per campaign | For details, see [Budget Allocation](/v3/portal/api/doc/CampaignBudgets). |

## 

Funnel Location[](#funnel-location)

An ad group funnel location identifies the focus or objective of your ad group (awareness, consideration, and conversion). For example, you may want to focus on getting people to consider your business, encourage them to make a purchase, or sign up for an event.

To measure the success of your ad groups effectively, you must set the `FunnelLocation` value when you [create](#createadgroups) your ad group:

| Funnel Location | Value | Description |
| Awareness | `AWARENESS` | Generate interest in your brand. Discover qualified leads to increase brand knowledge and reach as many people as possible in your target audience. Increasing brand awareness is about telling people what makes your business valuable. |
| Consideration | `CONSIDERATION` | Get people to think about your business and seek more information. Reach new customers and influence them to become prospective customers. |
| Conversion | `CONVERSION` | Encourage prospective customers who are already interested in your business to take a specific action. |

## 

Performance-Enhancing Features[](#ad-group-koa-features)

Here's what you need to know about performance-enhancing features for ad groups:

*   To enable a feature, set the corresponding property value to `true`. For an example of an ad group with some of the key performance-enhancing features turned on, see [Request Example](#ad-group-create).
*   All feature properties, except Predictive Clearing and Koa Optimizations, are part of the `RTBAttributes.AudienceTargeting` object.
*   Some features, like Audience Booster, apply only to ad groups with certain KPIs. Other features are mutually exclusive as noted in the feature and property descriptions.

The following table lists performance-enhancing features available for ad groups. The list indicates the ad group API settings for each feature and provides links to the Knowledge Portal pages and other resources where you can learn more.

| Feature | API Property | Description | Fee-Based? |
| [Predictive Clearing](/v3/portal/api/doc/PredictiveClearing) | `PredictiveClearingEnabled` | Predictive Clearing is a cost-saving feature that helps you win more impressions at a lower CPM while optimizing ad spend and improving campaign performance. When you turn on Predictive Clearing, it analyzes historical clearing prices to find a lower, optimal bid for each impression served in a first-price auction. | Yes |
| [Koa Optimizations](/v3/portal/api/doc/KoaOptimizations) | `KoaDimensions` | Koa Optimizations is off by default. When turned on, it enables Koa, the artificial intelligence that powers The Trade Desk platform, to automatically generate optimizations for the ad group dimensions that you specify. | No |
| [Identity Alliance](/v3/portal/api/doc/CrossDeviceTargeting) | `CrossDeviceVendorListForAudience` | Enables the platform to select the right option for a user across all cross-device vendors on an impression-by-impression basis.  
Set `CrossDeviceVendorId` to `10` for Identity Alliance (person) or `11` for Identity Alliance (household). For details, see [Cross-Device Targeting](/v3/portal/api/doc/CrossDeviceTargeting). | Yes |
| [Prism](/v3/portal/api/doc/Prism) | `AudienceExcluderEnabled` | Creates a custom audience for the ad group by excluding data segments that are less relevant to the advertiser's target audience. In other words, this custom audience increases the value of a campaign by focusing on the most valuable impressions and excluding users who are less likely to benefit the campaign. Here's what you need to know about this property:

*   This property cannot be used in conjunction with Audience Predictor.
*   Advertisers in the following IAB categories may not use this functionality: Personal Finance, Careers, Real Estate.

. | Yes |
| Audience Predictor | `AudiencePredictorEnabled` | Enables the platform to use the lookalike model data to create and continuously update an audience of users who are most likely to convert, and target them in your audience. Here's what you need to know about this functionality:

*   Enabling this functionality generates a custom audience. It is not compatible with Prism.
*   Advertisers in the following IAB categories cannot use third-party data or custom modeling sources with Audience Predictor: Personal Finance, Careers, Real Estate.

 | Yes |
| Adding Segments Resembling Your Target Customer | `AudienceBoosterEnabled` | A performance-enhancing functionality for conversion-based campaigns that have cost per acquisition (CPA) or return on ad spend (ROAS) as the primary goal. This functionality adds high-performing data segments that are similar to the advertiser's target audience. In other words, ads will be served only to users who benefit from the campaign and are most likely to convert. By default, it is set to `false`.  
**IMPORTANT**: This feature applies only to ad groups that have CPA or ROAS goals. | No |
| [News Navigator](https://desk.thetradedesk.com/knowledge-portal/en/inv-news-navigator.html) | `isNewsNavigatorEnabled` | Prioritizes reliable and objective news as scored by third-party news rating partners. Available through GraphQL only. By default, it is set to `true`. | No |

To enable a feature, set the corresponding property value to `true`. Some features, like Audience Booster, apply only to ad groups with certain KPIs. Other features are mutually exclusive as noted in the feature and property descriptions.

> **TIP**: For an example of an ad group with some of the key performance-enhancing features turned on, see [Request Example](#ad-group-create).

## 

Create an Ad Group[](#createadgroups)

To create an ad group, use either the [REST](#createadgroups-rest) API or [GraphQL](#createadgroups-gql) API.

> **TIP**: If you want to update multiple ad groups at once, use [bulk operations](/v3/portal/api/doc/GqlBulkOperations) in GraphQL.

### 

REST API[](#createadgroups-rest)

To create an ad group with the REST API, use the [POST /v3/adgroup](/v3/portal/api/ref/post-adgroup) endpoint with a minimum of the required fields listed in the following table. If you want to create multiple ad groups at once, use [bulk operations](/v3/portal/api/doc/GqlBulkOperations) in the GraphQL API.

> **TIP**: To prioritize best-performing and most relevant inventory based on your ad group's goals, consider turning on the [performance-enhancing settings](#ad-group-koa-features).

| Property Name | Required | RTB Attribute? | Notes |
| `CampaignId` | Required | No | The ID of the campaign associated with the ad group. |
| `AdGroupName` | Required | No | Specify a name that follows your naming conventions, if you have any. For example, include the audience, geographic location, and other details that will help you identify the ad group. |
| `AdGroupCategory` | Conditionally Required, Nullable | No | Required if the advertiser's industry category ID is not set. If set to `null`, the advertiser category will be used.  
**NOTE**: The Trade Desk uses the IAB Tech Lab Content Taxonomy [version 2.2](https://iabtechlab.com/wp-content/uploads/2020/12/Implementation_Guide_for_Brand_Suitability_with_IABTechLab_Content_Taxonomy_2-2.pdf) for assigning industry categories to advertisers. If you want to see how version 1.0 maps to version 2.2, see [IAB Content Taxonomy Mapping: Version 1.0 to 2.2](/v3/portal/openpath/doc/TaxonomyMapping). |
| `FunnelLocation` | Required | No | For details, see [Funnel Location](#funnel-location). |
| `Channel` | Required | No | Channels inform bidding behavior and provide recommendations and insights. For details, see [Channels](/v3/portal/api/doc/Channel). |
| `BaseBidCPM` | Required | RTB Attribute | CPM is used to define base and max bids. The base bid is the starting bid for an impression before bid adjustments from private contracts, bid lists, and optimizations. By setting a higher base bid for a valuable segment, you indicate a willingness to pay more for those impressions, improving your chances of winning them. |
| `CreativeIds` | Required | RTB Attribute | A list of the creative IDs that this ad group serves. Here's what you need to know about this property:

*   Ad groups require at least one approved creative to spend.
*   An ad group with no creatives will not spend.
*   You can include an empty array but be sure to upload your creatives before enabling your ad group.

 |
| `MaxBidCPM.Amount` | Required | RTB Attribute | The max bid must be greater than or equal to the minimum base bid threshold for the partner. The max bid is the highest amount an ad group will bid on a single impression. |
| `ROIGoal` | Required | RTB Attribute | [Goals](/v3/portal/api/doc/GoalsKPIs), or KPIs, measure the success of the ad group while driving performance and delivering results. An ad group can have its own goal set directly or inherit it from its parent campaign. Otherwise, the default value is `Reach`. |
| `AssociatedBidLists` | Recommended | No | A list of IDs of the [bid lists](/v3/portal/api/doc/BidList) to associate with this ad group. Here's what you need to know about this property:

*   You can associate bid lists with ad groups directly when creating or updating them.
*   You can use the `IncludeDefaultsFromCampaign` property to have bid lists inherited from the parent campaign when creating ad groups.
*   To enable the bid lists, set the `IsEnabled` property to `true`.

 |

#### Request Example

The following is an example of a [POST](/v3/portal/api/ref/post-adgroup) request to create an ad group targeting display ads with CPA as its ROI goal. Aside from the required properties, to enhance the ad group's performance, the request also turns on several [performance-enhancing features](#ad-group-koa-features), such as Predictive Clearing and Identity Alliance.

{

   "CampaignId":"{CAMPAIGN\_ID\_PLACEHOLDER}",

   "AdGroupName":"Strategy 1",

   "AdGroupCategory":{

      "CategoryId":8311

   },

   "PredictiveClearingEnabled":true,

   "FunnelLocation": "Awareness",

   "RTBAttributes":{

      "ROIGoal":{

         "CPAInAdvertiserCurrency":{

            "Amount":0.2,

            "CurrencyCode":"USD"

         }

      },

      "AudienceTargeting":{

         "CrossDeviceVendorListForAudience":\[

            {

               "CrossDeviceVendorId":11,

               "CrossDeviceVendorName":"Identity Alliance"

            }

         \]

      },

      "BaseBidCPM":{

         "Amount":1.0,

         "CurrencyCode":"USD"

      },

      "MaxBidCPM":{

         "Amount":5.0,

         "CurrencyCode":"USD"

      },

      "CreativeIds":\[

      \]

   },

   "AssociatedBidLists":\[

   \]

}

> **NOTE**: The provided request example does not include the `KoaOptimizationSettings.KoaDimensions` properties in the `RTBAttributes` object. With the exception of advertisers in certain industries, such as Careers, Medical Health, Personal Finance, and Real Estate, Koa Optimizations will be disabled for the newly created ad group. For details and instructions on how to enable it for certain dimensions, see [Koa Optimizations](/v3/portal/api/doc/KoaOptimizations). See also [FAQs](#faqs).

### 

GraphQL API[](#createadgroups-gql)

To create an ad group with the GraphQL API, use the `adGroupCreate` mutation.

> **TIP**: If you want to create multiple ad groups at once, you must use the GraphQL API for [bulk operations](/v3/portal/api/doc/GqlBulkOperations).

The following mutation example creates an ad group targeting CTV ads for maximum reach in brand awareness. It also enables [Predictive Clearing](/v3/portal/api/doc/PredictiveClearing) to enhance the ad group's performance.

mutation {

    adGroupCreate(

        input: {

            campaignId: "CAMPAIGN\_ID\_PLACEHOLDER"

            name: "AD\_GROUP\_NAME\_PLACEHOLDER"

            description: "AD\_GROUP\_DESCRIPTION\_PLACEHOLDER"

            isEnabled: true

            channel: DISPLAY

            funnelLocation: AWARENESS

            roiGoal: { maximizeReach: true }

            baseBidCPMInAdvertiserCurrency: 25

            maxBidCPMInAdvertiserCurrency: 40

            koaOptimizationSettings: { predictiveClearingEnabled: true 

            }

            creativeIdsToAdd: \["CREATIVE\_ID\_PLACEHOLDER"\]

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

Update an Ad Group[](#updateadgroups)

To update an ad group, use either the [REST](#rest-apis-update) API or [GraphQL](#gql-update) API.

> **TIP**: If you want to update multiple ad groups at once, use [bulk operations](/v3/portal/api/doc/GqlBulkOperations) in GraphQL.

### 

REST API[](#rest-apis-update)

Depending on your needs and preferences, you can update a single ad group using either of the following APIs:

| Task | Endpoint | Notes |
| Update the details of a specific ad group. | [PUT /v3/adgroup](/v3/portal/api/ref/put-adgroup) | When updating ad groups with list objects, such as `AssociatedBidLists` and `CreativeIds`, each list is replaced with the new content provided.  
**IMPORTANT**: To avoid overwriting any lists, retrieve the current state of these objects using the [GET /v3/adgroup/{adGroupId}](/v3/portal/api/ref/get-adgroup-adgroupid) endpoint and include the entire list, including changes, in the PUT request. |
| Enable or disable a specific ad group. | [PUT /v3/adgroup/status](/v3/portal/api/ref/put-adgroup-status) | To check the current ad group status, use the [GET /v3/adgroup/status/{adGroupId}](/v3/portal/api/ref/get-adgroup-status-adgroupid) endpoint. |

### 

GraphQL API[](#gql-update)

Here is an example of the `adGroupUpdate` mutation you can use to update an individual ad group. It sets our curated Sellers and Publishers 500+ list as the market type for the ad group, with awareness as the funnel location.

> **TIP**: If you want to create or update multiple ad groups at once, you must use the GraphQL API for [bulk operations](/v3/portal/api/doc/GqlBulkOperations).

mutation {

    adGroupUpdate(

        input: {

            marketType: MARKETPLACE

            Id: "abc1234"

            funnelLocation: AWARENESS

        }

    ) {

        data {

            baseBidCPMInAdvertiserCurrency

            budgetInAdvertiserCurrency

            campaignStackRank

            channel

            dealsPresent

            description

            id

            isPrivateMarket

            isTemplate

            marketType

            maxBidCPMInAdvertiserCurrency

            name

        }

        userErrors {

            field

            message

        }

    }

}

#### Manage Creatives in an Ad Group

You can associate (assign) and disassociate multiple creatives from an ad group at once. Here is an example of the `adGroupAssociateCreative` mutation that adds two creatives, removes a creative, and retrieves the first 100 creatives associated with the ad group:

mutation {

    adGroupAssociateCreative(input: {adGroupId: 

    "AD\_GROUP\_ID\_PLACEHOLDER", creativeIdsToAdd: 

    \["CREATIVE\_ID\_PLACEHOLDER\_1", "CREATIVE\_ID\_PLACEHOLDER\_2"\], 

    creativeIdsToRemove: \["CREATIVE\_ID\_PLACEHOLDER\_3"\]}) {

        data {

            creatives(first:100) {

                nodes {

                    id

                }

            }

        }

        errors {

            ...on InSchemaError {

                field

                message

            }

        }

    }

}

## 

Look Up Ad Groups[](#lookupadgroups)

You can retrieve ad group details using either API:

*   [REST API](#rest-apis-look)
*   [GraphQL API](#gql-look)

To decide which API to use, see [GraphQL API and REST API Comparison](#gql-rest).

### 

REST API[](#rest-apis-look)

The following table lists the endpoints you can call to look up ad groups.

> **NOTE**: You cannot use the REST API to look up campaign-level data or invisible ad groups. To do that, see [GraphQL Campaign Query Examples](/v3/portal/api/doc/CampaignQueryExamplesGQL).

| Task | Endpoint | Returns All Details? | Available Filters |
| Retrieve details for a specific ad group. | [GET /v3/adgroup/{adGroupId}](/v3/portal/api/ref/get-adgroup-adgroupid) | Yes | N/A |
| Retrieve a filtered, paginated list of ad groups for a campaign ID. | [POST /v3/adgroup/query/campaign](/v3/portal/api/ref/post-adgroup-query-campaign) | Yes | `AdGroupId`  
`Availability`  
`CampaignId`  
`Description`  
`Name`  
`Type` |
| Retrieve a filtered, paged list of ad groups for an advertiser ID. | [POST /v3/adgroup/query/advertiser](/v3/portal/api/ref/post-adgroup-query-advertiser) | Yes | `AdGroupId`  
`Availability`  
`CampaignId`  
`Description`  
`Name`  
`Type` |
| Check the status (enabled or not) of a specific ad group. | [GET /v3/adgroup/status/{adGroupId}](/v3/portal/api/ref/get-adgroup-status-adgroupid) | No | N/A |
| Retrieve the name of a specific ad group based on its ID. | [GET /v3/adgroup/name/{adGroupId}](/v3/portal/api/ref/get-adgroup-name-adgroupid) | No | N/A |

### 

GraphQL API[](#gql-look)

The following sections provide a list of sample queries that retrieve ad group information.

*   [Look Up Ad Groups by Name](#ad-group-name)
*   [Look Up Campaign Data for an Ad Group](#ad-group-snapshot)
*   [Look Up Ad Group Performance Metrics by Date Range](#reporting)
*   [Look Up Ad Groups for Multiple Advertiser IDs](#ad-group-search)
*   [Look Up Invisible or Disabled Ad Groups](#ad-group-search-where)
*   [Look Up Ad Group Settings](#ad-group-settings)
*   [Look Up Ad Group Prism Setting](#ad-group-prism)
*   [Look Up Ad Group Metadata](#ad-group-tiles)

> **TIP**: In GraphQL, you can also run multiple queries at once. For details, see [GraphQL Bulk Operations: Queries](/v3/portal/api/doc/GqlBulkOperations).

#### Look Up Ad Groups by Name

The following GraphQL query retrieves ad groups by name. You can configure the query to reduce or change the types of data returned. Other options include omitting the partner ID, searching across multiple advertisers, and combining search terms using the "and" operator.

If you have more than 100 items in your search results, use [pagination](/v3/portal/resources/doc/GqlApiQueries#pagination) to return them.

query GetAdGroupsByNameExample {

    adGroups(

        first: 100

        where: {

            partnerId: { eq: "PARTNER\_ID\_PLACEHOLDER" }

            advertiserId: { eq: "ADVERTISER\_ID\_PLACEHOLDER" }

            name: { contains: "SEARCH\_TERM\_PLACEHOLDER" }

        }

    ) {

        nodes {

            id

            name

            isArchived

            budget {

                currentFlightBudget

                isFluid

                total

            }

            adGroupFlights {

                nodes {

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

#### Look Up Campaign Data for an Ad Group

The following GraphQL query retrieves campaign-level data for an ad group.

query GetCampaignKeyMetricDataForAdGroupExample {

    adGroup(id: "abc1234") {

        adGroupFlights {

            totalCount

            nodes {

                adGroupId

                forecast {

                    projectedSpend

                    relevance

                    confidence

                    lastUpdated

                }

            }

        }

        spend {

            spend

        }

    }

}

#### Look Up Ad Group Performance Metrics by Date Range

With the GraphQL API, you can create and customize `adGroup` queries and include `reporting` fields that provide key performance metrics for tracking KPIs, cost and bidding, media quality, and overall effectiveness. You can either retrieve lifetime data or organize it by day or hour to help analyze trends, optimize bids, and measure engagement effectively. Whether you're evaluating media efficiency or optimizing your bidding strategy, these detailed performance metrics can help you make informed, data-driven decisions.

> **TIP**: You can also use the `reporting` field to retrieve performance metrics at the [advertiser](/v3/portal/api/doc/AdvertiserGQLQueryExamples#reporting) and [campaign](/v3/portal/api/doc/CampaignQueryExamplesGQL#reporting) level.

Here's what you need to know about looking up ad group performance metrics by date range:

*   You can filter the metrics only by date.
*   If you don't include a date range in the `where` filter, the query returns the ad group's lifetime metrics.
*   You can retrieve metrics at the following time intervals, specified in the `dimensions` field:
    *   Hourly (last 30 days)
    *   Daily (last year)
*   If you don’t include the `dimensions` field, the query returns aggregated totals for each metric without grouping data by time interval.

The following `adGroup` GraphQL query retrieves all metrics you can use to optimize campaign performance, manage spend and bidding, and so on. The date range is specified using `gte` (start, inclusive) and `lte` (end, inclusive) for the reporting period.

query GetAdGroupPerformanceMetricsbyDateRangeExample($adGroupId: ID!) {

  adGroup(id: $adGroupId) {

    reporting {

      generalReporting(

        where: { date: { gte: "2025-02-01", lte: "2025-02-28" } }

      ) {

        nodes {

          dimensions {

            time {

              day

            }

          }

          metrics {

            adPlays

            baseBid {

              advertiserCurrency

            }

            bidCpm {

              advertiserCurrency

            }

            bids

            clicks

            completionRate

            conversions

            cpa {

              advertiserCurrency

            }

            cpc {

              advertiserCurrency

            }

            cpcv {

              advertiserCurrency

            }

            cpm {

              advertiserCurrency

            }

            ctr

            customCpa {

              advertiserCurrency

            }

            customRoas {

              advertiserCurrency

            }

            impressions

            mediaCost {

              advertiserCurrency

            }

            mediaCpm {

              advertiserCurrency

            }

            nielsenOtp

            revenue

            roas {

              advertiserCurrency

            }

            spend {

              advertiserCurrency

            }

            tvQualityCpm {

              advertiserCurrency

            }

            tvQualityIndex

            vCpm {

              advertiserCurrency

            }

            viewability

            winRate

          }

        }

      }

    }

  }

}

#### Look Up Ad Groups for Multiple Advertiser IDs

The following GraphQL query retrieves the name and ID for ad groups across three advertisers.

query GetAdGroupForMultipleAdvertiserIdsExample {

  adGroups(where: { advertiserId: { in: 

  \["ADVERTISER\_ID\_\_PLACEHOLDER\_1", "ADVERTISER\_ID\_\_PLACEHOLDER\_2", 

  "ADVERTISER\_ID\_\_PLACEHOLDER\_3"\] } }) {

    nodes {

      id

      name

    }

  }

}

#### Look Up Invisible or Disabled Ad Groups

The following GraphQL query retrieves the names, IDs, visibility, and statuses of ad groups that are either disabled or invisible across three different advertisers.

query GetInvisibleOrDisabledAdGroupsExample {

  adGroups(

    where: {

      and: {

        advertiserId: {

          in: \["ADVERTISER\_ID\_\_PLACEHOLDER\_1", 

          "ADVERTISER\_ID\_\_PLACEHOLDER\_2", 

          "ADVERTISER\_ID\_\_PLACEHOLDER\_3"\]

        }

        or: { isEnabled: { eq: false }, isVisible: { eq: false } }

      }

    }

  ) {

    edges {

      cursor

      node {

        id

        name

        isVisible

        isEnabled

      }

    }

    pageInfo {

      endCursor

      hasNextPage

      hasPreviousPage

      startCursor

    }

  }

}

#### Look Up Ad Group Settings

The following GraphQL query retrieves the ad group settings.

query GetAdGroupSettingsExample($adGroupId: ID!) {

  adGroup(id: $adGroupId) {

    id

    name

    KoaSettings {

      areFutureFeaturesEnabled

      areFutureFeaturesEnabledForPartner

      optimizationsVersion

    }

    industryCategory {

      id

      name

      parentCategoryId

      isDefault

      isSensitive

    }

    availableIndustryCategories {

      id

      name

      parentCategoryId

      isDefault

      isSensitive

    }

  }

}

#### Look Up Ad Group Prism Setting

The following GraphQL query checks whether Prism is available and enabled for an ad group.

query GetAdGroupPrism ($adGroupId: ID!) {

  adGroup(id: $adGroupId) {

    audienceSettings {

        dataSettings {

            prism {

                isEnabled

            }

        }

    }

  }

}

#### Look Up Ad Group Metadata

The following GraphQL query retrieves Ad Group (**Ag**) tile metadata from the UI programmatic table.

query GetAdGroupTileMetadataExample ($adGroupId: ID!) {

  adGroup(id: $adGroupId) {

    id

    name

    programmaticTiles {

      isUserOptimized

      metadataSummaries

      type

    }

  }

}

## 

Archive Ad Groups with GraphQL[](#archive)

> **IMPORTANT**: An ad group that is archived cannot be restored.

To archive one or more ad groups at once, use the `adGroupsArchive` mutation. The following example archives two ad groups and returns a list of their IDs.

mutation {

    adGroupsArchive(input: { ids: \["AD\_GROUP\_ID\_PLACEHOLDER\_1", 

    "AD\_GROUP\_ID\_PLACEHOLDER\_2"\] }) {

        data

        errors {

            ... on InSchemaError {

                field

                message

            }

        }

    }

}

## 

REST API Troubleshooting Tips[](#troubleshootadgroups)

> **TIP**: If your ad group is not spending to your expectations, consider turning on performance-enhancing features.

To form a complete picture of all of the targeting, blocking, and optimizations applied to an ad group, look up the enabled bid lists for the ad group, campaign, advertiser, and partner.

| Task | Endpoint | Includes Bid Line Details? |
| Look up bid lists associated with and enabled for an ad group. | [GET /v3/adgroup/{adGroupId}](/v3/portal/api/ref/get-adgroup-adgroupid) | No |
| Look up bid lists associated with and enabled for the parent campaign. | [GET /v3/campaign/{campaignId}](/v3/portal/api/ref/get-campaign-campaignid) | No |
| Look up bid lists associated with and enabled for the parent advertiser. | [GET /v3/advertiser/{advertiserId}](/v3/portal/api/ref/get-advertiser-advertiserid) | No |
| Look up bid lists associated with and enabled for the parent partner. | [GET /v3/partner/{partnerId}](/v3/portal/api/ref/get-partner-partnerid) | No |
| Look up bid list details. | [GET /v3/bidlist/{bidListId}](/v3/portal/api/ref/get-bidlist-bidlistid) | Yes |

### 

Common Issues

The following table lists the common issues that prevent ad group spend and recommends possible solutions.

| Issue | Solution |
| The ad group does not have at least one bid list of type `TargetList` or `BlockList` associated and enabled. | Use [PUT /v3/adgroup](/v3/portal/api/ref/put-adgroup) and use the `AssociatedBidLists` property to associate and enable at least one bid list. |
| The ad group is disabled. | Use [PUT /v3/adgroup/status](/v3/portal/api/ref/put-adgroup-status) and set the `IsEnabled` property to `true`. |
| The ad group does not have creatives assigned. | Use [PUT /v3/adgroup](/v3/portal/api/ref/put-adgroup) or the [adGroupAssociateCreative mutation](#associate-creative) to add at least one creative in the `CreativeIds` property. |
| The ad group is associated with a bid list of type `TargetList` but the bid list is missing bid lines. | Use [PUT /v3/adgroup](/v3/portal/api/ref/put-adgroup) to disassociate the bid list, or use [PUT /v3/bidlist](/v3/portal/api/ref/put-bidlist) to add bid lines to the bid list. |
| The ad group cannot have additional flights when updating a campaign through the platform UI. | To remove flights from an ad group, you must use the platform UI.  
**NOTE**: You can remove only current flights from an ad group. |
| An ad group needs to be created and opted out of SP500+. | Set the `MarketplaceOptOut` parameter to `true`. |

## 

FAQs[](#faqs)

### 

How can I improve the user experience using the ad group endpoints?

For an improved user experience, integrate our API endpoints with your client-based UI. For example, you can clone and manage campaigns and ad groups in the backend, and then use our API endpoints for adjusting budgets and bid lists on a daily basis within your UI.

### 

How can I automatically opt cloned ad groups into my current marketplace?

In GraphQL, use the `DefaultUseInventoryMarketPlace` property. It enables campaigns to automatically opt cloned ad groups into your current marketplace. For details, see [Automatically Opt Cloned Ad Groups Into Marketplace](/v3/portal/api/doc/CampaignCloning#opt-marketplace).

### 

What happens if I don't set my ad group KPIs in a campaign that has multiple goals?

The primary campaign goal becomes the default KPI for all ad groups in the campaign.

### 

What happens if the channels in the ad group and campaign do not match?

When ad group and campaign channels are mismatched, only the ad group's channel is used for bidding.

For best practices, be sure ad groups have the same value in their `ChannelId` properties as the channel of the parent campaign. To target multiple channels and use the same campaign settings, clone the campaign and update the channel for the new copy of the campaign. For details, see [Channels](/v3/portal/api/doc/Channel).

### 

Can I allocate the budget during ad group creation?

No. You can use only the `campaignBudgetSettingsUpdate` mutation to allocate the budget, and only after you have created the ad group. For details, see [Update Campaign Budget and Other Settings](/v3/portal/api/doc/CampaignBudgets#mutations-budget-settings).

### 

How do I use GraphQL to associate an ad group to a new campaign flight?

Use the `campaignFlightUpdate` mutation. For an example, see [Update a Campaign Flight](/v3/portal/api/doc/CampaignBudgets#update-flight).

### 

I thought Koa Optimizations was off by default for newly created ad groups. Why do I see it enabled?

While [Koa Optimizations](/v3/portal/api/doc/KoaOptimizations) is typically disabled by default for new ad groups, there is an exception for certain industries. If your ad group belongs to certain categories like Careers, Medical Health, Personal Finance, or Real Estate, Koa Optimizations is automatically enabled for all dimensions except `Site`. This is part of the platform's default behavior to optimize for specific advertiser categories in different geographies.

### 

Can I enable Prism for all ad groups?

Yes. For details, see [Prism](/v3/portal/api/doc/Prism).