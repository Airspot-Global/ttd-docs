# PUT /v3/deliveryProfile → deliveryProfileUpdate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/put-v3-deliveryprofile
- Retrieved: 2026-11-14
- Category: REST_API

---

# PUT /v3/deliveryProfile → deliveryProfileUpdate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `PUT /v3/deliveryProfile` |
| GraphQL operation | `deliveryProfileUpdate` |
| Input type | `DeliveryProfileUpdateInput` |
| Output type | `DeliveryProfileUpdatePayload` (`data: DeliveryProfileREST`, `errors: [DeliveryProfileUpdateMutationError!]` / `RestProxyMutationError`) |

## Input field mapping

Input type: `DeliveryProfileUpdateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `DeliveryProfileId` | `deliveryProfileId` | ID! | Required | Required on update. |
| `OwnerPartnerId` | `ownerPartnerId` | ID | Optional | N/A |
| `Name` | `name` | String | Optional | Max 256 chars. |
| `Description` | `description` | String | Optional | N/A |
| `Permissions` | `permissions` | DeliveryProfilePermissionsRESTInput | Optional | Nested object preserved. |
| `Permissions.PartnerIdsAllowedToBuy` | `permissions.partnerIdsAllowedToBuy` | [String!] | Optional | Required when Permissions is provided. |
| `Permissions.AdvertiserIdsAllowedToBuy` | `permissions.advertiserIdsAllowedToBuy` | [String!] | Optional | Required when Permissions is provided. Cannot overlap with AdvertiserIdsForbiddenToBuy. |
| `Permissions.AdvertiserIdsForbiddenToBuy` | `permissions.advertiserIdsForbiddenToBuy` | [String!] | Optional | Required when Permissions is provided. Cannot overlap with AdvertiserIdsAllowedToBuy. |

## Output field mapping

Output type: `DeliveryProfileREST` (returned as `data` on `DeliveryProfileUpdatePayload`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `DeliveryProfileId` | `deliveryProfileId` | ID | Nullable | N/A |
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
PUT /v3/deliveryProfile HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "DeliveryProfileId": "dp123abc",
  "Name": "US Publishers (updated)",
  "Description": "Updated delivery profile description",
  "Permissions": {
    "PartnerIdsAllowedToBuy": ["prt456def"],
    "AdvertiserIdsAllowedToBuy": ["adv789ghi"],
    "AdvertiserIdsForbiddenToBuy": ["adv000xyz"]
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
  deliveryProfileUpdate(input: {
    deliveryProfileId: "dp123abc"
    name: "US Publishers (updated)"
    description: "Updated delivery profile description"
    permissions: {
      partnerIdsAllowedToBuy: ["prt456def"]
      advertiserIdsAllowedToBuy: ["adv789ghi"]
      advertiserIdsForbiddenToBuy: ["adv000xyz"]
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
