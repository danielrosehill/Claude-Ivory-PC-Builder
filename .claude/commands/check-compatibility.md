# Check Compatibility

Verify component compatibility for a build or set of components.

## Arguments

- `$ARGUMENTS` - Build number, or component names to check

## Instructions

### If build number provided:
1. Read `builds/$ARGUMENTS/suggested-build.md`
2. Extract all components
3. Verify compatibility

### If component names provided:
1. Search catalog for matching products
2. Check compatibility between specified components

## Compatibility Checks

### CPU + Motherboard
- Socket type must match (LGA1700, LGA1851, AM5, AM4, etc.)
- Chipset should be appropriate for CPU tier

### RAM + Motherboard
- DDR generation must match (DDR4 vs DDR5)
- Speed should be supported by motherboard

### Case + Motherboard
- Form factor compatibility:
  - ATX case: ATX, Micro-ATX, Mini-ITX
  - Micro-ATX case: Micro-ATX, Mini-ITX
  - Mini-ITX case: Mini-ITX only

### Case + PSU
- PSU form factor (ATX, SFX, SFX-L)
- PSU length clearance

### Case + CPU Cooler
- Cooler height vs case CPU cooler clearance
- Tower cooler RAM clearance

### PSU + Components
- Total system power draw estimate
- Recommended headroom (20-30%)

## Output

```markdown
# Compatibility Check: Build $ARGUMENTS

## Status: ✅ Compatible / ⚠️ Issues Found / ❌ Incompatible

### Checks Performed

| Check | Status | Notes |
|-------|--------|-------|
| CPU ↔ Motherboard | ✅/❌ | [Details] |
| RAM ↔ Motherboard | ✅/❌ | [Details] |
| Case ↔ Motherboard | ✅/❌ | [Details] |
| Case ↔ Cooler | ✅/❌ | [Details] |
| PSU Wattage | ✅/❌ | [Details] |

### Issues (if any)
- [Issue description and resolution]

### Recommendations
- [Any suggestions for improvement]
```
