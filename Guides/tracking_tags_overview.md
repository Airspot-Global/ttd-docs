# Tracking tags

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/data/doc/TrackingTagsOverview
- Retrieved: 2026-11-14
- Category: Guides

---

# Tracking tags

A tracking tag, or a pixel, is a piece of HTML or JavaScript code, that is placed on a webpage to track visitor activity on the page for the reporting and attribution purposes.

Based on their webpage placement and specific properties, tracking tags can pass information about pages visited or user actions taken on a given page, such as pressing buttons or making selections. For example, placing a pixel on a home page would track users who visit the page. Placing a tag on an order confirmation page can track users who purchased something, which can be classified as a conversion.

Events to be tracked can be differentiated by names assigned to the respective tracking tags in the `TrackingTagName` property in the tracking tag endpoints, for example, "Purchase Conversion," "Landing Page Visit," "Add Items to Shopping Basket," and so on.

## Workflow overview

After you create a tracking tag using the Platform API or UI and place the tracking tag code on the advertiser's website pages, the tracking process of visitor interactions consists of the following general steps:

1. A user visits a page on the website where the tracking tag is installed.
2. After the page is loaded, the user’s browser sends a request to load the tracking tag from The Trade Desk `adsrvr.org` tracking domain. This is broadly known as tag firing.
3. Using the IDs included in the request, which identify the advertiser and the tracking tag, The Trade Desk server places a tracking cookie in the user's browser, assigns a TDID to the user or reads an existing ID that has already been set, and performs cookie mapping as needed.

For details on the universal pixel workflow with CMP integration, see Universal pixel.

## Tracking tag categories

The tracking tag categories are defined in the `TrackingTagCategory` property in the tracking tag endpoints.

The main categories of The Trade Desk tracking tags include the following:

- Static tracking tag—contains an image in its `<img>` HTML tag.
- Universal pixel—contains JavaScript code in its `<script>` HTML tags.
- Item-level events tracking tag—contains JavaScript code in its `<script>` HTML tags. Merchants can include this tag on webpages to send user interaction events to The Trade Desk for conversion measurement and audience targeting campaigns running on The Trade Desk platform.

> **NOTE**: Universal pixels are more commonly used, because they support all the functionality of static tracking tags while also providing the optional functionality of pixel mappings and allowing more efficient implementation.

## Tracking tag syntax

When a tracking tag is fired, its `src` attribute is assigned a value that consists of two main parts, separated by a question mark (?) from each other:

- The tracking server URL, which also includes the tag type (`pxl` for static tags or `up` for universal pixels)
- Tracking tag query parameters, included as key=value pairs, separated by ampersands (&):

  - Required parameters include the advertiser ID and tracking tag ID.
The tracking tag ID for the universal pixel is the `upid` parameter value, and for static tracking tags, the ID is part of the `ct` parameter value.
  - Optional parameters include dynamic parameters that provide additional context for reporting purposes.

For details about the individual parameters, see Universal pixel and Static tracking tag respectively.

The following image provides an illustration of the two parts in the `src` attribute with the placeholder and sample values in red.

The following is an example of a fired static tracking tag with eight dynamic parameters in the `src` attribute value:

```
<img src="//insight.adsrvr.org/track/pxl/?adv=4w1ba8e&ct=0:kcvg8kk&fmt=3&v=9.99&vf=GBP&orderid=abc123XyZ&td1=AlbumName&td2=Artist&td3=Genre&td4=DigitalDownload&td5=new_customer"/>
```

The following is an example of a universal pixel iframe with the same eight dynamic parameters in the `src` attribute value:

```
<iframe id="universal_pixel_hc7ihke" src="https://insight.adsrvr.org/track/up/?adv=4w1ba8e&ref=https%3A%2F%2Fwww.thetradedesk.com%2F&upid=hc7ihke&upv=1.1.3&v=9.99&vf=GBP&orderid=abc123XyZ&td1=AlbumName&td2=Artist&td3=Genre&td4=DigitalDownload&td5=new_customer"></iframe>
```

Here's what you need to know about the tracking tag syntax:

- The Trade Desk tracking tags are schemeless, which means that you do not need to specify the `http` or `https` protocol in the server URL.
- Cookie syncing is always enabled for the universal pixel, but it can be turned off for the static tracking tag based on its `fmt` parameter value.
- Both tag categories can include optional dynamic parameters (up to ten custom dynamic parameters, as well as a revenue value, currency code, and the order ID).

For details about the individual parameters specific to each tag category and how to add dynamic parameters, see Universal pixel and Static tracking tag respectively.
