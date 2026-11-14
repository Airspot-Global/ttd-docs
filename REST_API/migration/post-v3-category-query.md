# POST /v3/category/query → Query.categories

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-category-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/category/query → Query.categories

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/category/query` |
| GraphQL query | `Query.categories(input: CategoryQueryInput!, first: Int, after: String)` |
| Return type | `LegacyRestCategoriesConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `CategorySourceType` | `CategoryQueryInput.categorySourceType` | `CategorySourceTypeInput!` | Required | Required in the POST body. See `CategorySourceTypeInput` value mapping below. |
| `PartnerId` | `CategoryQueryInput.partnerId` | `ID` | Optional | At least one of `PartnerId` or `AdvertiserId` is required; both empty returns HTTP 400 in REST and a GraphQL validation error. |
| `AdvertiserId` | `CategoryQueryInput.advertiserId` | `ID` | Optional | At least one of `PartnerId` or `AdvertiserId` is required. |
| `SortFields` | `CategoryQueryInput.sortFields` | `[CategorySortingFieldSortInput!]` | Optional | Each entry has `fieldId: CategorySortingFieldInput!` and `ascending`. REST defaults to Name ascending when omitted; GraphQL exposes only `PATH` for explicit sort. |
| `PageStartIndex` | `after` | `String` | Optional | N/A |
| `PageSize` | `first` | `Int` | Optional | N/A |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | `[CategoryInfo!]` | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | `Int!` | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].Id` | `CategoryInfo.id` | `ID!` | Not nullable | Contextual targeting ID. |
| `Result[].Name` | `CategoryInfo.name` | `String!` | Not nullable | N/A |
| `Result[].Path` | `CategoryInfo.path` | `String!` | Not nullable | Computed hierarchy path. |
| `Result[].ParentId` | `CategoryInfo.parentId` | `ID` | Nullable | Null at the root. |
| `Result[].CategoryBidListType` | `CategoryInfo.categoryBidListType` | `ContextualCategoryBidListType!` | Not nullable | N/A |

## Endpoint-specific nested types and enums

### CategoryInfo

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Id` | `id` | `ID!` | Not nullable | Contextual targeting ID. |
| `Name` | `name` | `String!` | Not nullable | N/A |
| `Path` | `path` | `String!` | Not nullable | Computed hierarchy path. |
| `ParentId` | `parentId` | `ID` | Nullable | Null at the root. |
| `CategoryBidListType` | `categoryBidListType` | `ContextualCategoryBidListType!` | Not nullable | N/A |

### CategorySortingFieldSortInput

| Field | GraphQL type | Required | Notes |
| --- | --- | --- | --- |
| fieldId | `CategorySortingFieldInput!` | Required | Sort field to apply. |
| ascending | `Boolean` | Optional | Sort direction. |

### CategorySortingFieldInput

| Enum value | Notes |
| --- | --- |
| `PATH` | Sort by the full hierarchical path of the category. |

### CategorySourceTypeInput

| REST value | GraphQL value | Notes |
| --- | --- | --- |
| `UniversalCategoryTaxonomy` | `UNIVERSAL_CATEGORY_TAXONOMY` | N/A |
| `IntegralContextual` | `INTEGRAL_CONTEXTUAL` | N/A |
| `SemasioContextual` | `SEMASIO_CONTEXTUAL` | N/A |
| `Peer39Contextual` | `PEER39_CONTEXTUAL` | N/A |
| `DoubleVerifyContextual` | `DOUBLE_VERIFY_CONTEXTUAL` | N/A |
| `IntegralBrandSafety` | `INTEGRAL_BRAND_SAFETY` | N/A |
| `IntegralVideoBrandSafety` | `INTEGRAL_VIDEO_BRAND_SAFETY` | N/A |
| `Peer39BrandSafety` | `PEER39_BRAND_SAFETY` | N/A |
| `DoubleVerifyBrandSafety` | `DOUBLE_VERIFY_BRAND_SAFETY` | N/A |
| `DoubleVerifyBotAvoidance` | `DOUBLE_VERIFY_BOT_AVOIDANCE` | N/A |
| `ContextualApp` | `CONTEXTUAL_APP` | N/A |
| `Peer39PageQuality` | `PEER39_PAGE_QUALITY` | N/A |
| `IntegralPageQuality` | `INTEGRAL_PAGE_QUALITY` | N/A |
| `IntegralVideoPageQuality` | `INTEGRAL_VIDEO_PAGE_QUALITY` | N/A |
| `IntegralViewability` | `INTEGRAL_VIEWABILITY` | N/A |
| `IntegralVideoViewability` | `INTEGRAL_VIDEO_VIEWABILITY` | N/A |
| `DoubleVerifyViewability` | `DOUBLE_VERIFY_VIEWABILITY` | N/A |
| `DoubleVerifyVideoViewability` | `DOUBLE_VERIFY_VIDEO_VIEWABILITY` | N/A |
| `Peer39Viewability` | `PEER39_VIEWABILITY` | N/A |
| `RTBAsiaPageQuality` | `RTB_ASIA_PAGE_QUALITY` | N/A |
| `RTBAsiaVideoPageQuality` | `RTB_ASIA_VIDEO_PAGE_QUALITY` | N/A |
| `ContextualSupplyVendorCategory` | `CONTEXTUAL_SUPPLY_VENDOR_CATEGORY` | N/A |
| `ContextualSupplyVendorGenre` | `CONTEXTUAL_SUPPLY_VENDOR_GENRE` | N/A |
| `TTDContextualCategory` | `TTD_CONTEXTUAL_CATEGORY` | N/A |
| `EmetriqContextualCategory` | `EMETRIQ_CONTEXTUAL_CATEGORY` | N/A |
| `TencentPageQualityCategory` | `TENCENT_PAGE_QUALITY_CATEGORY` | N/A |
| `ComscoreContextualCategory` | `COMSCORE_CONTEXTUAL_CATEGORY` | N/A |
| `CaptifyContextualCategory` | `CAPTIFY_CONTEXTUAL_CATEGORY` | N/A |
| `AdFontesContextualCategory` | `AD_FONTES_CONTEXTUAL_CATEGORY` | N/A |
| `GumGumContextualCategory` | `GUM_GUM_CONTEXTUAL_CATEGORY` | N/A |
| `NewsGuardContextualCategory` | `NEWS_GUARD_CONTEXTUAL_CATEGORY` | N/A |
| `IllumaContextualCategory` | `ILLUMA_CONTEXTUAL_CATEGORY` | N/A |
| `AudigentContextualCategory` | `AUDIGENT_CONTEXTUAL_CATEGORY` | N/A |
| `ShareThisContextualCategory` | `SHARE_THIS_CONTEXTUAL_CATEGORY` | N/A |
| `WeboramaContextualCategory` | `WEBORAMA_CONTEXTUAL_CATEGORY` | N/A |
| `DstilleryContextualCategory` | `DSTILLERY_CONTEXTUAL_CATEGORY` | N/A |
| `Scope3ContextualCategory` | `SCOPE3_CONTEXTUAL_CATEGORY` | N/A |
| `OSDSContextualCategory` | `OSDS_CONTEXTUAL_CATEGORY` | N/A |
| `CrossPixelContextualCategory` | `CROSS_PIXEL_CONTEXTUAL_CATEGORY` | N/A |
| `LumenContextualCategory` | `LUMEN_CONTEXTUAL_CATEGORY` | N/A |
| `AdelaideContextualCategory` | `ADELAIDE_CONTEXTUAL_CATEGORY` | N/A |
| `QwarryContextualCategory` | `QWARRY_CONTEXTUAL_CATEGORY` | N/A |
| `BarometerContextualCategory` | `BAROMETER_CONTEXTUAL_CATEGORY` | N/A |
| `SirdataContextualCategory` | `SIRDATA_CONTEXTUAL_CATEGORY` | N/A |
| `MobianContextualCategory` | `MOBIAN_CONTEXTUAL_CATEGORY` | N/A |
| `SilverpushContextualCategory` | `SILVERPUSH_CONTEXTUAL_CATEGORY` | N/A |
| `FourDContextualCategory` | `FOUR_D_CONTEXTUAL_CATEGORY` | N/A |
| `AeternaLabsContextualCategory` | `AETERNA_LABS_CONTEXTUAL_CATEGORY` | N/A |
| `XplnContextualCategory` | `XPLN_CONTEXTUAL_CATEGORY` | N/A |
| `AblidaContextualCategory` | `ABLIDA_CONTEXTUAL_CATEGORY` | N/A |
| `hyScoreContextualCategory` | `HY_SCORE_CONTEXTUAL_CATEGORY` | N/A |
| `TrueRelevanceContextualCategory` | `TRUE_RELEVANCE_CONTEXTUAL_CATEGORY` | N/A |
| `NanoInteractiveContextualCategory` | `NANO_INTERACTIVE_CONTEXTUAL_CATEGORY` | N/A |
| `RaasLabContextualCategory` | `RAAS_LAB_CONTEXTUAL_CATEGORY` | N/A |
| `AnokiIncContextualCategory` | `ANOKI_INC_CONTEXTUAL_CATEGORY` | N/A |

### ContextualCategoryBidListType

| Enum value | Notes |
| --- | --- |
| `BOTH` | N/A |
| `BLOCK` | N/A |
| `TARGET` | N/A |

## Code examples

### REST example

```
POST /v3/category/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "CategorySourceType": "UniversalCategoryTaxonomy",
  "PartnerId": "partner-id",
  "PageStartIndex": 0,
  "PageSize": 100,
  "SortFields": [
    { "FieldId": "Path", "Ascending": true }
  ]
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query Categories($input: CategoryQueryInput!) {
  categories(input: $input, first: 100) {
    nodes {
      id
      name
      path
      parentId
      categoryBidListType
    }
    totalCount
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

Variables:

```
{
  "input": {
    "categorySourceType": "UNIVERSAL_CATEGORY_TAXONOMY",
    "partnerId": "partner-id",
    "sortFields": [
      { "fieldId": "PATH", "ascending": true }
    ]
  }
}
```
