# Sellers and Publishers 500+ Marketplace

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/SP500
- Category: Guides

---

# Sellers and Publishers 500+ Marketplace

To help you focus on value and make audience-based buying work better for advertisers, The Trade Desk offers the Sellers and Publishers 500+ (SP500+) marketplace. This marketplace is a vetted, transparent pool of thousands of trusted sellers and publishers that provides advertisers with the option to buy premium [inventory](/v3/portal/resources/doc/Glossary#inventory) at scale across the open internet.

> **NOTE**: SP500+ settings can be set differently for each campaign or ad group under an advertiser.

The SP500+ spotlights the top 500 publishers, but it includes more than 20,000 websites and apps. It is also a dynamic marketplace, with publishers flowing in and out based on the quality of their ad experience and supply path transparency. By actively curating the SP500+, The Trade Desk eliminates the complexity and fragmentation of private marketplace buying while offering the scale of the open market. We're constantly reviewing the SP500+ publishers, their processes, and improving technologies.

The SP500+ includes publishers we've checked for high-quality ad load, ad refresh, content duration, content signal transparency, placement-level viewability, and more. We regularly update the SP500+ marketplace by revising these metrics and inclusion thresholds.

> **TIP**: You can customize your inventory marketplace options by using [Blue Lists](/v3/portal/api/doc/BlueLists) with [publisher lists](/v3/portal/api/doc/PublisherLists), typically with the SP500+ marketplace as the foundation.

## 

Opt-In Options[](#opt-in-options)

Accessing the SP500+ is straightforward. In many cases, we've already activated it for you. This table lists the options for opting in ad groups, if needed.

> **TIP**: To look up and verify SP500+ access for ad groups, see [Ad Group Marketplace Settings](#lookup).

| Status | Automatic Opt-In? | Can Inherit Access by Default |
| Advertiser | Yes. Most advertisers in Kokai automatically gain access to the SP500+. | N/A |
| New ad group | Yes. If the advertiser has its SP500+ marketplace setting enabled by default and the campaign has its `Version` property set to `Kokai`, the ad group also has access to SP500+. | Campaigns with SP500+ access will have their ad groups automatically inherit this access when created through the UI or API. |
| Existing ad group | No. To opt an ad group into SP500+ access, [set](#enable-existing) the `marketType` property to `MARKETPLACE`. | To be more efficient, use GraphQL to [set up](#set-default) your campaign to make new ad groups inherit the campaign marketplace access by default. |

## 

Add SP500+ Access to Ad Groups[](#enable-existing)

To configure SP500+ access for ad groups, set the `marketType` property to `MARKETPLACE`.

The following is a GraphQL mutation example for configuring SP500+ for an ad group by its ID.

mutation {

  adGroupUpdate(input: { adGroupId: "abc123", marketType: MARKETPLACE 

  }) {

    data {

      marketType

    }

    userErrors {

      field

      message

    }

  }

}

## 

Look Up SP500+ Settings with GraphQL[](#lookup)

The following sections are examples of GraphQL queries for looking up SP500+ settings for advertisers, campaigns, and ad groups.

### 

Advertiser Default Marketplace Setting[](#lookup-inherit-advertiser)

The following GraphQL query retrieves the `isMarketplaceEnabledByDefault` value of an advertiser.

query GetAdvertiserMarketplaceIsEnabledExample {

  advertiser(id: "abcd123") {

    isMarketplaceEnabledByDefault

  }

}

An advertiser that can propagate its marketplace settings to ad groups has its `isMarketplaceEnabledByDefault` property set to `true`.

### 

Ad Group Marketplace Settings[](#lookup)

To confirm if an ad group has SP500+ access, use the GraphQL API to query and verify the ad group marketplace settings.

The following GraphQL query retrieves the marketplace type and owner for an ad group.

query GetAdGroupMarketplaceSettingsExample {

  adGroup(id: "abc123") {

    marketType

    marketplace {

      name

      owner

    }

  }

}

An ad group with SP500+ access returns `MARKETPLACE` in the `marketType` property and `GLOBAL` in the `owner` property.

## 

FAQs[](#faqs)

### 

Where can I find the names of the top publishers in SP500+?

Take a quick look at which publishers are in the top 500 by browsing the SP500+ marketplace in the Inventory Controls (**Inv**) tile of the Kokai UI platform when viewing an ad group.

### 

How do I opt out advertisers created in Kokai from SP500+?

There is currently no way to opt out new advertisers through the API. Contact your Technical Account Manager for help.

### 

How do I opt out ad groups from SP500+?

When creating an ad group, set the `MarketplaceOptOut` parameter to `true` using REST API.

Here's a snippet of the `MarketplaceOptOut` parameter for opting out of SP500+ access in the [POST /v3/adgroup](/v3/portal/api/ref/post-adgroup) request body.

{

  "CampaignId": "{campaignId}",

  "AdGroupName": "Test Ad Group",

  "IndustryCategoryId": 292,

  "AdGroupCategory": {

    "CategoryId": 8311

  },

  "MarketplaceOptOut": true

}

### 

When cloning campaigns, how do I opt out ad groups from SP500+?

You have the option to opt ad groups out using either GraphQL or REST API.

| API | Endpoint / Mutation | Value |
| GraphQL | `campaignClonesCreate` mutation | Set the `useInventoryMarketPlace` property to `false`. |
| REST | [POST /v3/campaign](/v3/portal/api/area/Campaign) | Set the `MarketplaceOptOut` value to `true`. |

For details on using the GraphQL API to clone campaigns, see [Clone Campaigns with the GraphQL API](/v3/portal/api/doc/CampaignCloning#gql).