# Update ad groups

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/AdGroupUpdate
- Retrieved: 2026-11-14
- Category: Guides

---

# Update ad groups

This guide explains how to update, enable or disable, and archive ad groups. Updating is one step in a larger process; for the full sequence from creation through budget allocation, see Ad group creation workflows.

> **TIP**: If you want to update multiple ad groups at once, use bulk operations in GraphQL.

## GraphQL API

Here is an example of the `adGroupUpdate` mutation you can use to update an individual ad group. It sets our curated Sellers and Publishers 500+ list as the market type for the ad group, with awareness as the funnel location.

```
mutation {
    adGroupUpdate(
        input: {
            marketType: MARKETPLACE
            Id: "abc1234"
            funnelLocation: AWARENESS
        }
    ) {
        data {
            baseBidCPMInAdvertiserCurrency
            budgetInAdvertiserCurrency
            campaignStackRank
            channel
            dealsPresent
            description
            id
            isPrivateMarket
            isTemplate
            marketType
            maxBidCPMInAdvertiserCurrency
            name
        }
        userErrors {
            field
            message
        }
    }
}
```

### Manage creatives in an ad group

You can associate (assign) and disassociate multiple creatives from an ad group at once. Here is an example of the `adGroupAssociateCreative` mutation that adds two creatives, removes a creative, and retrieves the first 100 creatives associated with the ad group:

```
mutation {
    adGroupAssociateCreative(input: {adGroupId: "AD_GROUP_ID_PLACEHOLDER", creativeIdsToAdd: ["CREATIVE_ID_PLACEHOLDER_1", "CREATIVE_ID_PLACEHOLDER_2"], creativeIdsToRemove: ["CREATIVE_ID_PLACEHOLDER_3"]}) {
        data {
            creatives(first:100) {
                nodes {
                    id
                }
            }
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

## REST API

Depending on your needs and preferences, you can update a single ad group using either of the following APIs:

| Task | Endpoint | Notes |
| --- | --- | --- |
| Update the details of a specific ad group. | PUT /v3/adgroup | When updating ad groups with list objects, such as `AssociatedBidLists` and `CreativeIds`, each list is replaced with the new content provided. **IMPORTANT**: To avoid overwriting any lists, retrieve the current state of these objects using the GET /v3/adgroup/{adGroupId} endpoint and include the entire list, including changes, in the PUT request. |
| Enable or disable a specific ad group. | PUT /v3/adgroup/status | To check the current ad group status, use the GET /v3/adgroup/status/{adGroupId} endpoint. |

## Archive ad groups

> **IMPORTANT**: An ad group that is archived cannot be restored.

To archive one or more ad groups at once, use the `adGroupsArchive` mutation. The following example archives two ad groups and returns a list of their IDs.

```
mutation {
    adGroupsArchive(input: { ids: ["AD_GROUP_ID_PLACEHOLDER_1", "AD_GROUP_ID_PLACEHOLDER_2"] }) {
        data
        errors {
            ... on InSchemaError {
                field
                message
            }
        }
    }
}
```
