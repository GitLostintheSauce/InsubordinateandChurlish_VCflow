# Sources

Every number in the dashboard must trace to a citation here. The `source` column of `data/vc_by_sector.csv` holds the short key; the full reference lives below.

## ⭐ Source strategy (decided 2026-05-20)

**Single provider for all 6 sectors: CB Insights.** Use the annual "State of [Sector]" recap PDFs — each contains the four quarterly figures with one consistent methodology. This makes every sector directly comparable to every other.

| Sector | CB Insights report series |
|---|---|
| AI | State of AI |
| Fintech | State of Fintech |
| Climate | State of Climate Tech |
| Defense & Space | (least consistent — may need a labeled fallback) |
| Web3 | State of Blockchain |
| Biotech | State of Digital Health / Healthcare |

**Consistency rule:** each sector's 16-quarter line uses ONE report series the whole way. Because every sector is CB Insights, cross-sector $ levels are comparable too.

**Note on cadence:** these are *annual* recaps with quarterly breakdowns inside — not standalone quarterly reports. The 2025 recaps publish in early 2026 (now available as of this date).

## Active citations

- **CBI-Blockchain-2022** — CB Insights, *State of Blockchain — Global 2022 Recap* (annual PDF, quarterly breakdown). Q1 $10.8B/546, Q2 $7.6B/509, Q3 $5.1B/448, Q4 $3.2B/325; FY $26.8B/1,828. Accessed 2026-05-20. *(Add the public PDF URL here.)*
- *(Add CBI-Blockchain-2023/2024/2025, CBI-AI-YYYY, CBI-Fintech-YYYY, etc. as pulled.)*

## ⚠ SUPERSEDED — Crunchbase Web3 figures (kept for audit trail, NOT used)

Web3 was briefly sourced from Crunchbase, then switched to CB Insights *State of Blockchain* for single-provider consistency. These are retained only to document the decision; they differ ~2x from CB Insights due to a narrower "crypto" vs broader "blockchain" methodology.

- ~~CB-News-Crypto-2022Q1-NEEDLINK~~ — Crunchbase, Q1 2022 ~$4.9B (no link; never verified).
- ~~CB-News-Crypto-2022H1~~ — Crunchbase, Q2 2022 "more than $4.2B". https://news.crunchbase.com/fintech-ecommerce/crypto-funding-falls-h1-2022/
- ~~CB-News-Crypto-2022Q3~~ — Crunchbase, Q3 2022 ~$3.6B / >500 deals. https://news.crunchbase.com/business/web3-funding-crypto-blockchain-a16z/
- ~~CB-News-Crypto-2022Q4~~ — Crunchbase, Q4 2022 $2.4B. https://news.crunchbase.com/web3/startup-funding-q4-drop/
- ~~CB-News-Crypto-2025Q1~~ — Crunchbase, Q1 2025 $3.8B / 220 deals (Binance $2B outlier). https://news.crunchbase.com/web3/crypto-blockchain-funding-q1-2025-boost-binance/

## Definitions / methodology

- Sector taxonomy: matches CB Insights' breakdown (AI, fintech, healthcare, climate, etc.). Note any reclassifications here.
- All deal values in USD billions, current-year dollars unless noted.
- "Deal value" = total disclosed equity funding for the period, excluding debt and secondary sales (per CB Insights convention).
- Watch the lesson learned: the same number can mean different things across firms (e.g. Crunchbase "crypto" ≈ half of CB Insights "blockchain"). Never mix providers within one sector's line.
