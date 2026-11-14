# POST /v3/customcategory → customCategoryCreate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-customcategory
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/customcategory → customCategoryCreate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/customcategory` |
| GraphQL operation | `customCategoryCreate` |
| Input type | `CustomCategoryCreateInput` |
| Output type | `CustomCategoryCreatePayload` (`data: CustomCategoryREST`, `errors: [CustomCategoryCreateMutationError!]`) |

## Input field mapping

Input type: `CustomCategoryCreateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `CustomCategoryId` | N/A | N/A | Optional | Invalid on create—ignored if sent. Server assigns ID in response. |
| `CustomCategoryName` | `customCategoryName` | String | Required | Required on create. Max 100 characters. |
| `CustomCategoryType` | `customCategoryType` | CustomCategoryTypeRESTInput | Required | Required for TTD contextual categories. Cannot be changed after create. GraphQL enum values: `BLOCK`, `TARGET`, `UNSPECIFIED`. |
| `Keywords` | `keywords` | [CustomCategoryKeywordRESTInput!] | Required | At least one ExactMatch keyword required. Max 5 ExactRequired. Max 5,000 total. |
| `LanguageCode` | `languageCode` | String | Optional | Required if any keyword uses MatchApplication=Similar. |
| `AdvertiserId` | `advertiserId` | ID | Optional | Either AdvertiserId or PartnerId must be provided. |
| `PartnerId` | `partnerId` | ID | Optional | Either AdvertiserId or PartnerId must be provided. |
| `Keywords.Value` | `keywords.value` | String! | Required | Alphanumeric, spaces, apostrophes only. Not case-sensitive. |
| `Keywords.MatchType` | `keywords.matchType` | KeywordMatchTypeRESTInput! | Required | GraphQL enum values: `EXACT_MATCH`, `EXACT_REQUIRED`, `EXACT_AVOID`. |
| `Keywords.MatchApplication` | `keywords.matchApplication` | KeywordMatchApplicationRESTInput! | Required | GraphQL enum values: `EXACT`, `SIMILAR`. |

## Output field mapping

Output type: `CustomCategoryREST` (returned as `data` on `CustomCategoryCreatePayload`)

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

## Endpoint-specific nested types and enums

### CustomCategoryTypeRESTInput

GraphQL input enum values: `BLOCK`, `TARGET`, `UNSPECIFIED`

### KeywordMatchTypeRESTInput

GraphQL input enum values: `EXACT_MATCH`, `EXACT_REQUIRED`, `EXACT_AVOID`

### KeywordMatchApplicationRESTInput

GraphQL input enum values: `EXACT`, `SIMILAR`

## Code examples

### REST example

```
POST /v3/customcategory HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "CustomCategoryName": "Sports Enthusiasts",
  "CustomCategoryType": "Target",
  "PartnerId": "prt123abc",
  "Keywords": [
    {
      "Value": "football",
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
  customCategoryCreate(
    input: {
      customCategoryName: "Sports Enthusiasts"
      customCategoryType: TARGET
      partnerId: "prt123abc"
      keywords: [
        {
          value: "football"
          matchType: EXACT_MATCH
          matchApplication: EXACT
        }
      ]
    }
  ) {
    data {
      customCategoryId
      customCategoryName
      customCategoryType
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
