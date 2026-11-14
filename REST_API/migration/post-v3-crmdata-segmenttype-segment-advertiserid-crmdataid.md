# POST /v3/crmdata/{segmentType}/segment/{advertiserId}/{crmDataId} → crmDropBind

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-crmdata-segmenttype-segment-advertiserid-crmdataid
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/crmdata/{segmentType}/segment/{advertiserId}/{crmDataId} → crmDropBind

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/crmdata/{segmentType}/segment/{advertiserId}/{crmDataId}` |
| GraphQL operation | `crmDropBind` |
| Input type | `CrmDropBindInput` |
| Output type | `CrmDropBindPayload` (`data: CrmDrop`, `errors: [CrmDropBindMutationError!]`) |

## Multi-step operations

Same GraphQL mutation as `POST /v3/crmdata/segment/{advertiserId}/{crmDataId}`. The REST `segmentType` path segment selects the adapter only; GraphQL `crmDropBind` resolves the segment by `segmentId`.

## Input field mapping

Input type: `CrmDropBindInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `segmentType` | N/A | N/A | Required | Path parameter selects REST adapter (`targeting`, `conversion`, `npi`). GraphQL `crmDropBind` has no `segmentType` input—segment resolved by `segmentId`. |
| `advertiserId` | N/A | N/A | Required | Path parameter; ownership enforced via auth on returned `CrmDrop.ownerId`. |
| `crmDataId` | `segmentId` | String! | Required | Path parameter mapped to `segmentId` input |
| `PiiType` | `piiTypes` | [PiiType!] | Optional | REST accepts one optional PII type; GraphQL accepts a list. See CrmDataDropInfo domain page `CrmDataPiiType → PiiType` table for value mappings. |
| `MergeMode` | `mergeMode` | MergeMode! | Required | `CrmDataMergeMode` (`Add`, `Replace`) → `MergeMode` enum |
| `TtlInMinutes` | `ttl` | TimeSpan | Optional | Minutes → ISO-8601 `TimeSpan` (default P90D / 129600 minutes) |

## Output field mapping

Output type: `CrmDrop` (returned as `data` on `CrmDropBindPayload`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `ReferenceId` | `id` | ID! | Not nullable | Drop ID used for status polling |
| `Url` | `uploadUrl` | String | Nullable | Pre-signed upload URL |

## Endpoint-specific nested types and enums

### CrmDataPiiType → PiiType

REST accepts a single optional `CrmDataPiiType`; GraphQL `piiTypes` is a list. See the CrmDataDropInfo domain page `CrmDataPiiType → PiiType` table for REST → GraphQL value mappings.

### CrmDataMergeMode → MergeMode

| REST value | GraphQL enum |
| --- | --- |
| `Add` | `ADD` |
| `Replace` | `REPLACE` |

## Code examples

### REST example

```
POST /v3/crmdata/conversion/segment/abc123/crm-segment-id-456 HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "MergeMode": "Replace"
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation {
  crmDropBind(
    input: {
      segmentId: "crm-segment-id-456"
      mergeMode: REPLACE
    }
  ) {
    data {
      id
      uploadUrl
    }
    errors {
      ... on UserError {
        message
        field
      }
    }
  }
}
```
