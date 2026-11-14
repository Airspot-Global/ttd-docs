# POST /v3/redsfeed/query → Partner.redsFeeds

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-redsfeed-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/redsfeed/query → Partner.redsFeeds

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/redsfeed/query` |
| GraphQL query | `Partner.redsFeeds` |
| Return type | `RedsFeedsConnection` |

## Multi-step operations

This REST endpoint is exposed as a relationship field on `Partner`, not as a root query. Resolve the target partner with `Query.partner(id:)` before calling `redsFeeds`. REST `PartnerId` in the request body defaults to the user's primary partner when omitted; in GraphQL, pass the partner ID to `Query.partner(id:)`.

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PartnerId` | `Query.partner(id:)` | ID! | Optional | Defaults to primary partner in REST; GraphQL requires an explicit partner ID on `Query.partner`. |
| `SearchTerms` | `filter.searchTerms` | [String!] | Optional | N/A |
| `SortFields` | `filter.sortFields` | [RedsFeedSortingFieldSortingInput!] | Optional | Optional sort specification; see nested types below. |
| `SortFields[].FieldId` | `filter.sortFields.fieldId` | RedsFeedSortingFieldInput! | Required | N/A |
| `SortFields[].Ascending` | `filter.sortFields.ascending` | Boolean | Optional | Defaults to `true` when omitted. |
| `PageStartIndex` | `filter.pageStartIndex` | Int! | Required | N/A |
| `PageSize` | `filter.pageSize` | Int! | Required | N/A |
| N/A | `first` | Int | Optional | GraphQL-only page size on `redsFeeds`. |
| N/A | `after` | String | Optional | GraphQL-only continuation cursor. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [RedsFeedMetaDataModel!] | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |
| `Result[].FeedId` | `nodes.feedId` | ID | Nullable | N/A |
| `Result[].FeedType` | `nodes.feedType` | RedsFeedType! | Not nullable | N/A |
| `Result[].PartnerId` | `nodes.partnerId` | ID | Nullable | N/A |
| `Result[].AdvertiserIds` | `nodes.advertiserIds` | [String!] | Nullable | N/A |
| `Result[].Description` | `nodes.description` | String | Nullable | N/A |
| `Result[].HeaderIncluded` | `nodes.headerIncluded` | Boolean! | Not nullable | N/A |
| `Result[].GdprConsentHandlingType` | `nodes.gdprConsentHandlingType` | String | Nullable | N/A |
| `Result[].DestinationType` | `nodes.destinationType` | RedsFeedDestinationType! | Not nullable | N/A |
| `Result[].ConcatenationEnabled` | `nodes.concatenationEnabled` | Boolean! | Not nullable | N/A |
| `Result[].RawDestinationS3Key` | `nodes.rawDestinationS3Key` | String | Nullable | N/A |
| `Result[].ConcatenatedDestinationS3Key` | `nodes.concatenatedDestinationS3Key` | String | Nullable | N/A |
| `Result[].SnowflakeShare` | `nodes.snowflakeShare` | RedsFeedSnowflakeShareModel | Nullable | See nested type table. |
| `Result[].Columns` | `nodes.columns` | [REDSColumnItem!] | Nullable | See nested type table. |

## Endpoint-specific nested types and enums

### RedsFeedSortingFieldInput

| REST value | GraphQL enum value | Notes |
| --- | --- | --- |
| `FeedId` | `FEED_ID` | Default sort when `sortFields` is omitted. |

### REDSColumnItem (on RedsFeedMetaDataModel.columns)

| REST field | GraphQL field | GraphQL type | Notes |
| --- | --- | --- | --- |
| `ColumnName` | `columnName` | String | N/A |
| `Description` | `description` | String | N/A |
| `Facet` | `facet` | String | N/A |

### RedsFeedSnowflakeShareModel (on RedsFeedMetaDataModel.snowflakeShare)

| REST field | GraphQL field | GraphQL type | Notes |
| --- | --- | --- | --- |
| `ShareName` | `shareName` | String | N/A |
| `ShareDescription` | `shareDescription` | String | N/A |
| `RegionName` | `regionName` | String | N/A |
| `RegionDescription` | `regionDescription` | String | N/A |
| `AccountName` | `accountName` | String | N/A |

## Code examples

### REST example

```
POST /v3/redsfeed/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "SearchTerms": [],
  "SortFields": [],
  "PageStartIndex": 0,
  "PageSize": 100
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query RedsFeeds {
  partner(id: "<partner-id>") {
    redsFeeds(
      first: 100
      filter: {
        pageStartIndex: 0
        pageSize: 100
        searchTerms: []
        sortFields: [{ fieldId: FEED_ID, ascending: true }]
      }
    ) {
      nodes {
        feedId
        feedType
        partnerId
        advertiserIds
        description
        headerIncluded
        destinationType
        concatenationEnabled
        columns {
          columnName
          description
          facet
        }
        snowflakeShare {
          shareName
          shareDescription
          regionName
        }
      }
      totalCount
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
}
```
