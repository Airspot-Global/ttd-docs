# Get Started for Advertisers

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/AdvertisersOpenTTD
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/doc/Advertisers (retired)
- Retrieved: 2026-11-14
- Category: Guides

---

# Get started for advertisers

If you are an advertiser looking to purchase media for your brand, you've come to the right place. After you've received your API credentials, follow this guide for an overview of the steps involved in creating your advertiser account and setting up your campaigns. You'll also discover a variety of resources to help you explore new features and optimize performance. By using these resources, you can unlock the full potential of your campaigns and get the best return on investment.

Here's what you need to know about advertisers before you continue:

- To create campaigns, tracking tags, and data elements in the API platform, as well as upload creatives, you must first create your advertiser account. That generates the advertiser ID, which is required for all these entities. In the entity hierarchy, advertisers are the owners of campaigns, ad groups, and creatives. For more information, see Entity relationships.
- You can create, update, and manage your advertiser information using the GraphQL and REST endpoints. You can also use the GraphQL API to create custom queries, enabling you to retrieve specific data from multiple entities and records. For details, see FAQs.

## Workflow

The following tiles offer a high-level overview of the end-to-end workflow for creating your advertiser, setting up your campaign, optimizing performance, and generating reports. We recommend following the steps sequentially, but the specific order may depend on your situation.

### 1. Create an advertiser

/v3/portal/api/doc/AdvertiserCreate

Before you can buy ad space, you need to create an advertiser. An advertiser ID is required for most calls, including data onboarding, and creating campaigns.

### 2. Onboard data

/v3/portal/data/doc/DataGetStartedAdvertiser

Upload your first-party data to support audience-based buying. This customer data is the foundation of your campaigns.

### 3. Create seeds

/v3/portal/api/doc/Seed

Seeds form the core of your campaign strategy. Create the most accurate representation of your most valuable converted customers and help drive real-time insights and AI-driven optimizations.

### 4. Create campaigns

/v3/portal/api/doc/Campaigns

Set budgets and pacing to optimize your campaigns. Expand your audience reach and improve performance by adding channels like Connected TV.

### 5. Create ad groups

/v3/portal/api/doc/AdGroup

Set goals for each ad group and balance performance across the funnel. Assign your Creatives to ad groups and run different formats across multiple Channels.

### 6. Drive KPIs

/v3/portal/api/doc/DriveKPIs

Learn how our AI-driven algorithms help you bid for value, not just lower cost. Maximizing expressiveness gives the platform more flexibility to drive your KPIs toward success.

### 7. Inform decisions with reports

/v3/portal/reds/overview?/advertiser/docsApp/GuidesAdvertiser/reds/doc/ReportingGetStartedAdvertiser

Customize reports to gain insights into performance and audience behavior, so you can fine-tune your campaign strategies.

> **TIP**: For users with access, you can also explore the interactive workflow maps in the Knowledge Portal and visualize the programmatic process from left to right.

## Implementation resources

The following resources are available to help implement your campaigns.

| Documentation Resource | Description |
| --- | --- |
| Entity relationships diagrams | Take a look at the diagrams to better understand the ownership and assignment relationships between API platform entities from the partner level to the ad-group level. |
| Platform API: REST and GraphQL | While the GraphQL API is designed to support newer Kokai-first experiences, both the GraphQL and REST APIs can be used interchangeably for most core features. You can use them concurrently depending on your needs. REST remains essential for accessing legacy functionality, such as Solimar budgets, while GraphQL offers streamlined access to new Kokai-exclusive features and more efficient capabilities, such as bulk queries. |
| Partner Sandbox | To ensure your workflows are running smoothly before implementing any changes in production, be sure to test and verify your workflows in our new partner sandbox environment. This sandbox has the same data and users as our production environment and is wiped clean weekly. This allows you to experiment freely, knowing that next week your data in the sandbox will be fully restored to match your data in production. To access this sandbox environment, use your production Public API keys. In other words, no need to change anything in your code except the URL to test everything. |

## FAQs

The following is a list of frequently asked questions about advertisers and the campaign setup.

### How do I choose the right API?

You can use either the REST and GraphQL API to create and manage campaigns. Both are fully supported. However, if you want to create, clone, or update multiple campaigns in one call, GraphQL is the better fit. It's also required for features that are exclusive to Kokai, like Kokai budget allocation and seed management.

If you’re managing campaigns with Solimar budgets, or you're only updating a single campaign at a time, REST is still a great choice, especially for legacy workflows.

### What is the difference between the REST and GraphQL API? When would I use each option?

REST and GraphQL are technologies used for designing and querying APIs in web development, but they have different approaches, philosophies, and intended uses in our platform. You can use GraphQL to access new features, enable more flexible queries, and perform bulk operations. For details, see Platform API: REST and GraphQL. See also Campaign creation workflows.

### Do I need to create a seed before creating an advertiser?

No. You must create an advertiser before creating a seed. When you create the initial seed, it will automatically get attached to the advertiser, saving you a step. Unless specified otherwise, the seed will also be attached to new campaigns by default.
