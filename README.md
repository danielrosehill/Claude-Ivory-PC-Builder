[![Claude Code Project](https://img.shields.io/badge/Claude%20Code-Project-blue?style=flat-square&logo=anthropic)](https://github.com/danielrosehill/Claude-Code-Repos-Index)

# Ivory PC Builder

An AI-powered PC building assistant that uses Claude Code to generate optimized component specifications based on your requirements, with real-time pricing from [Ivory.co.il](https://www.ivory.co.il).

## Overview

This repository provides a structured workflow for speccing out custom PC builds:

1. **Define requirements** in a task file
2. **Run the AI assistant** to generate optimized specs
3. **Get component recommendations** with current pricing and links

The system uses a scraped catalog of computer components from Ivory.co.il (a major Israeli computer parts retailer) to make informed recommendations based on availability and pricing.

## Quick Start

### Prerequisites

- [Claude Code CLI](https://github.com/anthropics/claude-code) installed
- Python 3.10+ (for catalog updates)

### Create a New Build

1. Run Claude Code in the repository:
   ```bash
   claude
   ```

2. Create a new build:
   ```
   /new-build 1
   ```

3. Edit `builds/1/task.md` with your requirements

4. Generate your build:
   ```
   /generate-build 1
   ```

## Repository Structure

```
├── builds/              # Your build projects
│   └── {n}/
│       ├── task.md      # Requirements (input)
│       └── suggested-build.md  # Recommendations (output)
├── catalog/             # Component pricing data
│   ├── current/         # Symlink to latest catalog
│   ├── manifest.json    # Scrape history index
│   └── YYYY-MM-DD_HH-MM-SS/  # Timestamped snapshots
├── scraping/            # Catalog update scripts
├── .claude/
│   ├── commands/        # Slash commands
│   └── agents.yaml      # AI agent definitions
├── CLAUDE.md            # AI instructions
└── README.md            # This file
```

## Commands

### Build Commands

| Command | Description |
|---------|-------------|
| `/new-build {n}` | Create a new build project with template |
| `/generate-build {n}` | Generate spec for build number n |
| `/compare-builds` | Compare multiple configurations |
| `/check-compatibility` | Verify component compatibility |

### Catalog Commands

| Command | Description |
|---------|-------------|
| `/update-catalog` | Refresh pricing from Ivory.co.il |
| `/catalog-info` | Show current catalog info and stats |
| `/catalog-history` | List all historical catalog snapshots |
| `/use-catalog {timestamp}` | Switch to a historical catalog version |
| `/search-catalog {query}` | Search products across categories |
| `/price-check {id/name}` | Check price and history for a product |

## Catalog System

The scraper saves each run in a timestamped directory, preserving historical pricing data:

```
catalog/
├── manifest.json              # Index of all scrape runs
├── current -> 2026-02-05.../  # Symlink to latest
├── 2026-02-05_13-43-00/       # Latest snapshot
│   ├── summary.json
│   ├── intel_cpus.json
│   └── ...
└── 2026-02-04_10-00-00/       # Historical snapshot
```

This enables:
- **Price tracking** over time
- **Rollback** to previous catalog versions
- **Historical comparisons** for price trends

## Catalog Categories

The scraped catalog includes:

- **CPUs**: Intel and AMD processors
- **Motherboards**: Intel and AMD compatible boards
- **Memory**: DDR4 and DDR5 RAM
- **Storage**: SSDs and HDDs
- **Graphics**: NVIDIA and AMD GPUs
- **Cooling**: Air and liquid coolers
- **Cases**: Various form factors
- **Power Supplies**: PSUs
- **Accessories**: Fans, network cards, optical drives

## Updating the Catalog

Using the slash command (recommended):
```
/update-catalog
```

Or manually:
```bash
cd scraping
source ../.venv/bin/activate
python scraper.py
```

Each update creates a new timestamped snapshot while preserving history.

## Example Task File

```markdown
# Spec

Building a home server for running Docker containers and Frigate NVR
with 3 cameras. Need low power consumption and compact form factor.

# Run Requirements

- Docker workloads
- Frigate (3 cams)
- Home Assistant

# Existing Components

| Component | Model | Status |
|-----------|-------|--------|
| PSU | Corsair CX650 | ✓ Use |
| RAM | 32GB DDR4 | ✓ Use |
| Storage | 4× 480GB SSDs | ✓ Use (ZFS) |

# Constraints

- Case smaller than 445mm × 200mm × 430mm
- Must have 2.5G Ethernet
- Budget: ₪3,000 for new components

# Task

Generate a suggested spec in suggested-build.md
```

## Using as a Template

This repository can be used as a template for your own PC building projects:

1. Fork or clone this repository
2. Clear the `builds/` directory
3. Update `scraping/urls.json` if using a different retailer
4. Run the scraper to populate the catalog
5. Create your build requirements
6. Run Claude Code to generate specs

## Notes

- Prices are in Israeli Shekels (₪/ILS)
- Product names may contain Hebrew text
- Stock availability may vary; check Ivory.co.il for current status
- The scraper respects rate limits (1.5s delay between requests)
- Historical catalog data enables price trend analysis

## License

MIT License - Feel free to use and modify for your own PC building projects.

---

For more Claude Code projects, visit my [Claude Code Repos Index](https://github.com/danielrosehill/Claude-Code-Repos-Index).
