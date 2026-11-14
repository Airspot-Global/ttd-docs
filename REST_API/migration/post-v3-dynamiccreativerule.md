# POST /v3/dynamiccreativerule → dynamicCreativeRuleCreate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-dynamiccreativerule
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/dynamiccreativerule → dynamicCreativeRuleCreate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/dynamiccreativerule` |
| GraphQL operation | `dynamicCreativeRuleCreate` |
| Input type | `DynamicCreativeRuleCreateInput` |
| Output type | `DynamicCreativeRuleCreatePayload` (`data: DynamicCreativeRuleREST`, `errors: [DynamicCreativeRuleCreateMutationError!]`) |

## Input field mapping

Input type: `DynamicCreativeRuleCreateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `DynamicCreativeRuleId` | `dynamicCreativeRuleId` | ID | Optional | Ignored on create; returned on success |
| `AdvertiserId` | `advertiserId` | ID! | Required | N/A |
| `Name` | `name` | String! | Required | Max 128 chars enforced by REST |
| `DataElementGroups` | `dataElementGroups` | [DataElementGroupRESTInput!]! | Required | See DataElementGroupRESTInput on the DynamicCreativeRule domain page |

## Output field mapping

Output type: `DynamicCreativeRuleREST` (returned as `data` on `DynamicCreativeRuleCreatePayload`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `DynamicCreativeRuleId` | `dynamicCreativeRuleId` | ID! | Not nullable | Server-generated on create |
| `AdvertiserId` | `advertiserId` | ID! | Not nullable | N/A |
| `Name` | `name` | String! | Not nullable | N/A |
| `DataElementGroups` | `dataElementGroups` | [DataElementGroupREST!]! | Not nullable | See DataElementGroupREST below |

## Endpoint-specific nested types and enums

### DataElementGroupREST

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `GroupName` | `groupName` | String! | Not nullable | N/A |
| `OutputName` | `outputName` | String! | Not nullable | N/A |
| `FirstPartyDataIds` | `firstPartyDataIds` | [ID!] | Nullable | N/A |
| `ThirdPartyDataIds` | `thirdPartyDataIds` | [ID!] | Nullable | N/A |

## Code examples

### REST example

```
POST /v3/dynamiccreativerule HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserId": "adv123",
  "Name": "My DCR",
  "DataElementGroups": [
    {
      "GroupName": "sports",
      "OutputName": "SPORTS_MACRO",
      "FirstPartyDataIds": [1, 2]
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
mutation {
  dynamicCreativeRuleCreate(
    input: {
      advertiserId: "adv123"
      name: "My DCR"
      dataElementGroups: [
        {
          groupName: "sports"
          outputName: "SPORTS_MACRO"
          firstPartyDataIds: ["1", "2"]
        }
      ]
    }
  ) {
    data {
      dynamicCreativeRuleId
      advertiserId
      name
      dataElementGroups {
        groupName
        outputName
        firstPartyDataIds
        thirdPartyDataIds
      }
    }
    errors {
      ... on RestProxyMutationError {
        message
        field
      }
    }
  }
}
```
