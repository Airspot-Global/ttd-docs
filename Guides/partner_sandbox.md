# Partner Sandbox

- Source: https://open.thetradedesk.com/advertiser/docsApp/Foundations/resources/doc/PartnerSandbox
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/doc/PartnerSandbox (retired)
- Retrieved: 2026-11-14
- Category: Guides

---

# Partner Sandbox

The Partner Sandbox is an isolated environment for testing features of the Platform API without impacting your production data or billing cycle. The Partner Sandbox environment contains a clone of your production data that refreshes on a regular weekly basis, so you can try out different strategies and see how they impact your audience. You can start interacting with the sandbox by switching the root URL to match your API and platform type in Partner Sandbox endpoints.

> **NOTE**: This guide is for Platform API requests using REST and GraphQL. The Partner Sandbox does not support other APIs that do not use Platform Authentication.

Here's what you need to know about the Partner Sandbox testing environment:

- Changes made in the Partner Sandbox do not affect your production environment. No real spend from campaigns or ad groups occurs in the Partner Sandbox.
- Your Partner Sandbox partner ID, provider ID, and brand IDs are the same as in your production environment.
- Data is copied from your production environment on a weekly cadence, every Thursday night, and is ready for use by Friday morning in North America.
- The Partner Sandbox is wiped and refreshed weekly with the latest production data. Any production changes are synced in and your generated tokens are preserved throughout each refresh.
- The Partner Sandbox uses a different endpoint for REST and GraphQL requests. Update your root URL before using the API. For details, see Partner Sandbox endpoints.
- You might experience differences between sandbox and production outputs due to how data is handled differently. For details, see FAQs.

## Setup

Before you can use the Partner Sandbox, be sure to have completed these steps in any order:

- Verify that the data you are testing on has been synced with the Partner Sandbox.
- Have an existing API token or equivalent production key. For details, see API token authentication.
- If you need access to any hidden endpoints, contact your Technical Account Manager.

## Partner Sandbox endpoints

If you currently have an existing UI or API login in the production environment, an account might already exist in the Partner Sandbox. However, recently created accounts might not be available in the Partner Sandbox until the next refresh.

> **NOTE**: The Partner Sandbox mirrors your production environment. You can use your production key, but for additional security you can generate a sandbox-only key.

The following table shows two root URLs to access the REST and GraphQL APIs on the Partner Sandbox in The Trade Desk platform. For Walmart DSP, see FAQs.

| API | Root URL | Description |
| --- | --- | --- |
| REST | `https://ext-api.sb.thetradedesk.com/v3/` | The root URL for all REST Partner Sandbox requests. |
| GraphQL | `https://ext-api.sb.thetradedesk.com/graphql` | The root URL for all GraphQL Partner Sandbox requests. |
| MCP | `https://ext-api.sb.thetradedesk.com/mcp/koa` | The root URL for AI assistant Partner Sandbox requests. **NOTE**: You must have OAK authorization. |

For example, to create a new login token using the REST API, call `POST https://ext-api.sb.thetradedesk.com/v3/authentication`. See also API token authentication.

> **TIP**: In the Platform UI, you can view the results of your API calls at `https://ext-desk.sb.thetradedesk.com`, which serves as the UI equivalent of the API Partner Sandbox.

## FAQs

The following is a list of commonly asked question about the Partner Sandbox.

### How long does it take for the data refresh to complete?

The data refresh completion time varies due to many factors such as size and migration time. It is completed after it passes all tests. You may experience variations in refresh start and end times.

### Can I upload audience data into the Partner Sandbox?

No. Audience data is uploaded using header authentication for the Data API, which is incompatible with the Partner Sandbox. To test in the Partner Sandbox, you must upload your audience data into production and then wait for the weekly sync.

### What are some best practices to run Sandbox tests?

You should run test workflows as early as possible after refresh on Friday morning, and complete them within one to two days post-refresh. Use the remainder of the time to validate all applicable workflows before the wipe.

### Which Platform API endpoints are not supported in the Partner Sandbox?

None of the `/v3/study` endpoints related to lift studies are supported.

> **TIP**: For troubleshooting information, see GraphQL API errors and complexity limits or REST API return codes.

### What are the sandbox endpoints for Walmart DSP?

The following table shows two root URLs to access the REST and GraphQL APIs on the Partner Sandbox in Walmart DSP.

| API | Root URL | Description |
| --- | --- | --- |
| REST | `https://apisb-a.dsp.walmart.com/v3/` | The root URL for all REST Partner Sandbox requests. |
| GraphQL | `https://desksb-a.dsp.walmart.com/graphql` | The root URL for all GraphQL Partner Sandbox requests. |

For example, to create a new login token using the REST API, call `POST https://apisb-a.dsp.walmart.com/v3/authentication`. See also API token authentication.

> **TIP**: In the Platform UI, you can view the results of your API calls at `https://desksb-a.dsp.walmart.com`, which serves as the UI equivalent of the API Partner Sandbox.
