# Phase 1 Data Plan — "Where is the money flowing, and when?"

The dashboard answers one question: **where is VC money flowing across sectors, and when?** That drives the data model below. Reusable for prompting any AI model.

---

## 1. Data model (3 files)

| File | Role | Granularity |
|---|---|---|
| `data/sector_annual.csv` | **Comparison backbone** — the cross-sector "where + when" | annual, 6 sectors × 4 years = 24 rows |
| `data/web3_quarterly.csv` | **Web3 hero deep-dive** (crypto is the audience's market) | quarterly, 16 rows |
| `data/landmark_deals.csv` | **Landmark deals** (t5) — texture under the totals | per-deal |

**Sectors (fixed, 6):** AI · Fintech · Climate · Defense · Web3 · Biotech
**`sector_annual.csv` schema:** `sector, year, deal_value_usd_b, deal_count, source, note`

---

## 2. Source strategy — Crunchbase is the backbone

For an honest cross-sector comparison, every sector's annual total must use the **same definition**. So:

- **Backbone = Crunchbase annual totals, all 6 sectors.** It's the one free source covering every sector with a consistent "VC-backed startup" definition. Cross-sector bars are then comparable.
- **Galaxy Digital** = Web3 *quarterly* detail only (broader scope than Crunchbase — kept separate, labeled).
- **Defense is defense-tech only.** Space data is intentionally excluded rather than mixed into the same line.

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

**Backbone `sector_annual.csv` — 24/24:**
```
                2022    2023    2024    2025
AI              45.8    50.0   114.0   211.0    ✅ the surge → ~50% of all VC by 2025
Fintech         90.2    43.0    40.8    51.8    ✅
Climate         14.0e   13.9    24.0!   20.0    ⚠ scope shift: '22/'23 equity-only, '24/'25 all-stages
Defense          2.6     2.7     3.0     7.7     ✅ narrow Crunchbase defense-tech definition
Web3            26.6     6.8     7.7    12.0e   ⚠ 2025 estimated; no clean Crunchbase FY2025 total found
Biotech         40.0e   52.0e   60.0e   71.7    ⚠ '22 US-only, '24 derived, '23 estimated, '25 global
```
`e` = estimated/derived · `!` = scope-widened
**`web3_quarterly.csv`:** ✅ 16/16 (Galaxy). **`landmark_deals.csv`:** ✅ 145 deals after removing space-only and dual-use space rows.

**Remaining source caveats:**
1. Web3 FY2025 remains estimated because no clean Crunchbase full-year total was found.
2. Climate and Biotech have internal scope inconsistencies — see `sources.md`. These are footnoted and should not be used for precise slope claims.
3. Defense is intentionally defense-tech only; space data was removed to keep the category defensible.

---

## 6. Handoff
Paste raw model replies (links and all) into the Claude Code session. Claude structures them into the files, catches source-drift, and logs citations in `sources.md`.

For the actual tool/process record, see `PROMPTS.md`. It now includes the later Codex sessions: repo audit, docs cleanup, Defense-only scope correction, Defense chart visibility fix, UI/UX redesign, browser QA, and guidance on when to use Codex vs. Claude Code on similar projects.
