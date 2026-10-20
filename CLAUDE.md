This directory holds a long-running scholarly study project. The standing brief
below governs all work here; follow it in every session, including after
context compaction.

## Git in this project

This overrides the global instruction "Don't make git commits or propose
commit messages": in this project, Claude commits. Git is the archive of
drafts, so commit:

- before revising a chapter (so the draft that was reviewed is preserved), and
  after each new draft is written and passes the quote and URL checks;
- after a batch of reviews comes in, before processing them.

Commit to `master` with a plain message saying what changed (e.g. "Ch. 7
draft 2 after GPT review"). Never push, rewrite history, or force anything;
the user pushes. Leave untracked files you didn't create (such as rendered
`.html` copies of notes) out of commits unless the user asks.

Each chapter file carries its draft number as `<meta name="draft"
content="N">`; bump it when writing a new draft, and keep the heading of its
entry in `notes/chapter-summaries.md` in step. `notes/reviews/LOG.md` records,
for each review, the draft and the commit containing the text the reviewer
saw.

@BRIEF.md
