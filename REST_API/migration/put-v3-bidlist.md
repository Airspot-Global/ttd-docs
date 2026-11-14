# PUT /v3/bidlist → bidListSet / bidListUpdate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/put-v3-bidlist
- Retrieved: 2026-11-14
- Category: REST_API

---

# PUT /v3/bidlist → bidListSet / bidListUpdate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `PUT /v3/bidlist` |
| GraphQL operation | `bidListSet` (full replace) or `bidListUpdate` (partial) |
| Input type | `BidListSetInput` or `BidListUpdateInput` |
| Output type | `PayloadWithErrorsOfIBidList` (`data: IBidList`, `userErrors: [UserError!]!`) |

## Multi-step operations

REST `PUT /v3/bidlist` supported full bid line replacement and additive/subtractive line-level edits in a single request. GraphQL separates these into two mutations:

| REST behavior | GraphQL mutation | Input type |
| --- | --- | --- |
| Full replace of bid lines (REST PUT default) | `bidListSet` | `BidListSetInput` |
| Add or remove individual bid lines | `bidListUpdate` | `BidListUpdateInput` |

Fields not listed on `BidListSetInput` or `BidListUpdateInput` (for example `BidListSource`, `BidListAdjustmentType`, `ResolutionType`, `IsAvailableForLibraryUse`) are read-only or immutable after create.

## Input field mapping

### bidListSet (`BidListSetInput`)—full replace

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `BidListId` | `id` | ID! | Required | Required on update |
| `Name` | `name` | String | Optional | Omit to leave unchanged |
| `BidLines` | `bidLines` | [BidLineCreateInput!] | Optional | Full replacement; omit to leave unchanged; see BidList domain page for line fields |
| BidListOwner + BidListOwnerId | `newOwner` | BidListOwnerUpdateInput | Optional | Only `advertiserId`, `campaignId`, `partnerId`; new owner must be ancestor |

### bidListUpdate (`BidListUpdateInput`)—partial edit

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `BidListId` | `id` | ID! | Required | Required |
| `Name` | `name` | String | Optional | Omit to leave unchanged |
| BidLines (add) | `bidLinesToAdd` | [BidLineCreateInput!] | Optional | Lines to add; see BidList domain page for line fields |
| BidLines (remove) | `bidLinesToRemove` | [BidLineDeleteDimensionsInput!] | Optional | Provide dimension key fields to identify lines to remove |

## Output field mapping

Output type: `IBidList` (returned as `data` on `PayloadWithErrorsOfIBidList`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `BidListId` | `id` | ID! | Not nullable | N/A |
| `Name` | `name` | String! | Not nullable | N/A |
| `BidListSource` | `source` | BidListSource! | Not nullable | Read-only on response |
| `BidListAdjustmentType` | `adjustmentType` | BidListAdjustmentType! | Not nullable | N/A |
| `ResolutionType` | `resolutionType` | MultipleMatchResolutionType! | Not nullable | N/A |
| `BidLines` | `bidLines` | [BidLine!]! | Not nullable | See BidList domain page for BidLine (response) nested mapping |
| `IsAvailableForLibraryUse` | `isAvailableForLibraryUse` | Boolean! | Not nullable | N/A |
| `IsGlobal` | `ownerType` | BidListOwnerType! | Not nullable | `GLOBAL` when REST `IsGlobal` is true |
| `BidListDimensions` | `dimensions` | [BidListDimension!]! | Not nullable | N/A |
| `BidListType` | N/A | N/A | N/A | **Read-only** |
| `BidListOwner` | `ownerType` | BidListOwnerType! | Not nullable | N/A |
| `BidListOwnerId` | `owner` | BidListOwner | Nullable | Nested owner entity (`BidListOwner` union) |

## Code examples

Full replace of bid lines using `bidListSet` (REST PUT equivalent).

### REST example

```
PUT /v3/bidlist HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "BidListId": "bl_abc123",
  "Name": "Updated Site List",
  "BidLines": [
    { "BidAdjustment": 2.0, "DomainFragment": "newsite.com", "VolumeControlPriority": "None" },
    { "BidAdjustment": 1.5, "DomainFragment": "anothernewsite.com", "VolumeControlPriority": "None" }
  ]
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation ReplaceBidListLines {
  bidListSet(input: {
    id: "bl_abc123"
    name: "Updated Site List"
    bidLines: [
      { bidAdjustment: 2.0, domainFragment: "newsite.com", volumeControlPriority: NEUTRAL }
      { bidAdjustment: 1.5, domainFragment: "anothernewsite.com", volumeControlPriority: NEUTRAL }
    ]
  }) {
    data {
      id
      name
      bidLines {
        bidAdjustment
        domainFragment
      }
    }
    userErrors {
      message
      field
    }
  }
}
```

Partial update to add bid lines using `bidListUpdate`.

### REST example

```
PUT /v3/bidlist HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "BidListId": "bl_abc123",
  "BidLines": [
    { "BidAdjustment": 1.3, "DomainFragment": "addedsite.com", "VolumeControlPriority": "None" }
  ]
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation AddBidLines {
  bidListUpdate(input: {
    id: "bl_abc123"
    bidLinesToAdd: [
      { bidAdjustment: 1.3, domainFragment: "addedsite.com", volumeControlPriority: NEUTRAL }
    ]
  }) {
    data {
      id
      bidLines {
        bidAdjustment
        domainFragment
      }
    }
    userErrors {
      message
      field
    }
  }
}
```

Partial update to remove bid lines using `bidListUpdate`.

### REST example

```
PUT /v3/bidlist HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "BidListId": "bl_abc123",
  "BidLines": []
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation RemoveBidLines {
  bidListUpdate(input: {
    id: "bl_abc123"
    bidLinesToRemove: [
      { domainFragment: "oldsite.com" }
    ]
  }) {
    data {
      id
      bidLines {
        bidAdjustment
        domainFragment
      }
    }
    userErrors {
      message
      field
    }
  }
}
```

Transfer ownership to a parent advertiser using `bidListSet`.

### REST example

```
PUT /v3/bidlist HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "BidListId": "bl_abc123",
  "BidListOwner": "Advertiser",
  "BidListOwnerId": "adv456"
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation TransferBidListOwnership {
  bidListSet(input: {
    id: "bl_abc123"
    newOwner: { advertiserId: "adv456" }
  }) {
    data {
      id
      name
    }
    userErrors {
      message
      field
    }
  }
}
```
