# GET /v3/crmdata/{segmentType}/segment/{advertiserId}/{crmDataId} → Advertiser.crmDataSegmentStatus

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-crmdata-segmenttype-segment-advertiserid-crmdataid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/crmdata/{segmentType}/segment/{advertiserId}/{crmDataId} → Advertiser.crmDataSegmentStatus

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/crmdata/{segmentType}/segment/{advertiserId}/{crmDataId}` |
| GraphQL query | `Advertiser.crmDataSegmentStatus` |
| Return type | `CrmDataSegmentStatus` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `advertiserId` | (parent—Advertiser.id) | ID! | Required | Path parameter; resolved via parent Advertiser, not a public arg on `crmDataSegmentStatus`. |
| `crmDataId` | `crmDataId` | ID! | Required | Required resolver arg on Advertiser.`crmDataSegmentStatus`. |
| `segmentType` | `segmentType` | SegmentTypeInput | Required | Required REST path parameter. Valid path values: `targeting`, `npi`, `conversion` (see SegmentTypeInput). |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | (parent—Advertiser.id) | ID! | Not nullable | Omitted from CrmDataSegmentStatus; available from parent Advertiser. |
| `CrmDataId` | (CrmDataSegment.id) | ID! | Not nullable | Omitted from CrmDataSegmentStatus; available via `crmDataId` arg or `crmDataSegment`(id:) query. |
| `SegmentName` | (CrmDataSegment.name) | String! | Not nullable | Omitted from CrmDataSegmentStatus; available on CrmDataSegment.name. |
| `FirstPartyDataId` | `firstPartyDataId` | ID | Nullable | N/A |
| `ActiveIds` | `activeIds` | Long | Nullable | N/A |
| `ReceivedIds` | `receivedIds` | Long | Nullable | N/A |
| `LastUpdatedAt` | `lastUpdatedAt` | DateTime | Nullable | N/A |
| `Region` | (CrmDataSegment.region) | CrmDataRegion! | Not nullable | Omitted from CrmDataSegmentStatus; available on CrmDataSegment.region. |
| `SegmentType` | `segmentType` | SegmentType! | Not nullable | REST enum Targeting/TargetingNPI/Conversion maps to GraphQL SegmentType (TargetingNpi in schema). |
| `LatestActivatedDrop.State` | `latestActivatedDrop.state` | CrmDataDropState! | Not nullable | N/A |
| `LatestActivatedDrop.PiiType` | `latestActivatedDrop.piiType` | CrmDataPiiType! | Not nullable | REST field deprecated 2026-10-04; maps single PiiType only. |
| `LatestActivatedDrop.PiiTypes` | `latestActivatedDrop.piiType` | CrmDataPiiType! | Not nullable | Not currently available in GraphQL |
| `LatestActivatedDrop.MergeMode` | `latestActivatedDrop.mergeMode` | MergeMode! | Not nullable | N/A |
| `LatestActivatedDrop.SegmentType` | `latestActivatedDrop.segmentType` | SegmentType! | Not nullable | N/A |
| `LatestActivatedDrop.TtlInMinutes` | `latestActivatedDrop.ttlInMinutes` | Long! | Not nullable | N/A |
| `LatestActivatedDrop.RetentionEnabled` | `latestActivatedDrop.retentionEnabled` | Boolean! | Not nullable | N/A |
| `LatestActivatedDrop.RetentionRemainingInDays` | `latestActivatedDrop.retentionRemainingInDays` | Long! | Not nullable | N/A |
| `LatestActivatedDrop.CreatedAt` | `latestActivatedDrop.createdAt` | DateTime | Nullable | N/A |
| `LatestActivatedDrop.PiiUploadedAt` | `latestActivatedDrop.piiUploadedAt` | DateTime | Nullable | N/A |
| `LatestActivatedDrop.ProcessingAt` | `latestActivatedDrop.processingAt` | DateTime | Nullable | N/A |
| `LatestActivatedDrop.IngestedAt` | `latestActivatedDrop.ingestedAt` | DateTime | Nullable | N/A |
| `LatestActivatedDrop.SucceededAt` | `latestActivatedDrop.succeededAt` | DateTime | Nullable | N/A |
| `LatestActivatedDrop.CancelledAt` | `latestActivatedDrop.cancelledAt` | DateTime | Nullable | N/A |
| `LatestActivatedDrop.FailedAt` | `latestActivatedDrop.failedAt` | DateTime | Nullable | N/A |
| `LatestActivatedDrop.FailureMessage` | `latestActivatedDrop.failureMessage` | String | Nullable | N/A |
| `LatestActivatedDrop.ReceiptFileUrl` | `latestActivatedDrop.receiptFileUrl` | String | Nullable | N/A |
| `LatestActivatedDrop.Statistics.TotalRecords` | `latestActivatedDrop.statistics.totalRecords` | Long | Nullable | N/A |
| `LatestActivatedDrop.Statistics.ValidRecords` | `latestActivatedDrop.statistics.validRecords` | Long | Nullable | N/A |
| `LatestActivatedDrop.Statistics.UniqueIdDeficit` | `latestActivatedDrop.statistics.uniqueIdDeficit` | Long | Nullable | N/A |
| `LatestActivatedDrop.Statistics.SucceededRecords` | `latestActivatedDrop.statistics.succeededRecords` | Long | Nullable | N/A |
| `LatestActivatedDrop.Statistics.FailedRecords` | `latestActivatedDrop.statistics.failedRecords` | Long | Nullable | N/A |
| `LatestActivatedDrop.Statistics.EmptyRecords` | `latestActivatedDrop.statistics.emptyRecords` | Long | Nullable | N/A |
| `LatestActivatedDrop.Statistics.EmailRecordsNotInAcceptedEmailDomain` | `latestActivatedDrop.statistics.emailRecordsNotInAcceptedEmailDomain` | Long | Nullable | N/A |
| `LatestActivatedDrop.Statistics.EmailHashRecordsNotBase64EncodedSha256` | `latestActivatedDrop.statistics.emailHashRecordsNotBase64EncodedSha256` | Long | Nullable | N/A |
| `LatestActivatedDrop.Statistics.EmailInvalidFormat` | `latestActivatedDrop.statistics.emailInvalidFormat` | Long | Nullable | N/A |
| `LatestActivatedDrop.Statistics.IngestedInvalidCsvFormat` | `latestActivatedDrop.statistics.ingestedInvalidCsvFormat` | Long | Nullable | N/A |
| `LatestActivatedDrop.Statistics.IngestedRecords` | `latestActivatedDrop.statistics.ingestedRecords` | Long | Nullable | N/A |

## Endpoint-specific nested types and enums

### SegmentTypeInput

The `segmentType` resolver argument uses `SegmentTypeInput`. The `{segmentType}` URL path accepts lowercase values only; NPI segments use `npi`, not `targetingnpi` or `TargetingNPI`.

| REST path value | REST enum | GraphQL enum |
| --- | --- | --- |
| `targeting` | Targeting | `TARGETING` |
| `npi` | TargetingNPI | `TARGETING_NPI` |
| `conversion` | Conversion | `CONVERSION` |

## Code examples

### REST example

```
GET /v3/crmdata/{segmentType}/segment/{advertiserId}/{crmDataId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query CrmDataSegmentStatus {
  advertiser(id: "adv123") {
    crmDataSegmentStatus(segmentType: TARGETING, crmDataId: "crm-segment-id") {
      firstPartyDataId
      activeIds
      receivedIds
      lastUpdatedAt
      segmentType
      latestActivatedDrop {
        state
        mergeMode
        ttlInMinutes
      }
    }
  }
}
```
