# Programmatic guaranteed deals

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/deals/doc/PlatformDealPG
- Retrieved: 2026-11-14
- Category: Guides

---

# Programmatic guaranteed deals

Programmatic guaranteed (PG) deals use a fixed-price auction system to give buyers exclusive inventory and pricing in exchange for committing to a media spend goal.

## PG deal query

A PG deal is an agreement that grants you access to a specific segment of a publisher's inventory. This access is exclusive to the buyer and comes with additional conditions such as meeting bid rate percentages and media spend goals.

To view the terms of a PG deal, filter for the `isProgrammaticGuaranteed` field in the `targetableDeals` query. The following `partner` example lists all terms in a PG deal.

```
query GetPartnerProgrammaticGuaranteedTermsExample {
  partner(id: "PARTNER_ID_PLACEHOLDER") {
    targetableDeals(where: {
      isProgrammaticGuaranteed: { eq: true }
    }) {
      nodes {
        id
        dealType
        ... on InventoryCommitment {
          isProgrammaticGuaranteed
        }
      }
    }
  }
}
```

## Mutations

The following table lists all the tasks you perform with PG deals.

> **NOTE**: PG deals share the same mutations as commitment deals, but do not have expansion or cancellation.

| Task | Mutation |
| --- | --- |
| Add a new note for the specified standard deal and revision. | `inventoryCommitmentNoteCreate` |
| Update the standard deal name or display name. | `inventoryCommitmentUpdate` |
| Archive one or more standard deals. | `inventoryCommitmentArchive` |
| Unarchive one or more standard deals. | `inventoryCommitmentUnarchive` |

For details, see Commitment deals.
