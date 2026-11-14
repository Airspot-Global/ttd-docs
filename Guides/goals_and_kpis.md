# Goals and KPIs

- Source: https://open.thetradedesk.com/advertiser/docsApp/GuidesAdvertiser/api/doc/GoalsKPIs
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/doc/GoalsKPIs (retired)
- Retrieved: 2026-11-14
- Category: Guides

---

# Goals and KPIs

A KPI, or key performance indicator, is a metric that enables you to measure the success of your ad campaigns, while driving performance and delivering results. You can set goals at the campaign and ad group level. If enabled, Koa Optimizations uses your ad group goals to select and prioritize the best-performing and most relevant inventory, making sure that the right price is paid on impressions.

The following table lists the available goals.

| Goal | Has Target? | Description | Goal Object Property | Supported by Koa Optimizations? |
| --- | --- | --- | --- | --- |
| Reach | No | This is a broad goal without any specific metrics used as primary benchmarks. Choose this goal if you want to reach as many unique users as possible in your intended audience given your specified base bid, max bid, and any bid adjustments. | `MaximizeReach` | Yes |
| Incremental Reach | No | Maximize the number of unique viewers beyond those who have already been reached through linear TV. This goal prioritizes spend toward CTV PMP deals that improve unique or incremental reach of the ad group and deprioritize spends toward PMP deals that do the opposite. | `MaximizeLtvIncrementalReach` | Yes |
| CPC | Yes, currency amount | _Cost per click_. The amount the advertiser pays every time an ad is clicked. If your primary engagement metric is clicks, you may want to choose CPC as your goal. See also the CTR goal. | `CPCInAdvertiserCurrency` | Yes |
| CPA | Yes, currency amount | _Cost Per Acquisition_. The amount the advertiser pays based on the number of "acquisitions" (conversions) made. If your goal is a specific action like a purchase or a newsletter sign up, you may want to choose CPA as your goal. | `CPAInAdvertiserCurrency` | Yes |
| vCPM | Yes, currency amount | (Estimated) _Viewable Cost Per Mille_ (thousand). Setting this goal optimizes based on the cost of _viewable_ inventory. vCPM is calculated by dividing eCPM by the in-view rate (vCPM = eCPM / in-view rate). Unlike the Viewability goal, which optimizes toward an entered in-view target percentage, vCPM optimizes to inventory that is effective in terms of its viewable cost. | `VCPMInAdvertiserCurrency` | Yes |
| CPCV | Yes, currency amount | _Cost Per Completed View_. The amount the advertiser pays after a video has been viewed all the way through. Set this goal if your campaign is using video creatives and you want to encourage immediate engagement. This is a great option for brand-focused advertisers. | `CPCVInAdvertiserCurrency` | Yes |
| ROAS | Yes, percentage | _Return On Ad Spend_. The ratio of total revenue compared to total spend. Set this ROI-type of goal when you can pass specific revenue amounts to the platform in your conversion pixel. | `ReturnOnAdSpendPercent` | Yes |
| CTR | Yes, percentage | _Click Through Rate_. It is calculated by dividing the number of clicks by the number of impressions. A high CTR indicates a more successful campaign. This alternative to CPC does not consider the cost of the media, but only how often a user clicks an ad. | `CTRInPercent` | Yes |
| VCR | Yes, percentage | _Video Completion Rate_. This goal allows optimization toward inventory where ads are viewed or heard to completion. | `VCRInPercent` | Yes |
| Viewability | Yes, percentage | Viewability is a metric that measures whether an ad impression has been viewed by a website user rather than simply being displayed. Unlike the vCPM goal, which optimizes based on the cost of viewable inventory, Viewability optimizes toward an entered in-view target percentage. | `ViewabilityInPercent` | No |
| Nielsen OTP | Yes, percentage | Nielsen _On Target Percentage_. Setting this goal helps you optimize toward a percentage of impressions delivered to a chosen demographic (out of the total number of impressions served during your campaign). Nielsen sets different percentage benchmarks for different demographics and different regions. Nielsen's suggested benchmarks can be found on their website. You can also contact your Account Manager to get a better sense of what your percentage should be. When set, the demographic must be provided in the form of `NielsenTrackingAttributes` or you must set `TargetDemographicSettingsEnabled` to `true`. If you select this goal, fees for Nielsen reporting may apply. | `NielsenOTPInPercent` | No |
| Miaozhen OTP | Yes, percentage | Miaozhen _On Target Percentage_. Setting this goal will help you optimize toward a percentage of impressions delivered to a chosen demographic (out of the total number of impressions served during your campaign). When set, the demographic must be provided in `MiaozhenTrackingAttributes`. If you select this goal, reporting fees may apply. | `MiaozhenOTPInPercent` | No |

> **NOTE**: Some goals may require special permissions. If needed, contact your Account Manager for appropriate access.

## FAQs

The following is a list of frequently asked questions about goals and KPIs for campaigns and ad groups.

### How are ad group KPIs set when there are multiple campaign goals?

The primary campaign goal becomes the default KPI for all ad groups in the campaign.

### What happens if no ad groups meet their KPI targets?

In Kokai-budgeted campaigns, the platform optimizes bidding and allocates budget based on the primary campaign goal. Secondary and tertiary goals do not affect optimization or budget allocation, but you can use them to track additional KPIs in reporting.

In Solimar-budgeted campaigns that use AutoAllocator with Auto Prioritization, the platform ranks ad groups by the primary campaign goal. Ad groups that surpass the primary goal are then ranked by the secondary goal, and then by the tertiary goal. Secondary and tertiary goals do not affect bidding.

### How often are rankings/priorities updated?

For Solimar-budgeted campaigns that use Auto Prioritization, the platform updates rankings every other day, after a 24-hour data collection cycle.
