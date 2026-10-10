# Reporting Best Practices & Architecture Guide

## Overview

The Trade Desk (TTD) provides two distinct reporting paradigms for programmatic campaigns:
1. **Synchronous Tile API (GraphQL `SwedishCampaignReporting`)**: High-speed, real-time dashboard analytics built on OLAP tiles.
2. **Asynchronous Batch API (REST `My Reports` / HD Reports)**: Comprehensive, offline batch generation delivering complete dimensional data via CSV/TSV delivery.

Understanding the operational boundaries, data propagation latency, and fallback mechanisms between these two engines is critical for maintaining reporting data integrity across platform UI layers.

---

## Architecture Comparison: Tile API vs. My Reports

| Capability | Synchronous Tile API (`SwedishCampaignReporting`) | Asynchronous Batch API (`My Reports`) |
| :--- | :--- | :--- |
| **Protocol** | GraphQL (Tile Cube Rollups) | REST (`/v3/myreports/reportschedule`) |
| **Response Latency** | Sub-second to 2-3 seconds | Minutes (asynchronous execution) |
| **Dimension Depth** | Time, General, Basic Publisher | Full dimensional fidelity (Publisher, Domain, Deal, Ad Group, Creative, Device) |
| **Pagination & Limits** | 1,000 nodes per connection | No pagination caps (Full CSV/TSV batch files) |
| **Publisher Granularity** | Subject to tile indexing lag (up to 24-48h for older flights or sandbox) | Complete historical breakdown across entire campaign flight |
| **Primary Use Case** | Interactive platform charts, live pacing, time-of-day distribution | Auditing, billing reconciliation, publisher delivery verification |

---

## Dimensional Data Lag & Fallback Architecture

### Root Cause of Synchronous Publisher Lag
In the TTD Kokai infrastructure:
1. **General Metric Propagation**: Campaign impressions, gross spend, bids, and video completions propagate rapidly into core campaign summary tiles.
2. **Publisher Dimension Indexing**: Publisher property dimensions (`dimensions.publisherProperty.name`) require dimensional joining against supply-path metadata cubes. In sandbox environments or flights outside active retention windows, the Tile API `publisherReporting` connection may return 0 nodes while `generalReporting` returns complete day-level impressions.

### Safe Consumer Invariants (Stale-While-Revalidate)
To prevent collapsing verified historical publisher records into fallback rows (e.g. `Airspot Performance Network`) upon report refresh:
1. **Never Evict Cache Upfront**: Do not delete existing cached reports prior to background sync. Keep serving the stale cached payload while revalidation proceeds.
2. **Granular-Preserving Merge**:
   - If an incoming day slice contains genuine publisher nodes (`Discovery+`, `MAX`, `Amazon Prime Video`), adopt the fresh breakdown.
   - If an incoming day slice returns 0 publisher nodes and produces only a fallback aggregate row, check existing records for that date. If verified granular publishers exist, **preserve existing granular records** rather than overwriting with the fallback aggregate.
3. **Database Rehydration**: Ensure all granular performance records (`performanceRecords`) are persisted to PostgreSQL and rehydrated during cache misses.

---

## My Reports REST API Workflow

For exhaustive offline reporting or historical publisher reconciliation, platforms should utilize the asynchronous My Reports workflow:

### Step 1: Query Report Templates
Identify available report templates and required headers:
- `GET /v3/myreports/reporttemplate/facets`
- `POST /v3/myreports/reporttemplateheader/query`

### Step 2: Create Report Schedule
Schedule an asynchronous report execution:
- **Endpoint**: `POST /v3/myreports/reportschedule`
- **Payload Example**:
  ```json
  {
    "ReportScheduleName": "Campaign Publisher Delivery Audit",
    "ReportTemplateId": 1,
    "ReportScheduleType": "OneTime",
    "Timezone": "UTC",
    "ReportStartDateInclusive": "2026-05-01",
    "ReportEndDateExclusive": "2026-06-01",
    "AdvertiserIds": ["1ccsex3"],
    "CampaignIds": ["cvbox9d"],
    "ReportDelivery": {
      "DeliveryType": "Link"
    }
  }
  ```

### Step 3: Monitor Execution Status
Query the execution status for the advertiser:
- **Endpoint**: `POST /v3/myreports/reportexecution/query/advertisers`
- Poll until `ExecutionStatus` transitions from `InQueue` / `Executing` to `Complete`.

### Step 4: Retrieve Download URL & Ingest
Once completed, extract the delivery URL from `ReportDeliveries[0].DownloadUrl` and stream the CSV/TSV data into analytical storage.
