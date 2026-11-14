# Multi-dimensional bidding

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/DimensionalBidding
- Retrieved: 2026-11-14
- Category: Guides

---

# Multi-dimensional bidding

Multi-dimensional bidding applies a bid factor simultaneously across several dimensions (also known as vectors), unlike single-dimensional bidding. It uses combinations of dimensions, such as site and ad placement, to offer greater bid variety and more accurate targeting. For example, you can adjust bids higher or lower based on which supply-side platform (SSP) is requesting inventory, or block bids on display ads for websites if the ads are placed below the fold. For details on bid list ownership, terms, and requirements, see Bid lists.

## What you need to know

Here's what you need to know about multi-dimensional bidding:

- By default, you can use multi-dimensional bidding for two dimensions. More than that will cause API errors. If you require combinations that include more than two dimensions, contact your Technical Account Manager.
- Multi-dimensional bidding is available only in the API and not visible on the UI platform.

This guide focuses on multi-dimensional bid lines and provides examples in both GraphQL and REST.

## Anatomy of a multi-dimensional bid list

A multi-dimensional bid list is a collection of bid lines with the _same_ combination of _multiple_ dimensions. The following diagram compares a multi-dimensional bid list with a single-dimensional one. The main difference between them is that the multi-dimensional bid lines have the same combination of two dimensions (supply vendor, in red, and domain fragment), while the single-dimensional bid lines have one (domain fragment).

> **NOTE**: The rest of the requirements are the same for both single- and multi-dimensional bid lists. For details, see What you need to know.

## Bid optimization workflow

After you've created a campaign with a seed representing your top customers, you can optimize the campaign with multi-dimensional bidding. When The Trade Desk receives bid requests from publishers and SSPs, it translates them into combinations of dimensions to match your multi-dimensional bid list, such as:

- `SSP_One`, `example.com`
- `SSP_Two`, `example.com`

The optimization steps are:

1. We match these dimension combinations to bid lists and eligible ad groups.
2. For each matching line in the bid list, we multiply the base bid with the bid factor and determine the final adjustment using the bid list resolution type.
3. We calculate the final bid by multiplying the base bid for the ad group by its associated bid lists, bid factors, KPIs, relevance factors, pacing, and other signals.

## Create a multi-dimensional bid list

> **IMPORTANT**: By default, you can use multi-dimensional bidding for up to two dimensions. More than that will cause API errors. If you require combinations that include more than two dimensions, contact your Technical Account Manager.

To create multi-dimensional bid lists, use either the GraphQL API or REST API. Unlike single-dimensional bid lists, add extra dimensions in the `dimensions` (GraphQL) or `BidLines` (REST) array.

For instructions on managing and retrieving bid list information, see Create and manage bid lists in GraphQL or Create and manage bid lists in REST.

### GraphQL API

To create multi-dimensional bid lists in GraphQL, use the `bidListCreate` mutation as you would with single-dimensional bid lists but include the additional dimensions in the `dimensions` array.

The following GraphQL mutation example creates a multi-dimensional bid list for an ad group that excludes display ads below the fold from the domains `example1.com` and `example2.com`. The `adjustmentType` field is set to `EXCLUSION`, indicating the default bid factor is `0`.

The mutation returns the ID of the created bid list.

```
mutation {
bidListCreate(
    input: {
      name: "BID_LIST_NAME_PLACEHOLDER"
      dimensions: [
        HAS_PLACEMENT_POSITION_RELATIVE_TO_FOLD_ID
        HAS_DOMAIN_FRAGMENT_ID
      ]
      adjustmentType: EXCLUSION
      bidLines: [
        {
          bidAdjustment: 0
          volumeControlPriority: NEUTRAL
          placementPositionRelativeToFold: BELOW
          domainFragment: "example1.com"
        }
        {
          bidAdjustment: 0
          volumeControlPriority: NEUTRAL
          placementPositionRelativeToFold: BELOW
          domainFragment: "example2.com"
        }
      ]
      owner: { adGroupId: "AD_GROUP_ID_PLACEHOLDER" }
    }
  ) {
    data {
      id
    }
    userErrors {
      field
      message
    }
  }
}
```

### REST API

To create multi-dimensional bid lists in REST, use the POST /v3/bidlist endpoint as you would with single-dimensional bid lists but include the additional dimensions in the `BidLines` array.

The following is a block list example of a request that excludes CTV ads from the domains `example1.com` and `example2.com`. The `BidListAdjustmentType` property is set to `BlockList`, indicating the default bid factor is `0`.

The response returns the ID of the created bid list.

```
{
    "Name": "Site/App Block List",
    "BidListAdjustmentType": "BlockList",
    "BidLines": [
        {
        "DeviceType": "ConnectedTV",
        "DomainFragment": "example1.com"
        },
        {
        "DeviceType": "ConnectedTV",
        "DomainFragment": "example2.com"
        }
    ],
    "BidListOwner": "AdGroup",
    "BidListOwnerId": "3f8ges2a"
}
```

## FAQs

The following is a list of commonly asked questions about multi-dimensional bid lists.

### Can I combine single-dimensional and multi-dimensional bid lists in an ad group?

Yes. You can include both single-dimensional and multi-dimensional bid lists in an ad group. However, remember that your bid lists are multiplied _together_.

For example, consider three bid lists with the following bid factors:

| Dimensions | Bid Factors |
| --- | --- |
| `example.com` | `1.25` |
| `example.com` | `1.15` |
| `SSP_One` _and_ `example.com` | `1.5` |

If SSP One requests inventory on `example.com`, this would match both your bid factors for the SSP and the domain fragment _and_ your bid factor for the _combination_ of those dimensions. The result would be the product of _all_ bid factors (`1.25` * `1.15` * `1.5` = `2.16`).
