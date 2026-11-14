# GET /v3/inventoryclassification/name/{domainClassId} → Query.domainClass

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-inventoryclassification-name-domainclassid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/inventoryclassification/name/{domainClassId} → Query.domainClass

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/inventoryclassification/name/{domainClassId}` |
| GraphQL query | `Query.domainClass(id:)` |
| Return type | `DomainClass` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| domainClassId (path) | `id` on `Query.domainClass` | `ID!` | Required | REST path parameter maps to required GraphQL argument. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Id` | `id` | `ID!` | Not nullable | Path parameter `domainClassId` echoed in the response. |
| `Name` | `name` | `String` | Nullable | Display name. Shared with the `domainClasses` collection query. Nullable in schema; populated by the GET-by-ID resolver. |

## Code examples

### REST example

```
GET /v3/inventoryclassification/name/42 HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetDomainClass {
  domainClass(id: "42") {
    id
    name
  }
}
```
