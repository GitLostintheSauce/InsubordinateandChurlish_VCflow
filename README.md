# VC Flow — Where the Money Flowed, 2022–2025

An interactive dashboard visualizing how venture capital reallocated across six sectors from 2022 to 2025. It answers one question: **where is the money flowing, and when?**

**Live:** https://gitlostinthesauce.github.io/InsubordinateandChurlish_VCflow/

Built with LLMs as the primary tool for research, data, and code — the meta-skill of the project.

## Architecture

**Static site — vanilla HTML + [D3.js](https://d3js.org), served on GitHub Pages. No backend, no framework, no build step.** `index.html` loads the CSVs in `data/` directly via `d3.csv()` and renders the charts in the browser.

> Note: this project began as a Streamlit + Plotly + Python app. That stack was retired early on (Streamlit can't run on GitHub Pages) and fully removed — there is no `app.py`, `requirements.txt`, or `venv`. If you see Streamlit mentioned in `PROMPTS.md`, that's the historical build log, not the current architecture.

## What it shows

Current D3 views (vanilla HTML, no build step):
1. **Funding by sector, per year** — multi-line, with a linear ⇄ log toggle. AI's curve dwarfs everything (which is the story).
2. **Share of the pie, per year** — 100% stacked bars; AI's slab swells from ~21% (2022) to ~60% (2025).
3. **The crypto cycle, quarter-by-quarter** — Web3's peak → winter → rebuild, from Galaxy Digital.
4. **AI-energy nexus** — selected power-sector rounds and data-center electricity demand, clearly labeled as an illustrative deep dive rather than a market total.

The Phase 3 deals leaderboard is not built yet. `landmark_deals.csv` is prepared as the input for that later view.

## Repo structure

```
index.html                     The dashboard (loads the CSVs via d3.csv)
data/
  sector_annual.csv            ★ comparison backbone — Crunchbase annual, 6 sectors × 4 years
  web3_quarterly.csv           ★ Web3 hero detail — Galaxy Digital, quarterly
  energy_ai_funding.csv        AI-energy selected rounds
  energy_ai_ppa.csv            AI-energy hyperscaler power deals
  landmark_deals.csv           145 cited landmark rounds (reserved for Phase 3 leaderboard)
  raw/                         source-of-record research files (provenance)
    ai_vc_2022_2025.csv          ┐
    fintech_vc_2022_2025.csv     │ original per-sector research,
    climate_vc_2022_2025.csv     │ gathered via LLM with citations;
    biotech_vc_2022_2025.csv     │ data extracted into the consolidated
    defense_vc_2022_2025.csv     │ files above
    web3_crypto_vc_2022_2025.csv       │
    web3_galaxy_quarterly_provenance.csv  per-quarter Galaxy citations
NARRATIVE.md                   1-page narrative brief (the 4 big shifts)
DATA_MODEL.md                  data shapes + stack decision
sources.md                     every figure → its citation, with scope caveats
Plan.md                        the data-gathering playbook (prompt templates)
PROMPTS.md                     live prompt log
```
The files marked ★ are what the dashboard reads. `data/raw/` holds the originals so every consolidated number is traceable.

## Data principles

- **One source per sector line.** Mixing sources within a sector fakes the trend (different firms count differently). Backbone = **Crunchbase** for all sectors → cross-sector comparison is honest.
- **No hallucinated numbers.** Every figure traces to a citation in `sources.md`, or is marked `estimated` (shown as hollow dots on the charts). Five cells are estimated; the rest are sourced.
- **Scope caveats are visible, not hidden** — Climate and Biotech change definition across years and are flagged on the page.

## View locally

It loads CSVs over HTTP, so use a tiny static server (not `file://`):
```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

## Status

Phase 0 and Phase 1 are complete. Phase 2 is the current gate: the static dashboard, CSV loading, core charts, interaction, caveat labels, and GitHub Pages deployment are in place, but the project still needs a Phase 2 QA pass before moving to Phase 3.

Before Phase 3, verify the live page in a clean browser session, check the console for errors, test desktop and mobile widths, and update the prompt/process log with the Phase 2 implementation decisions. Phase 3 starts with the deals leaderboard.
