# Price Check

Check the current price of a specific product by ID or name.

## Arguments

- `$ARGUMENTS` - Product ID or partial name

## Instructions

1. Search current catalog for the product
2. If multiple matches, list all with prices
3. If historical catalogs exist, show price history

## Output Format

```markdown
# Price Check: $ARGUMENTS

## Current Price
**[Product Name]**
- Price: ₪X,XXX
- Category: [Category]
- ID: [ID]
- Link: [URL]

## Price History (if available)
| Date | Price | Change |
|------|-------|--------|
| 2026-02-05 | ₪1,250 | - |
| 2026-02-01 | ₪1,300 | -₪50 |
| ... | ... | ... |

## Similar Products
| Product | Price | Difference |
|---------|-------|------------|
| [Alternative 1] | ₪X,XXX | +₪XXX |
| [Alternative 2] | ₪X,XXX | -₪XXX |
```
