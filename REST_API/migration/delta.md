# Delta: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/delta-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Delta: REST → GraphQL migration guide

Activity-log and available-contract delta polling (`POST /v3/delta/activity/query/adgroup`, `POST /v3/delta/contract/query/advertiser/available`) are **Not currently available in GraphQL**—continue using REST for those surfaces.

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `POST /v3/delta/adgroup/query/advertiser` | `Query.adGroupDelta` | N/A |
| `POST /v3/delta/adgroup/query/campaign` | `Query.adGroupDelta` | N/A |
| `POST /v3/delta/advertiser/query/partner` | `Query.advertiserDelta` | N/A |
| `POST /v3/delta/campaign/query/advertiser` | `Query.campaignDelta` | N/A |
| `POST /v3/delta/creative/query/advertiser` | `Query.creativeDelta` | N/A |
| `POST /v3/delta/bidlist/query/partner` | `Partner.bidListDelta` | N/A |
| `POST /v3/delta/bidlist/query/global` | `Query.globalBidListDelta` | N/A |
| `POST /v3/delta/study` | `Query.liftStudyDelta` | Distinct from `conversionLiftStudyDelta` |
| `POST /v3/delta/dmp/query/advertiser/firstparty` | `Query.firstPartyDataDelta` | N/A |
| `POST /v3/delta/dmp/firstparty` | `Query.firstPartyDataDelta` | Deprecated REST path |
| `POST /v3/delta/advertiser` | `Query.advertiserDelta` | Deprecated REST path |
| `POST /v3/delta/campaign` | `Query.campaignDelta` | Deprecated REST path |
| `POST /v3/delta/creative` | `Query.creativeDelta` | Deprecated REST path |

## Shared nested types and enums

### TargetingData (FirstPartyData)

| REST field (via data[]) | GraphQL field | GraphQL type | Notes |
| --- | --- | --- | --- |
| DataType | `targetingData.dataType` | `TargetingDataType!` | N/A |

### ActiveUniques (FirstPartyData)

| REST field (via data[]) | GraphQL field | GraphQL type | Notes |
| --- | --- | --- | --- |
| UniqueUserCount / ActiveIDsCount | `activeUniques.idsCount` | `Long` | N/A |
| UniqueUserInAppCount / ActiveIDsInAppCount | `activeUniques.idsInAppCount` | `Long` | N/A |
| UniqueUserWebCount / ActiveIDsWebCount | `activeUniques.idsWebCount` | `Long` | N/A |
| UniqueConnectedTvCount / ActiveIDsConnectedTvCount | `activeUniques.idsConnectedTvCount` | `Long` | N/A |
| PersonsCount / ActivePersonsCount | `activeUniques.personsCount` | `Long` | N/A |
| HouseholdCount / ActiveHouseholdCount | `activeUniques.householdCount` | `Long` | N/A |
