# Platform synchronization

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/PlatformSynchronization
- Retrieved: 2026-11-14
- Category: Guides

---

# Platform synchronization

The Trade Desk supports platform synchronization through GraphQL API to sync updates. Platform synchronization is the process of connecting two or more systems together and keeping their data consistent, in order for the correct operational decisions to be made in a timely manner.

Every partner situation for this workflow is unique, but there are a few considerations to keep in mind as you move closer to a design approach:

- Why does this data need to be synchronized?
- How much data do you need to sync?
- How often does the data sync occur?
- How simple is your database schema?
- Do your customers interact with a UI?

Addressing these questions in the early phases of your workflow design can help define the best way to consume The Trade Desk data.

## Delta calls

To efficiently retrieve only the data that changed since a previous query you specify, use delta calls. This reduces the payload size for applications requiring near real-time data.

> **IMPORTANT**: To perform delta queries on ad group budget settings, such as flights, see Query ad group changes.

Here's what you need to know about making a delta call:

- Avoid sending a tracking version in your first call since there is no previous version to compare against.
- Wait 4-6 hours for results to sync and log subsequent calls in real-time. For details, see FAQs.
- Delta logs expire after 18 hours between tracking versions.
- Some deltas operate behind a workflow that has a lag between when the data is collected and when the data gets stored. This can result in a delay in tracking the latest changes.
- To request additional call volume for the delta endpoints, contact your Technical Account Manager.

### GraphQL API delta functions

To call a delta function, you must have a `changeTrackingVersion` value that marks the version history to search. You can further filter by date with the `lastUpdated` property. For details on date filters, see FAQs.

> **IMPORTANT**: If your delta function supports multiple entities, you must also specify which entity to use as an input.

The following table lists the objects that are supported by each delta function, in alphabetical order:

| Delta Function | Entities Supported |
| --- | --- |
| `adGroupDelta` | Advertiser, campaign, and partner. |
| `advertiserDelta` | Advertiser only. |
| `campaignDelta` | Advertiser and partner. |
| `creativeDelta` | Creatives only. |
| `trackingTagDelta` | Advertiser and partner. |

The following query returns the campaign delta for a given advertiser using the `campaignDelta` function and checks if more data is available with the `nextChangeTrackingVersion` and `moreAvailable` properties.

```
query GetCampaignsDeltaExample() {
  campaignDelta(
    input: {
      advertiser: {
        changeTrackingVersion: 0
      }
    }
  ) {
    nextChangeTrackingVersion
    moreAvailable
    campaigns {
      advertiser {
        id
      }
      name
      timeZone
      timeZoneIANA
      isArchived
      createdAtUtc
      lastUpdatedAtUtc
      conversionReportingColumns {
        totalCount
        nodes {
          reportingColumnId
          trackingTag {
              id
          }
        }
      }
      budget {
        total
      }
    }
  }
}
```

> **TIP**: For more examples, see our collection of Delta Python scripts.

### Query ad group changes

To get all changes in your ad groups for the given tracking version, use the ad group IDs from your response with the following `in` filter.

```
query GetAdGroupBudgetSettingsDeltaExample {
  adGroups(where: { id: { in: ["AD_GROUP_ID_PLACEHOLDER_1", "AD_GROUP_ID_PLACEHOLDER_2", "AD_GROUP_ID_PLACEHOLDER_3"] } }) {
    edges {
      node {
        campaign {
          id
        }
        adGroupFlights {
          edges {
            node {
              adGroupId
              budgetInImpressions
              campaignFlightId
              dailyTargetInAdvertiserCurrency
              dailyTargetInImpressions
              minimumSpendInAdvertiserCurrency
            }
          }
        }
      }
    }
  }
}
```

## FAQs

The following are the most commonly asked questions about the delta endpoints.

### What is the recommended workflow to pull all changes from delta endpoints within the past 24 hours?

To view all changes from delta endpoints, look through the activity log at the ad group level.

### How do I use the lastUpdated property to get the activity logs I need?

To view all changes from delta endpoints, look through the activity log at the ad group level. To track or sort delta changes by date, use the `lastUpdated` property in the GraphQL API. For details on GraphQL filters, see the GraphQL Resource Hub. When using this property, the behavior is set to update when the exact object is changed. It does not update when its relational objects or child objects are changed.

For example, you can have an ad group object that contains bid lists or an audience. When a bid list is updated or an audience is changed, the `lastUpdated` property in the ad group stays the same. However, if you modify the `isEnabled` property to allow spend, the property is updated because it's on the same ad group level. For details on object ownership and object assignment, see Entity relationships.
