# Manage Deals

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/deals/doc/PlatformDeal
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/doc/PlatformDeal (retired)
- Retrieved: 2026-11-14
- Category: Guides

---

# Manage deals

As a buying party, you receive deal proposals from selling parties. These often offer access to exclusive inventory that's not available on the public marketplace, Sellers and Publishers 500+ (SP500+), or Blue Lists, with custom floor prices. Using the Platform API, you can evaluate and respond to these pending deal proposals.

> **NOTE**: To run the following queries or mutations, you must use API token authentication.

Here's what you need to know about deal proposals and revisions:

- There are three types of deals: Commitment, Programmatic Guaranteed, and Standard.
- You can message the selling party to suggest changes to the deal.
- To address your concerns, the selling party can revise existing deals at any time.
- When you archive a deal, the deal is removed from your queries.
- When a new revision is made, you must accept or reject the latest revision for the changes to take effect.

> **IMPORTANT**: When a deal is paused by the selling party, all flights in the deal are frozen.

## Workflow overview

Deals are managed as a contract between two parties and go through many revisions. The following example describes a common workflow from deal negotiation to the end of flight.

1. You examine multiple deals sent to you from multiple selling parties.
2. Decide to accept or reject each deal proposal. Optionally, you can also message the selling party to ask for changes.
3. After a deal is accepted, add the deal ID to your inventory requests.
4. While the deal is active, either party can adjust the terms or end the deal early:

  - The selling party can renew or extend the deal by modifying the flight duration or pausing the deal.
  - Commitment deals require a valid reason to end the flight early, such as underdelivery of the promised win rate or minimum avails.
  - Standard deals can be archived to end the flight early.

## Deal origins

Every deal originates either inside The Trade Desk deal ecosystem or outside of it. Regardless of origin:

- The type of deal changes the financial terms and mutations allowed.
- Every deal is given an an ID, either by The Trade Desk or an external party.
- Some deal types have specific mutations.
- You must send individual requests to check the status of deals.

Deals that come from outside of The Trade Desk deal ecosystem are marked as external deals and require you to manually include the deal ID when you bid for the inventory. An external deal uses an additional `externalDealId` property in their respective `targetableDeals` object.

## Deal metadata

To view all your deals, send a query for the deal properties to the platform using GraphQL. When querying you must search through the `targetableDeals` object to specify what type of deal. The following table lists the most useful properties to filter a deal by.

| Property | Description |
| --- | --- |
| `name` | The name of a deal. |
| `id` | The ID of a deal. |
| `terms` | The terms of the deal, set by the selling party. |
| `status` | The status of the deal proposal sent by the selling party. |
| `spendingStatus` | The status of a previously accepted deal in flight. |
| `active` | The revision terms of the currently active deal. |
| `pending` | The revision terms of the latest version of the deal. |
| `forecastMetrics` | The forecast metrics for the deal. |
| `reportingMetrics` | The reporting metrics for the deal. |

## Check deals pending your acceptance

To view your pending deals, query for the status that has the `PENDING` value. To ensure you don't miss a deal, use pagination.

The following `partner` query returns up to 25 pending deals for a partner. Advertisers can replace the partner object with the advertiser object to use your advertiser ID as the `id` value.

> **IMPORTANT**: Include the `active` object in your query if your deal is live. Otherwise, use the `pending` object.

```
query GetPartnerPendingDealsExample {
  partner(id: "PARTNER_ID_PLACEHOLDER") {
    targetableDeals (
      where: {
        spendingstatus: {
          eq: PENDING
        }
      }, first: 25)
    {
      nodes {
        id
        totalCount
        active {
          createdAt
          description
          displayName
          name
          revisionNumber
          status
          biddingTerms {
            name
            observedPercentage
            marketPercentage
          }
        }
        pending {
          createdAt
          description
          displayName
          name
          revisionNumber
          status
          biddingTerms {
            name
            observedPercentage
            marketPercentage
          }
        }
      }
    }
  }
}
```

> **NOTE**: The revision number starts at 1, and increments each time a new proposal is sent.

### Active deal management

After your deal is active, you can start using the deal by including the deal ID in your campaign bid requests.

> **IMPORTANT**: To bid on your accepted deals, the max bid CPM of the ad group or campaign must be greater than or equal to the floor price of the deal.

To view which deals are in flight, query for the deal IDs with the `dealStatus` property equal to the `ACTIVE` value.

The following `partner` query returns the deal IDs of up to 10 active commitment deals.

```
query GetPartnerActiveDealsExample {
  partner(id: "PARTNER_ID_PLACEHOLDER") {
    targetableDeals (
      where: {
        dealStatus: {
          eq: "LIVE"
        }
      }, first: 10)
    {
      nodes {
        id
        totalCount
      }
    }
  }
}
```

## Mutations

The following table shows mutations that can be used regardless of deal type.

| Task | Mutation |
| --- | --- |
| Accept the latest deal revision for a deal. | `dealAccept` |
| Decline the latest deal revision for a deal. | `dealReject` |
| Assign the deal to newly created ad groups. **NOTE**: This was previously referred to as "default-on" deals but is now the "deal market." | `inventoryDealDefaultOnSet` |
| Update the prioritization of a deal across all advertisers. | `inventoryDealsPrioritizationSet` |
| Update the advertiser-level prioritization of a deal for a given advertiser. | `inventoryDealPrioritizationAdvertiserOverrideSet` |
| Reset the delivery profile settings. If the deal has no buying permissions set, the delivery profile resets to the owning partner of the deal. | `inventoryDealDeliveryProfileReset` |
| Update the deal market targeting setting for an ad group. | `adGroupSetDefaultOnDealsTargeting` |
| Update the inventory targeting for an ad group. | `adGroupInventoryTargetingUpdate` |

> **IMPORTANT**: Some mutations are only usable by specific deal type. For details, see Deal-specific mutations.

### Accept a deal

To accept a deal, use the `dealAccept` mutation and provide the deal ID.

```
mutation {
  dealAccept(input: {
    dealId: "DEAL_ID_PLACEHOLDER"
  }) {
    data {
      id
      dealType
    }
  }
}
```

### Reject a deal

To reject a deal, use the `dealReject` mutation and provide the deal ID.

```
mutation {
  dealReject(input: {
    dealId: "DEAL_ID_PLACEHOLDER"
  }) {
    data {
      id
      dealType
    }
  }
}
```

After you have identified your pending deals, see the corresponding Standard deal query or Commitment deal query sections to view the deal details.

## Target deals and ad groups

After accepting a deal, set up ad groups to target it directly, or add the deal to a deal market so that newly created ad groups automatically target it when eligible.

### Set deal market for deal

The deal market, also known as automatic deal inclusion, helps reduce manual deal management and improves inventory coverage by assigning new deals to existing pre-configured ad groups.

To opt in to the deal market, use the `inventoryDealDefaultOnSet` mutation. The following example shows how to set a deal to use the deal market.

```
mutation {
  inventoryDealDefaultOnSet(input: {
    inventoryDealsWithTargetingAssociated: [
      { dealId: "DEAL_ID_PLACEHOLDER"
      }
    ]
    isDefaultOnSet: true
  }) {
    data {
      id
      dealType
    }
  }
}
```

### Set deal market for ad group

After setting the deal to use the deal market, you can target your ad groups with the `adGroupSetDefaultOnDealsTargeting` mutation to set an ad group that the new deals always target. The following example shows how target ad groups with the deal market.

```
mutation {
  adGroupSetDefaultOnDealsTargeting(input: {
    adGroupId: "AD_GROUP_ID_PLACEHOLDER"
    isTargetingDefaultOnDeals: true
  }) {
    data { id }
  }
}
```

### Target an ad group

To target your standard deal, use the `adGroupInventoryTargetingUpdate` mutation. The following example shows all the ad group targeting parameters that the deal targets.

```
mutation {
  adGroupInventoryTargetingUpdate(input: {
    adGroupId: "AD_GROUP_ID_PLACEHOLDER"
    dealBidFactorsToUpdate: [
      {
        dealId: "DEAL_ID_PLACEHOLDER"
        bidFactor: "BID_FACTOR_PLACEHOLDER"
      }
    ]
    dealGroupIdsToExclude: ["DEAL_GROUP_ID_PLACEHOLDER"]
    dealGroupIdsToInclude: ["DEAL_GROUP_ID_PLACEHOLDER"]
    dealIdsToExclude: ["DEAL_ID_PLACEHOLDER"]
    dealIdsToInclude: ["DEAL_ID_PLACEHOLDER"]
    excludeAllDealGroups: false
    excludeAllDeals: false
    includeDefaultOnDeals: false
    inventoryMarketType: "MARKETPLACE"
  }) {
    data { id }
  }
}
```

### Deal-specific mutations

Some mutations are only usable depending on the deal type. For details, see the corresponding Programmatic Guaranteed deals, Standard deal or Commitment deal pages.

### Commitment deal mutations

 >**IMPORTANT**: PG deals share the same commitment mutations, but do not support expansion or cancellation.

The following are mutations for commitment deals.

| Task | Mutation |
| --- | --- |
| Add a note to a commitment deal. | `inventoryCommitmentNoteCreate` |
| Update the commitment deal name or display name. This name can contain up to 256 characters. | `inventoryCommitmentUpdate` |
| Expand a commitment deal to include expanded deal terms. | `inventoryCommitmentExpand` |
| Cancel the commitment deal after the cancellation threshold has been met. | `inventoryCommitmentCancel` |
| Archive a commitment deal. | `inventoryCommitmentArchive` |

### Standard deal mutations

 The following are mutations for standard deals, also known as endeavor deals in function calls.

| Task | Mutation |
| --- | --- |
| Add a new note for the specified standard deal and revision. | `inventoryEndeavorNoteCreate` |
| Update the standard deal name or display name. | `inventoryEndeavorUpdate` |
| Archive one or more standard deals. | `inventoryEndeavorsArchive` |
| Unarchive one or more standard deals. | `inventoryEndeavorsUnarchive` |

## FAQs

The following are commonly asked questions about managing deals as an advertiser.

### How do I add deal targeting?

Start by creating a campaign and ad group. After creating the ad group, you can configure deal targeting through bid lists associated with the ad group.

### Can I target deals that haven't yet been accepted?

No. You can create an ad group before deal acceptance, but you can't target a deal until it's accepted. For details, see Commitment deals or Standard deals.

### Can I create a campaign with deal targeting?

No. Deal targeting applies at the ad group level.

### Can deals created in Deal Desk be accepted using the API?

Yes. Provide the deal ID from Deal Desk and call the corresponding `inventoryCommitmentAccept` or `inventoryEndeavorAccept` mutation. For details, see Accept a deal.
