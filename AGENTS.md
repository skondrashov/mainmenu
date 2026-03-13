# Main Menu

If told to go, start, or begin — you are the **orchestrator**. See `agents/orchestrator.md`.

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

- 15,555 entries across 129 categories in 22 top-level groups
- Tree drill-down navigation (taxonomy.json → taxonomy.js)
- Warm amber color scheme, dark theme, category-colored card borders
- Cmd/Ctrl+K search shortcut, live result count
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

- **Taxonomy restructure**: 105 → 129 categories. Added Networking, Blockchain & Web3, Text Processing, Configuration, Terminal UI, NLP & Text AI, LLM Tools, Math & Numerics, Compression & Archiving.
- **Categorizer hardening**: 3 rounds of fixes. Stop-word filter, Tier 3 penalties for 10 categories, Tier 3 exclusions for Desktop App Frameworks and Mobile IDE & Tools, confidence threshold at 0.15. Tightened 30+ section map patterns (log→logging, ci→ci.?cd, date→date.?time, editor→text.?editor, gui→gui.?framework, etc.). Narrowed 6 overly broad keywords (editor, browser, launcher, date, copilot, proxy).
- **Networking category**: New category absorbing Go networking libraries from VPN. VPN: 274→59, Networking: 0→286.
- **Design UX**: Cmd/Ctrl+K search shortcut, live result count, category-colored card borders (22 group colors from taxonomy).
- **Re-scrape totals**: 14,409 discovered entries + 1,146 curated = 15,555 total.
