# Session Handoff — VCflow Dashboard

*Regenerated 2026-06-09. Paste this into a new session (or point it at this file) to get fully caught up.*

## TL;DR
**VCflow** is an interactive dashboard showing how venture capital reallocated across 6 sectors (AI, Fintech, Climate, Defense, Web3, Biotech) from 2022→2025. Static **vanilla HTML + D3**, deployed on **GitHub Pages**. It's an intern Week-1 project graded (revised-plan rubric) on source rigor 35% / dashboard clarity 25% / adaptive reasoning 20% / prompt-tool docs 20%. **Phases 0–4 are complete, committed, and pushed live.** Phase 5 (reflection + submission) is what's left — start with **t27 (prompt log cleanup); see `CODEX_KICKOFF.md`**.

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
- **Stack:** single `index.html` (~1212 lines) loads `data/*.csv` via `d3.csv()` (one `Promise.all`) and renders everything in-browser. No build step, no backend. (Began as Streamlit+Plotly; retired early — Pages can't run it.)
- **Latest commit:** `b273294` "Phase 4: insight cards + analyst-layer polish" — **pushed to `origin/main`, working tree clean.**
- **Page structure (top → bottom):**
  1. Hero + 4 KPIs (AI funding $211B · **Concentration ~$93B** · Web3 rebound $8.5B · Defense record $7.7B)
  2. Sticky 8-tab nav (Overview → Capital Share → Web3 Cycle → AI-Energy → Deals → Compare → Megarounds → Sources)
  3. Executive read intro
  4. **Headline insights panel — NEW in Phase 4** — 12 sourced insight cards, 3→2→1-col responsive, sector-tinted left borders
  5. Eight numbered panels matching the nav
- **Sections live now (8 nav tabs, indexed 01–08):**
  1. **Overview** — funding by sector per year (multi-line, **linear default**, log toggle — Phase 4 changed default from log to linear so AI's dominance is honest on first view)
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

## Gotchas / watch-outs
- **No `node` on this machine.** Use the JavaScriptCore syntax-check snippet above; can't run a headless browser here either.
- **`index.html` is NOT cache-busted** (only the CSVs have `?v=`). After editing, **hard-refresh** the browser (`Cmd+Shift+R`) or you'll see stale markup/CSS.
- **Always `git fetch` before pushing.** Another session has pushed to `main` mid-work before; pull/rebase first.
- **Needs YOUR (the human's) hands** — flagged in `PROMPTS.md`, none done by the agent:
  - **Live in-browser QA** on the deployed site: open the live URL incognito, confirm **zero console errors**, click all 8 nav tabs, hover bubbles/scatter dots/⚠️ flags, check ~375px mobile width. *(Phase 4 pushed but not yet human-verified on live — specifically: insight grid renders 12 cards, Overview opens linear, KPI #2 reads $93B, Biotech is magenta and Defense is steel in every chart, insight-card left borders show correct sector tints.)*
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
| `index.html` | the entire dashboard (markup + CSS + all D3). ~1212 lines. **Phase 4 added:** `INSIGHTS` array (~line 471), `renderInsights()` function (~line 641), `.insights` / `.insight` CSS block, `<section class="insights" id="headline-insights">` between executive intro and Overview, hero KPI swap, scale default `linear`, recolored `--Biotech` / `--Defense` and matching JS `COLOR` map. |
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
