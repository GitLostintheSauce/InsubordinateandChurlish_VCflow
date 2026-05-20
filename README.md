# Insubordinate & Churlish - VC Flow

An interactive dashboard visualizing how venture capital shifted across sectors from **2022 to 2025**.

## Mission

Built with LLMs as the primary tool for every part — research, coding, design, data, content. The meta-skill is wielding these tools effectively. Scope discipline matters more than ambition.

**Four focused features**, not eight half-finished ones:
1. Deal value over time, by sector
2. Sector share of total VC (stacked area)
3. Top sector movers — biggest gainers / losers over the window
4. Underlying data table with per-row sources

## Run locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Then open the URL Streamlit prints (usually `http://localhost:8501`).

## Data

Primary source: **CB Insights State of Venture** (quarterly).
Supplements: **PitchBook-NVCA Venture Monitor**, **Crunchbase News** quarterly recaps.

All numbers in the dashboard cite a source. See `sources.md`.

Data file: `data/vc_by_sector.csv` with columns:
- `year` (int)
- `quarter` (int, 1-4)
- `sector` (str)
- `deal_value_usd_b` (float, USD billions)
- `deal_count` (int)
- `source` (str — short citation key matching `sources.md`)

## Prompt log

Significant LLM prompts used to build this project are captured live in `PROMPTS.md` — reconstructing on Friday produces fiction; capturing live produces truth.

## Deployment

Currently target: **Streamlit Community Cloud** (connects to this GitHub repo).
Fallback: **GitHub Pages** as a static export — code is structured so the same Plotly charts can render either way.
