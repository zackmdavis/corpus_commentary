# LW_content — provenance

Fetched 2026-10-13 from the LessWrong GraphQL API (`https://www.lesswrong.com/graphql`,
no login), user `Zack_M_Davis` (id `mPipmBTniuABY5PQy`), view `userPosts`: 116 posts
(2009-11-06 to 2026-10-05). Bodies are LessWrong's `contents.markdown` export, unedited.

Deduplication was by content, not title: each post's text was split into 8-word
shingles (lowercased, link targets and HTML tags stripped), and the fraction of
its shingles found in the best-matching file anywhere under `AAL_content/` or
`UUT_content/` (including drafts and pages) was computed.

- **cross-post** (75): containment >= 0.5 (in practice 0.7–1.0); not copied here —
  cite the blog version.
- **lw-only** (32): containment ~0 and not a link to Davis's own blogs. Copied here.
- **linkpost-intro** (6): LessWrong link posts pointing to a post on Davis's own
  blogs, with a short LW-only introductory blurb. Copied here so the blurb can be
  quoted; the linked post itself is in the blog content.
- **linkpost-empty** (3): link posts to Davis's own blog with empty bodies
  (2017: "Dreaming of Political Bayescraft", "An Intuition on the Bayes-Structural
  Justification for Free Speech Norms", "Change"). Not copied.

Dates in the `Date:` header are LessWrong `postedAt`, in UTC. The full per-post
table is in `notes/lw-dedupe.md`. Do not edit these files: quote verification
checks against them.
