# Tracking Tags

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/TrackingTag
- Category: Guides

---

# Tracking Tags

A tracking tag is a piece of code that loads an anonymous cookie every time a new user lands on a website. When a user leaves a site, the cookie continues to track their behavior. Pixels enable retargeting, which means that the same ads might be displayed on other websites that the user visits. Tracking tags are also known as pixels, tracking pixels, re-targeting pixels, and conversion pixels. For more technical details on the tracking tag anatomy and functionality, see [Tracking Tags](/v3/portal/data/doc/TrackingTagsOverview).

To create a tracking tag, specify all the required properties in a [POST /v3/trackingtag](/v3/portal/api/ref/post-trackingtag) call. For example:

{

    "AdvertiserId": "{advertiserid}",

    "TrackingTagName": "Tracking Tag",

    "TrackingTagType": "Conversion",

    "TrackingTagLocation": "https://www.domain.com"

}

The following is a sample response for an image pixel with a tracking tag ID assigned.

{

    "AdvertiserId": "{advertiserid}",

    "TrackingTagId": "{trackingtagid}",

    "TrackingTagName": "Tracking Tag",

    "TrackingTagType": "Conversion",

    "TrackingTagLocation": "https://www.domain.com",

    "Revenue": null,

    "Currency": null,

    "ContainerTagBody": null,

    "FirstPartyDataId": {firstpartydataid},

    "TrackingTagCategory": "StaticTag",

    "TrackingTagAvailability": "Available",

    "OfflineDataProviderId": null,

    "UniversalPixelName": null,

    "HitCount7Day": 0,

    "TagRedirectUri": null,

    "HouseholdEnabled": true,

    "ImageTag": "<img height=\\"1\\" width=\\"1\\" style=\\"border-syle:none;\\" alt=\\"\\" 

    src=\\"//insight.adsrvr.org/track/conv/?adv={advertiserid}&ct=0:{trackingtagid}&fmt=3\\"/>",

    "iframeTag": "<iframe width=\\"0\\" height=\\"0\\" name=\\"Trade Desk Tracking - {trackingtagname}\\" 

    frameborder=\\"0\\" scrolling=\\"no\\" 

    src=\\"//insight.adsrvr.org/tags/{advertierid}/{trackingtagid}/iframe\\"></iframe>"

}