# Advertiser Queries

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/AdvertiserGQLQueryExamples
- Category: GraphQL

---

# Advertiser Queries

After creating the advertiser, you can retrieve advertiser details using either the GraphQL or REST APIs. While the REST endpoints allow you to retrieve only one advertiser at a time, the GraphQl API enables you to create custom queries to search across multiple associated child records.

> **TIP**: If you're new to GraphQL, explore our [GraphQL API Resource Hub](/v3/portal/resources/doc/GqlApiHub) to learn the basics—like query anatomy, authentication, and rate limits—as well as how to run [bulk queries](/v3/portal/api/doc/GqlBulkOperations).

The following sections provide examples of the `advertiser` query that you can use to look up advertiser information.

## 

Look Up Campaign Performance Metrics by Date Range[](#reporting)

With the GraphQL API, you can create and customize `advertiser` queries and include `reporting` fields that provide key performance metrics for tracking KPIs, cost and bidding, media quality, and the overall effectiveness of all campaigns associated with the advertiser. You can either retrieve lifetime data or organize it by day or hour to help analyze trends, optimize bids, and measure engagement effectively. Whether you're evaluating media efficiency or optimizing your bidding strategy, these detailed performance metrics can help you make informed, data-driven decisions.

> **TIP**: You can also use the `reporting` field to retrieve performance metrics at the [campaign](/v3/portal/api/doc/CampaignQueryExamplesGQL#reporting) and [ad group](/v3/portal/api/doc/AdGroup#reporting) level.

Here's what you need to know about looking up advertiser performance metrics by date range:

*   These metrics also include data from all of the ad groups and campaigns associated with the advertiser.
*   You can filter the metrics only by date.
*   If you don't include a date range in the `where` filter, the query returns the lifetime metrics for all campaigns associated with the advertiser.
*   You can retrieve metrics at the following time intervals, specified in the `dimensions` field:
    *   Hourly (last 30 days)
    *   Daily (last year)
*   If you don’t include the `dimensions` field, the query returns aggregated totals for each metric without grouping data by time interval.

The following `advertiser` GraphQL query retrieves all metrics you can use to optimize campaign performance, manage spend and bidding, and so on. The date range is specified using `gte` (start, inclusive) and `lte` (end, inclusive) for the reporting period.

query GetAdvertiserPerformanceMetricsbyDateRangeExample($advertiserId: 

ID!) {

  advertiser(id: $advertiserId) {

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

Look Up Advertiser Details[](#advertiser-key-metric)

The following GraphQL query retrieves key metric details, such as channel and funnel location counts, for an advertiser by its ID.

query GetAdvertiserKeyMetricDataExample($advertiserId: ID!) {

  advertiser(id: $advertiserId) {

    id

    name

    isFavoriteForUser

    logo

    channelCount

    totalCampaignChannelCount

    funnelLocationCount

    totalFunnelLocationCount

  }

}

## 

Look Up Advertiser Seeds[](#advertiser-seeds)

The following GraphQL query retrieves [seed](/v3/portal/api/doc/Seed) details for an advertiser.

query GetAdvertiserSeedsExample($advertiserId: ID!) {

  advertiser(id: $advertiserId) {

    id

    name

    seeds {

      createdAt

      id

      isDefault

      lastUpdatedAt

      name

      targetingData {

        contextualInclusion {

          ids

          keyphrases

          urls

        }

        countryFilter {

          id

          name

        }

        firstPartyInclusion {

          name

        }

        targetingDataId

      }

    }

  }

}

## 

Look Up Advertiser Data Segments[](#advertiser-data-segment-query)

The following GraphQL query retrieves advertiser first-party data segments. It is the equivalent of the `dmp/firstparty/advertiser` REST endpoint.

> **TIP**: When querying for as much first-party data as possible, to minimize query complexity, avoid requesting the `totalCount` field.

query GetFirstPartyDataExample($advertiserId: ID!) {

  advertiser(id: $advertiserId) {

    firstPartyData(

      first: 10

      where: {

        name: { contains: "SEGMENT\_NAME\_OR\_OTHER\_SEARCH\_TERM\_PLACEHOLDER" 

        }

      }

    ) {

      pageInfo {

        hasNextPage

        endCursor

      }

      nodes {

        name

        id

        activeUniques {

          householdCount

          idsConnectedTvCount

          idsCount

          idsInAppCount

          idsWebCount

          personsCount

        }

      }

    }

  }

}

Multiple search terms can be combined in a single request. For example, to retrieve first-party data for multiple advertisers, use an array of advertiser IDs. The following is a code fragment example:

query GetFirstPartyDataForMultipleAdvertisersExample {

    advertisers(first: 50, where: { id: { in: 

    \["ADVERTISER\_ID\_PLACEHOLDER\_01", "ADVERTISER\_ID\_PLACEHOLDER\_02", 

    "ADVERTISER\_ID\_PLACEHOLDER\_03"\] } })

## 

Look Up Advertiser Settings[](#query-advertiser-settings)

The following GraphQL query retrieves advertiser settings (also known as preferences in the UI), such as attribution windows, viewability, tracking, and so on.

query GetAdvertiserPreferencesExample($advertiserId: ID!) {

  advertiser(id: $advertiserId) {

    id

    name

    description

    domainAddress

    currency {

      id

      name

    }

    partner {

      id

      name

      chinaMSASigned

    }

    clickDedupeWindowInSeconds

    conversionDeDupeWindowInSeconds

    ignoreReferralUrlInConversion

    useMediaCostBasisForCampaignFees

    logo

    attribution {

      clickLookbackWindow

      clickInterval

      impressionInterval

      impressionLookbackWindow

    }

    defaultRightMediaOffer {

      id

      name

    }

    rightMediaOfferTypes {

      id

      name

    }

    availableIndustryCategories {

      id

      name

      parentCategoryId

      isDefault

      isSensitive

    }

    availableIndustrySubCategories {

      id

      name

      parentCategoryId

      isDefault

      isSensitive

    }

    industryCategory {

      id

      name

      parentCategoryId

      isDefault

      isSensitive

    }

    industrySubCategory {

      id

      name

      parentCategoryId

      isDefault

      isSensitive

    }

    brandOwner

    assignedBrands {

      id

      name

      owner

    }

    tracking {

      defaultUrls {

        selectedTrackingType

        partnerDefault

        advertiserDefault

        creativeTypes

      }

      defaultThirdPartyTags {

        selectedTrackingType

        partnerDefault

        advertiserDefault

        creativeTypes

      }

      defaultClickUrl {

        selectedTrackingType

        partnerDefault

        advertiserDefault

        creativeTypes

      }

    }

    viewability {

      availableProviders {

        displayName

        id

        isPartnerDefault

        fees {

          displayFee

          videoFee

        }

        settings {

          profileDisplayName

          providerId

          displaySamplingRate

          videoSamplingRate

        }

      }

      selectedProviderId

      settingsOverride {

        profileDisplayName

        providerId

        displaySamplingRate

        videoSamplingRate

      }

    }

    defaultPartnerViewabilitySettings {

      profileDisplayName

      providerId

      displaySamplingRate

      videoSamplingRate

    }

    political {

      categoryIds

      isBallotMeasure

      isCandidateElection

      candidateCount

    }

    isBlockedFromHhSolution

  }

}

## 

Look Up Advertiser Metadata[](#advertiser-tiles)

The following GraphQL query retrieves the programmatic tile metadata of an advertiser.

query GetAdvertiserTilesExample($advertiserId: ID!) {

  advertiser(id: $advertiserId) {

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

## 

Look Up Tracking Tags[](#tracking-tags)

The following GQL query uses a `trackingTags` filter to find the names and IDs of tracking tags used by an advertiser. To learn more about using filters, see [GraphQL API Queries](/v3/portal/resources/doc/GqlApiQueries#filters) in our GraphQL Resource Hub.

query GetTrackingTagNamesExample {

  advertiser(id: "ADVERTISER\_ID\_PLACEHOLDER") {

    trackingTags(where: {name: {eq: 

    "TRACKING\_TAGS\_OBJECT\_NAME\_PLACEHOLDER"}}) {

      nodes {

        name

        id

      }

    }

  }

}

## 

Look Up Prism Settings[](#prism-query)

The following GraphQL query checks whether Prism is available and enabled for an advertiser.

query GetPrismStatusExample($advertiserId: ID!) {

  advertiser(id: $advertiserId) {

    dataSettings {

      prism {

        isAvailable

        isEnabled

        metadata

      }

    }

  }

}