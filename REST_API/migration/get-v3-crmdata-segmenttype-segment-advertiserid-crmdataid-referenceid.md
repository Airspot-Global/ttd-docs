# GET /v3/crmdata/{segmentType}/segment/{advertiserId}/{crmDataId}/{referenceId} → Query.crmDataDropStatus

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-crmdata-segmenttype-segment-advertiserid-crmdataid-referenceid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/crmdata/{segmentType}/segment/{advertiserId}/{crmDataId}/{referenceId} → Query.crmDataDropStatus

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/crmdata/{segmentType}/segment/{advertiserId}/{crmDataId}/{referenceId}` |
| GraphQL query | `Query.crmDataDropStatus` |
| Return type | `CrmDataDropInfo` |

## Request and filter field mapping

| REST field | GraphQL argument | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `advertiserId` | `advertiserId` | ID! | Required | Path parameter mapped to required Query.`crmDataDropStatus` arg. |
| `crmDataId` | `crmDataId` | ID! | Required | N/A |
| `referenceId` | `referenceId` | ID! | Required | N/A |
| `segmentType` | `segmentType` | SegmentTypeInput | Required | Required REST path parameter. Valid path values: `targeting`, `npi`, `conversion` (see SegmentTypeInput). |

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `DropInfo` | (return value) | CrmDataDropInfo | Nullable | Returns null when REST DropInfo is null (404 path). |
| `DropInfo.State` | `state` | CrmDataDropState! | Not nullable | N/A |
| `DropInfo.PiiType` | `piiType` | CrmDataPiiType! | Not nullable | REST field deprecated 2026-10-04. |
| `DropInfo.PiiTypes` | `piiType` | CrmDataPiiType! | Not nullable | Not currently available in GraphQL |
| `DropInfo.MergeMode` | `mergeMode` | MergeMode! | Not nullable | N/A |
| `DropInfo.SegmentType` | `segmentType` | SegmentType! | Not nullable | N/A |
| `DropInfo.TtlInMinutes` | `ttlInMinutes` | Long! | Not nullable | N/A |
| `DropInfo.RetentionEnabled` | `retentionEnabled` | Boolean! | Not nullable | N/A |
| `DropInfo.RetentionRemainingInDays` | `retentionRemainingInDays` | Long! | Not nullable | N/A |
| `DropInfo.CreatedAt` | `createdAt` | DateTime | Nullable | N/A |
| `DropInfo.PiiUploadedAt` | `piiUploadedAt` | DateTime | Nullable | N/A |
| `DropInfo.ProcessingAt` | `processingAt` | DateTime | Nullable | N/A |
| `DropInfo.IngestedAt` | `ingestedAt` | DateTime | Nullable | N/A |
| `DropInfo.SucceededAt` | `succeededAt` | DateTime | Nullable | N/A |
| `DropInfo.CancelledAt` | `cancelledAt` | DateTime | Nullable | N/A |
| `DropInfo.FailedAt` | `failedAt` | DateTime | Nullable | N/A |
| `DropInfo.FailureMessage` | `failureMessage` | String | Nullable | N/A |
| `DropInfo.ReceiptFileUrl` | `receiptFileUrl` | String | Nullable | N/A |
| `DropInfo.Statistics.TotalRecords` | `statistics.totalRecords` | Long | Nullable | N/A |
| `DropInfo.Statistics.ValidRecords` | `statistics.validRecords` | Long | Nullable | N/A |
| `DropInfo.Statistics.UniqueIdDeficit` | `statistics.uniqueIdDeficit` | Long | Nullable | N/A |
| `DropInfo.Statistics.SucceededRecords` | `statistics.succeededRecords` | Long | Nullable | N/A |
| `DropInfo.Statistics.FailedRecords` | `statistics.failedRecords` | Long | Nullable | N/A |
| `DropInfo.Statistics.EmptyRecords` | `statistics.emptyRecords` | Long | Nullable | N/A |
| `DropInfo.Statistics.EmailRecordsNotInAcceptedEmailDomain` | `statistics.emailRecordsNotInAcceptedEmailDomain` | Long | Nullable | N/A |
| `DropInfo.Statistics.EmailHashRecordsNotBase64EncodedSha256` | `statistics.emailHashRecordsNotBase64EncodedSha256` | Long | Nullable | N/A |
| `DropInfo.Statistics.EmailInvalidFormat` | `statistics.emailInvalidFormat` | Long | Nullable | N/A |
| `DropInfo.Statistics.IngestedInvalidCsvFormat` | `statistics.ingestedInvalidCsvFormat` | Long | Nullable | N/A |
| `DropInfo.Statistics.IngestedRecords` | `statistics.ingestedRecords` | Long | Nullable | N/A |

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
GET /v3/crmdata/{segmentType}/segment/{advertiserId}/{crmDataId}/{referenceId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query CrmDataDropStatus {
  crmDataDropStatus(
    segmentType: TARGETING
    advertiserId: "adv123"
    crmDataId: "crm-segment-id"
    referenceId: "drop-ref-id"
  ) {
    state
    mergeMode
    segmentType
    ttlInMinutes
    retentionEnabled
    succeededAt
    statistics {
      totalRecords
      validRecords
    }
  }
}
```
