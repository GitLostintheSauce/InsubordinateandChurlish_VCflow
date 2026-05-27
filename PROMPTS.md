# Prompt Log

Live log of significant LLM prompts used to build this project. Reconstructing on Friday produces fiction; capturing live produces truth.

> **This is a historical record.** Earlier entries reference tooling that was later retired (e.g. the initial Streamlit + Plotly scaffold). For the *current* architecture, see `README.md` — this project is now a vanilla HTML + D3 static site.

Format per entry:
- **Date / Tool**: when and which LLM
- **Prompt**: what was asked (paste verbatim if significant)
- **Output usable?**: yes / partial / no — and why

---

## 2026-05-20 — Project kickoff

- **Tool**: Claude Code (Opus 4.7)
- **Prompt**: Pasted the project brief verbatim and asked Claude to scaffold a Streamlit + Plotly project with a GitHub remote, picking one primary VC data source.
- **Output usable?**: Yes — produced the initial folder, venv, `app.py` skeleton with 4 features, `requirements.txt`, `README.md`, `sources.md`, this prompt log, and pushed to GitHub.

---

## 2026-05-20 — Phase 0: deploy + realign stack (Perplexity + Claude Code)

- **Tool**: Perplexity (chart code) + Claude Code (deploy/review)
- **Prompt**: Asked Perplexity to build a single-file HTML + D3 bar chart of VC funding 2022–2025. Used Claude Code to deploy it to GitHub Pages and flag the data.
- **Output usable?**: Yes — Perplexity's D3 page became `index.html` and is live on Pages. Realigned project from Streamlit to vanilla HTML+D3 (Streamlit can't run on Pages). Perplexity's example funding numbers were **unverified**, so flagged on-page + per-row `source: TODO`; credited Perplexity in the footer.

## 2026-05-20 — Phase 1: data model + start sourcing (Claude Code + Perplexity)

- **Tool**: Claude Code (data model) + Perplexity (sourcing — in progress)
- **Prompt**: Built `data/vc_by_sector.csv` (96 blank rows: 6 sectors × 16 quarters, source=TODO) and `data/landmark_deals.csv`. Routing the actual number-gathering to Perplexity, one quarter at a time, primary source CB Insights State of Venture. (Paste reusable prompt + results here as you go.)
- **Output usable?**: TBD — filling cells as Perplexity returns cited figures.

---

## 2026-05-22 — Phase 1 close: stack + data model + narrative (t6, t7)

- **Tool**: Claude Code (Opus 4.7)
- **Stack decision (t6)**: *"I'm using vanilla HTML + D3.js with flat CSV data on GitHub Pages, because it deploys as a static site with no build step and keeps hand-curated data easy to edit/diff — a framework adds tooling with zero payoff for a 3–4 chart dashboard."* CSV instead of `data.json` (curated by hand; D3 loads CSV natively). Full data model in `DATA_MODEL.md`.
- **Narrative brief (t7)**: `NARRATIVE.md` — 4 shifts (AI's takeover → ~50% of all VC; concentration into mega-rounds; the crypto boom-bust-rebuild cycle; rotation to hard tech/defense). Climate/Biotech flagged as scope-shaky, not drawn as confident trends.
- **Output usable?**: Yes — both deliverables done. Phase 1 substantially complete at the time (backbone 21/24, 158 deals). Later cleanup narrowed the dashboard sector from "Defense & Space" to "Defense" and removed space-only/double-count-prone deal rows, leaving 145 landmark deals.

---

## 2026-05-27 — Phase 0 tool comparison (t1) [summary from memory — confirm personal verdicts]

The single small task used to compare the three required tools: **"scaffold a single-file HTML page that renders a VC-funding bar chart from flat data."**

| Tool | What it produced on the task | Where it helped / failed |
|---|---|---|
| **Perplexity** (sourced research) | A working single-file HTML + D3 bar chart, plus example funding numbers. | Helped: fastest path to runnable D3; good for cited sourcing later. Failed: its example numbers were **unverified** — had to flag every row `source: TODO` and re-source from Crunchbase. |
| **Claude Code** (code agent) | Repo scaffold, data files, deploy to GitHub Pages, multi-file edits, review. | Helped: full-project context — file edits, git, deploy, refactors (e.g. Streamlit→D3 realignment, Defense scope cleanup). Best for anything touching multiple files. |
| **Claude Desktop / ChatGPT** (conversational) | *[TODO: your verdict — used for reasoning/design discussion? add your own take here.]* | *[TODO: confirm how it felt vs the code agent.]* |

> ⚠️ The subjective "how each felt" judgments are yours to confirm — this entry reconstructs the factual side from the repo's history; replace the TODOs with your real impressions.

---

## 2026-05-27 — Phase 1 decision: source-quality pivot, quarterly → annual (the documented pivot)

**Decision:** the cross-sector backbone is **annual** (Crunchbase, all 6 sectors), not quarterly. Only **Web3** is carried at quarterly grain (Galaxy Digital), as a clearly-labeled sector deep dive.

**Why the pivot from the original "quarterly for all 6 sectors" plan:**
- A 6-sector × 16-quarter grid (96 cells) cannot be filled from free, public sources without mixing provider definitions or **estimating most cells** — which would violate the project's no-hallucinated-numbers rule.
- Crunchbase publishes clean *annual* sector totals under one consistent "VC-backed startup" definition, so annual figures are genuinely **comparable across sectors**. Forcing them to quarterly would manufacture false precision.
- Galaxy publishes consistent *quarterly* crypto VC, so Web3 — the audience's market — keeps its quarterly cycle view honestly.

**What this means for the deliverables:** the regular plan's quarterly hero + timeline scrubber (t9/t10) are **intentionally not built**, because the cross-sector data is annual; a scrubber over 4 annual points adds nothing over the existing year selector, and a 6-sector quarterly scrubber would require data we won't fabricate. This is the source-quality-first call the revised plan explicitly rewards (an undocumented pivot looks accidental; this one is deliberate and recorded).

---

## 2026-05-27 — Phase 2 QA pass (t20/t21) [summary from memory]

- **Live URL** https://gitlostinthesauce.github.io/InsubordinateandChurlish_VCflow/ — page and all four data CSVs return HTTP 200 on GitHub Pages (verified via request checks).
- **Data loading** — charts read `data/*.csv` via `d3.csv()`; no hardcoded chart values. Cache-busting `?v=` query is in place.
- **Interactions** — scale toggle, sector-focus chips, clickable legend filters, year selector, sticky section-nav all wired in the source.
- **Caveats** — estimated cells render as hollow dots; Climate/Biotech scope-shift caveats shown on-page.
- ⚠️ **Still needs a human browser check** (I can't run a live DOM/console session): open the live URL in a clean/incognito window, confirm **zero console errors**, click every control, and check a ~375px mobile width. Log any fixes here.

---

## Template for future entries

### YYYY-MM-DD — short title

- **Tool**:
- **Prompt**:
- **Output usable?**:
