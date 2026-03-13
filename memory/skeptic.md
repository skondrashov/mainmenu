# Skeptic Memory

## Last Session: Cycle 2-4 Review (2026-03-12)

### What I Did
- Reviewed all new entries from Cycles 2, 3, and 4 (98 new entries total)
- Spot-checked 20+ entries via WebFetch across: Beautiful Soup, Black, LangChain, FreeFileSync, Duplicati, Syncthing, HTTPX, restic, BiglyBT, Transmission, Lodash, Chocolatey, BorgBackup, Clippy, Mocha, date-fns, rsync, CrystalDiskInfo, Docker org page, uTorrent
- Ran schema validation: all 290 entries pass (required fields, ID pattern, OS enum, pricing enum, description length)
- Ran build.py: 290 entries, 42 categories, no warnings, no duplicates
- Verified orchestrator fixes: neofetch -> fastfetch (confirmed), task-manager -> process-explorer (confirmed)

### Issues Found and Fixed (this session)
1. **FIXED:** rsync missing `source` URL -> added `https://github.com/RsyncProject/rsync`
2. **FIXED:** FreeFileSync missing `source` URL -> added `https://github.com/nicedayzhu/FreeFileSync`
3. **FIXED:** APT missing `source` URL -> added `https://salsa.debian.org/apt-team/apt`
4. **FIXED:** GNU Emacs missing `source` URL -> added `https://git.savannah.gnu.org/cgit/emacs.git`
5. **FIXED:** iTerm2 missing `source` URL -> added `https://github.com/gnachman/iTerm2`
6. **FIXED:** Docker source URL `https://github.com/docker` -> `https://github.com/moby/moby` (org page, not repo)
7. **FIXED:** winget missing `"open-source"` tag (had source URL but no tag)
8. **FIXED:** Travis CI incorrectly had `"open-source"` tag (proprietary product)

### Open Warnings
- FreeFileSync "open-source" status is murky (non-standard license, restricts modified redistribution)
- Lodash is in "feature-complete" maintenance mode (not abandoned, but no new features)
- LangChain description mentions "chains" which is being de-emphasized in LangChain branding
- Tag/source consistency is uneven: 20+ entries in development.json have `source` URL but no `"open-source"` tag

### Previous Issues Now Resolved
- Neofetch -> Fastfetch: RESOLVED by orchestrator
- Process Explorer ID task-manager -> process-explorer: RESOLVED by orchestrator
- Camtasia pricing: RESOLVED in previous session
- Sumatra PDF source: RESOLVED in previous session

### Verification Approach
- WebFetch for URL and pricing verification
- Python script for schema compliance (required fields, ID pattern, OS/pricing enum, description length, duplicates)
- Python script for open-source tag vs source URL consistency
- build.py for integration testing
- Cross-file duplicate check (IDs, names, and normalized URLs)

### Notes for Next Review
- The tag/source consistency issue (S15) needs a curator cleanup pass -- 20+ entries in development.json and internet_comms.json
- FreeFileSync license situation should be researched more thoroughly
- BorgBackup does NOT support Windows natively (only via WSL/Cygwin) -- current OS tags `["macos", "linux"]` are correct
- Duplicati website uses Framer and is hard to WebFetch -- manual verification needed
- uTorrent website is hard to WebFetch -- manual verification needed
- BiglyBT Linux support is real (on Flathub) but not prominently shown on their site
- Apple Notes and iCloud Drive share the same URL (both point to apple.com/icloud)
- Strategist proposed `maintenance_status` schema field -- if added, Lodash would be "maintenance" and this addresses S13
- Catalog is at 290 entries / 42 categories as of this session
