# CRMData: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/crmdata-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# CRMData: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/crmdata/segment/{advertiserId}/{crmDataId}` | `Advertiser.crmDataSegmentStatus` | N/A |
| `GET /v3/crmdata/{segmentType}/segment/{advertiserId}/{crmDataId}` | `Advertiser.crmDataSegmentStatus` | REST path uses `targeting`, `npi`, or `conversion`; pass matching `segmentType` arg |
| `GET /v3/crmdata/segment/{advertiserId}` | `Advertiser.crmDataSegments` | N/A |
| `GET /v3/crmdata/segment/{advertiserId}/{crmDataId}/{referenceId}` | `Query.crmDataDropStatus` | N/A |
| `GET /v3/crmdata/{segmentType}/segment/{advertiserId}/{crmDataId}/{referenceId}` | `Query.crmDataDropStatus` | REST path uses `targeting`, `npi`, or `conversion`; pass matching `segmentType` arg |

## Shared nested types and enums

### SegmentType

| REST path value | REST enum | GraphQL enum |
| --- | --- | --- |
| `targeting` | Targeting | `TARGETING` |
| `npi` | TargetingNPI | `TARGETING_NPI` |
| `conversion` | Conversion | `CONVERSION` |
| N/A | N/A | `TARGETING_DIRECT_IP` |

### CrmDataDropInfo

REST `PiiTypes` (all types declared in the drop) is **Not currently available in GraphQL**—the graph exposes only singular `piiType` (first declared type).
