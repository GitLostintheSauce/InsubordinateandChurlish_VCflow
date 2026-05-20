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

## 2. Source strategy — keep it to TWO sources

The whole point is consistency. Target **just two providers**:

| Sectors | Source | Why |
|---|---|---|
| **Web3 / Crypto** | **Crunchbase News** quarterly crypto recaps | Crypto-native, published every quarter, openly accessible |
| **AI, Fintech, Climate, Defense & Space, Biotech** | **CB Insights — State of Venture** (quarterly) | One report series covering all sectors → cross-sector comparability |

**Hard rules:**
1. **One source per sector, across all 16 quarters.** Mixing sources *within* a sector's time series fakes the trend (different firms count deals differently). This is non-negotiable.
2. Prefer a **single report series per provider**. For the 5 CB Insights sectors, use *State of Venture* throughout. Only if *State of Venture* doesn't break out a sector in a given quarter, fall back to that sector's dedicated CB Insights report (e.g. *State of Fintech*, *State of Climate Tech*) — still CB Insights, so methodology stays close.
3. **A third source is a last resort**, only when neither CB Insights nor Crunchbase reports a sector-quarter at all (Defense & Space is the likely problem child). If used, label it explicitly in `source` and `note`, and accept that cell is not strictly comparable.
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

### Template C — Crunchbase, Web3 across a full year
```
[paste RULES block]

From Crunchbase News' quarterly crypto/blockchain venture funding recaps, give me global crypto & blockchain startup funding for each quarter of [YEAR]: Q1, Q2, Q3, Q4.
For each: total deal value (USD billions) and deal count, from Crunchbase only.
Cite the specific Crunchbase News article and link for each quarter.
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

**Web3 (Crunchbase):** 5/16
```
2022:  Q1 4.9*  Q2 4.2   Q3 3.6   Q4 2.4      (*Q1 needs source link)
2023:  Q1 —     Q2 —     Q3 —     Q4 —
2024:  Q1 —     Q2 —     Q3 —     Q4 —
2025:  Q1 3.8   Q2 —     Q3 —     Q4 —
```

**AI, Fintech, Climate, Defense & Space, Biotech (CB Insights):** 0/80 — not started.

**Known gaps / risks:**
- Q1 2022 Web3 ($4.9B) is provisional — needs the specific Crunchbase article link.
- Defense & Space is least likely to be broken out by either provider — expect a labeled fallback source or `estimated` cells here.
- Deal counts come back patchy (sources lead with $). Value is primary; leave counts blank rather than guess.
