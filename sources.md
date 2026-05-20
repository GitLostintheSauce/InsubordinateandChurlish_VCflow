# Sources

Every number in the dashboard must trace to a citation here. The `source` column of `data/vc_by_sector.csv` holds the short key; the full reference lives below.

## Primary

- **CBI-SOV-2025Q1** — CB Insights, *State of Venture: 2025 Q1 Report*, URL: <fill in>, accessed YYYY-MM-DD.
- **CBI-SOV-2024Q4** — CB Insights, *State of Venture: 2024 Q4 Report*, URL: <fill in>, accessed YYYY-MM-DD.
- (add a row per quarter you pull from)

## Supplements

- **PB-NVCA-2025Q1** — PitchBook-NVCA, *Venture Monitor Q1 2025*, URL: <fill in>, accessed YYYY-MM-DD.

## Web3 / Crypto (sector-specific — see source-consistency rule below)

- **CBI-Blockchain-2022Q1** — CB Insights, *State of Blockchain Q1 2022*, https://www.cbinsights.com/research/report/blockchain-trends-q1-2022/ . Total value ($9.2B) from CB Insights; deal count (461) via TechCrunch's writeup of the same CB Insights dataset (https://techcrunch.com/2022/05/12/vc-investment-into-crypto-startups-peaked-right-before-everything-went-to-hell/). Accessed 2026-05-20.
- **CB-News-Crypto-2022H1** — Crunchbase News, "Crypto Funding Numbers Fall During Bumpy First Half Of Year", https://news.crunchbase.com/fintech-ecommerce/crypto-funding-falls-h1-2022/ (Q2 2022: "more than $4.2B"; deal count not stated in accessible snippet). Accessed 2026-05-20.
- **CB-News-Crypto-2022Q3** — Crunchbase News, "Web3 Funding Sees Huge Drop As Big Rounds Dip", https://news.crunchbase.com/business/web3-funding-crypto-blockchain-a16z/ (Q3 2022: ~$3.6B in MORE THAN 500 deals — count is a floor). Accessed 2026-05-20.
- **CB-News-Crypto-2022Q4** — Crunchbase News, "Funding To Web3 Startups Plummets 74% in Q4", https://news.crunchbase.com/web3/startup-funding-q4-drop/ (Q4 2022: $2.4B; deal count not stated in accessible snippet). Accessed 2026-05-20.
- **CB-News-Crypto-2025Q1** — Crunchbase News, "Crypto/blockchain funding Q1 2025", https://news.crunchbase.com/web3/crypto-blockchain-funding-q1-2025-boost-binance/ ($3.8B, 220 deals; boosted by Binance $2B round). Accessed 2026-05-20.

### ⚠ Do-not-trust note (caught 2026-05-20)
- The "$9.3B" figure floating around the Q4 2022 recap refers to **Q4 2021** ("funding fell from $9.3B in Q4 2021 to $2.4B in Q4 2022"), NOT H1 2022. Do not use it as an in-window number.
- **Q1 2022 Web3 is still unfilled.** The Q2 article implies Q1 ≈ $5.2B (Q2 was "~$1B less than Q1"), but that's an inference, not a stated Crunchbase figure — left blank, `source = TODO-Crunchbase`.

## Definitions / methodology

- Sector taxonomy: matches CB Insights' breakdown (AI, fintech, healthcare, climate, etc.). Note any reclassifications here when blending sources.
- All deal values in USD billions, current-year dollars unless noted.
- "Deal value" = total disclosed equity funding for the period, excluding debt and secondary sales (per CBI convention).

## ⚠ Source-consistency rule (important)

- **Each sector's 16-quarter time series must use ONE source the whole way.** Mixing sources across quarters within a sector creates fake trends (different firms count deals differently). Mixing sources *across* sectors is acceptable but means cross-sector $ levels aren't strictly comparable — only trends are.
- **Web3 source = Crunchbase crypto recaps, all 16 quarters** (decided 2026-05-20, for consistency). The CB Insights Q1 2022 figure ($9.2B/461) is kept above as a reference only — NOT used in the series. Q1 2022 Web3 to be re-pulled from Crunchbase (`source` placeholder: `TODO-Crunchbase`).
- Other 5 sectors (AI, Fintech, Climate, Defense & Space, Biotech) source = **CB Insights State of Venture**, all quarters.
