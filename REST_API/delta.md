# Delta

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Delta
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Delta (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### GraphQL adGroupDelta Query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/ad-group-delta

Get all changed ad groups for an advertiser or campaign since the last change-tracking version.

### GraphQL campaignDelta Query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/campaign-delta

Get all changed campaigns for an advertiser since the last change-tracking version.

### GraphQL creativeDelta Query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/creative-delta

Get all changed creatives for an advertiser since the last change-tracking version.

### GraphQL trackingTagDelta Query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/tracking-tag-delta

Get all changed tracking tags for an advertiser since the last change-tracking version.

### POST /v3/delta/activity/query/adgroup

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-delta-activity-query-adgroup

Retrieve a list of IDs of all activity logs for the specified ad group that were updated since the last change tracking version.  
**TIP**: With GraphQL, you can significantly improve performance, tailor queries to specific criteria, and save both time and effort. To get started, use the [Delta Python scripts](https://github.com/thetradedesk/Platform/tree/main/Python/Delta). See also [Platform Synchronization](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/PlatformSynchronization).

### POST /v3/delta/adgroup/query/advertiser (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-delta-adgroup-query-advertiser

This is a legacy endpoint. Use the [`adGroupDelta` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/ad-group-delta) in GraphQL for improved performance and expanded functionality.

Retrieve a list of IDs of all ad groups for the specified advertiser that were modified since the last change tracking version.  
**TIP**: With GraphQL, you can significantly improve performance, tailor queries to specific criteria, and save both time and effort. To get started, use the [Delta Python scripts](https://github.com/thetradedesk/Platform/tree/main/Python/Delta). See also [Platform Synchronization](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/PlatformSynchronization).

### POST /v3/delta/adgroup/query/campaign (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-delta-adgroup-query-campaign

This is a legacy endpoint. Use the [`adGroupDelta` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/ad-group-delta) in GraphQL for improved performance and expanded functionality.

Retrieve a list of IDs of all ad groups for the specified campaign that were modified since the last change tracking version.  
**TIP**: With GraphQL, you can significantly improve performance, tailor queries to specific criteria, and save both time and effort. To get started, use the [Delta Python scripts](https://github.com/thetradedesk/Platform/tree/main/Python/Delta). See also [Platform Synchronization](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/PlatformSynchronization).

### POST /v3/delta/advertiser/query/partner (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-delta-advertiser-query-partner

This is a legacy endpoint. Use the [`advertiserDelta` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/advertiser-delta) in GraphQL for improved performance and expanded functionality.

Retrieve a list of IDs of all advertisers that were modified since the last change tracking version.  
**TIP**: With GraphQL, you can significantly improve performance, tailor queries to specific criteria, and save both time and effort. To get started, use the [Delta Python scripts](https://github.com/thetradedesk/Platform/tree/main/Python/Delta). See also [Platform Synchronization](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/PlatformSynchronization).

### POST /v3/delta/bidlist/query/global

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-delta-bidlist-query-global

Retrieve a list of IDs of all bid lists that were modified since the last change tracking version.  
**TIP**: With GraphQL, you can significantly improve performance, tailor queries to specific criteria, and save both time and effort. To get started, use the [Delta Python scripts](https://github.com/thetradedesk/Platform/tree/main/Python/Delta). See also [Platform Synchronization](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/PlatformSynchronization).

### POST /v3/delta/bidlist/query/partner

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-delta-bidlist-query-partner

Retrieve a list of IDs of partner bid lists that were modified since the last change tracking version.  
**TIP**: With GraphQL, you can significantly improve performance, tailor queries to specific criteria, and save both time and effort. To get started, use the [Delta Python scripts](https://github.com/thetradedesk/Platform/tree/main/Python/Delta). See also [Platform Synchronization](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/PlatformSynchronization).

### POST /v3/delta/campaign/query/advertiser (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-delta-campaign-query-advertiser

This is a legacy endpoint. Use the [`campaignDelta` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/campaign-delta) in GraphQL for improved performance and expanded functionality.

Retrieve a list of IDs of campaigns that were modified since the last change tracking version.  
**TIP**: With GraphQL, you can significantly improve performance, tailor queries to specific criteria, and save both time and effort. To get started, use the [Delta Python scripts](https://github.com/thetradedesk/Platform/tree/main/Python/Delta). See also [Platform Synchronization](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/PlatformSynchronization).

### POST /v3/delta/contract/query/advertiser/available

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-delta-contract-query-advertiser-available

Retrieve a list of IDs of available contracts that were modified since the last change tracking version.  
**TIP**: With GraphQL, you can significantly improve performance, tailor queries to specific criteria, and save both time and effort. To get started, use the [Delta Python scripts](https://github.com/thetradedesk/Platform/tree/main/Python/Delta). See also [Platform Synchronization](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/PlatformSynchronization).

### POST /v3/delta/creative/query/advertiser (legacy)

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-delta-creative-query-advertiser

This is a legacy endpoint. Use the [`creativeDelta` query](https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/gql-doc/creative-delta) in GraphQL for improved performance and expanded functionality.

Retrieve a list of IDs of creatives that were modified since the last change tracking version.  
**TIP**: With GraphQL, you can significantly improve performance, tailor queries to specific criteria, and save both time and effort. To get started, use the [Delta Python scripts](https://github.com/thetradedesk/Platform/tree/main/Python/Delta). See also [Platform Synchronization](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/PlatformSynchronization).

### POST /v3/delta/dmp/query/advertiser/firstparty

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-delta-dmp-query-advertiser-firstparty

Retrieve a list of IDs of all first-party data segments that were modified since the last change tracking version. For details, see [delta endpoints](https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/PlatformSynchronization#delta-endpoints).  
**NOTE**: This endpoint returns only newly created segments and those with updated metadata, such as changes to names or descriptions. Segments with updated user data, such as user counts, are not returned.
