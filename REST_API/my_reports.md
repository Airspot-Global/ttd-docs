# My Reports

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/My%20Reports
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/My%20Reports (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API
<!-- airspot:begin placement="header" -->
- Architectural Guide: [Reporting Best Practices & Architecture Guide](../Guides/reporting_best_practices.md)
<!-- airspot:end -->

---

<!-- airspot:begin placement="after-header" -->
> **Architecture Note**: My Reports is The Trade Desk's asynchronous batch reporting engine. For real-time, interactive UI dashboards, platforms use the synchronous GraphQL Tile API (`SwedishCampaignReporting`). When synchronous Tile API queries experience publisher indexing delays, consumers should apply non-destructive stale-while-revalidate caching and preserve historical publisher dimensions as documented in [Guides/reporting_best_practices.md](../Guides/reporting_best_practices.md).
<!-- airspot:end -->

## Operations and endpoints

### POST /v3/myreports/conversionpixelnames

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-myreports-conversionpixelnames

Get a list of conversion pixel names for use in scheduling reports. For details and examples, see [Create and Manage Report Schedules](/v3/portal/reds/doc/AggregatedReportsExecution).

### GET /v3/myreports/reportdelivery/facets

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-myreports-reportdelivery-facets

Get the facets of Report Deliveries.

### GET /v3/myreports/reportexecution/facets

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-myreports-reportexecution-facets

Get the facets of Report Executions.

### POST /v3/myreports/reportexecution/query/advertisers

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-myreports-reportexecution-query-advertisers

Get a page of Report Executions that match the Advertisers and filters in the specified query.

### POST /v3/myreports/reportschedule

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-myreports-reportschedule

Create a new report schedule.

### GET /v3/myreports/reportschedule/facets

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-myreports-reportschedule-facets

Get the facets of a Report Schedule.

### POST /v3/myreports/reportschedule/query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-myreports-reportschedule-query

Get a page of Report Schedules that match the filters in the specified query.

### GET /v3/myreports/reportschedule/{scheduleId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-myreports-reportschedule-scheduleid

Get a report schedule.

### DELETE /v3/myreports/reportschedule/{scheduleId}

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/delete-myreports-reportschedule-scheduleid

Delete the report schedule.

### GET /v3/myreports/reporttemplate/facets

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/get-myreports-reporttemplate-facets

Get the facets of Report Templates.

### POST /v3/myreports/reporttemplateheader/query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-myreports-reporttemplateheader-query

Get a page of Report Template Headers that match the filters in the specified query.

### POST /v3/myreports/supportedtailaggregationprofiles/query

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-myreports-supportedtailaggregationprofiles-query

Get the tail aggregation profiles that are supported by the Report Template in the specified query.
