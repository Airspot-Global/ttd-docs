# Supply path optimization list: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/supplypathoptimizationlist-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Supply path optimization list: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/supplypathoptimizationlist/{supplypathoptimizationlistid}` | `supplyPathOptimizationList(id:)` | Summary scalars only; list items not included |
| `GET /v3/supplypathoptimizationlist/detail/{supplypathoptimizationlistid}` | `SupplyPathOptimizationList.items` | Full list items collection; same scalars as summary when combined in one query |
| `POST /v3/supplypathoptimizationlist/query/advertiser` | `Advertiser.supplyPathOptimizationLists` | N/A |
| `POST /v3/supplypathoptimizationlist/query/partner` | `Partner.supplyPathOptimizationLists` | N/A |

## Shared nested types and enums

### SupplyPathOptimizationListFilterInput

| Enum value | Notes |
| --- | --- |
| `ADVERTISER_ONLY` | N/A |
| `PARTNER_ONLY` | N/A |
| `GLOBAL_ONLY` | N/A |
| `ALL` | N/A |

### MediaType

| Enum value | Notes |
| --- | --- |
| `Display` | N/A |
| `Video` | N/A |
| `Native` | N/A |
| `Audio` | N/A |
| `NativeVideo` | N/A |

GraphQL also defines `UNKNOWN` on `MediaType`; it is not a member of the REST `MediaType` enum for this domain.
