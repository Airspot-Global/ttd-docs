# Item-level event tracking tag

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/data/doc/TrackingTagsEvents
- Retrieved: 2026-11-14
- Category: Guides

---

# Item-level event tracking tag

> **NOTE**: If you're uploading event data as part of the product catalog integration workflow, first complete Step 2: Upload product catalog data.

The item-level event tracking tag is a snippet of JavaScript (JS) code that merchants can include on webpages to send user interaction events to The Trade Desk for conversion measurement and audience targeting campaigns running on The Trade Desk platform.

Item-level events are events that contain information about one or more product items: for example, an "Add To Cart" event with details of the product that was added to the cart, or a "Purchase" event with details of multiple products in the customer's order.

> **NOTE**: The event tracking tag is for real-time conversion events. It does not support Offline conversion events.

Item-level event tracking might be ideal for you if any of the following conditions apply to you:

- You are a commerce partner, direct-to-consumer (DTC) brand, marketplace, or commerce brand with an extensive catalog of products or items and you want to track the actions a user takes before converting.
- You are a merchant and want to use the product catalog feature to track item-level conversion events, page views, shopping cart additions, or other events. For a full list of supported events, see Predefined item events.

> **IMPORTANT**: If you're not using the product catalog—for example, if you're an advertiser who wants to automatically map the user journey across your website or app, passing back multiple events without manual mapping—do not use this option. Instead, use the Universal pixel with dynamic parameters.

## Tag overview

Here's what you need to know about the item-level event tracking tag:

- Event objects pushed to the tag must follow the schema of the Real-time conversion events API, including event names and dynamic parameters.
- If item-level tracking is not required, other tracking tags might be more suitable: see Universal pixel or Static tracking tag.
- You can get started with predefined events or customize your own event names.
- The tag automatically uses The Trade Desk's third-party cookie (TDID) for user identity.
- The event tracking tag requires user consent and a cookie. For details, see Prerequisites.

## Prerequisites

If you want to use item-level event tracking with the product catalog, which is recommended but not required, you'll need to have the following in place:

-

User consent: Before capturing data using the item-level events tag from The Trade Desk, you must make sure that appropriate user consent is obtained. If you use a consent management platform (CMP) that has the IAB Transparency & Consent Framework enabled, the tag automatically integrates with the CMP to retrieve the user's consent choices.

-

You must have a merchant ID, which is the unique identifier assigned by The Trade Desk to each merchant during the onboarding process. If you don't yet have a merchant ID, contact your Account Manager.

For details, see Getting started for merchants.

-

Your event must pass item objects, if it's an event such as a purchase. Some events, such as a site visit or login event, do not require item details.

## Integration options

There are two ways to implement the item-level event tracking tag on your website:

- Integrate the JavaScript code directly on your webpage or within a tag management solution. See Implement directly on your webpage.
- Use the pre-built Google Tag Manager template, which requires no development work in most cases. See Implement using Google Tag Manager.

The following sections provide details and instructions for each integration option.

## Implement directly on your webpage

To implement an item-level event tracking tag on your site by integrating the JavaScript code directly on your webpage, the workflow consists of the following steps:

1. Export the event tracking tag code.
2. Initialize the tag.
3. Send conversion events.
4. Verify the tag.

### Export the event tracking tag code

In the platform UI, complete these steps:

1.

Navigate to an advertiser, campaign, or ad group.

2.

In the left navigation, select **Libraries**, and then select **Advertiser Data**.

3.

Click the **Events Tracking** tab and find the tag that you want.

> **NOTE**: The **Events Tracking** tab is available only if you have a merchant ID.

4.

On the right, click **Export Code** to download and save the tag code (top section).

For details, see Item-level events tracking tag in the Knowledge Portal.

### Initialize the tag

To begin tracking events, you must first load and initialize the tracking tag code, which you exported in the previous step, onto your webpage. This performs the following actions:

-

Sets the merchant ID that the events will be captured with.

-

Loads the required additional JavaScript code from `js.adsrvr.org`.

-

Initializes a function, `ttdConversionEvents`, which is used to submit new events to capture via the tag.

-

Ensures that the Trade Desk ID (TDID) cookie is set. This cookie is automatically added to events when they are captured.

-

Sets a flag that determines whether debugging is enabled or disabled. By default debugging is disabled.

-

Sets a flag that determines whether cookie syncing is enabled or disabled. By default, cookie syncing is enabled.

> **IMPORTANT**: To make sure that the tag is initialized before events are generated, and that no events are missed, initialize the tag as early as possible during the page load. Place the tag within the `<head>` tag on your page to ensure that the initialization starts before the page is loaded and that the script has access to cookies for data collection. Alternatively, if you're using a tag manager, use the tag manager's built-in trigger feature to add the initialization code early within the page load sequence (for example, on a "DOM Ready" event).

The following fictitious example initializes the code to begin tracking events for the specified tracking tag to an account ID. The values for the `merchantId` field and `pixelIds` array, from the exported code, are your own unique values.

```
<script async src="https://js.adsrvr.org/up_loader.3.0.0.js"></script>
<script>
	window.ttdConversionEventsLayer = window.ttdConversionEventsLayer || [];
	function ttdConversionEvents() {window.ttdConversionEventsLayer.push(arguments);}
	ttdConversionEvents("init", { merchantId: 12345, pixelIds: ["ab1c2de"] });
</script>
```

#### Debug mode

To view tag information while developing your integration, you can enable debug mode during initialization by including `enableDebug: true` in the list of arguments in the `ttdConversionEvents` function for the `init` event layer, as shown in the following example.

When debug mode is enabled, the tag script logs records to the developer console, and information about the tags that are loaded appears in the **Network** tab, as shown in the following fictitious example.

```
ttdConversionEvents("init", { merchantId: 12345, pixelIds: ["ab1c2de"], enableDebug: true });
```

#### Cookie sync feature

By default, event tracking tags have cookie syncing enabled. Cookie syncing is required for matching user identities across different ad tech platforms. Without it, advertisers, merchants, and platforms might miss critical opportunities to identify and engage users accurately.

> **IMPORTANT**: Disabling cookie syncing can reduce the accuracy of user matching, affecting your ability to target and measure audiences. If necessary, disable it by adding a specific parameter in the pixel syntax.

For details, see Cookie syncing.

### Send conversion events

To send conversion events in the event tracking tag, call the script using the `ttdConversionEvents("event", { ... })` function with a list of arguments to represent your item events. Item-level event tracking requires a label for each event to track. You can choose to build this out using predefined events, or you can create your own with custom values.

#### Predefined item events

You can start with predefined item events that are built in to the tracking tag functionality and are automatically supported by The Trade Desk. These include common user actions, such as adding an item to a shopping cart or purchasing a product. Tags are configured to capture the `event_name` property and other metadata in the `items` object.

The following table lists all predefined events that you can associate directly into your application or website.

| Event Name | User Action |
| --- | --- |
| `purchase` | The user completed a purchase and has the Thank You page displayed. |
| `donate` | The user donated to the business or a cause. |
| `subscribe` | The user subscribed to a service or content offering. |
| `reserve` | The user made a reservation. |
| `starttrial` | The user started a free trial. |
| `applicationapproval` | The user's application was approved. |
| `submitapplication` | The user submitted an application. |
| `initiatecheckout` | The user started the checkout process. **TIP**: There is no functional difference between `initiatecheckout` and `startcheckout`. Choose the one that aligns best with your own internal systems. |
| `startcheckout` | The user started the checkout process. **TIP**: There is no functional difference between `initiatecheckout` and `startcheckout`. Choose the one that aligns best with your own internal systems. |
| `addpaymentinfo` | The user added payment information during checkout. |
| `addbilling` | The user added or updated their billing information. |
| `addtocart` | The user added an item to the shopping cart. |
| `addtowishlist` | The user added an item to the wish list. |
| `wishlistitem` | The user added an item or SKU number to the wish list. |
| `customizeproduct` | The user customized a product configuration. |
| `viewcart` | The user viewed the contents of the shopping cart. |
| `viewitem` | The user viewed an item or SKU number. |
| `viewcontent` | The user viewed a specific piece of content, such as a product or landing page. |
| `viewcategory` | The user viewed a category page. |
| `listview` | The user viewed a list of items. |
| `pageview` | The user viewed a page on the site. |
| `searchitem` | The user searched for an item or SKU number. |
| `searchcategory` | The user searched for a category. |
| `search` | The user performed a search on the site or app. |
| `sitevisit` | The user visited the site. |
| `login` | The user logged in to the site. |
| `contact` | The user contacted the business (for example, by chat, email, or phone). |
| `messagebusiness` | The user sent a message to the business or contacted the business via form or email. |
| `direction` | The user requested and received directions to the business. |
| `findlocation` | The user searched for or requested a store or business location. |
| `share` | The user shared content, a product, or a promotion. |
| `save` | The user saved content or an item to revisit later. |
| `rate` | The user rated a product or service. |
| `schedule` | The user scheduled an appointment or visit. |
| `invite` | The user invited another person to use the product or service. |
| `watchvideo` | The user watched a video. |
| `download` | The user downloaded a file or asset. |
| `adclick` | The user clicked an ad. |
| `adview` | The user viewed an ad. |
| `lead` | The user submitted their information as a lead. |
| `submitform` | The user submitted a form. |
| `completeregistration` | The user completed a registration or sign-up form. |
| `levelcomplete` | The user completed a level in a game or experience. |

For details, see Event names in the `POST /track/realtimeconversion` endpoint documentation.

> **NOTE**: If you require event values not listed in the table, you can create them in the Platform UI (see Define events in the Knowledge Portal) or contact your Technical Account Manager.

The code that you exported from the platform UI has all the basic values that you need, such as your merchant ID, but you might want to add custom fields or additional values.

You can include these event names in the list of arguments to the `ttdConversionEvents` function for the `event` layer in the `event_name` property.

The following fictitious example shows an item-level event tracking tag for user purchase events.

```
ttdConversionEvents("event",
{
  "merchantId": 12345,
  "pixelIds": ["ab1c2de"],
  "currency": "USD",
  "order_id": "order12345",
  "value": 29.98,
  "event_name": "purchase",
  "items":[
    {
      "item_code": "123456789",
      "name": "Blue T-Shirt",
      "qty": 1,
      "price": 19.99,
      "cat": 124
    },
    {
      "item_code": "012345678",
      "name": "Blue Shorts",
      "qty": 1,
      "price": 9.99,
      "cat": 123
    }
  ]
});
```

#### Custom metadata

To add your own custom metadata, you can manually define up to ten custom fields (`td1` through `td10`) in your tracking tag. For example, to track conversion events, you can define promo codes, campaign names, or referrer URLs.

The following fictitious example shows adding custom fields to the tracking tag to track custom metadata for limited-time promotions.

```
ttdConversionEvents("event",
{
  "event_name": "purchase",
  ...
  "td1": "Spring 2026 Promo", // The campaign name.
  "td2": "WELCOME10", // The promo code used.
  "td3": "store.domain.com" // The website where the event happened.
});
```

To simply your workflow, you can store all event values inside a variable and pass it to the `ttdConversionEvents` function, as shown in the following example.

```
ttdConversionEvents("event", eventPurchaseParameters);
```

### Verify the tag

After you've configured your tag properties and have created triggers to fire off events, you can test by verifying that the events tag appears in the **Network** tab of the element inspector in your web browser developer tools.

For example, in Chrome, right-click anywhere on the webpage and choose **Inspect** to view the developer tools.

> **IMPORTANT**: Inspecting a production or server-side webpage results in different outputs because of encoded query parameters. The following verification steps must be performed by developers or webmasters with access to your client-side website.

Here's how you can use the Element Inspector to search for your event tracking tag:

1.

In the Element Inspector, navigate to the **Network** tab.

2.

To display only requests for The Trade Desk tags, type `adsrvr` in the **Filter** text box. You should see requests with the following names:

  -

`up_loader.3.0.0.js` or `conversionEvents-v1.min.js`—The hosted JavaScript, loaded during initialization.

  -

cei**—The initialization request that sets the TDID cookie.

  -

`realtimeconversion`—Event data sent to the Real-time conversion events API from The Trade Desk.

> **NOTE**: The requests with `Type: xhr` (rather than `Preflight`) contain the actual event data that was sent.

3.

On the realtimeconversion xhr requests, view **the Payload tab** and check to make sure that the query parameters match the properties and types used in your tag

## Implement using Google Tag Manager

> **NOTE**: This section is intended for users familiar with Google Tag Manager (GTM), a popular tag management tool. It focuses on integrating the tracking tag.

Here's what you need to know to use the GTM community template:

- The GTM data layer is typically used to collect relevant event data within GTM and provide it to The Trade Desk tags. For an example, see Push events to GTM.
- If your event names are different from the ones defined by The Trade Desk, you can add your own event names in The Trade Desk platform.

### Prerequisites for GTM implementation

If you want to implement item-level event tracking in GTM, make sure you have the following in place:

- Make sure that the events you want to measure, and the required data (transaction ID, purchase value, product items), have been pushed into the GTM data layer. For details, see Use a data layer with event handlers in the Google documentation.
- Set up data layer variables that you can use to extract those items from the data layer.

### High-level implementation options for GTM

To set up item-level event tracking tags in GTM, triggered on the relevant events, there are two implementation strategies.

You set up tags, triggered on the relevant events, in one of the following ways:

-

**JavaScript**:

   1. **Initialization**: Create a custom HTML tag for the item-level event tracking tag initialization code, triggered as early as possible during the page load: for example, on a page view or DOM ready trigger. For details, see Page view triggers in the Google documentation.
   2. **Events**: Create a custom HTML tag that submits data to the item-level event tracking tag via the `ttdConversionEvents` function. This tag should be triggered on the events you want to submit to The Trade Desk: for example, trigger on an `add_to_cart` or `purchase` event.

-

**GTM Template**: Create one tag, using the GTM template, for the events you want to send to The Trade Desk.

The template automatically loads the required JavaScript onto the page and handles the initialization steps.

### Item identifier correlation

It's important to understand the relationship between item identifiers used in GTM examples and The Trade Desk schema fields.

For example, GA4 data layer examples use `item_id` and `item_name`. These are translated to The Trade Desk schema fields (such as `item_code`) by your GTM variables or custom JavaScript.

### Workflow for GTM implementation

The GTM workflow consists of the following steps:

1. Add tag template from the GTM gallery.
2. Create GTM variables.
3. Translate GTM event names.
4. Push events to GTM.
5. Verify the tag.

### Add tag template from the GTM gallery

Add the code to your workspace. On the page in the Google Community Template Gallery, it's called The Trade Desk Conversion Events JS SDK: it's the same thing. Follow these steps:

1. Sign in to your GTM workspace.
2. On the left, select **Templates**.
3. In the Tag Templates section, select **Search Gallery**.
4. In the Community Template Gallery section, search for **The Trade Desk Conversion Events JS SDK**.
5. Do one of the following:

  - If you're adding the template to your workspace for the first time: Select **Add to workspace**.
  - If you'd previously added the template to your workspace: Select **Open in Editor** (only present if you'd already added the template).

### Create GTM variables

After downloading the template, you might not be able to fill in all the template fields. You must configure your variables in GTM to match properties defined by The Trade Desk for sending conversion events.

To create a new variable in GTM, follow these steps:

1. Open your GTM workspace.
2. On the left, select **Variables** > **User Defined Variables**.
3. Select **New** to create a new user-defined variable. For suggestions, see User-defined variables.

#### User-defined variables

In Google Tag Manager, you can create custom user-defined variables, including constants and lookup tables.

> **IMPORTANT**: To declare nested properties, you must use the `parent.child` dot notation.

The following table lists all the conversion event properties that JSON requests to the `POST /track/realtimeconversion` endpoint support.

| Property | Required? | Data Type | Description | Value Example | Notes |
| --- | --- | --- | --- | --- | --- |
| `merchant_id` | Required, only for merchants | String | The platform ID of the merchant assigned by The Trade Desk to the merchant during the onboarding process. | `12345` | None |
| `adv` | Required, only for non-merchants | String | The platform ID for the advertiser on whose behalf the tracking call was made. | `4w1ba8e` | None |
| `pixel_id` | Required | String | The platform ID of the event tracker for merchant event mappings, or the Universal pixel ID of the event for URL mappings. | `ejs57s6` | For event mapping, include the event tracker and the `event_name` property in the request. |
| `pixel_ids` | Optional | String array | The list of IDs for event trackers or universal pixels. | `ejs57s6, hc7ihke` | You can include multiple IDs of the same type, or a combination of event tracker and universal pixel IDs. If this property is provided, `pixel_id` is ignored. |
| `tracker_id` | Not recommended, use `pixel_id` instead | String | The platform ID of the event tracker. | `hc7ihke` | This property has been deprecated. |
| `upixel_id` | Not recommended, use `pixel_id` instead | String | The universal pixel ID for the event. | `ejs57s6` | This property has been deprecated. |
| `value` | Required, only for purchase events | Decimal | The revenue-tracking value with a period (not a comma) as a decimal point. | `19.98` | If revenue is passed, it will be available in all reports. |
| `currency` | Optional | String | The ISO 4217 currency code for the revenue value. | `USD` | Here’s what you need to know about this property: - For merchants, include this property only if you want to use a different currency than the default currency that you set. - Revenue is calculated based on the advertiser’s currency, not the code passed in the event. |
| `event_name` | Optional | String | The type of event defined by the partner platform. | `addtocart` | For a list of event names to use, see Event names. For merchants with a product catalog, see Item-Level Event Tracking in the Knowledge Portal. . |
| `client_ip` | Optional | String | The client IPv4 or IPv6 IP address that uniquely identifies a network interface on a machine. | `7.7.7.7` | Make sure that it is the client, not server, IP address. |
| `referrer_url` | Required, if you are including a universal pixel ID | String | The website URL from where the event occurred, if any. | `site.com` | If you are using the conversion SDK, the URL will automatically be extracted. To provide a specific URL, set this value to the URL you want to provide. |
| `adid` | Optional | String | The unique advertising ID for the event. For details, see Supported user ID types. | `660e1d86-6796-463a-be86-897993136018` | If the `adid` value is empty and the `adid_type` value is not provided, your request might be rejected. Be sure to include this property if you are using any of the following: - The Trade Desk for attribution. - Segment and audience generation from The Trade Desk platform. - A third-party measurement partner, in a scenario where you want to provide additional data when an impression ID can't be found. |
| `adid_type` | Required, if `adid` is provided | String | The type of the advertising ID, specified in the `adid` property: TDID, IDFA, AAID, DAID, NAID, IDL, EUID, or UID2. For details, see Supported user ID types. | `TDID` | If this field is empty and `adid` is not provided, the default value is `TDID`. |
| `tdid` | Optional | String | The Trade Desk 36-character GUID (including dashes) for this user. | `660e1d86-6796-463a-be86-897993136018` | None |
| `daid` | Optional | String | A 36-character GUID (including dashes) that serves as the device advertising ID for this user. See also `idfa` for iOS, or `aaid` for Android devices. | `3ecef5dd-21da-4a9d-a6d7-cd541666bc1e` | None |
| `idfa` | Optional | String | A 36-character GUID (including dashes) that serves as the device advertising ID for Android devices. | `cc9d5044-5837-4bcd-b339-26115f56deb6` | None |
| `aaid` | Optional | String | A 36-character GUID (including dashes) that serves as the device advertising ID for iOS devices. | `8887b1e6-82cd-4b44-b36e-1a25655349a1` | None |
| `naid` | Optional | String | A 36-character GUID (including dashes) that serves as the device advertising ID for Windows devices. | `9aa5696c-af88-4127-bfdb-107b12417913` | None |
| `uid2_token` | Optional | String | The encrypted UID2 token, also known as an advertising token. This token is case-sensitive. Tokens are generated and managed using UID2 APIs. For details about UID2 APIs, see UID2 Endpoints. | See Request example. | None |
| `euid_token` | Optional | String | The encrypted EUID token, also known as an advertising token. This token is case-sensitive. For details about EUID APIs, see UID2 Endpoints. | See Request example. | None |
| `idl` | Optional | String | The 49-character or 70-character RampID (previously known as IdentityLink). **IMPORTANT**: This must be a RampID from LiveRamp that is mapped specifically for The Trade Desk. For details about mapping a RampID, see LiveRamp documentation. | `XY1234wXyWPB1SgpMUKIpzA0I3UaLEz-2lg0wFAr1PWK7FMhs` | A Ramp ID (formerly IDL) is a 49 or 70 character ID based on the LiveRamp identity graph. |
| `imp` | Optional | String | A 36-character GUID (including dashes) that serves as the unique ID for the impression to which the event is attributed. | `49gCBlwj-9d33-0927-s9g7-sd7nF3D248d5` | If you are using a third-party measurement partner, be sure to include this property for more accurate attribution. |
| `country` | Optional | String | Optional | The full name of the country where the conversion occurred. | `United States` |
| `region` | Required if `country` is set to `United States` | String | The full name or code of the region in the United States where the conversion occurred. | `NY`, `New York` |  |
| `NielsenDMA`* | Optional | Integer | The numerical metropolitan area geotargeting code where the conversion occurred. | `501` |  |
| `city` | Optional | String | The city where the conversion occurred. | `US NYC` | None |
| `zip` | Optional | String | The zip code or postal code. | `10004` | None |
| `order_id` | Optional | String | The associated order identifier of the event. | `abc123XyZ` | None |
| `items` | Optional | Object array | One or more items in the order. For object properties, see Item properties. | N/A | None |
| `privacy_settings` | Required for the EU unless an exemption has been approved by The Trade Desk Legal team. Optional for the US. | Object array | User privacy settings based on data privacy consent processing. For object properties, see Privacy settings properties. | N/A | None |
| `data_processing_option` | Required for applicable states | Object | A data processing option to pass users' opt-out choices, such as Limited Data Use (LDU), in applicable US states. This is an alternative to the `GPP` string in the Privacy settings properties. For object properties, see Data processing option properties. | N/A | The user choice processing options are supported only for events from US states where applicable laws and regulations are in effect. |
| `td1` - `td10` | Optional | String(150) | Ten sequentially numbered custom dynamic properties that can be used to provide additional conversion metadata. For details, see Custom line-item dynamic parameters. | N/A | None |

* © 2026, The Nielsen Company (US), LLC. The DMA® data is used pursuant to a license from The Nielsen Company (US), LLC. Any use and/or reproduction of these materials without the express written consent of The Nielsen Company (US), LLC, is strictly prohibited. DMA® data is valid for the period 2025 - 2026. DMA® is a registered service mark of The Nielsen Company (US), LLC and is used pursuant to license.

### Translate GTM event names

> **NOTE**: If you track only `purchase` or `login` events, you can skip this section.

GTM event names follow GA4, but to use the tracking tag you must use the `event_name` values without underscores, to match item events defined by The Trade Desk. To properly handle conversion events sent through GTM, you must create a lookup table that maps each event to the naming convention from The Trade Desk.

The following table maps common GA4 event names and The Trade Desk standard event names, ordered alphabetically by The Trade Desk event name.

| GA4 Event Name | The Trade Desk Event Name | Example User Action |
| --- | --- | --- |
| `add_to_cart` | `addtocart` | The user added an item to the shopping cart. |
| None | `direction` | The user requested and received directions to the business. |
| `login` | `login` | The user logged in to the site. |
| `generate_lead` | `messagebusiness` | The user sent a message to the business or contacted the business via form or email. |
| `purchase` | `purchase` | The user completed a purchase and the "Thank You" page was displayed to the user. |
| `search` | `searchitem` | The user searched for an item or SKU number. |
| `page_view` | `sitevisit` | The user visited the site. |
| `begin_checkout` | `startcheckout` | The user started the checkout process. |
| `view_cart` | `viewcart` | The user viewed the contents of the shopping cart. |
| `view_item` | `viewitem` | The user viewed an item or SKU number. |
| `add_to_wishlist` | `wishlistitem` | The user added an item or SKU number to the wishlist. |

### Push events to GTM

To send item-level events to GTM, you must create a trigger that sends events to the Real-Time Conversion Events API each time the data layer is updated using the `window.dataLayer.push` function. The payload for the arguments must exist within the tracking tag, and must use the user-defined variables mapped in the template.

The following is an example of code for sending a conversion event inside a tracking tag on GTM.

```
window.dataLayer.push(
  {
    "event": "purchase",
    "gtm":{
      "transaction_id": "order12345",
      "value": 13.49,
      "currency": "USD",
      "items":[
        {
          "item_id": "6789",
          "item_name": "Hand Soap",
          "unsupported_field": "unknown765",
          "item_category": 435,
          "price": 2.50,
          "quantity": 3
        }
    ]
}});
```

The template fires items by default, but you can set event triggers in your workspace to customize which pages are tracked.

To access the triggers page, follow these steps:

1. Open your GTM workspace.
2. On the left, select **Tags** and choose your tag to customize.
3. On the **Tag Configuration** screen, scroll down to the **Triggering** section.
4. (Optional) To customize the firing triggers, create a custom HTML tag.

#### Custom html tag

To customize the triggers, open a custom HTML tag in GTM and load it in the tracking tag script.

Create the following:

1.

A custom HTML tag for the initialization.

2.

One or more custom HTML tags for events. You could create one tag covering all events.

3.

A custom JavaScript variable to convert items from the data layer to the format used by The Trade Desk. Use this variable within the custom HTML tag that you created in Step 2, as shown in the following example.

The custom HTML code for a specific event might be something like the following. In this example, `{{JS - GA4 Items to The Trade Desk Items}}` is a Google Tag Manager custom JavaScript variable that does the following:

- Extracts the item list from the data layer.
- Returns an item list converted to the schema defined by The Trade Desk.

```
<script>
ttdConversionEvents("event",
{
  "merchantId": 12345,
  "pixelIds": ["ab1c2de"],
  "event_name": {{Event}},
  "value": {{DLV - Ecommerce Order Value}},
  "currency": {{DLV - Ecommerce Currency}},
  "items": {{JS - GA4 Items to The Trade Desk Items}},
  "td1": "example"
});
</script>
```

To test whether your GTM tags are firing, follow the steps in Verify the tag. To publish your event tracking tag, follow these steps: In your GTM workspace, select **Submit**, then create a version, and then select **Publish**.

## FAQs

The following are commonly asked questions about item-level event tracking tags.

### Is there a limit to the number of item-level events that can be stored?

There is no limit to the number of items in a single event. You can send up to 50 events in a single event call, and each event can have any number of items.

### How does the event tracking tag interact with the Real-Time Conversion Events API?

The event tracking tag calls the POST /track/realtimeconversion endpoint using an anonymous cookie and your merchant ID. This third-party cookie is then extracted to get the IDs.

All IDs supported by the underlying endpoint are supported by the event tracking tag.

### Can an item-level event tracking tag map to UIDs such as UID2 and EUID?

UIDs use first-party cookies and require a different setup and process. For details on UID integration for event tracking tags, contact your Technical Account Manager.

### Does the event tracking tag support universal pixel identifiers?

Yes. To capture conversion events as a tracking tag, you can add the universal pixel ID it to the `pixelIds` array:

```
pixelIds: ["UPIXEL_ID_PLACEHOLDER_01", "EVENT_TRACKING_TAG_02", ...]
```

### Can I map multiple event types in a single call?

No. The `event_name` property accepts one type of event at a time.

## Next steps

If you uploaded event data only for measurement, your integration is complete.

If you uploaded event data as part of a product catalog integration, the next step is to activate the data through your product catalog. To share access, continue to Step 4. Manage product catalog access. You can also create product lists to build audiences and measure sales performance.
