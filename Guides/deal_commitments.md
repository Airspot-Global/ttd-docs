# Commitment deals

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/deals/doc/PlatformDealCommitments
- Retrieved: 2026-11-14
- Category: Guides

---

# Commitment deals

Commitment deals are promises between all deal participants that both parties are responsible of delivering. These commitments have additional terms for expansion and cancellation, and require setting goals for media spend.

> **NOTE**: Both commitment deals and programmatic guaranteed deals (PG) are listed under the commitment deal type when querying the API.

## Retrieve commitment deal terms

A commitment deal is an agreement that specifies a target cost for media investment. It ensures that the designated investment amount is fulfilled between the participating parties. Commitment deals highlight these terms by setting minimum win rate guarantees and makegoods. To view the terms of a commitment deal, query for the `targetableDeals` object with the corresponding deal ID.

The following `partner` example is shortened due to the range of possible terms.

```
query GetPartnerCommitmentTermsExample {
  partner(id: "PARTNER_ID_PLACEHOLDER") {
    targetableDeals(where: {
      id: {
        eq: "COMMITMENT_DEAL_ID_PLACEHOLDER"
      }
    }) {
      nodes {
        id
        acceptedAt
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
        activityLog {
          nodes {
            actor
            body
            contact {
              name
              email
            }
            createdAt
            status
          }
        }
        displayName
        dealOwnerPartner {
          id
          name
          contact {
            email
            name
          }
        }
        externalDealId
        forecastMetrics {
          addressability
          auctionIntegrity
          campaignPerformanceContribution
          dealQualityScore
          decisionPower
          duplicationRate
          inventoryExclusivity
          priceCompetitiveness
          relevance
          signalFidelity
        }
        inventorySupplier {
          logoUrl
          id
          name
          contact {
            email
            name
          }
        }
        isArchived
        marketAverageForecastMetrics {
          signalFidelity
          duplicationRate
          auctionIntegrity
          addressability
        }
        name
        pausedByBuyer
        privateContractId
        reportingMetrics {
          cpm
          spend
          tvqi
        }
        spendingStatus
        supplyVendor {
          name
          logo
          id
        }
      }
    }
  }
}
```

## Mutations

The following table lists all the tasks you can perform with commitment deals.

| Task | Mutation |
| --- | --- |
| Add a note to the commitment deal. | `inventoryCommitmentNoteCreate` |
| Update the commitment deal name or display name. This name can contain up to 256 characters. | `inventoryCommitmentUpdate` |
| Expand the commitment deal to include expanded deal terms. | `inventoryCommitmentExpand` |
| Cancel the commitment deal after the cancellation threshold has been met. | `inventoryCommitmentCancel` |
| Archive the commitment deal. | `inventoryCommitmentArchive` |

## Add a note to the commitment deal

To add a note to a commitment deal, use the `inventoryCommitmentNoteCreate` mutation and enter your message in the `note` field.

The following `inventoryCommitmentNoteCreate` mutation example shows how to add a note.

```
mutation {
  inventoryCommitmentNoteCreate(input: {
    commitmentId: "COMMITMENT_DEAL_ID_PLACEHOLDER"
    note: "NOTE_TEXT_PLACEHOLDER"
    createdBy: {
      email: "SENDER_EMAIL_PLACEHOLDER"
      name: "SENDER_NAME_PLACEHOLDER"
    }
  }) {
    data { id }
  }
}
```

## Update the commitment deal

To update a commitment deal, use the `inventoryCommitmentUpdate` mutation and update the `name` or `displayName` fields.

The following `inventoryCommitmentUpdate` mutation example shows how to rename your deal.

```
mutation {
  inventoryCommitmentUpdate(input: {
    commitmentId: "COMMITMENT_DEAL_ID_PLACEHOLDER"
    displayName: "DISPLAY_NAME_PLACEHOLDER"
    name: "NAME_PLACEHOLDER"
  }) {
    data { id }
  }
}
```

## Expand the commitment deal

Deal expansion is an optional term set in commitment deal terms to increase the amount of available inventory that the selling party sends. If your deal supports deal expansion, you can accept more bid requests from the sources listed in the expanded terms. To apply expansion, you must meet the following requirements:

The deal is a live commitment deal.
 The lifetime pacing is below the threshold set for expansion.
 The deal has been underpacing for a set period of days.
 The deal terms contain expanded terms.

After a deal has met the requirements, you can use the `inventoryCommitmentExpand` mutation to start getting avails that match the expanded terms.

The following `inventoryCommitmentExpand` mutation example shows how to expand commitment deals that are pacing below the set threshold. If your commitment deal isn't pacing below the threshold or doesn't contain expansion terms, the mutation returns an error and doesn't expand the deal.

```
mutation {
  inventoryCommitmentExpand(input: {
    commitmentId: "COMMITMENT_DEAL_ID_PLACEHOLDER"
  }) {
    userErrors {
      message
    }
  }
}
```

## Cancel the commitment deal

In cases where the deal underpaces and the selling party is at fault, you can cancel the deal without penalty. To cancel a deal, it must meet the following requirements:

The deal is a live commitment deal.
 The lifetime pacing is below the threshold set for cancellation.
 The deal has been underpacing for a set period of days.

The deal has one of the following faults:

- The deal hasn't met the minimum bid rate and minimum win rate in the terms.
- The deal isn't sending the minimum number of avails.

After a deal has met these requirements, you can use the `inventoryCommitmentCancel` mutation to let the selling party know to send avails that match the expanded terms.

The following `inventoryCommitmentCancel` mutation example shows how to cancel a commitment deal.

```
mutation {
  inventoryCommitmentCancel(input: {
    commitmentId: "COMMITMENT_DEAL_ID_PLACEHOLDER"
  }) {
    userErrors {
      message
    }
  }
}
```

> **TIP**: After canceling a deal, you should archive the deal to clean up any remaining data. For details, see Active deal management.

## Archive the commitment deal

To end a deal in flight, you need the deal ID and latest revision number. To get the latest revision number, query for the latest active and pending status of the deal and use the larger revision number.

The following `partner` query returns the revision numbers for a commitment deal.

```
query GetCommitmentRevisionVersionExample {
  partner(id: "PARTNER_ID_PLACEHOLDER") {
    targetableDeals(where: {
      id: {
        eq: "DEAL_ID_PLACEHOLDER"
      }
    }) {
      nodes {
        id
        active {
          revisionNumber
        }
        pending {
          revisionNumber
        }
      }
    }
  }
}
```

After you have the revision number, you can archive the deal with the `inventoryCommitmentArchive` mutation. The following example archives a commitment deal with the latest revision number of `2`.

```
mutation {
  inventoryCommitmentArchive(
    input: {
      inventoryCommitmentRevisions: {
        commitmentId: "COMMITMENT_DEAL_ID_PLACEHOLDER"
        revisionNumber: 2
      }
    }
  )
}
```
