# PUT /v3/dynamiccreativerule → dynamicCreativeRuleUpdate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/put-v3-dynamiccreativerule
- Retrieved: 2026-11-14
- Category: REST_API

---

# PUT /v3/dynamiccreativerule → dynamicCreativeRuleUpdate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `PUT /v3/dynamiccreativerule` |
| GraphQL operation | `dynamicCreativeRuleUpdate` |
| Input type | `DynamicCreativeRuleUpdateInput` |
| Output type | `DynamicCreativeRuleUpdatePayload` (`data: DynamicCreativeRuleREST`, `errors: [DynamicCreativeRuleUpdateMutationError!]`) |

## Input field mapping

Input type: `DynamicCreativeRuleUpdateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `DynamicCreativeRuleId` | `dynamicCreativeRuleId` | ID! | Required | N/A |
| `AdvertiserId` | `advertiserId` | ID | Optional | N/A |
| `Name` | `name` | String | Optional | N/A |
| `DataElementGroups` | `dataElementGroups` | [DataElementGroupRESTInput!] | Optional | Replaces all groups when specified |

## Output field mapping

Output type: `DynamicCreativeRuleREST` (returned as `data` on `DynamicCreativeRuleUpdatePayload`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `DynamicCreativeRuleId` | `dynamicCreativeRuleId` | ID! | Not nullable | N/A |
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
PUT /v3/dynamiccreativerule HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "DynamicCreativeRuleId": "dcr-abc",
  "Name": "Renamed rule"
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
  dynamicCreativeRuleUpdate(
    input: { dynamicCreativeRuleId: "dcr-abc", name: "Renamed rule" }
  ) {
    data {
      dynamicCreativeRuleId
      name
      advertiserId
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
