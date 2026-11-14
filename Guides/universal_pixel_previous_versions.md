# Universal pixel: Previous versions

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/data/doc/TrackingTagsUniversalPixelPreviousVersions
- Retrieved: 2026-11-14
- Category: Guides

---

# Universal pixel: Previous versions

> **NOTE**: For details on the current version of the universal pixel, see Universal pixel.

The Trade Desk supports earlier versions of the universal pixel. The following table outlines key differences between the previous versions and the current version.

| What Changed | Current Version | Previous Versions |
| --- | --- | --- |
| Real-time web tracking | Use the universal pixel | Use the POST /track/realtimeconversion endpoint |
| Property names for dynamic parameters | - `value` - `currency` - `order_id` | - `v` - `vf` - `orderid` |
| Property names for data processing options | - `policies` - `region` | - `dpop` - `dpor` |
| Disabling cookie syncing | Set the `enableCookieSyncing` property to `false` | Set the `cookie_sync` property to `0` |

The following sections provide more details on previous versions of the dynamic parameters and setting for disabling cookie syncing.

## Universal pixel dynamic parameters

The following table explains each dynamic parameter in previous versions of the universal pixel.

| Parameter | Required? | Data Type | Description | Example | Notes |
| --- | --- | --- | --- | --- | --- |
| `v` | Optional | Float | The revenue value with a period (not a comma) as a decimal point. | `"v":12.99` | If revenue is passed, it will be available in all reports. |
| `vf` | Optional | String | The currency code for the revenue value. | `"vf":"USD"` | Revenue is calculated based on the advertiser's currency, not the code passed by the tag. |
| `orderid` | Optional | String | The advertiser ID for the order. | `"orderid":"abc123XyZ"` | N/A |
| `td1` – `td10` | Optional | String | Ten sequentially numbered custom dynamic parameters that can be used to provide additional context for the tracking tag. | `"td7":"Genre"` | These values can be tracked for reporting purposes, attributing on specific purchases, or retargeting based on the provided values using dynamic parameter rules. |

## Universal pixel data processing options

For US states with applicable privacy laws, in addition to passing users' opt-out choices as GPP strings to the platform through the workflow, you can also add data processing options, such as Limited Data Use (LDU), as dynamic parameters.

> **NOTE**: Users' opt-out choices passed to The Trade Desk are supported only for events from designated geographic areas with applicable laws.

To pass users' opt-out choices through previous versions of the universal pixel, add the applicable parameters to the pixel code by following the guidelines for inserting dynamic parameters. The following table explains the dynamic parameters for the data processing options.

| Parameter | Data Type | Description | Example | Notes |
| --- | --- | --- | --- | --- |
| `dpop` | String | A comma-separated list that specifies the data processing option policies. | `"dpop":"LDU"` | `LDU` (Limited Data Use) is currently the only supported value that signals the user's opt-out. |
| `dpor` | String | The data processing option region of the request in this format: `US` followed by a hyphen (-) and a two-letter state or territory abbreviation. | `"dpor"="US-CO"` (Colorado) | If the region is passed, The Trade Desk uses it to determine the enforcement of applicable regulations. Otherwise, we look up the geo location based on the IP address. |

## Cookie syncing

> **IMPORTANT**: Disabling cookie syncing can reduce the accuracy of user matching, affecting your ability to target and measure audiences. If necessary, disable it by adding a specific parameter in the pixel syntax.

By default, universal pixels have cookie syncing enabled, which is required for matching user identities across different ad tech platforms. Without it, advertisers and platforms might miss critical opportunities to identify and engage users accurately.

To disable cookie syncing in previous versions of the universal pixel, set the `cookie_sync` property to `0`, as shown in the following example:

```
<script src="https://js.adsrvr.org/up_loader.1.1.0.js" type="text/javascript"></script>
<script type="text/javascript">
  ttd_dom_ready( function() {
    if (typeof TTDUniversalPixelApi === 'function') {
      var universalPixelApi = new TTDUniversalPixelApi();
      universalPixelApi.init( "ADVERTISER_ID_PLACEHOLDER", ["UPIXEL_ID_PLACEHOLDER"], "https://insight.adsrvr.org/track/up",
      {
         "cookie_sync": "0"
      });
}
  });
</script>
```

## FAQs

The following is a list of frequently asked questions about previous versions of the universal pixel. Some answers in the FAQs for the current version also apply. For details, see Troubleshooting tips and FAQs.

#### How do I troubleshoot or get more insight into universal pixel issues?

To identify and troubleshoot issues, such as missing parameters, consent mismatches, or implementation errors, use the built-in debugging options for previous versions of the universal pixel. Here are steps for troubleshooting.

| Step | Description |
| --- | --- |
| 1 | Enable additional logging using one of these options: - In the JSON payload, set `debug` to `1`. - Add `upjs_debug=1` to the page URL. |
| 2 | Check browser developer tools for errors in the response payload from pixel-related network calls. Some errors are returned directly in the payload. |
