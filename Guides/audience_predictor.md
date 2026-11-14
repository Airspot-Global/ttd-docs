# Audience Predictor: Automated, performance-driven audience building

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/AudiencePredictor
- Retrieved: 2026-11-14
- Category: Guides

---

# Audience Predictor: Automated, performance-driven audience building

Audience Predictor enables Koa, the artificial intelligence that powers The Trade Desk platform, to build and continuously update custom audiences of net-new users who are most likely to convert. Rather than manually selecting data segments, you turn on Audience Predictor for an ad group and Koa models lookalike segments from a conversion pixel (or another modeling source of your choice) to reach users who resemble your recent converters.

> **NOTE**: Audience Predictor is a fee-based feature. To see the current fee, in the platform UI navigation, select **Campaigns**, then on the All Campaigns action bar, click **View Fees**.

## What you need to know

- You turn on Audience Predictor for ad groups. In the API, it's controlled by the `AudiencePredictorEnabled` property as part of the ad group's performance-enhancing features.
- Enabling Audience Predictor generates a custom audience for the ad group. This audience is not compatible with Prism; the two features cannot be used together in the same ad group.
- If the ad group's pixels don't have enough data to build relevant segments, you cannot use Audience Predictor. An individual conversion pixel typically needs 1000 hits or more.
- Advertisers in the following IAB categories cannot use third-party data or custom modeling sources with Audience Predictor: Personal Finance, Careers, Real Estate.
- Building the initial audience takes 3–5 days. During the campaign flight, Koa automatically updates the audience roughly every three days, removing underperforming segments and adding new ones as they become available.

## Methodology

When Audience Predictor is turned on, Koa analyzes the ad group's primary conversion pixel (or another modeling source you choose) and models custom lookalike segments consisting of net-new users resembling users who converted in the past seven days.

Koa then builds the audience as follows:

- Koa assigns each candidate data segment a relevance score based on its similarity to the modeling source.
- The most relevant segments are added until the audience reaches its target size or the maximum segment count is reached. Target size is calculated from the ad group's daily budget, geo rails, and its performance from the previous day.

## Custom modeling sources

By default, Audience Predictor uses the ad group's primary conversion pixel as its modeling source, and considers other pixels under the advertiser to help the audience reach scale. You can instead choose a custom modeling source from the following types:

- Specific advertiser pixels (first-party pixels)
- Imported advertiser data (imported first-party data segments)
- IP addresses (cookie matched)
- CRM data segments
- Campaign seed segments

Here's what you need to know about custom modeling sources:

- Imported advertiser data segments created by retargeting audiences are "imported advertiser data with base bid" segments and cannot be used as a custom modeling source with Audience Predictor.
- An audience built from a custom modeling source is not guaranteed to scale. Unlike the default configuration, a custom source uses only the lookalike results from the pixels or segments you choose. Other pixels under the advertiser are not considered to help the audience reach scale.

## FAQs

The following is a list of commonly asked questions about Audience Predictor.

### Can I use Audience Predictor together with Prism?

No. Prism and Audience Predictor cannot be used together on the same ad group. Both features generate a custom audience for the ad group, and the two are mutually exclusive.

### Can I use Audience Predictor on an Audience Unlimited campaign?

Yes. If an ad group uses an Audience Predictor audience, it continues to use Audience Predictor rather than switching to Audience Assistant, even on an Audience Unlimited campaign. For the broader distinction between the two, see What's the difference between Audience Predictor and Audience Assistant?

### How long does it take before Audience Predictor starts serving impressions?

Building the initial models and creating the data group can take 3–5 days after you turn on Audience Predictor.

### Will the audience Koa builds stay the same for the life of the campaign?

No. Koa updates the audience approximately every three days during the flight, removing underperforming segments and adding new, high-value segments when available.

### Why is Audience Predictor unavailable for my ad group?

Audience Predictor requires enough conversion data to build relevant lookalike segments — usually 1,000 hits or more on the individual conversion pixel. If the ad group's pixels don't meet that threshold, the option is unavailable.

### Can any advertiser use a custom modeling source with Audience Predictor?

No. Advertisers in the Personal Finance, Careers, or Real Estate IAB categories cannot use third-party data or custom modeling sources with Audience Predictor.

### If I use a custom modeling source, is my audience still guaranteed to scale?

No. A custom-source audience includes only the lookalike results from the pixels or segments you selected. Unlike the default (non-custom) configuration, other pixels under your advertiser aren't considered to help the audience reach scale.
