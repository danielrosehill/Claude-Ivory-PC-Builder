# Search Catalog

Search for products across all catalog categories.

## Arguments

- `$ARGUMENTS` - Search query (product name, ID, or keywords)

## Instructions

1. Load all JSON files from `catalog/current/`
2. Search for matches in:
   - Product name (partial match, case-insensitive)
   - Product ID (exact match)
3. Return matching products with prices

## Output Format

```markdown
# Search Results: "$ARGUMENTS"

Found XX products matching "$ARGUMENTS"

| Category | Product | Price (ILS) | ID | Link |
|----------|---------|-------------|-----|------|
| Intel CPUs | Intel Core i7-14700F... | ₪1,250 | 85530 | [Link] |
| ... | ... | ... | ... | ... |

## Price Range
- Lowest: ₪X,XXX - [Product Name]
- Highest: ₪X,XXX - [Product Name]
- Average: ₪X,XXX
```

## Tips

Search examples:
- `i7` - Find all Intel Core i7 processors
- `DDR5` - Find DDR5 memory
- `Mini-ITX` - Find Mini-ITX cases/motherboards
- `2.5G` - Find 2.5G network equipment
