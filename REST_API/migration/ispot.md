# ISpot: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/ispot-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# ISpot: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `POST /v3/ispot/brand/query` | `Query.incrementalReachProvider.brands` | Paged brand list with optional name filter |
| `GET /v3/ispot/reportsettings/campaign/{campaignId}` | `Campaign(id:).incrementalReachSettings.iSpotReachSetting` | `iSpot` reporting settings for a campaign |

## Shared nested types and enums

### IncrementalReachBrand

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `BrandId` | `id` | ID! | Not nullable | External `iSpot` brand ID. |
| `BrandName` | `name` | String! | Not nullable | Brand display name. |
