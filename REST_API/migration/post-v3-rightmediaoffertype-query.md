# POST /v3/rightmediaoffertype/query → Advertiser.rightMediaOfferTypes

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-rightmediaoffertype-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/rightmediaoffertype/query → Advertiser.rightMediaOfferTypes

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/rightmediaoffertype/query` |
| GraphQL query | `Advertiser.rightMediaOfferTypes` |
| Return type | `[RightMediaOfferType]!` |

REST `POST /v3/rightmediaoffertype/query` is a global paginated query with search, sort, and page-count fields. GraphQL exposes an advertiser-scoped plain list via `Advertiser.rightMediaOfferTypes` with no pagination, search, or sort arguments. Query through a parent `Advertiser` (requires `Advertiser.id`). The list type is `[RightMediaOfferType]!`—the list is non-null but individual elements may be null.

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PageStartIndex` | N/A | N/A | Optional | N/A |
| `PageSize` | N/A | N/A | Optional | N/A |
| `SearchTerms` | N/A | N/A | Optional | Not currently available in GraphQL |
| `SortFields` | N/A | N/A | Optional | Not currently available in GraphQL |
| `SortFields[].FieldId` | N/A | N/A | Required | Not currently available in GraphQL |
| `SortFields[].Ascending` | N/A | N/A | Optional | Not currently available in GraphQL |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `Advertiser.rightMediaOfferTypes` | [RightMediaOfferType]! | Not nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | N/A | N/A | N/A | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].RightMediaOfferTypeId` | `RightMediaOfferType.id` | ID! | Not nullable | `long` → `ID` (string). |
| `Result[].RightMediaOfferTypeName` | `RightMediaOfferType.name` | String! | Not nullable | Offer type display name. |

## Endpoint-specific nested types and enums

### RightMediaOfferType

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `RightMediaOfferTypeId` | `id` | ID! | Not nullable | `long` → `ID` (string). |
| `RightMediaOfferTypeName` | `name` | String! | Not nullable | Offer type display name. |

### RightMediaOfferTypeSortingField

REST enum used in `SortFields[].FieldId`. Values: `Name`. **Not currently available in GraphQL** on `Advertiser.rightMediaOfferTypes`.

## Code examples

### REST example

```
POST /v3/rightmediaoffertype/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "SearchTerms": ["display"],
  "PageStartIndex": 0,
  "PageSize": 20,
  "SortFields": [
    {
      "FieldId": "Name",
      "Ascending": true
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
query AdvertiserRightMediaOfferTypes {
  advertiser(id: "abc123") {
    rightMediaOfferTypes {
      id
      name
    }
  }
}
```
