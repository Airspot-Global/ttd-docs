# Channels

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/Channel
- Category: Guides

---

# Channels

After you've identified your ideal audience for targeting using seeds and established your budgets, consider the various campaigns and channels that can be used to reach them. In Kokai, channels are used to inform bidding behavior and provide recommendations and insights. For example, if you choose `Display`, we'll buy only display content for that campaign and [ad group](/v3/portal/api/doc/AdGroup). If you choose `TV` for a campaign and ad group targeting display inventory, we won't bid.

By viewing consumers through an omnichannel lens, you can engage consumers across multiple devices and channels where they spend their time. This allows you to control bidding behavior without relying on device and media type. Expanding into additional channels, such as Connected TV (CTV), audio, and Digital Out-Of-Home (DOOH), can boost performance, optimize the consumer's journey, and drive conversions.

## 

Best Practices[](#best-practices)

To successfully coordinate your funnel with your channels and audiences, follow these recommendations.

| Recommendation | Notes |
| If you want to advertise on multiple channels, create a separate campaign for each channel you want to target. This ensures that your campaign settings, goals, and optimizations align with the channel attributes, signals, and inventory. | If you are using TV, display, and audio, set up three distinct campaigns in the platform. |
| To represent different stages of the funnel within the same campaign, equate each ad group with a unique audience. | Designate a channel for your campaign and then create three distinct ad groups. Each ad group targets a different part of the funnel in the same campaign: prospecting, conquesting, and retargeting audiences. |
| Set up distinct KPI goals for each campaign and ad group. | The prospecting ad group introduces the consumer to the product, the conquesting ad group might drive them toward the product homepage, and the retargeting ad group might drive them toward the actual purchase. |

> **NOTE**: The audiences described here correspond to ad group funnel locations (awareness, consideration, and conversion), although the ultimate goal for each audience is driving conversions and sales. For more details on funnel locations, see [Ad Groups](/v3/portal/api/doc/AdGroup#funnel-location).

## 

Campaign and Ad Group Channels[](#primary-channel)

Setting the `PrimaryChannel` property for your campaign allows the platform to provide specific recommendations and automatically optimize toward reaching your goals. Here's what you need to know about selecting channels:

*   When creating a campaign, you must select a channel. It is one of the requirements along with the [primary goal](/v3/portal/api/doc/GoalsKPIs).
*   All campaign ad groups should have the same value in their `ChannelId` properties as the channel of the parent campaign.
*   If needed, you can change the campaign channel when updating or [cloning](/v3/portal/api/doc/CampaignCloning) a campaign, but you cannot remove it.
*   If you want to bid on different types of inventory, you should create a separate campaign for each channel you want to use.
*   You cannot update the ad group channel after the flight starts.
*   The ad group creative type must match the channel.

Select a channel for your campaign and channel IDs for your ad groups from the following options.

| Channel | Definition |
| `Display` | Ads served in standard, reserved spaces on web pages. These ads can be image- or text-based and found at the top of the webpage, in the middle, on the side, or at the bottom. |
| `Video` | Ads running before, during, and after video content playing on websites. Video ads can also be embedded within online articles or through banner ads. |
| `Audio` | The digital streaming of audio content, such as music, talk shows, and podcasts, through platforms like Spotify and Pandora. |
| `TV` | Premium, long-form content (such as full episodes) streaming through apps on CTVs or over-the-top devices. Ads can be served before content or during traditional commercial breaks. |
| `NativeDisplay` | Ads formatted to blend in with the design, function, and tone of the page on which they are placed. The disguised nature of native ads means consumers may not be able to easily distinguish a native ad from the publisher’s own content. |
| `NativeVideo` | Video ads that seamlessly integrate with the platform they appear in for amplified storytelling. A native video ad can extend up to five minutes. |
| `DigitalOutOfHome` | DOOH is primarily outdoor digital ad placements, such as digital billboards and signs in a variety of places including gas stations, airports, freeways, the sides of buildings, and so on. If you want to set DOOH as your channel but this option isn't available, contact your Technical Account Manager.  
**NOTE**: The DOOH value for ad groups is `OutOfHome`. |
| `Mixed` | Ads that use various media or device channels. This is a valid channel category if you do not designate a channel ID in your API POST calls. |

> **NOTE**: Some `ChannelId` settings are specific to certain channels. For example, content genre targeting for CTV wouldn’t apply to the `Display` channel.

For details, examples, and specifications for each channel, see the [Knowledge Portal](https://desk.thetradedesk.com/knowledge-portal/en/channels-intro.html).

## 

FAQs[](#faq)

We've got answers to your most commonly asked questions.

### 

Can I assign multiple channels to a single campaign?

Yes. While you can assign multiple channels to a single campaign, only the ad group's channel is used for bidding. Make sure each ad group has only one channel.

For best practices, be sure ad groups have the same value in their `ChannelId` properties as the channel of the parent campaign. To target multiple channels and use the same campaign settings, clone the campaign and update the channel for the new copy of the campaign.

### 

How do I update the ad group channel?

Update the `ChannelId` property for the ad group with the new channel option. For best practices, be sure it's the same value as the channel of the parent campaign.

> **NOTE**: You cannot update the ad group channel after the flight starts.

### 

The API reference says the Mixed value for the ChannelId property is deprecated, but here it lists Mixed as allowed. Can you clarify this?

Yes. `Mixed` is an allowed default value used as a placeholder when no channel ID is specified for an ad group. The API reference labels this as `Deprecated`, indicating it's not a value you should select.