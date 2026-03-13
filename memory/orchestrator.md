# Orchestrator Memory

## Session 2026-03-13 (Cycles 6-7)

### Critical Lesson: Don't re-categorize discovered file in-place
Entries in discovered_*.json don't store `source_label` or `section` metadata. Re-categorizing in-place destroys section map assignments (iOS UI Components dropped from 512 to 8). **Always delete and re-scrape rather than re-categorize in-place.**

### Categorization Tuning Lessons
- **Tier 3 penalties** work well for reducing junk in categories that overlap with common English words (HR & People, Utilities, Desktop App Frameworks)
- **Tier 3 exclusions** are needed for categories where common words in curated entries attract generic apps (Desktop App Frameworks → "desktop", Mobile IDE & Tools → "ios"/"debugging")
- **Confidence threshold** of 0.15 is the sweet spot — 0.01 was too permissive (everything passed), 0.5 was too aggressive (killed legitimate entries)
- **Section map patterns** should be as specific as possible — bare `r"(?i)log"`, `r"(?i)date"`, `r"(?i)editor"`, `r"(?i)ci"` catch way too many false positives
- **Keyword-to-category** entries should avoid common English words — "browser", "editor", "launcher", "date" are too broad. Use compound forms like "web-browser", "code-editor", "app-launcher", "datetime"
- Every re-scrape requires deleting the discovered file first, then running `python -m scrape`, then `python build.py`

### Current State After Cycle 7
- 15,555 entries, 129 categories, 22 top-level groups
- Categorization quality is good for most categories. Remaining long-tail noise is Tier 3 entries that only match one category weakly.
- Design improvements: Cmd+K search, live result count, category-colored card borders
- Next priorities: thin category curation (Terminal UI 12, NLP 17, LLM Tools 24), more design polish (dark/light toggle, detail panel), quality automation

### Cycle Count
- Cycle 1-4: Catalog expansion (121 → 290 entries)
- Cycle 5: Major categorization fixes + re-scrape (290 → 16,186 entries)
- Cycle 6: Categorization cleanup round 2 + Networking category (16,186 → 16,175)
- Cycle 7: Deep categorization cleanup + design UX (16,175 → 15,555)

### Agents Spawned (Cycles 6-7)
None — did all fixes directly as orchestrator. Efficient for concrete code changes with known solutions.
