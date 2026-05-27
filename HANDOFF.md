# Session Handoff — VCflow Dashboard

*Regenerated 2026-05-27. Paste this into a new session (or point it at this file) to get fully caught up.*

## TL;DR
**VCflow** is an interactive dashboard showing how venture capital reallocated across 6 sectors (AI, Fintech, Climate, Defense, Web3, Biotech) from 2022→2025. Static **vanilla HTML + D3**, deployed on **GitHub Pages**. It's an intern Week-1 project graded (revised-plan rubric) on source rigor 35% / dashboard clarity 25% / adaptive reasoning 20% / prompt-tool docs 20%. **Phases 0–3 are complete, committed, and pushed live.** Phase 4 (polish + insight cards) and Phase 5 (reflection/submission) are what's left.

## How to run / preview
- **Live:** https://gitlostinthesauce.github.io/InsubordinateandChurlish_VCflow/
- **Repo:** https://github.com/GitLostintheSauce/InsubordinateandChurlish_VCflow (local: `/Users/eleanor/InsubordinateandChurlish_VCflow`, default branch `main`)
- **Local preview** (CSVs need HTTP, not `file://`):
  ```bash
  cd /Users/eleanor/InsubordinateandChurlish_VCflow && python3 -m http.server 8000
  # then open http://localhost:8000
  ```
- **Quick JS syntax check** (no node installed; use macOS JavaScriptCore):
  ```bash
  awk '/<script>$/{f=1;next} /<\/script>/{f=0} f' index.html > /tmp/s.js
  osascript -l JavaScript -e 'ObjC.import("Foundation"); var s=$.NSString.stringWithContentsOfFileEncodingError("/tmp/s.js",4,null).js; try{new Function(s);"PARSE OK"}catch(e){"ERR: "+e}'
  ```

## Current state
- **Stack:** single `index.html` loads `data/*.csv` via `d3.csv()` (one `Promise.all`) and renders everything in-browser. No build step, no backend. (Began as Streamlit+Plotly; retired early — Pages can't run it.)
- **Latest commit:** `3a90def` "Phase 3: deals leaderboard, sector comparison, megaround insights + UX overhaul" — **pushed to `origin/main`, working tree clean.**
- **Sections live now (8 nav tabs, indexed 01–08):**
  1. **Overview** — funding by sector per year (multi-line, log/linear toggle)
  2. **Capital Share** — 100% stacked bars, year selector
  3. **Web3 Cycle** — quarterly Galaxy data (peak → winter → rebuild)
  4. **AI-Energy** — selected power rounds + data-center demand (labeled illustrative, not a market total)
  5. **Deals** — landmark deals leaderboard (filter by sector/year, click-to-sort, per-row source links, ⚠️ caveat flag on 24 deals)
  6. **Compare** — sector comparison: rebased-to-2022 (=100) growth chart for 2–3 picked sectors + stat cards (total funding, % change, sourced deal count, derived avg round size)
  7. **Megarounds** — *"The anatomy of the megaround era"*, 4 views computed live from `landmark_deals.csv`:
     - **Megaround escalation** scatter (avg deal $440M→$2.6B 2022→2025)
     - **Capital magnets** bubble pack (OpenAI/Anthropic/xAI ≈ half of all $197B)
     - **King vs crowd concentration** bars (AI top-3 = 53% vs Web3 top-3 = 29%)
     - **US vs rest-of-world geography** (AI 99% US, Climate ~70% non-US)
  8. **Sources** — source-discipline note
- **UX:** dark, orange `#ff7a18` / teal `#2dd4bf`, Chakra Petch display + JetBrains Mono labels. Recent overhaul (commit `3a90def`): terminal stat-readout KPI strip, indexed nav tabs, grain texture, crisper 1px borders / tight radii, **scroll-synced nav** + **reveal-on-scroll** motion (IntersectionObserver; opt-in via `body.anim` + 2.5s safety net so content never hides if JS fails; respects `prefers-reduced-motion`).
- **Data:** `sector_annual.csv` (Crunchbase, 6 sectors × 4 years, partial deal_count), `web3_quarterly.csv` (Galaxy, 16 quarters), `landmark_deals.csv` (145 cited deals), `energy_ai_funding.csv` + `energy_ai_ppa.csv`.
- **Docs complete:** `NARRATIVE.md`, `DATA_MODEL.md`, `sources.md`, `PROMPTS.md` (live prompt log, two documented pivots), `README.md`.

## Key decisions & rationale (do NOT undo these)
- **No hallucinated numbers.** Every figure traces to a citation in `sources.md` or is marked `estimated` (hollow dots). The megaround views are computed directly from `landmark_deals.csv` — verified with Python, not invented.
- **Quarterly → annual source-quality pivot (documented in `PROMPTS.md`).** Cross-sector backbone is **annual Crunchbase** (clean quarterly for all 6 sectors doesn't exist without estimating ~96 cells). Only **Web3** is quarterly (Galaxy). This is why the original plan's per-quarter animated hero + **timeline scrubber were intentionally not built**.
- **Deal-count / median pivot (documented in `PROMPTS.md` + README Data principles).** The Compare view shows funding + % change for all, but **deal count only where Crunchbase published it** (Fintech 2024–25, Defense 2022–24, Web3 2022–24). AI/Climate/Biotech show **"not published"** — confirmed via Crunchbase's own EOY reports that no comparable annual count exists. **Median round size deliberately omitted** (needs deal-level distribution we don't have). Do not fabricate these to "fill" the column.
- **Sankey / stage-flow view deliberately NOT built** — no real stage-level data exists; building one would require fabrication. The plan rewards this documented skip.
- **One source per sector line; specialized deep dives stay labeled separate** (Galaxy Web3, AI-energy named rounds).
- **Defense = defense-tech only** (space removed) to avoid mixing definitions.

## Gotchas / watch-outs
- **No `node` on this machine.** Use the JavaScriptCore syntax-check snippet above; can't run a headless browser here either.
- **`index.html` is NOT cache-busted** (only the CSVs have `?v=`). After editing, **hard-refresh** the browser (`Cmd+Shift+R`) or you'll see stale markup/CSS.
- **Always `git fetch` before pushing.** Another session has pushed to `main` mid-work before; pull/rebase first.
- **Needs YOUR (the human's) hands** — flagged in `PROMPTS.md`, none done by the agent:
  - **Live in-browser QA** on the deployed site: open the live URL incognito, confirm **zero console errors**, click all 8 nav tabs, hover bubbles/scatter dots/⚠️ flags, check ~375px mobile width. *(Pushed but not yet human-verified on live.)*
  - Confirm the personal verdicts in the Phase-0 tool-comparison entry (TODOs left in `PROMPTS.md`).
  - Claude Desktop **Project + screenshot** (external app).
- **Stale branch** `redesign-orange-gte` may still exist remotely and can be deleted. Old PR #1 (a status-line handoff) may still be open on GitHub.

## Next steps — Phase 4 (polish + insight layer, ~3h), then Phase 5
1. **Phase 4 — insight cards.** Add 8–12 prewritten insight cards (static JSON or inline) keyed to sector/year moments, surfaced as the user explores. **Do NOT call an LLM API from the live site** (no key on a static page). Source them from `NARRATIVE.md` + the megaround findings (e.g. "3 AI labs raised ~half of all landmark capital"; "avg deal $440M→$2.6B"; "Web3 = a crowd, AI = a king").
2. **Phase 4 — polish pass.** Typography/animation/responsiveness; fix anything the live QA surfaces; confirm 375px width.
3. **Phase 5 — reflection/submission.** Clean up annotated `PROMPTS.md` by phase; write retro + tool memo (1 page); draft 3 data-backed insight posts; record 5-min walkthrough; compile submission index (repo, live URL, prompt log, narrative, data, retro, recording).
- Keep the orange/teal theme + honesty conventions (caveats visible, sources linked, estimates marked) throughout.

## Map of key files
| File | Purpose |
|---|---|
| `index.html` | the entire dashboard (markup + CSS + all D3). ~1120 lines. |
| `data/sector_annual.csv` | ★ backbone — Crunchbase annual, 6 sectors × 4 yrs (deal_count partial) |
| `data/web3_quarterly.csv` | ★ Web3 quarterly deep dive (Galaxy) |
| `data/landmark_deals.csv` | ★ 145 cited deals — powers Deals leaderboard + all 4 Megaround views |
| `data/energy_ai_funding.csv`, `energy_ai_ppa.csv` | AI-energy section data |
| `data/raw/` | source-of-record research files (provenance) |
| `NARRATIVE.md` | 1-page brief (4 big shifts) → source for Phase-4 insight cards |
| `DATA_MODEL.md` | data shapes, stack decision, schema mapping |
| `sources.md` | feasibility matrix, citations, scope caveats |
| `PROMPTS.md` | live prompt log + both documented pivots (quarterly→annual, deal-count) |
| `Plan.md`, `plan_energy_AI.md` | data-gathering playbooks |
| `README.md` | project overview + Data principles (incl. deal-count rationale) |
