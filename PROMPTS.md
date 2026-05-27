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

## 2026-05-25 — Codex repo audit and plan alignment

- **Tool**: Codex (GPT-5) with GitHub plugin + local repo access.
- **Prompt**: Asked Codex to connect to `GitLostintheSauce/InsubordinateandChurlish_VCflow`, inspect the repo, read the two intern plan files, and discuss where the project stood relative to the plan.
- **Output usable?**: Yes. Codex cloned the repo, inspected `README.md`, `DATA_MODEL.md`, `NARRATIVE.md`, `sources.md`, `index.html`, and the CSVs. It identified that the revised plan mattered more than the original plan because it allowed the source-quality-first pivot from quarterly-everywhere to an annual Crunchbase backbone plus Web3 quarterly deep dive. It placed the project at Phase 0/1 complete and Phase 2 in progress, with Phase 3 not yet started.

## 2026-05-25 — Codex docs cleanup and Defense-only scope

- **Tool**: Codex (GPT-5) with local file editing, validation, git, and GitHub push.
- **Prompt**: Asked Codex to update stale docs, remove Space from the dashboard scope, explain how to finish the prompt/process record, and keep Phase 0/1/2 clean before moving into Phase 3.
- **Output usable?**: Yes. Codex updated `README.md`, `DATA_MODEL.md`, `Plan.md`, `sources.md`, and `PROMPTS.md`; renamed the annual dashboard sector from `Defense & Space` to `Defense`; removed Space-only and Dual-Use rows from `landmark_deals.csv`; replaced the mixed raw source file with `data/raw/defense_vc_2022_2025.csv`; and committed/pushed `e583393` (`Align docs and defense sector scope`).
- **Judgment call**: The dashboard should not claim "Defense & Space" while the annual backbone uses Crunchbase's narrow defense-tech definition. Removing Space made the data less flashy but more defensible.

## 2026-05-25 — Codex bug fix: Defense visibility

- **Tool**: Codex (GPT-5) with local server checks and GitHub push.
- **Prompt**: Reported that Defense no longer appeared clearly on the dashboard graphs after the sector rename.
- **Output usable?**: Yes. Codex diagnosed two issues: the browser could cache old CSV rows labeled `Defense & Space`, and the linear chart buried tiny Defense values near the baseline. It normalized old `Defense & Space` rows to `Defense`, cache-busted CSV URLs, made log scale the default, thickened Defense styling, verified served CSV rows locally, and committed/pushed `1dc1ddb` (`Make defense visible in dashboard charts`).
- **Lesson**: Data renames need visual QA, not just CSV checks. A technically correct line can still be invisible if the chart scale hides it.

## 2026-05-26 — Codex Phase 2 UI/UX polish

- **Tool**: Codex (GPT-5) with in-app browser QA.
- **Prompt**: Asked Codex to make the dashboard feel shockingly professional, remove emoji, focus on the user, improve flow, and add more interaction.
- **Output usable?**: Yes. Codex rebuilt `index.html` into a more polished analyst dashboard: executive hero, KPI tiles, sticky section navigation, sector focus controls, year selector, cleaner chart containers, better tooltips, a more professional AI-energy section, no visible emoji, and cache-busted data loading. It verified the page in the in-app browser, checked for console errors, tested Defense focus and year selection, and committed/pushed `636d144` (`Polish dashboard UI and interactions`).
- **Lesson**: Codex was especially useful for the "tight loop" of edit -> run local server -> inspect in browser -> fix UX issue -> commit.

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

## 2026-05-27 — Phase 3 decision: no deal-count / median-round-size metric (a second documented pivot)

**Context:** building the Phase 3 **sector comparison** view. The original plan envisioned comparing sectors on funding *and* deal count *and* median round size. Tested whether the backbone could honestly support deal count / median.

**Tool:** Claude Code (read the data) + Web search against Crunchbase's own end-of-year reports.

**Finding — deal count is only partially available, and the gaps are real, not lazy:**
- `sector_annual.csv` already carries clean Crunchbase deal counts for **Fintech 2024–25, Defense 2022–24, Web3 2022–24**. Those stay.
- **AI, Climate, Biotech counts are blank by design.** Crunchbase reports AI in *dollars and share of total* but publishes **no comparable annual AI deal count** — confirmed against its [AI EOY 2024](https://news.crunchbase.com/venture/global-funding-data-analysis-ai-eoy-2024/) and [AI trends EOY 2025](https://news.crunchbase.com/ai/big-funding-trends-charts-eoy-2025/) write-ups. The count-shaped numbers in circulation are **different scopes** ("~10,500 rounds" = all North American sectors; "250 companies" = one month), so using one as an "AI deal count" would mix definitions and fabricate a figure.
- Climate (equity-only → all-stages scope flips) and Biotech (US-only vs global) have no clean per-year counts for the same scope reasons already documented for their funding lines.

**Finding — median round size cannot be computed honestly:** it requires deal-level distribution data the project does not hold. *Average* round size (funding ÷ count) is derivable only where both numbers are real (labeled "derived"); a median over the 145 curated landmark deals is biased to large rounds and would misrepresent the market.

**Decision:** the comparison view reports **funding totals + % change** for all sectors, **deal count only where Crunchbase published it** (blanks shown as "not published," not invented), and an optional **derived** average round size where both inputs exist. No median. Same source-quality-first logic as the [quarterly → annual pivot](#2026-05-27--phase-1-decision-source-quality-pivot-quarterly--annual-the-documented-pivot); recorded so the gap reads as a judgment call, not an omission. Also logged in `README.md` (Data principles).

---

## Tool judgment: when to use Codex vs. Claude Code

Use **Codex** when the task is tightly connected to the repository state and needs execution, verification, and GitHub operations in one loop:

- repo inspection and "where are we actually?" audits
- precise multi-file edits with diffs
- data cleanup that needs validation scripts or CSV sanity checks
- local browser QA after frontend changes
- debugging a visual/runtime issue from user feedback
- committing and pushing a scoped change

Use **Claude Code / Claude Desktop** when the task benefits more from broad reasoning, writing, or early architecture:

- brainstorming the dashboard concept and narrative
- drafting the first data model or research plan
- synthesizing sourced research into a coherent story
- writing narrative briefs, caveats, and analysis copy
- exploring several design or data-model directions before choosing one

Practical rule for future projects: use Claude to think through the shape of the work; use Codex when it is time to make the repo match that decision, test it, and ship it. They overlap, but Codex felt strongest here during late Phase 2: cleanup, validation, UI polish, browser verification, and GitHub publishing.

---

## Template for future entries

### YYYY-MM-DD — short title

- **Tool**:
- **Prompt**:
- **Output usable?**:
