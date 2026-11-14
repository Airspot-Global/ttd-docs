# Universal pixel

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/data/doc/TrackingTagsUniversalPixel
- Retrieved: 2026-11-14
- Category: Guides

---

# Universal pixel

The Trade Desk universal pixel is a tracking tag that contains JavaScript (JS). As its name suggests, the universal pixel allows management of multiple processes with just one pixel added to an entire website. Conversion tracking tags can be created from a single universal pixel integration using the platform UI or API.

This guide provides developers with step-by-step instructions and best practices for integrating universal pixel tracking into advertising platforms.

Here’s what you need to know about The Trade Desk universal pixels:

- Universal pixels support all the functionality of a Static tracking tag, including dynamic parameters, while also providing the additional, optional functionality of pixel mappings.
- To optimize real-time web tracking, the universal pixel automatically sends the event or URL conversion data to the POST /track/realtimeconversion endpoint.
- Universal pixels are the recommended solution for passing consent-related information. For details, see Universal pixel workflow.
- Universal pixels can retarget web audiences without cookies by using Unified IDs (UIDs), a term that refers collectively to UID2 and EUID. For details, see UID support.
- To access the UID2 API, contact your Technical Account Manager.

The following sections provide details on how to implement and manage the universal pixel.

> **NOTE**: The Trade Desk supports older versions of the universal pixel. For details, see Universal pixels: Previous versions.

## Implementation

Here are guidelines for implementing universal pixels:

- The pixel code is the same for all advertisers, except for the advertiser ID and the universal pixel ID. Both are represented by the `ADVERTISER_ID_PLACEHOLDER` and `UPIXEL_ID_PLACEHOLDER` placeholders in the code samples.
- Universal pixels are asynchronous tags. This means that the two scripts in the pixel can be executed in any order. For details, see Pixel anatomy.
- To use a universal pixel, add its code to every page of the target website you want mapped, typically through a global footer or another site-wide mechanism. For details, see Universal pixel placement.
- To disable cookie syncing, add a specific parameter in the pixel syntax. For details, see Cookie syncing.
- You cannot use universal pixels as container tags, but you can host them inside container tags, for example, using Google Tag Manager, Floodlight, and so on.

The following sections cover the technical details of how the universal pixel works, how to configure and place it, and how to troubleshoot common issues.

## Workflow

Here's what you need to know about The Trade Desk universal pixel implementation:

- To ensure that page loading speed is not affected, the universal pixel is loaded only after the page has been fully loaded. If a user leaves the page before it is loaded ("bounces away"), the user will not be tracked.
- The universal pixel is fired when an `<iframe>` tag is loaded with a `src` attribute value constructed from the advertiser and universal pixel IDs from the pixel scripts, referrer URL, consent data strings, and other parameters. For details, see Universal pixel iframe anatomy.
- If consent is not provided for the Transparency and Consent Framework (TCF) and Global Privacy Platform (GPP) properties, identifiers for the event will not be logged.
- If UID is enabled, it is included in the `event` call.

The following sections describe the workflow with a diagram and step-by-step details. For a high-level tracking tag workflow overview, see Tracking tags.

> **NOTE**: In addition to passing users' opt-out choices as GPP strings to the platform, you can also add the data processing options `policies` and `region` as dynamic parameters.

The following diagram describes the universal pixel workflow, including when it triggers an `event` call to the POST /track/realtimeconversion endpoint with TDID and any stored consent parameters.

## Pixel anatomy

The universal pixel consists of two `<script>` tags, a pixel loading script and a pixel execution script. Use the appropriate pixel loading script based on whether you are implementing the pixel for The Trade Desk or Walmart DSP platform.

| Script tag | Description |
| --- | --- |
| The Trade Desk pixel loading `<script>` tag | Specifies the location of the `up_loader.3.0.0.js` file hosted on the The Trade Desk server. |
| Walmart DSP pixel loading `<script>` tag | Specifies the location of the `up_loader.3.0.0.js` file hosted on the Walmart DSP endpoint. |
| Pixel execution `<script>` tag | Contains the inline code that initiates the universal pixel and executes the loading instructions defined in the `up_loader.3.0.0.js` file. It also includes the advertiser ID and universal pixel ID used to identify and process data when the pixel fires. |

The following are code examples of a universal pixel with `ADVERTISER_ID_PLACEHOLDER` and `UPIXEL_ID_PLACEHOLDER` placeholders for the advertiser and universal pixel IDs.

**THE TRADE DESK**

Here's a code example of a universal pixel using The Trade Desk pixel loading `<script>` tag.

```
<script async src="https://js.adsrvr.org/up_loader.3.0.0.js"></script>
<script>
  window.ttdConversionEventsLayer = window.ttdConversionEventsLayer || [];
  function ttdConversionEvents() {window.ttdConversionEventsLayer.push(arguments);}
  ttdConversionEvents("init", { advertiserId: "ADVERTISER_ID_PLACEHOLDER", pixelIds: ["UPIXEL_ID_PLACEHOLDER"] });
  ttdConversionEvents("event", { advertiserId: "ADVERTISER_ID_PLACEHOLDER", pixelIds: ["UPIXEL_ID_PLACEHOLDER"] });
</script>
```

**WALMART**

Here's a code example of a universal pixel using the Walmart DSP pixel loading `<script>` tag.

```
<script async src="https://azjs.adsrvr.org/thetradedesk-ads/up_loader.3.0.0.js"></script>
<script>
  window.ttdConversionEventsLayer = window.ttdConversionEventsLayer || [];
  function ttdConversionEvents() {window.ttdConversionEventsLayer.push(arguments);}
  ttdConversionEvents("init", { advertiserId: "ADVERTISER_ID_PLACEHOLDER", pixelIds: ["UPIXEL_ID_PLACEHOLDER"] });
  ttdConversionEvents("event", { advertiserId: "ADVERTISER_ID_PLACEHOLDER", pixelIds: ["UPIXEL_ID_PLACEHOLDER"] });
</script>
```

## Cookie syncing

By default, universal pixels have cookie syncing enabled, which is required for matching user identities across different ad tech platforms. Without it, advertisers and platforms might miss critical opportunities to identify and engage users accurately.

> **IMPORTANT**: Disabling cookie syncing can reduce the accuracy of user matching, affecting your ability to target and measure audiences. If necessary, disable it by adding a specific parameter in the pixel syntax.

To disable cookie syncing, set the `enableCookieSyncing` property to `false`, as shown in the following example:

```
<script src="SOURCE_URL_PLACEHOLDER" type="text/javascript"></script>
<script>
  window.ttdConversionEventsLayer = window.ttdConversionEventsLayer || [];
  function ttdConversionEvents() {
    window.ttdConversionEventsLayer.push(arguments);
  }
  ttdConversionEvents("init", {
    advertiserId: "ADVERTISER_ID_PLACEHOLDER",
    pixelIds: ["UPIXEL_ID_PLACEHOLDER"],
    enableCookieSyncing: false
  });
  ttdConversionEvents("event", {
    "advertiserId": "ADVERTISER_ID_PLACEHOLDER",
    "pixelIds": ["UPIXEL_ID_PLACEHOLDER"]
  });
</script>
```

## Dynamic parameters

Depending on your needs, you can include the order ID, value, currency code, up to 10 dynamic parameters, and more to the universal pixel tracking tag.

> **NOTE**: In addition to passing users' opt-out choices to the platform as GPP strings through the workflow, you can also add the data processing options `policies` and `region` as dynamic parameters in US states with applicable privacy laws.

Here’s what you need to know if you want to modify a universal pixel by adding dynamic parameters:

- Always replace placeholder variables with actual values.
- The maximum number of characters stored for the `td` dynamic parameter values is 64. Longer values are logged but truncated in reports.
- Rules are not case sensitive.

To add dynamic parameters to a universal pixel:

1. Make a note of your advertiser ID and the universal pixel ID from your generated universal pixel code.
2. Open a new text file in your text editor and paste the universal pixel code template with the placeholders.
3. Delete the dynamic parameters that you do not need (including the trailing comma after the last parameter) and replace all placeholder variables with the actual values, including the `ADVERTISER_ID_PLACEHOLDER` and `UPIXEL_ID_PLACEHOLDER`. For example, see Universal pixel example with dynamic parameters.

> **TIP**: For more customization options, see the FAQs.

### Template

The following is the universal pixel code template with dynamic parameter placeholders:

```
<script async src="SOURCE_URL_PLACEHOLDER"></script>
<script>
  window.ttdConversionEventsLayer = window.ttdConversionEventsLayer || [];
  function ttdConversionEvents() {window.ttdConversionEventsLayer.push(arguments);}
  ttdConversionEvents("init", { advertiserId: "ADVERTISER_ID_PLACEHOLDER", pixelIds: ["UPIXEL_ID_PLACEHOLDER"] });
  ttdConversionEvents("event", {
    "advertiserId": "ADVERTISER_ID_PLACEHOLDER",
    "pixelIds": ["UPIXEL_ID_PLACEHOLDER"],
    "order_id": "ORDER_ID_PLACEHOLDER",
    "value": REVENUE_AMOUNT_PLACEHOLDER,
    "currency": "CURRENCY_CODE_PLACEHOLDER",
    "td1": "TD_1_VALUE_PLACEHOLDER",
    "td2": "TD_2_VALUE_PLACEHOLDER",
    "td3": "TD_3_VALUE_PLACEHOLDER",
    "td4": "TD_4_VALUE_PLACEHOLDER",
    "td5": "TD_5_VALUE_PLACEHOLDER",
    "td6": "TD_6_VALUE_PLACEHOLDER",
    "td7": "TD_7_VALUE_PLACEHOLDER",
    "td8": "TD_8_VALUE_PLACEHOLDER",
    "td9": "TD_9_VALUE_PLACEHOLDER",
    "td10": "TD_10_VALUE_PLACEHOLDER",
    "data_processing_option": {
      "policies": ["DATA_PROCESSING_OPTION_POLICIES_PLACEHOLDER"],
      "region": "DATA_PROCESSING_OPTION_REGION_PLACEHOLDER"
    }
  });
</script>
```

### Example

Here's a complete example of a universal pixel with dynamic parameters and all placeholder values replaced:

```
<script async src="SOURCE_URL_PLACEHOLDER"></script>
<script>
  window.ttdConversionEventsLayer = window.ttdConversionEventsLayer || [];
  function ttdConversionEvents() {window.ttdConversionEventsLayer.push(arguments);}
  ttdConversionEvents("init", { "advertiserId": "rt7ftg2", "pixelIds": ["ejs57s6"]});
  ttdConversionEvents("event", {
    "advertiserId": "rt7ftg2",
    "pixelIds": ["ejs57s6"],
    "order_id": "abc123XyZ",
    "value": 12.99,
    "currency": "USD",
    "td1": "AlbumName",
    "td2": "Artist",
    "td3": "Genre",
    "td4": "DigitalDownload",
    "td5": "new_customer",
    "data_processing_option": {
      "policies": ["LDU"],
      "region": "US-CO"
    }
  });
</script>
```

### Reference

The following table describes each dynamic parameter available for the universal pixel.

| Parameter | Required? | Data Type | Description | Notes |
| --- | --- | --- | --- | --- |
| `order_id` | Optional | String | The advertiser ID for the order. | None. |
| `value` | Optional | Float | The revenue value with a period (not a comma) as a decimal point. | If revenue is passed, it will be available in all reports. |
| `currency` | Optional | String | The currency code for the revenue value. | Revenue is calculated based on the advertiser's currency, not the code passed by the tag. |
| `td1` – `td10` | Optional | String | Ten sequentially numbered dynamic parameters that can be used to provide additional context for the tracking tag. | These values can be tracked for reporting purposes, attributing on specific purchases, or retargeting based on the provided values using dynamic parameter rules. |

> **NOTE**: You can also add the data processing options `policies` and `region` as dynamic parameters in US states with applicable privacy laws.

#### Data processing options

For US states with applicable privacy laws, in addition to passing users' opt-out choices as GPP strings to the platform through the workflow, you can also add data processing options, such as Limited Data Use (LDU), as dynamic parameters.

> **NOTE**: Users' opt-out choices passed to The Trade Desk are supported only for events from designated geographic areas with applicable laws.

To pass users' opt-out choices through a universal pixel, add the applicable parameters to the pixel code by following the guidelines for inserting dynamic parameters. The following table explains the dynamic parameters for the data processing options.

| Parameter | Data Type | Description | Example | Notes |
| --- | --- | --- | --- | --- |
| `policies` | String | A comma-separated list that specifies the data processing option policies. | `"policies":"LDU"` | `LDU` (Limited Data Use) is currently the only supported value that signals the user's opt-out. |
| `region` | String | The data processing option region in the request formatted as follows: `US` followed by a hyphen (-) and a two-letter state or territory abbreviation. | `"region":"US-CO"` (Colorado) | If the region is passed, The Trade Desk uses it to determine the enforcement of applicable regulations. Otherwise, The Trade Desk looks up the geo location based on the IP address. |

## iframe Anatomy

The Trade Desk universal pixel `<iframe>` element is created when the tag is fired. The iframe includes the following attributes with placeholder variables:

- The iframe `id` attribute with the `universal_pixel_UPIXEL_ID_PLACEHOLDER` value.
If the same universal pixel is manually placed on the same page multiple times, the existing iframe containing the same ID will be updated without slowing down the user’s browser.
- The `src` attribute with the pixel URL as its value, which has the following syntax, including four required query parameters:
`https://insight.adsrvr.org/track/TAG_TYPE_PLACEHOLDER?adv=ADVERTISER_ID_PLACEHOLDER&ref=REFERRER_URL_PLACEHOLDER&upid=UPIXEL_ID_PLACEHOLDER&upv=UPIXEL_VERSION_PLACEHOLDER`
- The title, style, size, and other standard iframe HTML attributes.

For example:

```
<iframe id="universal_pixel_hc7ihke" allowtransparency="true" height="0" width="0" style="display:none;" src="https://insight.adsrvr.org/track/cei?adv=ru6qq3d&ref=https%3A%2F%2Fwww.thetradedesk.com%2F&upid=hc7ihke&upv=3.0.0" title="TTD Universal Pixel"></iframe>
```

The following table explains the tracking tag type path parameter and the required and optional query parameters in the `src` attribute value of the iframe. For details about optional dynamic parameters, see Add dynamic parameters to universal pixels.

| Parameter | Required? | Data Type | Description | Example | Notes |
| --- | --- | --- | --- | --- | --- |
| `TAG_TYPE_PLACEHOLDER` | Required | String | A path parameter with the value of `up`, which indicates the type of the tracking tag, namely, the universal pixel. | `//insight.adsrvr.org/track/up/` | N/A |
| `adv` | Required | String | The platform ID for the advertiser that owns the tracking tag. | `adv=4w1ba8e` | N/A |
| `ref` | Required | String | The URL of the referrer specified in the header sent by the browser, typically the page from which the tag was fired. | `ref=https%3A%2F%2Fwww.thetradedesk.com%2F` Parsed as `https://www.thetradedesk.com/` | This parameter value is run through all URL mappings defined for the universal pixel ID. Here's what you need to know: - All matched URLs are logged as individually fired tracking tags. - If no patterns are matched, no tags are logged. For details, see Universal pixel mappings. |
| `upid` | Required | String | The ID of the universal pixel from the inline script in the universal pixel code. For details, see Pixel anatomy. | `upid=hc7ihke` | N/A |
| `upv` | Required | String | The Trade Desk version number of the universal pixel. | `upv=3.3.0` | N/A |

## URL mappings

To create universal pixel mappings that match against the referrer URL, you can use either the platform UI or API. By default, the pixel automatically extracts the referrer URL from the page where it is triggered, but you can also manually set this parameter during the initial call.

URL mappings provide more granular retargeting and attribution, enabling you to test strategies without adding extra pixels and helping to reduce pixel installation errors. Here’s what you need to know about pixel mappings, including key details and recommendations:

- URL mappings can be defined as exact-match or wildcard mappings. You can create unlimited exact-match mappings or 100 wildcard mappings.
- By default, all newly created universal pixels have a default URL mapping applied that consists of a "catch-all" wildcard. This allows tracking all pages on which the universal pixel is placed. If you remove this mapping, any unmatched mappings will be discarded. For details, see Mapping patterns.
- When the universal pixel is fired on a given webpage, the page URL passed in the `ref` parameter of the tracking call is run through all URL mappings defined for the specified universal pixel ID.
- Each match is defined as a separate tracking tag, which allows creating, editing, and removing tracking tags dynamically in both the UI and API, without any additional universal pixel code changes on the website.
- A tracking log is created for each matched mapping.
- To specify the amount of revenue to be reported on and its currency, use the optional dynamic parameter `value` for revenue. For details, see Add dynamic parameters to universal pixels.
- When creating pixel mappings, enable household extension (the `HouseholdEnabled` property in the POST /v3/trackingtag endpoint, if using the API).

> **NOTE**: Updating mappings using the PUT /v3/tracking/universalpixel endpoint will archive any tracking tags that become unmapped.

### Mapping patterns

There are two types of matches that you can define for the universal pixel URL matching:

- **Exact match**: Maps URL strings exactly one to one. For example, if the match is defined as `http://www.thetradedesk.com/` only the `thetradedesk.com` home page will be a possible match.
- **Wildcard match**: Uses asterisks (*) to replace parts of a URL to map to several URL strings that match a higher-level context.

The following table provides several wildcard match examples.

| Wildcard Pattern Example | Possible Matches |
| --- | --- |
| `*` | Any page on the website. |
| `*thetradedesk.com/*` | The homepage `thetradedesk.com` (`http` or `https`) and any page below it. |
| `*/about-us/` | Any page ending in `about-us`, but nothing below it. |
| `*thetradedesk.com/about-us/*` | The `thetradedesk.com/about-us/` page and any page below it, for example: `thetradedesk.com/about-us/` `thetradedesk.com/about-us/leadership/` `thetradedesk.com/about-us/careers/` |
| `*http://www.thetradedesk.com/` | No pages may be matched. **TIP**: To avoid issues when designing wildcard patterns for URLs, it's best to omit the schema. |

## Pixel placement

The universal pixel must be placed into the shared code of a webpage, such as a footer, a header, a persistent navigation menu, or another site-wide mechanism.

Here’s what you also need to keep in mind when installing the universal pixel:

- The target website must support JavaScript.
- The universal pixel can be put into a tag manager that supports JavaScript.
- The universal pixel must not be used as a container tag.

## UID support

For audience targeting, seeds, and measurement, you can use universal pixels to retarget web audiences without cookies by using UIDs. For details, see UID support.

> **NOTE**: As part of your universal pixel implementation workflow, UIDs can be used when triggering event calls to the POST /track/realtimeconversion endpoint.

## CSP requirements

A CSP is in your site's HTTP response header or in a `<meta>` tag in the page `<head>` tag. A different team usually manages a CSP than the one who implements the pixel. You do not configure the CSP in the pixel code itself.

If your website enforces a CSP, make sure it has the required domains. This ensures that pixel scripts and calls load and fire correctly. If a domain is missing, you might receive an error such as "Refused to connect because it violates the following Content Security directive."

CSPs can differ in form and function, with different directives. The following table lists the directives and domains required for universal pixels.

| Domain | Directive | Notes |
| --- | --- | --- |
| `js.adsrvr.org` | `script-src` | `script-src` also requires the `'unsafe-inline'` keyword. The universal pixel uses inline JavaScript code, and without this keyword, the pixel code can't execute. |
| `insight.adsrvr.org` | `frame-src` `connect-src` (real-time conversions) | - If you are using real-time conversions, add this domain to the `connect-src` directive. - If your CSP blocks the real-time conversions call under the `connect-src` directive, The Trade Desk still collects your conversions. It does this by reverting the universal pixel to its original version and using the Real-time conversion events API instead. |
| `match.adsrvr.org` | `frame-src` | None. |
| `js.adsrvr.org` | `script-src-elem` | Include only if your policy specifies `script-src-elem` separately from `script-src`. |

> **NOTE**: Cookie syncing for the universal pixel happens inside its own iframe, which is already covered by the domains inside `frame-src`. No additional domains are required.

The following is an example CSP configured for a universal pixel with UID support and a static tracking tag.

```
Content-Security-Policy:
  script-src 'self' 'unsafe-inline' js.adsrvr.org cdn.prod.uidapi.com;
  script-src-elem 'self' js.adsrvr.org cdn.prod.uidapi.com;
  img-src 'self' insight.adsrvr.org match.adsrvr.org;
  frame-src 'self' insight.adsrvr.org match.adsrvr.org;
  connect-src 'self'
    insight.adsrvr.org
    prod.uidapi.com
    *.prod.uidapi.com
    operator-integ.uidapi.com;
```

> **NOTE**: The leading asterisk (`*`) in `*.prod.uidapi.com` is an intentional wildcard that matches any subdomain of `prod.uidapi.com`.

For the domains required for static tracking tags, see Static tracking tag. For the domains required for UID support, see UID support.

## Troubleshooting tips and FAQs

If an error occurs when loading a universal pixel, make sure to check the following before contacting support:

- All placeholder variables have been replaced with the appropriate values.
- The scripts for pixel loading and execution in the universal pixel code are in the correct order. For details, see Pixel anatomy.
- The universal pixel is placed into the shared code of a webpage. For details, see Universal pixel placement.

## FAQs

The following is a list of frequently asked questions about the universal pixel. For UID support FAQs, see UID support FAQs.

#### Does adding dynamic parameters require editing of the universal pixel code?

Yes, you need to edit the pixel execution inline `<script>` tag in the universal pixel code. For details, see Add dynamic parameters to universal pixels.

#### Are universal pixel mappings required to capture events sent to The Trade Desk?

Yes. At least one universal pixel mapping must be configured for The Trade Desk to capture any events sent to us. If no mappings are in place, we cannot match conversions and all conversion events will be dropped.

#### What does the "ttd_dom_ready not defined" error mean?

The `ttd_dom_ready not defined` error means that the script for pixel execution in the universal pixel code has been executed before the script for pixel loading was run. This may occur, for example, when the `up_loader.3.0.0.js` file is not available or has not been loaded yet, or if the pixel loading script is not present altogether.

#### Why was the universal pixel never fired?

This may occur if there were errors in the code or the scripts were not in the correct order. For help troubleshooting, contact your Technical Account Manager.

#### Can cookie syncing be disabled for the universal pixel?

Yes. For details, see Cookie syncing.

#### Can I use the universal pixel on a single-page application?

Yes. The universal pixel supports single-page applications (SPAs), provided you use version 3.0.0 of the loader script. The following table shows the supported loader script and the version to replace for each platform.

| Platform | Supported loader script | Upgrade if using |
| --- | --- | --- |
| The Trade Desk | `js.adsrvr.org/up_loader.3.0.0.js` | `js.adsrvr.org/up_loader.1.1.0.js` |
| Walmart DSP | `azjs.adsrvr.org/thetradedesk-ads/up_loader.3.0.0.js` | `azjs.adsrvr.org/thetradedesk-ads/up_loader.1.1.0.js` |

For code examples, see Pixel anatomy.

#### How do I troubleshoot or get more insight into universal pixel issues?

To identify and troubleshoot issues, such as missing parameters, consent mismatches, or implementation errors, use the built-in debugging options in universal pixels. Here are steps for troubleshooting.

| Step | Description |
| --- | --- |
| 1 | Enable additional logging using one of these options: - In the initialization call, set `enableDebug` to `true` for detailed output in the browser console and response payload. - Add `upjs_debug=1` to the page URL. |
| 2 | Check browser developer tools for errors in the response payload from pixel-related network calls. Some errors are returned directly in the payload. |

#### Does the universal pixel support "dwell time"?

Yes. In some scenarios, you might need to add "dwell time," which delays the execution of an event until a specified duration has passed, such as 10 seconds after a page loads. To implement dwell time, run the event code within a timeout function, as shown in the following code example:

```
window.onload = function () {
    setTimeout(function () {
        ttdConversionEvents("event", { });
    }, 10000); // delay in milliseconds
};
```

#### Is it better to use a single universal pixel for my entire website instead of multiple page-specific pixels?

It’s best practice to install a single universal pixel on your website and use URL mappings for tracking specific pages. Placing multiple universal pixels can cause tracking conflicts, with all activity logged under just one pixel.

When a single universal pixel is placed across your domain, you can use URL mappings to track visits to specific pages, such as:

- `www.thetradedesk.com/`
- `www.thetradedesk.com/about-us`

If multiple universal pixels are added to different pages, this may cause The Trade Desk to track only one pixel. For example, if `UPIXEL_ID_PLACEHOLDER_1` is placed on `thetradedesk.com`, and `UPIXEL_ID_PLACEHOLDER_2` is placed on `thetradedesk.com/about_us`, visits to both pages may be recorded under `UPIXEL_ID_PLACEHOLDER_1` alone.

> **TIP**: Use a single universal pixel with URL mappings whenever possible. If multiple pixels are required, include the universal pixel ID in each event trigger so all pixels can capture site visit data.

Here's a code sample for adding `UPIXEL_ID_PLACEHOLDER_1` to an event trigger for one page or set of URL mappings:

```
<script async src="SOURCE_URL_PLACEHOLDER"></script>
<script>
  window.ttdConversionEventsLayer = window.ttdConversionEventsLayer || [];
  function ttdConversionEvents() {window.ttdConversionEventsLayer.push(arguments);}
  ttdConversionEvents("init", { advertiserId: "ADVERTISER_ID_PLACEHOLDER", pixelIds: ["UPIXEL_ID_PLACEHOLDER_1"]})
  ttdConversionEvents("event", {pixel_ids:["UPIXEL_ID_PLACEHOLDER_1"]});
</script>
```

And here's a code sample for adding `UPIXEL_ID_PLACEHOLDER_2` to an event trigger for a different page or set of URL mappings:

```
<script async src="SOURCE_URL_PLACEHOLDER"></script>
<script>
  window.ttdConversionEventsLayer = window.ttdConversionEventsLayer || [];
  function ttdConversionEvents() {window.ttdConversionEventsLayer.push(arguments);}
  ttdConversionEvents("init", { advertiserId: "ADVERTISER_ID_PLACEHOLDER", pixelIds: ["UPIXEL_ID_PLACEHOLDER_2"] });
  ttdConversionEvents("event", { advertiserId: "ADVERTISER_ID_PLACEHOLDER", pixelIds: ["UPIXEL_ID_PLACEHOLDER_2"] });
</script>
```

#### How do I trigger multiple pixel IDs on a single website?

It's best to use a single pixel with multiple rules. However, if you need multiple pixels for the same advertiser, you can combine them into one pixel trigger, as shown in the following example.

```
<script async src="SOURCE_URL_PLACEHOLDER"></script>
<script>
  window.ttdConversionEventsLayer = window.ttdConversionEventsLayer || [];
  function ttdConversionEvents() {window.ttdConversionEventsLayer.push(arguments);}
  ttdConversionEvents("init", { advertiserId: "ADVERTISER_ID_PLACEHOLDER", pixelIds: ["UPIXEL_ID_PLACEHOLDER_01", "UPIXEL_ID_PLACEHOLDER_02", ...] });
  ttdConversionEvents("event", { advertiserId: "ADVERTISER_ID_PLACEHOLDER", pixelIds: ["UPIXEL_ID_PLACEHOLDER_01", "UPIXEL_ID_PLACEHOLDER_02", ...] });
</script>
```

If you need to trigger different pixels at different times or in response to different events, call the event trigger when needed, such as on page load or within a JavaScript function, as shown in the following example.

```
<script async src="SOURCE_URL_PLACEHOLDER"></script>
<script>
  window.ttdConversionEventsLayer = window.ttdConversionEventsLayer || [];
  function ttdConversionEvents() {window.ttdConversionEventsLayer.push(arguments);}
  ttdConversionEvents("init", { advertiserId: "ADVERTISER_ID_PLACEHOLDER", pixelIds: ["UPIXEL_ID_PLACEHOLDER_01", "UPIXEL_ID_PLACEHOLDER_02", ...] });
</script>
<script>
  // Fire UPIXEL_ID_PLACEHOLDER_01 on page load
  ttdConversionEvents("event", { advertiserId: "ADVERTISER_ID_PLACEHOLDER", pixelIds: ["UPIXEL_ID_PLACEHOLDER_01"] });
</script>
<button onclick="myFunction()">Click me</button>
<script>
  // Fire UPIXEL_ID_PLACEHOLDER_02 on button trigger
  function myFunction() {
    ttdConversionEvents("event", { advertiserId: "ADVERTISER_ID_PLACEHOLDER", pixelIds: ["UPIXEL_ID_PLACEHOLDER_02"] });
  }
</script>
```

#### Are both init and event calls needed for the universal pixel?

Yes. The `init` call sets up the universal pixel for your advertiser and pixel configuration, and the `event` call sends tracking data to The Trade Desk. Both are required for the universal pixel to fire successfully.

#### How do I use the universal pixel in situations where I need pure JavaScript, such as with Adobe Launch or Data Collection?

If you're using tools that require pure JavaScript (not HTML), such as Adobe Launch, use the following alternative code:

```
(function () {
  var el = document.createElement('script');
  el.src = 'SOURCE_URL_PLACEHOLDER';
  el.async = true;
  window.ttdConversionEventsLayer = window.ttdConversionEventsLayer || [];
  function ttdConversionEvents() {
    window.ttdConversionEventsLayer.push(arguments);
  }
  ttdConversionEvents("init", {
    advertiserId: "ADVERTISER_ID_PLACEHOLDER",
    pixelIds: ["UPIXEL_ID_PLACEHOLDER"]
  });
  ttdConversionEvents("event", {
    advertiserId: "ADVERTISER_ID_PLACEHOLDER",
    pixelIds: ["UPIXEL_ID_PLACEHOLDER"]
  });
  document.head.appendChild(el);
})();
```

#### I want to use the universal pixel to track item-level conversion events and page views using the Product Catalog feature. What’s the best way to do this?

To track item-level conversion events using the Product Catalog feature, use the event tracking tag ID together with the universal pixel.

The following code samples show how to track item-level conversion events, page views, and a combination of both.

Here's a code sample for tracking item-level conversion events with an event tracking tag ID:

```
<script async src="SOURCE_URL_PLACEHOLDER"></script>
<script>
  window.ttdConversionEventsLayer = window.ttdConversionEventsLayer || [];
  function ttdConversionEvents() {window.ttdConversionEventsLayer.push(arguments);}
  ttdConversionEvents("init", { merchantId: MERCHANT_ID_PLACEHOLDER, pixelIds: ["EVENT_TRACKING_TAG_ID_PLACEHOLDER"] });
  ttdConversionEvents("event", { merchantId: MERCHANT_ID_PLACEHOLDER, pixelIds: ["EVENT_TRACKING_TAG_ID_PLACEHOLDER"] });
</script>
```

Here's a code sample for tracking page views with the universal pixel ID:

```
<script async src="SOURCE_URL_PLACEHOLDER"></script>
<script>
  window.ttdConversionEventsLayer = window.ttdConversionEventsLayer || [];
  function ttdConversionEvents() {window.ttdConversionEventsLayer.push(arguments);}
  ttdConversionEvents("init", { advertiserId: "ADVERTISER_ID_PLACEHOLDER", pixelIds: ["UPIXEL_ID_PLACEHOLDER"] });
  ttdConversionEvents("event", { advertiserId: "ADVERTISER_ID_PLACEHOLDER", pixelIds: ["UPIXEL_ID_PLACEHOLDER"] });
</script>
```

Here's a code sample that combines both identifiers in a single JavaScript code:

```
<script async src="SOURCE_URL_PLACEHOLDER"></script>
<script>
  window.ttdConversionEventsLayer = window.ttdConversionEventsLayer || [];
  function ttdConversionEvents() {window.ttdConversionEventsLayer.push(arguments);}
  ttdConversionEvents("init", { advertiserId: "ADVERTISER_ID_PLACEHOLDER", pixelIds: ["EVENT_TRACKING_TAG_ID_PLACEHOLDER", "UPIXEL_ID_PLACEHOLDER"]})
  ttdConversionEvents("event", { advertiserId: "ADVERTISER_ID_PLACEHOLDER", pixel_ids: ["EVENT_TRACKING_TAG_ID_PLACEHOLDER", "UPIXEL_ID_PLACEHOLDER"]});
</script>
```

The following is a more complex code example that combines the identifiers and tracks detailed purchase events:

```
<script async src="SOURCE_URL_PLACEHOLDER"></script>
<script>
  window.ttdConversionEventsLayer = window.ttdConversionEventsLayer || [];
  function ttdConversionEvents() {window.ttdConversionEventsLayer.push(arguments);}
  ttdConversionEvents("init", { advertiserId: "ADVERTISER_ID_PLACEHOLDER", pixelIds: ["EVENT_TRACKING_TAG_ID_PLACEHOLDER", "UPIXEL_ID_PLACEHOLDER"] });
  ttdConversionEvents("event", {
    "advertiserId": "ADVERTISER_ID_PLACEHOLDER",
    "pixelIds": ["EVENT_TRACKING_TAG_ID_PLACEHOLDER", "UPIXEL_ID_PLACEHOLDER"],
    "currency": "USD",
    "order_id": "ABC123",
    "value": 29.98,
    "event_name": "purchase",
    "items":[
      {
        "item_code": "203319203",
        "name": "Blue T-Shirt",
        "qty": 1,
        "price": 19.99,
        "cat": "Clothes"
      },
      {
        "item_code": "2234567892",
        "name": "Blue Shorts",
        "qty": 1,
        "price": 9.99,
        "cat": "Clothes"
      }
    ]
  });
</script>
```

#### I am using dynamic parameters in my universal pixel, but it's not firing. Why is that?

When using dynamic parameters (meaning JavaScript variables, not strings), define them on the page before executing the pixel. If not, the browser generates an error, preventing the pixel from firing.

Here's a code example with no variables defined.

```
<script async src="SOURCE_URL_PLACEHOLDER"></script>
<script>
    window.ttdConversionEventsLayer = window.ttdConversionEventsLayer || [];
    function ttdConversionEvents() {
        window.ttdConversionEventsLayer.push(arguments);
    }
    ttdConversionEvents("init", {
        advertiserId: "ADVERTISER_ID_PLACEHOLDER",
        pixelIds: ["UPIXEL_ID_PLACEHOLDER"]
    });
    ttdConversionEvents("event", {
        "advertiserId": "ADVERTISER_ID_PLACEHOLDER",
        "pixelIds": ["UPIXEL_ID_PLACEHOLDER"],
        "td1": EVENT_EXAMPLE_01,
        "td2": EVENT_EXAMPLE_02
    });
</script>
```

In the example, `EVENT_EXAMPLE_01` and `EVENT_EXAMPLE_02` are dynamic parameters that must be defined in your code, as shown in the following example:

```
const EVENT_EXAMPLE_01 = 'VALUE_PLACEHOLDER';
```

If these parameters are not set, JavaScript cannot resolve them and the script will fail before sending the pixel event.

#### How do I configure the event tracking tag ID?

The event tracking tag ID is configured in the platform UI (`pixel_id`). For details, see Item-Level Event Tracking in the Knowledge Portal (requires a platform login).

#### What URL do I use instead of SOURCE_URL_PLACEHOLDER?

Use the URL that specifies the location of the `up_loader.3.0.0.js` file on The Trade Desk server. For details, see Pixel anatomy.

#### If I use a CSP, do I need to add anything to an allowlist?

Yes. For details on which domains to add to your allowlist, see CSP requirements.

#### My site uses a CSP. Do I need to add anything to allow cookie syncing?

It depends on your pixel type. For details, see CSP requirements.

#### Where do I configure my site's CSP?

In your site's HTTP response header or a `<meta>` tag in the page's `<head>`, not in the pixel code itself. For details, see CSP requirements.

To learn more about implementing UIDs for the universal pixel, see UID support.
