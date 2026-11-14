# GET /v3/deliveryprofile/name/{deliveryProfileId} → Query.deliveryProfile(id:)

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-deliveryprofile-name-deliveryprofileid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/deliveryprofile/name/{deliveryProfileId} → Query.deliveryProfile(id:)

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/deliveryprofile/name/{deliveryProfileId}` |
| GraphQL query | `Query.deliveryProfile(id: ID!)` |
| Return type | `DeliveryProfile` |

## Response field mapping

REST `IdName` payload (`Id` / `Name`—not `DeliveryProfileId`). No additional GraphQL fields beyond `DeliveryProfile.id` / `DeliveryProfile.name`.

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Id` | `id` | ID! | Not nullable | Query `DeliveryProfile` by ID. |
| `Name` | `name` | String! | Not nullable | Available on `DeliveryProfile`. |

## Code examples

### REST example

```
GET /v3/deliveryprofile/name/{deliveryProfileId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetDeliveryProfileName($id: ID!) {
  deliveryProfile(id: $id) {
    id
    name
  }
}
```
