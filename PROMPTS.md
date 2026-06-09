# Prompt Log

Live log of significant LLM prompts used to build this project. Reconstructing on Friday produces fiction; capturing live produces truth.

> **This is a historical record.** Earlier entries reference tooling that was later retired (e.g. the initial Streamlit + Plotly scaffold). For the *current* architecture, see `README.md` — this project is now a vanilla HTML + D3 static site.

Format per entry:
- **Date / Tool**: when and which LLM
- **Prompt**: what was asked (paste verbatim if significant)
- **Output usable?**: yes / partial / no — and why

Phase 5 audit rule: each completed entry should make visible why that tool was chosen, what quality of output came back, and what changed in the repo because of it.

---

## Outstanding for the human

- **Phase 0 tool-comparison verdict**: `[TODO: Add your subjective verdict for Claude Desktop / ChatGPT. Keep it honest: how did it feel for reasoning, design discussion, or critique compared with Codex and Claude Code?]`
- **Phase 4 live browser QA**: `[TODO: Open the live GitHub Pages site in a clean/incognito browser, hard-refresh, click all 8 nav tabs, check ~375px mobile width, and confirm zero console errors.]`

---

## Phase 0 — Tools, repo, workflow

### 2026-05-20 — Project kickoff

- **Tool**: Claude Code (Opus 4.7)
- **Why this tool**: Claude Code could scaffold a repo, create files, and push the first project state in one pass.
- **Prompt**: Pasted the project brief verbatim and asked Claude to scaffold a Streamlit + Plotly project with a GitHub remote, picking one primary VC data source.
- **Output usable?**: Yes — produced the initial folder, venv, `app.py` skeleton with 4 features, `requirements.txt`, `README.md`, `sources.md`, this prompt log, and pushed to GitHub.
- **What changed because of it**: Created the initial repository and gave the project a first runnable direction, even though that stack was later replaced.

---

### 2026-05-20 — Phase 0: deploy + realign stack (Perplexity + Claude Code)

- **Tool**: Perplexity (chart code) + Claude Code (deploy/review)
- **Why this tool**: Perplexity was fast for a small D3 prototype; Claude Code was better for repo operations, deployment, and reviewing whether the prototype fit GitHub Pages.
- **Prompt**: Asked Perplexity to build a single-file HTML + D3 bar chart of VC funding 2022–2025. Used Claude Code to deploy it to GitHub Pages and flag the data.
- **Output usable?**: Yes, with caveats — Perplexity's D3 page became `index.html` and is live on Pages. Realigned project from Streamlit to vanilla HTML+D3 (Streamlit can't run on Pages). Perplexity's example funding numbers were **unverified**, so flagged on-page + per-row `source: TODO`; credited Perplexity in the footer.
- **What changed because of it**: The project moved from an app-server idea to a static GitHub Pages architecture, and the source-quality issue became visible early instead of being hidden in the chart.

---

### 2026-05-25 — Codex repo audit and plan alignment

- **Tool**: Codex (GPT-5) with GitHub plugin + local repo access.
- **Why this tool**: Codex could inspect the actual checkout and compare it against both intern plan files without relying on memory.
- **Prompt**: Asked Codex to connect to `GitLostintheSauce/InsubordinateandChurlish_VCflow`, inspect the repo, read the two intern plan files, and discuss where the project stood relative to the plan.
- **Output usable?**: Yes. Codex cloned the repo, inspected `README.md`, `DATA_MODEL.md`, `NARRATIVE.md`, `sources.md`, `index.html`, and the CSVs. It identified that the revised plan mattered more than the original plan because it allowed the source-quality-first pivot from quarterly-everywhere to an annual Crunchbase backbone plus Web3 quarterly deep dive. It placed the project at Phase 0/1 complete and Phase 2 in progress, with Phase 3 not yet started.
- **What changed because of it**: The project plan was re-centered around completing Phases 0–2 cleanly before adding later dashboard sections.

---

### 2026-05-27 — Phase 0 tool comparison (t1) [summary from memory — confirm personal verdicts]

The single small task used to compare the three required tools: **"scaffold a single-file HTML page that renders a VC-funding bar chart from flat data."**

| Tool | What it produced on the task | Where it helped / failed |
|---|---|---|
| **Perplexity** (sourced research) | A working single-file HTML + D3 bar chart, plus example funding numbers. | Helped: fastest path to runnable D3; good for cited sourcing later. Failed: its example numbers were **unverified** — had to flag every row `source: TODO` and re-source from Crunchbase. |
| **Claude Code** (code agent) | Repo scaffold, data files, deploy to GitHub Pages, multi-file edits, review. | Helped: full-project context — file edits, git, deploy, refactors (e.g. Streamlit→D3 realignment, Defense scope cleanup). Best for anything touching multiple files. |
| **Claude Desktop / ChatGPT** (conversational) | See [Outstanding for the human](#outstanding-for-the-human). | See [Outstanding for the human](#outstanding-for-the-human). |

- **Why these tools**: The comparison intentionally separated research, code-agent work, and conversational reasoning so their strengths were visible.
- **Output usable?**: Partial — factual repo history is recoverable, but the subjective Claude Desktop / ChatGPT verdict still needs the human's own take.
- **What changed because of it**: The log now documents that Perplexity was useful but required source auditing, Claude Code handled multi-file repo changes, and the remaining subjective comparison is explicitly flagged rather than invented.

---

## Phase 1 — Source audit & data architecture

### 2026-05-20 — Phase 1: data model + start sourcing (Claude Code + Perplexity)

- **Tool**: Claude Code (data model) + Perplexity (sourcing — in progress)
- **Why this tool**: Claude Code was used for the file/data scaffold; Perplexity was used where cited source discovery mattered.
- **Prompt**: Built `data/vc_by_sector.csv` (96 blank rows: 6 sectors × 16 quarters, source=TODO) and `data/landmark_deals.csv`. Routing the actual number-gathering to Perplexity, one quarter at a time, primary source CB Insights State of Venture. (Paste reusable prompt + results here as you go.)
- **Output usable?**: Partial at this point — the schema existed, but the actual sourced cells were still being filled.
- **What changed because of it**: The first explicit data model was created, making the later source-quality pivot possible to see and document.

---

### 2026-05-22 — Phase 1 close: stack + data model + narrative (t6, t7)

- **Tool**: Claude Code (Opus 4.7)
- **Why this tool**: Claude Code could update the data model, narrative docs, and repo structure together.
- **Stack decision (t6)**: *"I'm using vanilla HTML + D3.js with flat CSV data on GitHub Pages, because it deploys as a static site with no build step and keeps hand-curated data easy to edit/diff — a framework adds tooling with zero payoff for a 3–4 chart dashboard."* CSV instead of `data.json` (curated by hand; D3 loads CSV natively). Full data model in `DATA_MODEL.md`.
- **Narrative brief (t7)**: `NARRATIVE.md` — 4 shifts (AI's takeover → ~50% of all VC; concentration into mega-rounds; the crypto boom-bust-rebuild cycle; rotation to hard tech/defense). Climate/Biotech flagged as scope-shaky, not drawn as confident trends.
- **Output usable?**: Yes — both deliverables done. Phase 1 substantially complete at the time (backbone 21/24, 158 deals). Later cleanup narrowed the dashboard sector from "Defense & Space" to "Defense" and removed space-only/double-count-prone deal rows, leaving 145 landmark deals.
- **What changed because of it**: The repo had a clear static-site architecture, a written narrative, and an explicit warning against overconfident Climate/Biotech claims.

---

### 2026-05-25 — Codex docs cleanup and Defense-only scope

- **Tool**: Codex (GPT-5) with local file editing, validation, git, and GitHub push.
- **Why this tool**: Codex was the right fit because the task crossed docs, CSV data, validation, and GitHub publishing.
- **Prompt**: Asked Codex to update stale docs, remove Space from the dashboard scope, explain how to finish the prompt/process record, and keep Phase 0/1/2 clean before moving into Phase 3.
- **Output usable?**: Yes. Codex updated `README.md`, `DATA_MODEL.md`, `Plan.md`, `sources.md`, and `PROMPTS.md`; renamed the annual dashboard sector from `Defense & Space` to `Defense`; removed Space-only and Dual-Use rows from `landmark_deals.csv`; replaced the mixed raw source file with `data/raw/defense_vc_2022_2025.csv`; and committed/pushed `e583393` (`Align docs and defense sector scope`).
- **Judgment call**: The dashboard should not claim "Defense & Space" while the annual backbone uses Crunchbase's narrow defense-tech definition. Removing Space made the data less flashy but more defensible.
- **What changed because of it**: The project stopped mixing defense-tech and space-only data, and the docs/data started matching the dashboard's narrower claim.

---

Prompt-log note: the following pivot is preserved as the source-quality decision record for the annual backbone. It explains why the original quarterly-everywhere plan was not used.

### 2026-05-27 — Phase 1 decision: source-quality pivot, quarterly → annual (the documented pivot)

**Decision:** the cross-sector backbone is **annual** (Crunchbase, all 6 sectors), not quarterly. Only **Web3** is carried at quarterly grain (Galaxy Digital), as a clearly-labeled sector deep dive.

**Why the pivot from the original "quarterly for all 6 sectors" plan:**
- A 6-sector × 16-quarter grid (96 cells) cannot be filled from free, public sources without mixing provider definitions or **estimating most cells** — which would violate the project's no-hallucinated-numbers rule.
- Crunchbase publishes clean *annual* sector totals under one consistent "VC-backed startup" definition, so annual figures are genuinely **comparable across sectors**. Forcing them to quarterly would manufacture false precision.
- Galaxy publishes consistent *quarterly* crypto VC, so Web3 — the audience's market — keeps its quarterly cycle view honestly.

**What this means for the deliverables:** the regular plan's quarterly hero + timeline scrubber (t9/t10) are **intentionally not built**, because the cross-sector data is annual; a scrubber over 4 annual points adds nothing over the existing year selector, and a 6-sector quarterly scrubber would require data we won't fabricate. This is the source-quality-first call the revised plan explicitly rewards (an undocumented pivot looks accidental; this one is deliberate and recorded).

---

Prompt-log note: this second pivot happened while building Phase 3, but it is grouped here because it is a data-architecture constraint. The analytical reasoning below is preserved from the original decision record.

### 2026-05-27 — Phase 3 decision: no deal-count / median-round-size metric (a second documented pivot)

**Context:** building the Phase 3 **sector comparison** view. The original plan envisioned comparing sectors on funding *and* deal count *and* median round size. Tested whether the backbone could honestly support deal count / median.

**Tool:** Claude Code (read the data) + Web search against Crunchbase's own end-of-year reports.

**Finding — deal count is only partially available, and the gaps are real, not lazy:**
- `sector_annual.csv` already carries clean Crunchbase deal counts for **Fintech 2024–25, Defense 2022–24, Web3 2022–24**. Those stay.
- **AI, Climate, Biotech counts are blank by design.** Crunchbase reports AI in *dollars and share of total* but publishes **no comparable annual AI deal count** — confirmed against its [AI EOY 2024](https://news.crunchbase.com/venture/global-funding-data-analysis-ai-eoy-2024/) and [AI trends EOY 2025](https://news.crunchbase.com/ai/big-funding-trends-charts-eoy-2025/) write-ups. The count-shaped numbers in circulation are **different scopes** ("~10,500 rounds" = all North American sectors; "250 companies" = one month), so using one as an "AI deal count" would mix definitions and fabricate a figure.
- Climate (equity-only → all-stages scope flips) and Biotech (US-only vs global) have no clean per-year counts for the same scope reasons already documented for their funding lines.

**Finding — median round size cannot be computed honestly:** it requires deal-level distribution data the project does not hold. *Average* round size (funding ÷ count) is derivable only where both numbers are real (labeled "derived"); a median over the 145 curated landmark deals is biased to large rounds and would misrepresent the market.

**Decision:** the comparison view reports **funding totals + % change** for all sectors, **deal count only where Crunchbase published it** (blanks shown as "not published," not invented), and an optional **derived** average round size where both inputs exist. No median. Same source-quality-first logic as the [quarterly → annual pivot](#2026-05-27--phase-1-decision-source-quality-pivot-quarterly--annual-the-documented-pivot); recorded so the gap reads as a judgment call, not an omission. Also logged in `README.md` (Data principles).

---

## Phase 2 — Core dashboard

### 2026-05-25 — Codex bug fix: Defense visibility

- **Tool**: Codex (GPT-5) with local server checks and GitHub push.
- **Why this tool**: Codex could debug the live frontend symptom against the actual CSV labels, browser cache behavior, and chart rendering.
- **Prompt**: Reported that Defense no longer appeared clearly on the dashboard graphs after the sector rename.
- **Output usable?**: Yes. Codex diagnosed two issues: the browser could cache old CSV rows labeled `Defense & Space`, and the linear chart buried tiny Defense values near the baseline. It normalized old `Defense & Space` rows to `Defense`, cache-busted CSV URLs, made log scale the default, thickened Defense styling, verified served CSV rows locally, and committed/pushed `1dc1ddb` (`Make defense visible in dashboard charts`).
- **Lesson**: Data renames need visual QA, not just CSV checks. A technically correct line can still be invisible if the chart scale hides it.
- **What changed because of it**: Defense became visible in the dashboard and old cached labels stopped breaking the renamed sector.

---

### 2026-05-26 — Codex Phase 2 UI/UX polish

- **Tool**: Codex (GPT-5) with in-app browser QA.
- **Why this tool**: The request needed rapid frontend iteration with the page open, not just static code edits.
- **Prompt**: Asked Codex to make the dashboard feel shockingly professional, remove emoji, focus on the user, improve flow, and add more interaction.
- **Output usable?**: Yes. Codex rebuilt `index.html` into a more polished analyst dashboard: executive hero, KPI tiles, sticky section navigation, sector focus controls, year selector, cleaner chart containers, better tooltips, a more professional AI-energy section, no visible emoji, and cache-busted data loading. It verified the page in the in-app browser, checked for console errors, tested Defense focus and year selection, and committed/pushed `636d144` (`Polish dashboard UI and interactions`).
- **Lesson**: Codex was especially useful for the "tight loop" of edit -> run local server -> inspect in browser -> fix UX issue -> commit.
- **What changed because of it**: The dashboard moved from a functional chart page to a polished, interactive user-facing product.

---

### 2026-05-27 — Phase 2 QA pass (t20/t21) [summary from memory]

- **Tool**: Claude Code / local request checks, summarized from project history.
- **Why this tool**: The check was aimed at static deployment health: URLs, CSV loading paths, and whether the wired interactions existed in source.
- **Prompt**: Verify that the live GitHub Pages deployment and data files load, and record what still needs human browser QA.
- **Output usable?**: Partial — the static checks were useful, but they did not replace a real browser/console pass.
- **What changed because of it**:
  - **Live URL** https://gitlostinthesauce.github.io/InsubordinateandChurlish_VCflow/ — page and all four data CSVs return HTTP 200 on GitHub Pages (verified via request checks).
  - **Data loading** — charts read `data/*.csv` via `d3.csv()`; no hardcoded chart values. Cache-busting `?v=` query is in place.
  - **Interactions** — scale toggle, sector-focus chips, clickable legend filters, year selector, sticky section-nav all wired in the source.
  - **Caveats** — estimated cells render as hollow dots; Climate/Biotech scope-shift caveats shown on-page.
  - **Still needs a human browser check** — open the live URL in a clean/incognito window, confirm zero console errors, click every control, and check a ~375px mobile width. Log any fixes here.

---

## Phase 3 — Secondary views

### 2026-05-27 — Phase 3 shipped: deals leaderboard, sector comparison, megaround insights

- **Tool**: Claude Code (Opus 4.7), grounded in the local CSVs and docs.
- **Why this tool**: Phase 3 required a broad multi-section dashboard implementation, data-derived views, source caveats, documentation updates, and a commit that kept the no-hallucinated-numbers rule intact.
- **Prompt**: Paraphrased from repo history: implement the Phase 3 secondary views — landmark deals leaderboard, sector comparison, and megaround analysis — while keeping unsupported deal-count/median metrics out of the interface.
- **Output usable?**: Yes. Commit `3a90def` (`Phase 3: deals leaderboard, sector comparison, megaround insights + UX overhaul`) added:
  - A landmark deals leaderboard from `landmark_deals.csv` with sector/year filters, sortable columns, source links, and caveat flags.
  - A sector comparison view with rebased-to-2022 growth, total/% change stat cards, sourced deal counts where published, and derived average round where both inputs exist.
  - An "Anatomy of the megaround era" section with scatter, bubble, concentration, and geography views computed from the deals data.
  - A presentation UX pass: terminal-style stat strip, indexed nav tabs, grain texture, crisper borders, scroll-synced nav, and reveal-on-scroll motion with reduced-motion handling.
- **What changed because of it**: `index.html` expanded from the core dashboard into the full 8-panel analytical product, while `README.md` and `PROMPTS.md` documented the deal-count/median omission instead of pretending the missing data existed.
- **Lesson**: Phase 3 shows the right use of an LLM code agent: not just adding features, but refusing chart ideas that the available data could not honestly support.

---

## Phase 4 — Polish & insight layer

### 2026-06-09 — Phase 4 shipped: insight cards + analyst-layer polish

- **Tool**: Claude Code (Opus 4.7) with a re-runnable static QA script.
- **Why this tool**: Phase 4 needed critique-to-code translation across visual hierarchy, chart defaults, sourced claims, and regression checks.
- **Prompt**: Paraphrased from repo history: apply the analyst-layer critique, strengthen the top-level read, add sourced insight cards, adjust misleading or overloaded visual defaults, and leave behind a repeatable static check.
- **Output usable?**: Yes. Commit `b273294` (`Phase 4: insight cards + analyst-layer polish`) added the missing analyst layer and QA support:
  - Added a 12-card sourced insight grid from a hand-curated `INSIGHTS` JavaScript array between the executive summary and Overview.
  - Swapped hero KPI #2 from basket-dependent "AI share 56%" to the concentration stat: roughly `$93B / 3 AI labs`, about half of `$197B`.
  - Flipped the Overview default chart scale from log to linear so the first view matches the "AI dwarfs everything" thesis; log remains available as a toggle.
  - Recolored Biotech and Defense away from the `--danger` / `--warn` semantic tokens, using magenta for Biotech and steel for Defense.
  - Added `scripts/phase4_check.sh` for re-runnable JavaScript parse, anchor, and polish checks; the static check passed 17/17 at commit time.
- **What changed because of it**: `index.html` gained a stronger executive read and cleaner visual semantics, and `scripts/phase4_check.sh` became the lightweight QA safety net for this static site.
- **Lesson**: The best Phase 4 prompt was evaluative, not decorative: it asked what a professional reader would misunderstand, then converted that critique into specific chart defaults, colors, copy hierarchy, and checks.

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

Phase 4 adds one nuance: Claude Code was useful for a broad "criticize the dashboard like an analyst" pass, while Codex remains the better fit when the next step is a bounded repo task with explicit constraints, verification, commit, and push.

---

## Template for future entries

### YYYY-MM-DD — short title

- **Tool**:
- **Prompt**:
- **Output usable?**:
