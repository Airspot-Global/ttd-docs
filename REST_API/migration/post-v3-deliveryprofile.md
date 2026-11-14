# POST /v3/deliveryProfile → deliveryProfileCreate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-deliveryprofile
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/deliveryProfile → deliveryProfileCreate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/deliveryProfile` |
| GraphQL operation | `deliveryProfileCreate` |
| Input type | `DeliveryProfileCreateInput` |
| Output type | `DeliveryProfileCreatePayload` (`data: DeliveryProfileREST`, `errors: [DeliveryProfileCreateMutationError!]` / `RestProxyMutationError`) |

## Input field mapping

Input type: `DeliveryProfileCreateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `DeliveryProfileId` | N/A | N/A | Optional | Invalid on create (`InvalidOnCreate`); ignored if supplied—server assigns ID in response. |
| `OwnerPartnerId` | `ownerPartnerId` | ID! | Required | Must be valid PartnerId. |
| `Name` | `name` | String! | Required | Max 256 chars. |
| `Description` | `description` | String | Optional | N/A |
| `Permissions` | `permissions` | DeliveryProfilePermissionsRESTInput | Optional | Nested object preserved. |
| `Permissions.PartnerIdsAllowedToBuy` | `permissions.partnerIdsAllowedToBuy` | [String!] | Optional | Required when Permissions is provided. |
| `Permissions.AdvertiserIdsAllowedToBuy` | `permissions.advertiserIdsAllowedToBuy` | [String!] | Optional | Required when Permissions is provided. Cannot overlap with AdvertiserIdsForbiddenToBuy. |
| `Permissions.AdvertiserIdsForbiddenToBuy` | `permissions.advertiserIdsForbiddenToBuy` | [String!] | Optional | Required when Permissions is provided. Cannot overlap with AdvertiserIdsAllowedToBuy. |

## Output field mapping

Output type: `DeliveryProfileREST` (returned as `data` on `DeliveryProfileCreatePayload`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `DeliveryProfileId` | `deliveryProfileId` | ID | Nullable | Assigned by server on create. |
| `OwnerPartnerId` | `ownerPartnerId` | ID | Nullable | N/A |
| `Name` | `name` | String | Nullable | N/A |
| `Description` | `description` | String | Nullable | N/A |
| `Permissions` | `permissions` | DeliveryProfilePermissionsREST | Nullable | N/A |
| `Permissions.PartnerIdsAllowedToBuy` | `permissions.partnerIdsAllowedToBuy` | [String!] | Nullable | N/A |
| `Permissions.AdvertiserIdsAllowedToBuy` | `permissions.advertiserIdsAllowedToBuy` | [String!] | Nullable | N/A |
| `Permissions.AdvertiserIdsForbiddenToBuy` | `permissions.advertiserIdsForbiddenToBuy` | [String!] | Nullable | N/A |

## Code examples

### REST example

```
POST /v3/deliveryProfile HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "OwnerPartnerId": "prt123abc",
  "Name": "US Publishers",
  "Description": "Delivery profile for US publisher inventory",
  "IsAllAllowedToBuy": false,
  "Permissions": {
    "PartnerIdsAllowedToBuy": ["prt456def"],
    "AdvertiserIdsAllowedToBuy": ["adv789ghi"],
    "AdvertiserIdsForbiddenToBuy": []
  }
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation {
  deliveryProfileCreate(input: {
    ownerPartnerId: "prt123abc"
    name: "US Publishers"
    description: "Delivery profile for US publisher inventory"
    isAllAllowedToBuy: false
    permissions: {
      partnerIdsAllowedToBuy: ["prt456def"]
      advertiserIdsAllowedToBuy: ["adv789ghi"]
      advertiserIdsForbiddenToBuy: []
    }
  }) {
    data {
      deliveryProfileId
      ownerPartnerId
      name
      description
      isAllAllowedToBuy
      permissions {
        partnerIdsAllowedToBuy
        advertiserIdsAllowedToBuy
        advertiserIdsForbiddenToBuy
      }
    }
    errors { ... on RestProxyMutationError { message field } }
  }
}
```
