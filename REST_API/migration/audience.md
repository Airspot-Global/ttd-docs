# Audience: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/audience-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Audience: REST → GraphQL migration guide

Legacy data-group audience create maps to `audienceCreate` with a different input model; audience update is not currently available in GraphQL.

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/audience/{audienceId}` | `Query.audience(id: ID!)` | N/A |
| `GET /v3/audience/{audienceId}/{geoForCounts}` | `Query.audience(id: ID!)` | Same shape; REST path geo is not an argument on the GraphQL query |
| `POST /v3/audience/query/advertiser` | `Advertiser.audiences` | N/A |
| `GET /v3/audience/name/{audienceId}` | `Query.audience(id:)` | Lightweight ID/name—select `{ id name }` |
| `POST /v3/audience/insights/channelmix` | `Audience.channelMixInsights` | N/A |
| `POST /v3/audience/insights/browser` | `Audience.browserInsights` | N/A |
| `POST /v3/audience/insights/os` | `Audience.operatingSystemInsights` | N/A |
| `POST /v3/audience/insights/marketmix` | `Audience.marketMixInsights` | N/A |
| `POST /v3/audience/insights/device` | `Audience.deviceInsights` | N/A |
| `POST /v3/audience/insights/interests` | `Audience.interestAudienceInsights` | N/A |
| `POST /v3/audience/insights/thirdparty` | `Audience.thirdPartySegmentInsights` | N/A |
| `POST /v3/audience/insights/appssites` | `Audience.appsSitesInsights` | N/A |
| `POST /v3/audience/insights/privatecontract` | `Audience.privateContractInsights` | N/A |
| `POST /v3/audience/insights/geo` | `Audience.geoInsights` | N/A |
| `GET /v3/audience/availableaudienceacceleratorexclusions` | `Query.availableAudienceAcceleratorExclusions` | N/A |
| `POST /v3/audience` | `audienceCreate` | Audience Predictor workflow; not a 1:1 REST data-group mirror |
| `PUT /v3/audience` | — | **Not currently available in GraphQL** |

## Shared nested types and enums

### MoneyModel

Used by paged insight endpoints for CPM values on metric rows.

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Amount` | `amount` | Decimal! | Not nullable | N/A |
| `CurrencyCode` | `currencyCode` | CurrencyCode! | Not nullable | N/A |

### AudienceBreakdownInsightsParamInput

Shared filter input for single-response insight fields on `Audience` (`channelMixInsights`, `browserInsights`, `deviceInsights`, `operatingSystemInsights`, `marketMixInsights`, `interestAudienceInsights`). Audience ID is taken from the parent entity.

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `GeoSegmentIds` | `geoSegmentIds` | [ID!]! | Required | Required geo scope. |

### AudienceThirdPartySegmentInsightsParamInput

Filter input for `Audience.thirdPartySegmentInsights`.

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `GeoSegmentIds` | `geoSegmentIds` | [ID!]! | Required | Required geo scope. |

### AudienceAppsSitesInsightsParamInput

Filter input for `Audience.appsSitesInsights`.

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `GeoSegmentIds` | `geoSegmentIds` | [ID!]! | Required | Required geo scope. |

### AudiencePrivateContractInsightsParamInput

Filter input for `Audience.privateContractInsights`.

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `GeoSegmentIds` | `geoSegmentIds` | [ID!]! | Required | Required geo scope. |

### AudienceGeoInsightsParamInput

Filter input for `Audience.geoInsights`.

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `GeoSegmentIds` | `geoSegmentIds` | [ID!]! | Required | Required geo scope. |

### ThirdPartySegmentInsight

Row type returned in `ThirdPartySegmentInsightsConnection` nodes.

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `ThirdPartyDataId` | `thirdPartyDataId` | Long! | Not nullable | N/A |
| `ThirdPartyDataBrandId` | `thirdPartyDataBrandId` | String! | Not nullable | N/A |
| `SegmentName` | `segmentName` | String! | Not nullable | N/A |
| `BrandName` | `brandName` | String! | Not nullable | N/A |
| `Size` | `size` | Long! | Not nullable | N/A |
| `Cpm` | `cpm` | MoneyModel! | Not nullable | N/A |
| `RelevanceScore` | `relevanceScore` | Float! | Not nullable | N/A |

### AppsSitesInsight

Row type returned in `AppsSitesInsightsConnection` nodes.

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Name` | `name` | String! | Not nullable | N/A |
| `Avails` | `avails` | Float! | Not nullable | N/A |
| `Cpm` | `cpm` | MoneyModel! | Not nullable | N/A |
| `RelevanceScore` | `relevanceScore` | Float! | Not nullable | N/A |
| `IsApp` | `isApp` | Boolean! | Not nullable | N/A |
| `ChannelName` | `channelName` | String! | Not nullable | N/A |

### PrivateContractInsight

Row type returned in `PrivateContractInsightsConnection` nodes.

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `PrivateContractId` | `privateContractId` | ID! | Not nullable | N/A |
| `ContractName` | `contractName` | String! | Not nullable | N/A |
| `IsFirstParty` | `isFirstParty` | Boolean! | Not nullable | N/A |
| `PublisherIds` | `publishers.id` | [ID!]! | Not nullable | N/A |
| `Publishers` | `publishers.name` | [String!]! | Not nullable | N/A |
| `LogoUrl` | `logoUrl` | String! | Not nullable | N/A |
| `Avails` | `avails` | Float! | Not nullable | N/A |
| `Cpm` | `cpm` | MoneyModel! | Not nullable | N/A |
| `RelevanceScore` | `relevanceScore` | Float! | Not nullable | N/A |
| `ChannelName` | `channelName` | String! | Not nullable | N/A |

### GeoInsight

Row type returned in `GeoInsightsConnection` nodes.

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Name` | `geoSegment.name` | String! | Not nullable | N/A |
| `GeoSegmentId` | `geoSegment.id` | ID! | Not nullable | N/A |
| `GeoType` | `geoSegment.type` | GeoSegmentType! | Not nullable | N/A |
| `Cpm` | `cpm` | MoneyModel! | Not nullable | N/A |
| `Avails` | `avails` | Long! | Not nullable | N/A |
| `RelevanceScore` | `relevanceScore` | Float! | Not nullable | N/A |
