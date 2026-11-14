# CrmDataDropInfo: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/crmdatadropinfo-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# CrmDataDropInfo: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| POST `/v3/crmdata/segment` | `crmDataSegmentCreate` | Default targeting segment create; equivalent to `POST /v3/crmdata/targeting/segment` |
| POST `/v3/crmdata/{segmentType}/segment` | `crmDataSegmentCreate` | N/A |
| POST `/v3/crmdata/segment/{advertiserId}/{crmDataId}` | `crmDropBind` | N/A |
| POST `/v3/crmdata/{segmentType}/segment/{advertiserId}/{crmDataId}` | `crmDropBind` | REST `segmentType` path selects adapter only |
| DELETE `/v3/crmdata/segment/{advertiserId}/{crmDataId}` | `crmDataSegmentArchive` | Archives segment; not a hard delete |

## Shared nested types and enums

### SegmentType path → SegmentType

| REST path value | GraphQL enum |
| --- | --- |
| targeting | `TARGETING` |
| conversion | `CONVERSION` |
| npi | `TARGETING_NPI` |

### CrmDataRegion

| REST value | GraphQL enum |
| --- | --- |
| `US` | `US` |
| `EU` | `EU` |
| `APAC` | `APAC` |

### CrmDataMergeMode → MergeMode

| REST value | GraphQL enum |
| --- | --- |
| `Add` | `ADD` |
| `Replace` | `REPLACE` |

### CrmDataPiiType → PiiType

REST accepts a single optional PII type on drop create; GraphQL `crmDropBind` accepts a list (`piiTypes`).

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
