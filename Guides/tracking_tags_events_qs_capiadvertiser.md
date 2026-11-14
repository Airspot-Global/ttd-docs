# Upixel + RT conversion events: RT CAPI quickstart

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/data/doc/TrackingTagsEventsQsCAPIAdvertiser
- Retrieved: 2026-11-14
- Category: Guides

---

# Upixel + RT conversion events: RT CAPI quickstart

> **NOTE**: This guide describes one method for combining universal pixel (upixel) and conversion event tracking. For the full conceptual overview, see Implementing upixel and RT conversion events together. For full implementation details, see Real-Time Conversion Events API and Universal pixel.

This guide walks you through the minimum steps to start sending upixel and conversion event signals together using the Real-Time Conversion Events API (RT CAPI).

## Is this the right implementation for you?

| Aspect | Description |
| --- | --- |
| **Who it's for** | Advertisers _not_ using Google Tag Manager (GTM) |
| **What it does** | Tracks page visits and specific user actions and sends both to The Trade Desk in a single call |
| **What it tracks** | Site-visit signals (upixel) plus item-level conversion events (`purchase`, `addtocart`, `viewitem`, and so on) |
| **Best for** | Advertisers who need a server-to-server integration, or want to track in-app events |
| **Implementation** | Server-side without GTM; client-side (in-app only) |

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

## Step 2: Send a combined upixel and conversion event

Send a POST request to the POST /track/realtimeconversion endpoint. Pass both your upixel ID and your event tracker ID in the `pixel_ids` array, and replace the placeholders with your actual ID values. Here's what you need to know:

- You can map one page view and one user-interaction event to the same user in a single call, but only one of each type per call.
- Use `pixel_ids` (array) rather than `pixel_id` (single value) when passing multiple IDs.
- Include only `adv` (advertiser ID) **or** `merchant_id` (merchant ID), not both. For details, see Required IDs.

```
{
  "data": [
    {
      "adv": "ADVERTISER_ID_PLACEHOLDER",
      "pixel_ids": ["EVENT_TRACKING_TAG_ID_PLACEHOLDER", "UNIVERSAL_PIXEL_ID_PLACEHOLDER"],
      "event_name": "EVENT_NAME_PLACEHOLDER",
      "adid": "EVENT_ADVERTISING_ID_PLACEHOLDER",
      "adid_type": "UID2"
    }
  ]
}
```

For events with product-level data, such as `addtocart`, include the full event details:

```
{
  "data": [
    {
      "adv": "ADVERTISER_ID_PLACEHOLDER",
      "pixel_ids": ["EVENT_TRACKING_TAG_ID_PLACEHOLDER", "UNIVERSAL_PIXEL_ID_PLACEHOLDER"],
      "event_name": "addtocart",
      "referrer_url": "https://yoursite.com/product-page",
      "adid": "EVENT_ADVERTISING_ID_PLACEHOLDER",
      "adid_type": "UID2",
      "items": [
        {
          "item_code": "203319203",
          "name": "Blue T-Shirt",
          "qty": 1,
          "price": 19.99,
          "cat": "Clothes"
        }
      ]
    }
  ]
}
```

## FAQs

### What happens if I only pass the upixel ID and no event tracker ID?

Events are captured for audience and URL-based attribution tied to the upixel, but you will not get conversion event measurement for specific user actions (for example, purchases or add-to-carts).

## Next steps

If you uploaded event data only for measurement, your integration is complete.

If you uploaded event data as part of a product catalog integration, the next step is to activate the data through your product catalog. To share access, continue to Step 4. Manage product catalog access. You can also create product lists to build audiences and measure sales performance.
