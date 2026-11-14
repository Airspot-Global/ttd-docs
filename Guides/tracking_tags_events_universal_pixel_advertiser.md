# Implementing upixel and RT conversion events together

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/data/doc/TrackingTagsEventsUniversalPixelAdvertiser
- Retrieved: 2026-11-14
- Category: Guides

---

# Implementing upixel and RT conversion events together

The Trade Desk provides two complementary real-time conversion tracking mechanisms: universal pixel (upixel) and Real-Time Conversion Events API (RT CAPI). This page explains how they relate to each other and how to implement them together using different methods.

## Upixel vs. real-time conversion events

The two mechanisms are complementary. You can run both at the same time: the upixel establishes a persistent visitor pool, and real-time conversion events add granular action-level signals on top of that.

The following table outlines the differences.

| Aspect | Universal pixel | Real-time conversion events |
| --- | --- | --- |
| **What it does** | Tracks all page visits; powers URL-based site-visit attribution and segments | Tracks specific user actions (purchase, add to cart, sign-up, and so on). Powers event-based attribution and segments. |
| **When it fires** | On every page load | Only on designated conversion actions (potentially multiple actions per page) |
| **Primary use** | URL-based attribution and audience building | Conversion event-based attribution, product-level data for attribution and audience building |
| **Identifier required** | Upixel ID | Event tracker ID |

## Implementation quickstarts

Use the following table to identify the right implementation for your environment and the corresponding quickstart guide.

| Environment | Google Tag Manager | No GTM |
| --- | --- | --- |
| **Client-side (web)** | GTM (client-side) | JS SDK |
| **Client-side (in-app)** | N/A | RT CAPI |
| **Server-side** | GTM (server-side) | RT CAPI |

Each quickstart explains how to pass your upixel ID and event tracker ID together in a single call, so you don't need a separate upixel implementation.

## Full user guides

For field-level reference and advanced configuration beyond what the quickstarts cover, see the following guides:

### Shopify

/doc/DataShopifySummaryOpenTTD

Track site and checkout events directly from your Shopify store, with or without GTM.

### Real-Time Conversion Events API

/doc/DataConversionEventsApi

Complete API reference, including all supported ID types, event mapping, URL mapping, and FAQs.

### Item-level event tracking tag

/doc/TrackingTagsEvents

Complete reference for the JS tag implementation, including GTM, predefined events, custom metadata, and verification.

## FAQs

### Do I need a separate upixel implementation if I'm already using the RT CAPI?

No. If you pass your upixel ID alongside your event tracker ID in the `pixelIds` or `pixel_ids` array (or the GTM pixel IDs field), the upixel receives the signal without a separate implementation.

### What ID do I need to use with a upixel?

Use your advertiser ID for combined upixel and RT CAPI implementations. If you are a commerce advertiser with only a merchant ID and need to use the upixel, contact your Technical Account Manager to confirm the correct setup.

### Can I send multiple different conversion event types in the same integration?

Yes. Fire an event at each conversion point on your site (for example, `addtocart` when a user adds to the cart, `purchase` on the confirmation page). You can map one page view and one user-interaction event to the same user per call, but not two of the same type.

### What happens if I pass only the upixel ID and no event tracker ID?

Events are captured for audience and URL-based attribution tied to the upixel, but you will not have conversion event measurement for specific user actions.
