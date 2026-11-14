# GQL API response pagination

- Source: https://open.thetradedesk.com/advertiser/docsApp/Foundations/resources/doc/GqlApiResponses
- Retrieved: 2026-11-14
- Category: GraphQL

---

# GQL API response pagination

GraphQL supports cursor-based pagination to select a subset of data per response to reduce complexity and runtime when returning lists. It relies on cursors, which mark a location in the data and provide fine-tuned control over how much data is returned. Unlike traditional pagination, GraphQL doesn't use page numbers to navigate lists. Paginated responses are returned after you perform a query or mutation, and apply to all GraphQL Queries, and GraphQL Mutations with a `data` object.

Here's what you need to know about responses pagination in GraphQL:

- Plan for large responses to be paginated to preserve complexity.
- For large quantities of data, ensure data completeness by adding the `pageInfo` object to your request.
- To navigate paginated data, include the cursor in your request.

The following sections explain the anatomy of a successful reponse and how to use cursor pagination. If your response is unsuccessful, see GraphQL API errors and complexity limits.

## Paginate lists

To paginate the data returned, include the `pageInfo` object, which applies to any request that returns a list of nodes. If you plan on iterating through a large list of items, see Cursor Navigation.

The following example `adGroups` query shows how to get the channel, ID, and name for a list of ad groups.

```
query GetAdGroupChannelsExample {
  adGroups {
    edges {
      cursor
      node {
        id
        name
        channel
      }
    }
    totalCount
    pageInfo {
      endCursor
      hasNextPage
      hasPreviousPage
      startCursor
    }
  }
}
```

The following table explains the fields used for pagination.

| Field | Required? | Description |
| --- | --- | --- |
| `edges` | Recommended | A field that contains the node and cursor used to traverse a list. **IMPORTANT**: If your query doesn't use a list, avoid using this property. |
| `cursor` | Required | A unique ID that marks the current position in the paginated results. |
| `node` | Required | A field that contains the items returned on the page, such as the details of the ad group. |
| `totalCount` | Recommended | The number of items that can be returned. In this case, the total number of available ad groups. |
| `pageInfo` | Required | An object containing the metadata on the pagination state, such as cursor IDs and page information. |
| `endCursor` | Recommended | A cursor ID that marks the end of the current page. |
| `hasNextPage` | Optional | If the value is `true`, indicates that the end cursor ID has items after it. Otherwise, there's no next page. |
| `hasPreviousPage` | Optional | If the value is `true`, indicates that the start cursor ID has items before it. Otherwise, there's no previous page. |
| `startCursor` | Optional | A cursor ID that marks the start of the current page. |

A successful response returns the paginated data and requested cursors. These cursor IDs mark a location to start processing data from.

> **NOTE**: By default, responses always return the next 10 items starting from the cursor.

```
{
  "data": {
    "adGroups": {
      "edges": [
        {
          "cursor": "CURSOR_ADGROUPS_PLACEHOLDER_01",
          "node": {
            "id": "ADGROUP_PLACEHOLDER_01",
            "name": "Retargeting - CTV",
            "channel": "CTV"
          }
        },
        {
          "cursor": "CURSOR_ADGROUPS_PLACEHOLDER_02",
          "node": {
            "id": "ADGROUP_PLACEHOLDER_02",
            "name": "Prospecting - Display",
            "channel": "DISPLAY"
          }
        },
        {
          "cursor": "CURSOR_ADGROUPS_PLACEHOLDER_03",
          "node": {
            "id": "ADGROUP_PLACEHOLDER_03",
            "name": "Mobile App Engagement",
            "channel": "MOBILE"
          }
        },
        {
          "cursor": "CURSOR_ADGROUPS_PLACEHOLDER_04",
          "node": {
            "id": "ADGROUP_PLACEHOLDER_04",
            "name": "DOOH - Times Square Screens",
            "channel": "DOOH"
          }
        },
        {
          "cursor": "CURSOR_ADGROUPS_PLACEHOLDER_05",
          "node": {
            "id": "ADGROUP_PLACEHOLDER_05",
            "name": "DOOH - Transit Stations",
            "channel": "DOOH"
          }
        },
        {
          "cursor": "CURSOR_ADGROUPS_PLACEHOLDER_06",
          "node": {
            "id": "ADGROUP_PLACEHOLDER_06",
            "name": "In-Stream Video - Pre-roll",
            "channel": "VIDEO"
          }
        },
        {
          "cursor": "CURSOR_ADGROUPS_PLACEHOLDER_07",
          "node": {
            "id": "ADGROUP_PLACEHOLDER_07",
            "name": "Out-Stream Video Units",
            "channel": "VIDEO"
          }
        },
        {
          "cursor": "CURSOR_ADGROUPS_PLACEHOLDER_08",
          "node": {
            "id": "ADGROUP_PLACEHOLDER_08",
            "name": "Streaming Audio - Music",
            "channel": "AUDIO"
          }
        },
        {
          "cursor": "CURSOR_ADGROUPS_PLACEHOLDER_09",
          "node": {
            "id": "ADGROUP_PLACEHOLDER_09",
            "name": "Podcast Sponsorship",
            "channel": "AUDIO"
          }
        },
        {
          "cursor": "CURSOR_ADGROUPS_PLACEHOLDER_10",
          "node": {
            "id": "ADGROUP_PLACEHOLDER_10",
            "name": "High-Impact Mobile Interstitial",
            "channel": "MOBILE"
          }
        }
      ],
      "totalCount": 42,
      "pageInfo": {
        "startCursor": "CURSOR_ADGROUPS_PLACEHOLDER_01",
        "endCursor": "CURSOR_ADGROUPS_PLACEHOLDER_10",
        "hasNextPage": true,
        "hasPreviousPage": false
      }
    }
  }
}
```

The resulting response contains `"hasNextPage": true` and a total count of 42 items which shows that there are more ad groups that aren't included in this response.

## Cursor navigation

To get items missing from a response, use the cursor ID from the `endCursor` field to continue from the response. Update your original query with the `after` field using the new cursor position. For a long list of items, you can increase the number of results returned using either the `first` or `last` filters.

Here's an example `adgroups` query that combines the end cursor of the response with the `first` filter to return the remaining 32 items.

```
query GetNextAdGroupChannelsExample {
  adGroups(first: 32, after: CURSOR_ADGROUPS_PLACEHOLDER_10) {
    edges {
      cursor
      node {
        id
        name
        channel
      }
    }
    totalCount
    pageInfo {
      endCursor
      hasNextPage
      hasPreviousPage
      startCursor
    }
  }
}
```

### Backward navigation

Cursors support bi-directional navigation, which allows users to read data before or after the current cursor position. To fetch previous items from the cursor, pass the corresponding cursor ID as the `before` value, and set the query to use the `last` filter with the number of items to return. Here's an example that retrieves the last 10 items from the cursor location.

> **NOTE**: This also changes the order of the list, since the cursor position is now reversed, reading from the end to the start.

The following example `adGroups` query shows retrieves the channel, ID, and name for a list of ad groups in reverse order.

```
query GetPreviousAdGroupChannelsExample {
  advertiser(id: "ADVERTISER_ID_PLACEHOLDER") {
    id
    name
    campaigns(last: 10, before: CURSOR_ADGROUPS_PLACEHOLDER_10) {
      nodes {
        id
        name
        adGroups {
          nodes {
            id
            name
          }
          pageInfo {
            hasNextPage
            endCursor
          }
        }
      }
      pageInfo {
        endCursor
        hasNextPage
        hasPreviousPage
        startCursor
      }
    }
  }
}
```
