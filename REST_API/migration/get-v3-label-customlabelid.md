# GET /v3/label/{customLabelId} → Query.customLabel

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-label-customlabelid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/label/{customLabelId} → Query.customLabel

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/label/{customLabelId}` |
| GraphQL query | `Query.customLabel(id: ID!)` |
| Return type | `CustomLabel` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CustomLabelId` | `id` | ID! | Not nullable | N/A |
| `PartnerId` | `partner { id }` | Partner | Nullable | Nested partner relationship; no scalar `partnerId` on `CustomLabel`. |
| `LabelName` | `name` | String! | Not nullable | REST `LabelName` maps to GraphQL `name`. |

## Code examples

### REST example

```
GET /v3/label/{customLabelId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query CustomLabelById($id: ID!) {
  customLabel(id: $id) {
    id
    name
    partner {
      id
    }
  }
}
```
