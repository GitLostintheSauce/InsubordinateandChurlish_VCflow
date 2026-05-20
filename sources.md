# Sources

Every number in the dashboard must trace to a citation here. The `source` column of `data/vc_by_sector.csv` holds the short key; the full reference lives below.

## ⭐ Source strategy (per sector — one source per sector's full 16-quarter line)

| Sector | Source | Status |
|---|---|---|
| **Web3** | **Galaxy Digital** — *Crypto & Blockchain Venture Capital* quarterly reports | ✅ complete (16/16) |
| AI | CB Insights *State of AI* (or best consistent source) | not started |
| Fintech | CB Insights *State of Fintech* | not started |
| Climate | CB Insights *State of Climate Tech* | not started |
| Biotech | CB Insights *State of Digital Health / Healthcare* | not started |
| Defense & Space | TBD (least consistently covered) | not started |

**Rules:** one source per sector across all 16 quarters (mixing fakes the trend). Cross-sector $ levels are only loosely comparable because providers differ — trends are the honest comparison.

⚠️ **Watch:** CB Insights appears to have stopped publishing free annual sector PDFs after 2022. The other 5 sectors may need a different consistent source for 2023–2025 (as Web3 did → Galaxy). Decide per sector.

## Active citations

- **Galaxy-CryptoVC** — Galaxy Digital, *Crypto & Blockchain Venture Capital* quarterly reports (2022–2025), https://www.galaxy.com/insights/research/ . Per-quarter URLs, secondary citations, and confirmed-vs-derived status for all 16 quarters are recorded in **`data/web3_galaxy_provenance.csv`**. 14/16 directly cited; 2 derived (see below).
- **estimated** — used in `data/vc_by_sector.csv` for figures derived rather than directly read from a report:
  - **Web3 2022 Q4** ($3.5B): derived from Galaxy ~$30B annual total minus Q1–Q3. Deal count (366) is confirmed.
  - **Web3 2023 Q2** ($1.9B): derived from Galaxy ~$10B 2023 annual minus other quarters. Deal count only known as ">430" → left blank.
  - To close these: pull the primary Galaxy Q4 2022 and Q2 2023 PDFs.

## ⚠ SUPERSEDED (kept for audit trail, NOT used)

Web3 was sourced first from Crunchbase, then CB Insights *State of Blockchain*, before settling on Galaxy Digital for full single-source coverage 2022–2025. Earlier figures differed due to methodology scope (Crunchbase "crypto" < Galaxy < CB Insights "blockchain").

- ~~CBI-Blockchain-2022~~ — CB Insights *State of Blockchain Global 2022 Recap*: Q1 $10.8B/546, Q2 $7.6B/509, Q3 $5.1B/448, Q4 $3.2B/325. Broader scope than Galaxy. Replaced because CB Insights doesn't cover 2023–2025 freely.
- ~~CB-News-Crypto-*~~ — Crunchbase News crypto recaps (2022 quarters, Q1 2025). Narrower scope.

## Definitions / methodology

- All deal values in USD billions; quarterly unless a note says otherwise.
- "Deal value" = disclosed equity VC funding for the period.
- **Revised vs contemporaneous:** Galaxy revises quarters upward over time as late-reported deals are captured (e.g. 2023 Q3 $1.9B → $3.8B). Older quarters here use revised figures; recent quarters are contemporaneous and may rise later. Noted per-row in `note`.
- **Lesson:** the same metric means different things across firms. Never mix providers within one sector's line.
