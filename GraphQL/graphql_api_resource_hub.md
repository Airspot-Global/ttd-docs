# GraphQL API Resource Hub

- Source: https://partner.thetradedesk.com/v3/portal/resources/doc/GqlApiHub
- Category: GraphQL

---

# GraphQL API Resource Hub

Welcome to The Trade Desk GraphQL Resource Hub, your one-stop destination for all things GraphQL. Whether you're a seasoned developer or just getting started, this hub is designed to empower you with the tools and knowledge needed to make the most of our GraphQL APIs.

## 

Why GraphQL?[](#why)

GraphQL offers a query language and runtime that enables you to request exactly the data you need—no more, no less. It provides an intuitive and powerful alternative to REST, especially for complex data requirements or when consolidating multiple queries into a single request. While you can choose between REST and GraphQL based on your needs, both technologies can complement each other to maximize your capabilities.

Here’s a rundown of the foundational concepts that will help you get started:

| Concept | Description |
| Schemas | Define the structure and capabilities of the GraphQL API, including data types and relationships. |
| [Queries](/v3/portal/resources/doc/GqlApiQueries) | GraphQL queries request specific data from a single endpoint, unlike REST’s multiple endpoints. The GraphQL API enables you to construct and run queries to retrieve only the information you need. It can customize queries to return specific fields across multiple entities. This empowers you to precisely define the request, reduce complexity, and response times, by limiting the scope of information.  
**IMPORTANT**: While support for nested queries allows retrieving related data in a single call, [complexity limits](/v3/portal/resources/doc/GqlResponses#errors-system) apply. |
| [Mutations](/v3/portal/resources/doc/GqlApiMutations) | The GraphQL API enables you to construct and run mutations to create and update values in the schema. It accepts parameters to specify details, making them versatile for different use cases. GraphQL mutations function similarly to POST, PUT, and DELETE requests. |
| [Bulk Operation](/v3/portal/api/doc/GqlBulkOperations) | The GraphQL API enables you to run large-scale GraphQL operations without relying on spreadsheets or tedious manual pagination. |
| Fields and Aliases | Fields represent pieces of data requested in a query, allowing for optimized, selective data retrieval. Aliases in [queries](/v3/portal/resources/doc/GqlApiQueries) let you rename fields in the response, which is useful for retrieving the same type of data multiple times in a query. |
| Arguments and Filters | Arguments allow parameters to be passed to fields or mutations, enabling filters and sorting. You can apply [filters](/v3/portal/resources/doc/GqlApiQueries#filters) to data requests to control the data returned. |
| Introspective | Schema self-discovery allows clients to explore the schema programmatically, helping developers discover available types, fields, and mutations. |

> **TIP**: For a quick overview, see [GraphQL Explained in 100 Seconds](https://www.youtube.com/watch?v=eIQh02xuVw4) on YouTube.

## 

Master the Basics of Our GraphQL API[](#tasks)

Discover the foundational skills and concepts you need to unlock the full potential of our GraphQL API. The Resource Hub pages provide a focused overview of key capabilities, practical tools, and troubleshooting techniques to help you navigate and optimize your API interactions effectively. Here are some of the key tasks you can master with the help of this resource, regardless of The Trade Desk product you intend to use:

*   Retrieve the data you need with powerful and flexible query structures.
*   Modify data and perform actions efficiently.
*   Access the API securely.
*   Make API calls in Postman and Python.
*   Troubleshoot issues and understand system constraints.
*   Optimize your API usage while adhering to usage guidelines.

## 

FAQs[](#faqs)

The following are some of the commonly asked questions about GraphQL.

### 

Which of The Trade Desk products use GraphQL?

We've been adding GraphQL functionality incrementally to all of our products. We encourage you to check for updates as we roll out new functionality and enhancements. We greatly appreciate your patience and feedback as we continue to improve your experience.

### 

Can I use GraphQL to bypass rate limiting?

No. Although rate limiting won't work quite the same with the customizable nature of GraphQL, we have reasonable limits in place to prevent abuse and server overload. For details, see [GraphQL API Rate Limits](/v3/portal/resources/doc/GqlApiRateLimits).

### 

Will GraphQL API eventually replace REST API?

Currently, the GraphQL API is an augmentative feature within our API infrastructure to give users more control over their data than the REST API.

### 

How are GraphQL mutations similar to REST?

GraphQL mutations are similar to REST in that both enable you to modify server data through a request-response model. Like REST's HTTP methods (POST, PUT, DELETE), mutations allow for creating, updating, and deleting data, with inputs specified through arguments in GraphQL or request bodies in REST. Both provide feedback on the operation's success or failure—GraphQL through its response payload and REST via HTTP status codes and response bodies. While GraphQL mutations use a single endpoint for all operations, similar to REST's specific endpoints, both approaches ensure structured communication for data modification.

### 

Is there a test environment for GraphQL API?

It depends on the product. For example, for the Platform GraphQL API, we offer a [Partner Sandbox](/v3/portal/api/doc/PartnerSandbox) where you can test platform API integrations without breaking changes to your production environment.

### 

Is there a GraphQL API reference?

Yes, the API reference shows both GraphQL anhd REST API endpoints.

### 

What exactly is the difference between the two API technologies?

The following table provides a high-level comparison of the REST and GraphQL technologies.

| Comparison Aspect | REST API | GraphQL API |
| Architecture | Is an architectural style. | Is a query language. |
| Communication | Uses HTTP methods (GET, POST, PUT, DELETE) to perform CRUD (Create, Read, Update, Delete) operations on resources. | Is technically transport-agnostic, but in practice sends queries to create, export, and update data to a single endpoint with the POST HTTP method. |
| Data Fetching | Provides a fixed data structure for each endpoint. Can lead to over-fetching or under-fetching. | You can specify exactly what data you need in the query. Eliminates over-fetching and under-fetching. |
| Data Retrieval | Requires additional requests for additional data. | Retrieve multiple resources and related data in one request. |
| Schema | Has no formal schema, endpoints represent resources. | Requires a defined schema specifying capabilities and available data types. |
| Flexibility | Fixed structure; you must send additional requests for more data. | Flexible; you specify data needs in the query. |
| Developer Experience | Simplicity and scalability. | Efficiency and ability to optimize data fetching for your needs. |

For more details on each technology, see the following YouTube videos:

*   [GraphQL Explained in 100 Seconds](https://www.youtube.com/watch?v=eIQh02xuVw4)
*   [RESTful APIs in 100 Seconds](https://www.youtube.com/watch?v=-MTSQjw5DrM) (the first 2.5 minutes)