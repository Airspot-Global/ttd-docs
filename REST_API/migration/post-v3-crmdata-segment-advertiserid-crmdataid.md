# POST /v3/crmdata/segment/{advertiserId}/{crmDataId} → crmDropBind

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-crmdata-segment-advertiserid-crmdataid
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/crmdata/segment/{advertiserId}/{crmDataId} → crmDropBind

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/crmdata/segment/{advertiserId}/{crmDataId}` |
| GraphQL operation | `crmDropBind` |
| Input type | `CrmDropBindInput` |
| Output type | `CrmDropBindPayload` (`data: CrmDrop`, `errors: [CrmDropBindMutationError!]`) |

## Input field mapping

Input type: `CrmDropBindInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `advertiserId` | N/A | N/A | Required | Path parameter; GraphQL `crmDropBind` identifies segment by `segmentId` only. Ownership enforced via auth on returned `CrmDrop.ownerId`. |
| `crmDataId` | `segmentId` | String! | Required | Path parameter mapped to `segmentId` input |
| `PiiType` | `piiTypes` | [PiiType!] | Optional | REST accepts one optional PII type; GraphQL accepts a list. See `CrmDataPiiType → PiiType` table below for value mappings. |
| `MergeMode` | `mergeMode` | MergeMode! | Required | `CrmDataMergeMode` (`Add`, `Replace`) → `MergeMode` enum |
| `TtlInMinutes` | `ttl` | TimeSpan | Optional | Minutes → ISO-8601 `TimeSpan` (default P90D / 129600 minutes) |

## Output field mapping

Output type: `CrmDrop` (returned as `data` on `CrmDropBindPayload`)

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `ReferenceId` | `id` | ID! | Not nullable | Drop ID used for status polling |
| `Url` | `uploadUrl` | String | Nullable | Pre-signed upload URL; send PII via `PUT` to this URL |

## Endpoint-specific nested types and enums

### CrmDataPiiType → PiiType

REST accepts a single optional `CrmDataPiiType`; GraphQL `piiTypes` is a list.

| REST value | GraphQL enum |
| --- | --- |
| `Email` | `EMAIL` |
| `EmailHashedUnifiedId2` | `EMAIL_HASHED_UNIFIED_ID` |
| `EmailHashed` | `EMAIL_HASHED_UNIFIED_ID` |
| `Phone` | `PHONE` |
| `PhoneHashed` | `PHONE_HASHED_UNIFIED_ID` |
| `PhoneHashedUnifiedId2` | `PHONE_HASHED_UNIFIED_ID` |
| `UID2` | `UID2` |
| `UID2Token` | `UID2_TOKEN` |
| `EUID` | `EUID` |
| `EUIDToken` | `EUID_TOKEN` |
| `IDL` | `RAMP_ID` |
| `RampID` | `RAMP_ID` |
| `ID5` | `ID5` |
| `NetID` | `NET_ID` |
| `FirstId` | `FIRST_ID` |
| `TDID` | `TDID` |
| `DAID` | `DAID` |
| `NPI` | `NPI` |
| `IPv4` | `IPV4` |

### CrmDataMergeMode → MergeMode

| REST value | GraphQL enum |
| --- | --- |
| `Add` | `ADD` |
| `Replace` | `REPLACE` |

## Code examples

### REST example

```
POST /v3/crmdata/segment/abc123/crm-segment-id-456 HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "PiiType": "Email",
  "MergeMode": "Add",
  "TtlInMinutes": 129600
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
      piiTypes: [EMAIL]
      mergeMode: ADD
      ttl: "P90D"
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
