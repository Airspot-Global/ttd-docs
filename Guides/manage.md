# Manage Deals

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/PlatformDeal
- Category: Guides

---

# Manage Deals

As a buying party, you receive deal proposals from selling parties. These often offer access to exclusive inventory that's not available on the public marketplace, SP500+, or Blue Lists, with custom floor prices. Using the Platform API, you can evaluate and respond to these pending deal proposals.

> **NOTE**: To run the following queries or mutations, you must use [API token authentication](/v3/portal/api/doc/Authentication).

Here's what you need to know about deal proposals and revisions:

*   There are two types of deals: [commitment](/v3/portal/api/doc/PlatformDealCommitments) and [endeavor](/v3/portal/api/doc/PlatformDealEndeavors).
*   You can message the selling party to suggest changes to the deal.
*   To address your concerns, the selling party can revise existing deals at any time.
*   When you archive a deal, the deal is removed from your queries.
*   When a new revision is made, you must accept or reject the latest revision for the changes to take effect.

> **IMPORTANT**: When a deal is paused by the selling party, all flights in the deal are frozen.

## 

Workflow Overview[](#workflow)

Deals are managed as a contract between two parties and go through many revisions. The following example describes a common workflow from deal negotiation to the end of flight.

1.  You examine multiple deals sent to you from multiple selling parties.
2.  Decide to accept or reject each deal proposal.

1.  Optionally, you can also message the selling party to ask for changes.

4.  After a deal is accepted, add the deal ID to your inventory requests.
5.  While the deal is active, either party can adjust the terms or end the deal early:

1.  The selling party can renew or extend the deal by modifying the flight duration or pause the deal.
2.  Commitment deals require a valid reason to end the flight early, such as underdelivery of the promised win rate or minimum avails.
3.  Endeavor deals can be paused or archived to end the flight early.

## 

Deal Origins[](#origin)

Deals that come from outside of The Trade Desk deal ecosystem are marked as external deals and require you to manually include the deal ID when you bid for the inventory. These external deal use an additional `externalDealId` property in their respective `inventoryCommitment` or `inventoryEndeavor` object.

Here's what you need to know about deal types:

*   The type of deal changes the financial terms and mutations allowed.
*   Each deal creates an endeavor ID or a commitment ID to use as the deal ID.
*   You cannot mix deal IDs and mutations from different types.
*   You must send individual requests to check the status of commitment deals versus endeavor deals.

## 

Deal Metadata[](#metadata)

To view all your deals, send a query for the deal properties to the platform using GraphQL. When querying you must search through the `targetableCommitments` or `targetableEndeavors` object to specify what type of deal and use the corresponding `inventoryCommitment` or `inventoryEndeavor` object to apply filters. The following table lists the most useful properties to filter a deal by.

| Property | Description |
| `name` | The name of a commitment or endeavor deal. |
| `id` | The ID of a commitment or endeavor deal. |
| `terms` | The terms of the deal, set by the selling party. |
| `status` | The status of the deal proposal sent by the selling party. |
| `spendingStatus` | The status of a previously accepted deal in flight. |
| `active` | The revision terms of the currently active deal. |
| `pending` | The revision terms of the latest version of the deal. |
| `forecastMetrics` | The forecast metrics for the deal. |
| `reportingMetrics` | The reporting metrics for the deal. |

## 

Check Deals Pending Your Acceptance[](#proposal-pending)

To view your pending deals, query for the status that has the `PENDING` value. To ensure you don't miss a deal, use [pagination](/v3/portal/resources/doc/GqlApiQueries#pagination).

The following `partner` query returns up to 25 pending commitment deals for a partner. Advertisers can replace the partner object with the advertiser object to use your advertiser ID as the `id` value. To query for pending endeavor deals, use the `targetableEndeavors` field.

> **IMPORTANT**: Include the `active` object in your query if your deal is live. Otherwise, use the `pending` object.

query GetPartnerPendingCommitmentDealsExample {

  partner(id: "PARTNER\_ID\_PLACEHOLDER") {

    targetableCommitments (

      where: {

        spendingstatus: {

          eq: PENDING

        }

      }, first: 25)

    {

      nodes {

        id

        totalCount

        active {

          createdAt

          description

          displayName

          name

          revisionNumber

          status

          biddingTerms {

            name

            observedPercentage

            marketPercentage

          }

        }

        pending {

          createdAt

          description

          displayName

          name

          revisionNumber

          status

          biddingTerms {

            name

            observedPercentage

            marketPercentage

          }

        }

      }

    }

  }

}

> **NOTE**: The revision number starts at 1, and increments each time a new proposal is sent.

### 

Accept a Deal[](#proposal-accept)

To accept a deal, use the `inventory{DealType}Accept` mutation, replacing `{DealType}` with `Commitment` or `Endeavor`, depending on the type of deal you're accepting. The following `inventoryCommitmentAccept` mutation example accepts a commitment deal.

mutation {

  inventoryCommitmentAccept(input: {

    commitmentId: "COMMITMENT\_DEAL\_ID\_PLACEHOLDER",

    revisionNumber: 1}

  ) {

    userErrors {

      field

      message

    }

  }

}

### 

Reject a Deal[](#proposal-reject)

To accept a deal, use the `inventory{DealType}Accept` mutation, replacing `{DealType}` with `Commitment` or `Endeavor`, depending on the type of deal you're accepting.

The following `inventoryCommitmentAccept` mutation example rejects a revision to the commitment deal.

mutation {

  inventoryCommitmentReject(input: {

    commitmentId: "COMMITMENT\_DEAL\_ID\_PLACEHOLDER",

    revisionNumber: 2}

  ) {

    userErrors {

      field

      message

    }

  }

}

After you have identified your pending deals, see the corresponding [Endeavor Deal Query](/v3/portal/api/doc/PlatformDealEndeavors#endeavor) or [Commitment Deal Query](/v3/portal/api/doc/PlatformDealCommitments#commitment) sections to view the deal details.

## 

Active Deal Management[](#active)

After your deal is active, you can start using the deal by including the deal ID in your campaign bid requests.

> **IMPORTANT**: To bid on your accepted deals, the max bid CPM of the ad group or campaign must be greater than or equal to the floor price of the deal.

To view which deals are in flight, query for the deal IDs with the `spendingStatus` property equal to the `ACTIVE` value.

The following `partner` query returns the deal IDs of up to 10 active commitment deals.

query GetPartnerCommitmentActiveDealsExample {

  partner(id: "PARTNER\_ID\_PLACEHOLDER") {

    targetableCommitments (

      where: {

        spendingstatus: {

          eq: ACTIVE

        }

      }, first: 10)

    {

      nodes {

        id

        totalCount

      }

    }

  }

}

### 

Set Default-On Deal[](#default-deals)

Default-on, also known as automatic deal inclusion, helps reduce manual deal management and improves inventory coverage by assigning new deals to existing pre-configured ad groups. To opt-in, use the `inventoryDealDefaultOnSet` mutation and set the `isDefaultOn` value to true. The following example shows how to set a deal as default-on.

mutation {

  inventoryDealDefaultOnSet(input: {

    inventoryDealsWithTargetingAssociated: \[

      {

        dealId: "DEAL\_ID\_PLACEHOLDER"

      }

    \],

    isDefaultOn: true

  }) {

    errors {

      ... on MutationError {

        field

        message

      }

    }

  }

} 

### 

Set Default-On Ad Group[](#default-adgroup)

After setting the deal to default-on, you can target your ad groups with the `adGroupSetDefaultOnEndeavorsTargeting` mutation to select ad groups that can target the deal. The following example shows how target ad groups with default-on deals.

mutation {

  adGroupSetDefaultOnEndeavorsTargeting(input: {

    adGroupId: "AD\_GROUP\_ID\_PLACEHOLDER"

    isTargetingDefaultOnEndeavors: true

  }) {

    userErrors {

      field

      message

    }

  }

}

### 

Target an Ad Group[](#default-target)

To target your endeavor deal, use the `adGroupSetEndeavorTargeting` mutation. The following example shows how to add or remove endeavors from deal targeting.

mutation {

  adGroupSetEndeavorTargeting(input: {

    adGroupId: "AD\_GROUP\_ID\_PLACEHOLDER"

    endeavorsIdsToAdd: \[

      "ENDEAVOR\_DEAL\_ID\_PLACEHOLDER"

    \]

    endeavorsIdsToRemove: \[\]

  }) {

    userErrors {

      field

      message

    }

  }

}

## 

FAQs[](#faqs)

The following are commonly asked questions about managing deals as an advertiser.

### 

How do I add deal targeting?

Start by creating a campaign and ad group. After creating the ad group, you can configure deal targeting through bid lists associated with the ad group.

### 

Can I target deals that haven't yet been accepted?

No. You can create an ad group before deal acceptance, but you can't target a deal until it's accepted. For details, see [Commitments](/v3/portal/api/doc/PlatformDealCommitments) or [Endeavors](/v3/portal/api/doc/PlatformDealEndeavors).

### 

Can I create a campaign with deal targeting?

No. Deal targeting applies at the ad group level.

### 

Can deals created in Deal Desk be accepted using the API?

Yes. Provide the deal ID from Deal Desk and call the corresponding `inventoryCommitmentAccept` or `inventoryEndeavorAccept` mutation. For details, see [Accept a Deal](#proposal-accept).