# Use Catalog

Switch to a specific historical catalog version.

## Arguments

- `$ARGUMENTS` - The catalog timestamp/directory name (e.g., "2026-02-05_13-43-00")

## Instructions

1. Verify the specified catalog exists in `catalog/`
2. Update the `catalog/current` symlink to point to the specified version
3. Confirm the switch

## Execution

```bash
cd catalog
rm -f current
ln -s "$ARGUMENTS" current
```

## Output

Report:
- Previous catalog version
- New catalog version
- Product count in new catalog
- Timestamp of new catalog

## Notes

This allows using historical pricing data for builds. Useful for:
- Comparing prices over time
- Recreating a build spec from a specific date
- Rolling back if a scrape had issues
