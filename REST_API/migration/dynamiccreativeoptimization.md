# Dynamic creative optimization: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/dynamiccreativeoptimization-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Dynamic creative optimization: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/dynamiccreativerule/{dynamicCreativeRuleId}` | `Query.dynamicCreativeRule(id:)` | Fetch a single rule by ID |
| `POST /v3/dynamiccreativerule/query/advertiser` | `Advertiser.dynamicCreativeRules` | **Not currently available in GraphQL**—REST pagination/search/sort filters. |

## Shared nested types and enums

### DataElementGroup

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `GroupName` | `groupName` | String! | Not nullable | N/A |
| `OutputName` | `outputName` | String! | Not nullable | N/A |
| `FirstPartyDataIds` | `firstPartyDataIds` | [ID!]! | Not nullable | N/A |
| `ThirdPartyDataIds` | `thirdPartyDataIds` | [ID!]! | Not nullable | N/A |
