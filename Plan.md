# Phase 1 Data Acquisition Plan — VC Funding by Sector, 2022–2025

A reusable playbook for gathering the dashboard's funding data with **as few distinct sources as possible**. Built to be pasted into any AI model (Perplexity, ChatGPT, Claude, etc.) to extract real, cited numbers.

---

## 1. The goal

Fill `data/vc_by_sector.csv` — **6 sectors × 16 quarters (Q1 2022 → Q4 2025) = 96 rows**. Every cell must trace to a real, linkable source, or be left blank / marked `estimated`. **No invented numbers.**

### Sectors (fixed)
AI · Fintech · Climate · Defense & Space · Web3 · Biotech

### Exact output schema (one row per sector per quarter)
| column | meaning |
|---|---|
| `year` | 2022–2025 |
| `quarter` | 1–4 |
| `sector` | one of the 6 above (exact spelling) |
| `deal_value_usd_b` | total VC deal value, USD **billions** |
| `deal_count` | number of deals (blank if not stated) |
| `source` | short citation key (see `sources.md`) |
| `note` | qualifiers: annual-vs-quarterly, outlier rounds, ">500", etc. **No commas** (breaks CSV) |

---

## 2. Source strategy — one consistent source per sector

The whole point is consistency: **each sector's 16-quarter line uses ONE source the whole way.** Use CB Insights where it publishes freely; switch to the best consistent alternative where it doesn't (as Web3 did → Galaxy).

| Sector | Source | Note |
|---|---|---|
| Web3 | **Galaxy Digital** *Crypto & Blockchain VC* (quarterly) | ✅ done — CB Insights only free through 2022 |
| AI | CB Insights *State of AI* | verify 2023–25 are free |
| Fintech | CB Insights *State of Fintech* | |
| Climate | CB Insights *State of Climate Tech* | |
| Biotech | CB Insights *State of Digital Health* | |
| Defense & Space | TBD — least covered | likely fallback / `estimated` |

*(CB Insights PDFs often surface on third-party sites even when the platform is paywalled — but appear to stop after 2022.)*

**Hard rules:**
1. **One source per sector, across all 16 quarters.** Mixing sources *within* a sector's time series fakes the trend (different firms count deals differently — Crunchbase "crypto" came in ~half of CB Insights "blockchain"). Non-negotiable.
2. **Cadence:** these are *annual* recaps with quarterly breakdowns inside, not standalone quarterly reports. One PDF per sector per year gives you that year's Q1–Q4. The 2025 recaps publish early 2026 (now available).
3. **A second provider is a last resort**, only when CB Insights doesn't cover a sector-quarter at all (Defense & Space is the likely problem child). If used, label it explicitly in `source` + `note` and accept that cell isn't strictly comparable.
4. **If a number can't be sourced, leave it blank** and note why. Never estimate to fill a hole. If you must approximate, mark `source = estimated` and explain in `note`.

---

## 3. Rules for the AI (paste this block at the TOP of every data prompt)

```
RULES — follow exactly:
- Every figure must come with a SPECIFIC article/report title AND a working link. No link = treat the number as NOT FOUND.
- Use ONLY the source I name in this prompt. Do not substitute another source without saying so explicitly.
- If a sector or quarter is not directly reported by that source, say "not reported" — do NOT estimate, interpolate, or borrow from another source.
- Give deal value in USD billions and deal count as separate numbers.
- Flag any single mega-round that distorts a quarter's total (e.g. one $2B deal).
- Do not "correct" or "recall" figures from memory. Only report what the cited article states.
```

---

## 4. Prompt templates

### Template A — CB Insights, one sector across a full year (preferred: tight + comparable)
```
[paste RULES block]

From CB Insights' State of Venture quarterly reports, give me [SECTOR] global VC funding for each quarter of [YEAR]: Q1, Q2, Q3, Q4.
For each quarter: total deal value (USD billions) and deal count.
Cite the specific CB Insights report and link for each quarter.
```

### Template B — CB Insights, one quarter across all 5 sectors (good for completing a column)
```
[paste RULES block]

From CB Insights' State of Venture report for [QUARTER YEAR], give me global VC funding for each of: AI, Fintech, Climate tech, Defense/Space, Biotech (or healthcare).
For each: total deal value (USD billions) and deal count.
Cite the specific CB Insights report/section and link for each sector.
```

### Template C — Galaxy Digital, Web3 for a full year (Web3 DONE; kept as the crypto pattern)
```
[paste RULES block]

From Galaxy Digital's "Crypto & Blockchain Venture Capital" quarterly reports for [YEAR], give me Q1-Q4 deal value (USD billions) and deal count, plus the full-year total.
Read figures directly from each quarter's report — do NOT derive from other quarters. Cite each with a galaxy.com link.
```

### Template D — get a missing citation link (upgrade a provisional cell)
```
For [SECTOR] in [QUARTER YEAR], the figure is reported as ~$[X]B. Give me the EXACT [Crunchbase News / CB Insights] article title and link that states this number. If you cannot find the specific article, say so.
```

---

## 5. Recommended order of attack

1. **Web3 line first** (Template C, year by year) — it's the hero sector and single-source.
2. **Anchor quarters for the other 5 sectors**: Q1 2022 and Q4 2025 (Template B) — these define the migration story's endpoints.
3. **AI line** (Template A) — the headline "AI surge" trend.
4. Fill remaining sectors year by year (Template A), one sector at a time so a source switch is obvious if it happens.
5. Mop up gaps; mark anything unsourced as blank or `estimated`.

---

## 6. How to hand results back

Paste the model's **raw reply** (links and all) into the Claude Code session — don't clean it up first. Claude will (a) catch source-drift, (b) structure it into `data/vc_by_sector.csv`, (c) add the citation to `sources.md`. The CSV and `sources.md` are the source of truth, not this file.

---

## 7. Verification checklist (before any cell is "clean")
- [ ] Has a specific source **link**, not just a description
- [ ] Source matches the sector's assigned provider (Crunchbase=Web3, CB Insights=others)
- [ ] Value is in USD billions, quarterly (note if annual/half-year)
- [ ] Outlier mega-rounds flagged in `note`
- [ ] No commas in the `note` field

---

## 8. Progress tracker (update as cells fill)

**Web3 (Galaxy Digital):** ✅ 16/16
```
2022:  Q1 14.2  Q2 10.0  Q3 5.5   Q4 3.5*
2023:  Q1 2.4   Q2 1.9*  Q3 3.8   Q4 1.93
2024:  Q1 2.49  Q2 3.19  Q3 2.4   Q4 3.5
2025:  Q1 4.9   Q2 1.97  Q3 4.65  Q4 8.5
   * = estimated/derived (2022 Q4, 2023 Q2); full provenance in data/web3_galaxy_provenance.csv
```

**AI, Fintech, Climate, Defense & Space, Biotech:** 0/80 — not started. **AI is next.**

**Known gaps / risks:**
- 2 Web3 cells derived (2022 Q4, 2023 Q2) — marked `estimated`; close by pulling the primary Galaxy Q4 2022 / Q2 2023 PDFs.
- CB Insights free sector PDFs appear to stop after 2022 — the other 5 sectors may each need a Galaxy-style source switch for 2023–25. Decide per sector.
- Defense & Space least covered — expect a labeled fallback or `estimated` cells.
- Deal counts come back patchy (sources lead with $). Value is primary; leave counts blank rather than guess.
