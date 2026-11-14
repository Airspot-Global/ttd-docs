# POST /v3/customcategory/query → Query.customCategories(input:)

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-customcategory-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/customcategory/query → Query.customCategories(input:)

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/customcategory/query` |
| GraphQL query | `Query.customCategories(input:)` |
| Return type | `[CustomCategory!]!` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `CustomCategorySourceType` | `CustomCategoryQueryInput.customCategorySourceType` | CustomCategorySourceTypeInput! | Required | Required in the POST body. |
| `AdvertiserId` | `CustomCategoryQueryInput.advertiserId` | String | Optional | At least one of `AdvertiserId` or `PartnerId` is required at runtime for valid REST requests. |
| `PartnerId` | `CustomCategoryQueryInput.partnerId` | String | Optional | At least one of `AdvertiserId` or `PartnerId` is required at runtime for valid REST requests. |

## Response field mapping

REST returns a top-level JSON array of `CustomCategorySummary` objects.

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| _(top-level array)_ | `customCategories` | [CustomCategory!]! | Not nullable | N/A |
| `CustomCategoryId` | `id` | ID! | Not nullable | Same fields as advertiser list responses. |
| `CustomCategoryName` | `customCategoryName` | String | Nullable | N/A |
| `CustomCategoryType` | `customCategoryType` | CustomCategoryType | Nullable | N/A |
| `KeywordCount` | `keywordCount` | Long | Nullable | From summary payload. |
| `AdvertiserId` | `advertiser` | Advertiser | Nullable | N/A |
| `PartnerId` | `partnerId` | String | Nullable | N/A |
| `Status` | `status` | CustomCategoryStatus | Nullable | N/A |
| `LanguageCode` | `languageCode` | String | Nullable | N/A |
| `CategoryBidListType` | `categoryBidListType` | ContextualCategoryBidListType | Nullable | From summary for non-TTD sources. |

## Code examples

### REST example

```
POST /v3/customcategory/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserId": "<advertiser-id>",
  "CustomCategorySourceType": "TTDContextualCategory"
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query BySource($input: CustomCategoryQueryInput!) {
  customCategories(input: $input) {
    id
    customCategoryName
    categoryBidListType
  }
}
```

Variables:

```
{
  "input": {
    "advertiserId": "<advertiser-id>",
    "customCategorySourceType": "TTD_CONTEXTUAL_CATEGORY"
  }
}
```
