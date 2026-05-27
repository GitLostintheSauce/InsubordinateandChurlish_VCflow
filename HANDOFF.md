# Session Handoff — VCflow Dashboard

*Regenerated 2026-05-27. Paste this into a new session (or point it at this file) to get fully caught up.*

## TL;DR
This is **VCflow**, an interactive dashboard showing how venture capital reallocated across 6 sectors (AI, Fintech, Climate, Defense, Web3, Biotech) from 2022→2025. Static **vanilla HTML + D3**, deployed on **GitHub Pages**. It's an intern Week-1 project graded on source rigor, dashboard clarity, adaptive reasoning, and prompt/tool documentation. **Phases 0, 1, and 2 are complete and documented; Phase 3 (secondary views) is next.**

## How to run / preview
- **Live:** https://gitlostinthesauce.github.io/InsubordinateandChurlish_VCflow/
- **Repo:** https://github.com/GitLostintheSauce/InsubordinateandChurlish_VCflow (local: `/Users/eleanor/InsubordinateandChurlish_VCflow`, default branch `main`)
- **Local preview** (CSVs need HTTP, not `file://`):
  ```bash
  cd /Users/eleanor/InsubordinateandChurlish_VCflow && python3 -m http.server 8000
  # then open http://localhost:8000
  ```

## Current state
- **Stack:** single `index.html` loads `data/*.csv` via `d3.csv()` and renders charts in-browser. No build step, no backend. (Began as Streamlit+Plotly; that was retired — Pages can't run it.)
- **Charts live now:** (1) funding by sector per year (multi-line, log/linear toggle), (2) 100% share-of-pie stacked bars, (3) Web3 quarterly cycle (Galaxy), (4) AI-energy nexus (selected rounds + data-center demand). Interactions: scale toggle, sector-focus chips, clickable legend filters, year selector, sticky section-nav.
- **Current theme:** dark, **orange primary `#ff7a18` / teal accent `#2dd4bf`**, Chakra Petch display font, JetBrains Mono labels, depth (gradients/glow). (Mimics gte.xyz, the company's site.)
- **Data:** `sector_annual.csv` (Crunchbase, 6 sectors × 4 years), `web3_quarterly.csv` (Galaxy, 16 quarters), `landmark_deals.csv` (145 cited deals), `energy_ai_funding.csv` + `energy_ai_ppa.csv`.
- **Docs complete:** `NARRATIVE.md` (4 shifts brief), `DATA_MODEL.md` (+ schema mapping), `sources.md` (feasibility matrix, raw-access note, per-figure citations + scope caveats), `PROMPTS.md` (live prompt log incl. tool comparison, pivot, QA).

## Key decisions & rationale (do NOT undo these)
- **No hallucinated numbers.** Every figure traces to a citation in `sources.md` or is marked `estimated` (rendered as hollow dots). 5 cells are estimated.
- **Quarterly → annual source-quality pivot (documented).** The cross-sector backbone is **annual Crunchbase** because clean public quarterly data for all 6 sectors doesn't exist without estimating ~96 cells. Only **Web3** is quarterly (Galaxy). This is why the *original* plan's per-quarter animated hero + **timeline scrubber were intentionally not built** — a scrubber over 4 annual points adds nothing, and a 6-sector quarterly scrubber would require fabricated data. Recorded in `PROMPTS.md`.
- **One source per sector line.** Backbone is all-Crunchbase so cross-sector levels are comparable; CB Insights / PitchBook are context-only (their scopes differ).
- **Defense = defense-tech only** (space removed) to avoid mixing definitions.
- **AI-energy chart = selected named rounds, not a market total** (it under-counts); the card leads with published aggregates + an honest caveat.

## Gotchas / watch-outs
- **Uncommitted work right now:** documentation updates to `PROMPTS.md`, `sources.md`, `DATA_MODEL.md`, `README.md`, and this `HANDOFF.md` are on disk, not yet committed. (Commit them to `main`.)
- **Always `git fetch` before pushing.** Another session has pushed to `main` mid-work before; pull/rebase first to avoid clobbering.
- **Stale branch** `redesign-orange-gte` (a superseded standalone redesign) can be deleted. Old PR #1 (a status-line handoff) may still be open on GitHub.
- **Needs YOUR hands (can't be done by the agent), all flagged in `PROMPTS.md`:**
  - Confirm the personal verdicts in the Phase-0 tool-comparison entry (TODOs left in place).
  - Claude Desktop **Project + screenshot** (external app).
  - **Live in-browser QA**: open the live URL in incognito, confirm **zero console errors**, click every control, check ~375px mobile width. Log fixes in `PROMPTS.md`.

## Next steps — Phase 3 (secondary views, ~4h)
Build only views the data supports; each should answer something the hero charts can't. Recommended order:
1. **Deals leaderboard** — render `landmark_deals.csv` filtered by sector + (optionally) year: company, round type, amount, lead investor, source link. Real data already exists (145 deals).
2. **Sector comparison view** — pick 2–3 sectors, show total funding / deal count / % change over the period side by side, with sector pickers.
3. **(Optional / stretch)** a data table with source links. **Do NOT** build a Sankey/stage-flow unless real stage data exists — it doesn't, so skip it (and log why).
- Keep the orange/teal theme and the honesty conventions (caveats visible, sources linked, estimates marked).

## Map of key files
| File | Purpose |
|---|---|
| `index.html` | the entire dashboard (markup + CSS + D3) |
| `data/sector_annual.csv` | ★ backbone — Crunchbase annual, 6 sectors × 4 yrs |
| `data/web3_quarterly.csv` | ★ Web3 quarterly deep dive (Galaxy) |
| `data/landmark_deals.csv` | 145 cited deals — **input for the Phase 3 leaderboard** |
| `data/energy_ai_funding.csv`, `energy_ai_ppa.csv` | AI-energy section data |
| `NARRATIVE.md` | 1-page brief (4 big shifts) → source for insight cards (Phase 4) |
| `DATA_MODEL.md` | data shapes, stack decision, schema mapping |
| `sources.md` | feasibility matrix, citations, scope caveats |
| `PROMPTS.md` | live prompt log (tool comparison, pivot, QA) |
| `Plan.md` | the data-gathering playbook |
