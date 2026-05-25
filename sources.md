# Sources

Every number traces to a citation here. `source` columns in the data files hold short keys; full references below.

## ⭐ Source strategy

**Comparison backbone (`data/sector_annual.csv`) = Crunchbase annual totals, all 6 sectors.** One consistent "VC-backed startup" definition → sectors are comparable. Galaxy and Space Capital are kept as *labeled detail*, NOT in the backbone.

| Layer | Source | File |
|---|---|---|
| Cross-sector annual comparison | **Crunchbase News** funding recaps | `sector_annual.csv` |
| Web3 quarterly hero detail | **Galaxy Digital** *Crypto & Blockchain VC* | `web3_quarterly.csv` (+ `raw/web3_galaxy_quarterly_provenance.csv`) |
| Landmark deals | mixed (Crunchbase / TechCrunch / Fortune / etc.), cited per row | `landmark_deals.csv` |

**Rule:** one source per line. The backbone is all-Crunchbase — do not splice in CB Insights/PitchBook (scopes differ).

## Backbone citations (Crunchbase)

- **Fintech** — Crunchbase News: "Fintech Funding Jumped 27% In 2025" (https://news.crunchbase.com/fintech/funding-jumped-big-checks-ai-ye-2025/) and the 2023 year-end recap. FY: $90.2B / $43B / $40.8B (4486) / $51.8B (3457).
- **Web3** — Crunchbase News: "Web3 Funding Cratered In 2023" (https://news.crunchbase.com/web3/funding-cratered-sbf-ai-crypto-bitcoin-eoy-2023/) + Q4 2024 recap (https://news.crunchbase.com/web3/crypto-blockchain-vc-dollars-fall-q4-2024/). FY: $26.6B (2891) / $6.8B (1564) / $7.7B (1180) / **~$12B (2025, ESTIMATED)**. Crunchbase published no clean FY2025 web3 total (only Q1 = $3.8B); the 2025 global recap notes crypto "gained ground YoY." Estimate = 2024 base + that gain, cross-checked against Galaxy's ~+73% recovery. Marked `estimated`.
- **Defense** — Crunchbase News: "Defense Tech Funding Growth YIR 2024" (https://news.crunchbase.com/venture/defense-tech-funding-growth-yir-2024/) and "Sector Snapshot: Defense Tech Funding Hits Record High" (https://news.crunchbase.com/defense-tech/funding-hits-record-high-2025-snapshot/). FY: $2.6B (113) / $2.7B (100) / $3.0B (102) / **$7.7B (~100, 2025)** — all "military/national security/law enforcement" narrow definition. Line is defense-tech only; Crunchbase "space startups" ($9.6B'22/$5.9B'23) not separately folded in.
- **Space** (Crunchbase "space startups," narrow): $9.6B (2022), $5.9B (2023) — to be added to the Defense & Space line; 2024/2025 needed.
- **AI** — Crunchbase News AI/global recaps (EOY 2023, "12 Charts" YE2024, Q1 2026 foundational-AI snapshot). FY: $45.8B / ~$50B / $114B (revised from $100B) / $211B. AI ≈ 50% of all global VC by 2025. Counts not stated.
- **Climate** — Crunchbase News sustainability/cleantech recaps. FY: $14B (est) / $13.9B / $24B / $20B. ⚠ SCOPE SHIFT WITHIN LINE: 2022/2023 = equity-only; 2024/2025 = "all stages" incl project finance/debt. The $13.9B→$24B jump is partly scope, not growth (equity-only 2024 H1 was actually DOWN 10%). HolonIQ/BloombergNEF report $56-70B on far broader definitions — not used.
- **Biotech** — Crunchbase News health/biotech recaps. FY: $40B (US-only avg, est) / **~$52B (2023, ESTIMATED)** / $60B (global, derived) / $71.7B (global, stated). ⚠ SCOPE SHIFT WITHIN LINE: 2022 is a US-only boom average; 2024/2025 are global "Health, Wellness & Biotech." Only 2025 is directly stated; 2023 estimated as the trough between the 2022 boom and 2024's ~$60B (no clean Crunchbase broad-global FY2023 published). The weakest line — slopes indicative, not precise.

## Detail / reference sources

- **Galaxy-CryptoVC** — Galaxy Digital *Crypto & Blockchain VC* quarterly, 2022–2025. Full per-quarter provenance in `data/raw/web3_galaxy_quarterly_provenance.csv`. Powers `web3_quarterly.csv`. Broader scope than Crunchbase web3 (that's why it's detail, not backbone).
- **Space Capital IQ** — broad "space economy" ($20.1B/$12.5B/$26B) — reference only, NOT comparison backbone (counts GPS apps, infrastructure, etc.).

## ⚠ Known scope conflicts (do not naively compare)
- Space: Crunchbase "space startups" $9.6B vs Space Capital IQ "space economy" $20.1B (2022) — different universes.
- Defense: Crunchbase "defense tech" $3B vs PitchBook "aerospace & defense" $19B (2024) — different universes. Backbone uses Crunchbase only.
- Web3: Crunchbase "web3" $26.6B vs Galaxy "crypto VC" >$30B (2022). Backbone uses Crunchbase; Galaxy is the quarterly detail.

## Definitions
- Backbone values in USD billions, annual. Landmark deal amounts in USD millions.
- "Deal value" = disclosed equity VC funding. Lesson: the same metric differs across firms — never mix providers within one line.

## AI–energy nexus (the AI section's chart)

Deal-level rounds: `data/energy_ai_funding.csv` (per-row source links). Hyperscaler PPAs: `data/energy_ai_ppa.csv`. The deal list is **selected notable rounds, not a sector total** — it under-counts (esp. 2024). The card's headline figures use published **aggregates**:

- **Next-gen nuclear VC ≈ $2.4B in 2024, ~12× the prior year** — Oliver Wyman, "Clean Energy Startups Hit New VC Investment Peak In 2024" (https://www.oliverwyman.com/our-expertise/insights/2025/may/venture-capital-funding-clean-energy-startups-rebounds.html). Same source: clean-energy startup VC rebounded to ~$12.5B in 2024.
- **Private fusion ≈ $2.64B** in the year to mid-2025 — Fusion Industry Association (https://www.fusionindustryassociation.org/over-2-5-billion-invested-in-fusion-industry-in-past-year/).
- Data-center electricity demand — LBNL (US: 176 TWh / 4.4% in 2023 → 325–580 TWh by 2028) and IEA (global: 415 TWh in 2024 → ~945 TWh by 2030).
- ⚠ Lesson logged: a hand-curated deal list cannot produce a reliable year-over-year total/multiple. Earlier drafts ("14×", then "4×") were under-counting artifacts; the card now leads with aggregates and the honest caveat.
