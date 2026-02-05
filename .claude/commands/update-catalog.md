# Update Catalog

Refresh the component pricing catalog by scraping current data from Ivory.co.il.

## Instructions

1. Navigate to the scraping directory
2. Activate the virtual environment if it exists, or create one
3. Install dependencies if needed (requests, beautifulsoup4)
4. Run the scraper
5. Report the results

## Execution

```bash
cd scraping
source ../.venv/bin/activate 2>/dev/null || source .venv/bin/activate 2>/dev/null || true
python scraper.py
```

## Expected Output

The scraper will:
- Fetch current pricing from each category on Ivory.co.il
- Save JSON files to the `catalog/` directory
- Generate a summary in `catalog/scrape_summary.json`

Report the number of products scraped per category and any errors encountered.
