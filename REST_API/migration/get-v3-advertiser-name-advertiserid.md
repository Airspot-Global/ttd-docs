# GET /v3/advertiser/name/{advertiserId} → Advertiser.id / Advertiser.name

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-advertiser-name-advertiserid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/advertiser/name/{advertiserId} → Advertiser.id / Advertiser.name

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/advertiser/name/{advertiserId}` |
| GraphQL query | `Advertiser.id` / `Advertiser.name` |
| Return type | `Advertiser` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Id` | `id` | ID! | Not nullable | N/A |
| `Name` | `name` | String! | Not nullable | N/A |

## Code examples

### REST example

```
GET /v3/advertiser/name/{advertiserId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query AdvertiserName {
  advertiser(id: "abc123") {
    id
    name
  }
}
```
