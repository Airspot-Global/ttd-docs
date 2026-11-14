# Activity Log

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Activity%20Log
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Activity%20Log (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### PUT /v3/activity

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/put-activity

Create or update the `Note` property for an existing activity log. `Note` is the only property that accepts changes. All other property updates are silently ignored.

### GET /v3/activity/{activityLogId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-activity-activitylogid

Retrieve detail for an activity log entry by `ActivityLogId`.

### POST /v3/activity/query/adgroup

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-activity-query-adgroup

Retrieve and optionally filter a paged list of activity log entries for the specified ad group.

### POST /v3/activity/query/campaign

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-activity-query-campaign

Retrieve and optionally filter a paged list of activity log entries for the specified campaign.

### POST /v3/activity/query/facets

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-activity-query-facets

Retrieve a summary of changed properties and usernames responsible for the changes within the specified date range for the specified ad group or campaign. The results can be used to filter information in the POST /activity/query/adgroup and POST /activity/query/campaign endpoints. Either `AdGroupId` or `CampaignId` is required.
