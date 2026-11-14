# Overview: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/overview-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Overview: REST → GraphQL migration guide

GraphQL replaces each overview GET with a root `partner` or `advertiser` query and nested connection fields.

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/overview/partner/{partnerId}` | `Query.partner(id:)` | N/A |
| `GET /v3/overview/advertiser/{advertiserId}` | `Query.advertiser(id:)` | N/A |

## Shared nested types and enums

### AdvertiserOverview

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | `id` | ID! | Not nullable | N/A |
| `AdvertiserName` | `name` | String! | Not nullable | N/A |
| `Description` | `description` | String | Nullable | N/A |
| `Campaigns` | `campaigns` | CampaignsWithAggregatesConnection | Nullable | Paginate; nested fields under `campaigns { nodes { … } }`. |
| `Creatives` | `creatives` | AdvertiserCreativesConnection | Nullable | Advertiser-scoped creatives; paginate. |

### CampaignOverview

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CampaignId` | `id` | ID! | Not nullable | N/A |
| `CampaignName` | `name` | String! | Not nullable | N/A |
| `Description` | `description` | String | Nullable | N/A |
| `StartDateUTC` | `startDate` | DateTime! | Not nullable | REST name `StartDateUTC`; GraphQL `startDate` (UTC). |
| `EnddateUTC` | `endDate` | DateTime | Nullable | REST typo `EnddateUTC` preserved from contract. |
| `Availability` | `isArchived` | Boolean! | Not nullable | REST `Availability` enum maps to `isArchived`; see Availability. |
| `AdGroups` | `adGroups` | AdGroupsWithAggregatesConnection | Nullable | Paginate; nested fields under `adGroups { nodes { … } }`. |

### AdGroupOverview

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdGroupId` | `id` | ID! | Not nullable | N/A |
| `AdGroupName` | `name` | String! | Not nullable | N/A |
| `Description` | `description` | String | Nullable | N/A |
| `IsEnabled` | `isEnabled` | Boolean! | Not nullable | N/A |
| `Availability` | `isArchived` | Boolean! | Not nullable | REST `Availability` enum maps to `isArchived`; see Availability. |
| `Creatives` | `creatives` | AdGroupCreativesConnection | Nullable | Ad-group creative assignments; paginate. |

### CreativeOverview

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CreativeId` | `id` | ID! | Not nullable | Under `adGroups.nodes.creatives.nodes` or advertiser-scoped `creatives.nodes`. |
| `CreativeName` | `name` | String | Nullable | REST `CreativeName` → GraphQL `name`. |
| `Description` | `description` | String | Nullable | N/A |

### Availability

| REST `Availability` | GraphQL field | GraphQL value | Notes |
| --- | --- | --- | --- |
| Available | `isArchived` | `false` | N/A |
| Archived | `isArchived` | `true` | N/A |

Use `where: { isArchived: { eq: false } }` on `campaigns` and `adGroups` connections to approximate REST “available only” results.
