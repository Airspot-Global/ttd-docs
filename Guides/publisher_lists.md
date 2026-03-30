# Publisher Lists

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/PublisherLists
- Category: Guides

---

# Publisher Lists

Publisher lists provide a centralized view of all its sites and apps, collectively known as properties, associated with a specific publisher. They eliminate the need to navigate through disconnected properties, saving valuable time. They're also useful for managing publishers with large portfolios, some totaling in tens of thousands of properties. When you upload a list of publishers, you have the option to target any of those properties for your campaign for even more value.

Here's what you need to know about publisher lists:

*   The Trade Desk updates publisher lists automatically. When a publisher decides they no longer want to operate one of their properties, or expand into new properties, we update the list for you so you don’t have to monitor and manage your own lists.
*   You can [create](#create-publisher-list) a publisher list as an inclusion or exclusion list for a Blue List.
*   To adjust targeting thresholds for the [Sellers and Publishers 500+ (SP500+) marketplace](/v3/portal/api/doc/SP500), you can add this marketplace and your own [publisher lists](/v3/portal/api/doc/BlueLists#add-publisher-lists) to a Blue List.
*   Adjusting thresholds may incur fees. For details, contact your Technical Account Manager.

Publisher lists are created using the same GraphQL mutation as [bid lists](/v3/portal/api/doc/BidList), although these are two distinct types of lists. Use publisher lists to manage publisher relationships, and bid lists to optimize bids across various dimensions.

## 

Create a Publisher List[](#create-publisher-list)

To create a publisher list, use the `bidListCreate` mutation. Included and excluded publisher lists are used to configure [Blue Lists](/v3/portal/api/doc/BlueLists). This list is updated by The Trade Desk so you don’t have to monitor and manage your own lists.

Generally, you create a publisher list as you would a single-dimension bid list. The difference is the following requirements:

*   The `adjustmentType` field must be set to either `INCLUSION` or `EXCLUSION`, not `OPTIMIZED`.
*   The `dimensions` field must be set to `HAS_DOMAIN_FRAGMENT_ID`.
*   The bid adjustment must be set to `1` for inclusion or `0` for exclusion.
*   The `volumeControlPriority` field must be set to `NEUTRAL`.

The following `bidListCreate` mutation shows how to create a publisher list at the partner level for inclusion in a Blue List.

mutation {

  bidListCreate(input: {

    name: "PUBLISHER\_LIST\_NAME\_PLACEHOLDER",

    adjustmentType: INCLUSION,

    dimensions: \[HAS\_DOMAIN\_FRAGMENT\_ID\],

    isAvailableForLibraryUse: false,

    owner:  {

       partnerId: "PARTNER\_ID\_PLACEHOLDER",

       adGroupId: null,

       advertiserId: null,

       campaignId: null,

       forecastId: null

    },

    bidLines: \[

      {

        bidAdjustment: 1.0,

        volumeControlPriority: NEUTRAL,

        domainFragment: "PUBLISHER\_ID\_PLACEHOLDER"

      },

      {

        bidAdjustment: 1.0,

        volumeControlPriority: NEUTRAL,

        domainFragment: "example.com"

      },

    \]

  }) {

    data {

      id

    }

  }

}

The mutation returns a publisher list ID that you can use to [link](/v3/portal/api/doc/BlueLists#add-publisher-lists) to a Blue List.