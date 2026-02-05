# Generate Build

Generate a suggested PC build specification based on requirements.

## Arguments

- `$ARGUMENTS` - The build number (e.g., "1" for builds/1/)

## Instructions

1. Read the task file at `builds/$ARGUMENTS/task.md`
2. Load relevant catalog data from `catalog/*.json`
3. Analyze requirements:
   - Use case and workload requirements
   - Existing components to reuse
   - Constraints (size, budget, features)
4. Select compatible components:
   - Match CPU socket to motherboard
   - Match RAM type to motherboard (DDR4/DDR5)
   - Ensure case fits motherboard form factor
   - Check PSU wattage is adequate
   - Verify cooler clearance in case
5. Generate the build specification

## Output

Write the suggested build to `builds/$ARGUMENTS/suggested-build.md` using this format:

```markdown
# Suggested Build: [Build Name]

Generated: [Date]
Based on: builds/$ARGUMENTS/task.md

## Summary
[Brief description of design choices]

## Components

| Component | Product | Price (ILS) | Link |
|-----------|---------|-------------|------|
| CPU | [Name] | ₪X,XXX | [Link] |
| Motherboard | [Name] | ₪X,XXX | [Link] |
| CPU Cooler | [Name] | ₪X,XXX | [Link] |
| Case | [Name] | ₪X,XXX | [Link] |
| [etc.] | | | |

**Total (New Components): ₪X,XXX**

## Compatibility Notes
- [Socket compatibility]
- [Form factor compatibility]
- [Power requirements]

## Existing Components Used
- [List from task.md]

## Alternative Options
- [Component]: [Alternative] (₪X,XXX) - [reason to consider]

## Notes
- [Additional recommendations]
```

## Validation

After generating, verify:
- All required components are specified
- Socket/chipset compatibility is correct
- Form factors are compatible
- Budget constraints are met (if specified)
