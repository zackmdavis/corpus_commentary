# Review log

Which model reviewed what, how the model was verified, and whether the review
has been processed. Update this file whenever a review is run or processed.

Model is recorded from the run itself (subagent transcript for Claude
subagents; the Codex CLI's session output for GPT), never from the reviewer's
self-description.

File naming: reviews before 2026-10-18 are `notes/reviews/<stem>.md`; from
2026-10-18, `notes/reviews/<stem>-<reviewer>.md` (e.g. `07-whole-dumb-story-gpt.md`),
so a chapter can have reviews from more than one model. Packets the reviewers
read are built by `python3 -I tools/make_review_packet.py [stem ...]` into
`notes/review-packets/<stem>.md`; rebuild before each run so the packet
carries the current draft and summaries.

| Piece | Review file | Model (verified how) | Draft reviewed (commit) | Date | Processed |
|---|---|---|---|---|---|
| Plan | `plan.md` | Fable 5.1 (subagent transcript `claude-fable-5-1`) | plan draft 1 | 2026-10-17 | yes (plan draft 2) |
| Introduction | `00-introduction-gpt.md` | GPT `gpt-6-astra`, effort high (Codex session file; no tool calls) | draft 1 (`cfe5b33`) | 2026-10-19 | no |
| Ch. 1 | `01-apprentice-gpt.md` | GPT `gpt-6-astra`, effort high (Codex session file; no tool calls) | draft 1 (`cfe5b33`) | 2026-10-19 | yes (draft 2, 2026-10-20) |
| Ch. 2 | `02-testimony.md` | Opus 5.5, silent fallback from a Fable request (transcript `claude-opus-5-5`) | draft 1 | 2026-10-17 | yes (draft 2) |
| Ch. 2 | `02-testimony-gpt.md` | GPT `gpt-6-astra`, effort high (Codex session file; no tool calls) | draft 2 (`cfe5b33`) | 2026-10-19 | yes (draft 3, 2026-10-20) |
| Ch. 3 | `03-two-type-taxonomy.md` | Opus 5.5, silent fallback from a Fable request (transcript `claude-opus-5-5`) | draft 1 | 2026-10-17 | yes (draft 2, 2026-10-19) |
| Ch. 3 | `03-two-type-taxonomy-gpt.md` | GPT `gpt-6-astra`, effort high (Codex session file; no tool calls) | draft 1 (`cfe5b33`) | 2026-10-19 | yes (draft 2, 2026-10-19) |
| Ch. 4 | `04-categorization.md` | Fable 5.1 (subagent transcript `claude-fable-5-1`) | draft 1 | 2026-10-17 | yes (draft 2) |
| Ch. 4 | `04-categorization-gpt.md` | GPT `gpt-6-astra`, effort high (Codex session file; no tool calls) | draft 2 (`cfe5b33`) | 2026-10-19 | no |
| Ch. 5 | `05-deception.md` | Opus 5.5, silent fallback from a Fable request (transcript `claude-opus-5-5`) | draft 1 | 2026-10-17 | yes (draft 2) |
| Ch. 5 | `05-deception-gpt.md` | GPT `gpt-6-astra`, effort high (Codex session file; no tool calls) | draft 2 (`cfe5b33`) | 2026-10-19 | no |
| Ch. 6 | `06-discourse-norms.md` | Opus 5.5, silent fallback from a Fable request (transcript `claude-opus-5-5`) | draft 1 | 2026-10-17 | yes (draft 2) |
| Ch. 6 | `06-discourse-norms-gpt.md` | GPT `gpt-6-astra`, effort high (Codex session file; no tool calls) | draft 2 (`cfe5b33`) | 2026-10-19 | no |
| Ch. 7 | `07-whole-dumb-story-gpt.md` | GPT `gpt-6-astra`, effort high (Codex session file; no tool calls) | draft 1 (`cfe5b33`) | 2026-10-19 | yes (draft 2, 2026-10-19) |
| Ch. 8 | `08-forms-gpt.md` | GPT `gpt-6-astra`, effort high (Codex session file; no tool calls) | draft 1 (`cfe5b33`) | 2026-10-19 | yes (draft 2, 2026-10-20) |
| Ch. 9 | `09-obedience-tests-gpt.md` | GPT `gpt-6-astra`, effort high (Codex session file; no tool calls) | draft 1 (`cfe5b33`) | 2026-10-19 | yes (draft 2, 2026-10-19) |
| Ch. 10 | `10-politics-race-gpt.md` | GPT `gpt-6-astra`, effort high (Codex session file; no tool calls) | draft 1 (`cfe5b33`) | 2026-10-19 | yes (draft 2, 2026-10-19) |
| Ch. 11 | `11-faking-deeply-gpt.md` | GPT `gpt-6-astra`, effort high (Codex session file; no tool calls) | draft 1 (`cfe5b33`) | 2026-10-19 | yes (draft 2, 2026-10-20) |
| Conclusion | `12-conclusion-gpt.md` | GPT `gpt-6-astra`, effort high (Codex session file; no tool calls) | draft 1 (`cfe5b33`) | 2026-10-19 | no |

Drafts are archived in git (see `CLAUDE.md`, "Git in this project"). The
text each GPT review saw is the packet in commit `cfe5b33` (packets were not
changed by the 2026-10-19 runs). Draft 1 of Chs. 2, 4, 5 and 6, which their
first reviews read, predates the first commit and was not kept; the review
files quote the passages they criticize.

GPT runs: `tools/run_codex_review.sh <stem> [model] [effort]` (defaults
`gpt-6-astra`, `high`). Per-run records are in `notes/reviews/runs/`: the
Codex event log (`.jsonl`), and `.model`, which lists the thread id, the
Codex session file, the model and effort it records, the number of tool calls
(should be 0) and token usage.

## Status, 2026-10-19

GPT (`gpt-6-astra`, high) has reviewed every piece: the Introduction, Chs. 1–11
and the Conclusion. The GPT reviews of Chs. 2, 4, 5 and 6 are of draft 2
(already revised from their first reviews); the rest are of draft 1. The
13 runs used an estimated 80% of one Codex 5-hour window (49% after the first 8, per the Codex app). Next: process the reviews
(Ch. 3's two together). Undecided: whether to spend the ~$32 of usage
credits on a Fable review (recommended: Ch. 11).
