# Platform API: REST and GraphQL

- Source: https://partner.thetradedesk.com/v3/portal/api/doc/ApisPlatform
- Category: GraphQL

---

# Platform API: REST and GraphQL

The Trade Desk uses both Representational State Transfer (REST) and GraphQL for designing our Platform APIs. The choice between REST and GraphQL often depends on factors such as the complexity of data requirements, your preferences, and the task at hand. You can also leverage both technologies concurrently.

> **TIP**: If you are new to GraphQL, check out our [GraphQL API Resource Hub](/v3/portal/resources/doc/GqlApiHub) and familiarize yourself with the basics.

REST API

Use it to access any features available on the platform, including campaign creation and budget management. The only exception is brand-new, Kokai-only features and bulk operations, which are available exclusively through GraphQL.

[

GET STARTED



](/v3/portal/api/doc/ApiUsageGuidelines)

GraphQL API

Use it to access Kokai-only features or when you need a flexible way to query specific partner, advertiser, campaign, and ad group data, download dimension-specific reports, create seeds or campaigns, or perform bulk operations.

[

GET STARTED



](/v3/portal/api/doc/GqlApiCallsPlatform)

## 

FAQs[](#faqs)

The following are some of the commonly asked questions about GraphQL.

### 

Is the GraphQL API only for Kokai, and the REST API only for Solimar?

Not exactly. While the GraphQL API is designed to support newer Kokai-first experiences, both the GraphQL and REST APIs can be used interchangeably for most core features. You can use them concurrently depending on your needs. REST remains essential for accessing legacy functionality, such as Solimar budgets, while GraphQL offers streamlined access to new Kokai-exclusive features and more efficient capabilities, such as bulk queries.

### 

Will the GraphQL API eventually replace the REST API?

Currently, the GraphQL API is an augmentative feature within the platform API infrastructure to give users more control over their data than the REST API. Whether GraphQL might eventually replace REST, there is no specific timeline or roadmap for this transition.