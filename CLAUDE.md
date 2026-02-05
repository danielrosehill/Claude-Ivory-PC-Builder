# CLAUDE.md - Claude Code PC Builder

You are an AI assistant helping users spec out custom PC builds using component data scraped from Ivory.co.il (an Israeli computer parts retailer).

## Repository Structure

```
├── builds/              # Individual build projects
│   └── {n}/             # Each build has its own numbered directory
│       ├── task.md      # Requirements and constraints
│       └── suggested-build.md  # Generated spec (output)
├── catalog/             # Scraped component data
│   ├── current/         # Symlink to latest catalog
│   ├── manifest.json    # Scrape history index
│   └── YYYY-MM-DD_HH-MM-SS/  # Timestamped catalog snapshots
├── scraping/            # Web scraper for updating catalog
├── screenshots/         # Visual references if needed
└── .claude/             # Claude Code commands and agents
```

## Workflow

### 1. Update Catalog (if needed)
Before generating a build, ensure catalog data is current:
```bash
cd scraping && python scraper.py
```
Or use `/update-catalog`

### 2. Read Requirements
Each build's requirements are in `builds/{n}/task.md`. This includes:
- Use case (gaming, server, workstation, etc.)
- Existing components to reuse
- Constraints (size, budget, specific features)
- Performance requirements

### 3. Generate Build Spec
Output goes to `builds/{n}/suggested-build.md` with:
- Recommended components with prices (ILS)
- Compatibility notes
- Links to product pages
- Total estimated cost
- Alternative options where relevant

## Catalog System

### Structure

Catalogs are stored in timestamped directories for historical tracking:

```
catalog/
├── manifest.json           # Index of all scrape runs
├── current -> 2026-02-05_13-43-00/  # Symlink to latest
├── 2026-02-05_13-43-00/    # Timestamped snapshot
│   ├── summary.json        # Scrape run metadata
│   ├── intel_cpus.json
│   ├── amd_cpus.json
│   └── ...
└── 2026-02-04_10-00-00/    # Historical snapshot
    └── ...
```

### Manifest File

The `manifest.json` tracks all scrape runs:
```json
{
  "description": "Catalog scrape history",
  "latest": "2026-02-05_13-43-00",
  "updated_at": "2026-02-05T13:45:00",
  "runs": [
    {
      "timestamp": "2026-02-05_13-43-00",
      "scraped_at": "2026-02-05T13:43:00",
      "categories_scraped": 16,
      "total_products": 523,
      "directory": "2026-02-05_13-43-00"
    }
  ]
}
```

### Reading Catalog Data

Always read from `catalog/current/` for the latest data:
- `catalog/current/intel_cpus.json`
- `catalog/current/cases.json`
- etc.

### Category Files

| File | Contents |
|------|----------|
| `intel_cpus.json` | Intel processors |
| `amd_cpus.json` | AMD processors |
| `intel_motherboards.json` | Intel-compatible motherboards |
| `amd_motherboards.json` | AMD-compatible motherboards |
| `ram.json` | Memory modules |
| `cases.json` | Computer cases |
| `psus.json` | Power supplies |
| `cpu_coolers.json` | Air coolers |
| `water_coolers.json` | AIO liquid coolers |
| `gpus_nvidia.json` | NVIDIA graphics cards |
| `gpus_amd.json` | AMD graphics cards |
| `internal_ssds.json` | Solid state drives |
| `internal_hdds.json` | Hard disk drives |
| `case_fans.json` | Case fans |
| `network_cards.json` | Network adapters |
| `optical_drives.json` | Optical drives |

### Catalog Data Format

Each JSON file follows this structure:
```json
{
  "metadata": {
    "category_name": "Intel CPUs",
    "category_slug": "intel_cpus",
    "source_url": "https://www.ivory.co.il/...",
    "scraped_at": "2026-02-05T13:43:53.263139",
    "product_count": 48
  },
  "products": [
    {
      "id": "85530",
      "name": "מעבד Intel Core i7-14700F up to 5.40GHz 33MB Cache...",
      "price_ils": 1250.0,
      "url": "https://www.ivory.co.il/catalog.php?id=85530"
    }
  ]
}
```

## Build Generation Guidelines

### Compatibility Checks
- **CPU + Motherboard**: Match socket type (LGA1700, LGA1851, AM5, AM4, etc.)
- **RAM + Motherboard**: Match DDR generation (DDR4 vs DDR5)
- **Case + Motherboard**: Match form factor (ATX, Micro-ATX, Mini-ITX)
- **Case + PSU**: Check PSU length compatibility
- **Case + CPU Cooler**: Check cooler height clearance
- **PSU Wattage**: Ensure adequate power for all components

### Output Format for suggested-build.md

```markdown
# Suggested Build: [Build Name]

Generated: [Date]
Catalog: [Catalog timestamp]
Based on: builds/{n}/task.md

## Summary
[Brief description of the build and design choices]

## Components

| Component | Product | Price (ILS) | Link |
|-----------|---------|-------------|------|
| CPU | [Name] | ₪X,XXX | [Link] |
| Motherboard | [Name] | ₪X,XXX | [Link] |
| ... | ... | ... | ... |

**Total: ₪X,XXX**

## Compatibility Notes
- [Any compatibility considerations]

## Existing Components Used
- [List of components from task.md being reused]

## Alternative Options
- [CPU]: [Alternative] (₪X,XXX) - [reason]
- [etc.]

## Notes
- [Any additional recommendations or considerations]
```

## Commands

### Build Commands
| Command | Description |
|---------|-------------|
| `/new-build {n}` | Create a new build project with template |
| `/generate-build {n}` | Generate suggested spec for build n |
| `/compare-builds` | Compare multiple build configurations |
| `/check-compatibility` | Verify component compatibility |

### Catalog Commands
| Command | Description |
|---------|-------------|
| `/update-catalog` | Refresh pricing from Ivory.co.il (creates new timestamped snapshot) |
| `/catalog-info` | Show current catalog info and stats |
| `/catalog-history` | List all historical catalog snapshots |
| `/use-catalog {timestamp}` | Switch to a historical catalog version |
| `/search-catalog {query}` | Search products across all categories |
| `/price-check {id/name}` | Check price and history for a product |

## Notes

- Prices are in Israeli Shekels (ILS/₪)
- Product names may contain Hebrew text
- Catalog snapshots are preserved for price tracking
- Use `/catalog-info` to check catalog freshness before generating builds
- Historical catalogs enable price trend analysis
