# POST /v3/creative/generateuploadurlforaudiocreative → creativeCreatePresignedUrlGenerate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-creative-generateuploadurlforaudiocreative
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/creative/generateuploadurlforaudiocreative → creativeCreatePresignedUrlGenerate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/creative/generateuploadurlforaudiocreative` |
| GraphQL operation | `creativeCreatePresignedUrlGenerate` |
| Input type | `CreativeCreatePresignedUrlGenerateInput` |
| Output type | `CreativeCreatePresignedUrlGeneratePayload` (`creativeCreatePresignedUrl: CreativeCreatePresignedUrl`, `errors: [CreativeCreatePresignedUrlGenerateError!]`) |

GraphQL `creativeCreatePresignedUrlGenerate` is a unified presigned-upload mutation for audio, video, and other hosted assets. Set `file.contentType` to the MIME type for the audio file (for example `audio/mpeg` for `.mp3`).

## Multi-step operations

Presigned audio upload URLs are step 1 before calling `creativeCreate` with `hostedAudioOptions`. After uploading to the returned `url`, pass the public asset URL as `hostedAudioOptions.assetUrl` on create—GraphQL does not return REST's cycle-back `AudioUploadAttributes` object.

## Input field mapping

Input type: `CreativeCreatePresignedUrlGenerateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | `advertiserId` | ID! | Required | N/A |
| `FileName` | `file.fileName` | String! | Required | Valid extensions: .mp3, .m4a, .flac, .wav, .oga, .ogg |
| N/A | `file.contentType` | String! | Required | GraphQL-only on input; REST infers content type in the response. Supply the MIME type (e.g. `audio/mpeg`). |

## Output field mapping

Output type: `CreativeCreatePresignedUrlGeneratePayload`

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `AudioUploadUrl` | `creativeCreatePresignedUrl.url` | String! | Not nullable | Presigned S3 upload URL. |
| `AudioContentType` | N/A | N/A | N/A | Remodelled in GraphQL—GraphQL expects `file.contentType` on input instead. |
| `AudioUploadAttributes` | N/A | N/A | N/A | Remodelled in GraphQL—GraphQL uses `url` + `hostedAudioOptions` |
| `AudioUploadAttributes.AudioCreativeId` | N/A | N/A | N/A | Remodelled in GraphQL—derive asset URL from upload response. |
| `AudioUploadAttributes.AudioCreativeExtension` | `creativeCreatePresignedUrl.filename` | String! | Not nullable | Echo of requested file name; extension only—not a separate creative ID. |

## Endpoint-specific nested types and enums

### CreativesUploadPresignedUrlFileInput

Nested under `CreativeCreatePresignedUrlGenerateInput.file`.

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `FileName` | `fileName` | String! | Required | Include file extension. |
| N/A | `contentType` | String! | Required | GraphQL-only; set to audio MIME type matching the extension. |

## Code examples

### REST example

```
POST /v3/creative/generateuploadurlforaudiocreative HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserId": "abc123",
  "FileName": "creative-audio.mp3"
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation GenerateAudioUploadUrl($input: CreativeCreatePresignedUrlGenerateInput!) {
  creativeCreatePresignedUrlGenerate(input: $input) {
    creativeCreatePresignedUrl {
      url
      filename
    }
    errors {
      ... on AuthorizationError {
        message
        field
      }
      ... on CreativesUploadPresignedUrlsGenerateUnrecognizableFileTypeError {
        message
        field
        fileName
      }
    }
  }
}
```

Variables:

```
{
  "input": {
    "advertiserId": "abc123",
    "file": {
      "fileName": "creative-audio.mp3",
      "contentType": "audio/mpeg"
    }
  }
}
```

Upload the file to `creativeCreatePresignedUrl.url`, then pass the resulting public asset URL to `creativeCreate` via `hostedAudioOptions.assetUrl`.
