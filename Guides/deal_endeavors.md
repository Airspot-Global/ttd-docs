# Standard deals

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/deals/doc/PlatformDealEndeavors
- Retrieved: 2026-11-14
- Category: Guides

---

# Standard deals

Standard deals are useful for getting access to inventory without a hard commitment to meeting spend goals. These deals have flexible terms and can be paused by the selling party at any time.

> **NOTE**: Standard deals are also referred to as endeavor deals in function calls.

## Standard deal query

A standard deal is an agreement that grants you access to a specific segment of a publisher's inventory. This access may be offered at a distinct priority level, with a different price floor, or include publisher-provided audience segments, providing differentiated value in terms of inventory availability. To view the terms of a standard deal, query for the `targetableDeals` object with the corresponding deal ID.

The following `partner` query example is shortened due to the range of possible terms.

```
query GetPartnerEndeavorTermsExample {
  partner(id: "PARTNER_ID_PLACEHOLDER") {
    targetableDeals(where: {
      id: {
        eq: "ENDEAVOR_DEAL_ID_PLACEHOLDER"
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
        isDefaultOn
        isPrioritized
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

## Standard deal mutations

The following table lists all the following tasks you can do to standard deals.

| Task | Mutation |
| --- | --- |
| Add a new note for the specified standard deal and revision. | `inventoryEndeavorNoteCreate` |
| Update the standard deal name or display name. | `inventoryEndeavorUpdate` |
| Archive one or more standard deals. | `inventoryEndeavorsArchive` |
| Unarchive one or more standard deals. | `inventoryEndeavorsUnarchive` |

## Add a note to a standard deal

To add a note to a standard deal, use the `inventoryEndeavorNoteCreate` mutation and put your message in the `note` field.

The following `inventoryEndeavorNoteCreate` mutation example shows how to add a note.

```
mutation {
  inventoryEndeavorNoteCreate(input: {
    endeavorId: "ENDEAVOR_DEAL_ID_PLACEHOLDER"
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

## Update a standard deal

To update a standard deal, use the `inventoryEndeavorUpdate` mutation and update the `name` or `displayName` fields.

The following `inventoryEndeavorUpdate` mutation example shows how to rename your deal.

```
mutation {
  inventoryEndeavorUpdate(input: {
    endeavorId: "ENDEAVOR_DEAL_ID_PLACEHOLDER"
    displayName: "DISPLAY_NAME_PLACEHOLDER"
    name: "NAME_PLACEHOLDER"
  }) {
    data { id }
  }
}
```

## Archive standard deals

 To archive a standard deal, use the `inventoryEndeavorsArchive` mutation. This mutation supports multiple standard deals.

```
mutation {
  inventoryEndeavorsArchive(input: {
    inventoryEndeavorRevisionsWithAssociatedEndeavors: [
      { endeavorId: "ENDEAVOR_DEAL_ID_PLACEHOLDER" }
    ]
  }) {
    data { id }
  }
}
```

## Unarchive standard deals

 To unarchive a standard deal, use the `inventoryEndeavorsUnarchive` mutation. This mutation supports multiple standard deals.

```
mutation {
  inventoryEndeavorsUnarchive(input: {
    inventoryEndeavorRevisionsWithTargetingAssociated: [
      { endeavorId: "ENDEAVOR_DEAL_ID_PLACEHOLDER" }
    ]
  }) {
    data { id }
  }
}
```
