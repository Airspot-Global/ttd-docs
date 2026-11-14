# GET /v3/customcategory/ttd/languages → Query.customCategoryLanguages

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-customcategory-ttd-languages
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/customcategory/ttd/languages → Query.customCategoryLanguages

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/customcategory/ttd/languages` |
| GraphQL query | `Query.customCategoryLanguages` |
| Return type | `[CustomCategoryLanguage!]!` |

## Response field mapping

REST returns a top-level JSON array of `CustomCategoryLanguage` objects.

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| _(top-level array)_ | `customCategoryLanguages` | [CustomCategoryLanguage!]! | Not nullable | Top-level query field; select fields directly on each element. |
| `LanguageCode` | `code` | String! | Not nullable | N/A |
| `LanguageName` | `name` | String! | Not nullable | N/A |

## Endpoint-specific nested types and enums

### CustomCategoryLanguage

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `LanguageCode` | `code` | String! | Not nullable | N/A |
| `LanguageName` | `name` | String! | Not nullable | N/A |

## Code examples

### REST example

```
GET /v3/customcategory/ttd/languages HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query Languages {
  customCategoryLanguages {
    code
    name
  }
}
```
