# Prism: Precision through Exclusion

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/Prism
- Category: Guides

---

# Prism: Precision through Exclusion

Prism is a performance-enhancing feature that focuses on the most valuable impressions. Just like a physical prism selectively refracts and disperses light to reveal specific colors or elements, Prism excludes irrelevant user-based and non-user-based signals that are unlikely to benefit a campaign. To ensure exclusions happen without compromising campaign delivery, it works in real time with the pacing algorithm. Here's what you need to know about Prism:

*   By default, Prism is disabled.
*   You can enable the Prism settings at the advertiser level and have them automatically propagated to all ad groups created for the advertiser.
*   You can change Prism settings for all individual instances as needed when creating or updating them.
*   You cannot turn on Prism if you are advertising in the following IAB categories: Personal Finance, Careers, Real Estate.
*   In REST API, Prism is controlled by the `AudienceExcluderEnabled` property at the advertiser and ad group levels.
*   In GraphQL API, Prism is controlled by the `prism` property at both the advertiser and ad group levels.

> **NOTE**: Prism is generally not available for specific market types (such as Programmatic Guaranteed), specific channels (such as digital out of home (DOOH)), and advertisers working with sensitive categories (unless Prism appears for them as an option in the platform UI).

## 

Enable Prism[](#enable)

You can enable Prism using GraphQL or REST at either the advertiser or ad group level. The following table is a summary of the Prism properties.

| API | Advertiser-Level Prism Property | Ad Group-Level Prism Property |
| REST | `AdvertiserAudienceSettings.AudienceExcluderEnabled` | `RTBAttributes.AudienceTargeting.AudienceExcluderEnabled` |
| GraphQL | `prism` | `prism` |

To enable Prism at the advertiser or ad group level in REST, use the respective POST or PUT endpoints with the `AudienceExcluderEnabled` property set to `true`.

The following sections provide examples for enabling Prism in GraphQL.

### 

Advertiser[](#advertiser)

To enable Prism for an advertiser in GraphQL, do the following:

1.  (Optional) [Check](/v3/portal/api/doc/AdvertiserGQLQueryExamples#prism-query) if Prism is enabled for the advertiser.
2.  Use the `advertiserUpdate` mutation to set the `prism.isEnabled` property to `true`. See the following mutation example.

mutation {

  advertiserUpdate(

    input: {

      id: "ADVERTISER\_ID\_PLACEHOLDER",

      dataSettings: {

        prism: {

          isEnabled: true

        }

      }

    }

  ) {

    data {

      id

      dataSettings {

        prism {

          isEnabled

        }

      }

    }

    userErrors {

      field

      message

    }

  }

}

This enables Prism for all new ad groups. To update Prism settings for individual ad groups, see [Ad Group](#adgroup).

### 

Ad Group[](#ad-group)

To enable Prism for an ad group in GraphQL, do the following:

1.  (Optional) [Check](/v3/portal/api/doc/AdGroup#ad-group-prism) if Prism is enabled for the ad group.
2.  Use the `adGroupUpdate` mutation to set the `prism.isEnabled` property to `true`. See the following mutation example.

mutation {

  adGroupUpdate(

    input: {

      id: "AD\_GROUP\_ID\_PLACEHOLDER",

      dataSettings: {

        prism: {

          isEnabled: true

        }

      }

    }

  ) {

    data {

      id

      audienceSettings { 

        dataSettings {

          prism {

            isEnabled

          }

        }

      }

    }

    userErrors {

      field

      message

    }

  }

}

## 

FAQs[](#faqs)

Here are answers to frequently asked questions about Prism.

### 

How is Prism prioritized when determining bids on impressions?

Prism is evaluated first to decide if an impression is worth bidding on. If it is, Prism passes it to our distributed AI, which [sets](/v3/portal/api/doc/BidList#bid-adjustments) the final bid price. Basically, Prism helps manage budgets by avoiding low-value impressions, while the AI ensures efficient bidding on the worthwhile ones.

### 

I see a duplicate audience with "- Copy" in its name. Where did it come from?

When [cloning](/v3/portal/api/doc/CampaignCloning) a campaign, the platform also clones the audience associated with each ad group that has Prism enabled. The cloned audience has the `- Copy` suffix appended to its name, such as `AUDIENCE_NAME_PLACEHOLDER - Copy`. This duplication ensures Prism is optimized for each ad group.