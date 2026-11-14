# Language: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/language-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Language: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `POST /v3/language/query` | `Query.ttdLanguages`, `Query.peer39Languages` | Paged language query; choose query by `LanguageSourceType` (`Default` → `ttdLanguages`, `Peer39SiteLanguage` → `peer39Languages`) |
