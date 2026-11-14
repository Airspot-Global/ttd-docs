# GET /v3/customcategory/advertiser/{advertiserId} → Advertiser.customCategories

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-customcategory-advertiser-advertiserid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/customcategory/advertiser/{advertiserId} → Advertiser.customCategories

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/customcategory/advertiser/{advertiserId}` |
| GraphQL query | `Advertiser.customCategories` |
| Return type | `[CustomCategory!]!` |

## Response field mapping

REST returns a top-level JSON array of `CustomCategorySummary` objects.

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| _(top-level array)_ | `customCategories` | [CustomCategory!]! | Not nullable | Path parameter `advertiserId` selects the parent advertiser. |
| `CustomCategoryId` | `id` | ID! | Not nullable | List element. |
| `CustomCategoryName` | `customCategoryName` | String | Nullable | List element. |
| `CustomCategoryType` | `customCategoryType` | CustomCategoryType | Nullable | List element. |
| `KeywordCount` | `keywordCount` | Long | Nullable | From summary payload on list load paths. |
| `AdvertiserId` | `advertiser` | Advertiser | Nullable | List element. |
| `PartnerId` | `partnerId` | String | Nullable | List element. |
| `Status` | `status` | CustomCategoryStatus | Nullable | List element. |
| `LanguageCode` | `languageCode` | String | Nullable | List element. |
| `CategoryBidListType` | `categoryBidListType` | ContextualCategoryBidListType | Nullable | From summary for non-TTD sources. |
| N/A | `keywords` | [CustomCategoryKeyword!]! | Not nullable | Loaded via an extra GET-by-ID when selected on list results. |
| N/A | `ttdContextualCategoryId` | String | Nullable | Present on unified `CustomCategory` type. |

## Code examples

### REST example

```
GET /v3/customcategory/advertiser/{advertiserId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query ByAdvertiser($advertiserId: ID!) {
  advertiser(id: $advertiserId) {
    id
    customCategories {
      id
      customCategoryName
      keywordCount
    }
  }
}
```
