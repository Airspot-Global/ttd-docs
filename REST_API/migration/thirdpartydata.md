# Third party data: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/thirdpartydata-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Third party data: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `POST /v3/thirdpartydata/query` | `ThirdPartyDataProvider.thirdPartyDataTaxonomies` | N/A |
| `GET /v3/thirdpartydata/status/{providerId}/{providerElementId}` | `ThirdPartyDataProvider.taxonomyApprovalStatus` | N/A |
| `POST /v3/dmp/thirdparty/advertiser` | `Query.thirdPartyDatas` | **IMPORTANT**: `Query.thirdPartyDatas` is deprecated. Use `partner(id).thirdPartyDataExpanded` for segment discovery. |
| `POST /v3/dmp/firstparty/advertiser` | `Advertiser.firstPartyData` | **IMPORTANT**: `Advertiser.firstPartyData` is deprecated. Use `Advertiser(id).firstPartyData` with filtering instead. |
| `GET /v3/dmp/lookalikemodel/{firstPartyDataId}` | N/A | Not currently available in GraphQL |
| `GET /v3/dmp/lookalikemodel/build/{firstPartyDataId}` | N/A | Not currently available in GraphQL |
| `POST /v3/dmp/lookalikethirdpartydata/query` | `Advertiser.targetingDataSegments` | Select `lookAlikeThirdPartyData` on connection edges |
| `GET /v3/thirdpartydataprovider` | `Query.thirdPartyDataProvidersForBilling` | N/A |
| `GET /v3/thirdpartydataprovider/{providerId}` | `Query.thirdPartyDataProviderForBilling` | N/A |
| `GET /v3/thirdpartydataproviderbrandmapping` | `Query.thirdPartyDataProviderBrandMappings` | N/A |
| `GET /v3/thirdpartydataproviderbrandmapping/{brandId}` | `Query.thirdPartyDataProviderBrandMapping` | N/A |
| `POST /v3/datarate/query` | `ThirdPartyDataProvider.thirdPartyDataRates` | N/A |
| `GET /v3/datarate/batch/{batchId}` | `Query.thirdPartyDataRateBatch` | N/A |
| `GET /v3/datarate/brands/{providerId}` | `ThirdPartyDataProvider.brandsForDataRates` | N/A |

## Shared nested types and enums

### MoneyModel

| GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- |
| `amount` | `Decimal!` | Not nullable | N/A |
| `currency` | `Currency!` | Not nullable | N/A |
| `currencyCode` | `CurrencyCode!` | Not nullable | N/A |

### ThirdPartyDataRate

Node type returned by `ThirdPartyDataProvider.thirdPartyDataRates`. REST returns a flat `BrandId`; GraphQL exposes `brand: ThirdPartyDataBrand!`, so resolve the brand ID as `brand { id }`. REST `RateLevel` and `RateType` map to `rateLevel` and `rateType`.

| GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- |
| `advertiser` | `Advertiser` | Nullable | Present when `rateLevel` is advertiser-level |
| `brand` | `ThirdPartyDataBrand!` | Not nullable | REST `BrandId` → `brand { id }` |
| `cpmRate` | `MoneyModel` | Nullable | Present when `rateType` is CPM or hybrid |
| `inheritedFromProviderElementId` | `ID` | Nullable | N/A |
| `isInherited` | `Boolean` | Nullable | N/A |
| `partner` | `Partner` | Nullable | Present when `rateLevel` is partner-level |
| `percentOfMediaCostRate` | `Decimal` | Nullable | Present when `rateType` is percent-of-media-cost or hybrid |
| `provider` | `ThirdPartyDataProvider!` | Not nullable | N/A |
| `providerElementId` | `ID!` | Not nullable | N/A |
| `rateLevel` | `DataRateLevel!` | Not nullable | REST `RateLevel` |
| `rateType` | `ThirdPartyDataRateType!` | Not nullable | REST `RateType` |

### ThirdPartyDataRateBatchItem

Element type of `ThirdPartyDataRateBatch.dataRates`. REST returns a flat `BrandId`; GraphQL exposes `brand: ThirdPartyDataBrand!`, so resolve the brand ID as `brand { id }`. REST `RateLevel` and `RateType` map to `rateLevel` and `rateType`.

| GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- |
| `advertiser` | `Advertiser` | Nullable | Present when `rateLevel` is advertiser-level |
| `brand` | `ThirdPartyDataBrand!` | Not nullable | REST `BrandId` → `brand { id }` |
| `cpmRate` | `MoneyModel` | Nullable | Present when `rateType` is CPM or hybrid |
| `partner` | `Partner` | Nullable | Present when `rateLevel` is partner-level |
| `percentOfMediaCostRate` | `Decimal` | Nullable | Present when `rateType` is percent-of-media-cost or hybrid |
| `providerElementId` | `ID!` | Not nullable | N/A |
| `rateLevel` | `DataRateLevel!` | Not nullable | REST `RateLevel` |
| `rateType` | `ThirdPartyDataRateType!` | Not nullable | REST `RateType` |

### DataRateBatchApprovalStatus

Approval status on `ThirdPartyDataRateBatch.approvalStatus`.

| GraphQL value | Notes |
| --- | --- |
| `APPROVED` | N/A |
| `AWAITING_MANUAL_REVIEW` | N/A |
| `DENIED` | N/A |
| `NOT_REVIEWED` | N/A |

### DataRateLevelInput

| GraphQL value | Notes |
| --- | --- |
| `ADVERTISER` | N/A |
| `PARTNER` | N/A |
| `SYSTEM` | N/A |

### DataRateLevel

Distinct type from `DataRateLevelInput` above (output enum vs query filter); members are the same.

| GraphQL value | Notes |
| --- | --- |
| `ADVERTISER` | N/A |
| `PARTNER` | N/A |
| `SYSTEM` | N/A |

### ThirdPartyDataRateType

| GraphQL value | Notes |
| --- | --- |
| `CPM` | Priced per thousand impressions; read `cpmRate` |
| `HYBRID` | Both a CPM and a percentage of media cost apply |
| `PERCENT_OF_MEDIA_COST` | Priced as a share of media cost; read `percentOfMediaCostRate` |

### DataRateBatchProcessingStatus

Distinct from `DataRateBatchApprovalStatus` above.

| GraphQL value | Notes |
| --- | --- |
| `FAILED` | N/A |
| `IN_PROGRESS` | N/A |
| `NOT_STARTED` | N/A |
| `SUCCESSFUL` | N/A |

### DataEventType

| GraphQL value | Notes |
| --- | --- |
| `ADD_TO_CART` | N/A |
| `DIRECTION` | N/A |
| `LOCATION_VISITORS` | N/A |
| `LOGIN` | N/A |
| `LOYALTY_MEMBERS` | N/A |
| `MESSAGE_BUSINESS` | N/A |
| `MODELED_PHARMA` | N/A |
| `OTHER` | N/A |
| `PURCHASE` | N/A |
| `PURCHASE_CATEGORY` | N/A |
| `PURCHASE_CATEGORY_MODELED` | N/A |
| `PURCHASE_MODELED` | N/A |
| `REGISTERED_VOTERS` | N/A |
| `SEARCH_CATEGORY` | N/A |
| `SEARCH_ITEM` | N/A |
| `SITE_VISIT` | N/A |
| `START_CHECKOUT` | N/A |
| `SUBSCRIBE_TO_NEWSLETTER` | N/A |
| `VIEW_CART` | N/A |
| `VIEW_ITEM` | N/A |
| `VOTERS` | N/A |
| `WISH_LIST_ITEM` | N/A |

### TargetingDataType

| GraphQL value | Notes |
| --- | --- |
| `BULK_USER_LIST` | N/A |
| `CAMPAIGN_SEED_DATA` | N/A |
| `CLICK_RETARGETING` | N/A |
| `CRM_DATA` | N/A |
| `DIRECT_IP_TARGETING` | N/A |
| `DYNAMIC_TRACKING_RULE` | N/A |
| `ECOMMERCE_CATALOG_LIST` | N/A |
| `EMAIL_OPEN` | N/A |
| `FIXED_PRICE_USER` | N/A |
| `HOUSEHOLD_EXTENSION` | N/A |
| `IMPORTED_ADVERTISER_DATA` | N/A |
| `IMPORTED_ADVERTISER_DATA_WITH_BASE_BID` | N/A |
| `IP_ADDRESS_RANGE` | N/A |
| `LOOK_A_LIKE_DATA` | N/A |
| `PAID_SEARCH_CLICK` | N/A |
| `PLAYER_EVENT_COMPLETE` | N/A |
| `PLAYER_EVENT_MIDPOINT` | N/A |
| `PLAYER_EVENT_START` | N/A |
| `SEED_DATA` | N/A |
| `THIRD_PARTY_DATA` | N/A |
| `THIRD_PARTY_IMPRESSION` | N/A |
| `TRACKING_TAG` | N/A |
| `UNKNOWN` | N/A |

### SegmentAudienceExpansion

Object type, not an enum.

| GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- |
| `countries` | `[String!]` | Nullable | N/A |
| `isCrossDeviceExpansionEnabled` | `Boolean` | Nullable | N/A |
| `isEnabled` | `Boolean` | Nullable | N/A |
| `isLookAlikeExpansionEnabled` | `Boolean` | Nullable | N/A |
| `lastProcessedUtc` | `DateTime` | Nullable | N/A |
| `lookalikeSettings` | `AudienceExpansionLookalikeSettings` | Nullable | N/A |
| `providerElementIds` | `[String!]` | Nullable | N/A |

### ThirdPartyDataSortInput

Input object, not an enum.

| GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- |
| `id` | `SortEnumType` | Optional | N/A |
| `thirdPartyDataProviderId` | `SortEnumType` | Optional | N/A |
