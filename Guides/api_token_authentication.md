# API Token Authentication

- Source: https://open.thetradedesk.com/advertiser/docsApp/Foundations/resources/doc/PlatformAuthentication
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/doc/Authentication (retired)
- Retrieved: 2026-11-14
- Category: Guides

---

# API token authentication

To authenticate your requests to the REST or GraphQL API, you must generate API tokens in the OpenTTD access management app. These tokens have a lifetime from one week to one year.

If you also want to upload data to the platform for targeting purposes, use the Data API, which uses the same authentication method.

To access the REST and GraphQL API, you need the following:

 The API credentials provided by your Account Manager.
 An API token, generated and placed in the header of your request.

You must create and revoke API tokens using the interactive UI experience available through the OpenTTD Access Management app.

> **TIP**: To change the lifetime of a token or otherwise update it, you need to revoke it, generate a new token, and then replace the tokens in your integration.

## Create an API token

You can create tokens with a lifetime range of one week to one year using the OpenTTD access management app.

To generate an API token, complete the following steps:

1. Log in with your The Trade Desk account credentials.
2. Navigate directly to the OpenTTD Access Management app.
3. Click **Generate Token / Key**. The Generate API Token dialog appears.
4. Enter a descriptive name for your token. For example, include the tool name for which it will be used or any other details that will help you distinguish between multiple tokens later.
5. In the **Application** field, select **Platform API**.
6. Select the token lifetime based on your key rotation strategy and integration needs.
7. Click **Save**. A confirmation message appears with an API token.
8. Copy the displayed API token, save it to your secrets management system for future reference, and then close the message.
9. Include the token as the `TTD-Auth` value in the headers of all API calls that use tokens, for instance, as shown in the following example.

```
Content-Type: application/json
TTD-Auth: IBqLpJBhK/UnugaMLo56tUittjoBsjG1KCZ0FxxkIoY=
```

> **IMPORTANT**: Save your API token in your secrets management system, you cannot retrieve or regenerate the same token. If you lose it, you must create a new token.

To change the lifetime of a token or otherwise update it, you need to revoke it, generate a new token, and then replace the tokens in your integration. For details, see Platform authentication.

## Check your API token information

To check the creation and expiration dates or the names of your generated API tokens, complete the following steps:

1. Log in with your The Trade Desk account credentials.
2. Navigate directly to the OpenTTD Access Management app.

> **TIP**: To update a token, you need to revoke it, generate a new token, and then replace the tokens in your integration.

## Revoke an API token

If your API token has been compromised, is no longer needed, or needs to be replaced with a new token with a longer or shorter lifetime, you can revoke the token at any time.

To revoke a API token, complete the following steps:

1. Log in with your The Trade Desk account credentials.
2. Navigate directly to the OpenTTD Access Management app.
3. Find the row with the name of the token you want to revoke, then in the Actions column on the far right, click **Revoke**. A confirmation message appears.
4. Verify that you've selected the correct token and click **Continue**.
5. Update the integration where the token was used as needed (for example, by generating a new token and replacing the old one in the integration).

## FAQs

The following are the most commonly asked questions about generating tokens.

### When generating an API token, what do I do if the Application option I need to select is unavailable?

Contact your Technical Account Manager for assistance.

### What if I need a token that lasts for less than one week?

For applications or API that use a shorter token lifetime, you can create a short-lived token that lasts for up to 24 hours. For details, see Short-lived API tokens.

> **NOTE**: This feature is not available for PDP or OpenPath tokens.

### What should I do if I need access to an Amazon S3 bucket?

For details, see Amazon S3 Access.

### Can I use OAuth 2.0 instead of an API token to authenticate Data API calls?

Yes, if you're a third-party data provider that calls the Data API on behalf of advertisers. For details, see OAuth 2.0 authentication.
