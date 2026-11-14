# GET /v3/campaign/clone/status/{referenceId} → Query.campaignCloneProgress

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/get-v3-campaign-clone-status-referenceid
- Retrieved: 2026-11-14
- Category: REST_API

---

# GET /v3/campaign/clone/status/{referenceId} → Query.campaignCloneProgress

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `GET /v3/campaign/clone/status/{referenceId}` |
| GraphQL query | `Query.campaignCloneProgress(id:)` |
| Return type | `CampaignCloneProgress` |

REST `referenceId` maps to the clone-progress entity ID (`Long`). Per-job details (progress percentage, clone report, ad-group mappings) are on `jobs.nodes` (`CampaignCloneJob`).

## Response field mapping

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `ReferenceId` | `id` | Long! | Not nullable | Top-level `campaignCloneProgress(id:)` argument. |
| `Status` | `status` | CloneJobStatus! | Not nullable | Aggregate status on `CampaignCloneProgress`. Per-job status: `jobs.nodes[].status`. |
| `ProgressPercentage` | `jobs.nodes[].progressPercentage` | Float! | Not nullable | On each `CampaignCloneJob` in the `jobs` connection. |
| `CampaignId` | `jobs.nodes[].cloneInfo.campaignClone.id` | ID | Nullable | Populated when clone completes. |
| `CloneReport` | `jobs.nodes[].cloneReport` | [String!]! | Not nullable | N/A |
| `AdGroupIdMap` | `jobs.nodes[].cloneInfo.adGroupCloneMap` | [AdGroupClonePair!]! | Not nullable | Dictionary entries as paired original/cloned ad groups. |
| `FailureMessage` | `jobs.nodes[].failureMessage` | String | Nullable | N/A |
| `FailedAdGroupIds` | `jobs.nodes[].failedAdGroups` | [AdGroupCloneFailurePairing!]! | Not nullable | Dictionary entries as ad group + failure message pairings. |

## Endpoint-specific nested types and enums

### AdGroupClonePair (maps REST `AdGroupIdMap` dictionary entry)

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| Key (source ad group ID) | `originalAdGroup.id` | ID! | Not nullable | N/A |
| Value (cloned ad group ID) | `clonedAdGroup.id` | ID | Nullable | Null if clone failed for that ad group. |

### AdGroupCloneFailurePairing (maps REST `FailedAdGroupIds` dictionary entry)

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| Key (source ad group ID) | `adGroup.id` | ID! | Not nullable | N/A |
| Value (failure message) | `failureMessage` | String! | Not nullable | N/A |

## Code examples

### REST example

```
GET /v3/campaign/clone/status/{referenceId} HTTP/1.1
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
query GetCloneProgress($id: Long!) {
  campaignCloneProgress(id: $id) {
    id
    status
    cloneCount
    jobs {
      nodes {
        id
        status
        progressPercentage
        cloneReport
        failureMessage
        cloneInfo {
          campaignClone {
            id
          }
          adGroupCloneMap {
            originalAdGroup { id }
            clonedAdGroup { id }
          }
        }
        failedAdGroups {
          adGroup { id }
          failureMessage
        }
      }
    }
  }
}
```
