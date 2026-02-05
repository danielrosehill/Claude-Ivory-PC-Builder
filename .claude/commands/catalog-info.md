# Catalog Info

Display information about the current catalog and scrape history.

## Instructions

1. Read `catalog/manifest.json` for scrape history
2. Read `catalog/current/summary.json` for current catalog details
3. Display:
   - Current catalog timestamp
   - Total products in current catalog
   - Number of historical scrape runs
   - Categories available

## Output Format

```markdown
# Catalog Information

## Current Catalog
- **Timestamp**: YYYY-MM-DD HH:MM:SS
- **Products**: X,XXX total
- **Categories**: XX

## Category Breakdown
| Category | Products |
|----------|----------|
| Intel CPUs | XX |
| AMD CPUs | XX |
| ... | ... |

## Scrape History
- Total runs: XX
- First scrape: YYYY-MM-DD
- Latest scrape: YYYY-MM-DD

## Recent Runs
| Date | Products | Duration |
|------|----------|----------|
| ... | ... | ... |
```
