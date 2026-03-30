
const fs = require('fs');
const path = require('path');

const tsvPath = '/Users/abdessamadmisbah/Documents/DBA/Airspot/App/ttd-documentation/ttd-api-docs/taxonomy.tsv';
const jsonPath = '/Users/abdessamadmisbah/Documents/DBA/Airspot/App/ttd-documentation/ttd-api-docs/taxonomy.json';

try {
    const data = fs.readFileSync(tsvPath, 'utf8');
    const lines = data.split(/\r?\n/);

    // According to the file content view:
    // Line 1: Relational ID System ...
    // Line 2: Unique ID	Parent	Name	Tier 1	Tier 2	Tier 3	Tier 4

    const headers = lines[1].split('\t').map(h => h.trim());

    const idIdx = headers.indexOf('Unique ID');
    const nameIdx = headers.indexOf('Name');
    const tier1Idx = headers.indexOf('Tier 1');
    const tier2Idx = headers.indexOf('Tier 2');

    if (idIdx === -1 || nameIdx === -1 || tier1Idx === -1 || tier2Idx === -1) {
        console.error('Missing required headers in TSV');
        process.exit(1);
    }

    const results = [];

    // Start from line index 2 (third line)
    for (let i = 2; i < lines.length; i++) {
        const line = lines[i].trim();
        if (!line) continue;

        const columns = lines[i].split('\t');
        if (columns.length <= Math.max(idIdx, nameIdx, tier1Idx, tier2Idx)) continue;

        const entry = {
            id: columns[idIdx]?.trim() || '',
            Name: columns[nameIdx]?.trim() || '',
            'Taxonomy Tier 1': columns[tier1Idx]?.trim() || '',
            'Taxonomy Tier 2': columns[tier2Idx]?.trim() || ''
        };

        // Only push if there's an ID or Name
        if (entry.id || entry.Name) {
            results.push(entry);
        }
    }

    fs.writeFileSync(jsonPath, JSON.stringify(results, null, 2));
    console.log(`Successfully converted ${results.length} entries to ${jsonPath}`);

} catch (error) {
    console.error(`Error during conversion: ${error.message}`);
    process.exit(1);
}
