# Bidder service: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/bidderservice-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Bidder service: REST → GraphQL migration guide

**Write operations are not currently available in GraphQL.** Read operations (`Query.bidderService`, `Partner.bidderServices`) are available today.

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/bidderservice/{bidderServiceId}` | `Query.bidderService(id:)` | N/A |
| `POST /v3/bidderservice/query/partner` | `Partner.bidderServices` | N/A |
| `POST /v3/bidderservice` | N/A | Not currently available in GraphQL |
| `PUT /v3/bidderservice` | N/A | Not currently available in GraphQL |
| `DELETE /v3/bidderservice/{bidderServiceId}` | N/A | Not currently available in GraphQL |

## Shared nested types and enums

### BidderEndpoint

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `DataCenter` | `dataCenter` | BiddingDataCenter! | Not nullable | N/A |
| `Url` | `url` | String! | Not nullable | N/A |
| `IsEnabled` | `isEnabled` | Boolean! | Not nullable | N/A |

### BidderFeedbackEndpoint

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `DataCenter` | `dataCenter` | BiddingDataCenter! | Not nullable | N/A |
| `Url` | `url` | String! | Not nullable | N/A |
| `IsEnabled` | `isEnabled` | Boolean! | Not nullable | N/A |

### BiddingDataCenter

| REST value | GraphQL value |
| --- | --- |
| `LosAngelesUsWest` | `LOS_ANGELES_US_WEST` |
| `UsEast` | `US_EAST` |
| `Tokyo` | `TOKYO` |
| `SantaClaraUsWest` | `SANTA_CLARA_US_WEST` |
| `VirginiaUsEast` | `VIRGINIA_US_EAST` |
| `UKEuWest` | `UK_EU_WEST` |
| `JpAsiaPacific` | `JP_ASIA_PACIFIC` |
| `SgAsiaPacific` | `SG_ASIA_PACIFIC` |
| `BrSouthAmerica` | `BR_SOUTH_AMERICA` |
| `DeEuCentral` | `DE_EU_CENTRAL` |
| `IeEuWest` | `IE_EU_WEST` |
| `NYUsEast` | `NY_US_EAST` |
| `De2EuCentral` | `DE2_EU_CENTRAL` |

### VolumeControlPriority

| REST value | GraphQL value |
| --- | --- |
| `Negative` | `NEGATIVE` |
| `Neutral` | `NEUTRAL` |
| `One` | `ONE` |
| `Two` | `TWO` |
| `FrequencyGoal` | `FREQUENCY_GOAL` |
