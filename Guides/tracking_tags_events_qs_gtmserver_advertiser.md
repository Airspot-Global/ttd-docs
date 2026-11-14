# Upixel + RT conversion events: GTM server-side quickstart

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/data/doc/TrackingTagsEventsQsGTMserverAdvertiser
- Retrieved: 2026-11-14
- Category: Guides

---

# Upixel + RT conversion events: GTM server-side quickstart

> **NOTE**: This guide describes one method for combining universal pixel (upixel) and real-time conversion event tracking through server-side Google Tag Manager (GTM). For the full conceptual overview, see Implementing upixel and RT conversion events together. For full implementation details, see Item-level event tracking tag and Universal pixel.

This guide walks you through the minimum steps to start sending upixel and conversion event signals together using the Trade Desk server-side GTM template.

## Is this the right implementation for you?

| Aspect | Description |
| --- | --- |
| **Who it's for** | Advertisers using GTM |
| **What it does** | Tracks page visits and specific user actions and sends both to The Trade Desk through a GTM server container |
| **What it tracks** | Site-visit signals (upixel, through URL Mapping) plus item-level conversion events (`purchase`, `addtocart`, `viewitem`, and so on, through Event Mapping) |
| **How it works** | Tag fires from a server container; better for privacy-sensitive environments |
| **Best for** | Environments requiring a reduced client-side footprint |
| **Implementation** | Server-side, GTM |
| **Template** | The Trade Desk Conversion Events Server-Side Tag |

## Prerequisites

Before you begin, make sure you have the following:

Upixel ID (the pixel tied to your advertiser account for audience and page-view tracking).
 Event tracker ID (the ID of the tracking tag tied to your conversion event configuration).
 TDID cookie value (the first-party `ttd_TDID` cookie required for identity resolution). For details on obtaining it, see Cookie mapping.
 A GTM account with a server container configured (separate from your web container).
 A cloud-hosted server-side GTM endpoint.
 Advertiser ID (provided by your Technical Account Manager), required for this combined route
 Merchant ID (conversion-events only)

> **IMPORTANT**: This guide covers the combined upixel + conversion events route, which requires an advertiser ID. Merchant ID is not supported alongside the upixel. Using it will cause the pixel signal to fail. Merchant ID applies only if you are tracking conversion events without a upixel.

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

## Step 2: Install the GTM template

The Trade Desk server-side GTM template is available directly in the GTM template gallery. This is the recommended approach as gallery installations receive automatic updates when new versions are published.

1. In your GTM server container workspace, go to **Templates** in the left sidebar.
2. Under **Tag Templates**, click **Search Gallery**.
3. Search for **The Trade Desk** or **Conversion Events Server-Side SDK**.
4. Select the template and click **Add to workspace**.
5. Review the permissions and click **Add**.

> **NOTE**: If you need a specific version or cannot use the gallery, you can install the template manually from GitHub. For details, see Manually import GTM template from GitHub.

## Step 3: Configure GTM variables

Under **Variables** > **User-Defined Variables** > **New**, create the following **Constant variables** (static account IDs). For details, see Prerequisites.

| Variable name | GTM variable type | Value |
| --- | --- | --- |
| `TTD Advertiser ID` | Constant | Your advertiser ID |
| `TTD Pixel IDs` | Constant | Your upixel ID and event tracker ID |
| `TTD TDID Cookie` | first-party cookie | `ttd_TDID` |

## Step 4: Create and configure the tag

1.

In your GTM server container, go to **Tags** and click **New**.

2.

Click **Tag Configuration** and select the Trade Desk server-side template installed in Step 2.

3.

Configure the tag fields:

| Tag field | Value |
| --- | --- |
| **Advertiser ID** | `{{TTD Advertiser ID}}` |
| **Merchant ID** | Leave blank. It's not supported alongside the universal pixel in this combined route. |
| **Pixel IDs** | `{{TTD Pixel IDs}}` (Enter multiple IDs as a comma-separated list.) |
| **TDID Cookie** | `{{TTD TDID Cookie}}` |
| **Event Name** | `{{Event Name}}` |
| **Order/Item data** | `{{Data Layer - Ecommerce Items}}` |

## Step 5: Configure triggers

Create a trigger for each conversion event you want to track, plus a trigger for page views if you want the upixel to fire through URL Mapping, and assign all triggers to your tag.

## Manually import GTM template from GitHub

If you need a specific version or cannot use the GTM template gallery in Step 2, import the template manually:

1. Download the template file from github.com/thetradedesk/conversion-events-server-side-googletagmanager.
2. In your GTM server container workspace, go to **Templates** in the left sidebar.
3. Under **Tag Templates**, click **New**.
4. In the template editor, click the menu (three vertical dots in the top-right corner) and select **Import**.
5. Upload the template file.
6. Click **Save**.

The new template appears in your Templates list and is available when creating new tags. Continue to Step 3.

## Next steps

If you uploaded event data only for measurement, your integration is complete.

If you uploaded event data as part of a product catalog integration, the next step is to activate the data through your product catalog. To share access, continue to Step 4. Manage product catalog access. You can also create product lists to build audiences and measure sales performance.
