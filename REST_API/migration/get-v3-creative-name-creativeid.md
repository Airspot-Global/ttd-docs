# GET /v3/creative/name/{creativeId} → Creative

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-creative-name-creativeid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/creative/name/{creativeId} → Creative

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/creative/name/{creativeId}` |
| GraphQL query | `Creative` (via entity lookup by `id`) |
| Return type | `Creative` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Id` | `id` | ID! | Not nullable | Query `Creative` by ID. |
| `Name` | `name` | String | Nullable | Available on `Creative`. |

## Code examples

### REST example

```
GET /v3/creative/name/{creativeId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetCreativeName($id: ID!) {
  creative(id: $id) {
    id
    name
  }
}
```
