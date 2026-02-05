# Catalog History

List all historical catalog scrapes with details.

## Instructions

1. Read `catalog/manifest.json` for complete history
2. List all runs chronologically
3. Optionally compare product counts between runs

## Arguments

- `$ARGUMENTS` - Optional: "compare" to show changes between runs

## Output Format

```markdown
# Catalog Scrape History

| # | Timestamp | Products | Categories | Directory |
|---|-----------|----------|------------|-----------|
| 1 | 2026-02-05 13:43 | 523 | 16 | 2026-02-05_13-43-00 |
| 2 | 2026-02-06 10:00 | 531 | 16 | 2026-02-06_10-00-00 |
| ... | ... | ... | ... | ... |

## Notes
- Current catalog: [timestamp]
- Total historical snapshots: XX
```

If "compare" argument provided, also show:
```markdown
## Changes (Latest vs Previous)
- Products added: +XX
- Products removed: -XX
- Price changes: XX products
```
