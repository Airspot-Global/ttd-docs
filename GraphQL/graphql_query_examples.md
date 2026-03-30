# Campaign Details and Insights

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/CampaignQueryExamplesGQL
- Category: GraphQL

---

# Campaign Details and Insights

The following sections provide a list of commonly used GraphQL queries that you can use to retrieve [campaign](/v3/portal/api/doc/Campaigns) information.

> **TIP**: If you're new to GraphQL, explore our [GraphQL API Resource Hub](/v3/portal/resources/doc/GqlApiHub) to learn the basics—like query anatomy, authentication, and rate limits—as well as how to run [bulk queries](/v3/portal/api/doc/GqlBulkOperations).

## 

Campaign Performance Reporting Queries[](#reporting)

With the GraphQL API, you can create and customize `campaign` queries and include `reporting` fields that provide key performance metrics for tracking KPIs, cost and bidding, media quality, and overall effectiveness. You can either retrieve lifetime data or organize it by day or hour to help analyze trends, optimize bids, and measure engagement effectively. Whether you're evaluating media efficiency or optimizing your bidding strategy, these detailed performance metrics can help you make informed, data-driven decisions.

> **TIP**: You can also use the `reporting` field to retrieve performance metrics at the [advertiser](/v3/portal/api/doc/AdvertiserGQLQueryExamples#reporting) and [ad group](/v3/portal/api/doc/AdGroup#reporting) level.

The following sections provide GraphQL queries you can use to retrieve reporting metrics that track the performance of a campaign. These metrics can also be found in the Reports (**Rp**) tile in the platform UI.

### 

Look Up Campaign Lifetime Impressions and Spend[](#lifetime)

The following `campaign` GraphQL query retrieves the number of impressions and total spend of a campaign across all its current and past flights.

query GetCampaignLifetimeMetricsExample($campaignId: ID!) {

  campaign(id: $campaignId) {

    reporting {

      lifetimeImpressions

      lifetimeSpendInAdvertiserCurrency

    }

  }

}

For more granular metrics, see [Look Up Campaign Performance Metrics by Date Range](#general).

### 

Look Up Campaign Performance Metrics by Date Range[](#general)

Here's what you need to know about looking up campaign performance metrics by date range:

*   These metrics also include data from all of the ad groups in a campaign.
*   You can filter the metrics only by date.
*   If you don't include a date range in the `where` filter, the query returns the campaign's lifetime metrics.
*   You can retrieve metrics at the following time intervals, specified in the `dimensions` field:
    *   Hourly (last 30 days)
    *   Daily (last year)
*   If you don’t include the `dimensions` field, the query returns aggregated totals for each metric without grouping data by time interval. See also [Look Up Campaign Lifetime Impressions and Spend](#lifetime).

The following `campaign` GraphQL query retrieves all campaign metrics you can use to optimize campaign performance, manage spend and bidding, and so on. The date range is specified using `gte` (start, inclusive) and `lte` (end, inclusive) for the reporting period.

query GetCampaignPerformanceMetricsbyDateRangeExample($campaignId: ID!) 

{

  campaign(id: $campaignId) {

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

## 

Miscellaneous Campaign Data Queries[](#misc)

The following sections provide GraphQL queries you can use to look up campaign data and key metrics such as projected spend, forecasted spend, and relevance.

### 

Look Up Campaign Data[](#campaign-shopping-cart)

The following GraphQL query retrieves campaign-level data for a campaign ID.

query GetCampaignLevelDataExample($campaignId: ID!) {

  campaign(id: $campaignId) {

    currentOrNextFlight {

      daysRemaining

      forecast {

        projectedSpend

        relevance

        confidence

        lastUpdated

      }

      adGroupFlights {

        nodes {

          forecast {

            projectedSpend

            relevance

            confidence

            lastUpdated

          }

          adGroupId

        }

      }

    }

  }

}

### 

Look Up Campaign with Ad Groups[](#campaign-ad-groups)

The following GraphQL query retrieves the ID and name for a campaign and, for each campaign returned, the name and ID of each ad group in the campaign.

query GetCampaignWithAdGroupsExample($campaignId: ID!) {

  campaign(id: $campaignId) {

    id

    name

    adGroups {

      edges {

        node {

          id

          name

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

}

### 

Look Up Campaign Flights[](#campaign-flights)

The following GraphQL query uses a `flights` filter to retrieve campaign flight IDs and the maximum amount each flight may spend. To learn more about using filters, see [GraphQL API Queries](/v3/portal/resources/doc/GqlApiQueries#filters) in our GraphQL Resource Hub.

query GetFlightDataExample($campaignId: ID!, $campaignFlightId1: Long, 

$campaignFlightId2: Long) {

  campaign(id: $campaignId){

    id

    name

    flights(where: {id: {in: \[$campaignFlightId1, 

    $campaignFlightId2\]}}){

      nodes{

        id

        budgetInAdvertiserCurrency

      }

    }

  }

}

### 

Look Up Campaign Programmatic Table Data[](#campaign-tiles)

The following GraphQL query retrieves campaign-level metadata that appears on the Programmatic Table tiles in the UI.

query GetCampaignProgrammaticTableDataExample($campaignId: ID!) {

  campaign(id: $campaignId) {

    id

    name

    programmaticTiles {

      isKoaOptimized

      isUserOptimized

      metadataSummaries

      type

    }

  }

}

### 

FAQs

The following is a list of frequently asked questions about GraphQL queries for campaigns.

### 

How often do the Projected Spend and Relevance metrics get updated?

The following table lists how frequently the Projected Spend and Relevance metrics are updated.

| Metric | Update Frequency |
| Projected Spend | 

*   Approximately 2 hours after a campaign or ad group change
*   Once a day

 |
| Relevance | 

*   After a campaign change
*   Every two days

 |