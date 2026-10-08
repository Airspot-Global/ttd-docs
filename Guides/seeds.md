# Seeds

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/Seed
- Category: Guides

---

# Seeds

Seeds are at the center of each campaign in Kokai. This representation of your most valuable customers powers real-time insights and AI optimizations—and should be considered the nucleus of your campaign decisions. To run impactful campaigns in Kokai, you need at least one high-quality seed, ideally sourced from first-party data.

> **NOTE**: Even if you don't have access to first-party data, you can still create seeds with other sources, such as retail purchase data, providing a reliable foundation for effective targeting strategies. See [Choose Seed Data Sources](#data-sources).

Before you get started, let's lay the foundation by clarifying some key Kokai terms and their definitions.

A _seed_ is a representation of your converted customers. Converted customers are people who have taken valuable actions for your brand. These actions might include making purchases, signing up for your loyalty program, installing applications, and so on, as long as these actions align with your key objectives as an advertiser. Not all actions are valuable. For example, a landing page visit or creative click is not a valuable action. By creating a seed in the platform, you unlock relevance.

_Relevance_ is the metric that effectively scores numerous dimensions for your ideal customer. Relevance scores are a comparison tool that enables you to better understand which strategies (or adjustments to strategies) are more likely than others to be successful, so you can spend your budget as efficiently as possible. Relevance scores are calculated based on your seed, and are part of campaign snapshots.

To learn more about seeds, consider watching these videos:

*   [What is a seed? And how you can use it?](https://www.youtube.com/watch?v=lHPGtVIisMM)
*   [Tags and Seeds](https://player.vimeo.com/video/901680696?badge=0&autopause=0&player_id=0&app_id=58479) (in The Trade Desk platform UI)

See also [FAQs](#faqs).

## 

Seed Quality[](#quality)

High-quality seeds are deterministic, precise, and durable. To ensure that you receive the best relevance scores, leading to better outcomes, be sure to regularly monitor the health of your seeds.

The following table provides information about seed quality scores.

> **NOTE**: High-quality seeds represent converters—seeds that contain brand purchasers.

| Quality | Type of Data | Details |
| High | First-party | Includes segments that are categorized in the Advertiser Data and Identity (**One**) tile as one of the following:

*   Purchase
*   Loyalty members
*   Voters for political advertisers

  
First-party segments are defined in two ways:

*   User-defined
*   Categorized daily by The Trade Desk through keyword matching

 |
| Third-party | Includes only segments that are categorized as purchase. Only brand purchase segments are allowed (no category purchase), and the segment cannot be modeled. The Trade Desk categorizes third-party segments based on the data partner’s methodology. |
| Medium | First-party | These segments are used in reporting and attribution. |
| Either or both of the following:

*   Third-party/retail targeting
*   Offline conversion segments

 | Includes the following segments:

*   Category purchasers
*   Modeled brand purchasers
*   Modeled category purchasers
*   Location visitors
*   Modeled pharma segments for medical health
*   Registered voters for political advertisers

 |
| Low | All else |

> **TIP**: The quality of the customers that make up the seed is more important than its initial size. A smaller seed with rich signals can be more effective because it provides a concentrated pool of users with the most desired behaviors for your brand.

The following table lists a few practical guidelines for creating, updating, and evaluating your seeds to ensure the best relevance scores.

| Guideline | Description |
| Focus on converters | Prioritize seeds that represent converted audiences rather than proxy actions. Converters typically exhibit more distinct behaviors, enhancing the seed's utility for our algorithms. |
| Emphasize precision and concentration | Aim for the most precise and concentrated dataset possible. Our models do not rely on size to assess seed quality, and we need only 5000 IDs for modeling purposes, but platform averages typically range around 100,000. |
| Ensure behavior consistency | Ensure that the seed represents one behavior consistently. Avoid mixing homepage visits with conversion pixels or combining conversions from multiple product lines, as this can dilute the quality concentration of the seed and broaden the range of behaviors targeted. |
| Prioritize recent converters | When uploading first-party data, prioritize seeds containing individuals with recent conversion attributions. For example, seeds with converters from the last 30 days are more likely to appear in the bidstream for modeling, compared to those from the past six months. |
| Monitor seed health | Recognize that seeds can evolve over time. Regularly monitor the health of your seeds. |
| Track the number of active IDs | If a seed has fewer than 5000 active IDs, it does not impact bidding. When this happens, one way to improve the counts is to add contextual data. When the seed reaches 5000 active IDs, it prioritizes the segment again. |

## 

Choose Seed Data Sources[](#data-sources)

To create a high-quality seed, start with well-sourced data as your foundation. First-party data stands out as the prime choice, offering direct insights into your audience. Additionally, retail data serves as a valuable seed source, providing unique perspectives on consumer behavior. Third-party data and custom segments are also viable options, especially if they align with your target audience's conversion patterns. In the event that purchase data is unavailable, proxy seeds offer an alternative choice. For example, you might choose to include homepage visits, which serve as early signals of potential conversions, ensuring your seed remains robust even in circumstances that are less than ideal. You can use any combination of data sources for your seed.

> **IMPORTANT**: If you use third-party data, you must check that the segment supports seeds and that you have permission to use the data. To check whether your data is eligible for seed creation, see [FAQs](#faqs).

The following table summarizes various data sources that you can use to create a seed, listing them in descending order of quality. See also [FAQs](#faqs).

| Data Source | Seed Quality | Description |
| Real-time first-party conversion data | Converted audience | Online conversion events, such as purchases or sign-ups that we record. Best collected using pixels. |
| Imported conversions | Converted audience | CRM data or offline first-party segments. |
| Retail purchase data, precise and specific to the advertiser | Converted audience | Segments that The Trade Desk categorizes as including users who have made purchases from a specific brand. This might be a good choice, for example, if your product is for Consumer Packaged Goods (CPG), because you might not have the previous options. |
| Brand-specific third-party purchase data | Converted audience | Advertisers, such as pharmaceuticals, QSR, political advertisers. who might not have access to good first-party conversion or retail data. |
| Other real-time first-party data | Proxy audience | [Tracking tags](/v3/portal/data/doc/TrackingTagsOverview) or app data, representing homepage landings or proxy actions (clicks) that express interest. |
| Brand-specific category or interest data | Proxy audience | Less valuable than purchase data, but can be a starting point for a temporary seed. |
| Custom keywords or sites | Proxy audience | A temporary solution for advertisers to create their first seed, until they can leverage a higher-quality data source. |

## 

Seeds with Multiple Segments: Applying Boolean Logic[](#data-type)

You can create seeds using multiple segments. In this case, Boolean logic is applied to determine relevant users based on whether the segments are first-party or third-party data. Here's a high-level overview of the logic:

*   **First-party data segments**: These are treated as "OR" conditions. This means that a user needs to meet only one of the criteria. In other words, a user in _any_ of the included segments is relevant, such as users who have interacted with your company's app or made a purchase at its store.
    
*   **Third-party data segments**: These are treated as "AND" conditions. This means that a user must meet all the criteria. In other words, to be considered relevant, users must belong to _all_ listed third-party segments, such as users that are interested in sports _and_ are located in a specific country.
    

The following table describes the Boolean logic for various data segments, listed in order of relevance from highest to lowest, as recommended for creating your seed.

| Data Segment Type | Boolean Logic | Description |
| First-party data segments | OR | Users in any first-party data segment. |
| Retail converter data segments | OR | Users in any retail converter data segment (where they have made a purchase of a specific brand). Category purchasers are not included: for example, Coca-Cola purchasers are included, but soda purchasers are not.  
**TIP**: Use brand-purchase data whenever possible, because it directly represents your customers. |
| Retail non-converter segments | AND | Only users found in _all_ retail non-converter segments. |
| Offline measurement data segments | OR | Users in any offline measurement data segment. |
| Third-party data segments | AND | Only users found in _all_ third-party data segments. |
| Keywords or URLs for custom data segments | OR | Users if they match any keyword or URL in any segment. |
| Across all data segments | OR | Users in any segment. |

## 

Get Started[](#get-started)

Your partnership with us begins when you create your seed in the platform. You identify your ideal customer from the data uploaded to the platform, and we work together to find that type of person wherever they are on the internet.

If you've familiarized yourself with our guidelines for [seed quality](#quality) and [data sources](#data-sources), you're ready to harness the power of audience-based buying and to unlock relevance through your seeds. Here's a high-level overview of the steps for you to follow:

1.  Identify your seed data sources and make a list of segment IDs that you want to use for your seed. See also [FAQs](#faqs).
2.  [Create](#create) a seed.
3.  [Attach](#attach-to-campaign) the seed to your campaigns.

The following sections define the `seed` object and provide examples of key tasks and use cases associated with seeds.

### 

Seed Object[](#object)

The following table lists the high-level fields that are part of a seed in the GraphQL API. When creating or updating seeds, you can specify some of them as input and others as response data to be returned.

| Field | Data Type | Required? | Description |
| `id` | String | Required | The unique identifier for the seed, assigned at its creation. To update the seed, or to attach it to a campaign, you must provide the seed ID. |
| `advertiser` | Object | Required | The details of the advertiser that owns the seed. |
| `targetingData` | Object | Required | Depending on the [data sources](#data-sources) used for the seed, this might be a list of first-party, retail, or third-party data segment IDs, contextual key words and phrases, or URLs.  
**IMPORTANT**: If you use third-party data, you must check that the segment supports seeds and that you have permission to use the data. To check whether your data is eligible for seed creation, see [FAQs](#faqs). |
| `activeIds` | Integer | Optional | The number of IDs seen in bidding within the past seven days. For details, see [Unique ID Counting Methodologies](/v3/portal/api/doc/IdCountingMethodologies). |
| `createdAt` | DateTime | Optional | The date and time when the seed was created. |
| `lastUpdatedAt` | DateTime | Optional | The date and time when the seed was last updated. |
| `name` | String | Optional | The seed name. |
| `status` | String | Optional | The current status of the seed. For possible values, see [Seed Status Values](#seed-statuses). |
| `uniqueHouseholds` | Integer | Optional | The number of unique households that are in in the seed, based on matching it on the household graph. |
| `campaigns` | Object | Optional | The details of the campaigns to which the seed is attached. |

#### Seed Status Values

The following table lists the possible seed status values.

| Status | Description |
| `Pending` | We're currently gathering IDs for the seed. This might take up to 24 hours. |
| `Ready` | The seed contains sufficient high-quality signals, and is ready for use. |
| `Error` | The seed requires a minimum of 5,000 active IDs to be considered ready for use. Add more data segments. |

The following sections provide examples of critical seed mutations and queries.

### 

Create a Seed[](#create)

> **IMPORTANT**: Before you begin, be sure to review our guidelines for [seed quality](#quality) and [data sources](#data-sources).

To create a seed, you must have the following:

Your advertiser ID  
A name for your seed that describes it  
Your selected targeting (source) data IDs  
Approval to use your selected targeting (source) data IDs, if you are using third-party data  

> **TIP**: To look up targeting data IDs, use the [POST /v3/dmp/firstparty/advertiser](/v3/portal/api/ref/post-dmp-firstparty-advertiser) endpoint for first-party data or the [POST /v3/dmp/thirdparty/advertiser](/v3/portal/api/ref/post-dmp-thirdparty-advertiser) endpoint for third-party data. For details, see the [first-party data elements](/v3/portal/api/doc/Audience#data-elements-1p-lookup-tasks) and [third-party data elements](/v3/portal/api/doc/Audience#lookup-3p-data-elements-lookup-tasks) look-up task examples under [Audience](/v3/portal/api/doc/Audience).

Here's what you need to know about creating a seed:

*   You can create more than one seed per advertiser, but you can attach only one seed per campaign.
*   The first seed that you create is automatically set as your default seed, which is automatically attached to your campaigns in Kokai unless you specify a different seed. If you have more than one seed, you can change your default seed.

When you're ready, run a `seedCreate` mutation with your input information and specify the fields you want to be returned in the response, such as `id`. The following example includes different types of targeting data to illustrate how you can specify it as your input.

> **NOTE**: In the `targetingData` object, the `countryFilterIds` filter is intended for use with contextual data only. It is not a seed-specific targeting setting, and does not apply country-level targeting to the seed. If you are not using contextual targeting in your seed, omit this filter.

mutation {

    seedCreate(

        input: {

            advertiserId: "abc123x"

            name: "1pd-retail-3pd-custom-segment-seed"

            targetingData: {

                firstPartyDataInclusionIds: \[572489361, 817405926\]

                retailDataInclusion: \[

                    {thirdPartyDataId: 693210847, thirdPartyDataBrandId: 

                    "brandabc"},

                    {thirdPartyDataId: 856319742, thirdPartyDataBrandId: 

                    "xyzbrandid"}

                \]

                thirdPartyDataInclusion: \[

                    {thirdPartyDataId: 761834295, thirdPartyDataBrandId: 

                    "123brand"},

                    {thirdPartyDataId: 625039174, thirdPartyDataBrandId: 

                    "3pdbrandid"}

                \]

                contextualInclusion: { 

                    keyphrases: \["open internet", "kokai"\], 

                    urls: \["http://thetradedesk.com"\] 

                }

                countryFilterIds: \["US"\]

            }

        }

    ) {

        data {

            id

        }

    }

}

A successful response returns the values that you specify: for example, the platform ID for the newly created seed.

> **IMPORTANT**: To update the seed, or to attach it to a campaign, you must provide the seed ID.

If this is your first seed, it's automatically used as the default seed for all your campaigns. If you have more than one seed, you can attach your new seed to a campaign.

### 

Attach a Seed to a Campaign[](#attach-to-campaign)

To take advantage of audience-based buying, each campaign in Kokai requires a seed.

> **NOTE**: This section focuses on GraphQL instructions, but you can also use the REST API. For example, you can attach a seed when creating or cloning campaigns by including the optional `SeedId` property in your REST API call. For details, see [Campaigns](/v3/portal/api/doc/Campaigns).

Here's what you need to know about seeds in campaigns:

*   You can attach only your own seeds to your campaigns. In other words, the seed and the campaign must both belong to the same advertiser.
*   You can have multiple seeds, but you can attach only one seed per campaign.
*   You can reuse the same seed in multiple campaigns.
*   You can update a campaign to attach a different seed to it.
*   To attach a seed to a campaign, you must have the campaign ID and the seed ID.
*   The same GraphQL `campaignUpdateSeed` mutation enables you to attach a new seed to a campaign or replace the existing seed.
*   You can update seeds and other data for multiple campaigns in a single GraphQL call. For details, see [GraphQL API Bulk Operations](/v3/portal/api/doc/GqlBulkOperations).

> [!CAUTION]
> **Deprecated REST Endpoint (HTTP 405 Method Not Allowed)**:
> In Kokai environments, attempting to associate a seed with a campaign using legacy REST `PUT /v3/campaign/bulksettings` fails with `HTTP 405 Method Not Allowed` (`Allow: GET`).
> Seed assignment in Kokai is handled exclusively via the GraphQL `campaignUpdateSeed` mutation.

> **TIP**: To look up seed details, including the campaigns it's associated with, run a `seed` query. For an example, see [Look Up Seed Details by Seed ID](#get-seed).

Here's an example of a `campaignUpdateSeed` mutation that attaches a seed to a campaign:

```graphql
mutation CampaignUpdateSeed($campaignId: ID!, $seedId: ID!) {
  campaignUpdateSeed(
    input: {
      campaignId: $campaignId
      seedId: $seedId
    }
  ) {
    data {
      id
    }
    userErrors {
      message
      field
    }
  }
}
```

## 

Manage Seeds[](#manage)

The following table lists some of the common tasks associated with seeds that you might need to perform.

| Task | GraphQL Operation | Notes |
| [Look up details of a seed](#get-seed) by its ID. | Query | You can look up seed details as well as campaign details in a single call. |
| [Look up all seeds](#get-seed) for an advertiser ID. | Query | You can look up seed details as well as advertiser details in a single call. |
| [Update](#update) a seed. | Mutation | Updating seeds can help ensure their quality. |
| [Replace](#attach-to-campaign) a seed in a campaign. | Mutation | Use the same mutation to attach a new seed or to replace an existing one in a campaign. |
| [Change default](#change-default) seed for an advertiser. | Mutation | If you have multiple seeds, you can designate a different seed as the default. Only applicable if you have multiple seeds. |

> **TIP**: For basic guidelines on GraphQL operations, and additional examples, see [GraphQL queries](/v3/portal/resources/doc/GqlApiQueries).

The following sections provide details and examples for retrieving and updating seed information.

### 

Look Up Seed Details by Seed ID[](#get-seed)

The following example of the `seed` query illustrates how to retrieve active IDs, seed name, status, targeting data IDs, and other details, as well as the IDs of the campaigns that use the seed.

query GetSeedDetailsExample($seedId: ID!) {

  seed(id: $seedId) {

    activeIds

    campaigns {

      nodes {

        id

      }

    }

    targetingData {

      targetingDataId

      firstPartyInclusion {

        advertiserTargetingDataId

        name

      }

      thirdPartyDataInclusion {

        fullPath

        name

        thirdPartyDataBrandId

        thirdPartyDataId

      }

    }

    createdAt

    id

    isDefault

    lastUpdatedAt

    name

    status

    uniqueHouseholds

  }

}

> **TIP**: In the preceding example, we recommend that you [use pagination for `node` fields](#use-pagination-for-node-fields).

### 

Use Pagination for Node Fields[](#use-pagination-for-node-fields)

we recommend using pagination for `node` fields, such as `campaigns` in the `seed` query example in [Look Up Seed Details by Seed ID](#get-seed).

For example:

seed(id: $seedId) {

  campaigns(first: 10, after: $cursor, where: $conditions) {

    id

  }

}

### 

Look Up All Seeds for an Advertiser[](#get-seeds)

The following example of an `advertiser` query retrieves all seeds associated with a specific advertiser.

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

          advertiserTargetingDataId

          name

        }

        thirdPartyDataId

      }

    }

  }

}

### 

Update a Seed[](#update)

To ensure the [quality](#quality) of your seeds, you might have to update seeds. This depends on the [data sources](#data-sources) you use for your seeds. For example:

*   If you use deterministic conversion data from first-party data sources and update your segments on a regular basis, you don't need to make any updates to your seed.
*   If you use self-updating data sources such as pixels, there's no need to manually update your seed.
*   If you use imported third-party data segments, you should update your seed every time you upload new data segments.

Whether you want to update the seed source data, its name, or any other seed details, you must have your seed ID and the targeting (source) or other data you want to update.

Here's an example of a `seedUpdate` mutation:

mutation {

    seedUpdate(

        input: {

            id: "klmp432o"

            advertiserId: "abc123x"

            name: "1pd-retail-seed"

            targetingData: {

                firstPartyDataInclusionIds: \[572489361, 817405926\]

                retailDataInclusion: \[

                    {targetingDataId: 693210847, thirdPartyDataBrandId: 

                    "abcbrand"},

                    {targetingDataId: 856319742, thirdPartyDataBrandId: 

                    "3pdbrandid"}

                \]

            }

        }

    ) {

        data {

            id

        }

    }

}

### 

Change Default Seed for an Advertiser[](#change-default)

The first seed that you create is automatically set as your default seed, which is automatically attached to your campaigns in Kokai unless you specify a different seed. If you have more than one seed, you can change your default seed.

Here's an example of an `advertiserSetDefaultSeed` mutation:

mutation  { 

  advertiserSetDefaultSeed( { seedId: "123xyz2", advertiserId: "abc123x" } ) 

  {

    data {

      id

    }

  }

}

## 

FAQs[](#faqs)

The following is a list of commonly asked questions about seeds.

### 

Am I required to create a seed?

Yes. Without a seed, the platform cannot calculate relevance and QRI, both of which are powerful metrics that measure the overlap between your seed and your targeting. QRI, which is found in reporting, shows the relevance of a grain to the desired seed. Use this as a comparison to understand how similar the buy was to your highest quality data. Relevance is the metric that effectively scores numerous dimensions for your ideal customer, and is present throughout the UI.

### 

Where can I find targeting data IDs for my seed?

To look up targeting data IDs, use the following endpoints:

| Data | Endpoint | Look-up Task Examples |
| First-party | [POST /v3/dmp/firstparty/advertiser](/v3/portal/api/ref/post-dmp-firstparty-advertiser) | [First-Party Data Elements](/v3/portal/api/doc/Audience#data-elements-1p-lookup-tasks) |
| Third-party | [POST /v3/dmp/thirdparty/advertiser](/v3/portal/api/ref/post-dmp-thirdparty-advertiser) | [Third-Party Data Elements](/v3/portal/api/doc/Audience#lookup-3p-data-elements-lookup-tasks) |

### 

How do I determine whether third-party and retail segments are eligible for seed creation?

Use the [POST /v3/dmp/thirdparty/advertiser](/v3/portal/api/ref/post-dmp-thirdparty-advertiser) endpoint to check whether the `IsEligibleForSeeds` property is `true`.

### 

What if I don't have enough data or any data to create a seed?

Don't worry! Think of your seed as a dynamic entity in which data changes over time. Even if you don't have enough data to start, you can still create a seed and keep updating it as more data sources become available. You don't need a lot of data for seeds to work because seeds allow you to put even a few thousand user sign-ups to work. You can use third-party data, retail data, or custom keywords.

### 

Can I create multiple seeds?

Yes! In fact, we recommend that you create multiple seeds. For example, a shoe manufacturer might have two campaigns with different seeds as follows:

*   A campaign to sell running shoes, in which the seed includes customers who have previously purchased running shoes of the same brand.
*   A different campaign to sell basketball shoes, in which the seed includes customers who have previously purchased basketball shoes of the same brand.

### 

Should my seed represent existing customers or desired customers?

Seeds should represent people who have interacted with your brand in a valuable way: for example, conversions.

### 

How is seed different from audience?

Seed and [audience](/v3/portal/api/doc/Audience) are not the same:

*   A **seed** is a specific, concentrated group of individuals representing the core group of people that you want to target. This group typically consists of individuals who have taken valuable actions, or who exhibit traits that align with your campaign goals.
*   An **audience** is an expanded version of the core group. An audience includes the individuals in your seed, but also includes others who share similar traits or behaviors.

### 

Will I have to manually set my default seed?

The first seed that you create is your default seed. If you have more than one seed, you can [change](#change-default) the default at any time.

### 

Do I need seeds if I primarily run reach campaigns?

Yes. Seeds can help you find the best quality reach, even if you're targeting large demographic, behavioral, or interest categories. The seed is used to prioritize impressions that share similar behaviors within these large audiences, and to help drive them down the funnel. Therefore, if you have any first-party conversion data, you should use it as a seed. See also [Choose Seed Data Sources](#data-sources).

### 

Do I need seeds if I run exclusively CTV campaigns?

Yes. Seeds can help you better understand the quality of your reach, even on devices without deterministic attribution. We apply the graph to be able to find people across households and devices.

### 

What seed data should I use if I run full-funnel omnichannel campaigns for different KPIs?

If you have a single way to track the success of your advertising, such as a conversion pixel, this is probably the best seed for you. Regardless of the programmatic KPI, the platform always points towards finding the common behaviors of people that have bought the product through relevance. Relevance can help performance, but it does not always directly drive more KPI performance. Therefore, you can use a single conversion pixel across KPIs to help prioritize audience across all funnels, and to push them down the funnel based on the behaviors and attributions of lower-funnel converters.

### 

How many seeds should I have if I have different product lines?

Generally, create at least one seed per product line. If you mix completely different groups of people that have interacted with your brand, this dilutes the quality concentration of the seed and broadens the range of behaviors targeted.

### 

If I do measurement offline, can I use this data as a seed?

Yes! If you track any offline brand interactions—for example, through CRM lists or other first-party data collection methods—you can push them to the platform as onboarded first-party data.

> **TIP**: To ensure this is good for our models, the best segments are those that consist of people who have interacted with the brand more recently and frequently. For example, a 14-day or 30-day lookback is better than people from a year ago. See also [Seed Quality](#quality).

### 

What should I do if I don't have any conversion data or want to reach a totally new demographic?

You can start by testing out how audiences react and refine a data set that represents true people that engage with your brand. To do so, you should start with a proxy action, such as a homepage visit. For example, create an empty pixel and add in a third-party data segment or other data type that represents your new customer. As the pixel gets attributed conversions, the seed automatically prioritizes the new first-party data as it comes in.

### 

Why am I getting an error that an advertiser cannot access seeds?

Some advertisers have data policy restrictions in place that prevent them from creating, editing, or archiving seeds, or from assigning seeds to campaigns. For example, health advertisers in the European Union are blocked from using seeds in the API.

Blocked advertisers can still use campaign endpoints as usual by entering `null` as the seed ID.

### 

Can I use tracking tags (pixels) in seeds?

Yes. Just add the first-party data ID of the tracking tag ID in the `targetingData.firstPartyDataInclusionIds` list.

> **IMPORTANT**: Do not pass the tracking tag ID itself (a 7-character alphanumeric string): the tracking tag ID is not the same as the associated first-party data ID, and you'll get an error.

### 

Why doesn’t the countryFilterIds filter apply country targeting to my seed?

The `countryFilterIds` field in the `targetingData` object is relevant only when using contextual data with your seed. It comes from the contextual data service and does not directly control seed-level targeting.

### 

Can I delete a seed?

Yes. To delete a seed, contact your Technical Account Manager.