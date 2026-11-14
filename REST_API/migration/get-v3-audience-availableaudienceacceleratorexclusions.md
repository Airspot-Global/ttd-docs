# GET /v3/audience/availableaudienceacceleratorexclusions → Query.availableAudienceAcceleratorExclusions

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-audience-availableaudienceacceleratorexclusions
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/audience/availableaudienceacceleratorexclusions → Query.availableAudienceAcceleratorExclusions

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/audience/availableaudienceacceleratorexclusions` |
| GraphQL query | `Query.availableAudienceAcceleratorExclusions` |
| Return type | `AvailableAudienceAcceleratorExclusionsConnection` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| N/A | `first` | Int | Optional | GraphQL-only; REST returns the full list in one response. |
| N/A | `after` | String | Optional | GraphQL-only; REST returns the full list in one response. |
| N/A | `searchTerm` | String | Optional | Text search on third-party data name. |
| N/A | `where` | ThirdPartyDataFilterInput | Optional | Structured filtering. |
| N/A | `order` | [ThirdPartyDataSortInput!] | Optional | Sort order. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [ThirdPartyData!] | Nullable | N/A |
| `Result.ThirdPartyDataId` | `nodes.id` | ID! | Not nullable | Each node is `ThirdPartyData`. |
| `Result.Name` | `nodes.name` | String! | Not nullable | N/A |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |

## Code examples

### REST example

```
GET /v3/audience/availableaudienceacceleratorexclusions HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query AvailableExclusions {
  availableAudienceAcceleratorExclusions(first: 25) {
    nodes {
      id
      name
    }
    totalCount
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```
