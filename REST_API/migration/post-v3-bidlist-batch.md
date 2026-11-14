# POST /v3/bidlist/batch → bidListCreate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-bidlist-batch
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/bidlist/batch → bidListCreate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/bidlist/batch` |
| GraphQL operation | `bidListCreate` |
| Input type | `BidListCreateInput` |
| Output type | `PayloadWithErrorsOfIBidList` (`data: IBidList`, `userErrors: [UserError!]!`) |

## Multi-step operations

REST accepts an array of bid lists in one request. GraphQL has no batch-create mutation—issue one `bidListCreate` call per array element. The REST batch endpoint is deprecated in favor of `bidListCreate`.

## Input field mapping

Input type: `BidListCreateInput` (one call per REST array element)

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `Name` | `name` | String! | Required | N/A |
| `BidListAdjustmentType` | `adjustmentType` | BidListAdjustmentType! | Required | N/A |
| `ResolutionType` | `resolutionType` | MultipleMatchResolutionType! | Required | N/A |
| `BidLines` | `bidLines` | [BidLineCreateInput!]! | Required | N/A |
| `IsAvailableForLibraryUse` | `isAvailableForLibraryUse` | Boolean! | Required | N/A |
| `BidListOwner` | `owner` | BidListOwnerInput! | Required | REST pairs BidListOwner enum with BidListOwnerId; GraphQL uses BidListOwnerInput (set one of `partnerId`, `advertiserId`, `campaignId`, `adGroupId`, or `isGlobal`) |
| N/A | `dimensions` | [BidListDimension!]! | Required | GraphQL-only required field; infer from bid line dimensions in REST payload |
| `BidListSource` | `source` | BidListSource! | Required | Optional on REST create; required on GraphQL—pass `USER` for API-created lists |
| N/A | `associateBehavior` | BidListAssociateBehavior! | Required | GraphQL-only required field; controls association on creation: `DO_NOT_ASSOCIATE`, `ASSOCIATE`, `ASSOCIATE_AND_ENABLE` |

Bid line fields map to `BidLineCreateInput`; see the BidList domain page for the full nested field table.

## Output field mapping

Output type: `IBidList` (returned as `data` on `PayloadWithErrorsOfIBidList`)

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
POST /v3/bidlist/batch HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

[
  {
    "Name": "Site Target List",
    "BidListAdjustmentType": "Optimized",
    "BidListOwner": "Advertiser",
    "BidListOwnerId": "adv123",
    "BidLines": [
      {
        "DomainFragment": "example.com",
        "BidAdjustment": 1.0,
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
  bidListCreate(input: {
    name: "Site Target List"
    adjustmentType: OPTIMIZED
    resolutionType: APPLY_MULTIPLY_ADJUSTMENT
    source: USER
    dimensions: [HAS_DOMAIN_FRAGMENT_ID]
    isAvailableForLibraryUse: false
    owner: { advertiserId: "adv123" }
    associateBehavior: ASSOCIATE
    bidLines: [
      { domainFragment: "example.com", bidAdjustment: 1.0, volumeControlPriority: NEUTRAL }
    ]
  }) {
    data { id name adjustmentType }
    userErrors { message field }
  }
}
```
