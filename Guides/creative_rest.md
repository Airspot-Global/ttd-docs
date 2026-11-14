# Upload creatives in REST

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/CreativeREST
- Retrieved: 2026-11-14
- Category: Guides

---

# Upload creatives in REST

To upload a creative using REST, use the POST /v3/creative endpoint. This guide outlines key requirements and limitations when uploading creatives through the REST API.

The REST API for uploading creatives require the following parameters:

| Parameter | Description |
| --- | --- |
| `AdvertiserId` | The platform ID of the advertiser that owns the creative. |
| `CreativeName` | The name of the creative. **IMPORTANT**: Do not include any of the following special characters: `<>;^\r\n` |
| One of the `Attributes` objects | For example, `ImageAttributes`, `TradeDeskHostedVideoAttributes`, `Html5Attributes`, `ThirdPartyHostedVideoAttributes`, and so on. **NOTE**: You may specify only one creative-attributes object for any given creative. The choice depends on the type of the creative (display, video, HTML5, or other) and whether it is hosted by The Trade Desk or a third party. |

The partner-level and advertiser-level default URLs and tracking tags are assigned according to the creative type that the user selects in the platform UI. For details, see Upload creatives with default impression tracking tags and URLs.

For general details, see Creatives. For instructions on using our GraphQL API, see Upload creatives in GraphQL.

> **NOTE**: To update an existing creative, use the PUT /v3/creative endpoint.

## API call examples

The following sections provide examples for uploading video and display creatives hosted by The Trade Desk and a third-party ad server:

- Video creative hosted by The Trade Desk
- Audio creative hosted by The Trade Desk
- Display creative hosted by The Trade Desk
- Creative hosted by third parties
- Creative with default impression tracking tags and URLs

For more examples, see Upload creatives in the Creative connector article.

## Upload video creative hosted by The Trade Desk

The process of uploading video creatives hosted by The Trade Desk includes additional steps. The following table summarizes these steps.

| Step | Task | Endpoint |
| --- | --- | --- |
| 1 | Generate an upload URL. | POST /v3/creative/generateuploadurlforvideocreative |
| 2 | Upload your creative. | N/A |
| 3 | Post the creative details. | POST /v3/creative |

### Generate an upload URL

To upload your creative to a cloud storage, you need to generate a pre-signed URL. To do so, use the POST /v3/creative/generateuploadurlforvideocreative endpoint, which generates a pre-signed AWS S3 URL by default. To upload a video creative to Azure, include `x-ms-blob-type: BlockBlob` in the header.

Here's an example of a POST /v3/creative/generateuploadurlforvideocreative request that generates a URL:

```
{
    "AdvertiserId": "abc123",
    "FileName": "testcreative.mp4"
}
```

Here's an example of a POST /v3/creative/generateuploadurlforvideocreative response, which returns a URL, the creative ID, and its extension in the `VideoUploadAttributes` attribute:

```
{
    "VideoUploadUrl": "https://thetradedesk-video.s3.amazonaws.com/xyz123/abc123/d41qpmad.mp4?AWSAccessKeyId=AKI123456789876654321&Expires=1579376906&Signature=123456789786654321%3D",
    "VideoContentType": "video/mp4",
    "VideoUploadAttributes": { // These are the attributes to include in the POST /v3/creative request.
        "VideoCreativeId": "d41qpmad",
        "VideoCreativeExtension": "mp4"
    }
}
```

### Upload your video creative

To upload your video creative to the URL that you generated, make the following call with the values from the response and the file name:

```
curl -v -H "content-type:{VideoContentType}" -X PUT -T FileName -L "{VideoUploadUrl}"
```

Here's an example of a call:

```
curl -v -H "Content-Type: video/mp4" -X PUT -T testcreative.mp4 -L "https://thetradedesk-video.s3.amazonaws.com/xyz123/abc123/d41qpmad.mp4?AWSAccessKeyId=AKI123456789876654321&Expires=1579376906&Signature=123456789786654321%3D"
```

### Post the creative details

After you have uploaded your video creative to the generated URL, make a POST /v3/creative request and be sure to include the `VideoUploadAttributes` object from the `POST /v3/creative/generateuploadurlforvideocreative` response.

Here's an example of a POST /v3/creative request for uploading a video creative with companion creatives:

```
{
    "AdvertiserId": "abc123",
    "CreativeName": "TESTVIDEO",
    "TradeDeskHostedVideoAttributes": {
        "ClickthroughUrl": "https://www.xyz.com/",
        "LandingPageUrl": "https://www.xyz.com/",
        "VideoUploadAttributes": { // This is the object from the POST /v3/creative/generateuploadurlforvideocreative response.
            "VideoCreativeId": "d41qpmad",
            "VideoCreativeExtension": "mp4"
        },
        "CompanionCreativeIds": [
            "a6k1kltn",
            "b7k0klSn",
            "c8J0kltM"
        ]
    }
}
```

## Upload audio creative hosted by The Trade Desk

 The process of uploading audio creatives hosted by The Trade Desk includes additional steps. The following table summarizes these steps.

| Step | Task | Endpoint |
| --- | --- | --- |
| 1 | Generate an upload URL. | POST /v3/creative/generateuploadurlforaudiocreative |
| 2 | Upload your creative. | N/A |
| 3 | Assign the creative metadata details. | POST /v3/creative |

### Generate an upload URL

To upload your creative to a cloud storage, you need to generate a pre-signed URL. To do so, use the POST /v3/creative/generateuploadurlforaudiocreative endpoint, which generates a pre-signed AWS S3 URL by default. To upload a video creative to Azure, include `x-ms-blob-type: BlockBlob` in the header.

Here's an example of a POST /v3/creative/generateuploadurlforaudiocreative request that generates a URL:

```
{
    "AdvertiserID": "abc123",
    "FileName": "sample.m4a"
}
```

Here's an example of a POST /v3/creative/generateuploadurlforaudiocreative response, which returns a URL, the audio content type, and the `AudioUploadAttributes` attribute including the creative ID and file extension:

```
{
    "AudioUploadUrl": "https://thetradedesk-audio.s3.amazonaws.com/wwo3zpsa/abc123/v6k0kltn.m4a",
    "AudioContentType": "audio/m4a",
    "AudioUploadAttributes": {
        "AudioCreativeId": "v6k0kltn",
        "AudioCreativeExtension": "m4a"
    }
}
```

### Upload your audio creative

To upload your video creative to the URL that you generated, make the following call with the values from the response and the file name:

```
curl -v -H "content-type:{AudioContentType}" -X PUT -T Filename -L "{AudioUploadURL}"
```

Here's an example of a call:

```
curl -v -H "content-type:audio/mp4" -X PUT -T sample.m4a -L "https://thetradedesk-audio.s3.amazonaws.com/wwo3zpsa/abc123/v6k0kltn.m4a?AWSAccessKeyId=AKIAQBVJTGNIP6R6BDV2&Expires=1687980177&Signature=ChK%2B6zBXI25a6sdEAMFzAcWGKkQ%3D"
```

### Assign audio creative metadata details

After you have uploaded your audio creative to the generated URL, make a POST /v3/creative request and be sure to include the `AudioUploadAttributes` object from the `POST /v3/creative/generateuploadurlforaudiocreative` response.

Here's an example of a POST /v3/creative request for uploading an audio creative with companion creatives:

```
{
    "AdvertiserId": "abc123",
    "CreativeName": "TESTAUDIO",
    "TradeDeskHostedAudioAttributes": {
        "Description": "API Test Creative",
        "ClickthroughUrl": "https://www.xyz.com/",
        "LandingPageUrl": "https://www.xyz.com/",
        "AudioUploadAttributes": {
            "AudioCreativeId": "v6k0kltn",
            "AudioCreativeExtension": "m4a"
        },
        "CompanionCreativeIds": [
            "a6k1kltn",
            "b7k0klSn",
            "c8J0kltM"
        ]
    }
}
```

## Upload display creative hosted by The Trade Desk

The request example that follows uses a display creative with the following `ImageAttributes` object properties.

| Parameter | Description |
| --- | --- |
| `ImageContent` | The contents of the image as a base-64 encoded string. The image must be in the GIF, JPEG, or PNG format. The API automatically detects the format and the size of the image. For a full list of supported sizes, see the Ad Format API. If the format or size is not supported by The Trade Desk, the request will be rejected. This property is only used on create and will not be returned by the API. If this property is specified on update, the request will be rejected. |
| `ClickthroughUrl` | The URL to be invoked when the user clicks the ad. This may include additional click tracking. Typically, the user is redirected to the landing page after this URL is invoked. **IMPORTANT**: The click-through URL string must not exceed 600 characters. |
| `LandingPageUrl` | The URL of the page where the user is taken after clicking the ad. Must be in the form of `https://www.domain.com`. |

### Request example

Here is an example of a POST /v3/creative request body for uploading a display creative hosted by The Trade Desk:

```
{
   "AdvertiserId":"AbC123id",
   "CreativeName":"CreativeXYZ",
    "Description": "Test Creative",
    "ImageAttributes": {
        "ImageContent": "<insert Base64-encoded image string here>",
        "ClickthroughUrl": "http://www.google.com",
        "LandingPageUrl": "http://www.domain.com"
    }
}
```

### Response example

Here is an example of a POST /v3/creative response body for uploading a display creative hosted by The Trade Desk:

```
{
    "AdvertiserId": "AbC123id",
    "CreativeId": "xYz123id",
    "CreativeName": "API_TestHostedImage",
    "Description": null,
    "CreativeType": "Image",
    "ImageAttributes": {
        "AdTechnologyIds": [],
        "RightMediaOfferTypeId": 10,
        "Width": 300,
        "Height": 250,
        "ImageUrl": "https://ad.adsrvr.org/.../Image_300x250.jpeg",
        "ThirdPartyImpressionTrackingUrl": null,
        "ThirdPartyImpressionTrackingUrl2": null,
        "ThirdPartyImpressionTrackingUrl3": null,
        "ThirdPartyTrackingTags": [],
        "IsSecurable": true,
        "ClickthroughUrl": "http://thetradedesk.com",
        "LandingPageUrl": "http://thetradedesk.com",
        "AdServerName": "Other",
        "AdServerCreativeId": null
    },
    "CreativeAuditStatuses": [
        {
            "CreativeAuditor": "Google",
            "AuditStatus": "approved",
            "ReasonForStatus": "Approved"
        },
        {
            "CreativeAuditor": "AppNexus",
            "AuditStatus": "approved",
            "ReasonForStatus": null
        }
    ],
    "flightStart": null,
    "flightEnd": null,
    "Availability": "Available",
    "CreatedAtUTC": "2023-10-16T23:07:13.287",
    "LastUpdatedAtUTC": "2023-10-16T23:07:13.45",
    "ShareLink": "https://preview-desk.thetradedesk.com/Creatives/ClickTrackingPreview?CreativeId={id}&Token={token}&IsShare=True",
    "WillThisBeServedInChina": false
}
```

## Upload creative hosted by third parties

> **NOTE**:The Trade Desk automatically adds a click macro (`%%TTD_CLK%%`) to the ad tag for supported third-party ad servers.

Here's what you need to know about macros:

- If your ad does not click-through with the `%%TTD_CLK%%` macro, or if you are using an unsupported ad server, try `%%TTD_CLICK_ESC%%` instead.
- The Trade Desk click macros also support multiple escapes. This means that you can add the number of times you want to escape to the end of the macro (for example, `3` in `%%TTD_CLK_ESC3%%`).

For details, see Macros in the Knowledge Portal.

### Upload display creative

Here is an example of a POST /v3/creative request body with the `ThirdPartyTagAttributes` object properties for uploading a display creative hosted by a third party:

```
{
    "AdvertiserId":"AbC123id",
    "CreativeName":"CreativeXYZ",
    "Description": "Test Creative",
    "ThirdPartyTagAttributes": {
        "AdTag": "<Insert third-party HTML tag here>",
        "Width": 300,
        "Height": 600,
        "LandingPageUrls": [
            "http://www.domain.com"
        ],
        "AdServerName": "Celtra",
        "AdServerCreativeId": "{adservercreativeid}",
        "IsSecurable": true
    }
}
```

Here is an example of a POST /v3/creative response body for uploading a display creative hosted a third party:

```
{
    "AdvertiserId": "AbC123id",
    "CreativeId": "xYz123id",
    "CreativeName": "API_TestThirdPartyImage",
    "Description": null,
    "CreativeType": "ThirdPartyTag",
    "ThirdPartyTagAttributes": {
        "AdTag": "<a href=\"%%TTD_CLK%%http://thetradedesk.com\" target=\"_blank\"><img src=\"https://thetradedesk-support.s3.amazonaws.com/creatives/test_300x250.jpg\"></a>",
        "AdTechnologyIds": [],
        "RightMediaOfferTypeId": 10,
        "Width": 300,
        "Height": 250,
        "LandingPageUrls": [
            "http://thetradedesk.com"
        ],
        "AdServerName": "Other",
        "AdServerCreativeId": null,
        "IsSecurable": true,
        "MraidVersion": "Nonmraid",
        "ThirdPartyImpressionTrackingUrl": null,
        "ThirdPartyImpressionTrackingUrl2": null,
        "ThirdPartyImpressionTrackingUrl3": null,
        "ThirdPartyTrackingTags": []
    },
    "CreativeAuditStatuses": [
        {
            "CreativeAuditor": "Google",
            "AuditStatus": "approved",
            "ReasonForStatus": "Approved"
        },
        {
            "CreativeAuditor": "AppNexus",
            "AuditStatus": "approved",
            "ReasonForStatus": null
        }
    ],
    "flightStart": null,
    "flightEnd": null,
    "Availability": "Available",
    "CreatedAtUTC": "2023-10-16T23:07:20.027",
    "LastUpdatedAtUTC": "2023-10-16T23:07:20.197",
    "ShareLink": "https://preview-desk.thetradedesk.com/Creatives/ClickTrackingPreview?CreativeId={id}&Token={token}&IsShare=True",
    "WillThisBeServedInChina": false
}
```

### Upload video creative

Here is an example of a POST /v3/creative request to upload a video creative (based on VAST XML) with companion creatives that are hosted by a third party:

```
{
    "AdvertiserId":"AbC123id",
    "CreativeName":"CreativeXYZ",
    "Description":"Test Creative",
    "ThirdPartyHostedVideoAttributes":{
        "CompanionCreativeIds": [
            "a6k1kltn",
            "b7k0klSn",
            "c8J0kltM"
        ],
        "Duration":30,
        "LandingPageUrl":"http://www.domain.com",
        "VastXmlUrl":"<The URL of the VAST document for the video creative>"
    }
}
```

> **NOTE**: The VAST tag is automatically validated for the correct format. In some cases, you may have to specify the `Duration`, `LandingPageURL`, or `AllowIncompleteMediaFiles` properties.

## Upload creative with default impression tracking tags and URLs

Partner-level and advertiser-level default URLs and tracking tags are assigned according to the creative type that the user selects in the platform UI. The following table describes the default behavior.

| Creative Type | Default URL Behavior | Default Tag Behavior |
| --- | --- | --- |
| Display Native | The selected default URLs are assigned along with the URLs provided in the API request (Example 1). If the number of URLs exceeds the maximum limit of 3, the request will be rejected (Example 2). | Only selected default tags are assigned. |
| Video Audio | The selected default URLs are assigned as impression event trackers, along with the trackers provided in the API request (Example 4). | N/A. Users cannot apply tracking tags to video and audio creatives in the UI. |

### Examples

The examples provided in this section assume the following default tracking impression URLs and tags selected in the platform UI for video and display creatives at the partner or advertiser level.

| Creative Type | Default URL Example | DefaultTracking Tag Example |
| --- | --- | --- |
| Display | `https://SELECTED_IN_UI.1` | `<script>SELECTED_IN_UI.1</script>` |
| Video | `https://SELECTED_IN_UI.1` | N/A |

#### Example 1

Here's an example of a POST /v3/creative request snippet for a display creative with an impression tracking URL and a tracking tag provided in it.

```
{
   ...
        "ThirdPartyImpressionTrackingUrl": "https://INCLUDED_IN_REQUEST.1",
        "ThirdPartyImpressionTrackingUrl2": null,
        "ThirdPartyImpressionTrackingUrl3": null,
        "ThirdPartyTrackingTags": [
            "<script>INCLUDED_IN_REQUEST.1</script>"
         ]
   ...
}
```

Here's a snippet of a successful response, which includes the default URL selected in the UI and the one provided in the request.

```
{
   ...
        "ThirdPartyImpressionTrackingUrl": "https://SELECTED_IN_UI.1",
        "ThirdPartyImpressionTrackingUrl2": "https://INCLUDED_IN_REQUEST.1",
        "ThirdPartyImpressionTrackingUrl3": null,
        "ThirdPartyTrackingTags": [
            "<script>INCLUDED_IN_REQUEST.1</script>"
         ]
   ...
}
```

#### Example 2

Here's an example of a POST /v3/creative request snippet for a display creative with three impression tracking URLs and a tracking tag provided in it.

```
{
   ...
        "ThirdPartyImpressionTrackingUrl": "https://INCLUDED_IN_REQUEST.1",
        "ThirdPartyImpressionTrackingUrl2": "https://INCLUDED_IN_REQUEST.2",
        "ThirdPartyImpressionTrackingUrl3": "https://INCLUDED_IN_REQUEST.3",
        "ThirdPartyTrackingTags": [
            "<script>INCLUDED_IN_REQUEST.1</script>"
         ]
   ...
}
```

> **IMPORTANT**: Since the total number of the URLs provided in the request and those inherited from the advertiser or partner (through the selections in the UI) exceeds the maximum limit of 3 URLs, the request is rejected.

#### Example 3

Here's an example of a POST /v3/creative request snippet for a display creative with only impression tracking URL provided in it (with no tracking tag).

```
{
     ...
        "ThirdPartyImpressionTrackingUrl": "https://INCLUDED_IN_REQUEST.1",
        "ThirdPartyImpressionTrackingUrl2": null,
        "ThirdPartyImpressionTrackingUrl3": null
     ...
}
```

Here's a snippet of a successful response, which includes the default URL selected in the UI, the URL provided in the request, and the default tracking tag selected in the UI.

```
{
     ...
        "ThirdPartyImpressionTrackingUrl": "https://SELECTED_IN_UI.1",
        "ThirdPartyImpressionTrackingUrl2": "https://INCLUDED_IN_REQUEST.1",
        "ThirdPartyImpressionTrackingUrl3": null,
        "ThirdPartyTrackingTags": [
            "<script>SELECTED_IN_UI.1</script>"
         ]
     ...
}
```

#### Example 4

Here's an example of a POST /v3/creative request snippet for a video creative with an impression tracking URL provided in it.

```
{   ...
        "TrackingEvents": [
             {
                 "EventType": "impression",
                 "EventUrl": "https://INCLUDED_IN_REQUEST.1"
             }
        ]
   ...
}
```

Here's a snippet of a successful response, which includes the default URL selected in the UI and the one provided in the request.

```
{   ...
        "TrackingEvents": [
             {
                 "EventType": "impression",
                 "EventUrl": "https://INCLUDED_IN_REQUEST.1"
             },
             {
                 "EventType": "impression",
                 "EventUrl": "https://SELECTED_IN_UI.1"
             }
        ]
   ...
}
```
