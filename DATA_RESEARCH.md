# Data Research — Upgrading the VC Funding Backbone

*Deep-research run, 2026-06-09. 6 source families investigated in parallel (non-overlapping), 25 sources fetched, 124 claims extracted, top 25 adversarially verified by 3-vote panels: 24 confirmed, 1 refuted. Verifiers reproduced the key claims live (downloaded SEC bulk ZIPs, hit the EDGAR API, parsed DefiLlama's embedded dataset record-by-record).*

## The problem this solves

The dashboard's known data weaknesses:
1. No deal counts for AI / Climate / Biotech (Crunchbase never published them)
2. Web3 FY2025 is estimated
3. Climate and Biotech shift scope definitions across years
4. Only 145 hand-curated landmark deals as deal-level data

Strategy: pull as much **raw deal-level data as possible for free**, then combine + dedupe — instead of relying on editorial aggregate totals.

## Verdict (TL;DR)

A free raw backbone is achievable from **two sources**:

1. **SEC Form D bulk data** — the cross-sector US foundation. Free, public-domain, quarterly ZIPs covering every quarter of 2022–2025 (~13.6k offerings/quarter), with issuer, sale date, amounts, investor counts. Extract with the MIT-licensed `edgartools` Python library.
2. **DefiLlama Raises** — the Web3 fix. ~6,700–7,000 deal-level records (name, date, amount, round, investors, category) covering 2014–2026. The API is now paywalled ($300/mo) **but the full dataset is still free** via the page's embedded `__NEXT_DATA__` JSON / CSV-download buttons.

Almost everything else failed the free test: Dealroom (sales-gated, ~€20–50k/yr), Messari fundraising (Pro/Enterprise only), RootData API (paid Plus/Pro), OpenVC (investor directory — zero deal records). Crunchbase's license allows publishing **aggregates with attribution** but prohibits republishing any raw rows — so it stays a benchmark layer, never a deal feed.

**Honest framing requirement:** Form D totals will *systematically diverge* from editorial headline numbers (no round labels, pooled-fund noise, late/non-filers). Publish the new pipeline as an **independent bottom-up series with a reconciliation view** against the Crunchbase News numbers — not a silent replacement. This matches the project's existing honesty conventions.

## Verified source evaluations

### ✅ SEC Form D bulk data sets — the backbone (confidence: high, 3-0)
- **What:** Structured quarterly TSVs of all Form D exempt-offering filings (Reg D 504/506(b)/506(c), §4(a)(5)). Sept 2009 → March 2026; all 16 quarters of 2022–2025 present (2.9–4.06 MB each). Verifier unzipped `2024q4_d.zip`: tables `FORMDSUBMISSION, OFFERING, ISSUERS, RELATEDPERSONS, RECIPIENTS, SIGNATURES`; 13,612 offerings that quarter.
- **Fields:** issuer name/location, `SALE_DATE`, `TOTALOFFERINGAMOUNT`, `TOTALAMOUNTSOLD`, exemption list, equity-type flag, investor counts.
- **Access:** free unauthenticated download. **License:** US-government public domain.
- **Gaps:** as-filed (SEC disclaims accuracy); no round labels (Seed/Series A); no named investors; many filings are pooled funds that must be filtered out; stealth/late/non-filers missed.
- Source: https://www.sec.gov/data-research/sec-markets-data/form-d-data-sets

### ✅ EDGAR full-text search API — the between-quarters refresher (high, 3-0)
- `efts.sec.gov/LATEST/search-index?forms=D&dateRange=custom&startdt=…&enddt=…` — free JSON, no API key; just needs an identifying `User-Agent` (403 otherwise). ~10 req/sec fair-access cap (applies to everyone; not a paid tier).
- Returns filing metadata (CIK, issuer name, file date, accession, location) — amounts/round/investors require a second fetch of each filing's `primary_doc.xml`.
- Verified live: a 2-week 2022 slice returned exactly 3,315 Form D hits.

### ✅ edgartools — the extraction tool (high, 3-0)
- MIT-licensed, pip-installable, actively maintained (~2.3k stars, release 5.35.x June 2026). No key/signup; only `set_identity(email)` per SEC rules. Parses Form D into typed objects (`filing.obj() → .offering`, `.recipients`). MIT license = no vendor ToS on the tooling.
- https://github.com/dgunning/edgartools

### ✅ DefiLlama Raises — the Web3 fix (high, 3-0 on access; see refuted note)
- Per-deal records: name, unix date, amount ($M), round type, category/categoryGroup, lead + other investors, chains, valuation; source URL on ~56% of rows. 6,724 raises / $133.0B (Jan 2026 snapshot) → 7,005 / $140.1B (May 2026). Covers 2014–2026, fully spanning 2022–2025.
- **Access:** `api.llama.fi/raises` now returns HTTP 402 (Pro-only, $300/mo) — verified live. **But** `defillama.com/raises` is statically generated with the entire dataset embedded in `__NEXT_DATA__`, plus "Download .csv/.json" buttons. Direct `curl` hits Cloudflare 403; works via a normal browser (or Wayback snapshots).
- ⚠️ **Refuted claim (0-3):** an agent's computed per-year totals (e.g. FY2025 = $25.5B) did NOT survive verification. The dataset's existence, fields, and grand totals are verified; **annual aggregates must be computed and validated hands-on after download**, and reconciled against Galaxy's quarterly series.

### ✅ RootData — secondary Web3 cross-check (high, 3-0)
- 9,239 deal records (Dec 2025) with project/round/amount/valuation/date/source/investors and rich filters. API has a dedicated fundraising endpoint — **but it's paid** (Plus $128/mo or Pro $328/mo; free Basic tier covers only search/project/org lookups). Site is Tencent-captcha-walled. Use as a browsable spot-check, not a bulk feed.

### ❌ Messari — paywalled (high, 3-0)
14,000+ rounds, crypto-only. Browsing requires Pro; exports Enterprise; API access by sales contact. Not viable; covers 1 of 6 sectors.

### ❌ Dealroom — sales-gated (high, 3-0)
Real API with deal-level `/transactions/bulk` endpoints exists, but "Premium API" with no public pricing or free tier (platform €12.6k–€17k/yr; reported API ~€20k–€50k/yr).

### ❌ OpenVC — wrong data shape (high, 3-0)
Free, but it's a directory of ~16,700 **investor profiles**. No funded company, amount, date, or round fields at all.

### ⚖️ Crunchbase license — benchmark layer only (high, 3-0 / 2-1)
- Verified verbatim on the live license: *"Licensee may not license, sublicense, sell... distribute or otherwise provide any Crunchbase data to any third parties"* — raw rows can never be republished.
- *"Analysis and aggregate statistics derived from the data may be published"* — with visible "Powered by Crunchbase" attribution. **Applies only to validly licensed data** — it does not legitimize Kaggle/HuggingFace scraped dumps (the only legal open snapshot is the Oct 2013 CC-BY one, useless for 2022–2025).

## The pipeline plan

### Acquisition
1. **Backbone:** download all 16 SEC Form D quarterly ZIPs for 2022–2025; refresh current-quarter gaps via EDGAR full-text search + `edgartools`.
2. **Web3:** export DefiLlama raises JSON/CSV from the embedded page data; cross-check against RootData's browsable tracker; reconcile annual sums to Galaxy quarterly aggregates as the benchmark.
3. **Benchmarks:** keep Crunchbase News (and Galaxy) as aggregate reference series — never as redistributed rows.

### Dedup / entity resolution
- **Block** on normalized company name: lowercase, strip Inc/LLC/Ltd/Labs suffixes, token-sort; fuzzy-match within blocks (e.g. Jaro-Winkler > 0.9). Candidate tooling (verified, open-source): `splink` (MOJ) or `dedupe`.
- **Match** when: dates within **±90 days** (Form D `SALE_DATE` lags press announcements) AND amounts within **±10–15%** (`TOTALAMOUNTSOLD` often differs from announced round size; watch multi-tranche filings by the same issuer). Tie-break on investor overlap + HQ state.
- **Survivorship:** regulatory filing wins for amount/date/legal entity; news/crypto-tracker record wins for round label and named investors (Form D has neither).

### Sector mapping (fixes the scope-drift problem)
One **frozen, documented taxonomy** applied identically to all four years: inclusion keyword rules + classifier over company descriptions and Form D industry-group/SIC codes; DefiLlama/RootData category fields map directly to Web3. Validate the classifier against the 145 hand-curated landmark deals as labeled ground truth and report the measured error rate.

### Expected improvement (and limits)
- Deal counts become available for **all 6 sectors** (currently missing for AI/Climate/Biotech).
- Web3 FY2025 moves from estimate to **deal-level actuals**.
- Definitions become consistent across 2022–2025.
- Totals will **not** match Crunchbase News headlines — publish as an independent bottom-up series with a reconciliation view. Quantitative accuracy gain is an expectation, not a measured result, until the pipeline runs.

## Caveats from the research itself

- **Three source families produced no surviving verified claims:** (d) sector-specific trackers (CTVC/Sightline, BioPharma Dive/Evaluate, defense-tech), (e) news-scale extraction (GDELT, Common Crawl, RSS), and most of (b) (Kaggle/HF dumps, academic sets, non-US regulatory equivalents). Sector classification for AI/Climate/Defense/Biotech therefore rests on Form D + taxonomy work alone — the least-proven part of the plan.
- **Time-sensitivity:** DefiLlama's API went free → $300/mo; its free web-export path depends on a Cloudflare-fronted static page that could change. RootData docs were verified via Wayback. Vendor ToS can change.
- Some verifications (OpenVC, RootData, DefiLlama page data) relied on archived snapshots/indexed metadata because live fetches returned 403/captcha.

## Open questions (next actions)

1. Download the DefiLlama dataset and compute real 2022–2025 annual sums; reconcile vs. Galaxy. *(The one attempt to do this in-research was refuted 0-3.)*
2. Do CTVC/Sightline, BioPharma Dive/Evaluate, or any defense tracker expose raw deal rows, or only editorial aggregates? (Main remaining gap for non-Web3 sectors.)
3. Can GDELT/Common Crawl/RSS extraction recover round labels + named investors at acceptable precision to enrich Form D rows, and at what engineering cost?
4. How reliably can Form D records be classified into "AI" and "Defense tech" (no native Form D category)? Measure false-positive/negative rates against the 145 landmark deals before publishing any counts.

## Key sources

| Source | Quality | Role |
|---|---|---|
| [SEC Form D data sets](https://www.sec.gov/data-research/sec-markets-data/form-d-data-sets) | primary | backbone bulk data |
| [EDGAR full-text search](https://efts.sec.gov/LATEST/search-index?forms=D) | primary | between-quarter refresh |
| [edgartools](https://github.com/dgunning/edgartools) | primary (MIT) | extraction tooling |
| [DefiLlama raises](https://defillama.com/raises) + [API docs](https://api-docs.defillama.com/) | primary | Web3 deal rows |
| [RootData fundraising](https://www.rootdata.com/Fundraising) | primary | Web3 cross-check |
| [Crunchbase license](https://data.crunchbase.com/docs/license-agreement) | primary | legal constraints |
| [splink](https://github.com/moj-analytical-services/splink) / [dedupe](https://github.com/dedupeio/dedupe) | primary (OSS) | entity resolution |
| [Dealroom API](https://docs.dealroom.co/docs/premium-api), [Messari fundraising](https://messari.io/fundraising-data), [OpenVC](https://www.openvc.app/investor-database) | primary | evaluated, ruled out |
