# Source of these skills

Copied from the open source **claude-seo** plugin by AgriciDaniel (MIT license, see `LICENSE` in this folder):
https://github.com/AgriciDaniel/claude-seo, commit `5d7d85ef32ade08dd4265cb678af8357ca6e6098` (version 2.6.3, 26 Nov 2026).

Reviewed before copying (28 Nov 2026): no telemetry, no hidden network calls, no prompt-injection text.

## What was changed
- Only skills that fit this website were copied: seo (hub), seo-audit, seo-technical, seo-page, seo-schema, seo-sitemap, seo-hreflang, seo-geo, seo-content, seo-content-brief, seo-cluster, seo-images, seo-google, seo-agentic, seo-plan, seo-sxo, seo-competitor-pages, seo-drift, seo-flow, seo-programmatic, seo-bing. Their agents are in `.claude/agents/`.
- Left out: local, maps, ecommerce, shopify, backlinks, dataforseo, posthog, image-gen (paid services or not relevant), the plugin hook, the install scripts, the seo-cockpit add-on, and the maintainer scripts release_sign.py, verify_release.py, sync_flow.py. The hub skill still mentions the left-out commands; they are not available here.
- `${CLAUDE_PLUGIN_ROOT}` paths were rewritten to this repository: the launcher is `"$(git rev-parse --show-toplevel)/.claude/skills/seo/scripts/claude-seo"`.

## Runtime
Python tools need a one-time `/seo setup` (makes `.claude/skills/seo/.venv` and downloads Chromium; both are git-ignored and in `.assetsignore`, so they are never committed or served). Without it, skills that only read pages through Claude's own tools still work.

## Google sign-in
Read-only by default (Search Console + GA4). Never use the `--indexing` option. Credentials go to `~/.config/claude-seo/`, never into this repository.
