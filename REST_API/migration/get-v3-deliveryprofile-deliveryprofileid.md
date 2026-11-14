# GET /v3/deliveryProfile/{deliveryProfileId} → Query.deliveryProfile(id:)

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-deliveryprofile-deliveryprofileid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/deliveryProfile/{deliveryProfileId} → Query.deliveryProfile(id:)

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/deliveryProfile/{deliveryProfileId}` |
| GraphQL query | `Query.deliveryProfile(id: ID!)` |
| Return type | `DeliveryProfile` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `DeliveryProfileId` | `id` | ID! | Not nullable | Available on the existing `DeliveryProfile` type. |
| `OwnerPartnerId` | `ownerPartner.id` | ID! | Not nullable | Partner relationship on `DeliveryProfile`; select `ownerPartner { id }`. |
| `Name` | `name` | String! | Not nullable | Available on the existing `DeliveryProfile` type. |
| `Description` | `description` | String | Nullable | N/A |
| `Permissions` | `permissions` | DeliveryProfilePermissions | Nullable | Nested object—see DeliveryProfilePermissions below. |
| `Permissions.PartnerIdsAllowedToBuy` | `permissions.partnerIdsAllowedToBuy` | [ID!]! | Not nullable | N/A |
| `Permissions.AdvertiserIdsAllowedToBuy` | `permissions.advertiserIdsAllowedToBuy` | [ID!]! | Not nullable | N/A |
| `Permissions.AdvertiserIdsForbiddenToBuy` | `permissions.advertiserIdsForbiddenToBuy` | [ID!]! | Not nullable | N/A |

## Endpoint-specific nested types and enums

### DeliveryProfilePermissions

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `PartnerIdsAllowedToBuy` | `partnerIdsAllowedToBuy` | [ID!]! | Not nullable | N/A |
| `AdvertiserIdsAllowedToBuy` | `advertiserIdsAllowedToBuy` | [ID!]! | Not nullable | N/A |
| `AdvertiserIdsForbiddenToBuy` | `advertiserIdsForbiddenToBuy` | [ID!]! | Not nullable | N/A |

## Code examples

### REST example

```
GET /v3/deliveryProfile/{deliveryProfileId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetDeliveryProfile($id: ID!) {
  deliveryProfile(id: $id) {
    id
    name
    ownerPartner {
      id
    }
    isAllAllowedToBuy
    description
    permissions {
      partnerIdsAllowedToBuy
      advertiserIdsAllowedToBuy
      advertiserIdsForbiddenToBuy
    }
  }
}
```
