# PUT /v3/customcategory → customCategoryUpdate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/put-v3-customcategory
- Retrieved: 2026-11-14
- Category: REST_API

---

# PUT /v3/customcategory → customCategoryUpdate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `PUT /v3/customcategory` |
| GraphQL operation | `customCategoryUpdate` |
| Input type | `CustomCategoryUpdateInput` |
| Output type | `CustomCategoryUpdatePayload` (`data: CustomCategoryREST`, `errors: [CustomCategoryUpdateMutationError!]`) |

## Input field mapping

Input type: `CustomCategoryUpdateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `CustomCategoryId` | `customCategoryId` | ID! | Required | ID of the category to update. |
| `CustomCategoryName` | `customCategoryName` | String | Optional | Max 100 characters. |
| `CustomCategoryType` | `customCategoryType` | CustomCategoryTypeRESTInput | Optional | At least one of Keywords or CustomCategoryType must be provided. GraphQL enum values: `BLOCK`, `TARGET`, `UNSPECIFIED`. |
| `Keywords` | `keywords` | [CustomCategoryKeywordRESTInput!] | Optional | At least one of Keywords or CustomCategoryType must be provided. |
| `LanguageCode` | `languageCode` | String | Optional | N/A |
| `AdvertiserId` | `advertiserId` | ID | Optional | N/A |
| `PartnerId` | `partnerId` | ID | Optional | N/A |
| `Keywords.Value` | `keywords.value` | String! | Required | Alphanumeric, spaces, apostrophes only. Not case-sensitive. |
| `Keywords.MatchType` | `keywords.matchType` | KeywordMatchTypeRESTInput! | Required | GraphQL enum values: `EXACT_MATCH`, `EXACT_REQUIRED`, `EXACT_AVOID`. |
| `Keywords.MatchApplication` | `keywords.matchApplication` | KeywordMatchApplicationRESTInput! | Required | GraphQL enum values: `EXACT`, `SIMILAR`. |

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
PUT /v3/customcategory HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "CustomCategoryId": "12345",
  "Keywords": [
    {
      "Value": "basketball",
      "MatchType": "ExactMatch",
      "MatchApplication": "Exact"
    }
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
mutation {
  customCategoryUpdate(
    input: {
      customCategoryId: "12345"
      keywords: [
        {
          value: "basketball"
          matchType: EXACT_MATCH
          matchApplication: EXACT
        }
      ]
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
