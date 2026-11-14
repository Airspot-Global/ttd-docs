# GET /v3/dynamiccreativerule/{dynamicCreativeRuleId} → Query.dynamicCreativeRule

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-dynamiccreativerule-dynamiccreativeruleid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/dynamiccreativerule/{dynamicCreativeRuleId} → Query.dynamicCreativeRule

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/dynamiccreativerule/{dynamicCreativeRuleId}` |
| GraphQL query | `Query.dynamicCreativeRule(id:)` |
| Return type | `DynamicCreativeRule` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `DynamicCreativeRuleId` | `id` | String! | Not nullable | Existing field on `DynamicCreativeRule`. |
| `Name` | `name` | String! | Not nullable | Existing field on `DynamicCreativeRule`. |
| `AdvertiserId` | `advertiser` | Advertiser | Nullable | Entity reference instead of flat `advertiserId`. |
| `DataElementGroups` | `dataElementGroups` | [DataElementGroup!]! | Not nullable | List of `DataElementGroup` output objects. |
| `DataElementGroups.GroupName` | `dataElementGroups { groupName }` | String! | Not nullable | Nested leaf. |
| `DataElementGroups.OutputName` | `dataElementGroups { outputName }` | String! | Not nullable | Nested leaf. |
| `DataElementGroups.FirstPartyDataIds` | `dataElementGroups { firstPartyDataIds }` | [ID!]! | Not nullable | N/A |
| `DataElementGroups.ThirdPartyDataIds` | `dataElementGroups { thirdPartyDataIds }` | [ID!]! | Not nullable | N/A |

## Endpoint-specific nested types and enums

### DataElementGroup

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `GroupName` | `groupName` | String! | Not nullable | N/A |
| `OutputName` | `outputName` | String! | Not nullable | N/A |
| `FirstPartyDataIds` | `firstPartyDataIds` | [ID!]! | Not nullable | N/A |
| `ThirdPartyDataIds` | `thirdPartyDataIds` | [ID!]! | Not nullable | N/A |

## Code examples

### REST example

```
GET /v3/dynamiccreativerule/{dynamicCreativeRuleId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query DynamicCreativeRuleById {
  dynamicCreativeRule(id: "<DYNAMIC_CREATIVE_RULE_ID>") {
    id
    name
    advertiser {
      id
    }
    dataElementGroups {
      groupName
      outputName
      firstPartyDataIds
      thirdPartyDataIds
    }
  }
}
```
