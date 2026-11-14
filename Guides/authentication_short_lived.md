# Short-lived API tokens

- Source: https://open.thetradedesk.com/advertiser/docsApp/Foundations/resources/doc/AuthenticationShortLive
- Retrieved: 2026-11-14
- Category: Guides

---

# Short-lived API tokens

When authenticating to the REST or GraphQL API, you can create tokens through the Platform UI (recommended) or Platform API. When you create tokens through the API, creation is limited to short-lived tokens. These short-lived tokens are designed to provide a limited window of access that can last for up to a day.

> **TIP**: When using tokens in production, create API tokens through the Platform UI. For details, see Authentication.

Before you can create a token, you must have your Platform API credentials provided by your Account Manager. For details, see Get started.

## Create a short-Lived API token

You can create short-lived tokens with a lifetime range of up to 24 hours using the `POST /v3/authentication` endpoint.

To generate a short-lived API token with an expiration of up to 24 hours (1440 minutes), complete the following steps:

1. In the request body of the POST /v3/authentication endpoint, provide your Platform API credentials in the `Login` (your username) and `Password` properties.
2. (Optional) If you want to create a token with an expiration shorter than 24 hours, specify the appropriate life span in the `TokenExpirationInMinutes` property. Otherwise, its default value is `1440` minutes (24 hours).
3. Send your request and upon a successful response, copy the returned API token from the payload and save it to your secrets management system for future reference.
4. Include the token as the `TTD-Auth` value in the headers of all subsequent API calls.

> **IMPORTANT**: Be sure to save your generated API token to your secrets management system, as you will not be able to look it up or regenerate the same token. If you do not save your token, you will need to generate a new one.

The following sections provide examples of a POST /v3/authentication call, its request and response payloads, and a header with a newly generated API token.

### Endpoint

```
POST %%API_ROOT%%/authentication
```

### Request body example

The following example request generates a short-lived token that lasts for an hour.

```
{
 "Login" : "TTD_API_CLIENT_USERNAME_PLACEHOLDER",
 "Password":"TTD_API_CLIENT_PASSWORD_PLACEHOLDER",
 "TokenExpirationInMinutes":"60"
}
```

### Response body example

```
{
 "Token": "IBqLpJBhK/UnugaMLo56tUittjoBsjG1KCZ0FxxkIoY="
}
```

### Header example with an API token

```
Content-Type: application/json
TTD-Auth: IBqLpJBhK/UnugaMLo56tUittjoBsjG1KCZ0FxxkIoY=
```

## FAQs

The following are the most commonly asked questions about generating tokens.

### What's the maximum lifetime of a short-lived token?

Short-lived tokens can last for up to 24 hours (1,440 minutes).

### Can I refresh a short-lived token?

No. After a token is generated, the expiration date cannot be modified.

### Can I revoke my short-lived tokens?

No. You cannot revoke short-lived tokens. Tokens are automatically revoked only after they expire.

### How do tokens generated in the Platform API differ from tokens generated in the Platform UI?

Short-lived tokens are created through the Platform REST API and expire within a day. This is intended for temporary or low-risk use cases because these tokens cannot be altered or revoked.

Tokens created through the Platform UI can have a lifetime range from one week to one year. These tokens are generally recommended for most production scenarios, since you can modify or revoke the token. For details, see Authentication.

> **TIP**: When using tokens in production, create API tokens through the Platform UI. For details, see Authentication.
