# Create and manage bid lists in REST

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/BidListsCreateManageREST
- Retrieved: 2026-11-14
- Category: Guides

---

# Create and manage bid lists in REST

This guide walks you through setting up bid lists in REST, defining their key properties, and propagating them to associated campaigns and ad groups. Use REST if you need to access legacy features of the platform.

A unique aspect of bid lists is their flexibility in terms of ownership and assignment. They can be owned and assigned at various levels within the core entities: ad group, campaign, advertiser, and partner. For details, see Entity relationships.

To learn more about bid list terms and relationships, see Bid lists. For instructions on using our GraphQL API, see Create and manage bid lists in GraphQL.

## Requirements and guidelines

Here's what you need to know before making REST calls for bid lists:

- A bid list must contain at least one bid line, and all bid lines in a list must use the same dimension. For example, you can't mix a `DomainFragment` bid line with a `GeoSegmentId` bid line in the same list because doing so returns a validation error.

> **NOTE**: Some dimensions use third-party providers and might incur additional fees.

- The number of bid lines can't exceed the bid line relationship limits. To avoid recreating bid lists at multiple levels, use inheritance instead.
- Bid lists are limited to 500,000 bid lines each, regardless of owner type (ad group, campaign, advertiser, or partner), in addition to the bid line relationship limits.
- The adjustment type and bid adjustment values must match (see Adjustment types). The default resolution type, `ApplyMultiplyAdjustment`, multiplies bid adjustments from a bid list to calculate the final bid adjustment. This is required for target and block lists, and recommended for optimized lists.

Here's what you need to know about managing bid lists:

- To streamline management across multiple campaigns and ad groups, use default bid lists.
- To update or delete a bid list, or associate a bid list with an entity, use the GraphQL API instead of REST.

> **TIP**: To create, look up, or update multiple bid lists at once, use bulk operations.

The following sections provide examples of REST API calls for creating and managing bid lists.

## Adjustment types

When creating a bid list, choose an adjustment type to determine bid adjustments based on bid line matches. Target and block lists allow or deny bidding based on specified dimensions. Optimized lists offer flexible bid adjustments per bid line.

The following table outlines bid adjustment types in REST and their impact on matching and non-matching bid lines.

| Adjustment type | Description | Bid adjustment for matched bid lines | Bid adjustment for non-matching bid lines |
| --- | --- | --- | --- |
| `TargetList` | Includes impressions that match the specified dimensions for targeting. Impressions that do not match any line in a target list are excluded from bidding. | `1` | `0` |
| `BlockList` | Excludes impressions that match the specified dimensions from targeting. Only impressions that do not match any line in a block list are included in bidding. | `0` | `1` |
| `Optimized` | Offers more flexibility compared to block or target lists. Here are key points: - Unlike block or target lists, where bid adjustments are limited to `0` and `1`, optimized bid adjustments can include decimals like `0.25` or `1.75`. - Impressions matching a bid line get the specified adjustment. - If an impression matches multiple bid lines, the resolution type sets the final bid adjustment. **TIP**: Set the `ResolutionType` property to `ApplyMultiplyAdjustment` to multiply the bid adjustments of all matching bid lines. Impressions not matching any bid line continue to bid. | Value specified | `1` |

## Create bid lists

You can create a bid list as you're creating or updating an ad group using the `NewBidLists` object. The following request examples detail the requirements for creating different types of bid lists, such as target, block, and optimized.

### Target and block bid lists example

The following table describes the required properties for creating target and block bid lists.

| Property | Description |
| --- | --- |
| `Name` | A name to describe this bid list. |
| `BidListAdjustmentType` | Must be set to `TargetList` or `BlockList`. |
| `BidLines.<Dimension>` | Choose one of the dimensions from the `BidLines` object. Commonly used dimensions include `AdFormatId`, `DomainFragment`, `GeoSegmentId`, and `RecencyWindowInMinutes`. **NOTE**: Some dimensions use third-party providers and may incur additional fees. |

For target or block lists, the bid adjustment should not be passed, or if it is passed, it should be `1` for target lists and `0` for block lists. The following is a target list example of a POST /v3/adgroup request.

```
{
  "Name": "Site/App Target List",
  "BidListAdjustmentType": "TargetList",
  "BidLines": [
    {
      "DomainFragment": "example.com"
    },
    {
      "DomainFragment": "example.org"
    }
  ]
}
```

### Optimized bid list example

This table describes the required properties for creating optimized bid lists. These properties define the bid list's name, ownership, and the specific dimensions and adjustments to apply when an impression matches the criteria.

| Property | Description |
| --- | --- |
| `Name` | A name to describe this bid list. |
| `BidListAdjustmentType` | Must be set to `Optimized`. |
| `ResolutionType` | Must be set to `ApplyMultiplyAdjustment`. |
| `BidLines.BidAdjustment` | The adjustment applied to the base bid when an impression matches all of the dimensions in this bid line. |
| `BidLines.<Dimension>` | Choose one of the dimensions from the `BidLines` object. Commonly used dimensions include `AdFormatId`, `DomainFragment`, `GeoSegmentId`, and `RecencyWindowInMinutes`. **NOTE**: Some dimensions use third-party providers and may incur additional fees. |

The following is an optimized example of a POST /v3/adgroup request.

```
{
    "Name": "Site/App Optimized List",
    "BidListAdjustmentType": "Optimized",
    "ResolutionType": "ApplyMultiplyAdjustment",
    "BidLines":[
        {
        "BidAdjustment": 1.25,
        "DomainFragment": "example.com"
        },
        {
        "BidAdjustment": 1.1,
        "DomainFragment": "example.org"
        }
    ]
}
```

After creating a bid list, activate it by associating and enabling it.

### Common errors

The following are common errors you may encounter when creating bid lists. They are usually caused by incorrect property values, mismatched dimensions, or exceeding platform limits.

- You don't have access to the bid list owner or the bid line dimension specified for the bid list you're trying to create, or the owner and type don't align. For example, you cannot use an ad group ID with a campaign owner type.
- You try to create a target list with a bid adjustment other than `1`, or a block list with a bid adjustment other than `0`.
- You try to create a target or block list with a resolution type other than `ApplyMultiplyAdjustment`, or an optimized bid list without including the `ResolutionType` property.
- The number of bid lines exceeds the bid line limits, or the bid list contains bid lines with mismatched dimensions.

## Look up bid lists

To look up global bid lists (those maintained by The Trade Desk marketplace quality team), use the following endpoint. To look up other bid lists, including ones available to associate with a specific entity, see Bid list queries.

| Task | Endpoint | Requires bid list ID? | Filters |
| --- | --- | --- | --- |
| Get a list of global bid lists maintained by The Trade Desk marketplace quality team. | POST /v3/bidlistsummary/query/global | Not required | `DimensionDescriptorFilters` |
