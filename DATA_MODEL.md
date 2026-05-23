# Data Model & Stack Decision (Phase 1 / t6)

## Stack decision

**I'm using vanilla HTML + D3.js with flat CSV data files on GitHub Pages, because it deploys as a single static site with no build step and keeps the hand-curated data trivial to edit and diff — a framework would add tooling and surprises with zero payoff for a 3–4 chart dashboard.**

One deliberate deviation from the plan's default: **CSV, not `data.json`.** The data is curated by hand from cited sources, and CSV is far easier to read, edit, and review in git diffs. D3's `d3.csv()` loads it natively, so there's still no build step.

## The three data files

### 1. `data/sector_annual.csv` — the comparison backbone ("where + when")
One row per sector per year. **Single source = Crunchbase** (so sectors are comparable).
```
sector, year, deal_value_usd_b, deal_count, source, note
AI, 2024, 114.0, , Crunchbase, "Revised from $100B; AI ~1/3 of global VC..."
```
- 6 sectors × 4 years = 24 rows
- `source = estimated` flags derived/non-clean cells (Climate 2022, Biotech 2022/2024)
- Drives: the hero cross-sector chart, share-of-total, top movers

### 2. `data/web3_quarterly.csv` — the Web3 hero deep-dive
Quarterly Web3 funding (single source = **Galaxy Digital**; broader scope than the Crunchbase backbone, so kept separate and labeled).
```
year, quarter, sector, deal_value_usd_b, deal_count, source, note
2025, 4, Web3, 8.5, 425, Galaxy-CryptoVC, "+84% QoQ; strongest since Q2 2022..."
```
- 16 rows (Q1 2022 → Q4 2025)
- Drives: the Web3 timeline / scrubber (the crypto-cycle story for the perp-exchange audience)

### 3. `data/landmark_deals.csv` — the deals (t5)
One row per notable round. ~158 deals across all sectors.
```
company, sector, subsector, year, quarter, amount_usd_m, round_type, lead_investor, country, source_name, source_url, note
OpenAI, AI, Foundation Model, 2025, Q1, 40000, Private Round, SoftBank, USA, "Crunchbase News...", https://..., "...19% of 2025 AI total"
```
- Drives: the deals leaderboard (filter by sector + year)

## Values computed in-browser (no extra files)
- **Share of total per year** = sector value ÷ year total → the "AI ate the pie" view
- **YoY delta / top movers** = value[year] − value[year−1]
- **Concentration** = top-N deal amounts ÷ sector-year total (e.g. OpenAI = ~19% of 2025 AI)

## Provenance / reference (not loaded by the app)
- `data/raw/web3_galaxy_quarterly_provenance.csv` — per-quarter Galaxy citations
- `sources.md` — every `source` key resolved to a citation, with scope-conflict notes
