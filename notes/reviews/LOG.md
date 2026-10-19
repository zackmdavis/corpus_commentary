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

| Piece | Review file | Model (verified how) | Draft reviewed | Date | Processed |
|---|---|---|---|---|---|
| Plan | `plan.md` | Fable 5.1 (subagent transcript `claude-fable-5-1`) | plan draft 1 | 2026-10-17 | yes (plan draft 2) |
| Introduction | — | — | — | — | — |
| Ch. 1 | — | — | — | — | — |
| Ch. 2 | `02-testimony.md` | Opus 5.5, silent fallback from a Fable request (transcript `claude-opus-5-5`) | draft 1 | 2026-10-17 | yes (draft 2) |
| Ch. 3 | `03-two-type-taxonomy.md` | Opus 5.5, silent fallback from a Fable request (transcript `claude-opus-5-5`) | draft 1 | 2026-10-17 | **no** |
| Ch. 4 | `04-categorization.md` | Fable 5.1 (subagent transcript `claude-fable-5-1`) | draft 1 | 2026-10-17 | yes (draft 2) |
| Ch. 5 | `05-deception.md` | Opus 5.5, silent fallback from a Fable request (transcript `claude-opus-5-5`) | draft 1 | 2026-10-17 | yes (draft 2) |
| Ch. 6 | `06-discourse-norms.md` | Opus 5.5, silent fallback from a Fable request (transcript `claude-opus-5-5`) | draft 1 | 2026-10-17 | yes (draft 2) |
| Ch. 7 | — | — | — | — | — |
| Ch. 8 | — | — | — | — | — |
| Ch. 9 | — | — | — | — | — |
| Ch. 10 | — | — | — | — | — |
| Ch. 11 | — | — | — | — | — |
| Conclusion | — | — | — | — | — |

## Plan as of 2026-10-18

Usage credits left: about $32, roughly two Fable reviews at the old format. The
user is installing the Codex CLI so GPT can review. Proposed (awaiting the
user's go-ahead on the split): GPT reviews every piece above, including those
already reviewed (a reviewer from a different model family); Fable, if used,
spends the remaining credits on one chapter (probably Ch. 7), from the same
packet.
