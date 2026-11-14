# POST /v3/label/query/partner → Query.customLabels

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-label-query-partner
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/label/query/partner → Query.customLabels

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/label/query/partner` |
| GraphQL query | `Query.customLabels(input: CustomLabelsFilterInput!)` |
| Return type | `CustomLabelsConnection` |

> **Semantic note:** REST returns the partner's full label catalog. The GraphQL query `Query.customLabels` returns labels **assigned to entities** of the given `entityType` within scope—not a drop-in semantic match.

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `SearchTerms` | searchTerm (`CustomLabelsFilterInput`) | String | Optional | REST accepts zero or more search terms (OR match on label name). GraphQL accepts one optional `searchTerm` with contains semantics. |
| `PartnerId` | partnerId (`CustomLabelsFilterInput`) | ID | Optional | REST defaults to the user's primary partner when omitted. GraphQL requires exactly one scope arg (`partnerId`, `advertiserId`, or `campaignId`) together with `entityType`. |
| N/A | entityType (`CustomLabelsFilterInput`) | CustomLabelEntityTypeInput! | Required | GraphQL-only required filter (`ADVERTISER` \| `CAMPAIGN` \| `AD_GROUP`). REST partner query returns all labels in the partner catalog; GraphQL query returns labels assigned to entities of `entityType` within the given scope. |
| N/A | advertiserId (`CustomLabelsFilterInput`) | ID | Optional | GraphQL-only scope alternative to `partnerId`; not applicable to this REST endpoint. |
| N/A | campaignId (`CustomLabelsFilterInput`) | ID | Optional | GraphQL-only scope alternative to `partnerId`; not applicable to this REST endpoint. |
| N/A | `first` (`Query.customLabels`) | Int | Optional | GraphQL-only; REST returns a full unpaged list. |
| N/A | `after` (`Query.customLabels`) | String | Optional | GraphQL-only; no REST equivalent. |
| N/A | before (`Query.customLabels`) | String | Optional | GraphQL-only; no REST equivalent. |
| N/A | last (`Query.customLabels`) | Int | Optional | GraphQL-only; no REST equivalent. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `Result` | `nodes` | [CustomLabel!] | Nullable | N/A |
| `Result[].CustomLabelId` | id (on `CustomLabel`) | ID! | Not nullable | N/A |
| `Result[].LabelName` | name (on `CustomLabel`) | String! | Not nullable | REST `LabelName` maps to GraphQL `name`. |
| `Result[].PartnerId` | `partner` (on `CustomLabel`) | Partner | Nullable | Entity reference; select `partner { id }` for the identifier. |
| `ResultCount` | N/A | N/A | N/A | N/A |
| `TotalFilteredCount` | `totalCount` | Int! | Not nullable | N/A |
| `TotalUnfilteredCount` | N/A | N/A | N/A | N/A |

## Code examples

### REST example

```
POST /v3/label/query/partner HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "PartnerId": "abc123",
  "SearchTerms": ["promo"]
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query CustomLabelsForPartner {
  customLabels(
    input: {
      entityType: ADVERTISER
      partnerId: "abc123"
      searchTerm: "promo"
    }
    first: 10
  ) {
    totalCount
    nodes {
      id
      name
      partner {
        id
      }
    }
  }
}
```
