# Making REST API Calls

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/ApiUsageGuidelines
- Category: Guides

---

# Making REST API Calls

If you have completed the steps outlined in [Getting Started with The Trade Desk Platform API](/v3/portal/api/doc/ApiPlatformGetStarted) and have received your API credentials, you can now access our platform API.

## 

Environments[](#environments)

To manage production-release processes, we provide environments for users using The Trade Desk platform or Walmart DSP. To specify which production environment to make calls to, use the root URL that corresponds to your platform in the following table.

| Platform | Root URL |
| The Trade Desk | `https://api.thetradedesk.com/v3/` |
| Walmart DSP | `https://api.dsp.walmart.com/v3/` |

For details on generating authentication tokens, see [Authentication](/v3/portal/api/doc/Authentication).

> **IMPORTANT**: To run test processes, use the sandbox environment for Platform API integrations, since the sandbox code is synced with the codebase of our production environment. For details, see [Partner Sandbox](/v3/portal/api/doc/PartnerSandbox).

## 

Protocol[](#protocol)

Communication with The Trade Desk platform API is performed using JSON over HTTPS. When sending JSON requests to the API, be sure to set the HTTP `Content-Type` header to `application/json`:

Content-Type: application/json

When a request is successful, the API returns an HTTP response with a 200 status code and, if appropriate, a JSON response body. If an error occurs during request processing, the API returns an HTTP response with an appropriate error code and a JSON body describing the error.

For a list of the supported HTTP response codes, see [Return Codes](/v3/portal/api/doc/ReturnCodes). For details about the maximum number of calls you can make to each endpoint, see [Rate Limits](/v3/portal/api/doc/RateLimits).

## 

Partial Object Updates[](#partial-updates)

The API differentiates between the required properties, which must be present in a request, and nullable properties, which, if present, may be set to `null`. All properties are labeled accordingly in the documentation.

When submitting a request to the API, any properties included in the request will be updated, even if they have `null` values.

To update only a subset of properties for an object, submit the object ID and the properties that need to be updated in the JSON request. For example, if you wish to change the `Description` of the advertiser with ID `akj3m3`, make the following request:

{

    "AdvertiserId": "akj3m3",

    "Description": "Updated"

}

> **IMPORTANT**: Ensure that your JSON serialization library will allow unknown properties to appear in the JSON response without causing an error, which is standard behavior in most JSON serialization libraries.

See also [Platform Synchronization](/v3/portal/api/doc/PlatformSynchronization).

### 

Best Practices

*   Do not paste the entire GET response schema, as this slows down your request processing time.
*   Modify the values of the properties that you want to update and include only them in the PUT request schema. The endpoint documentation indicates any exceptions such as which properties revert to default values if you don’t include them in the request.
*   Arrays in PUT requests _replace_ the current ones instead of _adding_ to them. If you want to add items to any current arrays, make sure to retrieve them with the respective GET requests first and then include the current and new values in respective PUT requests with any other appropriate changes.
*   Track and log the 400 errors returned so you can detect potential coding mistakes.

See also [Rate Limits](/v3/portal/api/doc/RateLimits) and [Strict Mode](/v3/portal/api/doc/StrictMode).