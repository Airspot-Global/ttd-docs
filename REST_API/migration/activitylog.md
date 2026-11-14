# Activity log: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/activitylog-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Activity log: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/activity/{activityLogId}` | `Query.activityLog` | N/A |
| `POST /v3/activity/query/adgroup` | `AdGroup.activityLogs` | N/A |
| `POST /v3/activity/query/campaign` | `Campaign.activityLogs` | N/A |
