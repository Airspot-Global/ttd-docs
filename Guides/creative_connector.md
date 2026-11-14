# Creative connector

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/CreativeConnector
- Retrieved: 2026-11-14
- Category: Guides

---

# Creative connector

If you host creative data on a third-party ad server or your own internal database, you can build a Creative connector integration to push your ad tags to The Trade Desk platform. Automating your creative-upload process with The Trade Desk API reduces the time it takes to bulk upload creatives into the platform and eliminates human error in trafficking.

The following diagram illustrates the workflow schema.

> **TIP**: To begin testing the integration process, download the sample code in Python, which demonstrates the call pattern and best practices for this use case.

## Integration

The typical Creative connector build involves interactions with a suite of creative endpoints. The following table lists the high-level tasks.

| Task | Endpoint | Notes | Further Reference |
| --- | --- | --- | --- |
| Authenticate | POST /v3/authentication | Short-lived tokens are recommended. | Authentication |
| Retrieve advertisers | POST /v3/advertiser/query/partner | N/A | Create advertiser |
| Upload creatives | POST /v3/creative POST creative/generateuploadurlforvideocreative | Creatives hosted by The Trade Desk: - Display - HTML5 - Video Creatives hosted by third parties: - Display - Video | Creatives |

### Retrieve advertisers

Before uploading creatives, retrieve a list of all advertisers available to a partner to make sure that you are associating your ad tag to the correct advertiser.

Here's an example of a POST /v3/advertiser/query/partner request body that allows you retrieve a list of advertisers sorted by name for the specified partner ID:

```
{
   "PartnerId":"XyZ123id",
   "SortFields":[
      {
         "FieldId":"Name",
         "Ascending":true
      }
   ],
   "Availabilities":[
      "Available"
   ],
   "PageStartIndex":0,
   "PageSize":100
}
```

### Upload creatives

The Trade Desk curates inventory across display, video, mobile, audio, native, and connected TV. For details on the creative offerings, available macros, and supported third-party ad servers, see Ad Content Guidelines in the Knowledge Portal. When your creatives are uploaded or updated, they are auto-submitted to various supply vendors (Google, App-Nexus, and others) for approval. No ad group can spend unless the creative is approved.

The POST/PUT creative endpoints are fairly straightforward in their structures. Each creative type has a dedicated attribute subsection where you will be required to define the variables relevant to the creative type. When using these endpoints, use only one attribute subsection per creative.

The following sections provide examples of how to upload each creative format:

-

Creatives hosted by The Trade Desk:

  - Display
  - HTML5
  - Video

-

Creatives hosted by third parties:

  - Display
  - Video

> **IMPORTANT**: While you can upload creatives with non-secured URLs (http), secured URLs (https) are recommended. Most SSPs reject creatives with non-secured URLs, thus preventing spend.

#### The trade desk-hosted display creatives

Here is an example of a POST /v3/creative request body for uploading a display creative hosted by The Trade Desk:

```
{
   "AdvertiserId":"AbC123id",
   "CreativeName":"CreativeXYZ",
   "Description":"Test Creative",
   "ImageAttributes":{
      "ImageContent":"<insert base-64-encoded image string here>",
      "ClickthroughUrl":"http://www.google.com",
      "LandingPageUrl":"http://www.domain.com"
   }
}
```

#### The trade desk-hosted HTML5 creatives

> **IMPORTANT**: If all information for serving the creative is contained in a single HTML file, use the `HtmlFileContent` attribute. To upload creatives that consist of multiple files, use the `ZipArchiveContent` attribute.

Here is an example of a POST /v3/creative request payload for uploading an HTML5 creative hosted by The Trade Desk:

```
{
   "AdvertiserId":"AbC123id",
   "CreativeName":"CreativeXYZ",
   "Description":"Test Creative",
   "Html5Attributes":{
      "HtmlFileContent":"<insert contents of an HTML file as a base-64-encoded string here>",
      "Width":300,
      "Height":250,
      "ClickthroughUrl":"http://www.google.com",
      "LandingPageUrl":"http://www.domain.com",
      "ClickTrackingParameterName":"<insert case-sensitive click-tracking parameter used in the HTML file here>"
   }
}
```

#### The trade desk-hosted video creatives

To upload a video hosted by The Trade Desk, complete the following steps:

1. Generate a pre-signed URL with the POST creative/generateuploadurlforvideocreative endpoint, which returns the creative ID and its extension in the `VideoUploadAttributes` attribute in the response.
2. Upload your video creative to the URL that you generated and be sure to include your file name and the `content-type` value from the response. For details and examples, see Creatives.
3. Use the POST /v3/creative endpoint and be sure to include the `VideoUploadAttributes` object from the POST creative/generateuploadurlforvideocreative response.

Here is an example of a POST /v3/creative request body for uploading a video creative hosted by The Trade Desk:

```
{
   "AdvertiserId":"AbC123id",
   "CreativeName":"CreativeXYZ",
   "Description":"Test Creative",
   "TradeDeskHostedVideoAttributes":{
      "VideoUploadAttributes":{ // These are the attributes returned by the POST creative/generateuploadurlforvideocreative API.
         "VideoCreativeId":"123XYZid",
         "VideoCreativeExtension":"mp4"
      },
      "ClickthroughUrl":"http://www.google.com",
      "LandingPageUrl":"http://www.domain.com"
   }
}
```

#### Third-party-hosted display creatives

The Trade Desk automatically adds a click macro (`%%TTD_CLK%%`) to the ad tag for supported third-party ad servers. Here's what you need to know about macros:

- If your ad does not click-through with the `%%TTD_CLK%%` macro, or if you are using an unsupported ad server, try `%%TTD_CLICK_ESC%%` instead.
- The Trade Desk click macros also support multiple escapes. This means that you can add the number of times you want to escape to the end of the macro (for example, `3` in `%%TTD_CLK_ESC3%%`).

For details, see Macros in the Knowledge Portal.

Here is an example of a POST /v3/creative request to upload a display creative hosted by a third party:

```
{
   "AdvertiserId":"AbC123id",
   "CreativeName":"CreativeXYZ",
   "Description":"Test Creative",
   "ThirdPartyTagAttributes":{
      "AdTag":"<insert the third party HTML tag here>",
      "Width":300,
      "Height":600,
      "LandingPageUrls":[
         "http://www.domain.com"
      ],
      "AdServerName":"GenericInc123",
      "AdServerCreativeId":"12344321",
      "IsSecurable":true
   }
}
```

#### Third-party-hosted video creatives

Here is an example of a POST /v3/creative request to upload a video creative (based on VAST XML) hosted by a third party:

```
{
   "AdvertiserId":"AbC123id",
   "CreativeName":"CreativeXYZ",
   "Description":"Test Creative",
   "ThirdPartyHostedVideoAttributes":{
      "VastXmlUrl":"<insert The URL of the VAST document that describes the video creative here>",
      "Duration":30,
      "LandingPageUrl":"http://www.domain.com"
   }
}
```

> **NOTE**: The VAST tag is automatically validated for the correct format. In some cases, you may have to specify `Duration`, `LandingPageURL`, or the `AllowIncompleteMediaFiles` properties.

## Additional tasks

The Creative connector integration is not a predefined set of tasks. You may design your integration to automate other processes that impact the efficiency of your day-to-day operations. For example, some partners want to monitor the performance of their ad groups and campaigns by using the My Reports endpoints to download insights. For details, see the following:

- Create and manage report schedules
- Campaign connector

You may also associate your uploaded creatives with your strategies with the PUT /v3/adgroup or POST /v3/adgroup endpoints.
