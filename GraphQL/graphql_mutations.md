# GraphQL API mutations

- Source: https://open.thetradedesk.com/advertiser/docsApp/Foundations/resources/doc/GqlApiMutations
- Retrieved: 2026-11-14
- Category: GraphQL

---

# GraphQL API mutations

The GraphQL API enables you to construct and run mutations to create and update values in the schema. In contrast to our REST API, which provides a fixed structure of information for a single entity, GraphQL offers more customization and batch requests. GraphQL mutations function similarly to POST, PUT, and DELETE requests. To access read-only information, use queries.

Here's what you need to know about GraphQL mutations:

- You can use only mutations that your account has access to.
- You can create and edit fields based on the mutation schema.
- Most mutation names follow the format of _entityNameOperation_. For example, to clone campaigns, the mutation is `campaignClonesCreate`.
- Don't enclose enumeration values in quotation marks unless you're passing them as variables in a JSON object. For example, `funnelLocation: CONVERSION`.

> **IMPORTANT**: Each mutation has a set complexity cost. If your mutation exceeds the complexity limit set by GraphQL, the execution is cancelled.

The following sections use Platform API examples to illustrate GraphQL mutation concepts and conventions. These concepts apply to all API products at The Trade Desk that use GraphQL.

## Mutation anatomy

In our GraphQL API, a mutation is made up of three core components, a mutation name, data object, and mutation errors. Each object can consist of top-level fields and nested fields to provide additional information to the mutation. Each core component formats what the request is and what information to return. The valid fields for each object are defined in the schema.

Here's an example of a mutation to create a new ad group in GraphQL. It returns the data of the newly created ad group. For details on troubleshooting mutations, see Mutation errors.

```
mutation {
  adGroupCreate(
    input: {
      campaignId: "CAMPAIGN_ID_PLACEHOLDER"
      name: "AD_GROUP_NAME_PLACEHOLDER"
      channel: DISPLAY
      funnelLocation: CONVERSION
    }
  ) {
    data {
      id
      name
      funnelLocation
      channel
    }
    userErrors {
      field
      message
    }
  }
}

```

The following sections explain the core components of a mutation: name, data, and errors.

## Mutation name

Inside the mutation, the first object must be the name of the mutation you want to use and pass an input object as an argument. The inputs field names must match the variables in the schema.

Here's an example of a basic mutation that requests the bare minimum.

```
mutation {
  adGroupCreate(
    input: {
      campaignId: "CAMPAIGN_ID_PLACEHOLDER"
      name: "AD_GROUP_NAME_PLACEHOLDER"
      channel: DISPLAY
      funnelLocation: CONVERSION
    }
  )
}
```

The following table describes the `adGroupCreate` mutation.

| Field | Required? | Description |
| --- | --- | --- |
| `mutation` | Required | The type of GraphQL operation. Possible values include `query` and `mutation`. **NOTE**: To avoid confusion with mutation names in our API and optional mutation descriptions, mutation descriptions aren't included in our examples. |
| `adGroupCreate` | Required | The name of the GraphQL mutation denoted in the schema. **NOTE**: The mutation name format is _entityNameOperation_. Here, `adGroup` is the entity name and `create` is the operation. You must not modify or rename the mutation name. |
| `input` | Required | An object that contains all arguments for the mutation. |
| `campaignId`, `name`, `channel`, `funnelLocation` | Required | A variable. Here's what you need to know about variables: - You can only use variables inside the input field. - The schema specifies which variables are required with the `!` symbol. - You must specify all required variables to use the mutation. |

## Data object

To check for additional information from the response of a mutation, you can include fields to return inside the `data` object. This structure is similar to a query, but is limited to the data returned by the mutation, rather than the entire schema.

Here's an example of a mutation that requests the `id` and `name` fields to be returned.

```
mutation {
  ...
  data {
    id
    name
    channel
    Objective: funnelLocation
  }
}
```

In the context of the `adGroupCreate` mutation, this returns the ID, name, channel, and funnel location of the ad group you created.

The following table describes the data object.

| Property | Required? | Description |
| --- | --- | --- |
| `data` | Optional | An object that returns information on updates made by the mutation. |
| `id`, `name`, `channel` | Optional | The name of the field to return in the response. **IMPORTANT**: The field must match the response in the schema. To specify multiple fields, add them into the data object on each line. |
| `Objective` | Optional | An alias that you can use to rename a field for your needs in the response. |

## Mutation errors

> **IMPORTANT**: A mutation can send error information through the `errors` or `userErrors` objects, and doesn't check for some errors unless specified.

To find which error object to use, inspect your schema based on which mutations you're using. Inside the mutation, the schema shows whether it has an `errors` or `userErrors` object. For details on the error type pattern, see FAQs.

Here's what you need to know about errors in GraphQL mutations:

- All error information is stored in the `message` and `field` property. Some errors can have additional fields with more information.
- Check your GraphQL mutations to determine what values exist in your error. For details on retrieving the schema, see Making GraphQL API calls.
- Error messages only appear when you add the corresponding error object to your mutation body.

The following table describes the properties of an error.

| Property | Required? | Description |
| --- | --- | --- |
| `errors` | Depends | An error object that denotes information, such as error messages, bad fields, and more. |
| `userErrors` | Depends | A legacy error object that can contain the bad field and error messages. |
| `field` | Recommended | A field that when specified returns the list of fields that caused errors. Leave this as `field`. |
| `message` | Recommended | A field that when specified contains any error messages returned by the GraphQL API. Leave this as `message`. |

> **NOTE**: Errors can have other properties not listed. For details on which properties are available, see the error type in the schema.

After you've identified which object to use, refer to Errors object or UserErrors object.

### Errors object

To check if your request failed with the `errors` object, you must include the `__typename` field. GraphQL mutations that support the `errors` object in the mutation are more versatile and can return more properties than the `userErrors` object. To check for all possible errors, use `MutationError`.

#### Catch-All Errors object example

Here's an example GraphQL mutation that checks for all possible errors and returns back the type of error, field, and error message.

```
mutation {
  advertiserCreate ( input: { ... } ) {
    data { ... }
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

To return additional fields related to the error, refer to the schema and use the individual error type.

#### Individual Errors object example

Here's an example JSON response that troubleshoots for specific errors in a mutation. Each individual error type can be found in the `errors` property of the schema.

```
mutation {
  advertiserCreate( input: { ... } ) {
    data { ... }
    errors {
      ... on AdvertiserInternalExceptionError {
        field
        message
      }
      ... on AdvertiserValidationError {
        field
        message
      }
      ... on AdvertiserValidationRangeError {
        actualValue
        field
        max
        message
        min
      }
    }
  }
}
```

### UserErrors object

Older mutations might use the `userErrors` object instead of the `errors` object. Both objects function similarly, but `userErrors` doesn't have additional error fields.

When the GraphQL API sends error information through the `userErrors` object, it includes the fields that caused the error, and an error message. Here's an example of a mutation that uses the `userErrors` object to return any invalid fields and error messages.

```
mutation {
  adGroupCreate( input: { ... } ) {
    data { ... }
    userErrors {
      field
      message
    }
  }
}
```

## FAQs

The following is a list of commonly asked questions about our GraphQL API mutations.

### Are mutations supported in Solimar?

No. All mutations apply to only Kokai. To upgrade to Kokai and use mutations, see Campaign creation workflow with GraphQL.

### How are GraphQL mutations similar to REST?

Similar to REST, mutations can be used to accomplish POST, PUT, and DELETE operations. Some of these operations include campaign create, campaign clone, and campaign flight deletion.

### Can I use aliases in mutations?

No. Mutation names must match the schema. There is no alias for them. However, you can alias the data object values returned. For details, see GraphQL API queries.

### What's the difference between the errors object sent in a mutation and the GraphQL errors object?

The errors object is part of the mutation structure and contains information on expected errors. The GraphQL errors object reports unexpected errors related to the server, and isn't contained inside any mutations or queries. For details on error types, see GraphQL errors and limits.

### Why am I receiving a "cannot represent value" error in Postman?

When using the schema in Postman to create a mutation, Postman automatically adds quotation marks (") to all inline argument field values even if they're not strings. To avoid errors, remove the inserted quotation marks before you submit your request. For example, instead of `budgetInAdvertiserCurrency: "10000"`, use `budgetInAdvertiserCurrency: 10000`.

### How do I check which error object to use through my editor?

To check whether your mutation supports the `errors` or `userErrors` object, look at the return type of the error in the schema. The mutations should match the following patterns:

- If the mutation supports the `errors` object, the error return type ends with `Payload`.
- If the mutation supports the `userErrors` object, the error return type starts with `PayloadWithErrors`.
