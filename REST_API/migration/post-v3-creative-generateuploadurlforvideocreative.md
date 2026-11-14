# POST /v3/creative/generateuploadurlforvideocreative → creativeCreatePresignedUrlGenerate

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/doc/post-v3-creative-generateuploadurlforvideocreative
- Retrieved: 2026-11-14
- Category: REST_API

---

# POST /v3/creative/generateuploadurlforvideocreative → creativeCreatePresignedUrlGenerate

## Overview

| Property | Value |
| --- | --- |
| REST endpoint | `POST /v3/creative/generateuploadurlforvideocreative` |
| GraphQL operation | `creativeCreatePresignedUrlGenerate` |
| Input type | `CreativeCreatePresignedUrlGenerateInput` |
| Output type | `CreativeCreatePresignedUrlGeneratePayload` (`creativeCreatePresignedUrl: CreativeCreatePresignedUrl`, `errors: [CreativeCreatePresignedUrlGenerateError!]`) |

GraphQL `creativeCreatePresignedUrlGenerate` is a unified presigned-upload mutation for video, audio, and other hosted assets. Set `file.contentType` to the MIME type for the video file (for example `video/mp4` for `.mp4`).

## Multi-step operations

Presigned video upload URLs are step 1 before calling `creativeCreate` with `hostedVideoOptions` or `hostedNativeVideoOptions`. After uploading to the returned `url`, pass the public asset URL as `assetUrl` / `videoAssetUrl` on the relevant create options—GraphQL does not return REST's cycle-back `VideoUploadAttributes` object.

## Input field mapping

Input type: `CreativeCreatePresignedUrlGenerateInput`

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `AdvertiserId` | `advertiserId` | ID! | Required | N/A |
| `FileName` | `file.fileName` | String! | Required | Valid extensions: .webm, .mov, .wmv, .mpg, .mpeg, .mp4, .flv |
| N/A | `file.contentType` | String! | Required | GraphQL-only on input; REST infers content type in the response. Supply the MIME type (e.g. `video/mp4`). |

## Output field mapping

Output type: `CreativeCreatePresignedUrlGeneratePayload`

| REST response field | GraphQL field | GraphQL type | Nullable | Notes |
| --- | --- | --- | --- | --- |
| `VideoUploadUrl` | `creativeCreatePresignedUrl.url` | String! | Not nullable | Presigned S3 upload URL. |
| `VideoContentType` | N/A | N/A | N/A | Remodelled in GraphQL—GraphQL expects `file.contentType` on input instead. |
| `VideoUploadAttributes` | N/A | N/A | N/A | Remodelled in GraphQL—GraphQL uses `url` + options `assetUrl` / `videoAssetUrl` after upload |
| `VideoUploadAttributes.VideoCreativeId` | N/A | N/A | N/A | Remodelled in GraphQL—derive asset URL from upload response. |
| `VideoUploadAttributes.VideoCreativeExtension` | `creativeCreatePresignedUrl.filename` | String! | Not nullable | Echo of requested file name; extension only—not a separate creative ID. |

## Endpoint-specific nested types and enums

### CreativesUploadPresignedUrlFileInput

Nested under `CreativeCreatePresignedUrlGenerateInput.file`.

| REST field | GraphQL field | GraphQL type | Required | Notes |
| --- | --- | --- | --- | --- |
| `FileName` | `fileName` | String! | Required | Include file extension. |
| N/A | `contentType` | String! | Required | GraphQL-only; set to video MIME type matching the extension. |

## Code examples

### REST example

```
POST /v3/creative/generateuploadurlforvideocreative HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER

{
  "AdvertiserId": "abc123",
  "FileName": "creative-video.mp4"
}
```

### GraphQL example

```
POST /graphql HTTP/1.1
Content-Type: application/json
TTD-Auth: AUTH_TOKEN_PLACEHOLDER
```

```
mutation GenerateVideoUploadUrl($input: CreativeCreatePresignedUrlGenerateInput!) {
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
      "fileName": "creative-video.mp4",
      "contentType": "video/mp4"
    }
  }
}
```

Upload the file to `creativeCreatePresignedUrl.url`, then pass the resulting public asset URL to `creativeCreate` via `hostedVideoOptions.assetUrl` or `hostedNativeVideoOptions.videoAssetUrl`.
