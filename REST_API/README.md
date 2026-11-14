# REST API areas

Each `REST_API/<area>.md` file lists one area of TTD's REST reference: its GraphQL operations and REST endpoints,
one heading per operation (`### POST /v3/...`), each with a link to the live reference page. The request and
response schemas are not here (see the root `README.md`, "What is not here"). For field names per endpoint, use
the REST-to-GraphQL mapping pages in `REST_API/migration/` (`<verb>-v3-<path>.md`).

## Endpoints Airspot calls that are not in TTD's public reference

Checked 2026-11-14 against the live sitemap (`AdvertiserReferences/api/ref/...`) and the pre-refresh copy.
These are undocumented or hidden (access through TTD's account team). This folder cannot back any claim about them.

| Endpoint | Airspot caller (airspot-dsp `origin/dev`) |
|---|---|
| `PUT /v3/campaign/bulksettings` | `src/modules/rest/ttd-rest.service.ts:935` (already handles a 405) |
| `POST /v3/tracking/universalpixel/query/advertiser` | `src/modules/rest/ttd-rest.service.ts:1199` |
| `POST /v3/tracking/universalpixel/urlmapping` | `src/modules/rest/ttd-rest.service.ts:1266` |
| `POST /v3/tracking/universalpixel/eventmapping` | `src/modules/rest/ttd-rest.service.ts:1291` |
| `POST /v3/tracking/universalpixel/urlmapping/query/universalpixel` | `src/modules/rest/ttd-rest.service.ts:1316` |
| `POST /v3/tracking/universalpixel/eventmapping/query/universalpixel` | `src/modules/rest/ttd-rest.service.ts:1317` |
| `PUT /v3/tracking/universalpixel/urlmapping` | `src/modules/rest/ttd-rest.service.ts:1376` |
| `PUT /v3/tracking/universalpixel/eventmapping` | `src/modules/rest/ttd-rest.service.ts:1400` |

The documented route for pixel mappings is `PUT /v3/tracking/universalpixel` with the mappings in the body
(`REST_API/tracking.md`). Per `Guides/universal_pixel.md`, updating mappings that way archives any tracking tags
that become unmapped.
