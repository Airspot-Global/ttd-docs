# Delivery profile: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/deliveryprofile-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Delivery profile: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/deliveryProfile/{deliveryProfileId}` | `Query.deliveryProfile(id:)` | Self-extension fields on `DeliveryProfile` |
| `POST /v3/deliveryProfile/query/partner` | `Partner.deliveryProfiles` | N/A |
| `GET /v3/deliveryprofile/name/{deliveryProfileId}` | `Query.deliveryProfile(id:)` | Id and name only—redundant with `DeliveryProfile.id` / `DeliveryProfile.name` |
| `POST /v3/deliveryProfile` | `deliveryProfileCreate` | N/A |
| `PUT /v3/deliveryProfile` | `deliveryProfileUpdate` | N/A |

## Shared nested types and enums

### DeliveryProfilePermissionsRESTInput

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PartnerIdsAllowedToBuy` | `partnerIdsAllowedToBuy` | [String!] | Optional | Required when Permissions is provided. |
| `AdvertiserIdsAllowedToBuy` | `advertiserIdsAllowedToBuy` | [String!] | Optional | Required when Permissions is provided. Cannot overlap with AdvertiserIdsForbiddenToBuy. |
| `AdvertiserIdsForbiddenToBuy` | `advertiserIdsForbiddenToBuy` | [String!] | Optional | Required when Permissions is provided. Cannot overlap with AdvertiserIdsAllowedToBuy. |
