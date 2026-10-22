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
  - [x] Ch. 9 drafted 2026-10-17 (session 32892a11, which hit the cap right after writing it); bookkeeping finished 2026-10-18: reading log rebuilt from transcript, sources logged, summary written, one from-memory label added. 100 quotations, 0 problems; URLs clean; ~6,850 body words (~14% over ceiling). **Gitweb pins for its 5 drafts not yet confirmed** (Gitweb slow from scraper load); retry before Phase 4.
  - [x] Ch. 7 drafted 2026-10-18: reading log `notes/reading-logs/07-whole-dumb-story.md`; sources logged (Wayback Nov 2018 thread, Gould, A Rational Argument, SSC 2019); summary written; fact-check pass against sources done (comment ids, dates, attributions). 158 quotations, 0 problems; URLs clean; ~9,300 words (within ceiling). **Gitweb pins for its 4 UUT drafts not yet confirmed** (Gitweb unreachable 18 Oct); retry before Phase 4.
  - [x] Ch. 10 drafted 2026-10-18: reading log `notes/reading-logs/10-politics-race.md`; sources logged (Bird 2021, Turkheimer/Harden/Nisbett 2017, Warne review, Cudd NDPR, Alexander 2021 statement; Nisbett 2012/Cofnas/Winegard re-read). 68 quotations, 0 problems; URLs clean; ~5,730 words (within ceiling). **Gitweb pins for its 4 UUT drafts not yet confirmed.**
  - [x] Ch. 11 drafted 2026-10-18: reading log `notes/reading-logs/11-faking-deeply.md`; sources logged (Christiano 2017, AGI Ruin, Belrose & Pope; Soares 2015 and Constitution re-read). 55 quotations, 0 problems; URLs clean; ~5,030 words. Positionality procedure (plan §4) applied in §5. **Gitweb pin for 1 AAL draft not yet confirmed.** Conclusion file to be `study/12-conclusion.html` (nav links already point there).
  - [x] Ch. 8 drafted 2026-10-18: reading log `notes/reading-logs/08-forms.md`; no new external sources (Galileo from memory, labeled). 28 quotations, 0 problems; URLs clean; ~3,530 words. **Gitweb pins for 5 UUT drafts not yet confirmed.**
  - [x] Introduction drafted 2026-10-18 (`study/00-introduction.html`, ~3,450 words; 12 quotations clean). Academic-citation search run and logged: one citation found (Bailey 2019, Arch Sex Behav, references "Reply to Ozymandias on Autogynephilia"); reception.md Part C corrected. Archive attempts for Oct 2024 Yudkowsky tweets logged (none archived).
  - [x] Conclusion drafted 2026-10-18 (`study/12-conclusion.html`, ~2,150 words; 2 quotations clean).
  - [x] `study/index.html` contents page written (apparatus still to come).
  - [x] Whole study checks 2026-10-18: 1,032 quotations, 0 problems; URL check 0 problems; all internal anchors resolve.
  - [ ] **Next: review batch.** Tell the user drafts are done; ask whether Chs. 5, 6, 2, 3 should also get Fable reviews in the batch. Chapters needing first reviews: Introduction, 1, 7, 8, 9, 10, 11, Conclusion (Ch. 4 and plan already Fable-reviewed).
  - [ ] Gitweb pin confirmation for all cited drafts (Chs. 7–11, Intro) still pending (Gitweb unreachable 18 Oct); retry before Phase 4.
  - [ ] Cross-chapter pass (Opus) and apparatus (chronology, thematic index, bibliography, questions appendix) after reviews are processed. Flags: Ch. 9 ~14% over ceiling; Ch. 4 over; Ch. 7 near ceiling; Intro and Conclusion under target; Davis "30%"/"20%" misquote for Questions appendix. **Notes (user-approved 2026-10-18; see BRIEF "Attribution of reviewers' contributions"):** citations stay parenthetical; give every chapter a closing unnumbered "Note on method" (Chs. 2, 4, 5, 6 have one) including which models reviewed it; reviewer credits as numbered `sup.fn` notes. Move to numbered notes: "from memory" labels (~14), single-source access remarks (archive/paywall/login/not read, ~25; chapter-wide ones go in the Note on method), how commenters' real names were established, details of source checks (e.g. the 30%/20% misquote; the finding stays in the text if it matters), side debates in the literature (e.g. Ch. 10 genetics). Keep "as Davis quotes" inline where it qualifies the claim. **Fix:** Ch. 4's Note on method says Yudkowsky's Nov 2018 tweets rest on Davis's report alone; Ch. 7 found and checked Wayback copies.
  - [ ] Review batch (see BRIEF.md, "Per-chapter review, run in one batch"): ask the user about Fable re-reviews of Chs. 5, 6, 2, 3; user turns credits on; launch all reviewers in parallel; verify `claude-fable-…` in each transcript; stay idle; user turns credits off
  - [ ] Process all reviews (credits off): check claims against sources, revise, record handling in each review file
- [x] Apparatus: chronology, thematic index of posts, bibliography, index page (2026-10-20)
- [x] Opus cross-chapter pass (2026-10-20)
- [x] Opus length pass (2026-10-20; `notes/cuts-v1.md`)
- [x] Whole-book review by GPT via Codex (run 2026-10-20; `notes/reviews/whole-book-gpt.md`, 5,550 words; processed 2026-10-22, handling in the review file)
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
- 2026-10-18: **Reviewer change.** About $32 of usage credits left (roughly two Fable reviews at the old format: the plan and Ch. 4 Fable reviews used ~110–120k cache-write, 380–660k cache-read and 12–19k output tokens each). User is installing the Codex CLI to bring in GPT as reviewer. Built `tools/make_review_packet.py` → `notes/review-packets/<stem>.md` for all 13 pieces (instructions, BRIEF, plan, summaries, chapter as plain text; ~26–35k words each). Review/model tracking: `notes/reviews/LOG.md`. BRIEF amended ("Change, 2026-10-18"). Next: once Codex is installed, check `codex exec --help`, run one review as a test, confirm the model from Codex's output, then the rest.
- 2026-10-19: **Ch. 3 draft 2** after the Opus review (draft 1, unprocessed since 10-17) and the GPT review, processed together; handling recorded in both review files; 113 quotations, 0 problems; URLs clean; 16 notes (first use of the notes convention) + Note on method. ~9,600 words body (draft 1 ~7,700): longest chapter; book total ~85k; flag for cross-chapter pass. Open from the reviews: Alexander's response (if any) to the Dec 2023 reply not searched; Veale 2014 AGP frequency not checked; from-memory scholarship not fetched (listed in handling). Next: process the remaining GPT reviews (Chs. 7, 9, 10, 11, 1, 8 first; Intro after the commissioner decision; Conclusion last; Chs. 2, 4, 5, 6 second-round reviews of draft 2).


## Decision, 2026-10-20: naming the commissioner

The final published front matter will say who commissioned the study. Until
then the Introduction describes the commission (scope and method, per the
brief) without naming anyone, and drafting sessions should not bring the
question up again. Add the name when the front matter is assembled for v1.
This note is kept out of the review packets on purpose.

## Current state, 2026-10-22 (resume here; supersedes the sections below)

**Whole-book review processed** (Opus 5.5). Handling at the end of `notes/reviews/whole-book-gpt.md`; LOG.md updated. New drafts: Introduction 5; Chs. 3, 4, 7, 11 draft 6; Ch. 10 draft 5; Conclusion 4 (each with a "Draft N changes (whole-book…)" block in `notes/chapter-summaries.md`); corrections without new drafts in Chs. 2, 5, 6, 8, 9 and `d-questions.html`. Main substantive changes: the 2018-thread verdict narrowed (Ch. 7 §2); the coordination-argument finding restated as a burden unmet (Intro §3, Ch. 4 §8, Conclusion §2); Ch. 11 no longer says the Constitution "meets the minimum", and asks the advertising question of the label "corrigible"; alignment-faking report read in part and used in Ch. 11 n2. New source: `research/alignment-faking-2024/`. Checks: 1,091 quotations, 0 problems; URLs 0; anchors resolve; no visible local paths; apparatus rebuilt. Length 95.6k → 97.6k.

**Open.**
1. ~~The review's cut table~~ **Done 2026-10-22** (drafting model's judgment, at the user's request): Conclusion rewritten as synthesis, recap paragraphs cut in chapter conclusions, a few redundant passages; 97,563 → 95,157. The rest of the table was judged to cost argument; record in `notes/cuts-v1.md` § "Second length pass". See the review's §7 and `notes/cuts-v1.md` § "Considered and not cut".
2. Not adopted this round, candidates for later: inductive risk (needs Rudner/Douglas read), a full prose pass on the "corrective rhythm".
3. Items 1–3 and 5 of the late-evening list below still stand (commissioner's name at v1 freeze; citation styles; draft header dates; then Phase 4).

## Current state, 2026-10-20, night (superseded above)

**Length pass done** (session c653f79f, Opus 5.5). All 13 pieces read in full; 43 cuts in the Introduction and Chs. 1–11 (Conclusion unchanged), each listed with section, size and what the reader loses in `notes/cuts-v1.md`, **which the user will read and may ask for passages back from** (restore from commit 38fc8f4). Changed chapters bumped one draft (Intro 4, Ch. 1 3, Ch. 2 4, Ch. 3 5, Ch. 4 5, Ch. 5 4, Ch. 6 4, Ch. 7 5, Ch. 8 3, Ch. 9 5, Ch. 10 4, Ch. 11 5), each with a "Draft N changes (length pass…)" block in `notes/chapter-summaries.md`. Knock-on fixes: orphaned works-cited entries removed; Notes on method edited only where they named cut material; chronology's 2013 link → Ch. 9 §1. Apparatus rebuilt (215 works by Davis; 94 other; 41 reception). Checks: 1,081 quotations, 0 problems; URLs 0 problems; internal anchors 0 problems; no local paths in visible text.

**Length: 98,143 → 95,687 (−2,456)**, by html_to_text + wc -w on body + notes + Notes on method, works cited stripped (this measure gives 98.1k for the pre-pass state, not the 97.9k recorded below). Short of the 8–10k target. The drafting model judged most remaining material (argument steps, concessions, adopted review objections, from-memory/caveat notes, Notes on method) not worth cutting; these were its own limits, not the user's (an earlier wording here said "the user's exclusions", which was wrong; corrected 2026-10-22); `notes/cuts-v1.md` § "Considered and not cut" lists ~3,300 words of further candidates with what each would cost, and says that reaching 88–90k would take structural cuts in Ch. 4 §8, Ch. 6 §6, Ch. 10 §6 and Ch. 2 §6.

**Next (resume here, fresh session, after the Thursday quota reset):** process `notes/reviews/whole-book-gpt.md` (GPT-6-Astra, run 2026-10-20 on commit 63407d5; logged in LOG.md as unprocessed). Check each claim against the sources before acting; give special care to its §4 point that Anthropic receives "an especially consequential benefit of interpretation" (positionality rule) and its §2 challenge to Ch. 7's verdict on the 2018 thread; write a handling section in the review file; revise, bump drafts, update summaries, rerun build_apparatus and all checks; mark processed in LOG.md. The user has accepted the cuts in `cuts-v1.md`.

**Open.**
1. ~~User to read `notes/cuts-v1.md`~~ (accepted 2026-10-20): restore any passages, and decide whether to cut further from the "Considered and not cut" list.
2. **Whole-book review: GPT via Codex** (the user's decision; the brief now says so). Packet: `python3 -I tools/make_review_packet.py whole-book` → `notes/review-packets/whole-book.md` (built 2026-10-20: ~111k words, ~694 KB, ~178k tokens at the earlier runs' worst ratio, ~194k with Codex overhead, against a 258,400-token window; instructions, brief, plan, front matter, all 13 pieces without their works cited, chronology and questions appendix; chapter summaries, cuts-v1.md, thematic index and bibliography left out at the user's request or as redundant). Rebuild just before the run, after the user has settled `cuts-v1.md`; run with `tools/run_codex_review.sh whole-book` (cuts accepted by the user; context checked). Record the model from Codex's output; save the reply as `notes/reviews/whole-book-gpt.md`; update LOG.md.
3. Items 1–3 and 5 of the late-evening list below still stand (commissioner's name; citation styles; draft header dates; then Phase 4). Item 4 is superseded by 2.

## Current state, 2026-10-20, late evening (superseded above)

**Cross-chapter pass done** (session 35e531f0, Opus 5.5; commit 6129f74). All 13 pieces read in full. Cuts of repetition and lower-value detail in Chs. 3, 4, 7, 9, 11 (now draft 4; "Draft 4 changes" blocks in `notes/chapter-summaries.md`) and small fixes elsewhere: unfulfilled forward references removed (Ch. 4 → Ch. 7 "traces"; Ch. 7 → Ch. 9 "notes"); Ch. 8 and the Conclusion no longer attribute to Ch. 4 a finding that the stealth reply "cost him credibility"; Ch. 8 now quotes "I might be a woman" from "October Eleventh" (it had said a 2015 reader had only "the dragon"); Ch. 1 points to Ch. 4 on the two definitions sentences; Ch. 5 points to Ch. 11 (#claude) for the Constitution's non-deception clause; "TracingWoodgrains" (site display name) throughout; reviewer lines no longer mention the Fable→Opus fallback; plan's Empirical Claim date and Ch. 6 summary's Lady Justice line fixed. Flags from earlier notes checked: "norm of accounting" frequency is unremarkable (Ch. 7: 4); "Chapter N found" density in the Conclusion left as is; affiliations (Demski "MIRI researcher", Soares "executive director") are documented in the corpus.

**Length** (body + notes + notes on method, excluding works cited; `html_to_text` + `wc -w`): 100.1k before the pass, **97.9k after**. Under the 100k ceiling, still well over the 80k target. Largest: Ch. 4 11.0k, Ch. 7 10.8k, Ch. 3 10.4k. Further cuts are possible (candidates: Ch. 4 §8 "Two categories"; Ch. 7 §7; Ch. 6 §6; Ch. 10 §6; Ch. 2 §6–7) if the user wants more margin.

**Apparatus done.** `study/a-chronology.html` (hand-written from facts the chapters state, linked to chapter sections); `study/b-thematic-index.html` and `study/c-bibliography.html` generated by `python3 -I tools/build_apparatus.py` from the chapters' own links and data-src paths (233 works by Davis; 95 other works; 41 reception entries) — **rerun it after any chapter change**; `study/d-questions.html` (14 questions, including the 30%/20% figure); front matter and apparatus links in `study/index.html` (byline "Claude (Opus 5.5)", contributions statement). Checks: 1,116 quotations, 0 problems; URLs 0 problems; internal anchors 0 problems; no local paths in visible text.

**Open.**
1. Commissioner's name: an HTML comment in `study/index.html` marks where it goes at the v1 freeze. When it is added, the Introduction §6 ("at the commission of a reader who set its scope and method") must be reconciled with it.
2. Bibliography Parts II–III inherit the chapters' mixed citation styles (author-date in Chs. 7, 9–11, Introduction; humanities style elsewhere). Normalizing would mean editing each chapter's works-cited list; candidate for Phase 4.
3. Draft header dates are omitted from the bibliography because many are placeholders (1 Jan 2020/2021/2027).
4. ASK USER whether to run a whole-book review (Fable credits ~$7.42 left; a GPT run via Codex is the other option).
5. Then Phase 4 verification (scripted quote check, link check, re-run until clean), then freeze v1.

## Current state, 2026-10-20, evening (superseded above)

**Fable batch done and processed.** Seven Fable 5.1 reviews ran with credits on (Introduction, Conclusion, Chs. 3, 7, 9, 10, 11; ~$24.6, credits now $7.42 and off). All processed: those seven pieces are now draft 3 (commits 1a5ab2e, 4cd0243, a36261d, 1e64d6c, c5f79eb, f11311c, 56df8cf); consistency corrections without new drafts in Chs. 6, 7, 8. Handling sections are in each `notes/reviews/*-fable.md`; LOG.md is current. Whole-study checks: 1,138 quotations, 0 problems; URLs clean; internal anchors clean.

**Length.** Now ~97.8k body words, ~106k with notes and Notes on method: over the 100k ceiling. The cross-chapter pass must cut roughly 10–20k (candidates: Ch. 4, Ch. 3, Ch. 7, Ch. 9; Ch. 3 §7 univariate paragraph; Ch. 7 §4 Vassar quotations and §5 cost catalogue; Ch. 9 §1 biography, Stockholm paragraph, protest episode; Ch. 11 §6 LLM paragraph).

**Next.** Item 3 below (cross-chapter pass, then apparatus). Flags carried into it: Ch. 5/Ch. 11 duplicate quotation of the Constitution's "Non-deceptive" clause (Ch. 11 should own it); "norm of accounting" frequency in Ch. 7; "Chapter N found" density in the Conclusion; TracingWoodgrains vs Tracing Woodgrains spelling; Ch. 6 summary "Leaves" line still mentions Lady Justice for Ch. 11 (now removed in both); the plan's Ch. 3 entry dates the "Empirical Claim" to 2023 (it is 2 Jan 2024). The questions appendix should include the 30%/20% misquote.

## Current state, 2026-10-20 (morning; superseded above)

Supersedes the unchecked checklist items above where they conflict.

**Done.** GPT-6-Astra reviews (via Codex; see `notes/reviews/LOG.md`) are
processed for Chs. 1–11; each chapter has a new draft, a handling section in
its review file, a "Draft N changes" block in `notes/chapter-summaries.md`,
and a commit. Every chapter has a closing Note on method with a reviewer line.
Ch. 4's Nov 2018 tweet provenance has been fixed. The quote check (1,080
quotations) and URL check are clean for `study/*.html`.

**Next.**
1. ~~Process `notes/reviews/00-introduction-gpt.md`~~ **Done 2026-10-20**
   (draft 2; handling in the review file; reading log
   `notes/reading-logs/00-introduction.md`; 16 quotations clean; URLs and
   anchors clean). Found and fixed: hormone/psychosis chronology; Heads I Win
   date (23 Sep); 2026 retrospective overstated as "declined openly". For the
   cross-chapter pass: "TracingWoodgrains" (Ch. 2) vs "Tracing Woodgrains"
   (Intro); the Conclusion should assess, not re-quote, the "guess at the
   truth" sentence the Introduction closes on.
2. ~~Process `notes/reviews/12-conclusion-gpt.md`~~ **Done 2026-10-20**
   (draft 2, rewritten against each chapter's current conclusion; handling in
   the review file). Knock-on: Ch. 7's conclusion sentence on concessions
   corrected (no new draft). Whole study: 1,085 quotations, 0 problems; URLs
   and internal anchors clean. **All 13 GPT reviews now processed.**
   Cross-chapter flags found while doing it: Ch. 8 conclusion's "two years
   later" (actual: Jan 2026 review of the Jun 2024 third dialogue, ~19
   months); "TracingWoodgrains" (Ch. 2) vs "Tracing Woodgrains" (Intro).
3. Cross-chapter pass, then apparatus (chronology, thematic index,
   bibliography, questions appendix incl. the 30%/20% misquote, front matter
   with the contributions statement and byline "Claude (Opus 5.5)").
4. ~~Confirm Gitweb pins~~ **Done 2026-10-20**: 29 links, 27 identical; Pretraining Famous re-pinned to 68ea8bc; SF State in Twilight differs by a later TODO block (stated in Ch. 11's Note on method). See sources.md, "Gitweb pin confirmation".

**Cross-chapter theme from the GPT reviews.** In Chs. 4–6 disclosure now
works only conditionally: it turns distortion into missing information only
when it tells listeners the direction and size of the selection and reaches
them. The coordination argument (part (c)) still fails, with that
qualification. The Introduction and Conclusion must state it the same way.

**Length** (crude count incl. notes): ~94k total. Ch. 3 10.5k, Ch. 4 11.3k,
Ch. 7 10.4k, Ch. 6 8.8k, Ch. 2 8.5k, Ch. 5 8.4k. Over the 80k target, under
the 100k ceiling; trim in the cross-chapter pass.

**Fable credits (~$32).** The user wants to spend them but hasn't chosen a
chapter. Wait for the user to say which.
