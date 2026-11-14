# Upixel + RT conversion events: JS SDK quickstart

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/data/doc/TrackingTagsEventsQsSDKAdvertiser
- Retrieved: 2026-11-14
- Category: Guides

---

# Upixel + RT conversion events: JS SDK quickstart

> **NOTE**: This guide describes one method for combining universal pixel (upixel) and real-time conversion event tracking. For the full conceptual overview and all available methods, see Implementing upixel and RT conversion events together.

This guide walks you through the minimum steps to start sending upixel and conversion event signals together using the JavaScript (JS) SDK. For full implementation details, see Item-level event tracking tag or Real-Time Conversion Events API and Universal pixel.

## Is this the right implementation for you?

| Aspect | Description |
| --- | --- |
| **Who it's for** | Advertisers _not_ using Google Tag Manager (GTM) |
| **What it does** | Tracks page visits with the upixel and specific user actions with conversion events, and sends both to The Trade Desk in a single call |
| **What it tracks** | Site-visit signals (upixel) plus item-level web conversion events (`purchase`, `addtocart`, `viewitem`, and so on) |
| **Best for** | Advertisers who control their site directly and want one script for both the upixel and conversion events |
| **Implementation** | Client-side (browser, web events only), without GTM |

## Required IDs

Before you begin, make sure you have the following:

 Upixel ID (the pixel tied to your advertiser account for audience and page-view tracking)
 Event tracker ID (the ID of the tracking tag tied to your conversion event configuration)
 Advertiser ID (provided by your Technical Account Manager)
 Merchant ID (only for commerce advertisers)

> **IMPORTANT**: When combining upixel and conversion events, include only an advertiser ID or a merchant ID, never both.

## Step 1: Map your event types

Map your site actions to The Trade Desk standard event names.

The following table provides the most common examples. For a full list, see POST /track/realtimeconversion. If needed, you can also create custom events.

| Your site action | TTD event name |
| --- | --- |
| Page view | `sitevisit` |
| Product view | `viewitem` |
| Add to cart | `addtocart` |
| Begin checkout | `startcheckout` |
| Purchase | `purchase` |
| Lead / form submit | `messagebusiness` |
| Search | `searchitem` |
| View cart | `viewcart` |
| Add to wishlist | `wishlistitem` |
| Login | `login` |

## Step 2: Embed the script on your web pages

This step provides a single script that handles page-view attribution (upixel) and conversion measurement (conversion events) together, so no separate upixel tag is needed.

Embed the following script on the pages where you expect conversion events to fire and replace the placeholders with your actual ID values. Pass both your upixel ID and your event tracker ID in the `pixelIds` array.

> **TIP**: If you only want upixel page-view tracking with no conversion events, omit the event tracker IDs from the `pixelIds` array and pass the upixel ID alone.

```
<script async src="https://js.adsrvr.org/up_loader.3.0.0.js"></script>
<script>
  window.ttdConversionEventsLayer = window.ttdConversionEventsLayer || [];
  function ttdConversionEvents() { window.ttdConversionEventsLayer.push(arguments); }
  ttdConversionEvents("init", {
    advertiserId: "ADVERTISER_ID_PLACEHOLDER",
    pixelIds: ["EVENT_TRACKING_TAG_ID_PLACEHOLDER", "UPIXEL_ID_PLACEHOLDER"]
  });
  ttdConversionEvents("event", {
    advertiserId: "ADVERTISER_ID_PLACEHOLDER",
    pixelIds: ["EVENT_TRACKING_TAG_ID_PLACEHOLDER", "UPIXEL_ID_PLACEHOLDER"]
  });
</script>
```

For events with product-level data (for example, `purchase`), include the full event details in the `event` call:

```
ttdConversionEvents("event", {
  advertiserId: "ADVERTISER_ID_PLACEHOLDER",
  pixelIds: ["EVENT_TRACKING_TAG_ID_PLACEHOLDER", "UPIXEL_ID_PLACEHOLDER"],
  event_name: "purchase",
  currency: "USD",
  order_id: "ORDER_ID_PLACEHOLDER",
  value: 29.98,
  items: [
    { item_code: "203319203", name: "Blue T-Shirt", qty: 1, price: 19.99, cat: "Clothes" },
    { item_code: "2234567892", name: "Blue Shorts", qty: 1, price: 9.99, cat: "Clothes" }
  ]
});
```

## FAQs

### Do I need a separate upixel implementation if I'm already using this script?

No. Passing your upixel ID alongside your event tracker ID in the `pixelIds` array sends both signals from the same call.

### Can I send multiple conversion event types with this script?

Yes. Fire `ttdConversionEvents("event", {...})` with the relevant event name at each conversion point on your site (for example, `addtocart` when a user adds to the cart, `purchase` on the confirmation page).

## Next steps

If you uploaded event data only for measurement, your integration is complete.

If you uploaded event data as part of a product catalog integration, the next step is to activate the data through your product catalog. To share access, continue to Step 4. Manage product catalog access. You can also create product lists to build audiences and measure sales performance.
