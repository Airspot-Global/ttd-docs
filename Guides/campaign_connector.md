# Campaign Connector

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/CampaignConnector
- Category: Guides

---

# Campaign Connector

A Campaign Connector is a direct API integration between The Trade Desk and your preferred tools for media operations.

Most agencies and ad platforms use some type of media-operations or order-booking platforms to keep track of the details and billing for a media campaign. During the campaign setup process, media-buying teams have to manually enter campaign details twice: once in their operations tools, and another time in The Trade Desk platform. These duplicate entries are inefficient and often result in discrepancies across platforms that then require troubleshooting and reconciliation. With Campaign Connector, media buyers no longer have to re-enter campaign flight dates and budgets into both platforms. Instead, campaign details can be entered into the order-booking platform and pushed to The Trade Desk.

The following image illustrates the workflow schema of a Campaign Connector.

![Campaign Connector Schema](/v3/content/docs/Images/campaign-connector-workflow-schema.png)

## 

Integration[](#integration)

> **TIP**: To begin testing the integration process, download the [sample code in Python](/v3/content/docs/Samples/TTD_CampaignConnectorCodeSample.zip), which demonstrates the call pattern and best practices for this use case.

The typical Campaign Connector build involves interaction with a number of endpoints. Depending on your scenario, you may interact with some (if not all) of the endpoints outlined in the workflow.

| Call | Description |
| [Authentication](/v3/portal/api/doc/Authentication) | The authentication endpoint generates a user token that will be needed to sign all subsequent actions. Set an expiration for your token and ensure you include the token in the header of any other endpoint interactions. The token should be stored and regenerated periodically. Keep in mind that this endpoint is rate limited, so you will not be able to authenticate on every API call. Instead, it is recommended that you generate a new token once every 24 hours. |
| [Advertiser](/v3/portal/api/doc/Advertisers) | To create campaigns, you will first need to create an advertiser or map an existing one. Remember to pass your authentication token in the header of the call. |
| [Campaigns](/v3/portal/api/doc/Campaigns) | Now that you have an advertiser created, you can create a campaign, where you will define the flight dates, budget allocation, and global pacing settings for your strategies. |
| [Ad Groups](/v3/portal/api/doc/AdGroup) | The ad group is where you define the details of your bidding strategy. In our example below, we've defined an ad-group template that outlines the budget, bids, sitelists, and enabled forms of Auto-Optimization. To help reduce redundant work and ensure your strategies are set up correctly, when designing your ad-group templates, think about the repetitive tasks your team handles that the API can define instead. |

### 

Additional Tasks[](#additional-tasks)

The Campaign Connector build isn't a strictly defined set of tasks. You can design your integration to automate any number of processes that would impact the efficiency of your day-to-day operations. Some partners look to also monitor the performance of their ad groups and campaigns by using the [Reports](/v3/portal/reds/doc/ReportsGetStarted) endpoints to download insights. Managing the creative upload process by building a [Creative Connector](/v3/portal/api/doc/CreativeConnector) is another time-saving task that you can include in your design.

## 

Best Practices[](#best=practices)

The following sections provide additional guidance for building a Campaign Connector:

*   [Caching Responses and Partial Updates](#updates)
*   [Efficient Syncing using Delta Endpoints](#syncing)
*   [Error Handling](#error-handling)
*   [Rate Limits](#rate-limits)

See also [Platform Synchronization](/v3/portal/api/doc/PlatformSynchronization).

### 

Caching Responses and Partial Updates[](#updates)

Every API call returns the entire entity in the response payload. If your platform is responsible for defining the settings of any entity, caching the response is the most efficient option for this integration. It will conserve resources for retrieving entity data from The Trade Desk before you need to make an update.

If updates need to be pushed, we allow the flexibility to do partial updates to all entities by just supplying the entity ID and the parameters that you would like to change. In the example below, we use a PUT call to make an update to the campaign budget. The GET - PUT workflow is not supported with our API, as there are parameters that are included in the GET response that are not allowed when pushing an update. Use the related delta endpoint if you need to understand an entity's state before pushing a change.

> [!IMPORTANT]
> **Kokai Campaign Provisioning & Seed Association**:
> In Kokai, after creating a campaign via `POST /v3/campaign` or GraphQL `campaignCreate`, seed attachment must be performed via the GraphQL [`campaignUpdateSeed` mutation](seeds.md#attach-to-campaign). Legacy bulk settings endpoints such as `PUT /v3/campaign/bulksettings` are deprecated and return `HTTP 405 Method Not Allowed`.

### 

Efficient Syncing using Delta Endpoints[](#syncing)

When two platforms are linked, it is often necessary to keep both systems in sync. If there are users in our platform who will be making adjustments to The Trade Desk settings, then it is important to understand any changes that were made before pushing an update. We have a suite of delta endpoints that allow you to request any entities that have been created or have changed since the last time you requested the state. See our section on delta endpoints that details the list of all available endpoints.

The following example demonstrates how you would use the delta endpoint to retrieve all ad groups that have changed since the last time you requested the state. Every response to this endpoint provides the token "LastChangeTrackingVersion", which identifies a point in time when an entity's state was provided. This value should be stored and used on the subsequent delta request, so that our system understands the timestamp to use to compute entity changes from your prior request.

#### API Call Example

curl -H "Content-Type: application/json" -H "TTD-Auth:|Token|" -X "POST 

https://api.thetradedesk.com/v3/delta/adgroup/query/advertiser" -d 

'{"AdvertiserId": "|advertiserid|", "ReturnEntireAdGroup": true, 

"LastChangeTrackingVersion": 361335703}'

#### API Response Example

{

  "AdGroups": \[

    {

      "CampaignId": "|campaignid|",

      "AdGroupId": "|adgroupid|",

      "AdGroupName": "Test Ad Group ",

      "Description": "Testing Ad Group",

      "IsEnabled": false,

      "AdGroupCategory": 8311,

      "RTBAttributes": {........}

    }

  \],

  "MoreAdGroupsAvailable": false,

  "ElementIds": null,

  "LastChangeTrackingVersion": 361337290

}

If you are operating your own UI, there are also use cases in which clients are making inputs while service teams are making changes within The Trade Desk platform. In these cases, where updates are being made across both systems, there may be a need to understand the complete state of The Trade Desk entities to resync both platforms. Our query endpoints can help you accomplish this, by retrieving all entity data. These endpoints are strictly rate limited and should only be used for infrequent retrieval. The example below shows how you would use the query endpoint to retrieve all ad groups that are associated with an advertiser.

#### API Call Example

curl -H "Content-Type: application/json" -H "TTD-Auth:|Token|" -X "POST 

https://api.thetradedesk.com/v3/adgroup/query/advertiser" -d '{"AdvertiserId": 

"sample string 1", "Availabilities": \["Available"\], "PageStartIndex": 0, 

"PageSize": 100}'

### 

Error Handling[](#error-handling)

When a request is successful, the API will return an HTTP response with a 200 status code and, if appropriate, a JSON response body. If an error occurs during request processing, the API will return an HTTP response with an appropriate non-200 status code and a JSON body describing the error. In the case of 5xx errors, please check our API Status page and contact your solutions architect to look further into your issue. If you received a 4xx error, the issue is typically a user error. Please monitor the messages in the JSON response so that you can self-correct.

### 

Rate Limits[](#rate-limits)

To ensure sufficient capacity at all times for all our partners, we have implemented rate limits across our API endpoints. If limits are exceeded, the API will return a 429 response code. The proper behavior for handling 429 errors is using an exponential back-off policy until you are able to successfully complete a transaction. For details, see [Rate Limits](/v3/portal/api/doc/RateLimits).