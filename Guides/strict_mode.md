# Strict mode

- Source: https://open.thetradedesk.com/advertiser/docsApp/Foundations/resources/doc/StrictMode
- Retrieved: 2026-11-14
- Category: Guides

---

# Strict mode

Strict mode is an API feature that performs additional checks to highlight unrecognized elements in the API call. When enabled, the strict mode API feature returns an error response if either of the following conditions is true:

- The request body contains an unrecognized property.
- The request body specifies a value for a read-only property.

## Discover unrecognized properties

 When a request body contains an unrecognized property, the API ignores the error and returns a 200 success response. With strict mode enabled, when the platform identifies an unknown property in the request, the API responds with a 400 error. Strict mode is particularly useful for catching typos.

The following request code snippet has the `TrackingTagID` property misspelled as `TruckingTagId`:

```
{
	"CampaignConversionReportingColumns": [
    	{
        	"TruckingTagId": "{trackingtagid}",//the property name is misspelled
        	"ReportingColumnId": 56431304,
        	"TrackingTagName": "spring",
        	"BidListAdjustmentType": "TargetList",
        	"BidListDimensions": [
            	"HasGeoSegmentId": "USA",
             	"HasDeviceTypeId": "Roku"
        	]
		}
    ]
}

```

The following is the 400 error response for the `TruckingTagID` property with strict mode enabled:

```
{
    "Property": "$.CampaignConversionReportingColumns[1].TruckingTagId",
    "Reasons": [
        "The property '$.CampaignConversionReportingColumns[1].TruckingTagId' was not recognized."
    ]
}
```

## Recognize read-only properties

 When a request attempts to assign a value to a read-only property, the API ignores the error and returns a 200 success response. With strict mode enabled, when the platform identifies a read-only property in the request, the API responds with a 400 error.

The following request code snippet has values entered for the `BidListDimensions` property, a read-only property that doesn’t accept values:

```
{
	"AssociatedBidLists": [
    	{
        	"BidListId": 1357911,
        	"IsEnabled": true,
        	"IsDefaultForDimension": true,
        	"BidListAdjustmentType": "TargetList",
        	"BidListDimensions": [
            	"HasGeoSegmentId": "USA",//This is a read-only property where no values must be entered
            	"HasDeviceTypeId": "Roku"//This is a read-only property where no values must be entered
       		]
    	}
	]
}

```

The following is the 400 error response message for the `BidListDimensions` property with strict mode enabled:

```
{
	"Property": "$.AssociatedBidLists[1].BidListDimensions",
 	"Reasons": [
		"The property '$.AssociatedBidLists[1]/BidListDimensions' is read-only for POST."
	]
}
```

### How the API Manages Read-Only Properties

 While a 400 response from the API under strict mode alerts you not to assign values to read-only properties, the API treats read-only properties differently under some conditions:

| Read-Only Type | Description | Field Example |
| --- | --- | --- |
| Always Read-Only | These are always read-only. Any values entered will be ignored. | `CreatedAtUTC` |
| Read-Only On Create | These are read-only on create but may be required for updates. | `AdGroupId`, `CampaignId`, `BidListId` |
| Read-Only On Update | These are read-only properties that can be set when an entity is created but cannot be modified after. | `IsHighFillRate` |

## Enable Strict Mode

To enable strict mode when creating an API request, set the following values in the header:

1. Enter `TTD-Strict-Mode` as a new key value.
2. Set the `TTD-Strict-Mode` value to `true`. To disable strict mode, set it to `false`.

For example, the following is a POST /v3/campaign request with strict mode enabled in the header.

```
curl --location --request POST 'https://ext-api.sb.thetradedesk.com/v3/campaign' \
--header 'Content-Type: application/json' \
--header 'TTD-Strict-Mode: true' \
--header 'Ttd-Auth: yourauthtoken'
```

> **IMPORTANT**: Since requests that normally succeed may fail under strict mode, use strict mode _only_ when developing your integration. Using strict mode in your production application may cause unexpected failures. For details, see Best Practices.

If the header is not provided, the request will revert to the default setting. For details, see Change Strict Mode Default Settings.

### Change Strict Mode Default Settings

The default setting for strict mode is off. If you want to enable strict mode as your default user setting, contact your Account Manager. When enabled by default, strict mode is active even when you call the API without enabling the `TTD-Strict-Mode` header.

To override the default setting for Strict Mode if it already has been enabled/disabled:

1. Enter `TTD-Strict-Mode` in the header as shown in Enable Strict Mode.
2. Set the key value to `true` or `false` depending on your desired strict mode status.

## Best Practices

To avoid issues, adapt the following best practices:

- Enable strict mode as a testing feature during the integration stage. When you move the strict mode-enabled code from integration to production, make sure that it is vetted and suitable for production requests.
- To minimize risk, introduce strict mode incrementally in existing production code. Instead of enabling strict mode for all requests by default, enable it for individual requests that require additional validation.
- To avoid potential coding oversight, track and log the 400 errors returned by strict mode.
- When updating entities, avoid copying GET payloads to PUT requests for the following reasons:

  - This slows down your request processing time.
  - With strict mode enabled, you may inadvertently send in read-only properties, resulting in failure and a 400 error.

- Instead, in PUT requests, include only properties that require an update. When there are exceptions to this rule, the endpoint documentation indicates which properties revert to default if you don’t include them in the request.
