# Campaign Time Zones

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/CampaignTimeZones
- Category: Guides

---

# Campaign Time Zones

A time zone is a geographic area that uses the same standard time for legal, commercial, and social purposes. Time zones tend to follow the boundaries between countries and their subdivisions instead of strictly following longitude, because it is convenient for areas in frequent communication to keep the same time. All time zones are defined as offsets from Coordinated Universal Time (UTC), ranging from UTC−12:00 to UTC+14:00. The offsets are usually a whole number of hours, but a few zones are offset by an additional amount time, such as India, South Australia (30 minutes), and Nepal (45 minutes). For details and definitions of the different time zones, see the Wikipedia [Time Zone](https://en.wikipedia.org/wiki/Time_zone) article.

The Trade Desk platform uses time zones in campaigns, reports, and billing. To ensure that your campaign doesn't overspend and that your reporting is correct, keep time zone settings in mind when you set up your ad server reporting or your campaign. Here's what you need to know about time zones in The Trade Desk platform:

*   We use the standard Olson [time zone names](#time-zone-names) defined in the [windowsZones.xml](https://github.com/unicode-org/cldr/blob/main/common/supplemental/windowsZones.xml) file.
*   By default, all campaigns are set to run in Coordinated Universal Time (UTC), which appears as `Etc/GMT` in the response.
*   You can select a different time zone for your campaign when you create or update it.
*   Reporting is done based on UTC regardless of how you set your campaign time zone.

## 

How Time Zones Affect Pacing, Reporting, and Billing[](#reporting-pacing-billing)

> **IMPORTANT**: Be sure you understand how pacing, bidding, and billing might be affected if you change time zones.

Since campaign pacing, bidding, and billing in The Trade Desk platform are standardized on UTC, here's what you need to know if you decide to change the time zone for a campaign:

*   You might see discrepancies between your campaign settings and reported metrics at the end of the month. For example:
    *   If a campaign is set to end at midnight Eastern Standard Time (EST) on January 31st, the campaign will show spend through the morning of February 1st, because midnight EST is 5:00 AM UTC.
    *   Alternatively, if your campaign is set to run in UTC, but your ad server reports in EST, then with a campaign flight of January 1st to January 31st (UTC), the campaign ends at midnight (UTC) but is reported as ending at 7:00 PM (EST), five hours early.
*   Since billing is tracked in UTC, be sure to note when the billing cycle ends in the campaign time zone, especially if you intend to keep your accounting within customary boundaries such as a billing month, fiscal year, and so on. For example, if you set a campaign to end at midnight Pacific Standard Time (PST, UTC -8) on December 31, spend and billing will continue through 8:00 AM UTC on January 1st.

The following diagram illustrates what happens to a campaign that is set to end on October 31 at midnight but actually ends early in the PDT and EDT time zones and runs over in the IST and SGT time zones. This affects pacing and monthly billing, respectively, because they are standardized on UTC.

![Campaign time zone example](/v3/content/docs/Images/campaign-timezone-example.svg)

## 

Time Zone Names[](#time-zone-names)

The time zone names used in the platform are defined in the [windowsZones.xml](https://github.com/unicode-org/cldr/blob/main/common/supplemental/windowsZones.xml) file. In this file, all time zones are organized into groups by UTC time zone specified in the comments. For example, here's the _(UTC-08:00) Pacific Time (US & Canada)_ group.

<!-- (UTC-08\\:00) Pacific Time (US & Canada) -->

<mapZone other\="Pacific Standard Time" territory\="001" 

type\="America/Los\_Angeles"/>

<mapZone other\="Pacific Standard Time" territory\="CA" 

type\="America/Vancouver"/>

<mapZone other\="Pacific Standard Time" territory\="US" 

type\="America/Los\_Angeles"/>

<mapZone other\="Pacific Standard Time" territory\="ZZ" type\="PST8PDT"/>

In each UTC time zone group, all territories share the same standard time specified by the `other` value. For example, in the _(UTC-07:00) Arizona_ group, each time zone is in the `US Mountain Standard Time` region. Time zones that share the same region have the same time of day.

<!-- (UTC-07\\:00) Arizona -->

<mapZone other\="US Mountain Standard Time" territory\="001" 

type\="America/Phoenix"/>

<mapZone other\="US Mountain Standard Time" territory\="CA" 

type\="America/Creston America/Dawson\_Creek America/Fort\_Nelson"/>

<mapZone other\="US Mountain Standard Time" territory\="MX" 

type\="America/Hermosillo"/>

<mapZone other\="US Mountain Standard Time" territory\="US" 

type\="America/Phoenix"/>

<mapZone other\="US Mountain Standard Time" territory\="ZZ" type\="Etc/GMT+7"/>

The specific time zone names that you can pass in your campaign requests are the `type` attribute values. For example, `"TimeZone": "Asia/Singapore"`.

<!-- (UTC+08\\:00) Kuala Lumpur, Singapore -->

<mapZone other\="Singapore Standard Time" territory\="001" 

type\="Asia/Singapore"/>

<mapZone other\="Singapore Standard Time" territory\="BN" type\="Asia/Brunei"/>

<mapZone other\="Singapore Standard Time" territory\="ID" 

type\="Asia/Makassar"/>

<mapZone other\="Singapore Standard Time" territory\="MY" 

type\="Asia/Kuala\_Lumpur Asia/Kuching"/>

<mapZone other\="Singapore Standard Time" territory\="PH" type\="Asia/Manila"/>

<mapZone other\="Singapore Standard Time" territory\="SG" 

type\="Asia/Singapore"/>

<mapZone other\="Singapore Standard Time" territory\="ZZ" type\="Etc/GMT-8"/>

The default time zone that all campaigns use is `Etc/UTC`, which is part of the _(UTC) Coordinated Universal Time_ UTC group.

> **NOTE**: You do not need to specify this value in the request.

<!-- (UTC) Coordinated Universal Time -->

<mapZone other\="UTC" territory\="001" type\="Etc/UTC"/>

<mapZone other\="UTC" territory\="ZZ" type\="Etc/UTC Etc/GMT"/>

### 

Time Zone Names in Requests and Responses

You can pass any `type` attribute value from the same time zone group in your request, but the response will return only the time zone name with a `territory` value of `001`, which is the main time zone name of the UTC group.

![campaign time zone example](/v3/content/docs/Images/time-zone-main-example.svg)

For example, if the time zone you want to use is `America/Hermosillo` in the _(UTC-07:00) Arizona_ group, use the `America/Phoenix` value instead, as this is the value that will be returned in the response for any territory in the group.

> **TIP**: To avoid confusion, include the `type` attribute value from the top row of the time zone group.

The following table provides an example of the (UTC-07:00) Arizona time zone values in requests and responses.

| Request Value | Response Value |
| `America/Phoenix` | `America/Phoenix` |
| `America/Creston America/Dawson_Creek America/Fort_Nelson` | `America/Phoenix` |
| `America/Hermosillo` | `America/Phoenix` |
| `Etc/GMT+7` | `America/Phoenix` |

## 

Change a Campaign Time Zone[](#change-a-campaign-time-zone)

> **IMPORTANT**: If you set up a campaign in your local time zone without considering the equivalent UTC time, you will likely see inconsistencies in the way your campaign paces and bids, as well as your billing for the campaign. For details, see [How Time Zones Affect Pacing, Reporting, and Billing](#reporting-pacing-billing).

To change the campaign time zone, complete the following steps:

1.  In the [windowsZones.xml](https://github.com/unicode-org/cldr/blob/main/common/supplemental/windowsZones.xml) file, find the UTC group that has the time zone you want to use.
2.  In the top row of the time zone group, with the `territory` value of `001`, copy the top `type` attribute value. For example, if the time zone you want to use is in the _(UTC-08:00) Pacific Time (US & Canada)_ group, copy the `America/Los_Angeles` value.
3.  In a [POST /v3/campaign](/v3/portal/api/ref/post-campaign) or [PUT /v3/campaign](/v3/portal/api/ref/put-campaign) call, set the `timezone` property value to the time zone you have copied, as shown in the following code snippet. For a complete example with all required campaign properties, see [Create a Campaign](/v3/portal/api/doc/Campaigns#create-campaign).

{

    "AdvertiserId": "pt8jkg3",

    "CampaignName": "New Campaign XYZ",

    "TimeZone": "America/Los\_Angeles"

}

## 

FAQs[](#faqs)

The following is a list of commonly asked questions about campaign time zones.

### 

Why is the time zone name in the response different from the one I sent in the request?

The response returns only the main top-level time zone name that has a `territory` value of `001` regardless of which time zone name you set. However, since the returned time zone and the one you set share the same UTC time zone group, both names use the same time zone. For details, see [Time Zone Names in Requests and Responses](#time-zone-names-in-requests-and-responses).

### 

Where can I get a list of time zone values that I can use?

In the [windowsZones.xml](https://github.com/unicode-org/cldr/blob/main/common/supplemental/windowsZones.xml), use the corresponding `type` attribute value with the time zone name that you want to use. For details, see [Time Zone Names](#time-zone-names).

### 

Do I have to set the time zone for my campaign?

No. All campaigns are set to run in Coordinated Universal Time (UTC), so you do not need to set your campaign time zone unless you want to change it.

### 

What time zone is Etc/GMT?

The standard Universal Coordinated Time (UTC) which is the default value that you will see in the response.

### 

Can I pass a null or an empty time zone value?

No. If you send a null or empty `timezone` value in the request, you will receive an error.

### 

Will adjusting the campaign time zone affect reporting?

Reporting is done based on UTC regardless of how you set your campaign time zone. For details, see [How Time Zones Affect Pacing, Reporting, and Billing](#reporting-pacing-billing).