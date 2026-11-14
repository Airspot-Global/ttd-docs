# TTD API docs (Airspot copy)

A local copy of The Trade Desk's public advertiser API documentation, plus Airspot's own notes on
behaviour we observed. Airspot repos cite these files (`<file>:<line>`) as the source for TTD API claims.

- **Retrieved: 2026-11-14** (OpenTTD build `openTtd version 2.154.4`). This is the "as of" date to quote.
- Source site: `https://open.thetradedesk.com` (advertiser persona). The old Partner Portal
  (`partner.thetradedesk.com/v3/portal`) is retired; its URLs only appear on `- Legacy source:` lines.
- Sitemap: `https://open.thetradedesk.com/sitemap.xml`
- Scope (`scripts/scope.txt`): `Foundations/resources`, `GuidesAdvertiser/api`, `GuidesAdvertiser/deals`,
  `GuidesAdvertiser/data`, `AdvertiserNews/news` and `AdvertiserReferences/api/doc` (REST-to-GraphQL migration pages).
- **file:line citations dated before 2026-11-14 resolve against git tag `pre-openttd-refresh` (84b10ed).**

## Layout

| Folder | Content |
|---|---|
| `Guides/` | Guides, news, release notes and upgrade notices |
| `GraphQL/` | GraphQL guides and examples |
| `REST_API/` | One file per REST reference area: the area's GraphQL operations and REST endpoints, with links to the live reference |
| `REST_API/migration/` | TTD's REST-to-GraphQL migration guide: 291 files, `README.md` (`RestToGqlMigrationGuide`), 56 domain pages and 234 endpoint pages (field mappings). The live site lists 239 endpoint pages; the 5 REDS column pages serve no text (see below) |
| `manifest.tsv` | One row per TTD-sourced file: `local_path`, `live_url`, `legacy_url`, `retrieved`, `status` (`live`, `renamed`, `removed`), `sha256` of the TTD body (Airspot blocks excluded) |
| `scripts/` | The refresh tooling |

`Guides/reporting_best_practices.md` and the `README.md` files are written by Airspot. They have no TTD source,
are not in the manifest and are never touched by the refresh.

### What is not here
- **REST request and response schemas and the GraphQL type reference.** TTD draws those pages
  (`/api/ref/...`, `/api/gql-doc/...`, `/api/area/...`) in the browser; the server does not return their text.
  The site's JSON behind them could not be fetched within the fetch rules below: `/api/graphql-schema` returns the
  app shell, `/rest/openttd/advertiser/content/matchopenapi` without its (unknown) query string returns 404, and the
  app bundle that holds that query string is served from a CDN host outside `open.thetradedesk.com`
  (checked 2026-11-14). Field names per REST endpoint come from the migration pages in `REST_API/migration/`,
  which list the REST fields and their GraphQL equivalents but not every enum or constraint.
- The `REST_API/*.md` endpoint lists and one-line descriptions are the pre-refresh copy. Their links were checked
  against the live sitemap, and endpoints no longer in the reference are marked.
- Endpoints Airspot calls that are not in TTD's public reference are listed in `REST_API/README.md`.
- Pages in scope that return no text (checked 2026-11-14), so they have no file: `GuidesAdvertiser/api/doc/AudienceUnlimited`
  and the five REDS column mapping pages `AdvertiserReferences/api/doc/get-v3-reds-{bids,clicks,conversions,impressions,video}-columns`.
- Only the pages Airspot needs were added (manifest rows). Other in-scope pages (for example the rest of
  `GuidesAdvertiser/data/doc`) are fetched by the script but not kept; add a manifest row to keep one.

## Refresh

```
TTD_DOCS_UA=Claude-User scripts/refresh-docs.sh /tmp/ttd-refresh          # fetch + extract (writes only to that folder)
python3 -I scripts/merge_docs.py . /tmp/ttd-refresh <YYYY-MM-DD>          # dry run: summary only
python3 -I scripts/merge_docs.py . /tmp/ttd-refresh <YYYY-MM-DD> --write  # update the files and manifest.tsv
```

Run it monthly, or before any TTD-facing ticket. Read `Guides/upcoming_api_changes.md` first. A changed `sha256`
in `manifest.tsv` marks the pages to re-read; unchanged pages are not rewritten and keep their `- Retrieved:` date.
To add a page, add a manifest row (`local_path`, `live_url`, `status=live`, other columns empty) and run the merge.

- Extractor exit codes: 2 = no `llm-content` article (logged to `_noarticle.log`), 3 = unbalanced table markup
  (the run stops). Tests: `python3 -I scripts/test_extract_llm_content.py`.
- Comparing with the previous copy (the similarity table and word diffs behind a refresh review):
  `python3 -I scripts/compare.py <repo-root> <md-dir> <unused>` prints the token similarity of each Guides/GraphQL
  file with its live page; `python3 -I scripts/wdiff.py <local.md> <live.md> [max]` prints the word-level changes.

## Rules

1. **Keep file paths.** Every file keeps its path, because citations use paths. New pages get new snake_case files.
   Pages TTD removed stay, with a "Removed from TTD docs" banner and `status=removed`.
2. **Header** on every TTD-sourced file:
   ```
   # <Title>

   - Source: https://open.thetradedesk.com/advertiser/docsApp/<Section>/<hub>/<type>/<Name>
   - Legacy source: https://partner.thetradedesk.com/v3/portal/... (retired)   # only where one existed
   - Retrieved: YYYY-MM-DD
   - Category: GraphQL | Guides | REST_API

   ---
   ```
3. **Airspot notes are fenced** and put back by the merge, never retyped by hand:
   ```
   <!-- airspot:begin anchor="Environment URLs" -->
   > **Airspot note (observed 2026-11-09, ...):** ...
   <!-- airspot:end -->
   ```
   `anchor` is the heading text the block follows; the merge puts the block right after the first heading with
   that text (case-insensitive). If the heading is gone, the block goes under a final
   `## Airspot notes (anchor not found)` section and the merge prints a warning. `placement="header"` puts a block
   as the last line of the header list (before `---`); `placement="after-header"` puts it first after `---`.
   In `REST_API/*.md` the anchors are the endpoint headings, for example `POST /v3/geosegment/query/advertiser`.
4. **One "as of" record:** this README holds the retrieval date; `manifest.tsv` holds one row per TTD-sourced file.
5. Links to the retired portal (`/v3/portal/...`) are rewritten to OpenTTD URLs when the sitemap has the target.
   The merge prints the ones it cannot map (`UNMAPPED-LINK`).
6. Before a refresh that moves lines, tag the previous commit and add a citation sentence above.
7. **Fetch safety** (`scripts/refresh-docs.sh`, every request):
   - The URL must be `https` with the exact host `open.thetradedesk.com` (no subdomain, no port). Anything else
     stops the run. Sitemap entries on another host are skipped and logged to `_offhost.log`, never requested.
   - List mode: `TTD_DOCS_UA=... scripts/refresh-docs.sh <out-dir> <url-list-file>` (a second positional
     argument) fetches only the listed URLs, each with the same checks (https, exact host, no redirects, no cookies
     or auth, stop on an off-host URL). Its output has no `_sitemap_urls.txt`, so it is for spot re-fetches only;
     always run `merge_docs.py` on the output of a full sitemap run.
   - No redirects (`--max-redirs 0`). Any status other than 200, or an effective URL that differs from the
     requested one, stops the run.
   - No cookies, no `Authorization` or `TTD-Auth` header, no curl config file (`-q`). The only custom header is
     the user agent (`TTD_DOCS_UA`, an honest agent name; TTD serves page text only to agent user agents).
   - One request at a time, 0.3 s apart. Never call TTD's APIs (`api.thetradedesk.com`, `ext-api.sb.thetradedesk.com`).
8. Stage by explicit path (`git add README.md manifest.tsv scripts/ .gitignore GraphQL/ Guides/ REST_API/`).

Other files: `taxonomy.tsv`, `taxonomy.json` and `transform.js` hold the IAB Content Taxonomy v3.1. They are not
from TTD's site and are outside the refresh.
