# Making GraphQL API Calls

- Source: https://open.thetradedesk.com/advertiser/docsApp/Foundations/resources/doc/GqlApiCallsPlatform
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/doc/GqlApiCallsPlatform (retired)
- Retrieved: 2026-11-14
- Category: GraphQL

---

# Making GraphQL API calls

To make a GraphQL API call, you need the following:

 The Trade Desk Platform API credentials provided by your Account Manager.
 Your API token. For details, see Authentication.
 Your tool or method of choice for making API calls (for example, Postman or Python).
 A header (`TTD-Auth`) with your API token.
 The URL for the environment you want to use.

## Environment URLs

<!-- airspot:begin anchor="Environment URLs" -->
> **Airspot note (observed 2026-11-09, sandbox + production; not in TTD's official docs):**
> - GraphQL responses carry the headers `X-RateLimit-Limit-Two-Minutes-path-USER-ID: 800`, `X-RateLimit-Remaining-Two-Minutes-path-USER-ID`, `RateLimit-Limit-path-USER-ID`, `RateLimit-Remaining-path-USER-ID` and `RateLimit-Reset-path-USER-ID` (seconds until reset). That is 800 requests per two minutes per user per path, shared by every service that uses the same login.
> - `partner { thirdPartyData }` timed out after 60 seconds in both production and the sandbox.
> - The root `thirdPartyDatas` query returned `INTERNAL_SERVER_ERROR` in the sandbox.
> - `partner { firstPartyData }` does not exist (`GRAPHQL_VALIDATION_FAILED`). First-party data is only on `advertiser { firstPartyData }`.
<!-- airspot:end -->

> **IMPORTANT**: Complexity and rate limits apply to all platform GraphQL API calls. For details, see GraphQL API rate limits and GraphQL API errors and complexity limits.

The following table lists the URLs for the environments that you can use. If you are using Walmart DSP, see Walmart DSP URLs.

| Environment | URL | Note |
| --- | --- | --- |
| Production | `https://api.thetradedesk.com/graphql` | Build and deploy on production for professional use. |
| Sandbox | `https://ext-api.sb.thetradedesk.com/graphql` | Use the sandbox environment to test platform API integrations without breaking changes to your production environment. See also Partner Sandbox. |

Although you can use any tool of your choice to execute a GraphQL call, the following sections explain how to do so in Postman and Python.

## Postman

To make a GraphQL call in Postman, complete the following steps:

1. To create a new request, in the left panel and at the top, click **New** and choose **GraphQL** as your request type.
2. Enter the URL for the environment you want to use (sandbox or production).
3. Click the **Headers** tab, and in the **Key** field, enter `TTD-Auth`, and in the **Value** field, enter your API token.
4. To retrieve your schema, go to the **Schema** tab and click **Use GraphQL Introspective**.
5. On the **Query** tab, do either of the following:

  - To automatically generate and add fields to your query, select the available fields in the left pane and enter the appropriate values as needed.
  - To manually create your query, use the right pane.

6. To send your request to the GraphQL Platform API, click the blue **Query** button at the top-right.

The response appears in the bottom pane with the details you requested. For details on the query anatomy and usage guidelines, see GraphQL API queries. For a list of client libraries, see Code Using GraphQL.

## Python

The following example demonstrates a GraphQL call in Python.

> **IMPORTANT**: To make GraphQL Platform API calls with Python, be sure to have the requests library installed on your system; for example, the GraphQLPythonlibrary on GitHub. See also Code Using GraphQL.

Placeholder values that you must replace are shown in ALL CAPS.

```
import requests

# Define the GraphQL Platform API endpoint URLs.
sandbox_url = 'https://ext-api.sb.thetradedesk.com/graphql'
production_url = 'https://api.thetradedesk.com/graphql'

# Replace the placeholder value with your actual API token.
token = 'API_TOKEN_PLACEHOLDER'

# Define the GraphQL query.
query = """
query GetAdvertiser($advertiserId: ID!) {
    advertiser(id: $advertiserId) {
        id
        name
    }
}
"""

# Define the variables in the query.
variables = {
    "advertiserId": "ADVERTISER_ID_PLACEHOLDER"
}

# Create a dictionary for the GraphQL request.
data = {
    'query': query,
    'variables': variables
}

# Create headers with the authorization token.
headers = {
    # You can only use 1 auth header. You must choose 'TTD-Auth' (preferred) or 'Authorization'.

    # DeskAPI and UnifiedAPI Tokens ONLY
    'TTD-Auth': token

    # DeskUI JWT Token ONLY
    # 'Authorization': f'Bearer {token}'
}

# Send the GraphQL request.
# The `url` param is used only for demonstration purposes. Be sure to replace it with the GraphQL platform API URL you want to target.
response = requests.post(url=sandbox_url, json=data, headers=headers)

if response.status_code == 200:
    # Parse the response JSON
    result = response.json()
    print(result)
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)
```

## Platform GraphQL API resources

Here's a list of resources you can use to learn about the GraphQL API:

| Resource | Description |
| --- | --- |
| GraphQL API Resource Hub | A high-level introduction to GraphQL concepts, query and mutation anatomy, best practices, response errors, and other non-platform-specific information. |
| Partner Sandbox | A testing environment for workflows before implementing changes in production. |

### Walmart DSP URLs

The following table lists the URLs for Walmart DSP. Be sure to update the Postman and Python examples to use the corresponding `sandbox_url` and `production_url` values.

| Environment | URL | Note |
| --- | --- | --- |
| Production | `https://desk.dsp.walmart.com/graphql` | Build and deploy on production for professional use. |
| Sandbox | `https://desksb-a.dsp.walmart.com/graphql` | Use the sandbox environment to test platform API integrations without breaking changes to your production environment. See also Partner Sandbox. |
