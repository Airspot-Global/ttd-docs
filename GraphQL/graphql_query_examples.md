# Campaign Details and Insights

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/CampaignQueryExamplesGQL
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/doc/CampaignQueryExamplesGQL (retired)
- Retrieved: 2026-11-14
- Category: GraphQL

---

# Campaign details and insights

The following sections provide a list of commonly used GraphQL queries that you can use to retrieve campaign information.

> **TIP**: If you're new to GraphQL, explore our GraphQL API Resource Hub to learn the basics—like query anatomy, authentication, and rate limits—as well as how to run bulk queries.

## Campaign performance reporting queries

With the GraphQL API, you can create and customize `campaign` queries and include `reporting` fields that provide key performance metrics for tracking KPIs, cost and bidding, media quality, and overall effectiveness. You can either retrieve lifetime data or organize it by day or hour to help analyze trends, optimize bids, and measure engagement effectively. Whether you're evaluating media efficiency or optimizing your bidding strategy, these detailed performance metrics can help you make informed, data-driven decisions. For details, see On-demand reporting queries.

> **TIP**: You can also use the `reporting` field to retrieve performance metrics at the advertiser and ad group level.

The following sections provide GraphQL queries you can use to retrieve reporting metrics that track the performance of a campaign. These metrics can also be found in the Reports (**Rp**) tile in the platform UI.

### Look up campaign lifetime impressions and spend

The following `campaign` GraphQL query retrieves the number of impressions and total spend of a campaign across all its current and past flights.

```
query GetCampaignLifetimeMetricsExample($campaignId: ID!) {
  campaign(id: $campaignId) {
    reporting {
      generalReporting {
        nodes {
          metrics {
            impressions
            spend {
              advertiserCurrency
            }
          }
        }
      }
    }
  }
}
```

For more granular metrics, see Look up campaign performance metrics by date range.

### Look up campaign performance metrics by date range

Here's what you need to know about looking up campaign performance metrics by date range:

- These metrics also include data from all of the ad groups in a campaign.
- You can filter the metrics only by date.
- If you don't include a date range in the `where` filter, the query returns the campaign's lifetime metrics.
- You can retrieve metrics at the following time intervals, specified in the `dimensions` field:

  - Hourly (last 30 days)
  - Daily (last year)

- If you don’t include the `dimensions` field, the query returns aggregated totals for each metric without grouping data by time interval. See also Look up campaign lifetime impressions and spend.

The following `campaign` GraphQL query retrieves all campaign metrics you can use to optimize campaign performance, manage spend and bidding, and so on. The date range is specified using `gte` (start, inclusive) and `lt` (end, exclusive) for the reporting period.

```
query GetCampaignPerformanceMetricsbyDateRangeExample($campaignId: ID!) {
  campaign(id: $campaignId) {
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

### Look-up campaign publisher spending

The following `campaign` query retrieves a list of publishers a campaign spends on most and the CPA for each publisher.

```
query GetTop10PublishersExamples($campaignId: ID!) {
  campaign(id: $campaignId) {
    reporting {
      publisherReporting(
        first: 10
        where: {
          date: { gte: "2026-03-01T00:00:00Z", lt: "2026-04-01T00:00:00Z" }
        }
        order: [{ spend: { advertiserCurrency: DESC } }]
      ) {
        nodes {
          dimensions {
            publisherProperty {
              name
            }
          }
          metrics {
            spend {
              advertiserCurrency
            }
            cpa {
              advertiserCurrency
            }
          }
        }
      }
    }
  }
}
```

### Look-up campaign flight ROAS performance

The following `campaign` query retrieves the ROAS for the current campaign flight over time.

```
query GetCurrentFlightROASOverTimeExample($campaignId: ID!) {
  campaign(id: $campaignId) {
    currentFlight {
      reporting {
        generalReporting {
          nodes {
            dimensions {
              time {
                day
              }
            }
            metrics {
              roas {
                advertiserCurrency
              }
            }
          }
        }
      }
    }
  }
}
```

## Miscellaneous campaign data queries

<!-- airspot:begin anchor="Miscellaneous Campaign Data Queries" -->
> **Airspot note (observed 2026-11-09, sandbox + production; not in TTD's prose docs, only in the schema):**
> - `campaign { reporting { reachAndFrequencyReporting { nodes { metrics { ... } } } } }` also accepts `uniquePersons`, `frequencyPerPerson` and `matchedPersonImpressions`, next to `uniqueHouseholds`, `frequencyPerHousehold` and `matchedHouseholdImpressions`. The query validates in both environments.
> - In production, `uniquePersons` ÷ `uniqueHouseholds` was about 1.03–1.04 for the campaigns that returned data. Sandbox campaigns return no reach nodes because there is no delivery.
<!-- airspot:end -->

The following sections provide GraphQL queries you can use to look up inflight campaign data and key metrics such as projected spend and relevance.

> **TIP**: If you are planning a campaign and want to test configurations based on predicted estimated spend and delivery metrics, see Forecasting.

### Look up campaign with ad groups

The following GraphQL query retrieves the ID and name for a campaign and, for each campaign returned, the name and ID of each ad group in the campaign.

```
query GetCampaignWithAdGroupsExample($campaignId: ID!) {
  campaign(id: $campaignId) {
    id
    name
    adGroups {
      edges {
        node {
          id
          name
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
}
```

### Look up campaign flights

The following GraphQL query uses a `flights` filter to retrieve campaign flight IDs and the maximum amount each flight may spend. To learn more about using filters, see GraphQL API queries in our GraphQL Resource Hub.

```
query GetFlightDataExample($campaignId: ID!, $campaignFlightId1: Long, $campaignFlightId2: Long) {
  campaign(id: $campaignId){
    id
    name
    flights(where: {id: {in: [$campaignFlightId1, $campaignFlightId2]}}){
      nodes{
        id
        budgetInAdvertiserCurrency
      }
    }
  }
}
```

### FAQs

The following is a list of frequently asked questions about GraphQL queries for campaigns.

### How often do the Projected Spend and Relevance metrics get updated?

The following table lists how frequently the Projected Spend and Relevance metrics are updated.

| Metric | Update Frequency |
| --- | --- |
| Projected Spend | - Approximately 2 hours after a campaign or ad group change - Once a day |
| Relevance | - After a campaign change - Every two days |
