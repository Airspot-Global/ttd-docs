# POST /v3/language/query → Query.ttdLanguages / Query.peer39Languages

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-language-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/language/query → Query.ttdLanguages / Query.peer39Languages

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/language/query` |
| GraphQL query | `Query.ttdLanguages`, `Query.peer39Languages` |
| Return type | `TtdLanguagesConnection`, `Peer39LanguagesConnection` |

## Multi-step operations

One REST paged language query maps to two top-level GraphQL connections, selected by REST `LanguageSourceType` instead of a filter input:

| REST `LanguageSourceType` | GraphQL query | GraphQL node type |
| --- | --- | --- |
| `Default` (or omitted) | `Query.ttdLanguages` | `TTDLanguage` |
| `Peer39SiteLanguage` | `Query.peer39Languages` | `Peer39Language` |

Both connections support `first`/`after`/`last`/`before`, `where` filter inputs, and `order` sort inputs. Default sort is by `name` ascending (matches REST default of `Name` ascending).

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |
| `LanguageSourceType` | (query selection) | N/A | Optional | Choose `ttdLanguages` vs `peer39Languages` instead of a filter input. |
| `SortFields` | `order` | `[TTDLanguageSortInput!]` or `[Peer39LanguageSortInput!]` | Optional | REST `FieldId: Name` → `order: [{ name: ASC }]`. |
| `SortFields[].FieldId` | `order[].name` | SortEnumType | Required | REST `Name` → `name`. |
| `SortFields[].Ascending` | `order[].*` value | SortEnumType | Optional | `true` → `ASC`; `false` → `DESC`. |

### GraphQL-only filters (no REST POST equivalent)

| GraphQL argument | GraphQL type | Notes |
| --- | --- | --- |
| `where.id` | `StringIdOperationFilterInput` | Filter by language ID. |
| `where.name` | `StringOperationFilterInput` | Filter by display name. |
| `where.languageCode` | `StringOperationFilterInput` | Filter by language code. |

## Response field mapping

 | REST response field | GraphQL field | GraphQL type | Nullable | Notes | |---------------------|---------------|--------------|----------|-------| | `Result` | `nodes` | `[TTDLanguage!]` or `[Peer39Language!]` | Nullable | N/A | | `ResultCount` | N/A | N/A | N/A | N/A | | `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A | | `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |

### Default catalog (`LanguageSourceType: default` → `Query.ttdLanguages` → `TTDLanguage`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Id` | `id` | ID! | Not nullable | N/A |
| `Name` | `name` | String! | Not nullable | Display name. |
| `Code` | `languageCode` | String! | Not nullable | ISO 639-1 code. GraphQL field name is `languageCode`, not REST `Code`. |

### Peer39 catalog (`LanguageSourceType: Peer39SiteLanguage` → `Query.peer39Languages` → `Peer39Language`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Id` | `id` | ID! | Not nullable | Ids typically in the `1000–1499` range. |
| `Name` | `name` | String! | Not nullable | Display names omit the `Peer39_` prefix from provisioning names (e.g. `Peer39_English` → `English`). |
| `Code` | `languageCode` | String! | Not nullable | Peer39-specific code (e.g. `peer39-lang-en`). |

## Code examples

The following are examples of querying the default TTD language catalog and the Peer39 site-language catalog.

### REST example (Default)

```
POST /v3/language/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "PageStartIndex": 0,
  "PageSize": 25,
  "LanguageSourceType": "Default",
  "SortFields": [{ "FieldId": "Name", "Ascending": true }]
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query TtdLanguages {
  ttdLanguages(
    first: 25
    order: [{ name: ASC }]
  ) {
    nodes {
      id
      name
      languageCode
    }
    totalCount
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

### REST example (Peer39SiteLanguage)

```
POST /v3/language/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "PageStartIndex": 0,
  "PageSize": 25,
  "LanguageSourceType": "Peer39SiteLanguage",
  "SortFields": [{ "FieldId": "Name", "Ascending": true }]
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query Peer39Languages {
  peer39Languages(
    first: 25
    order: [{ name: ASC }]
  ) {
    nodes {
      id
      name
      languageCode
    }
    totalCount
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```
