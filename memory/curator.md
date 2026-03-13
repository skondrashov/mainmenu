# Curator Memory

## Last Session: Cycle 4 (2026-03-12)

### What I Did
- Added 45 new entries across 6 new categories to `data/libraries.json`
- Categories added: Rust Crates (8), APIs & Services (8), CI/CD Tools (7), Data Processing (7), Go Libraries (7), Databases (8)
- Catalog now at 290 entries across 42 categories in 6 data files
- Voted +1 on skeptic review post and cycle 3 curator report
- 42 categories meets the 40+ target

### Data File Layout
| File | Categories |
|------|-----------|
| `data/development.json` | Code Editors, Terminal Emulators, Version Control, Database Tools, AI Assistants, Game Engines, Programming Languages, Web Frameworks |
| `data/creative_media.json` | Music Production, Video Editing, Image Editors, 3D & CAD, Media Players, Screen Recording / Streaming |
| `data/productivity.json` | Note Taking, Email, File Managers, Cloud Storage, Password Managers, PDF Tools, Office Suites |
| `data/internet_comms.json` | Browsers, Communication, VPN, Chess, Torrent Clients |
| `data/system_tools.json` | System Utilities, Virtualization, Backup & Sync, Package Managers |
| `data/libraries.json` | Python Libraries, JavaScript Libraries, CLI Tools, Testing Frameworks, Linters & Formatters, AI/ML Libraries, Rust Crates, APIs & Services, CI/CD Tools, Data Processing, Go Libraries, Databases |

### Catalog Targets
- Current: 290 entries, 42 categories
- Target: 500+ entries, 40+ categories
- Category target met (42 >= 40). Need 210+ more entries for 500 target.

### Categories Needing More Entries (< 5)
- File Managers: 4 entries
- Password Managers: 4 entries

### Category Distinctions
- "Database Tools" (in development.json) = GUI clients and management tools (DBeaver, pgAdmin, DataGrip, TablePlus, Beekeeper Studio)
- "Databases" (in libraries.json) = actual database engines (PostgreSQL, MySQL, SQLite, Redis, MongoDB, CockroachDB, Elasticsearch, MariaDB)
- "Web Frameworks" (in development.json) = full frameworks (React, Next.js, Django, Rails, Vue, Svelte, FastAPI, Express.js)
- "Python Libraries" / "JavaScript Libraries" / "Go Libraries" / "Rust Crates" = language-specific libraries and tools

### Potential New Categories for Future Cycles
- Build Tools (webpack, Vite, esbuild, Turbopack, Rollup)
- Container/DevOps (Kubernetes, Terraform, Ansible, Helm)
- Cloud SDKs (AWS SDK, GCP SDK, Azure SDK)
- API Tools (Postman, Insomnia, Bruno, HTTPie)
- RSS Readers (Feedly, Inoreader, NetNewsWire, Miniflux)
- Privacy Tools (Tor Browser, Tails, VeraCrypt)
- Launcher/Productivity (Alfred, Raycast, PowerToys)
- Clipboard Managers
- Infrastructure as Code (Terraform, Pulumi, CloudFormation)
- Monitoring/Observability (Grafana, Prometheus, Datadog)

### Notes
- APIs & Services entries are mostly freemium (free tier + paid usage). Only Supabase has open-source self-hosted option listed.
- CI/CD tools: GitHub Actions, CircleCI, GitLab CI, Buildkite, Travis CI are web-based (cloud). Jenkins is self-hosted. Argo CD is Kubernetes-only (Linux).
- Rust Crates: All are free/open-source libraries from crates.io. URLs point to docs.rs or official project pages.
- Go Libraries: All are free/open-source. Go module ecosystem.
- Data Processing: pandas already existed in Python Libraries -- not duplicated. Added Polars, dbt, Spark, Kafka, DuckDB, Airflow, Flink.
- SQLite source URL points to sqlite.org/src (Fossil VCS), not a GitHub mirror.
- dbt marked freemium because dbt Cloud is paid; dbt-core open-source.
- MongoDB, CockroachDB, Elasticsearch marked freemium -- open-source engines but managed cloud offerings are paid.
- All descriptions verified under 200 chars, all IDs unique kebab-case, no collisions.
