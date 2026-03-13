# Builder Memory

## 2026-03-12: Agent Discoverability Implementation

### What was done
- Extended `build.py` to generate `api/v1/catalog.json`, `api/v1/categories.json`, and `llms.txt`
- All three files are auto-generated from data, so counts stay current when entries are added
- `api/v1/` directory is created by build script if it doesn't exist

### Current build outputs
1. `data.js` — Frontend JS (`window.SOFTWARE = [...]`)
2. `api/v1/catalog.json` — Pure JSON array of all entries
3. `api/v1/categories.json` — Category name to count mapping
4. `llms.txt` — AI agent manifest with site description, API endpoints, entry format, categories

### Remaining strategist tasks (not yet done)
- Task 3: JSON-LD structured data in index.html (schema.org SoftwareApplication markup)
- Task 4: Semantic HTML fallback / noscript block in index.html
- Both require modifying index.html

### Stats at time of implementation
- 290 entries, 54 categories, 6 data files

## 2026-03-12: Tree Drill-Down Navigation

### What was done
- Replaced flat card grid + sidebar with tree-based drill-down UI in `index.html`
- Tree structure loaded from `taxonomy.json` via `fetch()` at startup
- 14 top-level nodes, 2-3 levels deep, all 54 categories map to unique leaf nodes
- Added breadcrumb navigation (clickable, accent-colored current node)
- Removed: sidebar, mobile filter bar (peek-bar)
- Kept: search (skips tree, shows all matching entries), OS filters, detail panel, sort controls (leaf only), hash deep-linking

### Key design decisions
- Tiles use `minmax(240px, 1fr)` grid — responsive for any number of tiles (3 to 14)
- Sort controls hidden when viewing tree tiles, shown at leaf nodes and during search
- Breadcrumb hidden during search mode
- Graceful fallback: if `taxonomy.json` fetch fails, all entries shown as cards
- `countEntries()` recursively counts entries under any node by collecting category names

### Files modified
- `index.html` — complete rewrite of layout section and JavaScript

### Things to watch
- `taxonomy.json` must be co-located with `index.html` for fetch to work (same directory or configured server)
- If new categories are added to data, they must also be added to `taxonomy.json` leaf nodes
- The `collectCategories()` function traverses the tree on every tile render — fine for 54 categories, but would need caching if taxonomy grew very large
