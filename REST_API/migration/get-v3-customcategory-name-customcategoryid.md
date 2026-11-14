# GET /v3/customcategory/name/{customCategoryId} → Query.customCategory(id:)

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-customcategory-name-customcategoryid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/customcategory/name/{customCategoryId} → Query.customCategory(id:)

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/customcategory/name/{customCategoryId}` |
| GraphQL query | `Query.customCategory(id:)` |
| Return type | `CustomCategory` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Id` | `id` | ID! | Not nullable | On parent `CustomCategory`; no separate ID/name payload type. |
| `Name` | `customCategoryName` | String | Nullable | Use the `customCategoryName` field on `Query.customCategory(id:)` instead of a dedicated name endpoint. |

## Code examples

### REST example

```
GET /v3/customcategory/name/{customCategoryId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query CustomCategoryName($id: ID!) {
  customCategory(id: $id) {
    id
    customCategoryName
  }
}
```
