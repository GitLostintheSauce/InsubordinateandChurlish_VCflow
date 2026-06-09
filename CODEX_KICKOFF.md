# Codex Kickoff — Phase 5, t27 (Prompt Log Cleanup)

*Paste the contents of this file plus `HANDOFF.md` as Codex's first message. Read both before doing anything.*

---

## Context (1 paragraph)

This is **VCflow**, a Week-1 intern dashboard at `GitLostintheSauce/InsubordinateandChurlish_VCflow`, branch `main`, latest commit `b273294`. Phases 0–4 are complete and live; the project is now in **Phase 5 (reflection + submission)**. The full state, decisions, and gotchas live in `HANDOFF.md` — read that first. The rubric weights **prompt and tool workflow documentation at 20%**, so `PROMPTS.md` is a graded artifact, not internal notes.

## Your job this session (t27)

> Plan task: *"Clean up the annotated prompt log. Organize by phase and explain tool choice, output quality, and what changed because of the tool output."*

`PROMPTS.md` is currently 155 lines of chronological entries dated 2026-05-20 → 2026-05-27. It is **missing entries for Phase 3 and Phase 4** (which both shipped after the last entry), it is **not structurally grouped by phase**, and it has **unresolved TODOs** in the Phase-0 tool-comparison table (the Claude Desktop / ChatGPT verdict line). Your job is to fix all three without inventing facts.

## What "done" looks like

A reorganized `PROMPTS.md` that:

1. **Is grouped by phase**, not chronology. Suggested top-level structure:
   - `# Prompt Log` + intro paragraph (keep existing one — it's good)
   - `## Phase 0 — Tools, repo, workflow` (existing entries + the tool-comparison table)
   - `## Phase 1 — Source audit & data architecture` (existing entries + both documented pivots: quarterly→annual, deal-count omission)
   - `## Phase 2 — Core dashboard` (existing entries — the Codex Defense-visibility fix and UI polish)
   - `## Phase 3 — Secondary views` (**NEW — currently missing**)
   - `## Phase 4 — Polish & insight layer` (**NEW — currently missing**)
   - `## Tool judgment: when to use Codex vs. Claude Code` (existing essay — keep, optionally extend with one Phase-4 line)
   - `## Template for future entries` (existing — keep verbatim)
2. **Has accurate Phase 3 and Phase 4 entries.** Anchor them to real commits — `git log --oneline` is the source of truth. Phase 3 ended with commit `3a90def` ("Phase 3: deals leaderboard, sector comparison, megaround insights + UX overhaul"). Phase 4 ended with commit `b273294` ("Phase 4: insight cards + analyst-layer polish"). For each, in the standard entry format:
   - **Tool**, **Prompt** (paraphrase or summarize — don't fabricate a verbatim prompt you don't have), **Output usable?** (yes/partial/no + why), and **Lesson** if there's one worth recording.
   - Phase 4 specifically should mention: the analyst-layer critique that drove the changes (hero KPI swap to the concentration stat, default chart scale flipped log→linear, Biotech/Defense recolored off `--danger`/`--warn` semantic tokens, 12-card sourced insight grid added), and that `scripts/phase4_check.sh` was added as re-runnable static QA.
3. **Every entry explains, per the rubric**: *tool choice* (why this tool), *output quality* (what came back), and *what changed because of that output* (the action it caused in the repo). Audit existing entries — most already do this, a few don't.
4. **Surfaces the human-only TODOs explicitly** rather than fabricating verdicts. The Phase-0 tool-comparison table has a line for *Claude Desktop / ChatGPT* with `[TODO: your verdict — used for reasoning/design discussion? add your own take here.]`. **Do not invent the verdict.** Either leave it labeled as a flagged TODO for the human, or move it to a `## Outstanding for the human` block near the top. The grader rewards visible discipline, not papered-over gaps.
5. **Preserves the two documented pivots verbatim.** They are graded artifacts:
   - The quarterly → annual source-quality pivot
   - The deal-count / median omission pivot
   Don't reword the analytical reasoning in those sections. You may move them under their phase headers; you may not rewrite their conclusions.
6. **Is committed and pushed to `main` with a clear message.** Example: `Phase 5 (t27): reorganize prompt log by phase + add Phase 3/4 entries`. Sign-off as Codex.

## Constraints — read these before touching anything

- **Read `HANDOFF.md` first.** Its "Key decisions & rationale (do NOT undo these)" list is binding. The Phase-4 decisions (KPI swap, linear default, recolor, INSIGHTS as hand-curated array) are all deliberate trade-offs that look "fixable" if you don't know the rationale. Don't fix them.
- **Don't fabricate prompts you don't have.** For Phase 3 and Phase 4, the actual prompt history isn't all in this repo. Summarize what the work was, what tool did it, what the output was, and what changed in the repo — don't manufacture verbatim "Prompt:" strings you can't source. Honest summary is better than fake quotation.
- **Don't drop or rewrite:** the two pivot sections, the existing "Tool judgment" essay, the entry template at the end, or the intro paragraph.
- **Don't touch:** `index.html`, the `data/` files, `NARRATIVE.md`, `sources.md`, `README.md`, `scripts/`. Phase 5 t27 is `PROMPTS.md`-only. (Optionally, update `HANDOFF.md`'s "PROMPTS.md needs cleanup pass" note to reflect that t27 is done — that's the only other allowed edit.)
- **Always `git fetch` before pushing.** Another session has pushed to `main` mid-work before; pull/rebase first. The repo's working pattern is direct-to-`main` (GitHub Pages deploys from main); don't branch.
- **Verify before pushing.** Run `./scripts/phase4_check.sh` to make sure you didn't accidentally touch `index.html` (it should still pass 17/17). Skim the rendered `PROMPTS.md` for broken markdown.

## How to start

```bash
cd /Users/eleanor/InsubordinateandChurlish_VCflow   # local
# or: git clone https://github.com/GitLostintheSauce/InsubordinateandChurlish_VCflow.git

git fetch origin && git status
git log --oneline -15                # see what shipped in Phase 3 + Phase 4
cat HANDOFF.md                       # then this file, then PROMPTS.md
```

## When you're done

- Commit and push to `main` with a clear message.
- Reply with: the new top-level section list of `PROMPTS.md`, the commit SHA, and any `[TODO: …]` items still flagged for the human. That's the handoff back.

## After t27, the rest of Phase 5

If there's time and the human hasn't said otherwise, the remaining Phase 5 tasks (in order) are: **t28** retrospective + tool memo, **t29** three data-backed short-form insights, **t30** 5-minute walkthrough recording (human-only), **t31** submission index. Don't start them in this session unless asked — t27 is the scoped job.
