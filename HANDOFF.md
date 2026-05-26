# Session Handoff

**Date:** 2026-05-26
**Topic:** Custom Claude Code status line

## Status: Complete & verified

Configured a multi-line status line that displays context window usage, per-call
token breakdown, and Claude.ai subscription quota gauges.

## Files changed

- `~/.claude/settings.json` — added `statusLine.command` pointing to the script
  below. All other keys were preserved.
- `~/.claude/statusline-command.sh` — the status line script (created this session).

## What it renders (up to 4 lines)

```
~/projects/vcflow  Opus 4.7
Context:  in:15500       out:1200      used:8% / 200000 ctx  rem:92%
Last call:  in:8500        out:1200      cache-write:5000      cache-read:2000
Quotas:  5h quota: 24% used (resets 12:00)   7d quota: 41% used (resets 12:00)
```

1. Directory (`~`-abbreviated) + git branch (when present) + model name
2. **Context** — current input/output tokens in context, % used, window size, % remaining
3. **Last call** — most recent API call: input, output, cache-write, cache-read tokens
4. **Quotas** — 5-hour and 7-day rate-limit usage with reset times

## Things the next session should know

- **Lines 2–4 only appear after the first API call.** They're suppressed when the
  underlying data is null (e.g. right after `/compact`, until the next call).
- **Line 4 (Quotas) only shows for Claude.ai Pro/Max subscribers.** The `rate_limits`
  object isn't sent on API-key / console billing — its absence is expected, not a bug.
- All fields read by the script match the official schema at
  https://code.claude.com/docs/en/statusline (verified this session):
  `context_window.*`, `context_window.current_usage.*`,
  `rate_limits.five_hour|seven_day.{used_percentage,resets_at}`.
- `context_window.total_input_tokens/total_output_tokens` are **current context**
  (not cumulative) as of Claude Code v2.1.132.
- One bug was fixed: home dir was rendering as `\~`; changed the bash substitution
  replacement from `\~` to `~`.

## How to test the script manually

```bash
echo '{"model":{"display_name":"Opus 4.7"},"workspace":{"current_dir":"/Users/eleanor/projects/vcflow"},"context_window":{"total_input_tokens":15500,"total_output_tokens":1200,"context_window_size":200000,"used_percentage":8.4,"remaining_percentage":91.6,"current_usage":{"input_tokens":8500,"output_tokens":1200,"cache_creation_input_tokens":5000,"cache_read_input_tokens":2000}},"rate_limits":{"five_hour":{"used_percentage":23.5,"resets_at":1748275200},"seven_day":{"used_percentage":41.2,"resets_at":1748707200}}}' | bash ~/.claude/statusline-command.sh
```

## How to make further changes

Route formatting/field/color changes through the `statusline-setup` agent — just ask
Claude to adjust the status line.
