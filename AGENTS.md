# Main Menu

For agent startup protocol, communication rules, and forum voting, see `PROTOCOL.md`.

## Overview

Universal software directory at main.menu. Browse apps, libraries, protocols, and platforms across 128 categories in a tree hierarchy, filterable by OS. Static site — no backend.

## Stack

- **Frontend**: Single `index.html` (vanilla HTML/CSS/JS, no frameworks, no build tools)
- **Data**: JSON files in `data/` → `build.py` aggregates into `data.js`
- **Scraping**: `python -m scrape` fetches from awesome lists, Homebrew, CNCF → `data/discovered_*.json`
- **Taxonomy**: `taxonomy.json` defines the tree hierarchy → `build.py` generates `taxonomy.js`
- **Categorization**: `scrape/categorize.py` (keyword mapping), `scrape/sources/awesome_registry.py` (section maps)
- **Schema**: `schema.json` (JSON Schema draft-07) defines entry shape
- **Deploy**: `bash deploy.sh` → gcloud scp to thisminute.org/mainmenu

## Key Files

| File | Purpose |
|------|---------|
| `index.html` | Entire frontend — tree nav, search, OS filters, detail panel |
| `data.js` | Generated. `window.SOFTWARE` array of all entries |
| `taxonomy.js` | Generated. `window.TAXONOMY` tree for drill-down navigation |
| `taxonomy.json` | Tree hierarchy definition — 22 top-level groups, ~128 leaf categories |
| `build.py` | Aggregates `data/*.json`, deduplicates, generates data.js, taxonomy.js, api/, llms.txt, noscript HTML |
| `schema.json` | Defines entry shape |
| `data/*.json` | Source data files (22 files including discovered scrape data) |
| `scrape/categorize.py` | Keyword-to-category mapping and Tier 1/2/3 scoring |
| `scrape/sources/awesome_registry.py` | Section-to-category maps for 22 awesome lists |
| `scrape/pipeline.py` | Scrape pipeline: normalize → categorize → quality gate → dedup → validate |
| `deploy.sh` | Upload to thisminute.org via gcloud compute scp |

## Entry Schema (abbreviated)

Each entry has: `id` (kebab-case), `name`, `description` (~200 chars), `url`, `category` (one of 128), `os[]` (windows/macos/linux/web/ios/android), `pricing` (free/freemium/paid/subscription), `tags[]`, optional `source` (repo URL if open-source), optional `language`.

## Current State

- 16,337 entries across 128 categories in 22 top-level groups
- Tree drill-down navigation (taxonomy.json → taxonomy.js)
- Warm amber color scheme, dark theme
- Search across names, descriptions, categories, tags
- OS filtering, sort by category/A-Z/shuffle
- Detail panel with website + source code links
- API endpoint at api/v1/catalog.json, llms.txt for agent discovery
- Noscript fallback with full catalog HTML
- Live at https://thisminute.org/mainmenu
- Cross-links to sister projects (Rhizome, Agent Forge) in header

## Commands

- **Build**: `python build.py`
- **Scrape**: `python -m scrape` (default: awesome,homebrew,cncf sources)
- **Dry-run scrape**: `python -m scrape --dry-run`
- **Deploy**: `bash deploy.sh`
- **Local dev**: Open `index.html` in a browser (file:// works for basic testing, but taxonomy.json fetch needs a server)

## Quality Signals

- Are entry descriptions accurate and informative?
- Are URLs correct and not dead?
- Are OS tags accurate?
- Are pricing models current?
- Is every leaf category well-represented (30-200 entries)?
- Does the UI work on mobile?
- Do filters compose correctly (category + OS + search)?
- Are scrape section maps routing entries to the correct categories?
- Is the taxonomy tree intuitive to navigate?

## Recent Major Changes (2026-03-13)

- **Taxonomy restructure**: 105 → 128 categories. Split Web Frameworks (Frontend/Backend/Template Engines), Mobile Frameworks (iOS/Android/Cross-Platform), Database ORMs (ORMs/Drivers/Migrations/Caching), Linters & Formatters (Static Analysis/Linters/Formatters). Added Blockchain & Web3, Text Processing, Configuration, Terminal UI, NLP & Text AI, LLM Tools, Math & Numerics, Compression & Archiving.
- **Categorizer fixes**: Removed overly broad keywords (http, api, log, search, mobile). Added Utilities penalty in Tier 3 scoring. Normalized Tier 3 by category size (sqrt normalization).
- **Section map fixes**: Fixed catch-all `r".*"` patterns in awesome-static-analysis and awesome-android-ui. Narrowed HTTP routing. Split database routing. Added blockchain exclusion before AI patterns. Routed iOS entries to iOS UI Components / iOS Networking & Data.
- **Re-scrape**: 15,191 new entries from clean categorization. Utilities: 121 (was 3,313). HTTP Libraries: 18 (was 581 as HTTP Clients).
