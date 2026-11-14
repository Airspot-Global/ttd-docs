# Contextual category configuration

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/ContextualEntities
- Retrieved: 2026-11-14
- Category: Guides

---

# Contextual category configuration

Whether you're working with third-party or The Trade Desk contextual categories, to use them in your campaigns, you must first organize them into contextual groups and entities, then assign those entities to your ad groups. This page covers the relevant terms, key component relationships, and how to build and manage your contextual targeting configuration.

The following table defines the key terms.

| Term | Definition |
| --- | --- |
| Tactic | A tactic is a classification that defines how impressions are evaluated against categories before a bid is placed. **IMPORTANT**: Contextual entities, groups, and categories must share the same tactic. |
| Contextual entity group | A group of contextual categories that determines which categories you either target or block. Groups can be shared across multiple entities, but sharing must be explicitly enabled. |
| Contextual entity | A container that holds groups of categories and defines an overall contextual targeting strategy. |

For brevity, the documentation uses "entity" and "group" as shorthand for "contextual entity" and "contextual entity group" throughout.

## Tactics

A tactic defines what the platform measures impressions against before placing a bid. When you create an entity or group, you set a tactic to match your selected categories.

> **IMPORTANT**: Entities, groups, and categories must all share the same tactic.

The following table lists the available tactics and the type of content the platform measures each impression against before bidding.

| Tactic Enum Value | Types of Content |
| --- | --- |
| `CATEGORY` | General topics and subjects for relevance |
| `BRAND_SAFETY` | Safe or unsafe for your brand to appear next to |
| `ATTENTION` | Likely to drive user attention |
| `SUSTAINABILITY` | Environmental and sustainability topics |
| `NEWS_QUALITY` | Content filtered by the quality of news sources |

Here's what you need to know about tactics:

- Every contextual category has a tactic pre-assigned by its provider. TTD contextual categories use only the `CATEGORY` tactic.
- You cannot change the tactic or group type of an entity and group. To use a different tactic, archive the existing entity or group and create a new one.
- You can assign the same entity to multiple ad groups. An ad group cannot have two entities with the same tactic.

> **IMPORTANT**: Only the `CATEGORY` tactic allows categories from different providers in the same group and entity. For all other tactics, categories must share the same provider.

The following diagram illustrates the full assignment hierarchy and how tactics are organized at each level, from individual categories and entity composition to ad group assignment. Color indicates tactic: teal for Brand Safety, orange for Attention. All items within an entity share the same tactic; no mixing is allowed. A single entity can hold multiple groups of different types.

## Create and assign contextual entities and category groups

The following table lists the tasks for creating entities and groups and assigning them to ad groups.

| Step | Task | Operation | Notes |
| --- | --- | --- | --- |
| **1** | Decide on a tactic. | N/A | Your tactic determines which categories you can include in a single entity configuration. For details, see Tactics. |
| **2** | Look up and filter contextual categories by the chosen tactic. | `advertiser` query | Note the IDs of the categories you want to use for step 3. |
| **3** | Create a contextual entity. | `contextualEntityCreate` mutation | - This single mutation creates the entity and its groups of categories. - Groups are not sharable by default. To reuse a group across multiple entities, set the `isSharable` field to `true`. - After you create your contextual entity, you can always create additional groups and assign them to your existing entities. For details, see Manage contextual entities and groups. |
| **4** | Assign the entity to an ad group. | `adGroupAssociateContextualEntity` mutation | An ad group can hold one entity per tactic. |

### Look up contextual categories

To create a contextual entity, you must first select a tactic and retrieve available contextual categories. To do this, use the `advertiser` query and include your advertiser ID and filter by the tactic you want to use.

Here's an example `advertiser` query that retrieves available contextual categories for the `CATEGORY` tactic.

```
query GetContextualCategoriesExample {
  advertiser(id: "ADVERTISER_ID_PLACEHOLDER") {
    preBidContextualCategories(tactic: CATEGORY) {
      nodes {
        category {
          id
          tactic
          providerId
          brand {
            id
            name
          }
        }
      }
    }
  }
}
```

A successful response returns a list of contextual categories. Note the `id` and `tactic` values of each category you want to use when you create your contextual entity.

### Create a contextual entity

To create a contextual entity, use the `contextualEntityCreate` mutation. You can create new groups, attach existing ones, or both in the same call by doing the following:

- To attach existing groups, include their IDs in the `groups` field.
- To create new groups, include an object for each group in the `contextualEntityGroups` array. For each object, include the `tactic` field, a `groupType` value of `TARGETING` or `BLOCKING`, and the `categories` array with the list of category IDs you want to add to the group.
- You can include both targeting and blocking groups in the same entity.
- To make a new group reusable across entities, set the `isSharable` field to `true`. Without this value, you cannot assign the group to another entity.

> **IMPORTANT**: Your entity, groups, and all assigned categories must share the same tactic. Unless you are using the `CATEGORY` tactic, all categories within a group must also share the same provider.

Here's an example `contextualEntityCreate` mutation that creates a contextual entity and one group with the `CATEGORY` tactic, assigns two categories to the group, and attaches an existing group using the `groups` field.

```
mutation {
  contextualEntityCreate(
    input: {
      advertiserId: "ADVERTISER_ID_PLACEHOLDER"
      contextualEntities: [
        {
          name: "ENTITY_NAME_PLACEHOLDER"
          tactic: CATEGORY
          contextualEntityGroups: [
            {
              contextualEntityGroupToCreate: {
                name: "GROUP_NAME_PLACEHOLDER"
                groupType: TARGETING
                tactic: CATEGORY
                categories: [
                  { categoryId: "CATEGORY_A_ID_PLACEHOLDER" }
                  { categoryId: "CATEGORY_B_ID_PLACEHOLDER" }
                ]
                isSharable: true
              }
            }
          ]
          groups: [{ groupId: "EXISTING_GROUP_ID_PLACEHOLDER" }]
        }
      ]
    }
  ) {
    data {
      contextualEntities {
        id
        name
        tactic
      }
    }
    errors {
      ... on MutationError {
        field
        message
      }
    }
  }
}
```

A successful response returns the contextual entity ID in the `data.id` field. You need this ID to assign the entity to an ad group.

### Assign entities to ad groups

To assign one or more contextual entities to an ad group, use the `adGroupAssociateContextualEntity` mutation and include the `adGroupId` value and, in the `contextualEntityIdsToAdd` object array, the IDs of each entity you want to assign.

> **NOTE**: You can assign only one entity per tactic per ad group. To include multiple tactics, assign a separate entity for each.

Here's an example `adGroupAssociateContextualEntity` mutation that assigns two contextual entities to an ad group.

```
mutation {
  adGroupAssociateContextualEntity(
    input: {
      adGroupId: "AD_GROUP_ID_PLACEHOLDER"
      contextualEntityIdsToAdd: [
        "CONTEXTUAL_ENTITY_A_ID_PLACEHOLDER"
        "CONTEXTUAL_ENTITY_B_ID_PLACEHOLDER"
      ]
    }
  ) {
    errors {
      ... on MutationError {
        message
        field
      }
    }
  }
}
```

## Manage contextual entities and groups

The following table lists all tasks for managing your contextual targeting configurations.

> **IMPORTANT**: You cannot change the tactic or group type of entities and groups.

| Task | Operation | Notes |
| --- | --- | --- |
| Migrate existing contextual bid lists to entities. | `contextualEntityMigrate` mutation | Use this if you currently apply contextual categories to ad groups via bid lists and want to switch to the entities workflow. |
| Look up contextual entities. | `advertiser` query | Filter by tactic to narrow results. |
| Look up contextual groups. | `advertiser` query | None. |
| Create additional contextual entity groups. | `contextualEntityGroupCreate` mutation | None. |
| Update an entity. | `contextualEntityUpdate` mutation | Use this to create, add, or remove groups from an entity. |
| Update a group. | `contextualEntityGroupUpdate` mutation | Use this to add or remove categories from a group. |
| Remove an entity from an ad group. | `adGroupAssociateContextualEntity` mutation | This is required before you can archive an entity. |
| Archive a contextual entity. | `contextualEntityArchive` mutation | Before you archive an entity, you must remove it from all assigned ad groups. |
| Archive a contextual entity group. | `contextualEntityGroupArchive` mutation | Before you archive a group, you must remove it from all assigned entities and remove all categories from it. |

### Migrate bid lists to contextual entities

If you currently apply contextual categories to ad groups via bid lists, you can migrate your existing configuration to the entities workflow using the `contextualEntityMigrate` mutation. The mutation converts all contextual bid list lines in a campaign into contextual entities and groups, and automatically assigns them to the ad groups that previously held the bid list configurations.

Here's what you need to know:

- You migrate one campaign at a time by specifying its campaign ID.
- The mutation creates entities and groups that mirror your existing bid list structure, preserving tactic and category assignments.
- Migrated entities are automatically assigned to the relevant ad groups. No separate assignment step is required.

Here's an example `contextualEntityMigrate` mutation that migrates all contextual bid lists in a campaign.

```
mutation {
  contextualEntityMigrate(input: { campaignId: "CAMPAIGN_ID_PLACEHOLDER" }) {
    data {
      contextualEntities {
        id
        name
        tactic
        contextualEntityGroupMappings {
          nodes {
            groups {
              id
              name
              groupType
              tactic
              contextualEntityGroupCategories {
                nodes {
                  category {
                    id
                    name
                    brand {
                      id
                      name
                    }
                  }
                }
              }
            }
          }
        }
        adGroupContextualEntities {
          nodes {
            adGroup {
              id
              name
            }
          }
        }
      }
    }
    errors {
      ... on MutationError {
        field
        message
      }
    }
  }
}
```

A successful response returns the created entities with their assigned groups, categories, and the ad groups they were automatically associated with.

### Look up contextual entities

To retrieve contextual entities for an advertiser, use the `advertiser` query and include the `tactic` filter to narrow results to a specific tactic.

Here's an example `advertiser` query that retrieves contextual entities and their assigned groups that have the `ATTENTION` tactic.

```
query GetEntitiesAndGroupsExample {
  advertiser(id: "ADVERTISER_ID_PLACEHOLDER") {
    contextualEntities(tactic: ATTENTION) {
      nodes {
        id
        name
        tactic
        contextualEntityGroupMappings {
          nodes {
            groups {
              id
              isSharable
              name
              tactic
              groupType
              description
            }
          }
        }
      }
    }
  }
}
```

A successful response returns a list of contextual entities and their assigned groups.

### Look up contextual entity groups

To retrieve contextual entity groups for an advertiser, use the `advertiser` query and include your advertiser ID.

Here's an example `advertiser` query that retrieves contextual entity groups and their assigned categories.

```
query GetContextualGroupsExample {
  advertiser(id: "ADVERTISER_ID_PLACEHOLDER") {
    contextualEntityGroups {
      nodes {
        id
        name
        isSharable
        tactic
        contextualEntityGroupCategories {
          nodes {
            category {
              id
              name
              providerId
              brand {
                id
                name
              }
            }
          }
        }
      }
    }
  }
}
```

A successful response returns a list of contextual entity groups and their assigned categories.

### Create contextual entity groups

To create a standalone reusable group, use the `contextualEntityGroupCreate` mutation and include the `tactic` field and set the `groupType` field to either `TARGETING` or `BLOCKING`.

Here's an example `contextualEntityGroupCreate` mutation that creates a standalone reusable contextual entity group.

```
mutation {
  contextualEntityGroupCreate(
    input: {
      advertiserId: "ADVERTISER_ID_PLACEHOLDER"
      contextualEntityGroups: [
        {
          name: "GROUP_NAME_PLACEHOLDER"
          categories: [{ categoryId: "CATEGORY_ID_PLACEHOLDER" }]
          description: "GROUP_DESCRIPTION_PLACEHOLDER"
          groupType: TARGETING
          tactic: ATTENTION
        }
      ]
    }
  ) {
    data {
      contextualEntityGroups {
        id
        name
        description
        groupType
        tactic
      }
    }
    errors {
      ... on MutationError {
        field
        message
      }
    }
  }
}
```

A successful response returns the contextual entity group ID in the `data.id` field. You can use this ID to add categories to the group or assign the group to an entity.

### Update contextual entities

To update one or more contextual entities, use the `contextualEntityUpdate` mutation and in the `contextualEntitiesToUpdate` array, include each entity you want to update as an object. Here's what you need to know:

- To create additional groups for the entity, use the `contextualEntities` field. Groups created this way are automatically assigned to the entity.
- To add group assignments, include the group IDs in the `groupsToAddOrUpdate` field.
- To remove groups, use the `groupsToRemove` field and specify the IDs of the groups you want to remove.
- To add group assignments, include the group IDs in the `groupsToAddOrUpdate` field. You can add only groups with the `isSharable` field set to `true`. To enable sharing on an existing group, see Update contextual entity groups.

Here's an example `contextualEntityUpdate` mutation that updates a contextual entity's name and adds a group assignment.

```
mutation {
  contextualEntityUpdate(
    input: {
      advertiserId: "ADVERTISER_ID_PLACEHOLDER"
      contextualEntities: [
        {
          id: "CONTEXTUAL_ENTITY_ID_PLACEHOLDER"
          name: "UPDATED_ENTITY_NAME_PLACEHOLDER"
          groupsToCreate: [
            {
              contextualEntityGroupToCreate: {
                name: "GROUP_NAME_PLACEHOLDER"
                groupType: TARGETING
                tactic: CATEGORY
                categories: [{ categoryId: "CATEGORY_ID_PLACEHOLDER" }]
              }
            }
          ]
          groupsToAddOrUpdate: [{ groupId: "GROUP_ID_PLACEHOLDER" }]
          groupsToRemove: ["GROUP_ID_PLACEHOLDER"]
        }
      ]
    }
  ) {
    data {
      contextualEntities {
        id
        name
      }
    }
    errors {
      ... on MutationError {
        message
        field
      }
    }
  }
}
```

A successful response returns the updated contextual entity with its ID and name.

### Update contextual entity groups

To update one or more contextual entity groups, use the `contextualEntityGroupUpdate` mutation and in the `contextualEntityGroups` array, include each group you want to update as an object.

> **TIP**: To assign additional categories, include the list of category IDs you want to assign in the `categoriesToAddOrUpdate` field of each group.

Here's an example `contextualEntityGroupUpdate` mutation that assigns two categories to a group while removing another category.

```
mutation {
  contextualEntityGroupUpdate(
    input: {
      advertiserId: "ADVERTISER_ID_PLACEHOLDER"
      contextualEntityGroups: [
        {
          id: "GROUP_ID_PLACEHOLDER"
          categoriesToAddOrUpdate: [
            { categoryId: "CATEGORY_A_ID_PLACEHOLDER" }
            { categoryId: "CATEGORY_B_ID_PLACEHOLDER" }
          ]
          categoriesToRemove: ["CATEGORY_ID_TO_REMOVE_PLACEHOLDER"]
          sharability: MARK_SHARABLE
        }
      ]
    }
  ) {
    data {
      contextualEntityGroups {
        id
        name
        description
        tactic
      }
    }
    errors {
      ... on MutationError {
        field
        message
      }
    }
  }
}
```

A successful response returns the updated contextual entity group with its ID, name, and tactic.

### Remove an entity from an ad group

To remove one or more contextual entities from an ad group, use the `adGroupAssociateContextualEntity` mutation and include the `adGroupId` value and the entity IDs in the `contextualEntityIdsToRemove` array.

> **NOTE**: Removing an entity from an ad group does not archive it. The entity remains available to assign to other ad groups.

Here's an example `adGroupAssociateContextualEntity` mutation that removes two contextual entities from an ad group.

```
mutation {
  adGroupAssociateContextualEntity(
    input: {
      adGroupId: "AD_GROUP_ID_PLACEHOLDER"
      contextualEntityIdsToRemove: [
        "CONTEXTUAL_ENTITY_A_ID_PLACEHOLDER"
        "CONTEXTUAL_ENTITY_B_ID_PLACEHOLDER"
      ]
    }
  ) {
    errors {
      ... on MutationError {
        message
        field
      }
    }
  }
}
```

A successful response returns no errors, confirming the entities were removed from the ad group.

### Archive a contextual entity

> **IMPORTANT**: You must remove the entity from all ad groups before you can archive it. Use `adGroupAssociateContextualEntity` with `contextualEntityIdsToRemove` to disassociate the entity first.

To archive a contextual entity, use the `contextualEntityArchive` mutation and include your advertiser ID and the IDs of the entities you want to archive.

Here's an example `contextualEntityArchive` mutation that archives a contextual entity.

```
mutation {
  contextualEntityArchive(
    input: {
      advertiserId: "ADVERTISER_ID_PLACEHOLDER"
      ids: ["CONTEXTUAL_ENTITY_ID_PLACEHOLDER"]
    }
  ) {
    data
    errors {
      ... on MutationError {
        message
        field
      }
    }
  }
}
```

A successful response returns a `data` value confirming the contextual entity was archived.

### Archive a contextual entity group

To archive a contextual entity group, use the `contextualEntityGroupArchive` mutation and include your advertiser ID and the IDs of the groups you want to archive.

Here's an example `contextualEntityGroupArchive` mutation that archives a contextual entity group.

```
mutation {
  contextualEntityGroupArchive(
    input: {
      advertiserId: "ADVERTISER_ID_PLACEHOLDER"
      ids: ["CONTEXTUAL_ENTITY_GROUP_ID_PLACEHOLDER"]
    }
  ) {
    data
    errors {
      ... on MutationError {
        message
        field
      }
    }
  }
}
```

A successful response returns a `data` value confirming the contextual entity group was archived.

## FAQs

The following are frequently asked questions about contextual entities and groups.

### Can I change the tactic on a contextual entity after I create it?

No, you cannot change the tactic after creation. If you want to update a tactic, you must archive the existing entity and create a new one with the correct tactic. For details, see Archive a contextual entity.

### Can I assign more than one contextual entity to the same ad group?

Yes, you can assign multiple contextual entities to the same ad group, but each must have a different tactic. You cannot assign two entities with the same tactic to the same ad group.

### Can I combine categories from different data providers in the same group?

Yes, but only if the entity and groups use the `CATEGORY` tactic. For all other tactics, categories within a group must share the same provider.

### What do I need to do before archiving a contextual entity?

You must remove the entity from all ad groups before you can archive it. Use `adGroupAssociateContextualEntity` with `contextualEntityIdsToRemove` to disassociate the entity first. For details, see Archive a contextual entity.

### Can I assign a contextual entity directly to a campaign?

No, you can assign contextual entities only to ad groups.

### Can I reuse a contextual entity group across multiple entities?

Yes. By default, groups are not sharable. To reuse a group across multiple entities, set the `isSharable` field to `true` either when creating the group or afterward by updating it with the `sharability: MARK_SHARABLE` setting in the `contextualEntityGroupUpdate` mutation. You can then assign the group to additional entities using the `groupsToAddOrUpdate` field in the `contextualEntityUpdate` mutation.
