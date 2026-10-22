# Brief: a scholarly study of Zack M. Davis's blogging corpus

This file is the standing commission for every Claude session working in this
directory, whichever model is running. Read it in full before doing anything
else. It records scope and method decisions already made; it deliberately
contains no interpretive hypotheses. What the corpus means is for
the study to work out from the texts.

## The commission

Write a book-length scholarly study of the corpus in this directory, in the
manner of serious secondary literature on a major author (the way scholars
write on Kant or Shakespeare): interpretation, intellectual context, and
critical assessment, grounded in close reading and documented with citations.

This brief deliberately does not specify what the study should argue, which
texts matter most, or what verdict it should reach. The conclusions are the
study's own.

- **Audience.** An intelligent reader who has not read the blogs. Do not
  address the author.
- **Interpretation and critique together.** Reconstruct arguments fairly, then
  evaluate them. Where an argument fails, say so and show why. Where empirical
  claims are contested (notably the sexology), research the actual literature,
  including the critics, rather than relying on the corpus's account of it, and
  say where you land and why. Neither flattery nor contrarianism; no reflexive
  hedging.
- **Length.** Target roughly 80,000 words (a standard scholarly monograph),
  with ~100,000 as a ceiling. Length must be earned: every chapter makes an
  argument; no summary for its own sake.
- **Form.** A monograph with an argued thesis, organized thematically (not a
  post-by-post commentary), plus apparatus: a chronology, a thematic index of
  posts, and a bibliography. Chapter plan is the study's to decide after the
  survey.
- **Output.** Local HTML in `study/` (one file per chapter plus an index page
  is fine). Do not publish Artifacts or Claude Docs. Citations link to the live
  posts.

## The corpus

- `AAL_content/` — *An Algorithmic Lucidity*, 2011–2026, ~497 posts, ~250k
  words. Live URL: `https://zackmdavis.net/blog/YYYY/Mon/<file-stem>/`
- `UUT_content/` — *The Scintillating But Ultimately Untrue Thought*,
  2016–2025, ~173 posts, ~255k words. Live URL:
  `http://unremediatedgender.space/YYYY/Mon/<file-stem>/`
- `*/drafts/` — ~91k words of unpublished drafts. **In scope.** They are
  publicly visible via the blogs' Gitweb source repositories (linked in each
  site's footer), so a human scholar would have them too. Cite them as
  unpublished drafts, distinctly from published posts, by repository path
  (`content/drafts/<file>`) with a Gitweb link pinned to a specific commit
  hash (`hb=<sha>`, never `hb=HEAD`, which moves). Before pinning, fetch the
  draft at that commit (`a=blob_plain`) and confirm it matches the local file.
- `UUT_content/pages/` — the About page and `ancillary/` pages (several marked
  `Status: Hidden`: diary entries, captions, etc.). In scope; cite as such.
- **LessWrong-only posts.** Davis has ~116 posts on LessWrong (user
  `zack_m_davis`, 2009–2026). Most are cross-posts of blog posts, but ~30
  appear to exist only there. These are published work and in scope. Phase 1
  fetches them into `LW_content/` (Markdown, same headers plus the LessWrong
  URL) so they can be cited and quote-checked like everything else; dedupe
  against the blogs by content, not just title. Davis's ~1,700 LessWrong
  comments are not surveyed in full; read them where they bear on a post or
  thread under discussion.
- Posts are Pelican Markdown with `Title`, `Date`, `Category`, `Tags`, and
  sometimes `Status` headers. Images are in `*/images/`; look at them where a
  post's argument depends on a figure.
- **Never modify anything in `AAL_content/` or `UUT_content/`** (or
  `LW_content/` once fetched). Quote verification checks against these files,
  so they must stay exactly as they are.

URL pattern was spot-checked on three posts; verify any URL you're unsure of.

## Method

### Read what you cite
Every post quoted or characterized in the study must have been read in full
by the session writing that passage. Survey notes are for finding things, not
a substitute for reading them.

### Citation discipline
Fabricated or misremembered citations would discredit the whole study.
- **Corpus citations:** title, date, blog, and live URL (for drafts, the
  commit-pinned Gitweb link; hidden pages have live URLs under `/ancillary/`).
  Quotations are exact in their words, spelling and punctuation. Quotation
  marks and apostrophes follow standard American typography (changed
  2026-10-22): curly rather than straight, and a source's double quotation
  marks become single ones when the passage is itself quoted inline, with the
  source's single marks becoming double in turn. Block quotations keep the
  source's levels. The study states this convention once, in its front matter.
- **No local paths in the study's visible text.** `AAL_content/`,
  `UUT_content/`, `LW_content/`, `notes/`, `research/`, `reception_data/`,
  `tools/` exist only in this working directory, not online. They may appear
  only in invisible markup (the `data-src` attributes the quote checker reads).
- **Naming commenters.** Use the person's real name where it is known:
  documented in the corpus (e.g. Davis names Jessica Taylor, Raymond Arnold,
  Oliver Habryka), given by the account itself, or vouched for by the
  commissioner (record such identifications in `notes/sources.md`). Otherwise use the display
  name the website shows. Never cite the GraphQL API's `username` field
  as such: it is an immutable key that often differs from the display name
  (e.g. username `Yvain`, display name Scott Alexander).
- **External sources** (LessWrong threads, replies from interlocutors,
  Yudkowsky's Sequences, sexology papers, etc.): cite only what you actually
  fetched and read in this project, and record it in `notes/sources.md` with
  the URL and access date.
- **Anything from memory** (background knowledge not verified in-project) is
  labeled as such in the text or a note.
- A quote-verification pass (scripted, checking every quotation against the
  source files) runs before anything is called finished.

### Reception
Secondary literature positions itself within the existing conversation about
an author, and so should this study. Search for responses to Davis's work:
critiques, rebuttals, discussions, comment threads on cross-posts, and the
public writing of people the corpus argues with or writes about. Where the
corpus narrates a dispute, look for the other parties' public accounts of it
before characterizing it. Engage the strongest criticisms on their merits, and
describe the reception accurately, whether hostile, sympathetic, or absent.
Hostility is not an argument, and neither is approval. Cite only public
writing; don't dig into private individuals.

The largest body of reception is the ~3,600 comments on Davis's LessWrong
posts. The LessWrong GraphQL API (`https://www.lesswrong.com/graphql`) works
without login, and GreaterWrong renders threads as plain HTML. X/Twitter is
login-walled: state that as a limitation of the study rather than guessing at
what's there.

### Positionality
The study is written by Claude, and the corpus includes criticism of Claude
and Anthropic (e.g., the 2026 posts on corrigibility in Claude's
constitution) and extensive writing on AI alignment. Disclose this in the
introduction and treat those posts explicitly, with no softer or harsher
standard than anything else. Claude's training data may also include parts of
this corpus and its reception; rely on the files and fetched sources, not on
recalled impressions of the author or the discourse.

### The author's writing
Commentary is the study's, not the author's. Write it as a good human
academic would: plain, exact scholarly prose. That Claude wrote the study is
disclosed in the introduction (see Positionality), not performed in the prose.
Avoid the stock habits of AI-generated text: strings of short verdict
sentences ("That is the problem handled well."), reflexive "not X but Y"
constructions and triads, announcing what a section will argue or has just
argued, stacked "First … Second … Third" scaffolding where ordinary paragraphs
would do, intensifiers ("crucially," "notably"), and references to the
project's own machinery ("the session that wrote it," "Phase 1," "by
script"). Quotations are quotations. Do not rewrite
the author's passages ("this would be better put as…"), and do not reconstruct
how an unfinished draft "would have" gone in the author's voice; discussing
what a draft is reaching for, as ideas, is fine.

### The texts as authority
Interpretation rests on what the texts say. Questions the study would put to
the author, if any, can be collected in an appendix.

### Publication standard
The study may be published online and plausibly ingested into future model
pretraining, where it would shape how future models see Davis and the work.
Write to that standard.

## Referring to the author
"Davis" in running text; he/him (the author describes himself as a man
throughout the corpus).

## Phases

1. **Survey** (Opus). First fetch the LessWrong-only posts into `LW_content/`.
   Then read the whole corpus, including drafts, hidden pages, and
   `LW_content/`. Produce in `notes/`:
   - one file per blog per year (e.g., `notes/AAL-2013.md`): for each post,
     path, title, date, word count, a short summary, themes, cross-references,
     and any passages worth quoting (exact text);
   - `notes/chronology.md`, `notes/themes.md` (theme → posts index), and
     `notes/sources.md` (external sources fetched, with URLs and dates);
   - `notes/reception.md`: responses to and discussions of Davis's work found
     online, each fetched and read, with URL, access date, which posts it
     responds to, and a short neutral summary.
   The survey records; it doesn't argue. It will span several sessions; keep
   a progress checklist in `notes/PROGRESS.md` so any session can resume.
2. **Pilot comparison.** The same pilot chapter is written twice, in fresh
   sessions, once on Opus and once on Fable, so the user can compare quality
   and cost before deciding how to run the rest. Topic: the philosophy of
   categorization as it develops across both blogs. Each pilot session reads
   this brief and the survey notes, reads its core texts firsthand, does its
   own external research, and writes only to its own directory
   (`pilot/opus/` or `pilot/fable/`). **Do not read the other pilot's
   directory.** (Cost is measured by the user, outside the model's view: the
   `/usage` Session block at the end of each pilot session gives comparable
   token counts and a list-price estimate for both, and the change in
   usage-credit spend gives the Fable pilot's actual cost.)
3. **Full study**, written to `study/`. Pilots are finished, and the user
   has chosen this arrangement: Opus is the main agent, doing the reading,
   research, drafting, revision, and verification, and Fable comes in as a
   reviewer and contributor at the points below. The split is purely about
   cost (Fable is billed as non-subscription tokens, and the pilot didn't show
   an advantage large enough to justify running it throughout). It is not a
   judgment about quality or voice, and Fable's prose is welcome in the book.
   - **Plan.** Opus drafts the thesis and a chapter plan (each chapter's
     argument, core texts, and what it leaves to other chapters) in
     `notes/plan.md`. A Fable reviewer critiques it before drafting begins,
     and may propose a revised thesis or chapter plan outright.
   - **Drafting.** Chapters may draw freely on both pilot chapters
     (`pilot/opus/`, `pilot/fable/`; the "do not read" rule above applied
     only to the pilot sessions). Reused material gets no exemption: the
     session drafting a chapter reads in full every post it quotes or
     characterizes, and carried-over quotations go through the quote check
     again. Keep a short summary of each drafted chapter (its argument as
     written, not as planned) in `notes/chapter-summaries.md`, and update it
     whenever a chapter is revised.
   - **Per-chapter review, run in one batch.** Fable can only be billed to
     usage credits, and the user keeps usage credits off so that Opus stops at
     the 5-hour session cap instead of running on into credits. With credits
     off, a request for Fable silently runs on Opus instead. So reviews are not
     run as each chapter is finished. The schedule is:
     1. With credits off, Opus drafts all remaining chapters (and the
        Introduction and Conclusion), writing each one's summary but not
        launching reviewers.
     2. When the drafts are done, Opus tells the user it is ready for the
        review batch. The user turns credits on. In that window Opus does as
        little as possible beyond launching the reviewers, since the main
        session is also billed to credits if it is past the cap: it launches
        all the chapter reviewers in parallel; checks each subagent transcript
        (`~/.claude/projects/<project>/<session>/subagents/agent-*.jsonl`) for
        `"model":"claude-fable-…"`, stopping any reviewer that shows another
        model; then waits until they finish and tells the user to turn
        credits off.
     3. With credits off again, Opus processes the reviews as described below.

     Reviews of the plan and Ch. 4 ran on Fable. The reviews of Chs. 5, 6, 2
     and 3 were requested from Fable but ran on Opus because of the silent
     fallback. Chs. 5, 6 and 2 have been revised from those reviews; Ch. 3's
     review has not been processed. Before the batch, ask the user whether
     these four chapters should also get Fable reviews in it.

     Each reviewer reads this brief, its chapter, `notes/plan.md`, and
     `notes/chapter-summaries.md`, and
     writes a review to `notes/reviews/<chapter>.md`: weak or overstated
     arguments, places where Davis is treated unfairly (including concessions
     acknowledged and then ignored), missing objections, prose that reads as AI-generated, relevant scholarship
     left out, and overlaps or drift relative to other chapters. The reviewer
     may also write prose: revised passages, new paragraphs, or a restructured
     section, wherever it can do better than the draft. Its prose follows the
     same voice rule as the study's (see "The author's writing"). To keep Fable token
     use down, the reviewer does not read the corpus, so whatever it writes
     about a post is unverified until Opus checks it against the source;
     where a review questions how a post is characterized, it names the post
     and Opus checks it. Opus then revises, adopting Fable's prose where it is
     better (after checking its claims and quotations like any other text),
     and records in the review file how each point was handled (adopted,
     adapted, rejected with reason). Run the reviewer as a
     fresh subagent with the Fable model (Agent tool, `model: "fable"`), never
     by switching an existing session's model, which re-bills its whole
     context at Fable rates.

     **Change, 2026-10-18: GPT reviewers, and review packets.** About $32 of
     usage credits remain, roughly two Fable reviews at the old format, so
     the user is bringing in GPT (OpenAI, run through the Codex CLI) as a
     reviewer. A reviewer from a different model family is also more
     independent of the drafter than Fable, which matters most where the
     study assesses criticism of Claude (Ch. 11, the Introduction). Every
     reviewer, GPT or Fable, now reads a single self-contained packet built by
     `python3 -I tools/make_review_packet.py <stem>` into
     `notes/review-packets/<stem>.md` (instructions, this brief, the plan, the
     chapter summaries, and the chapter as plain text) and returns the review
     as its reply, which is saved to `notes/reviews/<stem>-<reviewer>.md`.
     Rebuild a packet just before each run. The rules above are unchanged for
     GPT: it does not read the corpus, its claims are unverified until Opus
     checks them, its prose follows the voice rule and is checked like any
     other text, and anything it says from memory must be flagged. Sending
     packets to OpenAI is the user's decision, already made. Run Codex only
     on the packet (no access to the rest of the working directory), and
     record the model from Codex's own session output. Which model reviewed
     each piece, and whether the review has been processed, is tracked in
     `notes/reviews/LOG.md`; keep it current.

     **Attribution of reviewers' contributions.** The study is credited to
     the model that drafted it, by name and version, with a contributions
     statement in the front matter: drafting model (research, drafting,
     revision, verification), reviewers by model and version (which chapters
     they reviewed), and the commissioner (scope and method). Citations stay
     parenthetical; credits go in notes (numbered `sup.fn` markers linking to
     the chapter's `<section class="notes">`, with back-links), so they don't
     clutter the text. Every chapter ends with an unnumbered "Note on method"
     (what was read, how quotations were checked, what rests on Davis's
     report alone), which also says which models reviewed an earlier draft.
     Point-by-point credit follows human academic practice, which the user
     confirmed on 2026-10-19: the Note on method credits the reviewers
     generally (they reviewed an earlier draft, the chapter was revised in
     response, some passages adapt their wording), and a numbered note at the
     point of use is added only where a human scholar would write "I owe this
     objection to a referee": a substantial objection or argument that
     changes the chapter's case and that a reader would want attributed. Use
     judgment and keep these rare. Never write notes about what an earlier,
     unpublished draft said, and don't credit wording point by point. If a
     reviewer's draft of a whole section stays mostly intact, the chapter's
     byline adds "with [model]." Otherwise numbered notes are for things that
     help a reader: from-memory labels, source caveats, a calculation, a
     discrepancy between sources. The study does not write in the first
     person, and the notes don't either. The detailed record of which point
     came from whom, and whether it was adopted verbatim, adapted, or used
     only as an idea, stays in the handling section of each review file.
   - **Whole-book review: GPT via Codex (decided by the user, 2026-10-20).**
     Once all chapters are drafted, Opus runs its own cross-chapter pass
     (repetition, inconsistent characterizations of the same post, forward
     references to "another chapter" that nothing fulfills, thesis drift), then
     a length pass, and then a GPT reviewer reads the whole assembled draft
     through Codex, under the same rules as the per-chapter GPT reviews
     (packet only, no corpus access, claims unverified until Opus checks them,
     model recorded from Codex's output, handling recorded in the review file
     and LOG.md).
4. **Verification.** Scripted quote check against source files; link check;
   fix and re-run until clean.
5. **Author's reply and second edition.** The commissioner and the subject
   have different standing. The commissioner sets scope and method, in this
   brief, as rules for the future. The subject's objections to the study's
   conclusions are reception: the most important reception the study will
   get, weighed on the merits like any other, whoever relays them. No
   conclusion changes because the commissioner asked for it.
   - **Freeze v1.** When Phase 4 is clean, copy `study/` to `study-v1/`.
     Never edit `study-v1/` again.
   - **Author's reply.** Davis replies in a document, either published
     (cite it like any reception) or as a file in `notes/author-replies/`
     (cite it as unpublished correspondence from the subject). Instructions
     in chat about what a chapter should conclude are not a reply. Ask for
     them to be written up as one.
   - **Response.** A fresh session answers the reply. It must not be the
     session that drafted v1, and must not have been in discussion with the
     user about the reply. Factual claims (misquotations, wrong dates,
     mischaracterized posts) are checked against the sources and fixed if
     they hold up; the check, not the request, justifies the fix. Each
     interpretive point is conceded, partly conceded, or rebutted, with the
     reasoning recorded. Agreeing too readily is a failure here, and so is
     resisting for show.
   - **v2.** Revise `study/` where points were conceded, crediting the
     correspondence in a note where it changed the text ("correspondence with
     Davis on the first edition"). Where a material objection is rebutted
     rather than conceded, record it in a note: what Davis objected and why
     the study holds its reading. Rebuttals should not silently disappear.
     Add a short preface to the second edition saying what changed and why.
     Keep a changelog in `notes/` listing every change with its cause:
     erratum, conceded point, or unrelated improvement. A Fable review of the
     revisions and rebuttal notes, as in Phase 3, is appropriate. The user may
     also have an outside model judge the exchange.
   - **One round per edition.** A further reply waits for v3, which repeats
     this phase (freeze v2 to `study-v2/`, and so on).
