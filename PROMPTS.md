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
- **Output usable?**: Yes — both deliverables done. Phase 1 substantially complete (backbone 21/24, 158 deals).

---

## Template for future entries

### YYYY-MM-DD — short title

- **Tool**:
- **Prompt**:
- **Output usable?**:
