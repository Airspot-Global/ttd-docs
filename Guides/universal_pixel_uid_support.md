# UID support

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/data/doc/TrackingTagsUniversalPixelUidSupport
- Retrieved: 2026-11-14
- Category: Guides

---

# UID support

A universal pixel can retarget web audiences without relying on cookies by using UIDs, which refer collectively to UID2 and EUID. When UID support is enabled, the universal pixel detects email addresses collected on an advertiser’s website. These email addresses are then sent in a client-side request to the UID service backend. The UID service processes this information and generates unique UID tokens, which are sent to The Trade Desk platform for audience targeting, seeds, and measurement.

> **NOTE**: UID2 is supported; EUID will be available soon.

To enable UID2 support for your universal pixel, do the following:

1. Contact your Technical Account Manager to get the necessary UID paperwork for signing. This is required to access the UID2 Portal.
2. In the UID2 Portal, set up the following with The Trade Desk:

  - Sharing permissions
  - Client-side integration key pairs, domain names, and mobile app IDs (if applicable)

> **TIP**: For more information about UID integration, see Client-Side Integration Guide for JavaScript and Account Setup.

When completed, configure your universal pixel for UID.

## Configure universal pixel

To configure a universal pixel to collect email addresses for UID, use the `UniversalPixelUidConfigCreate` GraphQL mutation and set the `collectionMethod` field to one of the options in the following table.

| Collection Method | Description | When to Use | Usage Details |
| --- | --- | --- | --- |
| `MACRO` | Passes raw or hashed email addresses from the client to the UID service. | You need control over how the email address is sourced, such as a custom function that supplies the email address through your own data layer. | See Email macro. |
| `DETECTION` | Scans the webpage for email inputs using identifiers such as CSS selectors and triggers, then forwards the collected email addresses to the UID service. | You want the universal pixel to collect email addresses automatically without writing custom logic to supply the email address. | See Detect email. |

Here's what you need to know about obtaining email addresses:

- You must collect email addresses on your webpage, usually during logins or form submissions.
- Both the email macro and detect email options transmit email addresses directly to the UID service, bypassing The Trade Desk servers.
- The Trade Desk neither accesses nor stores email addresses.
- You can switch the collection method, if needed. For details, see Update UID configuration.
- If a universal pixel is on a page where users don’t enter their email address, use the email macro option to retrieve the stored raw or hashed email addresses. For example, if the universal pixel is on `example.com/careers` and the email addresses are stored elsewhere, and the login happens in a different domain without the universal pixel like on `example.org/login`, use the email macro method on `example.com/careers`.

### Email macro

The email macro option enables The Trade Desk to send raw or hashed email addresses from the backend to the UID service.

Here's what you need to know about using the email macro:

- It requires the advertiser’s site to explicitly pass the email value to the universal pixel through JavaScript.
- Hashed email addresses must be normalized before hashing. For UID2, use the UID2 hashing tool to verify that your implementation is normalizing and encoding correctly.
- After implementing the email macro option, new universal pixel JavaScript code is generated. For details, see Obtain new universal pixel JavaScript code.
- The universal pixel reads only the value returned by the function at the time it is called.

Run the `UniversalPixelUidConfigCreate` mutation for the desired universal pixel with your input information and specify the fields you want to be returned in the response, such as `identityParamType`. The following example retrieves raw email addresses for the UID service, as the `identityParamType` field is set to `EMAIL`.

```
mutation UniversalPixelUidConfigCreate($input: UniversalPixelUidConfigInput!) {
  UniversalPixelUidConfigCreate(input: {
    advertiserId: "ADVERTISER_ID_PLACEHOLDER",
    collectionMethod: "MACRO",
    serverPublicKey: "SERVER_PUBLIC_KEY_PLACEHOLDER",
    subscriptionId: "SUBSCRIPTION_ID_PLACEHOLDER",
    uPixelId: "UPIXEL_ID_PLACEHOLDER",
    macroConfig: {
      identityMacro: "getEmail()",
      identityParamType: "EMAIL"
    }
  }) {
    data {
      collectionMethod
      serverPublicKey
      subscriptionId
      advertiserId
      ... on UniversalPixelUidMacroConfig {
        identityParamType
        identityMacro
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

#### Obtain new universal pixel JavaScript code

After you implement the email macro option, new universal pixel JavaScript code is generated. Obtain this code using the GET /v3/tracking/universalpixel/pixelcode/{universalPixelId} endpoint or through the platform UI. Then integrate it with your website by either adding it to or replacing the existing universal pixel JavaScript code in the shared location.

### Detect email

The detect email option enables The Trade Desk to automatically identify email input fields on a webpage and send collected email addresses to the UID service. When using the `UniversalPixelUidConfigCreate` mutation, you must provide at least one CSS selector and one trigger.

Specifying a selector and trigger tells the pixel exactly which field contains the email address and which user action should initiate collection (such as clicking the form submit button). The pixel reads the value from the specified input only when the trigger fires.

> **TIP**: For instructions on finding the CSS selectors and triggers, see this FAQ.

Run a `UniversalPixelUidConfigCreate` mutation for the desired universal pixel with your input information and specify the fields you want to be returned in the response, such as `cssSelectors` and `triggerElements`. The following example includes CSS selectors and trigger elements from multiple webpages in the `detectionConfig` object.

```
mutation UniversalPixelUidConfigCreate($input: UniversalPixelUidConfigInput!) {
  UniversalPixelUidConfigCreate(input: {
    advertiserId: "ADVERTISER_ID_PLACEHOLDER",
    collectionMethod: "DETECTION",
    detectionConfig: {
      cssSelectors: ["input.email", "input[id=CUSTOM_ID_PLACEHOLDER]", "input[id=EMAIL_ADDRESS_PLACEHOLDER]", "input[type=email]"],
      triggerElements: ["button[type=submit]", "input[type=submit]"]
    },
    serverPublicKey: "SERVER_PUBLIC_KEY_PLACEHOLDER",
    subscriptionId: "YOUR_SUBSCRIPTION_ID_PLACEHOLDER",
    uPixelId: "UPIXEL_ID_PLACEHOLDER"
  }) {
    data {
      collectionMethod
      serverPublicKey
      subscriptionId
      advertiserId
      ... on UniversalPixelUidDetectionConfig {
        cssSelectors
        triggerElements
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

## Validate setup

After configuring UID support, you can validate the setup using the `GetUniversalPixelUidConfigExample` GraphQL query. This query retrieves account details, including the identifier collection method and its configuration, such as CSS selectors, trigger elements, or identity parameter types.

```
query GetUniversalPixelUidConfigExample($universalPixelId: ID!) {
  universalPixel(id: $universalPixelId) {
    universalPixelUidConfig {
      collectionMethod
      serverPublicKey
      subscriptionId
      ... on UniversalPixelUidDetectionConfig {
        cssSelectors
        triggerElements
      }
      ... on UniversalPixelUidMacroConfig {
        identityParamType
        identityMacro
      }
    }
  }
}
```

> **TIP**: You can also validate UID support through the platform UI. The UID-enabled universal pixel is displayed there with the Unified ID logo next to its name.

## Update UID configuration

If you want to change the collection method or its configuration in the future, use the `UniversalPixelUidConfigUpdate` mutation. Here's an example of updating the collection method from detect email to email macro, with the identity parameter type configured for hashed email addresses.

If you change to the email macro, be sure to update the universal pixel JavaScript code. For details, see Email macro.

> **IMPORTANT**: Be sure the collection method matches the configuration input and response. For example, use `MACRO` with the `macroConfig` and `UniversalPixelUidMacroConfig` objects, or use `DETECTION` with the `detectionConfig` and `UniversalPixelUidDetectionConfig` objects.

```
mutation UniversalPixelUidConfigUpdate($input: UniversalPixelUidConfigInput!) {
  UniversalPixelUidConfigUpdate(input: {
    advertiserId: "ADVERTISER_ID_PLACEHOLDER",
    collectionMethod: "MACRO",
    serverPublicKey: "SERVER_PUBLIC_KEY_PLACEHOLDER",
    subscriptionId: "SUBSCRIPTION_ID_PLACEHOLDER",
    uPixelId: "UPIXEL_ID_PLACEHOLDER",
    macroConfig: {
      identityMacro: "getEmail()",
      identityParamType: "HASHED_EMAIL"
    }
  }) {
    data {
      collectionMethod
      serverPublicKey
      subscriptionId
      advertiserId
      ... on UniversalPixelUidMacroConfig {
        identityParamType
        identityMacro
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

## CSP requirements

A CSP is in your site's HTTP response header or in a `<meta>` tag in the page `<head>` tag. A different team usually manages a CSP than the one who implements the pixel. You do not configure the CSP in the pixel code itself.

If your website uses a CSP, make sure it has the domains required for universal pixels and, based on your collection method, the domains for UID support listed in the following table.

| Collection Method | Directives and domains |
| --- | --- |
| `DETECTION` | - `connect-src`: `https://*.prod.uidapi.com` `https://prod.uidapi.com` - `script-src`: `https://cdn.prod.uidapi.com` |
| `MACRO` | `operator-integ.uidapi.com` |

The following example shows the domains required for a universal pixel configured with the `DETECTION` collection method.

```
script-src 'self' cdn.prod.uidapi.com;
connect-src 'self'
  prod.uidapi.com
  *.prod.uidapi.com;
```

> **NOTE**: The leading asterisk (`*`) in `*.prod.uidapi.com` is an intentional wildcard that matches any subdomain of `prod.uidapi.com`.

The following example shows the domain required for a universal pixel configured with the `MACRO` collection method.

```
connect-src 'self'
  operator-integ.uidapi.com;
```

## FAQs

The following is a list of frequently asked questions about UID support.

#### Do I need to add domains for both UID collection methods?

No. Add only the domains for the collection method you've configured. Combine both sets only if you use multiple universal pixels with different collection methods on the same site.

#### Can I use my existing universal pixel for retargeting web audiences?

Yes, but only for the detect email option. Be sure to sign the applicable legal paperwork to get the subscription ID and server public key. For details, see Subscription ID and Public Key.

For the email macro option, you need to update the universal pixel JavaScript code.

#### Are there any changes in the requirements for pixel placement?

No. There are no changes in requirements with this upgrade; it’s still the standard JS placement, same as the existing pixel.

#### Where is the UID token stored?

The UID token is stored in the web local storage along with the refresh token. By default, data stored in the web local storage has no expiration unless the user clears their data. However, its usability depends on user opt-out and UID expiration (after one year).

#### Can I still capture UID from pages that do not directly collect the email address?

Yes. By storing the UID token in the web local storage, you can capture UID data from these pages.

#### Does a user have to log in again or pass the email address every time to generate a UID token?

No. By storing the UID token in the web local storage, you can capture UID data from these pages.

#### If Google decides to deprecate third-party cookies, could we still receive the UID token?

Yes. The UID token is not dependent on third-party cookies.

#### How comprehensively does a UID token generated at checkout track a user’s journey?

If the pages are in the same domain, The Trade Desk can track the user journey even if they haven’t provided an email address yet. For example, The Trade Desk can track the user browsing the homepage and About Us page before they provide an email address and check out their purchase.

#### Can phone numbers be used to generate UIDs from the universal pixel?

No. At this moment, only email addresses are allowed.

#### I generated UID tokens without using universal pixels and saved them in web local storage. Could the universal pixel pick them up?

Yes. The universal pixel can access UID tokens however they are generated.

#### What happens if the top-level domain of the page where the email is collected is different from the top-level domain of the landing page?

The Trade Desk would need the top-level domain of the page the email is collected on to register for UID. For example, if the landing page is `thetradedesk.ca` but the page where the email is added is `thetradedesk.com`, The Trade Desk needs both `thetradedesk.com` and `thetradedesk.ca` as domains to register for UID CSTG. Both domains can use the same public key and subscription ID.

#### When a user submits an email, does The Trade Desk ingest only UID?

No. If a cookie is present, The Trade Desk ingests both UID and cookies.

#### How do I find the CSS selectors and triggers for detecting email collection identifiers?

Use Chrome Developer Tools (or an equivalent tool in your preferred browser) to identify CSS selectors and trigger elements. You can do this by using its Inspect tool and hovering your cursor over each element, or by locating the relevant HTML code in the Elements tab.

As an example, the following table shows where each element is located in the UID2 Request Access webpage using Chrome Developer Tools.

| Element | Image |
| --- | --- |
| CSS selector for the email field (found with the Inspect tool): `input.#Email.mktoField.mktoEmailField.mktoHasWidth.mktoRequired` |  |
| CSS selector for the email input (found in the Elements tab): `input[type=email]` |  |
| Button trigger (found with the Inspect tool): `button.mktoButton` |  |
| Button trigger (found in the Elements tab): `button[type=submit]` |  |

To verify that the correct elements were selected, in the Console tab within your Chrome developer tools (or the equivalent tool in your preferred browser), enter `document.querySelector("ELEMENT_NAME_PLACEHOLDER")`. The following screenshot example shows the Console tab with the button element verified.
