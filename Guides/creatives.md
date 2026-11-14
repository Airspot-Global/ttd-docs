# Creatives

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/Creative
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/doc/Creative (retired)
- Retrieved: 2026-11-14
- Category: Guides

---

# Creatives

A creative is the video, audio, HTML5, or image (display) advertisement hosted either by The Trade Desk or by a third-party ad server. You can upload creatives using the GraphQL or REST APIs.

Here's what you need to know about uploading creatives:

- Ad groups require at least one associated creative to be able to spend.
- You can upload creatives using GraphQL or REST API. See the following for examples:

  - Upload creatives in GraphQL
  - Upload creatives in REST

- You cannot change the type of creative after creation.

For more information on creatives, see Ad Content Guidelines in the Knowledge Portal. The following sections compare using GraphQL and REST for uploading creatives and offer guidelines and examples to help you deploy and manage your creatives.

## GraphQL vs. REST

The following table describes some differences between using GraphQL and REST for uploading creatives.

| Task | GraphQL | REST |
| --- | --- | --- |
| Retrieve a creative. | getCreative query. | GET /v3/creative endpoint. |
| Upload a creative. | creativeCreate mutation. | GET /v3/creative endpoint (for example, through cURL). |
| Add metadata. | Add fields in the same `creativeCreate` mutation when uploading. | POST /v3/creative endpoint. |
| Get creative auto-approved (approved creatives don't require manual review or encoding workflows after upload). | For eligible creatives, you must explicitly enable automatic approval. | Creatives are automatically approved when eligible (also true in the platform UI). |
| Choose the format for providing creative content. | Use URLs. | Use URLs unless they are display creatives hosted by The Trade Desk. In that case, use Base64‑encoded strings. |
| Update a creative. | creativeUpdate mutation. | PUT /v3/creative endpoint. |

> **NOTE**: The GraphQL endpoints do not expose every field that exists in REST, and some fields are modeled differently. To retrieve a schema with every available GraphQL field, see Creative API reference.

## Management guidelines

Here are some guidelines for deploying and managing your creatives:

- While you can upload creatives with non-secured URLs (`http`), secured URLs (`https`) are recommended. Most SSPs reject creatives with non-secured URLs, thus preventing spend.
- For better control over which creatives are shown more frequently in an ad group, you can manually or automatically adjust their Creative weights.
- Use GraphQL to associate and manage creatives in ad groups.

## Examples

To find code examples of uploading creatives, see the following:

- GraphQL
- REST

For more examples in REST, see Upload creatives in the Creative connector article.

## FAQs

The following is a list of commonly asked questions about creatives.

### What's the best way to determine if a creative is approved?

Use the `approvedBy` field. If it's `null`, the creative is either not approved or waiting for approval. If it contains a username, the creative is approved.

### Can I rely on the internalCreativeReviewStatus field to determine the approval state?

No. The `internalCreativeReviewStatus` field is used for political creatives only, so it's usually `null` for other creatives.
