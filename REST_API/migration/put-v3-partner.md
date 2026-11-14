# PUT /v3/partner → partnerUpdate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/put-v3-partner
- Retrieved: 2026-11-14
- Category: REST_API

---

# PUT /v3/partner → partnerUpdate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `PUT /v3/partner` |
| GraphQL operation | `partnerUpdate` |
| Input type | `PartnerUpdateInput` |
| Output type | `PartnerUpdatePayload` (`data: Partner`, `errors: [PartnerUpdateMutationError!]`) |

## Multi-step operations

| REST behavior | GraphQL target |
| --- | --- |
| `AssociatedBidLists` on partner update | `partnerAssociateBidList`—not on `PartnerUpdateInput`; associate, enable, or remove bid lists via `PartnerAssociateBidListInput.bidListsToAddOrUpdate` and `bidListIdsToRemove` |
| `Increments` on partner update | Not currently available in GraphQL |
| `NewFrequencyConfigs` on partner update | Not currently available in GraphQL |

## Input field mapping

Input type: `PartnerUpdateInput` (plus `partnerAssociateBidList` where noted)

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PartnerId` | `id` | `String!` | Required | Entity ID on the REST body maps to `partnerUpdate.input.id`. |
| `AssociatedBidLists` | `partnerAssociateBidList` | `PayloadWithErrorsOfPartner!` | Optional | Not on `PartnerUpdateInput`. Use `Mutation.partnerAssociateBidList` with `bidListsToAddOrUpdate` and `bidListIdsToRemove` to associate, enable, or remove bid lists. |
| `AssociatedBidLists[].BidListId` | `bidListsToAddOrUpdate[].bidListId` | `ID!` | Required | Via `partnerAssociateBidList.input.bidListsToAddOrUpdate[].bidListId`. |
| `AssociatedBidLists[].IsEnabled` | `bidListsToAddOrUpdate[].isEnabled` | `Boolean` | Required | Via `partnerAssociateBidList.input.bidListsToAddOrUpdate[].isEnabled`. |
| `AssociatedBidLists[].IsDefaultForDimension` | N/A | N/A | Required | Not currently available in GraphQL |
| `AssociatedBidLists[].BidListAdjustmentType` | N/A | N/A | Optional | InvalidOnUpdate on REST—set at bid-list creation; no effect on partner PUT. |
| `AssociatedBidLists[].BidListDimensions` | N/A | N/A | Optional | InvalidOnUpdate on REST—read-only on PUT; no effect on update. |
| `AssociatedBidLists[].BidListSource` | N/A | N/A | Optional | InvalidOnUpdate on REST—read-only on PUT; no effect on update. |
| `Increments` | N/A | N/A | Optional | Not currently available in GraphQL |
| `NewFrequencyConfigs` | N/A | N/A | Optional | Not currently available in GraphQL |
| `NewFrequencyConfigs[].CounterId` | N/A | N/A | Optional | Not currently available in GraphQL |
| `NewFrequencyConfigs[].CounterName` | N/A | N/A | Optional | Not currently available in GraphQL |
| `NewFrequencyConfigs[].FrequencyCap` | N/A | N/A | Optional | Not currently available in GraphQL |
| `NewFrequencyConfigs[].FrequencyGoal` | N/A | N/A | Optional | Not currently available in GraphQL |
| `NewFrequencyConfigs[].ResetIntervalInMinutes` | N/A | N/A | Required | Not currently available in GraphQL |
| `NewFrequencyConfigs[].OwnedByPartner` | N/A | N/A | Optional | Accepted on REST but ignored on Partner PUT—no GraphQL mapping needed. |
| `PartnerIdInteger` | N/A | N/A | Optional | Read-only on the REST PUT body—no effect on update; readable as `Partner.idInteger` on the response. |
| `PartnerName` | `name` | `String` | Optional | REST marks `PartnerName` read-only on the PUT body, but GraphQL is more capable: `PartnerUpdateInput.name` accepts a new name—use `partnerUpdate` to rename a partner where REST would not. |

## Output field mapping

Output type: `Partner` (returned as `data` on `PartnerUpdatePayload`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AssociatedBidLists` | `associatedBidLists` | `AssociatedBidListsConnection` | Nullable | N/A |
| `AssociatedBidLists[].BidListId` | `associatedBidLists.nodes[].bidList.id` | `ID!` | Not nullable | Via nested `bidList` on `AssociatedBidList`. |
| `AssociatedBidLists[].IsEnabled` | `associatedBidLists.nodes[].isEnabled` | `Boolean!` | Not nullable | N/A |
| `AssociatedBidLists[].IsDefaultForDimension` | N/A | N/A | Nullable | Not currently available in GraphQL |
| `AssociatedBidLists[].BidListAdjustmentType` | `associatedBidLists.nodes[].bidList.adjustmentType` | `BidListAdjustmentType!` | Not nullable | N/A |
| `AssociatedBidLists[].BidListDimensions` | `associatedBidLists.nodes[].bidList.dimensions` | `[BidListDimension!]!` | Not nullable | N/A |
| `AssociatedBidLists[].BidListSource` | `associatedBidLists.nodes[].bidList.source` | `BidListSource!` | Not nullable | N/A |
| `Increments` | `increments` | `[String!]!` | Not nullable | N/A |
| `NewFrequencyConfigs` | N/A | N/A | Nullable | Not currently available in GraphQL |
| `PartnerId` | `id` | `ID!` | Not nullable | N/A |
| `PartnerIdInteger` | `idInteger` | `Int!` | Not nullable | N/A |
| `PartnerName` | `name` | `String!` | Not nullable | N/A |

## Code examples

### REST example—update partner ID and name

```
PUT /v3/partner HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "PartnerId": "abc123",
  "PartnerName": "Updated Partner Name"
}
```

### GraphQL example—update partner ID and name

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation {
  partnerUpdate(input: { id: "abc123", name: "Updated Partner Name" }) {
    data {
      id
      idInteger
      name
    }
    errors {
      ... on PartnerValidationError {
        message
        field
      }
    }
  }
}
```

### REST example—associate and enable a bid list

REST `PUT /v3/partner` accepts `AssociatedBidLists` on the same body. In GraphQL, call `partnerAssociateBidList` separately:

```
PUT /v3/partner HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "PartnerId": "abc123",
  "AssociatedBidLists": [
    {
      "BidListId": "bl456",
      "IsEnabled": true,
      "IsDefaultForDimension": false
    }
  ]
}
```

### GraphQL example—associate and enable a bid list

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation {
  partnerAssociateBidList(
    input: {
      partnerId: "abc123"
      bidListsToAddOrUpdate: [{ bidListId: "bl456", isEnabled: true }]
    }
  ) {
    data {
      id
      associatedBidLists {
        nodes {
          isEnabled
          bidList { id adjustmentType source }
        }
      }
    }
    userErrors {
      message
      field
    }
  }
}
```

### GraphQL example—read increments on the updated partner

Increments cannot be written via GraphQL today, but the current value is readable on the returned `Partner`:

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation {
  partnerUpdate(input: { id: "abc123" }) {
    data {
      id
      increments
    }
    errors {
      ... on PartnerValidationError {
        message
        field
      }
    }
  }
}
```
