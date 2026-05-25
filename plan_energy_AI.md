# Plan: Is AI's Energy Appetite Pulling VC Into Power? (Energy × AI)

## The spark
CB Insights *Venture Trends 2025* (https://www.cbinsights.com/research/report/venture-trends-2025/): **~48% of all VC went to AI in 2025**, and **~49% of AI VC went to just 6 companies** — one being **Aligned**, which builds AI data centers. Data centers are enormously power-hungry, and the AI buildout is now constrained by *electricity*, not just chips. So the question:

> **As AI capital concentrates and data-center buildout explodes, is venture money following into the energy that powers it — and who is actually capturing that money?**

## Research questions
1. **Has VC funding to energy/power companies (especially data-center power) risen 2024 → 2025?**
2. **Is that rise correlated with the AI funding surge — and is the link causal or just coincident?**
3. **The discrepancy:** within "energy for AI," are *startups* capturing the VC, or are *established players / project finance / hyperscaler power deals* taking the largest share?
4. **How did all of this shift specifically from 2024 to 2025?**

## Working hypothesis (to test, not assume — confirm or kill it with data)
The energy *supply* for AI is flowing disproportionately to **established players, project finance, and hyperscaler power-purchase agreements (PPAs)** — Microsoft–Constellation, Amazon–X-energy, Google–Kairos, Meta's nuclear RFP — while pure-play **energy startups capture a smaller venture slice**. If true, this *mirrors the concentration we already documented in AI itself*: the money piles into a few large, de-risked recipients. The interesting tension is that "AI is creating an energy boom" may be truer for incumbents and infrastructure finance than for the startup venture market.

---

## Part A — Mine the existing repo FIRST (don't gather what you already have)

Before any new research, extract every energy/power signal already in the repo:

- **`data/landmark_deals.csv`** — filter `sector = Climate` for energy/power rows. We already have:
  - **X-energy** ($500M, Amazon, advanced nuclear/SMR — note explicitly says *"to power data centers"*) — the single most on-thesis deal we own.
  - **Base Power** ($200M, residential energy storage), **Generate Capital** ($1.5B, climate/sustainable infrastructure), **Peregrine Energy** ($700M, distributed energy), **Silicon Ranch** ($600M, utility-scale solar).
  - Battery/grid plays (Northvolt, Verkor, Redwood, Ascend Elements) — relevant to grid/storage, less to direct data-center supply.
- **`data/sector_annual.csv`** — the **Climate** line ($14 → 13.9 → **24** → 20). The 2024 jump is *partly* because Crunchbase widened scope to "all stages incl. project finance" — and big energy **project-finance** deals (Northvolt $5B, H2 Green Steel $4.6B) are exactly that. **That scope-shift is itself a clue** for Q3: energy capital increasingly arrived as project finance, not equity VC.
- **AI deals** (`sector = AI`) — scan for data-center / compute-infra plays. Our AI deals skew to foundation models, so this will likely be thin — which is itself a finding (the data-center-infra layer, like Aligned, isn't well captured in our current AI cut).

**What the repo can answer:** directional evidence on nuclear/energy-infra deals and the project-finance shift.
**What it can't:** it has no dedicated "energy" or "data-center" category, the Climate line is scope-shifty, and 2025 energy detail is thin. So Part B is required.

---

## Part B — New data to gather

Build one small, well-scoped dataset: **`data/raw/energy_ai_2024_2025.csv`**, focused on 2024 vs 2025, splitting capital by **type** (this split *is* the answer to Q3):

| Column | Meaning |
|---|---|
| `company` | recipient |
| `year`, `quarter` | timing |
| `amount_usd_m` | deal size |
| `capital_type` | **`VC equity` / `project finance` / `corporate PPA-or-strategic` / `public-market`** ← the key field |
| `energy_subsector` | nuclear/SMR · fusion · geothermal · grid/transmission · storage · gas/turbines · solar · power software |
| `data_center_link` | explicit (named DC/hyperscaler customer) vs. general |
| `recipient_type` | **startup vs. established company** ← the Q3 discriminator |
| `source_name`, `source_url`, `note` | citation, per our no-hallucination rule |

Things to specifically collect:
- **Energy-startup VC rounds** 2024–2025: SMR developers (X-energy, Kairos, Oklo, Terra Power), fusion (Commonwealth Fusion, Pacific Fusion, Helion), geothermal (Fervo), grid/power software, behind-the-meter & storage (Base Power, Crusoe's energy arm).
- **Data-center-infra companies** and their energy angle: Aligned, CoreWeave, Crusoe, Switch, Vantage — how much they raised and how they source power.
- **Hyperscaler power deals** (the incumbent channel): Microsoft–Constellation (Three Mile Island restart), Amazon–Talen / Amazon–X-energy, Google–Kairos, Meta nuclear RFP. These are mostly *PPAs / strategic*, not VC — and that's the point.
- **The driver variable:** US/global **data-center electricity demand** (TWh, % of grid) 2023→2025 and projections — from IEA, Lawrence Berkeley National Lab, or EPRI. This is the "why" behind any funding move.

---

## Source strategy (same discipline as the rest of the repo)
- **One source per series.** For VC funding totals, stay on **Crunchbase** (consistent with our backbone). For data-center *demand*, use **IEA / LBNL / EPRI** (and keep that separate from funding — it's context, not a funding number).
- **Keep capital types separate.** VC equity ≠ project finance ≠ PPA ≠ public markets. Mixing them is the same trap as our Climate scope-shift — and here it would *manufacture* a false "energy VC boom" when much of the money is actually project finance/PPAs. The `capital_type` column exists precisely to prevent this.
- **No hallucinated numbers.** Every figure gets a source link or is marked `estimated`. Hyperscaler PPA "values" are often unstated — record "undisclosed" rather than guessing.

---

## Which AI to use for what
- **Perplexity (or another web-grounded model)** → the sourced-research engine. Use it to pull cited energy-VC rounds, data-center demand figures, and hyperscaler deals. Make it cite every number with a link (same rules block as `Plan.md`). This is *not* a job for a non-grounded chat model — fabrication risk is high on niche energy deals.
- **CB Insights** (the report you found) **/ Crunchbase** → the AI-funding concentration baseline and any energy/cleantech sector cuts. CB Insights is strong on the "X% to N companies" concentration framing you're already using.
- **Claude Code (here)** → structuring the data into `data/raw/energy_ai_2024_2025.csv`, computing the 2024→2025 deltas and the startup-vs-established split, catching source-drift, building a chart/annotation, and pressure-testing the causal story (correlation ≠ causation).
- **Division of labor:** Perplexity/CB Insights *find & cite*; Claude *structures, computes, and reasons*. You *judge* — if you can't defend a claim out loud, cut it.

---

## How to answer each question
- **Q1 (did energy VC rise?)** — sum `capital_type = VC equity` energy rounds for 2024 vs 2025; report $ and deal count. Compare to the Climate-sector baseline already in the repo.
- **Q2 (correlation with AI?)** — place AI funding ($114B→$211B) next to energy-for-DC funding on the same timeline. **Be honest: 2 years (or 4 annual points) cannot establish statistical correlation** — frame it as *directional co-movement*, and name the causal chain explicitly (AI capex → data centers → power demand → energy investment) while acknowledging other drivers (electrification, grid modernization, reshoring).
- **Q3 (discrepancy)** — pivot the new dataset by `capital_type` and `recipient_type`. The headline metric: **what % of energy-for-AI capital went to startups via VC vs. to established players via PPA/project finance?** That table is the core deliverable.
- **Q4 (2024→2025 shift)** — YoY deltas on each capital type and subsector; call out what changed (e.g., did SMR/nuclear VC accelerate? did PPAs scale faster than VC?).

## Analytical cautions (read before claiming anything)
1. **Correlation ≠ causation, and n is tiny.** AI is *a* driver of energy investment, not the only one. Don't say "AI caused the energy boom"; say "energy investment rose alongside AI, concentrated in data-center-adjacent power, via these channels."
2. **Capital-type apples-to-oranges** (see source strategy) — the single biggest way to get this wrong.
3. **"Energy supplying data centers" is hard to isolate** — most energy startups aren't exclusively DC-focused. Use the `data_center_link` field and be explicit about what's "named DC customer" vs. "plausibly relevant."
4. **Disclosure gaps** — many PPA and project-finance values are undisclosed; the incumbent channel will look *smaller than it is* if you only count disclosed figures. Note this when interpreting Q3.

## Deliverables
1. `data/raw/energy_ai_2024_2025.csv` — the cited dataset.
2. A short analysis note (`ENERGY_AI_FINDINGS.md`) answering Q1–Q4 with the startup-vs-established table front and center.
3. Optionally, a 4th chart or annotation on the dashboard (energy-for-AI funding by capital type, 2024 vs 2025).
4. A one-line verdict on the hypothesis: confirmed / refuted / mixed — with the evidence.

## What would answer this definitively vs. what will stay inference
- **Definitive with Crunchbase Pro + IEA data:** the VC-equity energy totals and the startup-vs-established VC split.
- **Will stay inference:** the *causal* link to AI specifically, and the true size of the PPA/project-finance channel (disclosure gaps). Frame those as directional, well-reasoned arguments — not proven facts.
