# POST /v3/study/query → Query.conversionLiftProvider(conversionLiftProviderId:).conversionLiftStudies(first:, after:)

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-study-query
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/study/query → Query.conversionLiftProvider(conversionLiftProviderId:).conversionLiftStudies(first:, after:)

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/study/query` |
| GraphQL query | `Query.conversionLiftProvider(conversionLiftProviderId:).conversionLiftStudies(first:, after:)` |
| Return type | `ConversionLiftStudiesConnection` |

Also available: `Advertiser(id: "...").conversionLiftStudies(...)` when scoped to one advertiser. Default sort: `createdAt` descending (matches REST creation-date-desc ordering).

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `PageStartIndex` | `after` | String | Optional | N/A |
| `PageSize` | `first` | Int | Optional | N/A |
| N/A | `conversionLiftProviderId` (parent) | Int! | Required | No REST body field; select provider via parent `conversionLiftProvider(conversionLiftProviderId:)` (or scope via `Advertiser.conversionLiftStudies`). |

## Response field mapping

Row-level field mapping is identical to GET `/v3/study/{studyId}`—each node in `conversionLiftStudies.nodes` maps to `ConversionLiftStudy` fields. See the GET-by-ID endpoint doc for the full field table.

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [ConversionLiftStudy!] | Nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |

## Code examples

### REST example

```
POST /v3/study/query HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "PageStartIndex": 0,
  "PageSize": 50
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query ConversionLiftStudyList {
  conversionLiftProvider(conversionLiftProviderId: 3) {
    conversionLiftStudies(first: 50) {
      nodes {
        studyId
        name
        status
        createdAt
      }
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
}
```
