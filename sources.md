# Sources

Every number traces to a citation here. `source` columns in the data files hold short keys; full references below.

## ⭐ Source strategy

**Comparison backbone (`data/sector_annual.csv`) = Crunchbase annual totals, all 6 sectors.** One consistent "VC-backed startup" definition → sectors are comparable. Galaxy and Space Capital are kept as *labeled detail*, NOT in the backbone.

| Layer | Source | File |
|---|---|---|
| Cross-sector annual comparison | **Crunchbase News** funding recaps | `sector_annual.csv` |
| Web3 quarterly hero detail | **Galaxy Digital** *Crypto & Blockchain VC* | `web3_quarterly.csv` (+ `web3_galaxy_provenance.csv`) |
| Landmark deals | mixed (Crunchbase / TechCrunch / Fortune / etc.), cited per row | `landmark_deals.csv` |

**Rule:** one source per line. The backbone is all-Crunchbase — do not splice in CB Insights/PitchBook (scopes differ).

## Backbone citations (Crunchbase)

- **Fintech** — Crunchbase News: "Fintech Funding Jumped 27% In 2025" (https://news.crunchbase.com/fintech/funding-jumped-big-checks-ai-ye-2025/) and the 2023 year-end recap. FY: $90.2B / $43B / $40.8B (4486) / $51.8B (3457).
- **Web3** — Crunchbase News: "Web3 Funding Cratered In 2023" (https://news.crunchbase.com/web3/funding-cratered-sbf-ai-crypto-bitcoin-eoy-2023/) + Q4 2024 recap (https://news.crunchbase.com/web3/crypto-blockchain-vc-dollars-fall-q4-2024/). FY: $26.6B (2891) / $6.8B (1564) / $7.7B (1180). FY2025 still needed.
- **Defense** — Crunchbase News: "Defense Tech Funding Growth YIR 2024" (https://news.crunchbase.com/venture/defense-tech-funding-growth-yir-2024/). FY: $2.6B (113) / $2.7B (100) / $3.0B (102). "Defense tech" = narrow definition.
- **Space** (Crunchbase "space startups," narrow): $9.6B (2022), $5.9B (2023) — to be added to the Defense & Space line; 2024/2025 needed.
- **AI** — Crunchbase News AI/global recaps (EOY 2023, "12 Charts" YE2024, Q1 2026 foundational-AI snapshot). FY: $45.8B / ~$50B / $114B (revised from $100B) / $211B. AI ≈ 50% of all global VC by 2025. Counts not stated.
- Biotech, Climate — not yet gathered.

## Detail / reference sources

- **Galaxy-CryptoVC** — Galaxy Digital *Crypto & Blockchain VC* quarterly, 2022–2025. Full per-quarter provenance in `data/web3_galaxy_provenance.csv`. Powers `web3_quarterly.csv`. Broader scope than Crunchbase web3 (that's why it's detail, not backbone).
- **Space Capital IQ** — broad "space economy" ($20.1B/$12.5B/$26B) — reference only, NOT comparison backbone (counts GPS apps, infrastructure, etc.).

## ⚠ Known scope conflicts (do not naively compare)
- Space: Crunchbase "space startups" $9.6B vs Space Capital IQ "space economy" $20.1B (2022) — different universes.
- Defense: Crunchbase "defense tech" $3B vs PitchBook "aerospace & defense" $19B (2024) — different universes. Backbone uses Crunchbase only.
- Web3: Crunchbase "web3" $26.6B vs Galaxy "crypto VC" >$30B (2022). Backbone uses Crunchbase; Galaxy is the quarterly detail.

## Definitions
- Backbone values in USD billions, annual. Landmark deal amounts in USD millions.
- "Deal value" = disclosed equity VC funding. Lesson: the same metric differs across firms — never mix providers within one line.
