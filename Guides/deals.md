# Getting Started with Deals

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/PlatformDealOverview
- Category: Guides

---

# Getting Started with Deals

Deals are formed as private marketplace contracts where a [selling party](#party-terminology) can directly sell you, a buying party, access to their inventory not available in the open marketplace.

In the Platform API or Deal Desk UI, you can assess deal quality before campaigns launch, and organize and respond to deal proposals. After deals are accepted, The Trade Desk provides real-time reporting metrics to improve deal transparency around supply path optimization and price discovery.

The following sections outline deal types, key terminology, and the roles and responsibilities of each party involved.

## 

Deal Types[](#deal-types)

The Platform API provides two structured deal types—commitments and endeavors—both designed to work with Kokai's decisioning features and default-on settings.

The following table lists the main types of deals available.

| Type | Description |
| Commitment | A commitment deal is an agreement in the platform that specifies a target cost for media investment and a timeframe for its delivery. The Trade Desk platform ensures that the participating parties can fulfill the designated investment amount. A commitment deal specifies a selling party, a buying party, and the inventory composition including publishers and other parameters. |
| Endeavor | An endeavor deal is an agreement that grants a buying party access to inventory from one or more publishers. It can optionally include inventory composition, pricing, seeking differentiation in terms of value and availability. |

Here's what you need to know about deals regardless of their type:

*   All deals are approved electronically on The Trade Desk platform by two parties: a single authorized The Trade Desk partner, such as an agency, and the deal owner, such as supplier such as a seller or intermediary.
*   A deal can specify what types of inventory is being sold, relevant inventory composition, and commitment goals, when applicable.
*   The selling party must respect the do-not-air lists, provided by the advertiser through the Platform API, across any deals or open market buys.
*   All inventory transacted through a deal must include all necessary signals listed in the bidding terms.
*   To identify the deal and accurately track the associated spend The Trade Desk platform, include the deal ID in the bid response.

### 

Commitment Deals[](#commitment)

A commitment deal is an agreement in the platform that specifies goals for media investment. It ensures that the committed spend amount is fulfilled between the participating parties. Here are some key characteristics about the terms you might see in commitment deals:

*   Commitment deals must include a minimum win rate guarantee. If the win rate drops below this level for several days, you can request to cancel the deal.
*   The selling party must respect your do-not-air lists across any deals and open market buys.
*   Commitments can be a single deal, or as all the spend from a given agency into a given partner inventory.
*   Commitments may include expansion terms to unlock additional inventory if pacing towards the media spend goal falls behind.
*   The selling party defines cancellation terms, which are used to cancel the deal when pacing falls further below the agreed threshold.
*   You can ask the selling party to include additional deal IDs to count spend toward the commitment goal from other deals without spend goals. This spend is counted when the inventory from the contributing deal matches the commitment's terms.

For details, see [Commitment Deals](/v3/portal/api/doc/PlatformDealCommitments).

### 

Endeavor Deals[](#endeavor)

An endeavor deal is an agreement that grants access to a specific segment of a publisher's inventory. Endeavor deals are similar to commitments in terms of available terms, except for the following differences:

*   Unlike commitments, endeavor deals aren't strongly enforced and have flexible terms.
*   The selling party can pause your endeavor deals in-flight.
*   Endeavor deals with no media spend goal can contribute their spend toward another deal's media spend goal—either a commitment deal or another endeavor deal with a media spend goal.

For details, see [Endeavor Deals](/v3/portal/api/doc/PlatformDealEndeavors).

## 

Deal Participant Responsibilities[](#party)

The following diagram outlines the responsibilities of the buying party, selling party, and The Trade Desk when sending deals, while the sections that follow provide additional details.

![Deal Creation Party Diagram](/v3/content/docs/Images/PDP-sequence-deal-creation.svg)

### 

Terminology[](#party-terminology)

The following sections defines key terms for understanding the classification of deal participants in the Platform API and Deal Desk UI.

| Term | Description |
| Buying Party | An agency or advertiser on The Trade Desk platform that negotiates, accepts, and bids on the deal. The buying party is the primary owner and administrator of the deal on The Trade Desk platform. |
| Selling Party | A seller, intermediary, or publisher that creates proposals for negotiated deals. It represents the sell-side user and uses the account ID to propose deals with the PDP API. |
| Additional Participants | Additional participants who own seats on The Trade Desk platform that you allow to bid on the proposed deal. As the deal owner, you create a delivery profile and allows access to additional participants. |
| Seller | An entity that owns one or more publishers, and sells inventory created by those publishers. Seller IDs are typically sourced from the `sellers.json` file.  
**NOTE**: Under limited circumstances, a classified seller might also resell small amounts of inventory owned by another seller. |
| Publisher | A content owner whose content or inventory is available for sale by a seller. The PDP API maps publishers using information found in the `ads.txt` file, with additional curation from The Trade Desk. |
| Intermediary | An entity, such as an SSP, that facilitates ad inventory distribution but doesn't own inventory. |
| Agency | An advertising agency that buys ad inventory on behalf of a brand.  
**NOTE**: Under limited circumstances, a classified seller might also be an agency. |
| Advertiser | A brand that acquires inventory through The Trade Desk platform. |

Details on deal management for each party are included in the corresponding sections. See also [The Trade Desk Glossary](/v3/portal/resources/doc/Glossary).

### 

Buying Party[](#buy)

As the buying party, you're expected to do the following:

*   Accept or reject deal proposals, and communicate with the selling party to modify the deal terms.
*   Configure ad groups to target your deals and update base bid prices to match floor prices.
*   Set [deal decisioning](/v3/portal/api/doc/PlatformDealNonDecisioned), prioritization, and default-on preferences.

### 

Selling Party[](#sell)

The selling party is expected to do the following:

*   Send deals to a buying party for acceptance.
*   Communicate changes to accepted deals with additional proposals.
*   Meet the deal requirements for minimum daily avails and promised win rates.
*   Provide access to unique inventory not found in the public marketplace.

> **IMPORTANT**: Supply vendors and publishers must have a clearly defined `ads.txt` file deployed on their site. See also [Inventory Policies](/v3/portal/ssp/doc/InventoryPolicies#transparency).

### 

The Trade Desk[](#ttd)

The Trade Desk does the following through the PDP API or Deal Desk:

*   Provide deal quality scores to help brands make data-driven decisions.
*   Examine deal avails, signal completeness, and monitor delivery metrics when applicable.
*   Offer reporting tools to track commitments and pacing, helping all deal participants stay on track with their goals.

## 

Benefits[](#benefits)

Our Platform API offers several key benefits that improve efficiency, accuracy, and performance towards managing and reporting for deals:

*   **Reduces reliance on manual input**: Structured deal metadata minimizes errors by automating and clarifying inventory identification.
*   **Improves deal accuracy**: Clear identification of inventory ensures precise targeting and correct parameters.
*   **Enhances performance analysis**: Accurate metadata enables better tracking and analysis of deal performance.
*   **Supports better decision-making**: Improved data allows for more informed alternatives and recommendations.
*   **Lowers operational costs**: Reduces time-consuming troubleshooting and errors associated with poorly devised deals.
*   **Eliminates redundant deals**: Avoids duplication of inventory already available through the open market or always-on deals.
*   **Increases efficiency of advertising investments**: Optimizes the deployment of resources by improving deal structure and targeting.
*   **Improves delivery and performance of programmatic investments**: Major programmatic commitments benefit from more accurate, high-performing deals.