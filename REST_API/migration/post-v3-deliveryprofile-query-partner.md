# POST /v3/deliveryProfile/query/partner → Partner.deliveryProfiles

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-deliveryprofile-query-partner
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/deliveryProfile/query/partner → Partner.deliveryProfiles

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/deliveryProfile/query/partner` |
| GraphQL query | `Partner.deliveryProfiles` |
| Return type | `DeliveryProfilesConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PartnerId` | Parent: `Partner.deliveryProfiles` (relationship field) | N/A | Required | Parent entity identifies the partner; supplied by `Partner.id`, not a filter arg. |
| `SearchTerms` | `filter.searchTerms` | [String!] | Optional | All terms must match in ID, name, or description. |
| `SortFields` | `filter.sortFields` | [DeliveryProfileSortingFieldSortingInput!] | Optional | Nested sorting input; `fieldId` is `DeliveryProfileSortingFieldInput`, `ascending` is Boolean. |
| `Availabilities` | `filter.availabilities` | [AvailabilityInput!] | Optional | `AvailabilityInput` enum (`AVAILABLE`, `ARCHIVED`). |
| `ReturnOnlyIds` | `filter.returnOnlyIds` | Boolean | Optional | Whether result items contain IDs only. |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [DeliveryProfile!] | Nullable | N/A |
| `Result[].DeliveryProfileId` | `id` (on `DeliveryProfile`) | ID! | Not nullable | N/A |
| `Result[].OwnerPartnerId` | `ownerPartner` (on `DeliveryProfile`) | Partner | Nullable | Entity reference; select `ownerPartner { id }` for the identifier. |
| `Result[].Name` | `name` (on `DeliveryProfile`) | String! | Not nullable | N/A |
| `Result[].Description` | `description` (on `DeliveryProfile`) | String | Nullable | N/A |
| `Result[].Permissions` | `permissions` (on `DeliveryProfile`) | DeliveryProfilePermissions | Nullable | Nested object—see DeliveryProfilePermissions below. |
| `Result[].Permissions.PartnerIdsAllowedToBuy` | `permissions.partnerIdsAllowedToBuy` | [ID!]! | Not nullable | N/A |
| `Result[].Permissions.AdvertiserIdsAllowedToBuy` | `permissions.advertiserIdsAllowedToBuy` | [ID!]! | Not nullable | N/A |
| `Result[].Permissions.AdvertiserIdsForbiddenToBuy` | `permissions.advertiserIdsForbiddenToBuy` | [ID!]! | Not nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |

## Endpoint-specific nested types and enums

### DeliveryProfile

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `DeliveryProfileId` | `id` | ID! | Not nullable | N/A |
| `OwnerPartnerId` | `ownerPartner` | Partner | Nullable | Entity reference; select `ownerPartner { id }` for the identifier. |
| `Name` | `name` | String! | Not nullable | N/A |
| `Description` | `description` | String | Nullable | N/A |
| `Permissions` | `permissions` | DeliveryProfilePermissions | Nullable | Nested object—see DeliveryProfilePermissions below. |

### DeliveryProfilePermissions

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `PartnerIdsAllowedToBuy` | `partnerIdsAllowedToBuy` | [ID!]! | Not nullable | N/A |
| `AdvertiserIdsAllowedToBuy` | `advertiserIdsAllowedToBuy` | [ID!]! | Not nullable | N/A |
| `AdvertiserIdsForbiddenToBuy` | `advertiserIdsForbiddenToBuy` | [ID!]! | Not nullable | N/A |

### AvailabilityInput

| REST value | GraphQL value |
| --- | --- |
| `Available` | `AVAILABLE` |
| `Archived` | `ARCHIVED` |

### DeliveryProfileSortingFieldSortingInput

| Field | GraphQL type | Required | Notes |
| --- | --- | --- | --- |
| fieldId | DeliveryProfileSortingFieldInput! | Required | Sort field to apply. |
| ascending | Boolean | Optional | Sort direction; defaults to ascending when omitted. |

### DeliveryProfileSortingFieldInput

| Enum value | Notes |
| --- | --- |
| `NAME` | Sort by delivery profile name. |
| `DESCRIPTION` | Sort by delivery profile description. |

## Code examples

### REST example

```
POST /v3/deliveryProfile/query/partner HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "PartnerId": "<partner-id>",
  "SearchTerms": ["promo"],
  "Availabilities": ["Available"],
  "SortFields": [{ "FieldId": "Name", "Ascending": true }],
  "PageStartIndex": 0,
  "PageSize": 100
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query PartnerDeliveryProfiles($partnerId: ID!) {
  partner(id: $partnerId) {
    id
    deliveryProfiles(
      first: 100
      filter: {
        searchTerms: ["promo"]
        availabilities: [AVAILABLE]
        sortFields: [{ fieldId: NAME, ascending: true }]
      }
    ) {
      nodes {
        id
        name
        ownerPartner {
          id
        }
      }
      totalCount
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
}
```
