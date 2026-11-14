# Create and manage bid lists in GraphQL

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/BidListsCreateManageGQL
- Retrieved: 2026-11-14
- Category: GraphQL

---

# Create and manage bid lists in GraphQL

This guide walks you through the process of creating and updating bid lists in GraphQL, including defining their key properties and propagating them to associated campaigns and ad groups. You can either create bid lists from scratch or by cloning an existing list. Bid lists can then be owned and assigned at various levels within the core entities, including partner, advertiser, campaign, and ad group. To activate a bid list, associate and enable it for its owner or a descendant.

You can also use GraphQL to look up the data you need, especially for complex data requirements or when consolidating multiple queries into a single request.

> **TIP**: If you are new to GraphQL, check out our GraphQL API Resource Hub and familiarize yourself with the basics.

To learn more about bid list terms and relationships, see Bid lists. For instructions on using our REST API, see Create and manage bid lists in REST.

Bid lines can be single- or multi-dimensional. This guide focuses on single-dimensional bid lines. To learn more about creating bid lists with multi-dimensional bid lines, see Multi-dimensional bidding.

## Requirements and guidelines

Here's what you need to know before making GraphQL calls for bid lists:

- A bid list must contain at least one bid line.
- If you try to create a bid list with bid lines of different dimensions, you will get a validation error (the bid list won't be created in that state). For example, if one bid line uses the `DomainFragment` dimension while another uses the `GeoSegmentId` dimension, it can lead to errors.
- Some dimensions use third-party providers and might incur additional fees.
- The number of bid lines may not exceed bid line relationship limits. To avoid needing to recreate bid lists at different levels, be sure to leverage inheritance. For details, see Inheritance.
- Bid lists are limited to 500,000 bid lines each, regardless of owner type (ad group, campaign, advertiser, or partner), in addition to the bid line relationship limits.
- The adjustment type and bid adjustment values must match. For details, see Adjustment types.
- The default resolution type is `APPLY_MULTIPLY_ADJUSTMENT`, which multiplies bid adjustments from a bid list to calculate the final bid adjustment. It is required for target and block lists and recommended for optimized lists.
- To streamline the management of bid lists across multiple campaigns and ad groups, use Default bid lists.

> **TIP**: To create, look up, or update multiple bid lists at once, see GraphQL API bulk operations.

The following sections provide examples of bid list mutations and queries for creating, managing, and retrieving bid list information. For basic terms and definitions, see Bid lists.

## Adjustment types

When creating a bid list, choose an adjustment type to determine bid adjustments based on bid line matches. Target and block lists allow and deny bidding based on specified dimensions. Optimized lists allow you to set bid adjustments when the request matches the bid lines.

The following table outlines the different types of bid list adjustments available.

| Adjustment Type | Description | Bid adjustment for matched bid lines | Bid adjustment for non-matched bid lines |
| --- | --- | --- | --- |
| `INCLUSION` | Includes the ad group in bidding without any bid adjustment when the request matches the bid lines. | `1` | `0` |
| `EXCLUSION` | Excludes the ad group from bidding when the request matches the bid lines. | `0` | `1` |
| `OPTIMIZED` | An optimized list can do the following: - When requests match bid lines, apply bid adjustments using decimals to ad groups, unlike inclusion or exclusion lists which are limited to `0` or `1`. - Use the resolution type to determine the final bid adjustment when an impression matches multiple bid lines. - Allow bids for impressions that do not match any bid line. | Value specified | `1` |

## Create bid lists

To create a bid list in GraphQL, you can use the `bidListCreate` mutation and manually define its bid lines and key properties, including the dimensions and bid list adjustment type. To quickly create a bid list based on an existing one for a new owner, use the `bidListClone` mutation instead. For details, see Clone bid lists for new owners.

> **TIP**: To be efficient and stay within bid line relationship limits, instead of creating new bid lists, you can associate and enable bid lists for parent-level entities. This allows bid lists to be inherited across descendants like ad groups for greater impact.

### Examples

The following are some common GraphQL mutation examples for creating bid lists, illustrating how to include or exclude impressions based on dimensions such as domain and video playback type.

#### Create a bid list based on domains

The following GraphQL mutation example creates a bid list owned by an ad group that excludes impressions from the domains `domainToExclude.com` and `otherDomainToExclude.com`. The mutation returns the ID of the created bid list.

```
mutation {
bidListCreate(
    input: {
      name: "BID_LIST_NAME_PLACEHOLDER",
      dimensions: [HAS_DOMAIN_FRAGMENT_ID],
      adjustmentType: EXCLUSION,
      bidLines: [
        {
          bidAdjustment: 0,
          volumeControlPriority: NEUTRAL,
          domainFragment: "domainToExclude.com"
        },
        {
          bidAdjustment: 0,
          volumeControlPriority: NEUTRAL,
          domainFragment: "otherDomainToExclude.com"
        }
      ],
      owner: { adGroupId: "ab1c23de" }
    }
  ) {
    data {
      id
    }
    userErrors {
      field
      message
    }
  }
}
```

#### Create a bid list based on video playback types

The following GraphQL mutation example creates a bid list owned by an ad group that targets CTV and video impressions specifically for "pre-roll" or "accompanying content" video playback types. The mutation returns the ID of the created bid list.

```
mutation {
bidListCreate(
    input: {
      name: "BID_LIST_NAME_PLACEHOLDER",
      dimensions: [HAS_VIDEO_PLAYBACK_TYPE_ID],
      adjustmentType: OPTIMIZED,
      bidLines: [
        {
          bidAdjustment: 1.5,
          volumeControlPriority: NEUTRAL,
          videoPlaybackType: PRE_ROLL
        },
        {
          bidAdjustment: 2,
          volumeControlPriority: NEUTRAL,
          videoPlaybackType: ACCOMPANYING_CONTENT
        }
      ],
      owner: { adGroupId: "ab1c23de" }
    }
  ) {
    data {
      id
    }
    userErrors {
      field
      message
    }
  }
}
```

## Clone bid lists for new owners

To quickly create a bid list based on an existing one for a new owner, use the `bidListClone` mutation. The original bid list remains unchanged, and the new bid list is automatically associated with and enabled at the new owner's entity level. Cloning counts toward the new owner's bid line relationship limits.

> **NOTE**: You cannot update fields in the `bidListClone` mutation. After you have created the clone, use the `AssociateBidList` and `bidListUpdate` mutations to modify the cloned bid list. For details, see Associate bid lists and Update bid lists.

### Example

The following `bidListClone` mutation clones a bid list and assigns it to a new owner (in this case, an ad group).

```
mutation {
    bidListClone(
        input: {
            id: "BID_LIST_ID_PLACEHOLDER",
            newOwner: {adGroupId: "NEW_OWNER_AD_GROUP_ID_EXAMPLE"}
        }
    ) {
        data {
            id
        }
        userErrors {
            field
            message
        }
    }
}
```

## Associate bid lists

Simply owning a bid list doesn't mean it's being used in bidding. You must activate bid lists. This means you must associate a bid list with a partner, advertiser, campaign, or ad group, and then enable them for their owner or its descendants. Here's what you need to know:

- You can add, remove, and update the enabled status of multiple bid lists in a single call. In this context, "add" and "remove" means add to and remove from the association list.
- You cannot associate a bid list with an entity if it's already associated to an ancestor. For check associations and other details, see Bid list queries.
- Make sure an ancestor owns the bid list, rather than a peer. For example, you cannot associate a bid list owned by an ad group with another ad group. For details, see Association.
- To avoid disabling the bid list and potential validation issues in ad group calls, set the `IsEnabled` property to `true` for the associated bid list.
- If you are using default bid lists, make sure only one bid list has the `IsDefault` property set to `true` for the same dimension combination and bid list type at the ad group level.

> **TIP**: As bid list associations at the campaign and advertiser level are not visible in the UI, it is a best practice to associate bid lists at the ad group level.

### Example

The following `AssociateBidList` mutation example adds and updates a bid list in the `bidListsToAddOrUpdate` array and removes an unwanted one in the `bidListIdsToRemove` array.

```
mutation {
    adGroupAssociateBidList(
        input: {
            adGroupId: "AD_GROUP_ID_PLACEHOLDER",
            bidListsToAddOrUpdate: [
                {
                    bidListId: "BID_LIST_ID_PLACEHOLDER_01",
                    isDefault: false,
                    isEnabled: true
                }
            ],
            bidListIdsToRemove: ["BID_LIST_ID_PLACEHOLDER_02"]
        }
    ) {
        data {
            name
            associatedBidLists {
                nodes {
                    bidList {
                        id
                    }
                }
            }
        }
        userErrors {
            field
            message
        }
    }
}
```

## Bid list queries

To understand the nuances of bid list ownership and individual bid lines, you can look up bid list details, their associations, and whether they are enabled. The following sections provide examples of using the `bidList` query to look up key bid list details and an ad group's relationship with multiple bid lists.

### Look up bid list details

The following GraphQL query example retrieves key details of a specific bid list, including its ownership, individual bid lines, adjustment type, dimensions, and whether it is used only for Volume control. Each `...on` fragment retrieves the IDs for the corresponding owner type.

```
query GetBidListDetailsExample {
    bidList(id: "BID_LIST_ID_PLACEHOLDER") {
        adjustmentType
        bidLinesCount
        dimensions
        id
        isAvailableForLibraryUse
        name
        owner {
            ...on AdGroup {
                id
            }
            ...on Campaign {
                id
            }
            ...on Advertiser {
                id
            }
            ...on Partner {
                id
            }
        }
        ownerType
        source
        volumeControlOnly
        bidLines {
            domainFragment
            bidAdjustment
            volumeControlPriority
        }
    }
}
```

### Look up bid list associations

The following ad group GraphQL query example retrieves details about an ad group's relationship with multiple bid lists, including ownership, associations, and active bidding status. This is helpful for checking bid line relationship limits and ensuring that specific bid lists are activated for your campaign strategy.

```
query GetBidListAssociationsForAdGroupExample {
    adGroup(id: "AD_GROUP_ID_PLACEHOLDER") {
        id
        name
        ownedBidLists {
            nodes {
                id
            }
        }
        associatedBidLists {
            nodes {
                isEnabled
                bidList {
                    id
                }
            }
        }
        appliedBidLists {
            nodes {
                id
            }
        }
    }
}
```

## Update bid lists

To optimize your ad campaign, you can make adjustments to your bid list using different mutations as described in the following table.

| Mutation | Description |
| --- | --- |
| `bidListSet` | Updates bid list details such as the bid list name, owner, and all its bid lines at once. |
| `bidListUpdate` | Adds and removes bid lines in a bid list. |
| `bidFactorBulkUpdate` | Updates multiple bid lists at once. |

> **NOTE**: You can also update bid lines for an entity by activating or deactivating bid lists inherited from parent entities. To update bid list associations, whether bid lists are defaults, and whether they are enabled, use an `AssociateBidList` mutation. For details, see Associate bid lists.

Here's what you need to know:

- You cannot update its bid list adjustment type.
- The bid list must stay within relationship limits.

### Set a specified bid list

You can use the `bidListSet` mutation to update the following:

- All the bid lines in a bid list with the same specified values.
- The name of the bid list.
- The owner of the bid list.

#### Example

To optimize bid list association and inheritance, you can re-set the ownership of a bid list to a higher-level parent entity. The following `bidListSet` mutation example shows how to update a bid list with its new name and owner. The new owner must be an ancestor of the current owner within the entity hierarchy.

```
mutation {
    bidListSet(input: { id: BID_LIST_ID_PLACEHOLDER, name:"NEW_BID_LIST_NAME_PLACEHOLDER", newOwner: { partnerId: "PARTNER_ID_PLACEHOLDER" } }) {
        data {
            id
            name
            owner {
                __typename
                ... on Partner {
                    id
                    name
                }
                ... on Advertiser {
                    id
                    name
                }
            }
        }
        userErrors {
            message
            field
        }
    }
}
```

### Add and remove bid lines

The `bidListUpdate` mutation allows you to add and remove individual bid lines without requiring you to specify all lines. If there are existing bid lines that have the same dimensional values as the ones you provide, they will be replaced.

#### Example

The following `bidListUpdate` mutation shows how to update a bid list by adding a bid line and removing an existing one for the specified domains. The bid list now targets impressions with a bid adjustment of `1` and a neutral volume control priority.

```
mutation {
    bidListUpdate(
        input: {
            id: "BID_LIST_ID_PLACEHOLDER",
            bidLinesToAdd: [
                {
                domainFragment: "DOMAIN_COM_1_PLACEHOLDER",
                bidAdjustment: 1,
                volumeControlPriority: NEUTRAL
                }
            ],
            bidLinesToRemove: [{domainFragment: "DOMAIN_COM_1_PLACEHOLDER"}]
        }
    ) {
        data {
            id
        }
        userErrors {
            field
            message
        }
    }
}
```

### Bulk edit bid lines

The `bidFactorBulkUpdate` mutation allows you to update multiple bid lists within a single request. It supports the following bid dimensions:

- `HasGeoSegmentId`
- `HasDomainFragmentId`
- `HasLiveEventId`
- `HasLiveEventTypeId`
- `HasRenderingContextId`
- `HasAdFormatId`
- `HasBrowserId`
- `HasDeviceTypeId`
- `HasOsId`
- `HasDeviceModelId`
- `HasCarrierId`
- `HasInternetConnectionTypeId`

#### Update bid factors example

The following `bidFactorBulkUpdate` mutation shows how to update bid factors for an ad group associated with a specified geographic segment. This includes setting the bid adjustment value for optimized lists to 10%.

```
mutation {
    bidFactorBulkUpdate(
        input: {
            dimensions: [HAS_GEO_SEGMENT_ID_PLACEHOLDER]
            bulkBidFactorsToUpdate: [{
                adGroupId: "AD_GROUP_ID_PLACEHOLDER"
                bidFactorsToUpdateOrAdd: [{
                    value: 10
                    bidFactorType: TARGET
                    geoSegmentId: "GEO_SEGMENT_ID_PLACEHOLDER"
                    volumeControlPriority: NEUTRAL
                }]
            }]
        }
    ) {
        data {
            adGroups {
                id
                name
                bidFactors(dimensions: [HAS_GEO_SEGMENT_ID_PLACEHOLDER]){
                    type
                    value
                    dimension{
                        geoSegment{
                            id
                            name
                        }
                    }
                }

            }
        }
        errors {
          __typename
          ... on MutationError {
            field
            message
          }
        }
    }
}
```

#### Remove bid factors example

The following `bidFactorBulkUpdate` mutation shows how to remove bid factors for an ad group associated with a specified geofence segment. For details on how to create a geofence segment, see Geofence targeting.

```
mutation BidFactorBulkUpdate {
  bidFactorBulkUpdate(
    input: {
      bulkBidFactorsToUpdate: {
        bidFactorsToRemove: [{ geoSegmentId: "GEO_SEGMENT_ID_PLACEHOLDER" }]
        adGroupId: "AD_GROUP_ID_PLACEHOLDER"
      }
      dimensions: [HAS_GEO_SEGMENT_ID]
    }
  ) {
    data {
      adGroups {
        id
        name
        bidFactors(dimensions: [HAS_GEO_SEGMENT_ID]) {
          type
          value
          dimension {
            geoSegment {
              id
              name
            }
          }
        }
      }
    }
    errors {
      __typename
      ... on MutationError {
        field
        message
      }
    }
  }
}
```

## Delete a bid list

To permanently remove and disassociate a bid list from all associated partners, advertisers, campaigns, and ad groups, use the `bidListDelete` mutation.

```
mutation {
    bidListDelete(input: { id: "BID_LIST_ID_PLACEHOLDER" }) {
        data {
            wasDeleted
        }
        errors {
            ...on InSchemaError {
                field
                message
            }
        }
    }
}
```

> **TIP**: Since GraphQL delta calls don't track bid list deletions, use REST instead. For details, see the POST /v3/delta/activity/query/adgroup endpoint.

## FAQs

The following is a list of frequently asked questions about creating and managing bid lists in GraphQL.

### I created a bid list for an owner entity, but how do I turn it on?

After creating a bid list, you need to also associate and enable it for the owner or its descendant. This includes setting the `isEnabled` property to `true`.

### How do I update a single bid line in a bid list?

You can use the `bidListUpdate` mutation to add the updated bid line and remove the existing one, as there is no direct way to update a single line. For details, see Update bid lists.

### If I created a bid list for geo targeting, can I target users based on their home location instead of real-time location?

Yes, you can target users based on their home location instead of their real-time location. This enables you to include users who reside in the locations you want to target instead of users who are visiting or just passing through.

To target or block users based on home location, create a bid list and set the `locationContextType` value to `HOME`.

Here's an `$input` variable example snippet for a `bidListCreate` mutation that shows how to configure the bid list to include users based on their home addresses. See also Create bid lists.

```
{
  "input": {
    "dimensionConfig": {
      "geo": {
        "locationContextType": "HOME"
      }
    }
  }
}
```
