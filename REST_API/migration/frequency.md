# Frequency: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/frequency-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Frequency: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/frequency/config/{counterId}` | `FrequencyCounter.frequencyConfig` | N/A |
| `POST /v3/frequency/config/query` | `Partner.frequencyConfigs`, `Advertiser.frequencyConfigs`, `AdGroup.frequencyConfigs` | Campaign not supported |
| `POST /v3/frequency/config/query/bidlist` | `BidList.frequencyConfigs` | N/A |
| `POST /v3/frequency/config/query/counter` | `FrequencyCounter.frequencyConfig` | Replaced by per-counter config load |
| `GET /v3/frequency/counter/{counterId}` | `FrequencyCounter` | N/A |
| `POST /v3/frequency/counter/query` | `Advertiser.frequencyCounters`, `Partner.frequencyCounters` | N/A |
| `POST /v3/frequency/migration/query/restrictedcounters` | `Advertiser.restrictedFrequencyCounters`, `Partner.restrictedFrequencyCounters` | N/A |
| `POST /v3/frequency/migration/bidlist/status` | `BidList.frequencyMigrationStatus` | N/A |

## Shared nested types and enums

### FrequencyMigratedBidListState

| GraphQL field | GraphQL type | Nullable | REST source field |
| --- | --- | --- | --- |
| `frequencyAdjustmentBidlistId` | Long! | Not nullable | FrequencyAdjustmentBidlistId |
| `isPending` | Boolean! | Not nullable | IsPending |
| `requestCreationDate` | DateTime! | Not nullable | RequestCreationDate |
| `frequencyV2AdjustmentBidlistId` | Long | Nullable | FrequencyV2AdjustmentBidlistId |
| `oneToManyMigration` | Boolean | Nullable | OneToManyMigration |
| `state` | String | Nullable | State |
