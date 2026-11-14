# GET /v3/audience/name/{audienceId} → Query.audience

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-audience-name-audienceid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/audience/name/{audienceId} → Query.audience

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/audience/name/{audienceId}` |
| GraphQL query | `Query.audience(id: ID!)` |
| Return type | `Audience` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Id` | `id` | ID! | Not nullable | N/A |
| `Name` | `name` | String! | Not nullable | N/A |

## Code examples

### REST example

```
GET /v3/audience/name/{audienceId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query AudienceName {
  audience(id: "<audience-id>") {
    id
    name
  }
}
```
