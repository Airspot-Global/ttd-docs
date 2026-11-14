# GraphQL API queries

- Source: https://open.thetradedesk.com/advertiser/docsApp/Foundations/resources/doc/GqlApiQueries
- Retrieved: 2026-11-14
- Category: GraphQL

---

# GraphQL API queries

The GraphQL API enables you to construct and run queries to retrieve only the information you need. In contrast to our REST API, which provides a fixed structure of information for a single entity, GraphQL can customize queries to return specific fields across multiple entities. This empowers you to precisely define the request, reduce complexity, and response times, by limiting the scope of information.

> **NOTE**: To edit information, use mutations instead of queries.

Here's what you need to know about GraphQL queries and their best practices:

- Even though it's optional, it is always a best practice to name your queries. This makes it easier to distinguish between multiple queries.
- You can retrieve individual fields (ID, name, description, and so on) or lists (flights, ad groups, and so on).
- You can filter and refine your results.
- For lists, be sure to follow best practices for cursor-based pagination to limit results per query.
- Do not enclose enum values in quotation marks unless you're passing them as variables in a JSON object. For example, `funnelLocation: CONSIDERATION`.
- Avoid creating overly complex calls, such as those containing many levels of nested fields. For details, see System errors.
- Rate limits apply to GraphQL calls.

> **TIP**: To retrieve your schema, run an introspection query. For details, see Making GraphQL API calls.

The following sections explain the anatomy of a query and best practices, using Platform API examples. These concepts apply to all API products at The Trade Desk that use GraphQL.

## Query anatomy

A GraphQL query consists of top-level fields and nested fields, which provides a structured approach to constructing your query and retrieving specific information from the platform.

> **IMPORTANT**: This structure must map to values in the schema and gets more complex as you delve deeper into nested fields, or query for a wide arrange of items.

Here's an example of a query that passes the ad group ID to retrieve the ID, name, and details of an ad group. It starts at the ad group level and nests down to retrieve detailed information such as spend priority and total budget, with an alias used to customize the response.

```
query GetAdGroupDetailsExample ($adGroupId: ID!) {
  adGroup(id: $adGroupId) {
    id
    name
    budget {
      spendPriority
      TotalBudget: total
    }
  }
}
```

The following table details the components of the query example.

| Component | Required? | Description |
| --- | --- | --- |
| `query` | Required | The type of GraphQL operation. Possible values include `query` and `mutation`. |
| `GetAdGroupDetailsExample` | Optional | The custom name of the query that you create. **IMPORTANT**: Do not include spaces in the name. |
| `$adGroupId: ID!` | Optional | A variable. Here's what you need to know about variables: - You can only use variables in arguments. - You can specify which variables are required. - You must specify the variable data type (float, string, ID, and so on). |
| `adGroup(id: $adGroupId)` | Required | A top-level field that specifies the ad group information you want to retrieve. Here's what you need to know about top-level fields: - If needed, you can include multiple top-level fields in your query. - Most top-level fields require arguments by which to filter the results. For example, an `adGroup` top-level field requires an `id` argument to return only the results related to a single ad group. |
| `id`, `name`, `budget`, `total` | Required | The fields (from the schema) to be returned for the ad group specified in the top-level field. **IMPORTANT**: Avoid creating too many layers of nested fields. For details, see System errors. |
| `TotalBudget` | Optional | An alias that you can use to rename the `total` field to make it more specific in the response. |

## Filter and refine results

To filter and narrow your search by specific criteria, include the arguments that correspond to the fields by which you want to filter.

> **IMPORTANT:** Not all queries have arguments that can narrow your search. Be sure to check your schema to view which arguments are available for the fields you want to include.

Here's an example `adGroups` query that retrieves ad groups with either the awareness or consideration objectives for funnel location.

```
query GetAdGroupFunnelLocationExample {
  adGroups(
    where: {
      and: [
        {
          channel: { in: [TV, DISPLAY] }
          or: [
            { funnelLocation: { eq: AWARENESS } }
            { funnelLocation: { eq: CONSIDERATION } }
          ]
        }
      ]
    }
  ) {
    nodes {
      id
      name
      channel
      funnelLocation
    }
  }
}
```

> **NOTE**: This filter is for demonstration purposes and is not optimized. If the response takes a long time to return, consider pagination.
