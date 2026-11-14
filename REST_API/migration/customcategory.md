# Custom category: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/customcategory-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Custom category: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/customcategory/{customCategoryId}` | `Query.customCategory(id:)` | Full category detail including keywords |
| `GET /v3/customcategory/advertiser/{advertiserId}` | `Advertiser.customCategories` | Summary list for an advertiser |
| `POST /v3/customcategory/query` | `Query.customCategories(input:)` | Query filtered by source type and advertiser or partner |
| `GET /v3/customcategory/name/{customCategoryId}` | `Query.customCategory(id:)` | Lightweight ID/name via `id` and `customCategoryName` |
| `GET /v3/customcategory/ttd/languages` | `Query.customCategoryLanguages` | TTD contextual language catalog |
| `POST /v3/customcategory` | `customCategoryCreate` | Create TTD contextual custom category |
| `PUT /v3/customcategory` | `customCategoryUpdate` | Update custom category keywords, type, or metadata |
| `POST /v3/customcategory/rename` | `customCategoryUpdate` | Rename via update, setting only `customCategoryId` and `customCategoryName` |
| `DELETE /v3/customcategory/{customCategoryId}` | N/A | Not currently available in GraphQL |

## Shared nested types and enums

### CustomCategoryKeyword

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Value` | `value` | String! | Not nullable | N/A |
| `MatchType` | `matchType` | KeywordMatchType! | Not nullable | N/A |
| `MatchApplication` | `matchApplication` | KeywordMatchApplication! | Not nullable | N/A |

### CustomCategoryKeywordRESTInput

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `Value` | `value` | String! | Required | Alphanumeric, spaces, apostrophes only. Not case-sensitive. |
| `MatchType` | `matchType` | KeywordMatchTypeRESTInput! | Required | GraphQL enum values: `EXACT_MATCH`, `EXACT_REQUIRED`, `EXACT_AVOID`. |
| `MatchApplication` | `matchApplication` | KeywordMatchApplicationRESTInput! | Required | GraphQL enum values: `EXACT`, `SIMILAR`. |

### CustomCategoryTypeRESTInput

GraphQL enum values: `BLOCK`, `TARGET`, `UNSPECIFIED`

### CustomCategoryTypeREST

GraphQL enum values: `BLOCK`, `TARGET`, `UNSPECIFIED`

### KeywordMatchTypeRESTInput

GraphQL enum values: `EXACT_MATCH`, `EXACT_REQUIRED`, `EXACT_AVOID`

### KeywordMatchApplicationRESTInput

GraphQL enum values: `EXACT`, `SIMILAR`

### CustomCategoryStatusREST

| REST value | GraphQL value |
| --- | --- |
| `NotReady` | `NOT_READY` |
| `Live` | `LIVE` |
| `Unusable` | `UNUSABLE` |

### ContextualCategoryBidListTypeREST

| REST value | GraphQL value |
| --- | --- |
| `Both` | `BOTH` |
| `Block` | `BLOCK` |
| `Target` | `TARGET` |
