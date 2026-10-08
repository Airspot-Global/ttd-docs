#!/usr/bin/env node

/**
 * verify-ttd-docs.js
 * Programmatic verification script for ttd-docs repository integrity.
 */

const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '..');

const REQUIRED_FILES = [
  'GraphQL/advertiser_create.md',
  'GraphQL/advertiser_queries.md',
  'Guides/campaign_creation_payload.md',
  'Guides/campaign_connector.md',
  'Guides/campaigns.md',
  'Guides/cross_device.md',
  'Guides/forecasting_api.md',
  'Guides/seeds.md',
  'REST_API/ad_group.md',
  'REST_API/campaign.md',
  'REST_API/forecast.md',
  'REST_API/universal_forecasting.md',
  'taxonomy.json',
];

const REQUIRED_ASSERTIONS = [
  {
    file: 'Guides/cross_device.md',
    contains: ['deprecated on 2026 January 12', 'AdBrainHouseholdCrossDeviceEnabled', 'Identity Alliance', 'CrossDeviceVendorId'],
    desc: 'Cross-Device 2026 Deprecations and Identity Alliance'
  },
  {
    file: 'REST_API/ad_group.md',
    contains: ['HTTP 410 Gone', 'AdBrainHouseholdCrossDeviceEnabled was deprecated on 2026 January 12', 'Identity Alliance'],
    desc: 'Ad Group REST API 410 Gone Deprecation notice'
  },
  {
    file: 'Guides/seeds.md',
    contains: ['campaignUpdateSeed', '405 Method Not Allowed', 'Deprecated REST Endpoint'],
    desc: 'Kokai Seed GraphQL mutation and bulksettings 405 notice'
  },
  {
    file: 'REST_API/campaign.md',
    contains: ['put[/v3/campaign/bulksettings]', 'HTTP 405 Method Not Allowed', 'campaignUpdateSeed'],
    desc: 'Campaign REST API 405 Method Not Allowed bulksettings warning'
  },
  {
    file: 'Guides/campaign_creation_payload.md',
    contains: ['Creative Association & Variation Linking', 'status: AVAILABLE', 'Draft vs Launch Rules'],
    desc: 'Section 7 Creative Linking and Kokai AVAILABLE status enum'
  },
];

console.log('=== Running TTD Docs Verification ===\n');

let hasError = false;

// 1. Verify existence of required files
console.log('1. Checking required files existence...');
for (const relPath of REQUIRED_FILES) {
  const fullPath = path.join(ROOT_DIR, relPath);
  if (!fs.existsSync(fullPath)) {
    console.error(`  [FAIL] Missing required file: ${relPath}`);
    hasError = true;
  } else {
    console.log(`  [PASS] Found: ${relPath}`);
  }
}

// 2. Check for unwanted hardcoded home paths in markdown files
console.log('\n2. Scanning for hardcoded local user paths in markdown files...');
const docDirs = ['GraphQL', 'Guides', 'REST_API'];
for (const dir of docDirs) {
  const dirPath = path.join(ROOT_DIR, dir);
  if (!fs.existsSync(dirPath)) continue;
  const files = fs.readdirSync(dirPath).filter(f => f.endsWith('.md'));
  for (const f of files) {
    const fullPath = path.join(dirPath, f);
    const content = fs.readFileSync(fullPath, 'utf8');
    if (content.includes('abdessamadmisbah') || content.includes('file:///Users/')) {
      console.error(`  [FAIL] Hardcoded local path found in: ${dir}/${f}`);
      hasError = true;
    }
  }
}
if (!hasError) {
  console.log('  [PASS] No hardcoded local paths found.');
}

// 3. Verify specific content assertions
console.log('\n3. Verifying key deprecations and Kokai content assertions...');
for (const check of REQUIRED_ASSERTIONS) {
  const fullPath = path.join(ROOT_DIR, check.file);
  if (!fs.existsSync(fullPath)) continue;
  const content = fs.readFileSync(fullPath, 'utf8');
  for (const str of check.contains) {
    if (!content.includes(str)) {
      console.error(`  [FAIL] ${check.file} missing required substring: "${str}" (${check.desc})`);
      hasError = true;
    }
  }
  if (!hasError) {
    console.log(`  [PASS] Verified assertions in: ${check.file} (${check.desc})`);
  }
}

// 4. Validate taxonomy.json
console.log('\n4. Validating taxonomy.json structure...');
try {
  const taxPath = path.join(ROOT_DIR, 'taxonomy.json');
  const taxData = JSON.parse(fs.readFileSync(taxPath, 'utf8'));
  const count = Array.isArray(taxData) ? taxData.length : Object.keys(taxData).length;
  if (count < 100) {
    console.error(`  [FAIL] taxonomy.json has unexpectedly few records: ${count}`);
    hasError = true;
  } else {
    console.log(`  [PASS] taxonomy.json parsed successfully (${count} entries).`);
  }
} catch (e) {
  console.error(`  [FAIL] Failed to parse taxonomy.json: ${e.message}`);
  hasError = true;
}

console.log('\n=======================================');
if (hasError) {
  console.error('TTD Docs verification FAILED. Please fix the above errors.');
  process.exit(1);
} else {
  console.log('All TTD Docs verification checks PASSED successfully!');
  process.exit(0);
}
