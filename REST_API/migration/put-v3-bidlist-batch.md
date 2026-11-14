# PUT /v3/bidlist/batch → bidListSetBatch

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/put-v3-bidlist-batch
- Retrieved: 2026-11-14
- Category: REST_API

---

# PUT /v3/bidlist/batch → bidListSetBatch

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `PUT /v3/bidlist/batch` |
| GraphQL operation | `bidListSetBatch` |
| Input type | `BidListSetInput` |
| Output type | `PayloadWithErrorsOfListOfBidList` (`data: [IBidList]`, `userErrors: [UserError!]!`) |

## Input field mapping

Input type: `BidListSetInput` (one element per REST array item, passed as `input` on `bidListSetBatch`)

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `BidListId` | `id` | ID! | Required | N/A |
| `Name` | `name` | String | Optional | N/A |
| `BidLines` | `bidLines` | [BidLineCreateInput!] | Optional | N/A |
| BidListOwner + BidListOwnerId | `newOwner` | BidListOwnerUpdateInput | Optional | Owner transfer only—supports `advertiserId`, `campaignId`, or `partnerId`; new owner must be an ancestor |
| `BidListSource` | N/A | N/A | Optional | **Read-only** |
| `BidListAdjustmentType` | N/A | N/A | Optional | **Read-only** |
| `ResolutionType` | N/A | N/A | Optional | **Read-only** |
| `IsAvailableForLibraryUse` | N/A | N/A | Optional | **Read-only** |

Bid line fields map to `BidLineCreateInput`; see the BidList domain page for the full nested field table.

## Output field mapping

Output type: `[IBidList]` (returned as `data` on `PayloadWithErrorsOfListOfBidList`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `BidListId` | `id` | ID! | Not nullable | N/A |
| `Name` | `name` | String! | Not nullable | N/A |
| `BidListSource` | `source` | BidListSource! | Not nullable | N/A |
| `BidListAdjustmentType` | `adjustmentType` | BidListAdjustmentType! | Not nullable | N/A |
| `ResolutionType` | `resolutionType` | MultipleMatchResolutionType! | Not nullable | N/A |
| `BidLines` | `bidLines` | [BidLine!]! | Not nullable | See BidList domain page for BidLine (response) nested mapping |
| `IsAvailableForLibraryUse` | `isAvailableForLibraryUse` | Boolean! | Not nullable | N/A |
| `IsGlobal` | `ownerType` | BidListOwnerType! | Not nullable | N/A |
| `BidListDimensions` | `dimensions` | [BidListDimension!]! | Not nullable | N/A |
| `BidListType` | N/A | N/A | N/A | **Read-only** |
| `BidListOwner` | `ownerType` | BidListOwnerType! | Not nullable | N/A |
| `BidListOwnerId` | `owner` | BidListOwner | Nullable | Nested owner entity (`BidListOwner` union) |

## Code examples

### REST example

```
PUT /v3/bidlist/batch HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

[
  {
    "BidListId": "bl_111",
    "BidLines": [
      {
        "DomainFragment": "site-a.com",
        "BidAdjustment": 1.2,
        "VolumeControlPriority": "Neutral"
      }
    ]
  }
]
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation {
  bidListSetBatch(input: [
    {
      id: "bl_111"
      bidLines: [
        { domainFragment: "site-a.com", bidAdjustment: 1.2, volumeControlPriority: NEUTRAL }
      ]
    }
    {
      id: "bl_222"
      bidLines: [
        { domainFragment: "site-b.com", bidAdjustment: 0.9, volumeControlPriority: NEUTRAL }
      ]
    }
  ]) {
    data { id name }
    userErrors { message field }
  }
}
```
