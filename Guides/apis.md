# The Trade Desk users and APIs

- Source: https://open.thetradedesk.com/advertiser/docsApp/Foundations/resources/doc/Apis
- Retrieved: 2026-11-14
- Category: Guides

---

# The Trade Desk users and APIs

Whether you're an advertiser, provider, or seller, The Trade Desk APIs give you the tools to build, integrate, and scale. Our APIs power The Trade Desk platform, Deal Desk, and other products and solutions, as well as partner offerings.

The following sections define who our users are and outline the available APIs.

## Our users

The Trade Desk platform serves three fundamentally different roles in the programmatic advertising ecosystem, and each role interacts with the platform in a distinct way. Advertisers run campaigns on the Open Internet, providers supply targeting data, and sellers supply inventory for advertisers to buy. Some organizations, such as data onboarders acting on behalf of advertisers, may use APIs associated with both the advertiser and provider roles.

The following table describes each user group.

| User group | Description | Example tasks | Example users |
| --- | --- | --- | --- |
| Advertiser | A brand or agency that runs campaigns, creatives, and reports for purchasing media on the Open Internet. | - Upload your first-party data. - Manage campaigns and drive KPIs. - Run reports. | Brand, agency, holding company, DSP |
| Provider | A third party that provides targeting or measurement data, lift studies, or partner-specific integrations. | - Onboard third-party data and make it available in the DMP. - Upload first-party data on behalf of an advertiser. - Monetize audience and sales data for brands to use in their campaigns. | Audience, contextual, geo, or measurement data provider; retailer (merchant), lift study or MMM provider, integrated partner, data onboarder |
| Seller | An inventory source or path that supplies ad space on the Open Internet to sell to advertisers. | - Propose deals to advertisers and manage live deal performance. - Create direct connections to supply through OpenPath. - Leverage insights into advertiser quality or validate the fairness of the auction. | Supply vendor, publisher, SSP, intermediary |

## Our APIs

The Trade Desk offers three API suites built around distinct platform activities. For example, the Data API handles data movement at scale, from onboarding first- and third-party data to managing identities and processing opt-outs. The Platform API powers campaign management and drives KPIs. The PDP API serves the supply side, by enabling deal creation and management, and provisioning data.

> **NOTE**: Your user role determines which APIs you'll primarily work with, though some Data and Platform API endpoints might overlap across advertiser and provider workflows.

The following table explains The Trade Desk APIs, what they do, how to access them, and who they're for.

| API | Technology | Description | Intended user group | Authentication | Notes |
| --- | --- | --- | --- | --- | --- |
| Data API | REST and GraphQL | Onboard large-scale data into The Trade Desk's servers for data integration, and ID deletion and opt-out management. | Provider, advertiser | - API Token - Signature Header (legacy) | - For a comparison of integration options (SDK, third-party connectors), see Integration options. - Some data workflows require selecting a target data center. |
| Platform API | REST and GraphQL | Manage campaigns, creatives, audiences, bid lists, and retrieve performance reports. | Advertiser, provider | API Token | Providers can use the API to manage taxonomies and data rates for third-party data, and to run reports. |
| PDP API (Price Discovery and Provisioning) | GraphQL | Create and manage deals and provisioning data between sellers and buyers. | Seller | API Token | Access is restricted. Contact your Technical Account Manager to enable access. |
