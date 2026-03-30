# API Token Authentication

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/Authentication
- Category: Guides

---

# API Token Authentication

To authenticate your requests to the REST or GraphQL API, you must generate access tokens in the Platform UI. These tokens can be configured to last from one week to one year.

To access the REST and GraphQL API, you need the following:

 The Platform API credentials provided by your Account Manager. For details, see [Get Started](/v3/portal/api/doc/ApiPlatformGetStarted).  
 An authentication token that you need to generate and place in the header of your integration.  

You can [create](#ui-method-create) and [revoke](#ui-method-revoke) API tokens using the interactive UI experience available through [Manage API Tokens](/v3/tokens).

> **TIP**: To change the lifetime of a token or otherwise update it, you need to revoke it, generate a new token, and then replace the tokens in your integration.

## 

Create an API Token[](#ui-method-create)

You can create tokens with a lifetime range of one week to one year using the Platform UI.

To generate an API token, complete the following steps:

1.  Log in to the Partner Portal with your The Trade Desk account credentials.
2.  Navigate directly to [Manage API Tokens](/v3/tokens).
3.  Click **Generate Token**. The Generate API Token dialog appears.
4.  Enter a descriptive name for your token. For example, include the tool name for which it will be used or any other details that will help you distinguish between multiple tokens later.
5.  In the **Application** field, select **Platform API**.
6.  Select the token lifetime based on your key rotation strategy and integration needs.
7.  Click **Save**. A confirmation message appears with an API token.
8.  Copy the displayed API token, save it to your secrets management system for future reference, and then close the message.
9.  Include the token as the `TTD-Auth` value in the headers of all subsequent API calls, for instance, as shown in the following example.

Content-Type: application/json

TTD-Auth: IBqLpJBhK/UnugaMLo56tUittjoBsjG1KCZ0FxxkIoY=

> **IMPORTANT**: Be sure to save your generated API token to your secrets management system, as you will not be able to look it up or regenerate the same token. If you do not save your token, you will need to generate a new one.

## 

Check Your API Token Information[](#ui-method-view)

To check the creation and expiration dates or the names of your generated API tokens, complete the following steps:

1.  Log in to the Partner Portal with your The Trade Desk account credentials.
2.  Navigate directly to [Manage API Tokens](/v3/tokens).

> **TIP**: To update a token, you need to revoke it, generate a new token, and then replace the tokens in your integration.

## 

Revoke an API Token[](#ui-method-revoke)

If your API token has been compromised, is no longer needed, or needs to be replaced with a new token with a longer or shorter lifetime, you can revoke the token at any time.

To revoke a API token, complete the following steps:

1.  Log in to the Partner Portal with your The Trade Desk account credentials.
2.  Navigate directly to [Manage API Tokens](/v3/tokens).
3.  Find the row with the name of the token you want to revoke, then in the Actions column on the far right, click **Revoke**. A confirmation message appears.
4.  Verify that you've selected the correct token and click **Continue**.
5.  Update the integration where the token was used as needed (for example, by [generating a new token](#ui-method-create) and replacing the old one in the integration).

## 

FAQs[](#faqs)

The following are the most commonly asked questions about generating tokens.

### 

When generating an API token, what do I do if the Application option I need to select is unavailable?

Contact your Technical Account Manager for assistance.

### 

What if I need a token that lasts for less than one week?

For applications or APIs that use a shorter token lifetime, you can create a short-lived token that lasts for up to 24 hours. For details, see [Short-Lived API Tokens](/v3/portal/api/doc/AuthenticationShortLive).