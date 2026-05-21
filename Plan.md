# Phase 1 Data Plan — "Where is the money flowing, and when?"

The dashboard answers one question: **where is VC money flowing across sectors, and when?** That drives the data model below. Reusable for prompting any AI model.

---

## 1. Data model (3 files)

| File | Role | Granularity |
|---|---|---|
| `data/sector_annual.csv` | **Comparison backbone** — the cross-sector "where + when" | annual, 6 sectors × 4 years = 24 rows |
| `data/web3_quarterly.csv` | **Web3 hero deep-dive** (crypto is the audience's market) | quarterly, 16 rows |
| `data/landmark_deals.csv` | **Landmark deals** (t5) — texture under the totals | per-deal |

**Sectors (fixed, 6):** AI · Fintech · Climate · Defense & Space · Web3 · Biotech
**`sector_annual.csv` schema:** `sector, year, deal_value_usd_b, deal_count, source, note`

---

## 2. Source strategy — Crunchbase is the backbone

For an honest cross-sector comparison, every sector's annual total must use the **same definition**. So:

- **Backbone = Crunchbase annual totals, all 6 sectors.** It's the one free source covering every sector with a consistent "VC-backed startup" definition. Cross-sector bars are then comparable.
- **Galaxy Digital** = Web3 *quarterly* detail only (broader scope than Crunchbase — kept separate, labeled).
- **Space Capital IQ** = optional space deep-dive reference (very broad scope — NOT used in the comparison).

**Hard rules:**
1. **One source per line.** The annual backbone is all-Crunchbase. Don't splice PitchBook/CB Insights into it (their scopes differ — e.g. PitchBook "defense" $10B vs Crunchbase "defense tech" $3B).
2. **Cross-sector levels are only comparable because they're all Crunchbase.** Note any sector where that breaks.
3. **No estimating.** Missing cell → blank + `source = TODO-Crunchbase`. If you must approximate, `source = estimated` + explain in `note`.

---

## 3. Rules for the AI (paste at the TOP of every data prompt)

```
RULES — follow exactly:
- Every figure needs a specific article/report title AND a working link. No link = NOT FOUND.
- Use ONLY Crunchbase figures. Do not substitute CB Insights / PitchBook / others without saying so.
- If a year isn't reported by Crunchbase, say "not reported" — do NOT estimate or borrow another source.
- Give deal value in USD billions and deal count as separate numbers.
- Flag any single mega-round that distorts a year's total.
```

---

## 4. Prompt templates

### Template A — Crunchbase annual totals for one sector (the main task)
```
[paste RULES block]

From Crunchbase News' funding recaps, give me TOTAL [SECTOR] venture funding for each full year 2022, 2023, 2024, 2025.
For each year: total deal value (USD billions) and deal count. Cite the specific Crunchbase News article + link per year.
```
Swap `[SECTOR]`: "AI / artificial intelligence", "biotech / healthcare", "climate tech".

### Template B — landmark deals for a sector (already mostly done)
```
[paste RULES block]

Give me the 5 largest [SECTOR] venture rounds of [YEAR]: company, amount (USD millions), round type, lead investor, quarter, and a source link each.
```

---

## 5. Progress

**Backbone `sector_annual.csv` — 10/24:**
```
                2022    2023    2024    2025
AI               —       —       —       —      ← NEXT
Fintech         90.2    43.0    40.8    51.8    ✅
Climate          —       —       —       —      ← then this
Defense&Space    2.6*    2.7*    3.0*     —      *defense-only; add Crunchbase "space startups" ($9.6B'22, $5.9B'23) + 2025
Web3            26.6     6.8     7.7      —      need Crunchbase FY2025 (only Q1 $3.8B confirmed)
Biotech          —       —       —       —      ← then this
```
**`web3_quarterly.csv`:** ✅ 16/16 (Galaxy). **`landmark_deals.csv`:** ✅ 106 deals.

**Remaining to gather (all Crunchbase annual):**
1. **AI** 2022–2025 (Template A) — the headline surge
2. **Biotech** 2022–2025
3. **Climate** 2022–2025
4. Stragglers: Web3 FY2025, Defense&Space 2025 + the space component, 2024 space

**Open question:** "Defense & Space" is one sector but Crunchbase tracks them separately (defense tech ~$3B vs space startups ~$9.6B). Decide: combine the two Crunchbase cuts, or split into two sectors (would break the 6-sector cap).

---

## 6. Handoff
Paste raw model replies (links and all) into the Claude Code session. Claude structures them into the files, catches source-drift, and logs citations in `sources.md`.
