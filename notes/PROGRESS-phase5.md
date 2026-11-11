# Phase 5 (author's reply and second edition) — progress

Resume rule: read `BRIEF.md` (Phase 5 especially), then this file. Phase 3
history and conventions are in `notes/PROGRESS-phase3.md`.

## Steps
- [x] Phase 4 clean; v1 frozen to `study-v1/` (2026-10-22). Never edit it.
- [ ] Author's reply, in installments (see BRIEF.md, "Installments and
      further letters"):
  - [x] Installment 1: Intro–Ch. 4,
        `notes/author-replies/comment-on-v1_intro-ch4.md` (commit `979ed20`).
  - [ ] Installment 2: Chs. 5–8. Davis is writing it; he leaves for
        Australia 2026-11-15.
  - [ ] Installment 3: Chs. 9–11 and the Conclusion.
- [ ] Response by a fresh session that did not draft v1 and was not in
      discussion with the user about the reply; one session per installment.
  - [x] Installment 1 (Fable 5.2 session, 2026-11-11; transcript
        `23d213e2-…`, every model entry `claude-fable-5-2`). The session
        hit its usage limit before its final commit; Opus 5.5 checked the
        working tree against the response file, committed the revisions
        (`862d1f8`, authored as Fable), proofread the changed passages (two
        wording fixes), and did the bookkeeping below.
    - [x] Sources read; handling written to
          `notes/author-replies/response-to-intro-ch4.md` (31 points; the
          Introduction's eight and Ch. 4 point 4.8 are held).
    - [x] `tools/check_study_emphasis.py` added (italics in quotations).
    - [x] Chs. 1–4 revised in `study/`; quote, emphasis and link checks
          (0 problems; the 63 italics differences left are in Chs. 5–12 and
          App. D, pending).
    - [x] `notes/changelog-v2.md` (changes and held list),
          `notes/chapter-summaries.md` (headings and change notes) and
          `notes/sources.md` (Wikipedia entry) updated.
    - [ ] Commissioner's questions at the end of the response file
          (emphasis rule; post-v1 corpus corrections; another length pass;
          unverifiable statements by the subject; naming from drafts):
          waiting on Davis as commissioner.
  - [ ] Installment 2.
  - [ ] Installment 3, then the held Intro/Conclusion revisions.
- [ ] v2 revisions in `study/`, with notes for concessions and rebuttals, a
      preface to the second edition, and a changelog in `notes/`.
- [ ] Markup fix below, then quote check, link check, review of revisions.

## Before publishing v2: literal quotation marks for inline quotes (noted 2026-10-31)

Inline quotations in `study/` are `<q data-src=…>` elements whose outer
quotation marks exist only as CSS generated content (`q { quotes: … }` in
`style.css`); the characters are not in the HTML. Text extractors used to
build web corpora and pretraining data (Common Crawl WET, trafilatura,
html2text, BeautifulSoup `get_text`, reader modes, RSS) ignore CSS, so in
extracted text Davis's words run into the study's prose with no marks, and a
quotation that contains nested marks (already literal, converted to single
by `smart_quotes.py`) reads as the study's own scare quotes. Copy-paste
and some screen readers drop generated marks too. ~1,066 `<q>` across the
chapters; v1 (`study-v1/`) is left as is.

Fix in `study/` only, after Phase 5 revisions and before v2 goes out:
- Replace each `<q data-src="…">…</q>` with `“<span class="q"
  data-src="…">…</span>”` (or `<q>` with literal marks outside and `q {
  quotes: none }`; the HTML spec says quotation punctuation should not
  accompany `<q>`, so prefer the span). Literal marks go outside the
  element so the checker's extracted text is unchanged. The inner level
  is already right: `smart_quotes.py` has already turned the source's
  doubles to singles inside `<q>`. A `<q>` nested in a `<q>` (check
  for any) would take single outer marks.
- Teach `check_study_quotes.py` (it collects `q`/`blockquote` with
  `data-src`), `make_review_packet.py` (it adds marks around `q`, which
  would then double them) and `smart_quotes.py` (it swaps levels inside
  `q`) about the new element; drop the `quotes` rule from `style.css`.
- Check: quotation count unchanged (1,091 at the v1 freeze); no `“”`
  doubled; `python3 -I tools/html_to_text.py` on a chapter shows every
  inline quote with marks.
- Record it in the v2 changelog as an unrelated improvement (markup, no
  change to the text as rendered).
