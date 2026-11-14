# GET /v3/customcategory/{customCategoryId} → Query.customCategory(id:)

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-customcategory-customcategoryid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/customcategory/{customCategoryId} → Query.customCategory(id:)

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/customcategory/{customCategoryId}` |
| GraphQL query | `Query.customCategory(id:)` |
| Return type | `CustomCategory` |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CustomCategoryId` | `id` | ID! | Not nullable | N/A |
| `CustomCategoryName` | `customCategoryName` | String | Nullable | N/A |
| `CustomCategoryType` | `customCategoryType` | CustomCategoryType | Nullable | N/A |
| `Keywords` | `keywords` | [CustomCategoryKeyword!]! | Not nullable | Plain list; select fields directly on each element. |
| `Keywords.Value` | `keywords { value }` | String! | Not nullable | Nested keyword field. |
| `Keywords.MatchType` | `keywords { matchType }` | KeywordMatchType! | Not nullable | N/A |
| `Keywords.MatchApplication` | `keywords { matchApplication }` | KeywordMatchApplication! | Not nullable | N/A |
| `LanguageCode` | `languageCode` | String | Nullable | N/A |
| `AdvertiserId` | `advertiser` | Advertiser | Nullable | Advertiser relationship. |
| `PartnerId` | `partnerId` | String | Nullable | N/A |
| `Status` | `status` | CustomCategoryStatus | Nullable | N/A |
| `TTDContextualCategoryId` | `ttdContextualCategoryId` | String | Nullable | N/A |
| N/A | `keywordCount` | Long | Nullable | Derived from keyword count when loaded via GET-by-ID. |
| N/A | `categoryBidListType` | ContextualCategoryBidListType | Nullable | Null for TTD contextual categories on this load path. |

## Endpoint-specific nested types and enums

### CustomCategoryKeyword

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Value` | `value` | String! | Not nullable | N/A |
| `MatchType` | `matchType` | KeywordMatchType! | Not nullable | N/A |
| `MatchApplication` | `matchApplication` | KeywordMatchApplication! | Not nullable | N/A |

## Code examples

### REST example

```
GET /v3/customcategory/{customCategoryId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query ById($id: ID!) {
  customCategory(id: $id) {
    id
    customCategoryName
    status
    ttdContextualCategoryId
    keywords {
      value
      matchType
      matchApplication
    }
  }
}
```
