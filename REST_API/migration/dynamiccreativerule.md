# DynamicCreativeRule: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/dynamiccreativerule-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# DynamicCreativeRule: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| POST `/v3/dynamiccreativerule` | `dynamicCreativeRuleCreate` | Requires advertiser, name, and data element groups |
| PUT `/v3/dynamiccreativerule` | `dynamicCreativeRuleUpdate` | Requires rule ID; other fields optional |

## Shared nested types and enums

### DataElementGroupRESTInput

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `GroupName` | `groupName` | String! | Required | N/A |
| `OutputName` | `outputName` | String! | Required | N/A |
| `FirstPartyDataIds` | `firstPartyDataIds` | [ID!] | Optional | N/A |
| `ThirdPartyDataIds` | `thirdPartyDataIds` | [ID!] | Optional | N/A |
