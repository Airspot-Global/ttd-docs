# GET /v3/thirdpartydata/status/{providerId}/{providerElementId} → ThirdPartyDataProvider.taxonomyApprovalStatus

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-thirdpartydata-status-providerid-providerelementid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/thirdpartydata/status/{providerId}/{providerElementId} → ThirdPartyDataProvider.taxonomyApprovalStatus

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/thirdpartydata/status/{providerId}/{providerElementId}` |
| GraphQL query | `ThirdPartyDataProvider.taxonomyApprovalStatus` |
| Return type | `ThirdPartyDataTaxonomyApprovalStatus` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `providerId` | `ThirdPartyDataProvider(id:)` | N/A | Required | Parent lookup |
| `providerElementId` | `providerElementId` | String! | Required | Path parameter |

## Response field mapping

The REST response body is a bare `ThirdPartyDataTaxonomyApprovalStatus` enum scalar—there is no object wrapper and no pagination envelope. GraphQL exposes the same enum value on `ThirdPartyDataProvider.taxonomyApprovalStatus`.

## Code examples

### REST example

```
GET /v3/thirdpartydata/status/prov123/elem456 HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query TaxonomyApprovalStatus {
  thirdPartyDataProvider(id: "prov123") {
    taxonomyApprovalStatus(providerElementId: "elem456")
  }
}
```
