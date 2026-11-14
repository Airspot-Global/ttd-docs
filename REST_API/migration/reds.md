# REDS: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/reds-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# REDS: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `POST /v3/redsfeed/query` | `Partner.redsFeeds` | Enter via `Query.partner(id:)` |
| `GET /v3/redsfeed/{feedId}` | `Query.redsFeedColumns(feedId:)` | N/A |
| `GET /v3/reds/bids/columns` | N/A | Retired (HTTP 410 Gone); use `Query.redsFeedColumns` with a feed ID |
| `GET /v3/reds/impressions/columns` | N/A | Retired (HTTP 410 Gone); use `Query.redsFeedColumns` with a feed ID |
| `GET /v3/reds/conversions/columns` | N/A | Retired (HTTP 410 Gone); use `Query.redsFeedColumns` with a feed ID |
| `GET /v3/reds/clicks/columns` | N/A | Retired (HTTP 410 Gone); use `Query.redsFeedColumns` with a feed ID |
| `GET /v3/reds/video/columns` | N/A | Retired (HTTP 410 Gone); use `Query.redsFeedColumns` with a feed ID |

## Shared nested types and enums

### REDSColumnItem

| REST field | GraphQL field | GraphQL type | Notes |
| --- | --- | --- | --- |
| `ColumnName` | `columnName` | String | N/A |
| `Description` | `description` | String | N/A |
| `Facet` | `facet` | String | N/A |

### RedsFeedSnowflakeShareModel

| REST field | GraphQL field | GraphQL type | Notes |
| --- | --- | --- | --- |
| `ShareName` | `shareName` | String | N/A |
| `ShareDescription` | `shareDescription` | String | N/A |
| `RegionName` | `regionName` | String | N/A |
| `RegionDescription` | `regionDescription` | String | N/A |
| `AccountName` | `accountName` | String | N/A |
