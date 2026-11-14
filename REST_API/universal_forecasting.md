# Universal Forecasting

- Source: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/area/Universal%20Forecasting
- Legacy source: https://partner.thetradedesk.com/v3/portal/api/area/Universal%20Forecasting (retired)
- Retrieved: 2026-11-14 (endpoint list from the pre-refresh copy; the live area page is drawn in the browser, so only its endpoint links were checked against the sitemap)
- Category: REST_API

---

## Operations and endpoints

### POST /v3/universalforecasting/generate

<!-- airspot:begin anchor="POST /v3/universalforecasting/generate" -->
> **Airspot note (observed 2026-11-09, sandbox + production; not in TTD's official docs):** This page only links to the reference. The shape below is what we send and what came back. It is not a complete field list.
>
> **Request fields we send:**
> - `AdvertiserId`, `StartDate`, `EndDate` (ISO 8601), `TimeWindow` (days), `Budget`.
> - `RTBAttributes.MaxBidCPM { Amount, CurrencyCode }`.
> - `Targeting.DemographicTargeting.AgeRangeTargeting.AgeRanges` (for example `["25-34", ...]`).
> - `UseCtvCrossDevice: true`.
> - `UniversalForecastingBidLists: [{ Name, BidListAdjustmentType: "TargetList", BidLines: [{ DeviceType: "ConnectedTV" }] or [{ GeoSegmentId }] }]`, one dimension per list.
> - `AverageBidCPMInAdvertiserCurrency`, `GenerateBudgetPoints: true`, and optionally `AudienceId`.
>
> **Response:**
> - Top-level keys: `AdvertiserId`, `LastCalculatedAt` (always `0001-01-01T00:00:00`), `TimeWindow`, `MetricResults`, `PrivateContractMetricResults`, `PrivateContractGroupMetricResults`, `PrivateContractMetricGeoResults`, `AverageBidCPMInAdvertiserCurrency`, `TargetKnownUsers`, `Audience`, `BudgetMetrics`.
> - `MetricResults[]` items are `{ InsightMetricType, RangeStart, RangeEnd, IsCurrency }`. Types seen: `Impressions`, `Spend`, `ReachHousehold`, `ReachPeople`, `ReachUsers`, `FrequencyHousehold`, `FrequencyPeople`, `FrequencyUsers`.
> - `BudgetMetrics` has 301 points. Each point is an array of the same metric objects. Spend and impressions run linearly from 0 to the full forecast supply, so each step is about 1/300 of the total supply spend. From the 2nd point on, the figures are already at full-supply scale, so the curve is coarse for small budgets.
> - `AverageBidCPMInAdvertiserCurrency` is echoed back unchanged, even for a bid 10× lower than usual. We never saw it differ from the bid sent.
> - With `AudienceId`, the echoed `Audience` block has every count `null`.
>
> **Behaviour:**
> - In production, a 10× lower bid kept about 75% of the forecast impressions.
> - In production, people ÷ households is about 1.01.
> - The **sandbox returns synthetic numbers.** We saw 45–57 ads per household per week, and impressions that barely react to the bid. Do not use sandbox forecasts as market figures.
> - REST responses carry no rate-limit headers. They include `Access-Control-Allow-Origin`, so browsers can call the endpoint directly.
<!-- airspot:end -->

Reference: https://open.thetradedesk.com/advertiser/docsApp/AdvertiserReferences/api/ref/post-universalforecasting-generate

Generate a forecast based on the data available at the time the forecast is requested. Because available data changes as time passes, forecasts generated with the same parameters at different times return unique results optimized for each point in time.
