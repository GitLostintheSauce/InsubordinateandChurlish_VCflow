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

## 2. Source strategy — ONE provider: CB Insights

The whole point is consistency. Target **a single provider for all 6 sectors: CB Insights**, using its annual **"State of [Sector]" recap PDFs** (each holds the four quarterly figures under one methodology). Every sector then compares cleanly to every other.

| Sector | CB Insights report |
|---|---|
| AI | State of AI |
| Fintech | State of Fintech |
| Climate | State of Climate Tech |
| Defense & Space | (least consistently covered — possible labeled fallback) |
| Web3 | State of Blockchain |
| Biotech | State of Digital Health / Healthcare |

*(These PDFs often surface on third-party sites even when the CB Insights platform is paywalled.)*

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

### Template C — CB Insights State of Blockchain, Web3 for a full year
```
[paste RULES block]

From the CB Insights "State of Blockchain — Global [YEAR] Recap" report, give me the quarterly blockchain/crypto venture funding for [YEAR]: Q1, Q2, Q3, Q4.
For each quarter: total deal value (USD billions) and deal count, plus the full-year total.
Cite the specific CB Insights report and a link to the PDF.
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

**Web3 (CB Insights State of Blockchain):** 4/16
```
2022:  Q1 10.8  Q2 7.6   Q3 5.1   Q4 3.2      ✅ from State of Blockchain 2022 Recap
2023:  Q1 —     Q2 —     Q3 —     Q4 —         (need State of Blockchain 2023)
2024:  Q1 —     Q2 —     Q3 —     Q4 —         (need State of Blockchain 2024)
2025:  Q1 —     Q2 —     Q3 —     Q4 —         (need State of Blockchain 2025)
```

**AI, Fintech, Climate, Defense & Space, Biotech (CB Insights):** 0/80 — not started.

**Known gaps / risks:**
- Web3 switched from Crunchbase to CB Insights (single-provider consistency). The old Crunchbase Q1 2025 ($3.8B) was removed — re-pull from State of Blockchain 2025.
- Defense & Space is least likely to be broken out by CB Insights — expect a labeled fallback source or `estimated` cells here.
- Deal counts come back patchy (sources lead with $). Value is primary; leave counts blank rather than guess.
