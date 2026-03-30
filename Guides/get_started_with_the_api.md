# Onboarding to The Trade Desk Platform API

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/ApiPlatformGetStarted
- Category: Guides

---

# Onboarding to The Trade Desk Platform API

The Trade Desk is a flexible, open platform that you can tailor to fit your business needs. Even if you’re already using the platform, chances are you’re not taking full advantage of all the ways you can use it to grow your business. With The Trade Desk API, you can grow your advantage and push the boundaries of your programmatic strategies with more granular control and deeper insights. Create custom optimizations to automate more trading, integrate third-party platforms to automate workflows, and even build your own custom media planning and buying products on top of our platform.

## 

Process Overview[](#process-overview)

Here's a high-level outline of the onboarding process.

| Step | Description | Notes |
| 1 | Create an account and verify your email address. | To create an account, you need to provide your name, email address, phone number, company name and address, and other information to your Account Manager or Technical Account Manager. If you don't have one assigned, [contact us](https://open.thetradedesk.com/contact-us) and fill out the form. |
| 2 | Choose the API features and custom solutions that meet your needs. | This step typically requires close collaboration with your Account Manager and Technical Account Manager. Certain custom solutions might require additional paperwork and access permissions. |
| 3 | Sign all the contract and other required paperwork and receive your API credentials. | After your account is set up, you'll receive an activation email with your API credentials that allow you to access both the sandbox and production environments.  
**NOTE**: Your API credentials do not provide access to the platform UI. |
| 4 | Use your API credentials to [generate an authentication token](/v3/portal/api/doc/Authentication) and start building your integrations. | Here's what you need to know about using the Platform API:

*   To access the Platform API, you must authenticate yourself.
*   Depending on your task at hand, communication with the Platform API is performed either via [REST and GraphQL](/v3/portal/api/doc/ApisPlatform).
*   To test your integrations, use the respective [sandbox environments](/v3/portal/api/doc/PartnerSandbox).

 |
| 5 | Use your auth token to [call the Platform API for REST and GraphQL](/v3/portal/api/doc/ApisPlatform) | The Platform API supports two methods for making calls, each with different endpoints and schemas. For more information, see [Making REST API Calls](/v3/portal/api/doc/ApiUsageGuidelines) or [Making GraphQL API Calls](/v3/portal/api/doc/GqlApiCallsPlatform). |

## 

Custom Solutions and API Services Menu[](#solutions-menu)

The following table lists the most commonly used custom solutions and API services and indicates the approximate level of effort required of a single engineer to set them up.

| Solution | Description | Approximate Building Time | Comments and Further Reference |
| Full API access | This enables you to create campaigns, ad groups, and bid lists, automate campaign activation, onboard and activate first-party data, create custom targeting and optimization rules, customize and automate reporting. | Depends on your needs | The access includes the workflow automation solutions. |
| Workflow automation | Key workflow automation solutions include the following:

*   [Campaign Connector](/v3/portal/api/doc/CampaignConnector) (automatic campaign creation by syncing with client-booking systems, such as Salesforce, MediaOcean, Strata, or an internal system of record)
*   [Creative Connector](/v3/portal/api/doc/CreativeConnector) (automatic creative upload and management by syncing with a client ad server or creative database)

 | 2-4 weeks | None. |
| Custom segments | The ability to upload custom first-party data segments to the platform using the data API. | 2 weeks | [Getting Started with Data Onboarding](/v3/portal/data/doc/DataGetStarted) |
| Custom bidding strategies | These include The Trade Desk Dimensional Bidding and User Scoring algorithms that use custom data-driven logic to enrich your buying strategies. | 4 weeks | [Custom Optimization Algorithms](/v3/portal/api/doc/CustomOptimizationAlgorithms) |
| Custom reporting and insights | The Trade Desk offers three custom reporting and attribution solutions that enable you to get deeper insights on your ROAS: My Reports, Hourly Performance Feeds, and Raw Event Data Stream (REDS). | 1 week  
2-4 weeks for REDS | To compare data availability, delivery methods, and other details, see [Reporting Solutions](/v3/portal/reds/overview). |

> **NOTE**: Custom solutions and API services typically require a setup fee. Be sure to speak to your assigned Business Development or Client Services lead.

## 

FAQs[](#faqs)

The following are most commonly asked questions about creating an account.

### 

What do I do if I lost my initial activation email?

Log in to the Partner Portal. A new activation email will be sent.

### 

What do I do if I forgot my password for logging in to the Partner Portal?

You must reset your password. To do this, go to the Partner Portal login page, enter your email and, when asked to enter your password, click **Forgot Password**. You will receive a confirmation email with instructions on how to create a new password.