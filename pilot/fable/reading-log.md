# Reading log — Fable pilot chapter

Session model: Fable 5.1 (`claude-fable-5-1`), as reported by the harness at
session start. Session date: 2026-10-16. All corpus texts below were read in
full through `tools/show.py` in this session before being quoted or
characterized. Nothing in `pilot/opus/` was read.

## Corpus texts read in full

### An Algorithmic Lucidity (`AAL_content/`)
- 2013/classification.md
- 2016/prescription.md; 2016/prescription-ii.md
- 2017/an-intuition-on-the-bayes-structural-justification-for-free-speech-norms.md
- 2019/where-to-draw-the-boundaries.md; the-univariate-fallacy.md;
  schelling-categories-and-simple-membership-tests.md; feature-reduction.md;
  hobbyhorse-apology.md; algorithms-of-deception.md; maybe-lying-doesnt-exist.md;
  relevance-norms-or-gricean-implicature-queers-the-decoupling-contextualizing-binary.md;
  firming-up-not-lying-around-its-edge-cases-is-less-broadly-useful-than-one-might-initially-think.md
- 2020/philosophy-in-the-darkest-timeline-basics-of-the-evolution-of-meaning.md;
  maybe-lying-cant-exist.md
- 2021/unnatural-categories-are-optimized-for-deception.md;
  reply-to-nate-soares-on-dolphins.md; blood-is-thicker-than-water.md;
  comment-on-deception-as-cooperation.md
- 2024/deep-learning-is-function-approximation.md

### The Scintillating But Ultimately Untrue Thought (`UUT_content/`)
- 2018/blegg-mode.md; the-categories-were-made-for-man-to-make-predictions.md;
  reply-to-the-unit-of-caring-on-adult-human-females.md; interlude-xv.md;
  untitled-metablogging-26-december-2018.md
- 2019/use-it-or-lose-it.md; interlude-xviii.md; link-where-to-draw-the-boundaries.md;
  self-identity-is-a-schelling-point.md; reply-to-ozymandias-on-fully-consensual-gender.md;
  terminology-proposal-developmental-sex.md; more-schelling.md;
  on-the-argumentative-form-super-proton-things-tend-to-come-in-varieties.md
- 2020/book-review-the-origins-of-unfairness.md; crossing-the-line.md;
  oceans-rise-empires-fall.md
- 2021/link-unnatural-categories-are-optimized-for-deception.md;
  link-blood-is-thicker-than-water.md;
  you-are-right-and-i-was-wrong-reply-to-tailcalled-on-causality.md;
  sexual-dimorphism-in-the-sequences-in-relation-to-my-gender-problems.md
- 2022/challenges-to-yudkowskys-pronoun-reform-proposal.md;
  the-two-type-taxonomy-is-a-useful-approximation-for-a-more-detailed-causal-model.md
- 2023/a-hill-of-validity-in-defense-of-meaning.md; beyond-the-binary.md;
  if-clarity-seems-like-death-to-them.md
- 2024/agreeing-with-stalin-in-ways-that-exhibit-generally-rationalist-principles.md;
  prediction-markets-are-not-a-drop-in-replacement-for-concepts.md
- 2025/a-generic-ontological-finickiness.md
- Drafts (`UUT_content/drafts/`): two-kinds-of-value-dependence; elision-vs-choice;
  taxometrics…; assigned-at-birth-is-a-schelling-point;
  but-im-not-quite-sure-what-that-means…; lies-to-cis-people…; the-view-from-nowhere;
  on-being-stereotyped-badly; i-mean-yes-i-agree-that-man-should-allocate-some-more-categories-but;
  i-tell-myself-to-let-the-story-end…
- Pages: pages/ancillary/dolphin-war.md; pages/ancillary/twelve-short-stories-about-language.md
- Images viewed: images/blegg_categorization_criteria.png; genderspace_cluster_choice.png;
  yudkowsky-the_disclaimer.png; piper-spending_social_capital_on_talking_about_trans_issues.png;
  bensinger-doesnt_unambiguously_refer_to_the_thing.png

### LessWrong-only posts (`LW_content/`)
- 2019/blegg-mode (linkpost intro); 2020/brief-response-to-suspended-reason…;
  2020/containment-thread-on-the-motivation-and-political-context.md;
  2023/lying-alignment-chart (+ image)

## Reception read
- `notes/reception.md` entries for: Blegg Mode, Where to Draw the Boundaries?,
  Schelling Categories, Maybe Lying Doesn't Exist, Containment Thread,
  Unnatural Categories, Reply to Nate Soares, Blood Is Thicker Than Water,
  Challenges, Hill of Validity, If Clarity, Agreeing With Stalin, Ozy 2018,
  SneerClub 2023, Ozy 2023, Isso threads, Part C.
- Full comment texts from `reception_data/lw_threads/` (by commentId; every ID
  cited in the chapter was located and its author/date verified by script):
  Boundaries (Said Achmiz, Wei Dai, abramdemski, Raemon ×2, TAG, Davis, Hornbein);
  Unnatural Categories (johnswentworth, iceman, Wei Dai ×2, tslarm, DanielFilan, Davis 2025);
  Soares thread (So8res, Vaniver ×2, Davis); Blood (aphyer, Yvain, Davis);
  Maybe Lying (Yvain ×2, Connor Flexman, Jessica Taylor); Challenges (habryka, gjm,
  localdeity, Davis); Hill of Validity (Raemon); If Clarity (Vaniver).
- `reception_data/isso_threads/2021_link-unnatural-categories-are-optimized-for-deception.md`
- `reception_data/web/ozy-2018-man-should-allocate/text.txt` (post in full)
- `reception_data/web/reddit-sneerclub-categories-2023/text.txt` (thread in full)

## External sources
See `sources.md` for every external document fetched, with URL, access date,
and what portion was read. Items that could not be fetched (Yudkowsky's 2018
tweets and 2020/2021 Facebook posts, Soares's tweets, Piper's Tumblr post,
Byrne 2020, the PNAS full texts) are quoted only as the corpus quotes them, and
the chapter says so where it uses them.

## Verification
- `python3 -I pilot/fable/tools/check_quotes.py pilot/fable/parts/*.html`:
  269 quotations checked, 0 problems (final run).
- Every corpus footnote date was checked by script against the file `Date:`
  header (32 checked; two URL/date errors found and fixed).
- Link check: 71 distinct external URLs; all returned HTTP 200 except the
  Wayback Machine snapshot of Alexander's 2014 essay, which returned 429 (rate
  limit) on the check pass after having been fetched successfully earlier in
  the session.
