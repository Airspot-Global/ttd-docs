# GET /v3/partner/name/{partnerId} → Query.partnerBasicInfo

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-partner-name-partnerid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/partner/name/{partnerId} → Query.partnerBasicInfo

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/partner/name/{partnerId}` |
| GraphQL query | `Query.partnerBasicInfo(ids:)` |
| Return type | `[PartnerBasicInfo!]!` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Id` | `id` | ID! | Not nullable | On `PartnerBasicInfo` (or `Partner.id` via `Query.partner`). |
| `Name` | `name` | String! | Not nullable | On `PartnerBasicInfo` (or `Partner.name` via `Query.partner`). |

## Code examples

### REST example

```
GET /v3/partner/name/{partnerId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetPartnerName($id: ID!) {
  partnerBasicInfo(ids: [$id]) {
    id
    name
  }
}
```
