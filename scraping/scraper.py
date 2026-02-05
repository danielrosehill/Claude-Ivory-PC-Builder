#!/usr/bin/env python3
"""
Ivory Computer Parts Scraper

Scrapes product listings from Ivory.co.il catalog pages,
extracting product names and regular prices (not Eilat prices).

Saves catalogs in timestamped directories for historical tracking.
"""

import json
import os
import re
import time
from datetime import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup

# Paths
SCRIPT_DIR = Path(__file__).parent
URLS_FILE = SCRIPT_DIR / "urls.json"
CATALOG_BASE_DIR = SCRIPT_DIR.parent / "catalog"

# Request settings
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}
REQUEST_DELAY = 1.5  # seconds between requests


def load_urls() -> dict:
    """Load category URLs from JSON file."""
    with open(URLS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def parse_price(price_str: str) -> float | None:
    """Parse price string to float, handling Hebrew formatting."""
    if not price_str:
        return None
    # Remove commas and whitespace, extract digits
    cleaned = re.sub(r"[^\d.]", "", price_str.replace(",", ""))
    try:
        return float(cleaned)
    except ValueError:
        return None


def scrape_category(url: str, category_name: str) -> list[dict]:
    """
    Scrape products from a category page.

    Products are contained within <div class="row justify-content-rigth 8085">
    Each product is in an <a class="product-anchor"> with:
    - Product name in div.title_product_catalog
    - Regular price in span.price (NOT the ones with eilatprice class)
    """
    products = []

    try:
        print(f"  Fetching: {url}")
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Find the main products container using the identified div pattern
        # Note: "rigth" is a typo in the original site's HTML
        products_container = soup.find("div", class_=re.compile(r"row justify-content-rigth 8085"))

        if not products_container:
            print(f"  Warning: Products container not found for {category_name}")
            # Fall back to searching entire page
            products_container = soup

        # Find all product anchors
        product_anchors = products_container.find_all("a", class_="product-anchor")

        if not product_anchors:
            print(f"  Warning: No products found for {category_name}")
            return products

        print(f"  Found {len(product_anchors)} products")

        for anchor in product_anchors:
            product = extract_product_data(anchor)
            if product:
                products.append(product)

    except requests.RequestException as e:
        print(f"  Error fetching {url}: {e}")
    except Exception as e:
        print(f"  Error parsing {category_name}: {e}")

    return products


def extract_product_data(anchor) -> dict | None:
    """Extract product name and price from a product anchor element."""
    try:
        # Get product ID
        product_id = anchor.get("data-product-id", "")

        # Get product URL
        product_url = anchor.get("href", "")
        if product_url and not product_url.startswith("http"):
            product_url = f"https://www.ivory.co.il/{product_url}"

        # Get product name from title_product_catalog div
        name_div = anchor.find("div", class_=re.compile(r"title_product_catalog"))
        if not name_div:
            return None

        product_name = name_div.get_text(strip=True)
        if not product_name:
            return None

        # Get regular price (NOT eilat price)
        # The regular price is in span.price WITHOUT the eilatprice class
        price = None
        price_area = anchor.find("span", class_="price-area")
        if price_area:
            # Find span.price that doesn't have eilatprice class
            price_span = price_area.find("span", class_="price")
            if price_span and "eilatprice" not in price_span.get("class", []):
                price = parse_price(price_span.get_text())

        # Alternative: look for pricing-details without eilat
        if price is None:
            pricing_details = anchor.find("div", class_="pricing-details")
            if pricing_details:
                # Find the first price-area that's not eilatprice
                for pa in pricing_details.find_all("span", class_="price-area"):
                    if "eilatprice" not in pa.get("class", []):
                        price_span = pa.find("span", class_="price")
                        if price_span and "eilatprice" not in price_span.get("class", []):
                            price = parse_price(price_span.get_text())
                            break

        return {
            "id": product_id,
            "name": product_name,
            "price_ils": price,
            "url": product_url,
        }

    except Exception as e:
        print(f"    Error extracting product: {e}")
        return None


def get_timestamped_dir() -> tuple[Path, str]:
    """Create and return a timestamped directory for this scrape run."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    timestamped_dir = CATALOG_BASE_DIR / timestamp
    timestamped_dir.mkdir(parents=True, exist_ok=True)
    return timestamped_dir, timestamp


def update_current_symlink(timestamped_dir: Path):
    """Update the 'current' symlink to point to the latest catalog."""
    current_link = CATALOG_BASE_DIR / "current"

    # Remove existing symlink if present
    if current_link.is_symlink():
        current_link.unlink()
    elif current_link.exists():
        # If it's a regular directory (from old format), leave it
        print(f"  Note: {current_link} is not a symlink, skipping update")
        return

    # Create relative symlink
    try:
        current_link.symlink_to(timestamped_dir.name)
        print(f"  Updated 'current' symlink -> {timestamped_dir.name}")
    except OSError as e:
        print(f"  Warning: Could not create symlink: {e}")


def update_manifest(timestamp: str, summary: dict):
    """Update the catalog manifest with this scrape run."""
    manifest_file = CATALOG_BASE_DIR / "manifest.json"

    # Load existing manifest or create new
    if manifest_file.exists():
        with open(manifest_file, "r", encoding="utf-8") as f:
            manifest = json.load(f)
    else:
        manifest = {
            "description": "Catalog scrape history",
            "runs": []
        }

    # Add this run
    manifest["runs"].append({
        "timestamp": timestamp,
        "scraped_at": summary["scraped_at"],
        "categories_scraped": summary["categories_scraped"],
        "total_products": summary["total_products"],
        "directory": timestamp
    })

    # Update latest pointer
    manifest["latest"] = timestamp
    manifest["updated_at"] = datetime.now().isoformat()

    # Save manifest
    with open(manifest_file, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(f"  Updated manifest: {len(manifest['runs'])} total runs")


def save_catalog(catalog_dir: Path, category_slug: str, products: list[dict], metadata: dict):
    """Save scraped products to JSON file in catalog directory."""
    output = {
        "metadata": metadata,
        "products": products,
    }

    output_file = catalog_dir / f"{category_slug}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"  Saved {len(products)} products to {output_file.name}")


def main():
    """Main scraping function."""
    print("Ivory Computer Parts Scraper")
    print("=" * 50)

    # Create timestamped directory for this run
    catalog_dir, timestamp = get_timestamped_dir()
    print(f"Catalog directory: {catalog_dir}")

    # Load URLs
    config = load_urls()
    categories = config.get("categories", [])

    if not categories:
        print("Error: No categories found in urls.json")
        return

    print(f"Found {len(categories)} categories to scrape\n")

    # Scrape each category
    all_results = {}
    scrape_start = datetime.now()

    for i, category in enumerate(categories):
        name = category.get("name", "Unknown")
        slug = category.get("slug", f"category_{i}")
        url = category.get("url", "")

        if not url:
            print(f"Skipping {name}: No URL")
            continue

        print(f"\n[{i+1}/{len(categories)}] Scraping: {name}")

        products = scrape_category(url, name)

        metadata = {
            "category_name": name,
            "category_slug": slug,
            "source_url": url,
            "scraped_at": datetime.now().isoformat(),
            "product_count": len(products),
        }

        save_catalog(catalog_dir, slug, products, metadata)
        all_results[slug] = len(products)

        # Rate limiting
        if i < len(categories) - 1:
            time.sleep(REQUEST_DELAY)

    # Save summary in the timestamped directory
    scrape_end = datetime.now()
    summary = {
        "timestamp": timestamp,
        "scraped_at": scrape_start.isoformat(),
        "completed_at": scrape_end.isoformat(),
        "duration_seconds": (scrape_end - scrape_start).total_seconds(),
        "categories_scraped": len(all_results),
        "total_products": sum(all_results.values()),
        "results_by_category": all_results,
    }

    summary_file = catalog_dir / "summary.json"
    with open(summary_file, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    # Update the 'current' symlink and manifest
    update_current_symlink(catalog_dir)
    update_manifest(timestamp, summary)

    print("\n" + "=" * 50)
    print(f"Scraping complete!")
    print(f"Timestamp: {timestamp}")
    print(f"Total products: {summary['total_products']}")
    print(f"Duration: {summary['duration_seconds']:.1f}s")
    print(f"Catalog saved to: {catalog_dir}")


if __name__ == "__main__":
    main()
