# Creative: REST → GraphQL migration guide

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/creative-domain
- Retrieved: 2026-11-14
- Category: REST_API

---

# Creative: REST → GraphQL migration guide

## Quick reference table

| REST endpoint | GraphQL operation | Notes |
| --- | --- | --- |
| `GET /v3/creative/{creativeId}` | `Creative` | N/A |
| `POST /v3/creative/query/advertiser` | `Advertiser.creatives` | N/A |
| `GET /v3/creative/name/{creativeId}` | `Creative.id`, `Creative.name` | Lightweight ID/name—no new fields |
| `POST /v3/creative` | `creativeCreate` | N/A |
| `PUT /v3/creative` | `creativeUpdate` | N/A |
| `POST /v3/creative/generateuploadurlforaudiocreative` | `creativeCreatePresignedUrlGenerate` | Unified presigned upload; set audio MIME type on `file.contentType` |
| `POST /v3/creative/generateuploadurlforvideocreative` | `creativeCreatePresignedUrlGenerate` | Same mutation; set video MIME type on `file.contentType` |
| `POST /v3/creative/scan/tmt/{account}/policyViolation` | N/A | Not currently available in GraphQL |
| `POST /v3/creative/scan/tmt/{account}/incident` | N/A | Not currently available in GraphQL |

## Shared nested types and enums

### CreativeDeepLink

REST `CreativeDeepLinkAttributes` nests links under `UriScheme.Link` and `UniversalLink.Link`. GraphQL exposes a flat `deepLinks` array on supported concrete types only (`HostedDisplayCreative`, `HostedNativeCreative`, `HostedNativeVideoCreative`, `HostedVideoCreative`)—not on the `Creative` interface. Query with an inline fragment.

| REST field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `UriScheme.Link` | `link` | String! | Not nullable | Where `linkType` is `URI_SCHEME`. |
| `UniversalLink.Link` | `link` | String! | Not nullable | Where `linkType` is `UNIVERSAL_LINK`. |
| N/A | `linkType` | DeepLinkType! | Not nullable | `URI_SCHEME` or `UNIVERSAL_LINK`. |

On create, deep links can also be supplied via `chinaCreativeInfo.uriSchemeDeepLink` / `universalLinkDeepLink` on format `*Options` inputs when `willThisBeServedInChina: true`.

### Format-specific REST *attributes wrappers

REST returns one `*Attributes` wrapper per creative. GraphQL flattens those leaves onto concrete `Creative` implementors:

| REST attributes wrapper | GraphQL concrete type | Create input | Update input |
| --- | --- | --- | --- |
| ImageAttributes | `HostedDisplayCreative` | `hostedDisplayOptions` | `hostedDisplayCreativeOptions` |
| ThirdPartyTagAttributes | `ThirdPartyDisplayCreative` | `thirdPartyDisplayOptions` | `thirdPartyDisplayCreativeOptions` |
| TradeDeskHostedVideoAttributes | `HostedVideoCreative` | `hostedVideoOptions` | `hostedVideoCreativeOptions` |
| TradeDeskHostedAudioAttributes | `HostedAudioCreative` | `hostedAudioOptions` | `hostedAudioCreativeOptions` |
| ThirdPartyHostedVideoAttributes | `ThirdPartyVideoCreative` | `thirdPartyVideoOptions` | `thirdPartyVideoCreativeOptions` |
| ThirdPartyHostedAudioAttributes | `ThirdPartyAudioCreative` | `thirdPartyAudioOptions` | `thirdPartyAudioCreativeOptions` |
| Html5Attributes | `HostedHtml5Creative` | `hostedHtml5Options` | `hostedHtml5CreativeOptions` |
| HostedNativeAttributes | `HostedNativeCreative` | `hostedNativeOptions` | `hostedNativeCreativeOptions` |
| HostedNativeWithThirdPartyVideoAttributes | `HostedNativeVideoCreative` | `hostedNativeVideoOptions` | `hostedNativeVideoCreativeOptions` |
| ThirdPartyNativeAttributes | `ThirdPartyDisplayCreative` | `thirdPartyDisplayOptions` | `thirdPartyDisplayCreativeOptions` |
| FacebookAttributes | N/A | N/A | Deprecated on REST |
| FacebookPagePostAttributes | N/A | N/A | Deprecated on REST |
| FlashAttributes | N/A | N/A | Deprecated on REST |

Set `creativeType` on `CreativeCreateInput` to the enum value matching the chosen `*Options` input. See `POST /v3/creative` for per-field nested mappings within each options type.

### CreativeTypeInput (create)

Required on `CreativeCreateInput.creativeType`. Set to match the single `*Options` input provided.

| REST CreativeType (conceptual) | GraphQL enum value |
| --- | --- |
| Hosted display (image) | `HOSTED_DISPLAY` |
| Third-party display (tag) | `THIRD_PARTY_DISPLAY` |
| Hosted video | `HOSTED_VIDEO` |
| Hosted audio | `HOSTED_AUDIO` |
| Third-party video | `THIRD_PARTY_VIDEO` |
| Third-party audio | `THIRD_PARTY_AUDIO` |
| HTML5 | `HOSTED_HTML5` |
| Hosted native | `HOSTED_NATIVE` |
| Hosted native + video | `HOSTED_NATIVE_VIDEO` |
| Broadcaster hosted video | `BROADCASTER_HOSTED_VIDEO` |

See endpoint docs for full per-field mappings within each `*OptionsInput` / `*ICreativeOptionsInput` type.
