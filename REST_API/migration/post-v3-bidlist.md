# POST /v3/bidlist → bidListCreate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-bidlist
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/bidlist → bidListCreate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/bidlist` |
| GraphQL operation | `bidListCreate` |
| Input type | `BidListCreateInput` |
| Output type | `PayloadWithErrorsOfIBidList` (`data: IBidList`, `userErrors: [UserError!]!`) |

## Input field mapping

Input type: `BidListCreateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `BidListId` | N/A | N/A | Optional | InvalidOnCreate; omit on create |
| `Name` | `name` | String! | Required | Max 512 chars |
| `BidListSource` | `source` | BidListSource! | Required | REST marks InvalidOnCreate; GraphQL requires `source` on create—pass `USER` for API-created lists |
| `BidListAdjustmentType` | `adjustmentType` | BidListAdjustmentType! | Required | Immutable after creation |
| `ResolutionType` | `resolutionType` | MultipleMatchResolutionType! | Required | Required in GraphQL; defaults to APPLY_MULTIPLY_ADJUSTMENT in REST |
| BidListOwner + BidListOwnerId | `owner` | BidListOwnerInput! | Required | Two flat fields become one object; see BidList domain page |
| `IsAvailableForLibraryUse` | `isAvailableForLibraryUse` | Boolean! | Required | Required in GraphQL; pass false if not used |
| `BidLines` | `bidLines` | [BidLineCreateInput!] | Optional | See BidList domain page for BidLineCreateInput nested mapping |

### GraphQL-only input fields (no REST equivalent)

| GraphQL field | GraphQL type | Description |
| --- | --- | --- |
| `associateBehavior` | BidListAssociateBehavior! | DO_NOT_ASSOCIATE, ASSOCIATE, ASSOCIATE_AND_ENABLE |
| `dimensions` | [BidListDimension!]! |  |

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

Simple bid list create with ad group owner and site/app targeting.

### REST example

```
POST /v3/bidlist HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "Name": "Site/App Target List",
  "BidListAdjustmentType": "Adjustment",
  "BidListOwner": "AdGroup",
  "BidListOwnerId": "ag1234567",
  "IsAvailableForLibraryUse": false,
  "BidLines": [
    {
      "BidAdjustment": 1.5,
      "DomainFragment": "example.com",
      "VolumeControlPriority": "None"
    }
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
mutation CreateSiteTargetBidList {
  bidListCreate(input: {
    name: "Site/App Target List"
    adjustmentType: OPTIMIZED
    resolutionType: APPLY_MULTIPLY_ADJUSTMENT
    source: USER
    owner: { adGroupId: "ag1234567" }
    associateBehavior: ASSOCIATE_AND_ENABLE
    dimensions: [HAS_DOMAIN_FRAGMENT_ID]
    isAvailableForLibraryUse: false
    bidLines: [
      {
        bidAdjustment: 1.5
        domainFragment: "example.com"
        volumeControlPriority: NEUTRAL
      }
    ]
  }) {
    data {
      id
      name
      adjustmentType
    }
    userErrors {
      message
      field
    }
  }
}
```

Create a global bid list owned at the global level.

### REST example

```
POST /v3/bidlist HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "Name": "Global Exclusion List",
  "BidListAdjustmentType": "Block",
  "BidListOwner": "Global",
  "IsAvailableForLibraryUse": true,
  "BidLines": [
    {
      "BidAdjustment": 0.0,
      "DomainFragment": "blockedsite.com",
      "VolumeControlPriority": "None"
    }
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
mutation CreateGlobalBidList {
  bidListCreate(input: {
    name: "Global Exclusion List"
    adjustmentType: EXCLUSION
    resolutionType: APPLY_MULTIPLY_ADJUSTMENT
    source: USER
    owner: { isGlobal: true }
    associateBehavior: DO_NOT_ASSOCIATE
    dimensions: [HAS_DOMAIN_FRAGMENT_ID]
    isAvailableForLibraryUse: true
    bidLines: [
      {
        bidAdjustment: 0.0
        domainFragment: "blockedsite.com"
        volumeControlPriority: NEUTRAL
      }
    ]
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
