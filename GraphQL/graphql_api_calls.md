# Making GraphQL API Calls

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/GqlApiCallsPlatform
- Category: GraphQL

---

# Making GraphQL API Calls

To make a GraphQL API call, you need the following:

 The Trade Desk platform API credentials provided by your Account Manager.  
 Your API token. For details, see [Authentication](/v3/portal/api/doc/Authentication).  
 Your tool or method of choice for making API calls (for example, Postman or Python).  
 A header (`TTD-Auth`) with your API token.  
 The URL for the environment you want to use.  

## 

Environment URLs[](#urls)

The following table lists the URLs for the environments that you can use.

| Environment | URL | Note |
| Production | `https://api.thetradedesk.com/graphql` | Build and deploy on production for professional use. |
| Sandbox | `https://ext-api.sb.thetradedesk.com/graphql` | Use the sandbox environment to test platform API integrations without breaking changes to your production environment. See also [Partner Sandbox](/v3/portal/api/doc/PartnerSandbox). |

> **IMPORTANT**: Complexity and rate limits apply to all platform GraphQL API calls. For details, see [GraphQL API Rate Limits](/v3/portal/resources/doc/GqlApiRateLimits) and [GraphQL API Errors and Complexity Limits](/v3/portal/resources/doc/GqlResponses).

Although you can use any tool of your choice to execute a GraphQL call, the following sections explain how to do so in [Postman](#postman) and [Python](#python).

## 

Postman[](#postman)

To make a GraphQL call in Postman, complete the following steps:

1.  To create a new request, in the left panel and at the top, click **New** and choose **GraphQL** as your request type.
2.  Enter the URL for the environment you want to use (sandbox or production).
3.  Click the **Headers** tab, and in the **Key** field, enter `TTD-Auth`, and in the **Value** field, enter your API token.
4.  To retrieve your schema, go to the **Schema** tab and click **Use GraphQL Introspective**.
5.  On the **Query** tab, do either of the following:
    *   To automatically generate and add fields to your [query](#sample-query), select the available fields in the left pane and enter the appropriate values as needed.
    *   To manually create your query, use the right pane.
6.  To send your request to the GraphQL Platform API, click the blue **Query** button at the top-right.

The response appears in the bottom pane with the details you requested. For details on the query anatomy and usage guidelines, see [GraphQL API Queries](/v3/portal/resources/doc/GqlApiQueries). For a list of client libraries, see [Code Using GraphQL](https://graphql.org/community/tools-and-libraries/).

## 

Python[](#python)

The following example demonstrates a GraphQL call in Python.

> **IMPORTANT**: To make GraphQL Platform API calls with Python, be sure to have the requests library installed on your system; for example, the GraphQLPythonlibrary on [GitHub](https://github.com/graphql-python/gql). See also [Code Using GraphQL](https://graphql.org/community/tools-and-libraries/).

Placeholder values that you must replace are shown in ALL CAPS.

import requests

# Define the GraphQL Platform API endpoint URLs.

sandbox\_url = 'https://ext-api.sb.thetradedesk.com/graphql'

production\_url = 'https://api.thetradedesk.com/graphql'

# Replace the placeholder value with your actual API token.

token = 'API\_TOKEN\_PLACEHOLDER'

# Define the GraphQL query.

query = """

query GetAdvertiser($advertiserId: ID!) {

    advertiser(id: $advertiserId) {

        id

        name

    }

}

"""

# Define the variables in the query.

variables = {

    "advertiserId": "ADVERTISER\_ID\_PLACEHOLDER"

}

# Create a dictionary for the GraphQL request.

data = {

    'query': query,

    'variables': variables

}

# Create headers with the authorization token.

headers = {

    # You can only use 1 auth header. You must choose 'TTD-Auth' 

    (preferred) or 'Authorization'.

    # DeskAPI and UnifiedAPI Tokens ONLY

    'TTD-Auth': token

    # DeskUI JWT Token ONLY

    # 'Authorization': f'Bearer {token}'

}

# Send the GraphQL request.

# The \`url\` param is used only for demonstration purposes. Be sure to 

replace it with the GraphQL platform API URL you want to target.

response = requests.post(url\=sandbox\_url, json\=data, headers\=headers)

if response.status\_code == 200:

    # Parse the response JSON

    result = response.json()

    print(result)

else:

    print(f"Request failed with status code: {response.status\_code}")

    print(response.text)

## 

Platform GraphQL API Resources[](#resources)

Here's a list of resources you can use to learn about the GraphQL API:

| Resource | Description |
| [GraphQL API Resource Hub](/v3/portal/resources/doc/GqlApiHub) | A high-level introduction to GraphQL concepts, query and mutation anatomy, best practices, response errors, and other non-platform-specific information. |
| [Partner Sandbox](/v3/portal/api/doc/PartnerSandbox) | A testing environment for workflows before implementing changes in production. |