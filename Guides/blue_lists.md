# Blue Lists for Customizing Inventory Marketplace

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/BlueLists
- Category: Guides

---

# Blue Lists for Customizing Inventory Marketplace

A Blue List is an inventory management tool for large agencies to fine-tune and target premium inventory on the open internet, typically with the Sellers and Publishers 500+ (SP500+) Marketplace as a foundation. To create a Blue List, curate publisher lists and set supply path preferences for each publisher. The Blue List scales seamlessly, as it automatically updates its publisher list mappings based on a provided list of domains and apps. To access the Blue List feature, contact your Technical Account Manager.

Here's what you need to know about Blue Lists:

*   You can [create](#create-blue-list) a Blue List for a partner or advertiser using SP500+ publishers (marketplace ID `gicljc6`) as a starting point, or build a custom list from scratch.
*   You can add [publisher lists](/v3/portal/api/doc/PublisherLists) at the marketplace or channel level, and configure them to include or exclude specific publishers from the Blue List. For details, see [Add Publisher Lists](#add-publisher-lists).
*   Blue Lists must be at least 50% of the scale of the [SP500+](/v3/portal/api/doc/SP500) marketplace across all channels. You cannot publish a Blue List unless the scale scores meet that threshold. For details, see [Scale Score](#scale).
*   You can specify [supply path preferences](#supply-path-preferences) for each publisher by downloading, updating, and uploading an Excel file. The default preference is `Optimization with AI-powered SPO` (supply-path optimization).
*   To be more efficient, you can upload supply path preferences before publishing the Blue List.
*   Blue Lists do not include deals, which are managed separately in [Price Discovery and Provisioning (PDP)](/v3/portal/pdpapi/doc/PdpApiOverview). However, deals can be assigned to ad groups targeting Blue Lists, meaning Blue List rules apply to those deals too.

Blue Lists prioritize impressions with higher quality gradients. If two impressions are otherwise identical, the one with higher quality gradients is preferred for the Blue List. The following table shows the ad formats and quality gradients that Blue Lists target.

| Format | Quality Gradients |
| Display, video, and native display, but not native video | Ad load, ad refresh rate, viewability |
| Video-specific | Playback type |
| TV-specific | Content duration, signal transparency, playback type |
| All formats | Additional applicable quality gradients |

The following sections guide you through best practices for curating publisher lists for a Blue List, as well as creating and updating a Blue List. That includes including linking the publisher lists to a Blue List and optimizing supply path preferences.

## 

Get Started[](#get-started)

Creating a Blue List begins with upgrading an existing site or app list, and considering factors like publishing the list at the marketplace or channel level and blocking certain publishers.

The following sections outline key tasks and provide a code example for creating a Blue List.

### 

Add Publisher Lists[](#add-publisher-lists)

To build your Blue List, [add](/v3/portal/api/doc/PublisherLists) publisher lists from the partner’s library, as long as they're upgraded from a site or app list and include at least one publisher. Publisher lists update automatically with changes from the platform library.

> **IMPORTANT**: To use available publisher mappings for sites or apps in your Blue List, you must upgrade the mapping manually through the [Inventory Selection (**Is**) tile](https://desk.thetradedesk.com/knowledge-portal/en/is.html#is---inventory-selection) in the platform UI. Publisher lists don't update automatically with new mappings. Although linked lists may show unmapped sites and apps, this won't affect their performance.

The following describes the statuses for publishers included in a Blue List, determined by their publisher list type and inclusion in the SP500+ marketplace:

*   Included publishers: We will buy from this publisher.
*   Excluded publishers: The publisher is in your custom block list.
*   Blocked publishers: Our analysis indicates the publisher inventory won’t run in a Blue List.

> **NOTE**: If you don’t upload a publisher list, we will only buy inventory through the SP500+ marketplace, which has the most transparent and reliable sellers.

### 

Marketplace and Channel Levels[](#channel-curation)

To optimize your Blue List, add publisher lists at the marketplace or channel level. You can use SP500+ publishers as a starting point or build from scratch. To block publishers, add the publisher lists as exclusion lists even if they appear in the 500+ marketplace.

Adding publisher lists at the channel level is the same as at the marketplace level, except for the following differences:

*   You must add a Blue List for each channel manually if the SP500+ marketplace is disabled.
*   In the `publisherLists` array, you must add a `channel` field for each `publisher` field.

> **IMPORTANT**: Switching between the marketplace and channel levels resets existing Blue Lists. For details, see [Update a Blue List](#update-blue-list).

### 

Blocked Publishers[](#block)

Publishers are blocked from the marketplaces if they are not transparent and reliable sellers or do not have recent spend against them. Here's what you need to know about the blocks:

*   If you are using the SP500+ marketplace, we remove any publisher blocks if this publisher appears in your inclusion list.
*   Sellers blocked in the SP500+ marketplace cannot be unblocked. We buy your publishers through all seller paths except for the blocked sellers.
*   We don’t include or block sites and apps that are not mapped to publishers. However, they will still transact if eligible impressions are available in the marketplace through any unblocked sellers.

If you don't think a publisher should be blocked from the marketplace, contact your Technical Account Manager.

### 

Create a Blue List[](#create-blue-list)

To create a Blue List, use the `marketplaceCreate` mutation. Enabling and publishing the Blue List makes it the default inventory marketplace for all linked advertisers' new campaigns, and advertisers will automatically target it. Tailor your Blue List with your agency or brand strategy by doing the following:

1.  In the `baseMarketplaceId` field, do either of the following:
    *   To start targeting with the SP500+ marketplace as a foundation, enter `gicljc6`.
    *   To build a custom list without using the SP500+ marketplace, set this field to `null`.
2.  In the `publisherLists` field, [add](#add-publisher-lists) IDs of the publisher lists you want to add the Blue List.

> **TIP**: Use the domain name or given publisher name to [find](/v3/portal/api/doc/PublisherLists#lookup) the publisher ID.

3.  In the `publisherListCurationType` field, do either of the following:
    *   To curate at the marketplace level, enter `NONE`.
    *   To curate per [channel](#channel-curation), enter `CHANNEL`.

> **TIP**: Add exclusion-based publisher lists to block specific publishers, even if they appear in the SP500+ marketplace.

#### Example

The following `marketplaceCreate` example shows how to create a Blue List that starts its targeting with the SP500+ marketplace, links to a publisher list, and curates that list at the marketplace level.

mutation {

  marketplaceCreate(input: {

    name: "BLUE\_LIST\_NAME\_PLACEHOLDER",

    shortName: "BLUE\_LIST\_SHORT\_NAME\_PLACEHOLDER",

    baseMarketplaceId: "gicljc6",

    owner: PARTNER,

    ownerEntityId: "a12bcdef",

    isPublished: true,

    isEnabled: true,

    publisherLists: \[{ publisherListId: 12345678 }\],

    publisherListCurationType: NONE

  }) {

    data {

      id

      name

      shortName

      isPublished

      isEnabled

      baseMarketplace {

        id

        name

      }

      publisherListCurationType

      publisherLists {

        edges {

          channel

          ... @defer {

            includedPublisherPropertiesCount

            blockedPublisherPropertiesCount

          }

          node {

            id

            name

            adjustmentType

            bidLinesCount

            ... @defer {

              publisherPropertiesCount

            }

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

The mutation returns the Blue List ID in the `id` field, which is required for updating the Blue List.

## 

Manage Blue Lists[](#manage-blue-list)

After creating a Blue List, you can optimize it by adjusting publisher lists, changing its curation type, and customizing supply path preference for each publisher.

The following sections provide details for updating a Blue List and setting supply path preferences.

### 

Update a Blue List[](#update-blue-list)

To update a Blue List, use the following `marketplaceUpdate` mutation example. This allows you to add or remove publisher lists and change the publisher list curation type. Be sure to use the `id` property instead of the `owner` and `ownerEntityId` properties for creating a Blue List.

Here's what you need to know about updating Blue Lists:

*   Switching the `publisherListCurationType` field between the `NONE` and `CHANNEL` options resets the links to publisher lists. To resolve this, you need to [link](#add-publisher-lists) new publisher list IDs with the [included publishers](#included) status in the same mutation. When switching to the `CHANNEL` option, you must associate each publisher list with a channel.
*   To stop using a Blue List and revert to the SP500+ or open marketplace at the partner or advertiser level, contact your Technical Account Manager.

The following `marketplaceUpdate` mutation shows how to update a Blue List by linking two publisher lists and their channels with curation enabled.

mutation {

    marketplaceUpdate(input: { 

        id: "a12bcde", 

        name: "BLUE\_LIST\_NAME\_PLACEHOLDER", 

        publisherListCurationType: CHANNEL, 

        publisherLists: \[

            { channel: TV, publisherListId: 13245678 }, 

            { channel: DISPLAY, publisherListId: 1324567 }

        \] 

    }) {

        data {

            id

            name

            publisherListCurationType

            publisherLists {

                edges {

                    channel

                    node {

                        id

                    }

                }

            }

        }

        userErrors {

            message

            field

        }

    }

}

### 

Supply Path Preferences[](#supply-path-preferences)

To ensure we buy the best path based on value, after linking publishers to your Blue Lists, we recommend considering more inventory by keeping the automatic optimizations enabled. However, you can set your preferred supply paths to publishers manually. To access this feature, contact your Technical Account Manager.

There are three supply-path preference options available, as shown in the following table:

| Preference | What It Means | When to Use It |
| `Optimization with AI-powered SPO` (default) | Uses AI to find the most efficient path for every impression, considering all available paths. | Recommended in most cases for maximum optimization and scale. |
| `Partial optimization` | Prioritizes your preferred [intermediaries](/v3/portal/resources/doc/Glossary#intermediary), then uses AI to optimize across the rest. | Use when you want to give preference to specific SSPs but still allow flexibility. |
| `Manual configuration` | Restrict buying to only the intermediaries you name, without AI optimization. | Use for strict SSP deals or when testing a smaller set of paths. |

> **NOTE**: You cannot set supply path preferences for sites or apps that are not mapped to a publisher in the Blue List. The spend for an unmapped site or app defaults to `Optimization with AI-powered SPO`. This should affect less than 1% of the spend and have minimal impact.

Here's what you need to know about preferred supply paths to publishers:

*   We consider SSPs to be intermediaries because they are not a direct path to inventory.
*   Percent thresholds are targets, but supply factors like availability and in-platform quality filters can affect allocations.
*   If [SP500+](/v3/portal/api/doc/SP500) is enabled, the following applies:
    *   It dynamically includes qualified new publishers from the open internet in the supply path, which defaults to `Optimization with AI-powered SPO`.
    *   Its SPO settings apply to the Blue List unless you override them.
*   Preferred supply paths respect existing supply vendor targeting and optimization settings configured outside of the Blue List.

We recommend the following regarding supply paths:

*   As existing supply vendor targeting and global optimizations are being phased out, migrate those use cases to Blue Lists.
*   If you use SP500+, keep its SPO settings enabled to ensure quality, transparency, and value for both marketers and publishers. If you need to adjust path optimization, the best place to do so is in your Blue List, where you have access to the latest tools and data insights.

### 

Get Supply Path Status of a Blue List[](#current-status)

Before managing the supply path configurations, get the supply path status of the desired Blue List using the following query.

query GetBlueListSupplyPathStatusExample {

  partner(id: "PARTNER\_ID\_PLACEHOLDER") {

    id

    name

    marketplaces {

      nodes {

        id

        name

        baseMarketplace {

          id

          name

        }

        owner

        isEnabled

        isPublished

        isUsingManualSupplyPathConfiguration

        publisherListCurationType

        publisherLists {

          nodes {

            id

            name

          }

        }

      }

    }

  }

}

The query retrieves all marketplaces your partner is using. Typically, this returns the SP500+ marketplace, which is a global marketplace, along with the Blue List marketplaces.

The following code example shows that when the `isUsingManualSupplyPathConfiguration` property is set to `true`, it indicates that the associated marketplace is using a Blue List with a custom supply path configuration.

{

  "data": {

    "partner": {

      "id": "PARTNER\_ID\_PLACEHOLDER",

      "name": "PARTNER\_NAME",

      "marketplaces": {

        "nodes": \[

          {

            "id": "abcdef1",

            "name": "Sellers and Publishers 500+",

            "baseMarketplace": null,

            "owner": "GLOBAL",

            "isEnabled": true,

            "isPublished": true,

            "isUsingManualSupplyPathConfiguration": false,

            "publisherListCurationType": "NONE",

            "publisherLists": {

              "nodes": \[\]

            }

          },

          {

            "id": "BLUE\_LIST\_ID\_PLACEHOLDER",

            "name": "PARTNER\_NAME",

            "baseMarketplace": {

              "id": "abcdef1",

              "name": "Sellers and Publishers 500+"

            },

            "owner": "PARTNER",

            "isEnabled": true,

            "isPublished": true,

            "isUsingManualSupplyPathConfiguration": true,

            "publisherListCurationType": "NONE",

            "publisherLists": {

              "nodes": \[\]

            }

          }

        \]

      }

    }

  }

}

### 

Update an Excel File[](#configure-excel)

To set the supply path preferences, follow these steps:

1.  [Download](#download-configs) an Excel file with the current configurations.
2.  [Update](#update-supply-paths) the supply-path preference options and intermediaries for targeted publishers in the Blue List.
3.  [Upload](#upload-changes) the changes to start buying through your preferred paths.

> **TIP**: To be more efficient, you can upload supply path preferences before publishing the Blue List.

The following sections detail the workflow for setting supply paths for Blue Lists manually.

#### Download Supply Path Configurations

To generate a download URL for an Excel file containing the supply path configurations of a Blue List, use the `marketplacePathPreferencesExport` mutation with the Blue List ID.

Here is a `marketplacePathPreferencesExport` mutation example showing how to generate the URL.

mutation {

  marketplacePathPreferencesExport(input: { marketplaceId: 

  "BLUE\_LIST\_ID\_PLACEHOLDER" }) {

    data {

      exportUrl

    }

    errors {

      ... on InSchemaError {

        field

        message

      }

    }

  }

}

The downloaded Excel file lists all publishers included in the Blue List.

#### Update Publisher Supply Paths

After downloading the Excel file, update the supply path options. The file includes the following columns.

| Column | Editable? | Description |
| Publisher Name | Read-only | The name of the publisher is filled in automatically. |
| Publisher ID | Read-only | The unique ID of the publisher is filled in automatically. |
| Path Optimization | Editable | Enter your desired preference (the default is `Optimization with AI-powered SPO`). For details, see the [supply-path preference options](#wyntk-supply-paths). |
| Preferred Intermediaries | Editable | (Optional) Enter intermediary names that should bypass the selected optimization option. |
| Available Intermediaries | Read-only | A list of intermediaries for each publisher is filled in automatically based on an analysis of platform avails data from the previous seven days. |
| Error Description | Read-only | User input validation and an informative message are filled in automatically for correcting any errors detected in the publisher-specific input. |

After updating the file, [upload](#upload-changes) it.

#### Upload Supply Path Configurations

To upload the updated Blue List supply path configurations, use the following steps.

| Step | Description | Method |
| **1** | [Generate](#generate-upload-URL) a unique upload URL for the updated Excel file. | `fileUpload` mutation |
| **2** | [Upload](#upload-updated-excel) the updated Excel file. | HTTP PUT request |
| **3** | [Import](#import-config) the supply path configurations from the uploaded Excel file to The Trade Desk graph. | `marketplacePathPreferencesImport` mutation |

##### Generate File Upload Mutation Example

The following `fileUpload` mutation example shows how to create a unique upload URL for an updated Excel file:

fileUpload(

    contentType: "application/vnd.openxmlformats-

    officedocument.spreadsheetml.sheet",

    fileExtension: "xslx"

) {

    uploadUrl

    id

}

The returned `uploadUrl` property contains a file ID and upload URL:

{

  "id": "1234a5b6-c7d8-9e0f-1ghi-12j4567klm.xlsx",

  "uploadUrl": "https://ttd-uapi-uploads-

  sb.s3.amazonaws.com/uploads/\[FILE\_ID\_FROM\_GENERATED\_UPLOAD\_URL\]"

}

Use the returned file ID and upload URL to [upload](#upload-updated-excel) the file.

##### HTTP PUT Upload Example

The following HTTP PUT request example shows how to upload an updated Excel file with an upload URL:

curl -X PUT https://ttd-uapi-uploads-

sb.s3.amazonaws.com/uploads/UPLOAD\_URL

. -H "Content-Type: application/vnd.openxmlformats\-

officedocument.spreadsheetml.sheet"

  -H "x-ms-blob-type: BlockBlob"

. --data-binary "UPDATED\_EXCEL\_FILE"

##### Import Marketplace Path Preferences Mutation Example

The `marketplacePathPreferencesImport` mutation example hows to import supply path configurations from an uploaded Excel file to the The Trade Desk graph:

mutation {

  marketplacePathPreferencesImport(

    input: {

      marketplaceId: "BLUE\_LIST\_ID\_PLACEHOLDER",

      fileUploadId: "FILE\_ID\_FROM\_GENERATED\_UPLOAD\_URL"

    }

  ) {

    data {

      isSuccessful

    }

    errors {

      ...on InSchemaError {

        field

        message

      }

    }

  }

}

The `isSuccessful` property indicates if the new configuration is saved. Otherwise, errors are included in the `errors` property.

## 

Scale Scores[](#scale)

To ensure your Blue List is not too constrained, check your Blue List scale scores. These scores compare your Blue List to the SP500+ marketplace baseline, focusing on the lowest-scoring channel and countries linked to relevant advertisers.

Here's what you need to know about scale scores:

*   If you don't use the SP500+ marketplace as a foundation, channels that are heavily deal-based, such as CTV, audio, and digital out of home (DOOH), are not considered.
*   Only publisher inclusions and exclusions are counted, not individual sites and apps.
*   Scale scores are calculated immediately after configuration, then recalculated daily for the platform UI.
*   You cannot publish a Blue List unless the scale scores are at least 50% of the scale of the SP500+ marketplace across all channels.
*   If a scale score drops below 50% of the SP500+ scale in any channel, the Blue List is non-compliant. You'll then receive a notification through the platform UI and your Technical Account Manager. We recommend working with them to resolve this issue. Non-compliance for 30 days or more defaults new campaigns to the [SP500+](/v3/portal/api/doc/SP500) marketplace.

To look up scale scores, use the following options:

*   [Pre-calculated daily scale scores](#pre-calculated-scores)
*   [Newly calculated scale scores](#newly-calculated-scores)

### 

Look Up Pre-Calculated Scores[](#pre-calculated-scores)

To retrieve the pre-calculated daily overall and channel-specific scale scores at the marketplace level, such as for displaying on a UI, use the following `partner` query.

query GetPartnerScaleScoreExample {

  partner(id: "PARTNER\_ID\_PLACEHOLDER") {

    id

    name

    marketplaces {

      nodes {

        id

        name

        owner

        isEnabled

        isPublished

        publisherListCurationType

        supplyPathConfigurationStatus {

          isUsingCustomConfiguration

          lastUploadedPathConfigurationFileName

        }

        marketplaceScaleScore {

          overallScaleScore

          channelScaleScores {

            channel

            isIgnored

            scaleScore

          }

          scaleScoreThreshold

          isScaleScoreReady

          fixByDate

        }

      }

    }

  }

}

### 

Look Up Newly Calculated Scores[](#newly-calculated-scores)

To retrieve newly calculated overall and channel-specific scale scores, use the following `marketPlaceScaleScore` query example. These scores are more accurate than the daily scores when updating your Blue List.

query GetMarketPlaceScaleScoreExample {

  marketplaceScaleScore(

    input: {

      isSP500FoundationEnabled: true

      ownerPartnerId: "OWNER\_PARTNER\_ID\_PLACEHOLDER"

      publisherLists: \[

        {

          channel: VIDEO

          publisherListId: 123456

        }

        {

          channel: VIDEO

          publisherListId: 9012345

        }

        {

          channel: DISPLAY

          publisherListId: 23456

        }

      \]

    }

  ) {

    channelScaleScores {

      channel

      isIgnored

      scaleScore

    }

    fixByDate

    isScaleScoreReady

    overallScaleScore

    scaleScoreThreshold

  }

}

## 

FAQs[](#faqs)

The following is a list of frequently asked questions about Blue Lists.

### 

Do Blue Lists support native video?

No. Due to compromises in quality, Blue Lists do not support native video.

### 

Can I configure Blue Lists to buy open market inventory?

No. You cannot configure Blue Lists to buy from the open market. A Blue List already includes all open market inventory that meets a minimum quality threshold. We consider display, video, and native display formats as open market, but not TV, digital out of home (DOOH), and audio. The TV open market is available at your own risk.

The Trade Desk enforces its platform and marketplace policy through deal selection for all TV content in the SP500+ marketplace and Blue Lists.

### 

How do I link publisher lists to Blue Lists?

In the `publisherLists` array, enter the IDs for the publisher lists. If you are targeting publisher lists at the channel level, add the channel before the publisher ID. For an example, see [Update a Blue List](#update-blue-list).

### 

What is the difference between a Blue List and a publisher list?

A Blue List is a curated pool of premium inventory based on publisher lists and their supply path preferences, typically with the SP500+ marketplace as the foundation. A [publisher list](/v3/portal/api/doc/PublisherLists) is a centralized list of all the sites and apps associated with a specific publisher.

### 

Where does the SP500+ marketplace fit in?

The SP500+ marketplace is an option you can use to serve as a foundation for your Blue List. It includes thousands of trusted sellers and publishers for premium inventory, while blocking those that are not transparent and reliable sellers or do not have recent spend against them.

### 

Can I delete a Blue List?

No. You cannot un-publish a Blue List or revert it to a draft. For help, contact your Technical Account Manager.

### 

Can I change the default marketplace for an advertiser in a Blue List after it's been published?

Yes. To change the default marketplace, contact your Technical Account Manager.