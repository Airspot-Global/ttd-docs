# Static tracking tag

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/data/doc/TrackingTagsStatic
- Retrieved: 2026-11-14
- Category: Guides

---

# Static tracking tag

A static tracking tag contains an invisible image (1x1 pixel in size), which is loaded from The Trade Desk `adsrvr.org` tracking domain at the user’s browser request when the user visits a page. The request includes certain IDs, which identify the advertiser and the tag loaded. It also allows the server to place a tracking cookie in the user's browser that has requested a given tracking tag for the advertiser. For the tracking tag workflow overview, see Tracking tags.

> **NOTE**: Universal pixels are more commonly used as they support all the functionality of static tracking tags while also providing the optional functionality of pixel mappings and allowing more efficient implementation.

The following sections walk you through the process of building the static tracking tag and deploying it to your website.

## Build the tag

To build the static tracking tag, you must include the required query parameters in the `src` property of the image HTML tag. The following table lists the query parameters you can include when building a static tracking tag.

| Query parameters | Required? | Description |
| --- | --- | --- |
| Base parameters | Required | Identify the advertiser and tag, and can initiate cookie syncing. |
| Dynamic parameters | Optional | Pass additional context about the tracking event. |
| Users' choices | Optional | Pass users' consent or opt-out choices for GDPR, GPP, or other regional privacy regulations. **NOTE**: These parameters are only applicable to events from designated geographic areas with applicable laws. |

### Static tracking tag syntax

The following is an example of a static tracking tag with five optional dynamic parameters:

```
<img src="//insight.adsrvr.org/track/pxl/?adv=4w1ba8e&ct=0:kcvg8kk&fmt=3&v=12.99vf=GBP&orderid=abc123XyZ&td1=AlbumName&td2=Artist&td3=Genre&td4=DigitalDownload&td5=new_customer" height="1" width="1" style="border-style:none;" alt="" />
```

The URL syntax in the `src` property of the image HTML tag follows the same basic syntax explained in Tracking tags. In other words, it consists of the following two main parts (with the variable-value parameters indicated by the curly braces {}):

- The server URL, which includes the tag type but may omit the http protocol:
`//insight.adsrvr.org/track/{TAG_TYPE}/`
- Tracking tag required and optional query parameters, included as key=value pairs, listed after the question mark (?) and separated by ampersands (&) from each other:
`adv=ADVERTISER_ID_PLACEHOLDER&ct=0:TRACKING_TAG_ID_PLACEHOLDER&fmt=3`

The following table explains the tracking tag path parameter and the required query parameters in the `src` attribute value. You can also add optional dynamic parameters, including the user's opt-out choices per GDPR, GPP, and other regulations, as explained in Add dynamic parameters.

| Parameter | Required? | Data Type | Description | Default value | Example | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `{TAG_TYPE}` | Required | String | A path parameter that indicates the type of the tracking tag. The only value currently supported for all static tag types is `pxl`. | `pxl` | `//insight.adsrvr.org/track/pxl/` | Deprecated but still in use values may include the following: `conv` (conversion), `envt` (retargeting), and `imp` (impression). |
| `adv` | Required | String | The platform ID for the advertiser that owns the tracking tag. | N/A | `adv=4w1ba8e` | N/A |
| `ct` | Required | Integer | The image pixel attribute. | `0` | `ct=0` | This is a legacy parameter; the value doesn’t change. |
| `{TRACKING_TAG_ID}` | Required | String | The platform ID for the tracking tag. | N/A | `ct=0:kcvg8kk` | N/A |
| `fmt` | Required | Integer | The cookie syncing setting: `3`—initiate cookie syncing `4`—stop cookie syncing **IMPORTANT**: If you choose to stop cookie syncing, no new cookies will be set. | `3` | `fmt=3` | If your website uses a CSP and you initiate cookie syncing, you must specify the domains of each cookie sync partner in the `img-src` directive. For details, see CSP requirements. |

### Add dynamic parameters to static tracking tags

If needed, you can add up to ten custom dynamic parameters, a revenue value, a currency code, and the order ID to the static tracking tag.

> **NOTE**: You can also signal users' choices from designated geographic areas with applicable laws.

Here’s what you need to know if you want to modify a static tracking tag by adding dynamic parameters:

- Do not use the iframe format for passing parameters dynamically in a tag.
- Always replace placeholder variables in curly braces {} with the actual values with no braces.
- Use ampersands (&) to separate parameter key-value pairs and an equal sign (=) to separate the key and its value in each pair.
- Do not include any spaces.
- The maximum number of characters stored for the `td` custom dynamic parameter values is 64.

The following is a snippet of the `src` attribute value with dynamic parameters and placeholder values in curly braces.

```
&v={REVENUE}&vf={CURRENCY}&orderid={ORDER_ID}&td1={VALUE_1}&td2={VALUE_2}&td3={VALUE_3}&td4={VALUE_4}&td5={VALUE_5}&td6={VALUE_6}&td7={VALUE_7}&td8={VALUE_8}&td9={VALUE_9}&td10={VALUE_10}
```

The following table explains each dynamic parameter.

| Parameter | Required? | Data Type | Description | Example | Notes |
| --- | --- | --- | --- | --- | --- |
| `v` | Optional | Float | The revenue value with a period (not a comma) as a decimal point. | `v=12.99` | If revenue is passed, it will be available in all reports. |
| `vf` | Optional | String | The currency code for the revenue value. | `vf=USD` | Revenue is calculated based on the advertiser's currency, not the code passed by the tag. |
| `orderid` | Optional | String | The advertiser ID for the order. | `orderid=abc123XyZ` | N/A |
| `td1` – `td10` | Optional | String | Ten sequentially numbered custom dynamic parameters that can be used to provide additional context for the tracking tag. | `td7=Genre` | These values can be tracked for reporting purposes, attributing on specific purchases, or retargeting based on the provided values using dynamic parameter rules. |

### Pass users' choices in static tracking tags

To comply with General Data Protection Regulation (GDPR) and applicable state laws in the US, The Trade Desk static tracking tag supports the passing of users' choices via the Transparency and Consent Framework (TCF) and Global Privacy Platform (GPP) strings, as well as other data processing options such as the Limited Data Use (LDU) attribute. Here's what you need to know about these parameters:

- The parameters for processing users' choices are supported only for events from the designated geographic areas where applicable laws and regulations are in effect.
- The placeholder values for the GDPR or GPP parameters must be replaced with the appropriate macros, not any specific values. Be sure to work with your CMP to ensure that the correct values are being passed.
- In the US, we offer two ways for you to indicate users' opt-out choices in pixels:

  - By using the `gpp_consent` parameter.
  - By using the `dpop` and `dpor` parameters.

- If both parameters are sent, we process an opt-out even if only one of them indicates so.
- To pass users' choices through a static tag, add the applicable parameters to the `src` attribute value of the tag by following the guidelines for inserting dynamic parameters.

The following table lists the available parameters for passing users' choice information.

| Parameter | Data Type | Policy | Description | Example | Notes |
| --- | --- | --- | --- | --- | --- |
| `gdpr` | String | GDPR | Indicates whether the GDPR applies. | `gdpr={APPLICABLE:0\|1}` | If set to `true` (`1`), the policy is enforced. |
| `gdpr_consent` | String | GDPR | Indicates the user’s choices when the GDPR applies and TCF policies are in effect. | `gdpr_consent={IAB_CONSENT_STRING}` | The Transparency and Consent String (TC String) is a technical component of the IAB Europe Transparency and Consent Framework. |
| `gpp_consent` | String | GPP | The user's opt-out choice when the GPP policies are in effect. | `gpp_consent={IAB_CONSENT_STRING}` | None. |
| `dpop` | String | US state privacy regulations | A comma-separated list that specifies the data processing option policies. | `dpop=LDU` | `LDU` (Limited Data Use) is currently the only supported value that signals the user's opt-out. |
| `dpor` | String | US state privacy regulations | The data processing option region of the request in this format: `US` followed by a hyphen (-) and a two-letter state or territory abbreviation. | `dpor=US-CO` (Colorado) | If the region is passed, The Trade Desk uses it to determine the enforcement of applicable regulations. Otherwise, we look up the geo location based on the IP address. |

 Here's an example with the GDPR parameters and placeholder values:

```
<img height="1" width="1" style="border-style:none;" alt="" src="//insight.adsrvr.org/track/pxl/?adv=lxd3raf&ct=0:ikqrr56&fmt=3&gdpr={APPLICABLE:0|1}&gdpr_consent={IAB_CONSENT_STRING}"/>
```

 Here's an example with the Limited Data Use data processing options:

```
<img height="1" width="1" style="border-style:none;" alt="" src="//insight.adsrvr.org/track/pxl/?adv=lxd3raf&ct=0:ikqrr56&fmt=3&dpop=LDU&dpor=US-CO"/>
```

If you need help or require additional information, be sure to contact your Technical Account Manager for support.

## Deploy the tag

After you build your tracking tag, you can deploy it to your website. The following table outlines the tasks for deploying a static tracking tag.

| Task | Required? |
| --- | --- |
| Implement the tag on your pages. | Required |
| Check your CSP requirements. | Required if your website enforces a CSP. |

### Implementing static tracking tags

Since static tracking tags fire as soon as they are initiated, be sure to place the static tracking tag code in the header of the webpage as indicated in the following code snippet.

```
<html>
    <head>
    ...
        Paste the static tracking tag code here.
    ...
    </head>
    <body>
    </body>
</html>
```

### Check CSP requirements

A CSP is in your site's HTTP response header or in a `<meta>` tag in the page `<head>` tag. A different team usually manages a CSP than the one who implements the pixel. You do not configure the CSP in the pixel code itself.

If your website enforces a Content Security Policy (CSP) and you initiate cookie syncing, you must ensure the following domains are in the `img-src` CSP directive:

 `insight.adsrvr.org`
`match.adsrvr.org`
 The domain for each cookie sync partner you use.
 If your site uses `data:image/...` images, make sure the `data:` URL scheme is included in the `img-src` directive, for example: `img-src 'self' data: insight.adsrvr.org match.adsrvr.org`.

> **IMPORTANT**: If a domain is missing, you might receive an error when the scripts load or the pixels fire.

The following example shows how to provide the required domains, including a sample of partner domains.

```
Content-Security-Policy:
  img-src 'self'
    insight.adsrvr.org
    match.adsrvr.org
    pixel.advertising.com
    ib.adnxs.com
    x.bidswitch.net
    dsum-sec.casalemedia.com
    cm.g.doubleclick.net
    simage2.pubmatic.com
    ups.analytics.yahoo.com
    pixel.rubiconproject.com;
```

> **TIP**: If you use both a universal pixel and a static tracking tag, you can rely on the universal pixel for cookie syncing and disable cookie syncing on the static tracking tag.

## Troubleshooting tips

If an error occurs when loading a static tracking tag, make sure to check the following before contacting support:

- There are no spaces in the `src` attribute URL, for example, if the dynamic parameters were added.
- All placeholder variables have been replaced with the appropriate values with no curly braces {}.
- The tracking tag is placed high enough in the header of the webpage.

> **TIP**: To confirm the tag has been placed correctly, use one of several web debugging tools such as Ghostery, Fiddler, or Firebug.
