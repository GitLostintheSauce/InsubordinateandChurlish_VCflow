# Data Model & Stack Decision (Phase 1 / t6)

## Stack decision

**I'm using vanilla HTML + D3.js with flat CSV data files on GitHub Pages, because it deploys as a single static site with no build step and keeps the hand-curated data trivial to edit and diff — a framework would add tooling and surprises with zero payoff for a 3–4 chart dashboard.**

One deliberate deviation from the plan's default: **CSV, not `data.json`.** The data is curated by hand from cited sources, and CSV is far easier to read, edit, and review in git diffs. D3's `d3.csv()` loads it natively, so there's still no build step.

## The dashboard data files

### 1. `data/sector_annual.csv` — the comparison backbone ("where + when")
One row per sector per year. **Single source = Crunchbase** (so sectors are comparable).
```
sector, year, deal_value_usd_b, deal_count, source, note
AI, 2024, 114.0, , Crunchbase, "Revised from $100B; AI ~1/3 of global VC..."
```
- 6 sectors × 4 years = 24 rows
- `source = estimated` flags derived/non-clean cells (Climate 2022, Web3 2025, Biotech 2022/2023/2024)
- Drives: the hero cross-sector chart, share-of-total, top movers
- Sectors: AI, Fintech, Climate, Defense, Web3, Biotech. The defense line is deliberately defense-tech only; space data was removed to avoid mixing definitions.

### 2. `data/web3_quarterly.csv` — the Web3 hero deep-dive
Quarterly Web3 funding (single source = **Galaxy Digital**; broader scope than the Crunchbase backbone, so kept separate and labeled).
```
year, quarter, sector, deal_value_usd_b, deal_count, source, note
2025, 4, Web3, 8.5, 425, Galaxy-CryptoVC, "+84% QoQ; strongest since Q2 2022..."
```
- 16 rows (Q1 2022 → Q4 2025)
- Drives: the Web3 timeline / scrubber (the crypto-cycle story for the perp-exchange audience)

### 3. `data/landmark_deals.csv` — the deals (t5 / Phase 3 input)
One row per notable round. 145 deals across the dashboard sectors. Space-only and dual-use space rows were removed when the sector label was narrowed to Defense.
```
company, sector, subsector, year, quarter, amount_usd_m, round_type, lead_investor, country, source_name, source_url, note
OpenAI, AI, Foundation Model, 2025, Q1, 40000, Private Round, SoftBank, USA, "Crunchbase News...", https://..., "...19% of 2025 AI total"
```
- Reserved for: the Phase 3 deals leaderboard (filter by sector + year). This view is not built yet.

### 4. `data/energy_ai_funding.csv` and `data/energy_ai_ppa.csv` — AI-energy deep dive
Selected named rounds, grants, exclusions, and hyperscaler power deals used by the AI-energy section.
- `energy_ai_funding.csv` separates `VC`, `gov-grant`, and `excluded` capital classes so the chart does not mix venture capital with grants, SPACs, or infrastructure finance.
- `energy_ai_ppa.csv` records hyperscaler power deals whose dollar values are often undisclosed; it supports the narrative caveat rather than a summed market total.

## Schema vs the revised plan's unified schema (t10)

The revised plan proposed one unified table:
`sector,year,quarter,period_grain,deal_value_usd_b,deal_count,source_key,source_url,figure_type,method_note`

This project uses **per-file schemas** instead of one combined table, because the backbone is annual and only Web3 is quarterly — a single table would leave `quarter` blank for 24 of 40 rows and invite false precision. Every field in the unified schema is still represented; here is the mapping:

| Unified field | Where it lives here |
|---|---|
| `sector` | `sector` column |
| `year` | `year` column |
| `quarter` | only in `web3_quarterly.csv` (the sole quarterly series) |
| `period_grain` | **implicit by file**: `sector_annual.csv` = annual, `web3_quarterly.csv` = quarterly (stated in headers/README/sources) |
| `deal_value_usd_b` | `deal_value_usd_b` column |
| `deal_count` | `deal_count` column (blank where Crunchbase didn't publish a count) |
| `source_key` | `source` column (short key → resolved in `sources.md`) |
| `source_url` | full URLs live in `sources.md` (per-key) and per-row in `landmark_deals.csv` |
| `figure_type` | `source=estimated` flags estimated/derived cells; reported vs scope-shifted is annotated in `note` + `sources.md` |
| `method_note` | `note` column + `sources.md` method notes |

If a future phase needs the single flat table (e.g. for a data-table view or export), it can be generated from these files — the information is all present, just normalized across files rather than denormalized into one.

## Values computed in-browser (no extra files)
- **Share of total per year** = sector value ÷ year total → the "AI ate the pie" view
- **YoY delta / top movers** = value[year] − value[year−1]
- **Concentration** = top-N deal amounts ÷ sector-year total (e.g. OpenAI = ~19% of 2025 AI)
- **AI-energy selected VC totals** = sum named `VC` rows by year/subsector; shown as illustrative, not as a full market total

## Provenance / reference (not loaded by the app)
- `data/raw/web3_galaxy_quarterly_provenance.csv` — per-quarter Galaxy citations
- `data/raw/defense_vc_2022_2025.csv` — defense-only source research retained after removing space from the sector scope
- `sources.md` — every `source` key resolved to a citation, with scope-conflict notes
