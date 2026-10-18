# Phase 3 (full study) — progress

Resume rule: read `BRIEF.md`, then this file; continue with the first unchecked item.
Main agent: Opus (this session started 2026-10-17; harness-reported model **Opus 5.5**, claude-opus-5-5).
Fable reviewers: fresh subagents only (Agent tool, `model: "fable"`), never a model switch.

## Steps
- [x] Read survey notes in full (year notes, drafts, pages, LW-only, themes vocabulary, reception overview + main threads) to plan
- [x] Draft `notes/plan.md` (thesis + chapter plan: argument, core texts, what each leaves to others) — draft 1, 2026-10-17
- [x] Fable review of plan → `notes/reviews/plan.md`; revise plan (draft 2); record handling — 2026-10-17
- [ ] Chapters (each: read core texts in full → draft `study/<ch>.html` → quote check → `notes/chapter-summaries.md` → Fable review `notes/reviews/<ch>.md` → revise, record handling)
  - [x] Ch. 4 read (log `notes/reading-logs/04-categorization.md`), drafted `study/04-categorization.html` (~9,900 words; 129 quotations, 0 problems), summary written — 2026-10-17
  - [x] Ch. 4 Fable review → revise → record handling (draft 2, 2026-10-17; 142 quotations, 0 problems; handling at end of `notes/reviews/04-categorization.md`; ~3% over ceiling by crude count, flag for cross-chapter pass)
  - [x] Ch. 6 read (log `notes/reading-logs/06-discourse-norms.md`), drafted `study/06-discourse-norms.html` (~6,400 words; 81 quotations, 0 problems; URLs clean), summary written — 2026-10-17
  - [x] Ch. 6 review (requested Fable; ran on Opus, see model check below) processed 2026-10-17: all 22 checks run against sources; draft 2 written (133 quotations, 0 problems; URLs clean; ~7,750 words, ~0.7% over ceiling); handling at end of `notes/reviews/06-discourse-norms.md`; summary and reading log updated. Ch. 5 hand-offs (false negatives, trust beyond evidence, disclosed non-publication) now in Ch. 6. Thesis changed: crux is pricing; anti-extortion argument (part c) is where thesis 2 is tested; Salamon's disclosed discount vs Davis's coin room is the cleanest case.
  - [x] Ch. 2 read (log `notes/reading-logs/02-testimony.md`), drafted `study/02-testimony.html` (~6,650 words; 93 quotations, 0 problems; URLs clean), summary written — 2026-10-17
  - [x] Ch. 2 review (requested Fable; ran on Opus) processed 2026-10-17: draft 2 written (102 quotations, 0 problems; URLs clean; ~7,650 words, just under ceiling); handling at end of `notes/reviews/02-testimony.md`; summary, reading log, sources updated.
  - [x] Ch. 3 read (log `notes/reading-logs/03-two-type-taxonomy.md`), drafted `study/03-two-type-taxonomy.html` (~8,150 words; 95 quotations, 0 problems; URLs clean; drafts verified identical at b844bcd), summary written — 2026-10-17
  - [ ] Ch. 3 review: an Opus-run review exists (`notes/reviews/03-two-type-taxonomy.md`, header corrected), not yet processed. Ask the user whether to process it now or with the Fable batch.
  - [x] Ch. 1 read (log `notes/reading-logs/01-apprentice.md`), drafted `study/01-apprentice.html` (~5,100 words; 62 quotations, 0 problems; URLs clean), summary written — 2026-10-17. Ch. 3 Opus review held for the batch (user's choice by default).
  - [ ] Draft Ch. 7, 9, 10, 11, 8, Introduction, Conclusion (credits off; **no reviewers**; summaries as usual)
  - [ ] Review batch (see BRIEF.md, "Per-chapter review, run in one batch"): ask the user about Fable re-reviews of Chs. 5, 6, 2, 3; user turns credits on; launch all reviewers in parallel; verify `claude-fable-…` in each transcript; stay idle; user turns credits off
  - [ ] Process all reviews (credits off): check claims against sources, revise, record handling in each review file
- [ ] Apparatus: chronology, thematic index of posts, bibliography, index page
- [ ] Opus cross-chapter pass
- [ ] ASK USER whether to run a whole-book Fable review
- (Phase 4 verification follows)

## Session log
- 2026-10-17: Phase 3 begun. Read chronology, reception overview (Part C), both pilot chapters.
- 2026-10-17: plan draft 1 written; Fable plan reviewer launched (writes notes/reviews/plan.md). Tooling: `tools/check_study_quotes.py` (tested on both pilots: 137 + 269 quotations, 0 problems; negative test catches alterations and untagged quotes); `study/style.css`. Research begun: 31 sexology papers from Davis's /papers/ collection + Crossref search for recent literature (Lawrence 2026 and replies paywalled, logged as not read); Anthropic Constitution; MIRI corrigibility paper; pilot sources copied into `research/`. All logged in notes/sources.md (Phase 3 section).

## Conventions (Phase 3)
- URLs: run `python3 -I tools/check_study_urls.py study/*.html` (blog links vs. file stems and Date months, hidden pages, LW ids, draft links pinned to full hashes, data-src paths).
- Quotations: `<q data-src="path">`/`<blockquote data-src="path">` (attribution line as `<p class="attr">`); run `python3 -I tools/check_study_quotes.py study/*.html`.
- External sources live in `research/<slug>/text.txt`. NB `research/fb-yudkowsky-*` and `research/archive-yudkowsky-nov2018-thread` are login-wall/failed fetches from the Fable pilot: do not quote them.
- Reading logs per chapter: `notes/reading-logs/<chapter>.md`.
- 2026-10-17: Fable plan review received; §9 checks run against sources; plan draft 2 written (5 Parts, 11 chapters + forms chapter; thesis = criterion / norm of accounting / coordination argument, plus role-relative standard and self-application). Handling recorded at end of notes/reviews/plan.md. Next: draft chapters. Order chosen: Ch. 4 first (pilot material), then 5, 6, 2, 3, 1, 7, 9, 10, 11, 8, Introduction, Conclusion, apparatus.

- 2026-10-17: Ch. 4 drafted. Read for it (beyond the pre-compaction list): "Challenges…," "A Hill of Validity…," "If Clarity…," hidden pages, five drafts, "Maybe Lying Doesn't Exist," "You Are Right and I Was Wrong," "Message Length," "Contemporary," "Prescription"; LW threads for Blegg Mode, Boundaries, Unnatural Categories, Blood, Dolphins, Challenges (cited comments); Ozy 2018. New external source: Plunkett & Sundell 2013 (ANU repository). Numbers re-derived (scratchpad `ch4_numbers.py`). Checker tweak: `norm()` now drops the space a stripped tag leaves after "(" or before ")" and punctuation (opus pilot still 0 problems).

## File names (study/)
00-introduction, 01-apprentice, 02-testimony, 03-two-type-taxonomy, 04-categorization, 05-deception, 06-discourse-norms, 07-whole-dumb-story, 08-forms, 09-obedience-tests, 10-politics-race, 11-faking-deeply, 12-conclusion (.html); apparatus a-chronology, b-thematic-index, c-bibliography, d-questions; index.html. Cross-references in drafted chapters use these names.

### 2026-10-17 (later): commissioner's method notes, applied
Four rules added to BRIEF.md and plan.md: (1) name LW commenters by real name where known (corpus or account), else display name, never API username; `tools/render_lw_threads.py` now prints display names and threads were re-rendered; (2) no local paths in visible study text; (3) human-academic voice, no AI-prose habits (also added to the Fable review checklist); (4) Gitweb draft links pinned to commit hashes, after confirming each draft matches the local file at that commit.
- Applied to Ch. 4 and Ch. 5: names, paths, and commit pins done (UUT b844bcd1a8a9afd09c8bdfcf1b198d765bdcbf8e, AAL 6814824737e69b04fe0ce7333c49c8c06b033f65; all four cited drafts identical to local). Quote check: 187 quotations, 0 problems.
- [x] Style pass (rule 3) on Ch. 4: done in draft 2
- [x] Style pass (rule 3) on Ch. 5 (2026-10-17; also aligned with Ch. 4 draft 2: "Speaking Truth" quote now cited back to Ch. 4 §8)
- [x] Ch. 5: URL check (new `tools/check_study_urls.py`, negative-tested; 0 problems for Chs. 4–5); chapter-summaries entry written
- [x] Ch. 5: review (requested Fable; ran on Opus) processed 2026-10-17; draft 2 written (75 quotations, 0 problems; URLs clean; ~7,350 words, ~3% over ceiling); handling recorded; summary updated
- [x] Ch. 4: process `notes/reviews/04-categorization.md` (done 2026-10-17)
- Open question for the cross-chapter pass: affiliations stated from memory (e.g. "MIRI researcher Abram Demski") need a corpus or fetched source, or a label.

- 2026-10-17 (new session, Opus 5.5): Ch. 4 revised to draft 2 after Fable review. All 20 reviewer checks run against sources; main changes: strong claims located by text/date (the 2021 essay already holds the norm of accounting, so no retreat arc); disclosure argument against the coordination argument's exceptionlessness (Hooker; "Speaking Truth to Power"); two categories = developmental sex and social gender, the dispute classified as first-kind value-dependence; lesbians reductio corrected (psychological dimensions only); stealth reply as a norm-of-accounting failure; motive weighed both ways. New sources: Kleinberg 2002, Chalmers 2011, SEP Rule Consequentialism; Byrne 2020 and Barsalou 1983 not retrievable. "Law of exclusion" dropped as a term; Introduction should use "part (c), the coordination argument." Thesis 2's core argument now lives in Ch. 4 §8; the Conclusion should cite it.
- 2026-10-17: Ch. 6 drafted. Checker fix: `check_study_quotes.py` tag regex no longer treats a bare "<" (e.g. "X<p∗Z" in Habryka's post) as an HTML tag; Chs. 4–6 and the Opus pilot still pass. URL checker now also accepts LW post ids recorded in notes/reception.md and sources.md. "ricraz" = Richard Ngo's username; cite as Richard Ngo.

- 2026-10-17 (later, new session, Opus 5.5): Ch. 6 revised to draft 2 after Fable review. New external sources: Aaronson 2005, Mill *On Liberty* ch. 2, Mercier & Sperber 2011 (Shapin–Feingold PDF image-only, not read). Draft 1 backed up in the session scratchpad. Next: Ch. 2.

- 2026-10-17 (same session): Ch. 2 drafted. New sources: Bettcher 2014 (PubMed abstract; body via Chinese translation), IEP "Epistemic Injustice," Nisbett & Wilson 1977 (degraded scan). Drafts pinned at b844bcd verified by cmp. Chapter file names assumed for links: 01-apprentice.html, 03-two-type-taxonomy.html.

- 2026-10-17: **Model check.** Subagent transcripts show the reviews of the plan and Ch. 4 ran on Fable (claude-fable-5-1), but the reviews of Ch. 5, Ch. 6 and Ch. 2 ran on Opus (claude-opus-5-5) although `model: "fable"` was requested; the fallback was silent. Review headers corrected. User's decision: do not re-run them. **Standing procedure from now on:** after any reviewer spawn, grep the subagent jsonl (`~/.claude/projects/<project>/<session>/subagents/agent-*.jsonl`) for `"model":` and confirm `claude-fable-…` before using the review; report the verified model to the user.
- 2026-10-17: Ch. 2 revised to draft 2. URL checker fix: hidden pages in subdirectories (e.g. /ancillary/diary/53/) now resolve; all chapters 0 problems. Next: Ch. 3.

- 2026-10-17 (new session, Opus 5.5): Ch. 3 drafted. New sources: Lawrence 2005, Hsu 1994 (Davis's collection); Långström & Zucker 2005, Guillamon 2016, Frigerio 2021, Mueller 2021 ENIGMA, Dreger 2008, USTS 2015, Del Giudice 2012, Joel 2015, Alexander 2020 SSC (logged in sources.md). Davis's BDI figures checked: three exact, Nuttbrock 69% a slip (73.2%). PNAS letters captcha-walled (titles only). Note for cross-chapter pass: tailcalled's real name appears only in an unpublished draft ("Carl 'Tailcalled' Dybahl", spelling uncertain); chapters use the display name.
- 2026-10-17 (21:10): **Model check, Ch. 3 review.** Requested `model: "fable"`; the subagent transcript shows claude-opus-5-5. A one-word probe with `model: "fable"` also ran on claude-opus-5-5. Subagent history: Fable at 10:21 and 11:03 (plan, Ch. 4); every spawn since 14:21 has fallen back to Opus. Fable appears unavailable to this session; the fallback is silent. The Ch. 3 review was left running on Opus; whether to use it or wait for a Fable re-run is the user's call.
- 2026-10-17 (late): Cause of the fallback found: the user had turned usage credits off (to make Opus stop at the 5-hour cap), and Fable is credits-only; the harness silently served Opus. User reported it via /feedback. **User's decision: batch schedule.** Draft all remaining chapters with credits off and no reviewers, then run every Fable review in one credits-on window. BRIEF.md Phase 3 updated ("Per-chapter review, run in one batch"). Plan Fable re-reviews of Chs. 5, 6, 2, 3 are pending the user's decision before the batch.
