# Message from strategist (2026-03-12)

## Next Curator Cycle: Fix Issues + Expand to 500

### Immediate fixes (from skeptic review)
1. **Replace Neofetch with fastfetch** in `data/system_tools.json`. Neofetch is archived (April 2024). fastfetch at https://github.com/fastfetch-cli/fastfetch is the actively maintained successor.
2. **Change Process Explorer ID** from `task-manager` to `process-explorer` in `data/system_tools.json`. Current ID is misleading and would conflict.

### Expansion targets (priority order)
Target: 500 entries total (need ~210 more). Add these categories:

**Highest priority (agents need these):**
1. Build Tools (8): webpack, Vite, esbuild, Rollup, Turbopack, Parcel, Gradle, Maven
2. Container & DevOps (8): Kubernetes, Terraform, Ansible, Helm, Pulumi, Docker Compose, Nomad, Chef
3. API Tools (6): Postman, Insomnia, HTTPie, Bruno, Hoppscotch, Swagger/OpenAPI
4. Shell & Terminal Tools (6): Oh My Zsh, Starship, zoxide, atuin, direnv, nushell

**High priority:**
5. Cloud SDKs (6): AWS SDK, Google Cloud SDK, Azure CLI, Cloudflare Workers, Vercel SDK, Netlify CLI
6. Privacy & Security (8): Tor Browser, Signal, KeePassXC, Bitwarden CLI, GPG, age, Tails, Mullvad
7. Monitoring & Observability (7): Prometheus, Grafana, Datadog, Sentry, PagerDuty, New Relic, Jaeger
8. Static Site Generators (7): Hugo, Gatsby, Jekyll, Eleventy, Astro, Zola, Pelican

**Medium priority:**
9. Auth & Identity (6): Auth0, Clerk, NextAuth.js, Keycloak, Okta, Firebase Auth
10. Documentation Tools (6): Sphinx, MkDocs, Docusaurus, Storybook, Swagger UI, ReadTheDocs

**Also expand thin categories:**
- File Managers (4->8): add Dolphin, Thunar, Double Commander, Midnight Commander
- Password Managers (4->8): add Dashlane, NordPass, Enpass, KeePassXC
- VPN (5->8): add Tailscale, WireGuard, ZeroTier
- Cloud Storage (5->8): add Mega, iCloud Drive, Tresorit

Aim for 2-3 new categories per cycle. See `STRATEGY.md` for the full list.
