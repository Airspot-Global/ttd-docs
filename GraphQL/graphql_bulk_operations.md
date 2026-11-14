# GraphQL API bulk operations

- Source: https://open.thetradedesk.com/advertiser/docsApp/Foundations/resources/doc/GqlBulkOperations
- Retrieved: 2026-11-14
- Category: GraphQL

---

# GraphQL API bulk operations

In today's data-driven world, efficiently managing large datasets is key to making timely, informed decisions. That’s where GraphQL bulk operations come in.

Whether you're retrieving data or making large-scale updates, bulk operations enable you to handle high volumes of information asynchronously and at scale. Instead of iterating through paginated responses or sending multiple mutation calls, you can execute everything in a single request—saving time, reducing overhead, and boosting performance.

For example, bulk queries can improve data retrieval performance by up to 20% compared to standard queries for large datasets. By allowing you to execute multiple operations in a single request, bulk queries streamline your workflow, conserve resources, and deliver results—no matter how big your dataset.

Bulk mutations offer another powerful solution. If you want to modify data in large batches instead of manually iterating calls to a mutation, you can include multiple large input objects for each mutation you want to execute asynchronously.

This guide explains how to use bulk operations with The Trade Desk GraphQL API for the following entities:

- Advertisers
- Campaigns
- Ad Groups

## Bulk operation workflow

Running a bulk operation is a two-step process.

| Step |  | Task | Notes |
| --- | --- | --- | --- |
| **1** | Create a query or mutation. | `createQueryBulk` mutation `createMutationBulk` mutation | - If you have an HTTP server configured to receive POST requests, you can set up an optional callback to trigger upon the job completion. - If you want to reuse a bulk query with different values, you can pass variables. - When the operation is submitted, a job is created. When it's completed, results and errors are merged into one file. - You can have up to 10 active bulk jobs at a time and a maximum of 20 bulk jobs that are queued. |
| **2** | Retrieve results. | `bulkJob` query | - Processing time depends on the complexity of the job. - The output file expires one hour after it's created. |

> **NOTE**: You can currently cancel bulk query jobs at any time, but mutation jobs cannot be canceled.

The following sections provide additional details about each step in the process.

## Create a bulk query

To create a bulk query, use the `createQueryBulk` GraphQL mutation. To reuse a query with different values, see Create a bulk query with variables.

Here's what you need to know about the formatting and other bulk query requirements:

- You can paginate up to four levels deep in your query structure, counting each field that returns a paginated list (`nodes` or `edges`).
- Pagination within lists is not supported. If a list contains more than one item, only the first page of any nested paginated fields will be processed.
- To encapsulate multi-line query strings, use triple quotes (`"""`).
- Avoid using pagination-specific arguments such as `before`, `after`, `first`, `last`, `cursor`, `totalCount`, and `pageInfo`—they are automatically stripped from the query and have no effect on the result.
- Do not use inline fragments such as `...on AdGroup` in the `query` input field. They're not currently supported in bulk queries.
- To find out why a request was rejected, include the `BulkJobQueryValidationError` snippet, with the `queryErrors` field, in the `errors` object of your mutation. When validation fails, the `message` field returns a generic message: "Batch query failed validation. Please check queryErrors." The `queryErrors` field contains the specific errors.
- You can cancel a bulk query job at any time. For details, see Cancel a bulk query job.

The following `createQueryBulk` mutation shows how to use nested pagination to query multiple ad groups across all campaigns for a specific advertiser, including each ad group's ID and archived status. See also Set up an optional callback.

```
mutation {
  createQueryBulk(
    input: {
      query: """
      query GetAdvertiserExample {
          advertiser(id:"ADVERTISER_ID_PLACEHOLDER") {
              campaigns {
                  nodes {
                      id
                      adGroups{
                          nodes{
                              isArchived
                              id
                          }
                      }
                  }
              }
          }
      }
      """
    }
  ) {
    errors {
      ... on MutationError {
        message
        field
      }
      ... on BulkJobQueryValidationError {
        queryErrors
      }
    }
    data {
      id
      status
      createdAt
    }
  }
}
```

When you call the `createQueryBulk` mutation, a job is created to process your query. All paginated and nested data is fully iterated and returned in a single output file. Processing time varies by query complexity.

> **TIP**: Note the job ID—it’s required to check the job status and retrieve the results. For details, see Check job status and retrieve results. Alternatively, you can include the status and results field in the `data` response as shown in the example.

### Cancel a bulk query job

If you want to cancel a bulk query job, use the `cancelBulkJob` mutation and include the ID of the job you want to cancel.

```
mutation {
  cancelBulkJob(input: { jobId: 123 }) {
    data {
      id
    }
  }
}
```

## Create a bulk query with variables

To run the same bulk query with different values, such as for multiple advertisers, you can define the query once and supply the changing values as variables. To do this, declare the variables in the `query` input field and provide their values in the `queryVariables` input field of the `createQueryBulk` mutation. The mutation creates a job that processes your query. To check the job status and retrieve the results, see Check job status and retrieve results.

> **NOTE**: Formatting and other bulk query requirements also apply when you use variables.

Here's what you need to know about using variables in a bulk query:

- Declare each variable and its type in parentheses after the query name, and reference it with the `$` prefix wherever you want to use the value. For example, `query GetAdvertisersExample($advertiserId1: ID!)` declares the `$advertiserId1` variable. For details about variables, see Query anatomy.
- The `queryVariables` field is optional. To use fixed values instead, specify them directly in the `query` input field, as shown in Create a bulk query.
- The `queryVariables` field is a string that contains a JSON object. Each key in the object matches a variable name without the `$` prefix. You can specify the variables directly in the mutation or pass them with the request. In the latter case, pass the variables as an escaped JSON string.
- To find out why a request was rejected, include the `BulkJobQueryValidationError` snippet, with the `queryErrors` field, in the `errors` object of your mutation. When validation fails, the `message` field returns a generic message: "Batch query failed validation. Please check queryErrors." The `queryErrors` field contains the specific errors.

The examples in the following sections use the `$advertiserId1` and `$advertiserId2` variables to query two advertisers in a single job. The `q1` and `q2` aliases distinguish between the two queries. The first query returns the ID and archived status of every ad group across all campaigns for the first advertiser. The second query returns the ID of the second advertiser.

> **NOTE**: Replace the `ADVERTISER_ID_1_PLACEHOLDER` and `ADVERTISER_ID_2_PLACEHOLDER` values in both examples with your own advertiser IDs.

### Specify query variables directly in the mutation

Put the query variables, as a JSON object, between triple quotes (`"""`) in the `queryVariables` field. The following `createQueryBulk` mutation specifies the variables directly:

```
mutation {
  createQueryBulk(
    input: {
      query: """
      query GetAdvertisersExample($advertiserId1: ID!, $advertiserId2: ID!) {
          q1: advertiser(id: $advertiserId1) {
              campaigns {
                  nodes {
                      id
                      adGroups{
                          nodes{
                              isArchived
                              id
                          }
                      }
                  }
              }
          }

          q2: advertiser(id: $advertiserId2) {
              id
          }
      }
      """
      queryVariables: """{ "advertiserId1": "ADVERTISER_ID_1_PLACEHOLDER", "advertiserId2": "ADVERTISER_ID_2_PLACEHOLDER" }"""
    }
  ) {
    errors {
      ... on MutationError {
        message
        field
      }
      ... on BulkJobQueryValidationError {
        queryErrors
      }
    }
    data {
      id
      status
    }
  }
}
```

### Pass query variables with the request

To keep the values separate from the query, declare `$queryVariables` as a GraphQL variable of the `String!` type and assign it to the `queryVariables` input field. This way, you can reuse the same mutation and change only the variables JSON for each request. The following `createQueryBulk` mutation declares and assigns the variable:

```
mutation ($queryVariables: String!) {
  createQueryBulk(
    input: {
      query: """
      query GetAdvertisersExample($advertiserId1: ID!, $advertiserId2: ID!) {
          q1: advertiser(id: $advertiserId1) {
              campaigns {
                  nodes {
                      id
                      adGroups{
                          nodes{
                              isArchived
                              id
                          }
                      }
                  }
              }
          }

          q2: advertiser(id: $advertiserId2) {
              id
          }
      }
      """
      queryVariables: $queryVariables
    }
  ) {
    errors {
      ... on MutationError {
        message
        field
      }
      ... on BulkJobQueryValidationError {
        queryErrors
      }
    }
    data {
      id
      status
    }
  }
}
```

#### Request body example

The `queryVariables` input field is a string, so pass the query variables as an escaped JSON string in the `variables` property of your request body, alongside the mutation in the `query` property:

```
{
  "query": "mutation ($queryVariables: String!) { createQueryBulk(input: { ... }) { ... } }",
  "variables": {
    "queryVariables": "{\"advertiserId1\": \"ADVERTISER_ID_1_PLACEHOLDER\", \"advertiserId2\": \"ADVERTISER_ID_2_PLACEHOLDER\"}"
  }
}
```

For a Python example that passes variables, see Python.

## Create a bulk mutation

Bulk mutations enable you to execute multiple instances of a single GraphQL mutation at the advertiser, campaign, and ad group levels. For example, you can create multiple ad groups at once in a single request and define different values for each one.

> **IMPORTANT**: You cannot cancel a bulk mutation job after it starts.

To create a bulk mutation, use the `createMutationBulk` GraphQL mutation.

Here's what you need to know about the formatting and other bulk mutation requirements:

- You can include only one mutation operation.
- To encapsulate multi-line input strings, use triple quotes (`"""`).
- A bulk mutation must have fewer than 15,000 lexical tokens. This includes all keywords, properties, values, and punctuation marks (`mutation`, `createMutationBulk`, `input`, `{}`, `adGroupId`).
- To execute multiple mutations, use the `mutationVariables` object array with the following guidelines:

  - For each mutation you want to execute, include an `input` object.
  - You can include a maximum of 1000 `input` objects.
  - Pass the `mutationVariables` object array as a variable to avoid exceeding token limits.

The following `createMutationBulk` mutation shows how to create multiple ad groups using the `mutationVariables` GraphQL variable. See also Set up an optional callback.

```
mutation {
  createMutationBulk (
    input: {
      mutation: """
      mutation ($input: AdGroupCreateInput!) {
          adGroupCreate(input: $input) {
              data {
                  id
              }
              userErrors {
                  field
                  message
              }
          }
      }
      """
      mutationVariables: $mutationVariables
    }
  ) {
    errors {
      ... on MutationError {
        message
        field
      }
    }
    data {
      id
      status
      runtimeErrors
      internalErrors
      url
      rawResult
    }
  }
}
```

To include the input values in a GraphQL variable, be sure to include them as a JSON object and escape each string field.

Here's an example of using the `mutationVariables` object array as a GraphQL variable to provide a list of ad groups to create.

```
{
  "mutationVariables": [
    "{ \"input\": { \"campaignId\": \"abc123\", \"name\": \"AdGroup1\", \"channel\": \"TV\", \"funnelLocation\": \"CONVERSION\" } }",
    "{ \"input\": { \"campaignId\": \"def456\", \"name\": \"AdGroup2\", \"description\": \"test\", \"channel\": \"TV\", \"funnelLocation\": \"CONVERSION\" } }",
    "{ \"input\": { \"campaignId\": \"ghi789\", \"name\": \"AdGroup3\", \"channel\": \"TV\", \"funnelLocation\": \"CONVERSION\" } }"
  ]
}
```

When you call the `createMutationBulk` mutation, a job is created to process your mutations.

> **TIP**: Note the job ID—it’s required to check the job status and retrieve the results. For details, see Check job status and retrieve results.

## Set up a callback

If you have an HTTP server configured to receive POST requests, you can opt in to receive a callback upon job completion. To do this, in the `createQueryBulk` or `createMutationBulk` mutation, specify a callback URL and (optionally) custom headers in the `bulkJobCallback` object of your query. For details about the query requirements and structure, see Create a bulk query for mutations, see Create a bulk mutation.

Here's an example of the `bulkJobCallback` object that you would include in the `input` object of the `createQueryBulk` or `createMutationBulk` mutation.

```
bulkJobCallback: {
  callbackUrl: "https://example.com/callback",
  callbackHeaders: [
    {
      key: "HEADER_1_PLACEHOLDER",
      value: "VALUE_1_PLACEHOLDER",
    },
  ],
}
```

Here's a complete example of adding a callback to a bulk query operation.

```
mutation {
  createQueryBulk(
    input: {
      bulkJobCallback: {
        callbackHeaders: [
          { key: "HEADER_1_PLACEHOLDER", value: "VALUE_1_PLACEHOLDER" }
        ]
        callbackUrl: "https://example.com/callback"
      }
      query: """..."""
    }
  ) {
    errors {
      ... on MutationError {
        message
        field
      }
      ... on BulkJobQueryValidationError {
        queryErrors
      }
    }
  }
}
```

When your bulk query job is completed, your server will receive a POST request with the headers specified (if any), and a JSON body. For example:

```
{
    "jobId": 123,
    "status": "Success",
    "completedAtUtc": "2025-04-25T22:02:24.34567"
}
```

## Check job status and retrieve results

After a bulk operation job is created, you can check its status and retrieve the results by running the `bulkJob` query for a given job ID.

Here's what you need to know about bulk operation job processing:

- If the result of your job is small enough, it is returned in the `rawResult` field of the `bulkJob` query. Otherwise, download the result file from the link specified in the `url` field.
- Depending on the outcome, the job is marked with one of the following:

  - `SUCCESS`: The job executed successfully.
  - `PARTIAL_SUCCESS`: Only a portion of the job was successful. The results include a subset of the total expected data.
  - `FAILURE`: No requested data was retrieved and no data was updated or added.

> **IMPORTANT**: The generated JSON file with the query results expires one hour after the time specified in the `completedAt` field.

The following `bulkJob` GraphQL query retrieves the job status information, including the job creation and completion timestamps, completion percentage, current status, the file download URL, and errors if present.

```
query GetBulkQueryResultsExample {
  bulkJob(id: 123) {
    id
    createdAt
    rawResult
    completionPercentage
    completedAt
    status
    url
    runtimeErrors
    ... on BulkMutationJob {
      mutationGqlErrors {
        error
        index
      }
    }
    ... on BulkQueryJob {
      queryGqlErrors
    }
  }
}
```

## FAQs

The following is a list of frequently asked questions about bulk queries.

### Who can access a bulk operation job?

Only the user who submitted the bulk operation job can view its status and results.

### How many bulk jobs can I run at the same time?

You can have up to 10 active bulk jobs at a time and a maximum of 20 jobs that are queued. If you try to start a new bulk job while the limits are already active, you’ll need to wait until one completes before submitting another.

### Where can I find my bulk operation results?

If the result of your job is small enough, it is returned in the `rawResult` field of the `bulkJob` query. Otherwise, download the result file from the link specified in the `url` field. For details, see Check job status and retrieve results.

### How long can I access the results of a bulk operation job?

You have one hour to access the results after the job is finished.

### What happens if I missed the one-hour window to retrieve my bulk operation results?

You have to run the appropriate mutation for your bulk operation job again.

### What are lexical tokens?

Lexical tokens include all keywords, properties, values, and punctuation marks. For example, `mutation`, `createMutationBulk`, `input`, `{}`, `adGroupId`. You cannot include more than 15,000 lexical tokens in a bulk mutation operation.

### Which entities can I use bulk operations to for?

Bulk operations are available only at the advertiser, campaign, and ad group level.
