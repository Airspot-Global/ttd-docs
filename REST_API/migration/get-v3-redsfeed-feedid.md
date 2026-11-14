# GET /v3/redsfeed/{feedId} → Query.redsFeedColumns

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-redsfeed-feedid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/redsfeed/{feedId} → Query.redsFeedColumns

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/redsfeed/{feedId}` |
| GraphQL query | `Query.redsFeedColumns(feedId:)` |
| Return type | `RedsFeedColumns` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `feedId` | `feedId` | ID! | Required | Feed identifier from the URL path. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Columns` | `columns` | [REDSColumnItem!]! | Not nullable | See nested type table. |
| `Columns[].ColumnName` | `columns { columnName }` | String | Nullable | N/A |
| `Columns[].Description` | `columns { description }` | String | Nullable | N/A |
| `Columns[].Facet` | `columns { facet }` | String | Nullable | N/A |

## Endpoint-specific nested types and enums

### columns (REDSColumnItem)

| REST field | GraphQL field | GraphQL type | Notes |
| --- | --- | --- | --- |
| `ColumnName` | `columnName` | String | N/A |
| `Description` | `description` | String | N/A |
| `Facet` | `facet` | String | N/A |

## Code examples

### REST example

```
GET /v3/redsfeed/<feed-id> HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query RedsFeedColumns {
  redsFeedColumns(feedId: "<example-feed-id>") {
    columns {
      columnName
      description
      facet
    }
  }
}
```
