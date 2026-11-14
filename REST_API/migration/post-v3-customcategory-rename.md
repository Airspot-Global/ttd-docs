# POST /v3/customcategory/rename → customCategoryUpdate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-customcategory-rename
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/customcategory/rename → customCategoryUpdate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/customcategory/rename` |
| GraphQL operation | `customCategoryUpdate` |
| Input type | `CustomCategoryUpdateInput` |
| Output type | `CustomCategoryUpdatePayload` (`data: CustomCategoryREST`, `errors: [CustomCategoryUpdateMutationError!]`) |

> **IMPORTANT:** REST accepts names up to **256** characters (`NewName`). The GraphQL update input documents a maximum of **100** characters for `customCategoryName`. A category name between 101 and 256 characters that succeeds on REST will be **rejected** by GraphQL. Trim or shorten names in that range before migrating.

> **NOTE:** `CustomCategoryUpdateInput` is a general-purpose update type. For a rename, supply **only** `customCategoryId` and `customCategoryName`. Leave `keywords`, `customCategoryType`, `languageCode`, `advertiserId`, and `partnerId` unset (omit them from the mutation input). Sending other fields may unintentionally clear or overwrite category data.

## Input field mapping

Input type: `CustomCategoryUpdateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `CustomCategoryId` | `customCategoryId` | ID! | Required | ID of the category to rename. |
| `NewName` | `customCategoryName` | String | Required | REST request body field `NewName` (not `CustomCategoryName`). Maps to GraphQL input `customCategoryName`. Max 100 characters on GraphQL (REST allows 256—see IMPORTANT note above). |

## Output field mapping

Output type: `CustomCategoryREST` (returned as `data` on `CustomCategoryUpdatePayload`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `CustomCategoryId` | `customCategoryId` | ID | Nullable | N/A |
| `CustomCategoryName` | `customCategoryName` | String | Nullable | N/A |
| `CustomCategoryType` | `customCategoryType` | CustomCategoryTypeREST | Nullable | Returned only for TTD contextual categories |
| `KeywordCount` | `keywordCount` | Long | Nullable | REST non-nullable long; GraphQL exposes nullable Long |
| `AdvertiserId` | `advertiserId` | ID | Nullable | N/A |
| `PartnerId` | `partnerId` | ID | Nullable | N/A |
| `Status` | `status` | CustomCategoryStatusREST | Nullable | See CustomCategory domain page `CustomCategoryStatusREST` enum mapping. |
| `LanguageCode` | `languageCode` | String | Nullable | N/A |
| `CategoryBidListType` | `categoryBidListType` | ContextualCategoryBidListTypeREST | Nullable | Returned for all categories except TTD contextual categories. See CustomCategory domain page `ContextualCategoryBidListTypeREST` enum mapping. |

## Code examples

### REST example

```
POST /v3/customcategory/rename HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "CustomCategoryId": "12345",
  "NewName": "Sports Enthusiasts Updated"
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation {
  customCategoryUpdate(
    input: {
      customCategoryId: "12345"
      customCategoryName: "Sports Enthusiasts Updated"
    }
  ) {
    data {
      customCategoryId
      customCategoryName
      keywordCount
      status
    }
    errors {
      ... on RestProxyMutationError {
        message
        field
      }
    }
  }
}
```
