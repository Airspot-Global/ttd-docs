# Upixel + RT conversion events: GTM client-side quickstart

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/data/doc/TrackingTagsEventsQsGTMclientAdvertiser
- Retrieved: 2026-11-14
- Category: Guides

---

# Upixel + RT conversion events: GTM client-side quickstart

> **NOTE**: This guide describes one method for combining universal pixel (upixel) and real-time conversion event tracking through client-side Google Tag Manager (GTM). For the full conceptual overview, see Implementing upixel and RT conversion events together. For full implementation details, see Item-level event tracking tag and Universal pixel.

This guide walks you through the minimum steps to start sending upixel and conversion event signals together using the official Trade Desk GTM client-side template.

## Is this the right implementation for you?

| Aspect | Description |
| --- | --- |
| **Who it's for** | Advertisers using GTM |
| **What it does** | Tracks page visits and specific user actions and sends both to The Trade Desk through GTM, from a single tag |
| **What it tracks** | Site-visit signals (upixel) plus item-level web conversion events (`purchase`, `addtocart`, `viewitem`, and so on) |
| **How it works** | Tag fires from the user's browser using the hosted Conversion Events SDK |
| **Best for** | Standard web implementations; recommended for most teams |
| **Implementation** | Client-side (browser), GTM |
| **Template** | The Trade Desk Conversion Events SDK |

## Prerequisites

Before you begin, make sure you have the following:

 Upixel ID (the pixel tied to your advertiser account for audience and page-view tracking)
 Event tracker ID (the ID of the tracking tag tied to your conversion event configuration)
 A GTM account with a web container configured for your site
 The GTM container snippet already installed on your site
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

## Step 2: Install the GTM template

The Trade Desk GTM template is available directly in the GTM template gallery. This is the recommended approach—gallery installations receive automatic updates when new versions are published.

1. In your GTM workspace, go to **Templates** in the left sidebar.
2. Under **Tag Templates**, click **Search Gallery**.
3. Search for **The Trade Desk** or **Conversion Events SDK**.
4. Select the template and click **Add to workspace**.
5. Review the permissions and click **Add**.

> **NOTE**: If you need a specific version or cannot use the gallery, you can install the template manually from GitHub. For details, see Manually import GTM template from GitHub.

## Step 3: Configure GTM variables

1.

Under **Variables** > **User-Defined Variables** > **New**, create the following variables:

  -

**Constant variables** (static account IDs):

| Variable name | GTM variable type | Value |
| --- | --- | --- |
| `TTD Advertiser ID` | Constant | Your advertiser ID _(leave blank if using a merchant ID instead)_ |
| `TTD Merchant ID` | Constant | Your merchant ID _(commerce advertisers only; leave blank if using an advertiser ID)_ |
| `TTD Pixel IDs` | Constant | Your upixel ID and event tracker ID, as a comma-separated string, for example `UPIXEL_ID_PLACEHOLDER, EVENT_TRACKING_TAG_ID_PLACEHOLDER` |

  -

**Data layer variables** (dynamic event data):

| Variable name | GTM variable type | Data layer variable name |
| --- | --- | --- |
| `Data Layer - Transaction ID` | Data layer variable | `ecommerce.transaction_id` |
| `Data Layer - Order Value` | Data layer variable | `ecommerce.value` |
| `Data Layer - Order Currency` | Data layer variable | `ecommerce.currency` |
| `Data Layer - Ecommerce Items` | Data layer variable | `ecommerce.items` |

2.

Under **Variables** > **Configure**, enable the **Page URL** built-in variable.

3.

Create a Lookup Table variable to translate your site's event names into The Trade Desk standard event names:

| Setting | Value |
| --- | --- |
| Variable name | `TTD Event Name` |
| Type | Lookup table |
| Input variable | `{{Event}}` |
| Default value | `{{Event}}` |

4.

Configure the lookup table rows using your event name mappings from Step 1. Include a row for `page_view` mapped to `sitevisit` if you want the upixel signal to fire on every page load.

## Step 4: Create and configure the tag

1.

In GTM, go to **Tags** and click **New**.

2.

Click **Tag Configuration** and select the Trade Desk template installed in Step 2.

3.

Configure the tag fields:

| Tag field | Value |
| --- | --- |
| **Advertiser ID** | `{{TTD Advertiser ID}}` |
| **Merchant ID** | `{{TTD Merchant ID}}` (leave blank if not applicable.) |
| **Pixel IDs** | `{{TTD Pixel IDs}}` (Enter multiple IDs as a comma-separated list.) |
| **Page URL** | `{{Page URL}}` |
| **Event Name** | `{{TTD Event Name}}` |
| **Order ID** | `{{Data Layer - Transaction ID}}` |
| **Order Value** | `{{Data Layer - Order Value}}` |
| **Order Currency** | `{{Data Layer - Order Currency}}` |
| **Ecommerce Event Item/Product Data** | `{{Data Layer - Ecommerce Items}}` |

For the **Ecommerce Event Item/Product Data** field, use the following item field mappings:

| TTD field | Item field name |
| --- | --- |
| Item Code | `item_id` |
| Name | `item_name` |
| Category | `item_category` |
| Price | `price` |
| Quantity | `quantity` |

> **NOTE**: A single tag with both IDs in the `{{TTD Pixel IDs}}` variable handles upixel audience signals and conversion event measurement at the same time — no separate upixel tag is needed.

## Step 5: Configure triggers

1.

Create a custom event trigger for each event you want to track and assign all triggers to your tag. Include a `page_view` trigger if you want the upixel to fire on every page load:

| Trigger name | Trigger type | Event name |
| --- | --- | --- |
| `TTD - Page View` | Custom event | `page_view` |
| `TTD - Add to Cart` | Custom event | `add_to_cart` |
| `TTD - Begin Checkout` | Custom event | `begin_checkout` |
| `TTD - Purchase` | Custom event | `purchase` |

2.

Add additional triggers for any other events you are tracking.

> **IMPORTANT**: Your site must push events to the GTM data layer for triggers to fire.

Here's an example `purchase` push:

```
window.dataLayer.push({
  event: 'purchase',
  ecommerce: {
    transaction_id: 'order12345',
    value: 13.49,
    currency: 'USD',
    items: [
      {
        item_id: 'item1234',
        item_name: 'Washing Liquid',
        item_category: 'Laundry',
        price: 5.99,
        quantity: 1
      }
    ]
  }
});
```

> **NOTE**: If your site already sends Google Analytics 4 (GA4) events to GTM, the Trade Desk template can read from the same data layer pushes with no changes to your site code.

## Step 6 (optional): Test your implementation

Use GTM Preview mode to verify that your tag is firing correctly and that events are reaching The Trade Desk platform.

1. In GTM, enable **Preview mode** to activate the GTM Tag Assistant debugger.
2. Navigate to your site and trigger each event you have configured.
3. In the debugger, verify the following:

  - The correct trigger is firing for each event.
  - The tag is receiving the expected variable values (advertiser ID, pixel IDs, event name, order and item data).
  - Both the upixel ID and the event tracker ID appear in the Pixel IDs field.

4. In The Trade Desk platform, check your conversion tag reporting to confirm events are being received.

## Troubleshooting

If your tag is not behaving as expected, use the following common issues and fixes as a starting point.

### Tag is not firing

Confirm that the event names in your custom event triggers exactly match what your site pushes to the GTM data layer (`window.dataLayer`). Use GTM Preview mode to inspect which triggers activate on each page action.

### Event name is showing as undefined or empty

Verify that the `TTD Event Name` lookup table variable is configured correctly and that the data layer event name matches an input row. Confirm the default value is set to `{{Event}}`.

### Order or item data is missing

Confirm your data layer pushes include the `ecommerce` object with the correct structure. Check that data layer variable names use the exact dot-notation paths (`ecommerce.transaction_id`, `ecommerce.items`, and so on).

### Only one pixel ID is receiving signals

Confirm your `TTD Pixel IDs` constant contains both IDs separated by a comma, with no extra characters. For example, `UPIXEL_ID_PLACEHOLDER, EVENT_TRACKING_TAG_ID_PLACEHOLDER`.

## Manually import GTM template from GitHub

If you want a specific template version or cannot use the GTM template gallery in Step 2, import the template manually:

1. Download the template file from the GitHub repository: github.com/thetradedesk/conversion-events-sdk-for-googletagmanager.
2. In your GTM workspace, go to **Templates** in the left sidebar.
3. Under **Tag Templates**, click **New**.
4. In the template editor, click the menu (three vertical dots in the top-right corner) and select **Import**.
5. Upload the template file from the repository.
6. Review the Template Preview. To see the editable fields, click the **Tag Configuration** header.
7. Click **Save**, then click **Close (x)** to return to the workspace.

The new template appears in your Templates list and is available when creating new tags. Continue to Step 3.

## Next steps

If you uploaded event data only for measurement, your integration is complete.

If you uploaded event data as part of a product catalog integration, the next step is to activate the data through your product catalog. To share access, continue to Step 4. Manage product catalog access. You can also create product lists to build audiences and measure sales performance.
