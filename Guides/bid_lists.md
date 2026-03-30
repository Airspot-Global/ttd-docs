# Bid Lists

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/BidList
- Category: Guides

---

# Bid Lists

Bid lists are sets of bid dimensions and adjustments applied to ad groups to enhance the performance of your advertising campaigns. Each bid list is comprised of bid lines that define targeting, blocking, and bid factors based on shared dimensions (also known as vectors) including site, geography, and ad format. Unlike other [entity relationships](/v3/portal/api/doc/EntityRelationships), bid lists can be owned by and associated with partners, advertisers, campaigns, or ad groups, and can be enabled or disabled as needed.

## 

Terms and Definitions[](#terms)

The following table defines key terms used for bid lists.

| Term | Definition |
| Bid list | A collection of bid lines with the same dimensions. It is used to target, block, or apply optimizations to adjust the base bid of an ad group. For example, a bid list might include bid lines that target specific domains or geographic locations. Bid list names typically describe the dimension and adjustment type, such as "Site/App Target List". |
| Bid line | A component of a bid list used in digital advertising to adjust an ad group's base bid based on specific criteria. Each bid line consists of dimensions and bid factors. For details, see [bid factors](#bid-adjustments). |
| Dimension | A specific attribute or data point used to categorize, filter, or analyze audiences, campaigns, or inventory. It serves as a parameter for targeting, helping advertisers define who sees an ad. For example, you can target users based on a geographical dimension or a device dimension.  
Bid lists can be either single- or [multi-dimensional](/v3/portal/api/doc/DimensionalBidding#multi-dimension-bidding). |
| Bid factor | A multiplier applied to your base bid to adjust the value placed on specific dimensions, such as location, device type, or audience segment. |
| Bid adjustment type/bid list type | The method for controlling bidding strategies by aligning adjustments with specific criteria for each impression. It establishes rules for modifying bids, including allowing or denying participation in bidding or applying specific adjustments based on predefined dimensions. |
| Bid list owner | The entity that owns a bid list, such as the partner, advertiser, campaign, or ad group. This ownership determines who can use and manage the bid list. Owning does not automatically associate or enable the bid list for use. For details, see [Ownership](#bidlistownership). |
| Resolution type | The method for resolving multiple bid factors when an impression matches more than one bid line within the same bid list. Typically, this is done by multiplying bid factor values. |

## 

Bid Factors[](#bid-adjustments)

To manage bid expressiveness and add value to your campaigns, set bid factors to increase or decrease bids dynamically. For example, setting a higher bid factor means you value an impression highly and are willing to pay more for it. This increases your chances of winning and leads to more volume.

Bid factors indicate the value and performance of the bid lists rather than their pricing. To reflect how users value impressions, the base bid can be multiplied using these bid factor examples:

*   `0` to block bidding
*   `0.5` indicates that impressions with a dimension matching this attribute are half as valuable (indicating you want fewer like this and would pay less for it)
*   `1` to bid at the base bid price
*   `1.25` indicates that impressions with a dimension matching this attribute are 25% more valuable (indicating you want more like this and would pay more for it)

To lower the value of a bid, decrease the bid factor. This strategy is useful if you want to de-prioritize certain publishers. On the other hand, to indicate high value, increase the bid factor to more than `1`. For example, use a bid factor of `1.25` for users in a specific city or on a preferred device where performance is stronger.

To inform the bid price, these adjustments are factored in using our AI-driven algorithms, alongside metrics like KPI, relevance, and pacing. The final bid price is calculated based on this value but won't exceed the ad group's maximum bid. When pacing is on track, bid prices align with value influenced by the adjustments, impacting both volume and bid price direction.

## 

Anatomy of a Bid List[](#anatomy)

A bid list is a collection of bid lines with the _same_ dimensions. For example, the following diagram shows a campaign bid list with two example bid lines. Each bid line contains a domain fragment for the dimension and a bid factor. The bid list adjustment type is optimized with the resolution type of "Apply Multiply Adjustment," indicating matching bid factors are multiplied for the final adjustment. When activated (meaning it is associated and enabled), this bid list applies to the campaign and its ad groups. For details, see [Bid List Relationships](#bidlistrelationships).

![A chart showing a box labeled Bid List containing two boxes labeled Bid Line 1 and Bid Line 2. The adjustment type is "Optimized" and the resolution type is "Apply Multiply Adjustment." The bid line boxes each contain a dimension and bid factor. Bid Line 1 shows a dimension with the domain fragment of example.com and a bid factor of 1. Bid Line 2 shows the same domain fragment dimension, but with the value of example.org, and a bid factor of 1.75.](/v3/content/docs/Images/platform-single-dimensional-bidline-structure.svg)

The following sections explore differences between using GraphQL and the REST APIs, entity relationships, and association and inheritance limitations.

## 

Workflow[](#workflow)

After you understand the relationships between the [entities](/v3/portal/api/doc/EntityRelationships) and leverage them for maximum efficiency, managing bid lists becomes straightforward. You can manage bid lists for ad groups individually by creating a bid list for each, or uniformly by leveraging a single bid list at a parent entity level. To account for variations, you can set the bid list adjustment type to block unwanted domains within individual ad groups without editing parent bid lists.

There are two key steps in the process of manually creating bid lists:

1.  Create a bid list. This includes defining the correct level of ownership and key properties, such as bid factors.
2.  Activate the bid list by associating and enabling it for its owner or descendants. The bid list activation propagates to any descendants. For example, bid lists activated for an advertiser automatically apply to all new campaigns and ad groups.

When The Trade Desk receives bid requests from publishers and SSPs, we do the following:

1.  We match bid requests to bid lists and eligible ad groups.
2.  For each matching line in the bid list, we multiply the base bid with the bid factor and determine the final adjustment using the bid list resolution type.
3.  We calculate the final bid by multiplying the base bid for the ad group by its associated bid lists, bid factors, KPIs, relevance factors, pacing, and other signals.

### 

What You Need to Know[](#points)

Here's what you need to know about bid lists:

*   The ability to create a bid list requires permissions at the level of creation. For example, to create a partner-level bid list, you need partner-level permissions.
*   For target and block lists, a bid list is treated as a filter or restriction for your ad group. The more bid lists you apply, the fewer impressions are eligible for your bids because all requirements must be met.
*   Simply owning a bid list doesn't mean it's being used. To activate a bid list, associate it with the desired entity and enable it for the owner or a descendant.
*   Ad group bid lists override advertiser bid lists of the same type. For the purposes of your spend, the platform acts only on ad group bid lists, whether those are advertiser [default bid lists](/v3/portal/api/doc/BidListDefault) inherited from the advertiser or bid lists created for that ad group.
*   When you edit an existing list, those changes are also applied to that list as inherited by the entity’s descendants. For details, see [Inheritance](#bidlistinheritance).
*   Bid lists, whether created manually or generated through [Koa Optimizations](/v3/portal/api/doc/KoaOptimizations), respect both manual and Koa-generated adjustments.

## 

GraphQL vs. REST[](#gqlvsrest)

When it comes to managing bid lists, both [GraphQL](/v3/portal/api/doc/BidListsCreateManageGQL) and [REST](/v3/portal/api/doc/BidListsCreateManageREST) APIs offer distinct advantages. For example, bid list cloning is only available through GraphQL.

The following table compares the bid list actions supported by each API. For a general comparison of our platform APIs, see [Platform API: REST and GraphQL](/v3/portal/api/doc/ApisPlatform).

| Action | GraphQL | REST |
| Create a bid list. | Supported | Supported |
| Clone a bid list. | Supported | Not supported |
| Associate a bid list. | Supported | Supported |
| Enable a bid list. | Supported | Supported |
| Look up a bid list. | Supported | Supported |
| Update a bid list. | Supported | Supported |
| Delete a bid list. | Not supported | Supported |
| Create or update multiple bid lists at once. | Not supported | Supported. Use batch requests. |
| Make bid adjustments. | Supported. Use these options:

*   `INCLUSION`
*   `EXCLUSION`
*   `OPTIMIZED`

 | Supported. Use these options:

*   `TargetList`
*   `BlockList`
*   `Optimized`

 |

## 

Bid List Relationships[](#bidlistrelationships)

Bid lists can be owned, associated, and inherited at various [entity levels](/v3/portal/api/doc/EntityRelationships), including the partner, advertiser, campaign, and ad group. The following sections provide detailed information on each relationship and their specific uses.

> **IMPORTANT**: There are limits to the number of bid lines owned by or associated with an entity. For details, see [Relationship Limits](#bidlinelimits).

### 

Ownership[](#bidlistownership)

A bid list must have a single owner: a partner, advertiser, campaign, or ad group. Designating an owner allows the bid list to be propagated to its descendants, making it available for their use. For example, choosing a campaign as the owner of a bid list means that the campaign can share the bid list with its ad groups through association and inheritance, simplifying bid list management. On the other hand, selecting an ad group as the owner means the bid list is only available to that specific ad group and not to other ad groups within the campaign, other campaigns, or other advertisers.

> **NOTE**: The Trade Desk also supports global bid lists, like our global block list, but they are not included in this guide because they are managed by our marketplace quality team and not by entities in your advertising campaign. To see available global lists that you can associate, use [POST /v3/bidlistsummary/query/global](/v3/portal/api/ref/post-bidlistsummary-query-global).

Here's what you need to know about owning bid lists:

*   Ownership determines other bid list relationships, such as [associations](#bidlistassociation) with and [inheritance](#bidlistinheritance) by its descendants.
*   Owning a bid list does not automatically associate or enable a bid list for the owner or its descendants. You must associate and enable bid lists explicitly. For details, see [Association](#bidlistassociation).

The following diagram shows bid-list ownership across different entity levels. Each entity can own many bid lists.

![A diagram showing bid-list ownership among various entities.](/v3/content/docs/Images/bid-list-ownership.svg)

### 

Association[](#bidlistassociation)

For specific bid list adjustments to be applied, you must associate and enable bid lists for either the owner entity or a descendant for which the bid factors are intended. For details, see [Workflow](#workflow).

The following table lists the entities a bid list can be associated with based on its ownership. For example, a bid list owned by an advertiser can be associated only with that advertiser or one of its descendants (the campaigns and ad groups that the advertiser owns). The bid list cannot be associated with the parent partner or any other advertisers or their campaigns.

|  | Bid List Owned By |
| Bid Lists Can Be Associated With | Partner | Advertiser | Campaign | Ad Group |
| Partner | Owning Partner Only | No | No | No |
| Advertiser | Yes | Owning Advertiser Only | No | No |
| Campaign | Yes | Yes | Owning Campaign Only | No |
| Ad Group | Yes | Yes | Yes | Owning Ad Group Only |

> **TIP**: As bid list associations at the campaign or advertiser level are not visible in the UI, it is a best practice to associate bid lists at the ad group level.

The following diagram shows bid list association relationships at different entity levels. For example, a campaign-owned bid list can be associated only with that campaign or its ad groups, not with advertisers or partners.

![A diagram showing the bid-list association relationships among various entity levels.](/v3/content/docs/Images/bid-list-association.svg)

> **NOTE**: Bid lists cannot be associated with and enabled for more than one entity type within the same relational tree. For example, a partner-owned bid list cannot be associated with and enabled for both a campaign and an ad group within that campaign.

### 

Inheritance[](#bidlistinheritance)

To avoid needing to recreate, associate, and activate bid lists at multiple levels, entities and their descendants can inherit bid lines and bidding rules based on ownership. The following diagram shows bid-list inheritance relationships at different entity levels. For example, a campaign has its own bid lists while also inheriting bid lists from its parent entities, the partner and advertiser. This ensures that the campaign has the same associated and enabled bid lists as its parents without needing individual bid list activation at the campaign level.

![A diagram showing the bid-list inheritance relationships among various entity levels.](/v3/content/docs/Images/bid-list-inheritance.svg)

### 

Relationship Limits[](#bidlinelimits)

There are limits to the number of bid lines owned by or associated with each ad group, advertiser, or partner.

> **TIP**: To use bid lines efficiently, create bid lists at a parent-level entity that can be shared and [inherited](#bidlistinheritance) by the descendants.

| Entity Type | Maximum Number of Bid Lines | Bid Lines Counted Toward Limit |
| Partner | 20,000,000 | Bid lines in bid lists owned by a partner, including its advertisers, campaigns, and ad groups. |
| Advertiser | 5,000,000 | Bid lines in bid lists owned by an advertiser, including its campaigns and ad groups. |
| Campaign | No campaign limit | While there are no bid line limits for campaign-owned bid lists, these bid lines still count toward advertiser and partner limits. |
| Ad group | 10,000 | This limit applies to bid lines in ad-group owned bid lists associated with the ad group. Unassociated ad-group owned bid lists only apply to advertiser and partner limits. |

Exceeding bid line limits will cause bid list creation or updates to fail. The following limitations also apply:

*   These limitations do not apply to bid lists automatically generated by Koa. Manually created bid lists using Koa do count toward bid line limits.
*   To verify which bid lines are owned by an entity, use a [GraphQL query](/v3/portal/api/doc/BidListsCreateManageGQL#getbidlists) or the [POST /v3/bidlistsummary/query/{entity}/available](/v3/portal/api/ref/post-bidlistsummary-query-adgroup-available) endpoint in REST.
*   Bid lines within bid lists count toward partner and advertiser bid line limits until the bid list is deleted using the [DELETE /v3/bidlist/{bidListId}](/v3/portal/api/ref/delete-bidlist-bidlistid) endpoint.

## 

FAQs[](#faqs)

The following is a list of frequently asked questions about bid lists.

### 

How is the final bid for an ad group determined?

When a bid request is received, the final bid is calculated by multiplying the base bid with the bid factors from the various bid lists associated with the ad group, along with other signals like KPIs, relevance factors, and pacing. However, it won’t exceed the ad group’s maximum bid. For example, including a block list sets the bid factor to `0`, resulting in a $0 bid for the ad group regardless of other bid factors, effectively preventing bidding.

### 

I created a bid list for an entity, but how do I turn it on?

After creating a bid list, you need to also associate and enable it for the owner or its descendant. This includes setting the `isEnabled` property to `true`.

### 

How do I handle multiple bid list matches?

If an impression matches multiple bid lists, their adjustments apply. Target and block lists are restrictive: if an impression does not match a target list, or it matches a block list, it receives a bid factor of `0`, overriding all other adjustments.

### 

How do I resolve multiple bid line matches in a single bid list?

When an impression matches multiple bid lines in the same bid list, the final adjustment is determined by the bid list resolution type.

> **IMPORTANT**: If you're using the target or block list bid adjustment type, you must set the resolution type to multiply bid factors from a bid list to calculate the final adjustment. It's recommended, but not required, for optimized lists.

An impression can match multiple bid lines in a few dimensions:

*   `DomainFragment` - An impression could match multiple sites or apps if the list includes both domains and subdomains.
*   `GeoSegmentId` - An impression for a geographical area could match multiple lines if it falls into different area types (country, state, region, city).
*   `RecencyWindowInMinutes` - If the bid list contains overlapping ranges, an impression could match multiple lines for recency. Avoid setting up overlapping ranges.
*   `TemperatureRangeInCelsius` - If the bid list contains overlapping ranges, an impression could match multiple lines for temperature. Avoid setting up overlapping ranges.
*   `FrequencyTarget` - If the bid list contains overlapping ranges, an impression could match multiple lines for frequency.

### 

When creating a bid list with more than 1000 bid lines in GraphQL, I get a token limit error. How should I resolve this?

For better performance and stability, GraphQL restricts the number of tokens that can be included in a request. To manage token usage efficiently, use variables as a workaround.

The following code example shows a `bidListCreate` mutation that passes a `BidLineCreateInput` object using a `$bidLines` variable. Though only one bid line is shown, this method supports adding more than 1000 bid lines to the `$bidlines` variable, minimizing the risk of exceeding token limits.

mutation BidListCreate($bidLines: \[BidLineCreateInput!\]!) {

    bidListCreate(input: {bidLines: $bidLines})

}

The corresponding variable is:

{

    "bidLines":\[{"domainFragment": "example.com"}\]

}

For details on the error, see [GraphQL API Errors and Complexity Limits](/v3/portal/resources/doc/GqlResponses).