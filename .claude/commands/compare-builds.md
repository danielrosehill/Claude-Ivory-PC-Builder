# Compare Builds

Compare multiple build configurations side by side.

## Instructions

1. Scan the `builds/` directory for all builds with `suggested-build.md` files
2. Extract key information from each:
   - Total cost
   - CPU choice
   - Platform (Intel/AMD)
   - Form factor
   - Key features
3. Present a comparison table

## Output Format

```markdown
# Build Comparison

| Aspect | Build 1 | Build 2 | Build N |
|--------|---------|---------|---------|
| **Use Case** | ... | ... | ... |
| **CPU** | ... | ... | ... |
| **Platform** | Intel/AMD | Intel/AMD | ... |
| **Form Factor** | ATX/mATX/ITX | ... | ... |
| **Total Cost** | ₪X,XXX | ₪X,XXX | ... |

## Analysis

[Brief analysis of trade-offs between builds]
```

If no builds exist yet, report that and suggest creating one with `/generate-build`.
