# GET /v3/overview/partner/{partnerId} → Query.partner(id:)

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-overview-partner-partnerid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/overview/partner/{partnerId} → Query.partner(id:)

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/overview/partner/{partnerId}` |
| GraphQL query | `Query.partner(id:)` |
| Return type | `Partner` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `partnerId` | `partner(id: $partnerId)` | ID! | Required | Root query argument. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `PartnerId` | `id` | ID! | Not nullable | N/A |
| `PartnerName` | `name` | String! | Not nullable | N/A |
| `Advertisers` | `advertisers` | AdvertisersConnection | Nullable | REST unpaged list → Connection; paginate with `first`/`after`. Nested fields under `advertisers { nodes { … } }`; see AdvertiserOverview on the Overview domain page. |

## Code examples

### REST example

```
GET /v3/overview/partner/{partnerId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query PartnerOverview($partnerId: ID!) {
  partner(id: $partnerId) {
    id
    name
    advertisers(first: 100) {
      nodes {
        id
        name
        description
        campaigns(first: 100, where: { isArchived: { eq: false } }) {
          nodes {
            id
            name
            description
            startDate
            endDate
            isArchived
            adGroups(first: 100, where: { isArchived: { eq: false } }) {
              nodes {
                id
                name
                description
                isEnabled
                isArchived
                creatives(first: 100) {
                  nodes { id name description }
                }
              }
            }
          }
        }
        creatives(first: 100) {
          nodes { id name description }
        }
      }
    }
  }
}
```
