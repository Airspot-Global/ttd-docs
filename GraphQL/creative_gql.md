# Upload creatives in GraphQL (closed beta)

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/CreativeGQL
- Retrieved: 2026-11-14
- Category: GraphQL

---

# Upload creatives in GraphQL (closed beta)

> **NOTE**: This feature is available to select clients through a closed beta. Ask your Technical Account Manager for access permission to the API.

This guide explains how to upload creatives using the GraphQL API. For general information about creatives, including creative types, requirements, and differences between GraphQL and REST, see Creatives.

Here's what you need to know when uploading creatives with GraphQL:

- Creative content should be provided using the hosted URLs.
- For eligible creatives, you can enable automatic approval. Approved creatives don't require manual review or encoding workflows after upload.

For the complete GraphQL schema and available fields, see Creative API reference. For instructions on uploading creatives using REST, see Upload creatives in REST.

## Workflow

Uploading creatives using GraphQL is a straightforward process. Use the following steps:

> **NOTE**: In GraphQL, creative creation and asset upload are separate steps. This guide uses "upload" as a shorthand for the combined workflow.

1. Determine whether the creative is hosted by The Trade Desk or a third party.
2. If hosted by The Trade Desk, generate a presigned upload URL.
3. Upload the creative asset.
4. Call the `creativeCreate` mutation to submit the creative metadata.
5. (Optional) For eligible creatives, enable automatic approval.

After completing the basic workflow, you can also do the following:

- Generate a share link for the creative by including the `shareLink` field in the `creativeCreateResult` object of the mutation.
- Update existing creatives using the creativeUpdate mutation.
- Use GraphQL to manage creatives in an ad group.

## Upload creatives hosted by The Trade Desk

If you are uploading creatives hosted by The Trade Desk, generate an upload URL before using the `creativeCreate` mutation.

> **TIP**: You can enable automatic approval for eligible creatives as an option. Approved creatives don't require manual review or encoding workflows after upload.

### Generate upload URL

To generate an upload URL, use the `creativeCreatePresignedUrlGenerate` mutation and add your advertiser ID and creative file information. Here is an example:

> **NOTE**: The value for the `contentType` field is a standard MIME-type string, such as `image/jpeg`, `image/png`, `video/mp4`, and `audio/mpeg`.

```
mutation {
  creativeCreatePresignedUrlGenerate(input: {
    advertiserId: "ADVERTISER_ID_PLACEHOLDER"
    file: {
      contentType: "CONTENT_TYPE_PLACEHOLDER"
      fileName: "IMAGE_FILENAME_PLACEHOLDER"
    }
  }) {
    creativeCreatePresignedUrl {
      filename
      url
    }
    errors {
      ... on AuthorizationError {
        field
        message
      }
      ... on CreativesUploadPresignedUrlsGenerateUnrecognizableFileTypeError {
        field
        fileName
        message
      }
    }
  }
}
```

The mutation returns a presigned upload URL, enabling you to securely upload the creative file. After you upload the file, use the `creativeCreate` mutation with the appropriate options, and provide the resulting URL to reference the uploaded file.

See examples of uploading creatives hosted by The Trade Desk and third parties.

### Enable automatic approval

To automatically approve eligible creatives, set the `shouldAutoApprove` field to `true` in the `creativeCreate` mutation. This feature is disabled by default.

The following creatives hosted by The Trade Desk are eligible for auto-approval:

- Video
- Audio
- Native video

For an example of the field used in a mutation, see Upload video creative hosted by The Trade Desk.

The following sections provide mutation examples for uploading video and display creatives hosted by The Trade Desk and a third-party ad server:

- Hosted by The Trade Desk
- Hosted by a third-party or broadcaster

For an example of a successful response, see Response.

## Examples of creatives hosted by The Trade Desk

> **IMPORTANT**: Before using a mutation, you must generate an upload URL.

The following sections provide mutation examples for creatives hosted by The Trade Desk:

- Video
- Audio
- Display
- HTML5
- Native display
- Native video

### Video

Here's an example `creativeCreate` mutation that shows how to upload a video creative hosted by The Trade Desk. It includes the `shouldAutoApprove` field for turning on auto-approval. Required fields for this creative type are the following:

- `assetUrl`
- `clickthroughUrl`
- `landingPageUrl`

```
mutation {
  creativeCreate(input: {
    advertiserId: "ADVERTISER_ID_PLACEHOLDER"
    creativeType: HOSTED_VIDEO
    name: "CREATIVE_NAME_PLACEHOLDER"
    shouldAutoApprove: true
    hostedVideoOptions: {
      assetUrl: "PRESIGNED_S3_URL"
      clickthroughUrl: "CLICKTHROUGH_URL_PLACEHOLDER"
      landingPageUrl: "LANDING_PAGE_URL_PLACEHOLDER"
    }
  }) {
    creativeCreateResult {
      creative {
        id
        name
      }
    }
    errors {
      ... on CreativeCreateValidationError {
        field
        message
      }
      ... on CreativeCreateServerError {
        field
        message
      }
      ... on AuthorizationError {
        message
      }
    }
  }
}
```

### Audio

Here's an example `creativeCreate` mutation that shows how to upload an audio creative hosted by The Trade Desk. Required fields for this creative type are the following:

- `assetUrl`
- `clickthroughUrl`
- `landingPageUrl`

```

mutation {
  creativeCreate(input: {
    advertiserId: "ADVERTISER_ID_PLACEHOLDER"
    creativeType: HOSTED_AUDIO
    name: "CREATIVE_NAME_PLACEHOLDER"
    hostedAudioOptions: {
      assetUrl: "PRESIGNED_S3_URL"
      clickthroughUrl: "CLICKTHROUGH_URL_PLACEHOLDER"
      landingPageUrl: "LANDING_PAGE_URL_PLACEHOLDER"
    }
  }) {
    creativeCreateResult {
      creative {
        id
        name
      }
    }
    errors {
      ... on CreativeCreateValidationError {
        field
        message
      }
      ... on CreativeCreateServerError {
        field
        message
      }
      ... on AuthorizationError {
        message
      }
    }
  }
}
```

### Display

Here's an example `creativeCreate` mutation that shows how to upload a display creative hosted by The Trade Desk. Required fields for this creative type are the following:

- `assetUrl`
- `clickthroughUrl`
- `landingPageUrl`

```
mutation {
  creativeCreate(input: {
    advertiserId: "ADVERTISER_ID_PLACEHOLDER"
    creativeType: HOSTED_DISPLAY
    name: "CREATIVE_NAME_PLACEHOLDER"
    hostedDisplayOptions: {
      assetUrl: "PRESIGNED_S3_URL"
      clickthroughUrl: "CLICKTHROUGH_URL_PLACEHOLDER"
      landingPageUrl: "LANDING_PAGE_URL_PLACEHOLDER"
    }
  }) {
    creativeCreateResult {
      creative {
        id
        name
      }
    }
    errors {
      ... on CreativeCreateValidationError {
        field
        message
      }
      ... on CreativeCreateServerError {
        field
        message
      }
      ... on AuthorizationError {
        message
      }
    }
  }
}
```

### HTML5

Here's an example `creativeCreate` mutation that shows how to upload an HTML5 creative hosted by The Trade Desk. Required fields for this creative type are the following:

- `clickTrackingParamName`
- `htmlAssetUrl`
- `landingPageUrls`
- `useClickthroughAsDefault`

> **NOTE**: If the `useClickthroughAsDefault` field is set to `true`, you must provide the clickthrough URL.

```

mutation {
  creativeCreate(input: {
    advertiserId: "ADVERTISER_ID_PLACEHOLDER"
    creativeType: HOSTED_HTML5
    name: "CREATIVE_NAME_PLACEHOLDER"
    hostedHtml5Options: {
      htmlAssetUrl: "PRESIGNED_S3_URL"
      clickthroughUrl: "CLICKTHROUGH_URL_PLACEHOLDER"
      clickTrackingParamName: "PARAMETER_NAME_PLACEHOLDER"
      heightInPixels: NUMBER_OF_PIXELS_PLACEHOLDER
      widthInPixels: NUMBER_OF_PIXELS_PLACEHOLDER
      landingPageUrls: ["LANDING_PAGE_URL_01_PLACEHOLDER", "LANDING_PAGE_URL_02_PLACEHOLDER" ]
      useClickthroughAsDefault: true
    }
  }) {
    creativeCreateResult {
      creative {
        id
        name
      }
    }
    errors {
      ... on CreativeCreateValidationError {
        field
        message
      }
      ... on CreativeCreateServerError {
        field
        message
      }
      ... on AuthorizationError {
        message
      }
    }
  }
}
```

### Native display

Here's an example `creativeCreate` mutation that shows how to upload a native display hosted by The Trade Desk. Required fields for this creative type are the following:

- `clickthroughUrl`
- `landingPageUrl`
- `mainAssetUrls`

```

mutation {
  creativeCreate(input: {
    advertiserId: "ADVERTISER_ID_PLACEHOLDER"
    creativeType: HOSTED_NATIVE
    name: "CREATIVE_NAME_PLACEHOLDER"
    hostedNativeOptions: {
      clickthroughUrl: "CLICKTHROUGH_URL_PLACEHOLDER"
      landingPageUrl: "LANDING_PAGE_URL_PLACEHOLDER"
      mainAssetUrls: ["PRESIGNED_S3_URL_01", "PRESIGNED_S3_URL_02"]
      sponsor: "SPONSOR_PLACEHOLDER"
      shortTitle: "SHORT_TITLE_PLACEHOLDER"
      shortDescription: "SHORT_DESCRIPTION_PLACEHOLDER"
    }
  }) {
    creativeCreateResult {
      creative {
        id
        name
      }
    }
    errors {
      ... on CreativeCreateValidationError {
        field
        message
      }
      ... on CreativeCreateServerError {
        field
        message
      }
      ... on AuthorizationError {
        message
      }
    }
  }
}
```

### Native video

Here's an example `creativeCreate` mutation that shows how to upload a native video hosted by The Trade Desk. Required fields for this creative type are the following:

- `clickthroughUrl`
- `landingPageUrl`
- `mainAssetUrls`
- `videoAssetUrl`

```
mutation {
  creativeCreate(input: {
    advertiserId: "ADVERTISER_ID_PLACEHOLDER"
    creativeType: HOSTED_NATIVE_VIDEO
    name: "CREATIVE_NAME_PLACEHOLDER"
    hostedNativeVideoOptions: {
      clickthroughUrl: "CLICKTHROUGH_URL_PLACEHOLDER"
      landingPageUrl: "LANDING_PAGE_URL_PLACEHOLDER"
      mainAssetUrls: ["PRESIGNED_S3_URL_01", "PRESIGNED_S3_URL_02"]
      sponsor: "SPONSOR_PLACEHOLDER"
      videoAssetUrl: "PRESIGNED_S3_URL_03"
      shortTitle: "SHORT_TITLE_PLACEHOLDER"
      shortDescription: "SHORT_DESCRIPTION_PLACEHOLDER"
    }
  }) {
    creativeCreateResult {
      creative {
        id
        name
      }
    }
    errors {
      ... on CreativeCreateValidationError {
        field
        message
      }
      ... on CreativeCreateServerError {
        field
        message
      }
      ... on AuthorizationError {
        message
      }
    }
  }
}
```

## Examples of creatives hosted by a third party or broadcaster

The following sections provide mutation examples for creatives hosted by a third-party ad server or broadcaster:

- Video
- Audio
- Display
- Video hosted by a broadcaster

### Video

Here's an example `creativeCreate` mutation that shows how to upload a video creative hosted by a third party.

> **IMPORTANT**: When explicitly provided, the landing page URL for the third-party video creative overrides the one in VAST. If the landing page URL is not found in VAST, it must be provided in the mutation.

```
mutation {
  creativeCreate(input: {
    advertiserId: "ADVERTISER_ID_PLACEHOLDER"
    creativeType: THIRD_PARTY_VIDEO
    name: "CREATIVE_NAME_PLACEHOLDER"
    thirdPartyVideoOptions: {
      vastXmlUrl: "VAST_URL_PLACEHOLDER"
      landingPageUrl: "LANDING_PAGE_URL_PLACEHOLDER"
    }
  }) {
    creativeCreateResult {
      creative {
        id
        name
      }
    }
    errors {
      ... on CreativeCreateValidationError {
        field
        message
      }
      ... on CreativeCreateServerError {
        field
        message
      }
      ... on AuthorizationError {
        message
      }
    }
  }
}
```

### Audio

Here's an example `creativeCreate` mutation that shows how to upload an audio creative hosted by a third party.

> **IMPORTANT**: When explicitly provided, the landing page URL for the third-party audio creative overrides the one in VAST. If the landing page URL is not found in VAST, it must be provided in the mutation.

```
mutation {
  creativeCreate(input: {
    advertiserId: "ADVERTISER_ID_PLACEHOLDER"
    creativeType: THIRD_PARTY_AUDIO
    name: "CREATIVE_NAME_PLACEHOLDER"
    thirdPartyAudioOptions: {
      vastOrDaastUrl: "VAST_URL_PLACEHOLDER"
      landingPageUrl: "LANDING_PAGE_URL_PLACEHOLDER"
    }
  }) {
    creativeCreateResult {
      creative {
        id
        name
      }
    }
    errors {
      ... on CreativeCreateValidationError {
        field
        message
      }
      ... on CreativeCreateServerError {
        field
        message
      }
      ... on AuthorizationError {
        message
      }
    }
  }
}
```

### Display

Here's an example `creativeCreate` mutation that shows how to upload a display creative hosted by a third party. Required fields for this creative type are the following:

- `adTag`
- `heightInPixels`
- `widthInPixels`
- `landingPageUrls`

```
mutation {
  creativeCreate(input: {
    advertiserId: "ADVERTISER_ID_PLACEHOLDER"
    creativeType: THIRD_PARTY_DISPLAY
    name: "CREATIVE_NAME_PLACEHOLDER"
    thirdPartyDisplayOptions: {
      adTag: "<script src='AD_TAG_URL_PLACEHOLDER'></script>"
      heightInPixels: 250
      widthInPixels: 300
      landingPageUrls: ["LANDING_PAGE_URL_01_PLACEHOLDER", "LANDING_PAGE_URL_02_PLACEHOLDER"]
    }
  }) {
    creativeCreateResult {
      creative {
        id
        name
      }
    }
    errors {
      ... on CreativeCreateValidationError {
        field
        message
      }
      ... on CreativeCreateServerError {
        field
        message
      }
      ... on AuthorizationError {
        message
      }
    }
  }
}
```

### Video hosted by a broadcaster

Here's an example `creativeCreate` mutation that shows how to upload a video creative hosted by a broadcaster (see BVOD). Required fields for this creative type are the following:

- `assetUrls`
- `clickthroughUrl`
- `landingPageUrl`

```
mutation {
  creativeCreate(input: {
    advertiserId: "ADVERTISER_ID_PLACEHOLDER"
    creativeType: BROADCASTER_HOSTED_VIDEO
    name: "CREATIVE_NAME_PLACEHOLDER"
    broadcasterHostedVideoOptions: {
      assetUrls: ["BROADCASTER_ASSET_URL_01", "BROADCASTER_ASSET_URL_02"]
      clickthroughUrl: "CLICKTHROUGH_URL_PLACEHOLDER"
      landingPageUrl: "LANDING_PAGE_URL_PLACEHOLDER"
    }
  }) {
    creativeCreateResult {
      creative {
        id
        name
      }
    }
    errors {
      ... on CreativeCreateValidationError {
        field
        message
      }
      ... on CreativeCreateServerError {
        field
        message
      }
      ... on AuthorizationError {
        message
      }
    }
  }
}
```

## Response

For all examples of uploading creatives hosted by The Trade Desk and third parties, a successful response appears in the following format:

```
{
  "data": {
    "creativeCreate": {
      "creativeCreateResult": {
        "creative": {
          "id": "CREATIVE_ID_PLACEHOLDER",
          "name": "CREATIVE_NAME_PLACEHOLDER"
        }
      },
      "errors": null
    }
  }
}
```
