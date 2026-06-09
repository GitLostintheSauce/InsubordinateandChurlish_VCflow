# Session Handoff — VCflow Dashboard

*Regenerated 2026-06-09 (post content-cleanup). Paste this into a new session (or point it at this file) to get fully caught up.*

## TL;DR
**VCflow** is an interactive dashboard showing how venture capital reallocated across 6 sectors (AI, Fintech, Climate, Defense, Web3, Biotech) from 2022→2025. Static **vanilla HTML + D3**, deployed on **GitHub Pages**. It's an intern Week-1 project graded (revised-plan rubric) on source rigor 35% / dashboard clarity 25% / adaptive reasoning 20% / prompt-tool docs 20%. **Phases 0–4 are complete, committed, and pushed live.** A late content-cleanup pass (post Phase-4) followed the founder-lens critique: page now leads with the concentration thesis, reorders sections for inverted emphasis (Concentration → Deals → Macro → …), drops the redundant "Source discipline" section in favor of a top-of-page methodology strip, slims the AI-Energy chrome, and date-stamps the hero figures. Phase 5 (reflection + submission) is what's left — start with **t27 (prompt log cleanup); see `CODEX_KICKOFF.md`**.

## How to run / preview
- **Live:** https://gitlostinthesauce.github.io/InsubordinateandChurlish_VCflow/
- **Repo:** https://github.com/GitLostintheSauce/InsubordinateandChurlish_VCflow (local: `/Users/eleanor/InsubordinateandChurlish_VCflow`, default branch `main`)
- **Local preview** (CSVs need HTTP, not `file://`):
  ```bash
  cd /Users/eleanor/InsubordinateandChurlish_VCflow && python3 -m http.server 8000
  # then open http://localhost:8000
  ```
- **Phase-4 static QA** (re-runnable; verifies JS parse + 17 anchors):
  ```bash
  ./scripts/phase4_check.sh
  ```
- **Quick JS syntax check** (no node installed; use macOS JavaScriptCore):
  ```bash
  awk '/<script>$/{f=1;next} /<\/script>/{f=0} f' index.html > /tmp/s.js
  osascript -l JavaScript -e 'ObjC.import("Foundation"); var s=$.NSString.stringWithContentsOfFileEncodingError("/tmp/s.js",4,null).js; try{new Function(s);"PARSE OK"}catch(e){"ERR: "+e}'
  ```

## Current state
- **Stack:** single `index.html` (~1206 lines) loads `data/*.csv` via `d3.csv()` (one `Promise.all`) and renders everything in-browser. No build step, no backend. (Began as Streamlit+Plotly; retired early — Pages can't run it.)
- **Latest commit:** *(updated each session — see `git log --oneline -1`)*. Working tree should be clean.
- **Page structure (top → bottom, post content-cleanup):**
  1. **Hero** — opinionated thesis (*"It wasn't a rotation. It was a concentration event."*) + 4 date-stamped KPIs (AI funding $211B FY2025 · **Concentration ~$93B** · Web3 rebound $8.5B Q4 2025 · Defense record $7.7B FY2025) + 3 CTAs pointing at #thesis / #deals-section / #methodology
  2. **Sticky 6-tab nav** — Concentration → Deals → Macro → Web3 Cycle → AI-Energy → Compare (down from 8; "Sources" folded into the top methodology strip, "Overview" + "Capital Share" merged into "Macro")
  3. **Methodology strip** (`#methodology`) — 4-line micro-grid (Backbone · Web3 deep dive · AI-energy · Deals leaderboard) + a one-line sources/estimates note. Replaces the old "Executive read" intro.
  4. **Headline insights panel** — 12 sourced insight cards, 3→2→1-col responsive, sector-tinted left borders
  5. **Six analytical sections in the new order:**
     1. **Concentration** (`#thesis`, section-label) — the spine of the dashboard, 4 panels computed live from `landmark_deals.csv`: megaround escalation ($440M→$2.6B), capital magnets (3 labs ≈ half of $197B), king-vs-crowd (AI 53% top-3 vs Web3 29%), US-vs-RoW geography (AI ~99% US, Climate ~70% non-US)
     2. **Deals** (`#deals-section`, panel `.num` 2) — the 145-deal leaderboard, framed as "the product"; filter by sector/year, click-to-sort, per-row source links, ⚠️ flag on 24 deals
     3. **Macro context** (`#macro-section`, panel `.num` 3) — merged old Overview + Capital Share into one panel with two sub-headings; linear-default line chart + stacked-share bars
     4. **Web3 Cycle** (`#web3-section`, panel `.num` 4) — Galaxy quarterly (peak → winter → rebuild); copy now leads with the Q4 2025 $8.5B fact
     5. **AI-Energy** (`#energy-section`, section-label) — single slimmed panel with 2 sub-charts (selected rounds + data-center demand) and 1 consolidated methodology `<details>` (was 2 panels + 3 Q&A boxes + 2 `<details>`)
     6. **Compare** (`#compare-section`, panel `.num` 6) — rebased-to-2022 (=100) head-to-head + stat cards (funding, % change, sourced deal count, derived avg round size)
- **UX:** dark, orange `#ff7a18` / teal `#2dd4bf`, Chakra Petch display + JetBrains Mono labels. Phase-4 polish: Biotech recolored to **magenta `#e879d4`** and Defense to **steel `#9ca0a8`** so neither shares hue with the `--danger` / `--warn` semantic tokens. Hero KPI #2 swapped from the basket-dependent "AI share 56%" to the concentration stat "~$93B / 3 AI labs ≈ half of $197B."
- **Data:** `sector_annual.csv` (Crunchbase, 6 sectors × 4 years, partial deal_count), `web3_quarterly.csv` (Galaxy, 16 quarters), `landmark_deals.csv` (145 cited deals), `energy_ai_funding.csv` + `energy_ai_ppa.csv`.
- **Docs complete:** `NARRATIVE.md`, `DATA_MODEL.md`, `sources.md`, `PROMPTS.md` (live prompt log, two documented pivots — **needs Phase 5 t27 cleanup pass: Phase 3 and Phase 4 entries are missing, and a couple of TODOs in the Phase-0 tool-comparison table are still flagged for the human**), `README.md`.

## Key decisions & rationale (do NOT undo these)
- **No hallucinated numbers.** Every figure traces to a citation in `sources.md` or is marked `estimated` (hollow dots). The megaround views are computed directly from `landmark_deals.csv` — verified with Python, not invented.
- **Quarterly → annual source-quality pivot (documented in `PROMPTS.md`).** Cross-sector backbone is **annual Crunchbase** (clean quarterly for all 6 sectors doesn't exist without estimating ~96 cells). Only **Web3** is quarterly (Galaxy). This is why the original plan's per-quarter animated hero + **timeline scrubber were intentionally not built**.
- **Deal-count / median pivot (documented in `PROMPTS.md` + README Data principles).** The Compare view shows funding + % change for all, but **deal count only where Crunchbase published it** (Fintech 2024–25, Defense 2022–24, Web3 2022–24). AI/Climate/Biotech show **"not published"** — confirmed via Crunchbase's own EOY reports that no comparable annual count exists. **Median round size deliberately omitted** (needs deal-level distribution we don't have). Do not fabricate these to "fill" the column.
- **Sankey / stage-flow view deliberately NOT built** — no real stage-level data exists; building one would require fabrication. The plan rewards this documented skip.
- **One source per sector line; specialized deep dives stay labeled separate** (Galaxy Web3, AI-energy named rounds).
- **Defense = defense-tech only** (space removed) to avoid mixing definitions.
- **(Phase 4) Hero KPI #2 = the concentration stat, not "AI share 56%."** "56% of tracked sectors" is mechanically a function of which six sectors were picked; the concentration stat (~$93B / 3 AI labs ≈ half of $197B) is computed from `landmark_deals.csv` and is the project's most-quotable, most-defensible fact. Do not revert.
- **(Phase 4) Default chart scale = linear.** Log is a toggle for inspecting small sectors. The README's own thesis is "AI dwarfs everything"; defaulting to log was muting that. Sector focus filter handles small-sector readability instead.
- **(Phase 4) Biotech = magenta, Defense = steel.** Old hues `#ff7575` and `#ffd76b` collided with the `--danger` and `--warn` semantic tokens (and `#ffd76b` was also the "Estimated" tooltip color). The recolor freed those hues for pure semantic use. Do not swap back without a colorblind-safe and semantic-clean replacement plan.
- **(Phase 4) `INSIGHTS` is a hand-curated JS array of 12 sourced cards** in `index.html`. Every claim traces to `sources.md` or to `landmark_deals.csv`. Extend only from sourced facts — do not generate cards from intuition.
- **(Post Phase-4 content cleanup) Page leads with the thesis, not the dashboards.** Hero h1 is one opinionated claim ("It wasn't a rotation. It was a concentration event."); section order is Concentration → Deals → Macro → Web3 → AI-Energy → Compare. The Concentration section is the spine, the Deals leaderboard is framed as "the product," and Macro is explicitly "context, not thesis." Do not revert to the equal-weight 8-section layout — the strategic critique that drove this was specifically that the old layout hedged.
- **(Post Phase-4 content cleanup) Methodology lives at the top, not at the bottom.** A 4-line `.methodology` strip (`#methodology`) sits between nav and the headline insights and replaces both the old "Executive read" `.intro` and the redundant section-08 "Source discipline" panel. Do not re-add either — the strip is the single source of methodology framing.
- **(Post Phase-4 content cleanup) Hero KPIs are date-stamped.** `FY2025 final · Crunchbase` etc. Don't drop the as-of qualifier; ambiguous "2025 annual total" is exactly what a skeptical reader flags.
- **(Post Phase-4 content cleanup) AI-Energy is slimmed.** The 3 Q&A `.answer` boxes ("Did energy VC rise?" etc.) are removed (they paraphrased what the charts said). The two `<details>` panels are consolidated into one. Don't re-bloat — the section's value is the second-order thinking, not the prose.

## Gotchas / watch-outs
- **No `node` on this machine.** Use the JavaScriptCore syntax-check snippet above; can't run a headless browser here either.
- **`index.html` is NOT cache-busted** (only the CSVs have `?v=`). After editing, **hard-refresh** the browser (`Cmd+Shift+R`) or you'll see stale markup/CSS.
- **Always `git fetch` before pushing.** Another session has pushed to `main` mid-work before; pull/rebase first.
- **Needs YOUR (the human's) hands** — flagged in `PROMPTS.md`, none done by the agent:
  - **Live in-browser QA** on the deployed site: open the live URL incognito, confirm **zero console errors**, click all **6** nav tabs, hover bubbles/scatter dots/⚠️ flags, check ~375px mobile width. *(Phase 4 + content-cleanup pushed but not yet human-verified on live — specifically: hero h1 reads as the thesis sentence, methodology strip renders 4-col on desktop / 1-col on mobile, Concentration is the first analytical section, Deals leaderboard is second, Macro panel renders both sub-charts under one header with the year-selector working, insight grid renders 12 cards, Biotech is magenta and Defense is steel in every chart.)*
  - **Confirm the personal verdicts** in the Phase-0 tool-comparison entry of `PROMPTS.md` (Claude Desktop / ChatGPT verdict line is still `[TODO: …]`).
  - Claude Desktop **Project + screenshot** (external app).
- **Stale branch** `redesign-orange-gte` may still exist remotely and can be deleted. Old PR #1 (a status-line handoff) may still be open on GitHub.
- **PROMPTS.md is structurally chronological**, not organized by phase, and is missing entries for Phase 3 (commit `3a90def`) and Phase 4 (commit `b273294`). t27 in Phase 5 is the cleanup pass — see `CODEX_KICKOFF.md`.

## Next steps — Phase 5 (reflection + submission, ~3h)
**Start here:** `CODEX_KICKOFF.md` — a self-contained one-paragraph kickoff for Codex (or any cold session) targeting t27 specifically.
1. **t27 — Clean up the annotated prompt log.** Re-organize `PROMPTS.md` by phase; add the missing Phase 3 + Phase 4 entries (anchored to real commits — `git log --oneline` is the source of truth); each entry must show tool choice + output quality + what changed because of the tool output; preserve the two documented pivots verbatim; surface the human-only TODOs explicitly rather than fabricating verdicts. See `CODEX_KICKOFF.md`.
2. **t28 — Write the retrospective and tool memo.** What you'd do differently, which tools were actually useful, top skill gaps. Draws on the cleaned-up prompt log.
3. **t29 — Draft three data-backed short-form insights.** Each one specific claim + specific number + caveat. Source from `NARRATIVE.md` and the 12 `INSIGHTS` cards.
4. **t30 — Record the 5-minute walkthrough.** Present to a time-constrained investor; insight, not feature narration.
5. **t31 — Compile the final submission index.** Repo, live URL, source audit, data files, narrative brief, prompt log, retrospective, recording.
- Keep the orange/teal theme + honesty conventions (caveats visible, sources linked, estimates marked) throughout.

## Map of key files
| File | Purpose |
|---|---|
| `index.html` | the entire dashboard (markup + CSS + all D3). ~1206 lines. **Phase 4 added:** `INSIGHTS` array, `renderInsights()` function, `.insights` / `.insight` CSS block, `<section class="insights" id="headline-insights">`, hero KPI swap, scale default `linear`, recolored `--Biotech` / `--Defense` + matching JS `COLOR` map. **Post-Phase-4 content cleanup:** hero rewritten as opinionated thesis, nav reduced 8→6 tabs and reordered (Concentration → Deals → Macro → Web3 → AI-Energy → Compare), `.intro` replaced with `.methodology` strip, Overview + Capital Share merged into one `#macro-section` panel with `.subhead` sub-headers, old `#insights-section` (Megarounds container) renamed to `#thesis`, `#sources-section` removed, AI-Energy slimmed (no Q&A, one `<details>`). All SVG IDs (`#lines`, `#stack`, `#web3`, `#escalation`, `#magnets`, `#concentration`, `#geography`, `#energyChart`, `#demandChart`, `#compare`) preserved — JS render functions untouched. |
| `data/sector_annual.csv` | ★ backbone — Crunchbase annual, 6 sectors × 4 yrs (deal_count partial) |
| `data/web3_quarterly.csv` | ★ Web3 quarterly deep dive (Galaxy) |
| `data/landmark_deals.csv` | ★ 145 cited deals — powers Deals leaderboard + all 4 Megaround views |
| `data/energy_ai_funding.csv`, `energy_ai_ppa.csv` | AI-energy section data |
| `data/raw/` | source-of-record research files (provenance) |
| `scripts/phase4_check.sh` | **NEW in Phase 4** — re-runnable static QA: JS parses, all Phase-4 anchors present, no sector still uses `--danger` / `--warn` hues. 17/17 currently passing. |
| `NARRATIVE.md` | 1-page brief (4 big shifts) → source for the 12 insight cards |
| `DATA_MODEL.md` | data shapes, stack decision, schema mapping |
| `sources.md` | feasibility matrix, citations, scope caveats |
| `PROMPTS.md` | live prompt log + both documented pivots (quarterly→annual, deal-count). **Needs t27 cleanup pass.** |
| `Plan.md`, `plan_energy_AI.md` | data-gathering playbooks |
| `README.md` | project overview + Data principles (incl. deal-count rationale) |
| `CODEX_KICKOFF.md` | **NEW** — one-paragraph kickoff for the next Codex session, targeting Phase 5 t27 specifically. |
