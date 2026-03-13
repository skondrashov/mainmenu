# Skeptic Memory

## Last Session: Taxonomy Restructure Review (2026-03-13)

### What I Did
- Reviewed results of 290 → 16,237 entry scrape with restructured 128-category taxonomy
- Analyzed all 15,091 discovered_20260313.json entries via Python scripts
- Spot-checked 10 entries each in: AI Assistants, Cloud SDKs & CLIs, Task Runners, Utilities, HTTP Libraries, iOS UI Components, Static Analysis, Frontend Frameworks, Backend Frameworks, ORMs
- Checked HR & People (220), Package Managers (222), Mobile IDE & Tools (262) for inflation
- Verified top-10 categories for obvious garbage
- Identified 2 new root-cause bugs (stop-word contamination in Tier 3, awesome-go dependency injection routing)

### Issues Found (this session)

#### Confirmed Fixed (no action needed)
- Tier 3 feedback loop from discovered_*.json: FIXED (categorize.py line 258)
- AI Assistants: 579 → 21 scraped entries — clean (not 36 as claimed, but close enough)
- Cloud SDKs: 558 → 29 scraped entries — mostly clean
- Task Runners: 344 → 29 scraped entries — mostly clean (but wrong entries — automation apps, not task runners)
- Utilities: 3,313 → 110 — fixed
- HTTP Libraries: 581 → 18 — fixed and clean

#### New bugs requiring action (high priority)

**S18 — HR & People: Stop-word contamination (CRITICAL)**
- 210/212 scraped entries are garbage
- Root cause: Tier 3 keyword index contains "and" (15 occurrences) from curated HR descriptions
- Any entry with "and" in desc scores 15 raw / 12.12 normalized = 1.24 for HR — beats everything
- Fix: filter stop words from build_category_index(), OR add HR & People to the 0.3x penalty set

**S19 — Package Managers: awesome-go section map bug (HIGH)**
- ~179/210 scraped entries are garbage
- Root cause: r"(?i)package|dependen" in awesome-go routes entire "dependency injection" section (25 entries) to Package Managers
- Fix: change to r"(?i)package.?manager|package.?registry"
- Also: WISO Steuer tax apps (5 entries), iOS activity indicators (3), gaming software (2) via Tier 3

**S21 — CI/CD Tools: "ci" pattern too broad (MEDIUM)**
- Entries with "ci" in GitHub Actions badge URLs or tags are landing in CI/CD
- Confirmed garbage: rustzx (ZX Spectrum emulator), chromem-go (vector DB), bbgo (crypto trading bot), ofxgo (OFX parser), saphyr (YAML parser)
- Fix: tighten r"(?i)devops|deploy|ci" to r"(?i)ci.?cd|continuous.?integr|deploy.?pipeline"

**S24 — Logging & Diagnostics: "log" pattern too broad (MEDIUM)**
- r"(?i)log" matches text segmentation libs, color themes, app scanners
- Confirmed garbage: segment (Unicode text segmenter), Go64 (app scanner), Solarized-Dark-for-Xcode (color theme)
- Fix: change to r"(?i)logging|log.?management|structured.?log"

#### Warnings (lower priority)

**S20 — Task Runners: automation section misrouted**
- awesome-selfhosted automation section routes workflow automation (Kibitzr, Automatisch, Healthchecks) to Task Runners
- These are legitimate tools but wrong category — should be "Workflow Automation" or "Project Management"

**S22 — Code Editors: ~10-15% garbage**
- Molecule visualizer, circuit simulator, music tag editor landing here via Tier 3

**S23 — Data Analysis: ~10-15% garbage**
- iOS animation chart libs, Substrate/Polkadot portal, Go reactive libs routing here

**S25 — AI Assistants: copilot keyword false positives**
- "copilot" keyword: catches Poker Copilot (poker HUD), money tracking app
- "assistant" in description: catches MacBreakZ (break reminder), Isabelle (proof assistant)
- Fix: remove "copilot" from KEYWORD_TO_CATEGORY or narrow to "ai-copilot"

**S26 — Mobile IDE & Tools: ~30% garbage**
- "debugging" and "ios" keywords in small curated index draw generic macOS apps via Tier 3

### Categories Verified as Clean
- AI Assistants (21): 95% legitimate after fix
- HTTP Libraries (18): 100% clean — model category
- iOS UI Components (512): legitimate — all genuine iOS UI components
- Static Analysis (526): legitimate — all genuine static analysis tools
- ORMs (110): 100% clean — automated check found 0 obviously non-ORM entries
- Backend Frameworks (297): ~90% clean — some scope overlap with router/networking libs
- Utilities (110): clean — 0.3x penalty working correctly

### The Stop-Word Bug (Key Finding)
The Tier 3 category scoring uses word frequency from descriptions, but does NOT filter stop words.
For small curated categories (HR & People has only 8 entries = 147 total keyword weight), stop words
like "and" (15 occurrences) dominate the index. sqrt(147) = 12.12, so any entry with "and" anywhere
scores 15/12.12 = 1.24 normalized — enough to win over most other categories.
This will affect ANY small category. Currently visible in HR & People, potentially in:
- Chess (147 keyword weight — same as HR!)
- Flashcards & Study (143)
- Error Handling (121)
Any category with <200 total keyword weight is vulnerable to stop-word false positives.

### Previous Open Warnings (from 2026-03-12)
- FreeFileSync "open-source" status murky: still open
- Lodash "feature-complete" maintenance: still open
- LangChain description drift: still open
- Tag/source consistency uneven (S15): still open
- Apple Notes / iCloud Drive share URL: still open
