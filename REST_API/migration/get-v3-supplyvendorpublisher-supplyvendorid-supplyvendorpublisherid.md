# GET /v3/supplyvendorpublisher/{supplyVendorId}/{supplyVendorPublisherId} → SupplyVendor.publisher

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-supplyvendorpublisher-supplyvendorid-supplyvendorpublisherid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/supplyvendorpublisher/{supplyVendorId}/{supplyVendorPublisherId} → SupplyVendor.publisher

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/supplyvendorpublisher/{supplyVendorId}/{supplyVendorPublisherId}` |
| GraphQL query | `SupplyVendor.publisher(supplyVendorPublisherId:)` |
| Return type | `SupplyVendorPublisher` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `supplyVendorId` | Parent: `SupplyVendor.id` | ID! | Required | Path parameter identifying the parent supply vendor. Reach `SupplyVendor` via a parent query such as `partner(id:).supplyVendors` or `advertiser(id:).supplyVendors`. |
| `supplyVendorPublisherId` | Arg: `SupplyVendor.publisher(supplyVendorPublisherId:)` | ID! | Required | Path parameter passed as the `publisher` field argument. |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `SupplyVendorId` | `supplyVendorId` | Long! | Not nullable | Platform ID of the supply vendor. |
| `SupplyVendorPublisherId` | `supplyVendorPublisherId` | String! | Not nullable | Platform ID of the supply vendor publisher. |
| `SupplyVendorName` | `supplyVendor.name` | String! | Not nullable | Supply vendor display name via the `supplyVendor` relationship. |
| `SellerName` | `sellerName` | String | Nullable | Name of the seller. |
| `SellerDomain` | `sellerDomain` | String | Nullable | Domain of the seller. |

## Code examples

### REST example

```
GET /v3/supplyvendorpublisher/<supply-vendor-id>/<supply-vendor-publisher-id> HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query SupplyVendorPublisher {
  partner(id: "<partner-id>") {
    supplyVendors(first: 1) {
      nodes {
        publisher(supplyVendorPublisherId: "<supply-vendor-publisher-id>") {
          supplyVendorId
          supplyVendorPublisherId
          sellerName
          sellerDomain
          supplyVendor {
            name
          }
        }
      }
    }
  }
}
```
