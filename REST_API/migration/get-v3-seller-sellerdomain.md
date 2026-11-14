# GET /v3/seller/{sellerDomain} → Query.publishers(where:)

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-seller-sellerdomain
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/seller/{sellerDomain} → Query.publishers(where:)

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/seller/{sellerDomain}` |
| GraphQL query | `Query.publishers(where:)` |
| Return type | `Publisher` |

## Multi-step operations

| REST field group | GraphQL placement | Notes |
| --- | --- | --- |
| `SellerDomain`, `SellerName` | `Publisher.domain`, `Publisher.name` | `Publisher` fields. |
| `IsTargetable`, `SellerStatus`, `AliasToSellerDomain`, `SellerDomainAliases` | `Publisher.isTargetable`, `Publisher.sellerStatus`, `Publisher.aliasToSellerDomain`, `Publisher.sellerDomainAliases` | Seller metadata fields backed by this GET. |

Resolve a seller by domain via `Query.publishers(where: { publisherDomain: { eq: sellerDomain } })` and select the fields on the matching `Publisher` node.

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| sellerDomain (path) | `Query.publishers(where: { publisherDomain: { eq: } })` | String | Required | REST path parameter; filter publishers by domain. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `SellerDomain` | `domain` | String! | Not nullable | Same underlying seller domain. |
| `SellerName` | `name` | String! | Not nullable | Seller display name. |
| `AliasToSellerDomain` | `aliasToSellerDomain` | String | Nullable | Domain this seller aliases to, if any. |
| `SellerDomainAliases` | `sellerDomainAliases` | [String!]! | Not nullable | List of domain aliases; may be empty. |
| `SellerStatus` | `sellerStatus` | SellerStatus | Nullable | `Allowed`/`Disallowed` → `ALLOWED`/`DISALLOWED`. |
| `IsTargetable` | `isTargetable` | Boolean | Nullable | Whether the seller domain is targetable for bidding. |

## Endpoint-specific nested types and enums

### SellerStatus

| REST value | GraphQL value |
| --- | --- |
| `Allowed` | `ALLOWED` |
| `Disallowed` | `DISALLOWED` |

## Code examples

### REST example

```
GET /v3/seller/{sellerDomain} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query SellerByDomain($domain: String!) {
  publishers(first: 1, where: { publisherDomain: { eq: $domain } }) {
    nodes {
      id
      domain
      name
      isTargetable
      sellerStatus
      aliasToSellerDomain
      sellerDomainAliases
    }
  }
}
```
