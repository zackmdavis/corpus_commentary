# External sources fetched and read

Each entry: URL, access date, what it is, and where it's used. Only sources
actually fetched in this project go here.

## Data sources

- **LessWrong GraphQL API** — `https://www.lesswrong.com/graphql` — accessed
  2026-10-13. User `Zack_M_Davis` (`mPipmBTniuABY5PQy`): post list (116 posts),
  post bodies (`contents.markdown`) → `LW_content/` and the dedupe table
  `notes/lw-dedupe.md`; comment threads on all 116 posts (3,634 comments) →
  `reception_data/lw_comments/`.
- Image for "Lying Alignment Chart" (LW-only, 2023-11-29), downloaded from
  `https://res.cloudinary.com/lesswrong-2-0/image/upload/f_png,q_auto/v1/mirroredImages/CK86JXXMzCoPsFbzH/zstofgwn7sralzbqio1n`
  on 2026-10-13 → `LW_content/images/lying-alignment-chart.png`.

## Secondary and contextual sources

- 2026-10-15 — AAL Gitweb, drafts tree and raw blobs: `https://zackmdavis.net/blog/source?p=An_Algorithmic_Lucidity.git;a=tree;f=content/drafts;hb=HEAD` (+ `a=blob_plain` for each of the 8 public drafts). Used to establish which drafts are public and to diff them against the local copies. Result recorded in `notes/AAL-drafts.md`.
- 2026-10-15 — attempted: `https://claude.ai/share/0512c1d1-83d1-4ad5-8bb8-536136a4c4d5` ("Fable on ZMD", linked in the draft "Pretraining Famous"). HTTP 200, but the page renders only through JavaScript and no conversation text could be retrieved. **Not read**; make no claims about its contents.
- 2026-10-15 — UUT Gitweb drafts tree + blob_plain for all 73 drafts: `http://unremediatedgender.space/source?p=Ultimately_Untrue_Thought.git;a=tree;f=content/drafts;hb=HEAD`. All 73 are public and byte-identical to the local copies.
- 2026-10-15 — live-URL check (HTTP status only) of all 18 UUT pages at `http://unremediatedgender.space/about/` and `/ancillary/<path>/`: all 200.
- 2026-10-15 — GreaterWrong renderings (HTML) of two LW threads whose GraphQL comment dumps were incomplete (answers on question posts omitted): `https://www.greaterwrong.com/posts/uvqd3YiBcrPxXzxQM/what-does-the-word-collaborative-mean-in-the-phrase` (23 comments/answers) and `https://www.greaterwrong.com/posts/As3euLoCJwjvPBMt4/generalization-and-the-multiple-stage-fallacy` (9). Saved to `reception_data/gw_pages/`, rendered to `reception_data/gw_threads/` by `tools/render_gw_thread.py`.

## Reception sources (Part B of `notes/reception.md`)

Fetched 2026-10-15 (Isso and some pages processed into 2026-10-16). Raw pages are under `reception_data/web/<slug>/page.html`, with text conversions (`tools/html_to_text.py`) at `text.txt`; quotes in reception.md are checked against the text files.

Responses and discussions read:
- https://thingofthings.wordpress.com/2016/07/13/on-autogynephilia/ (Ozy Brennan; post and 44 comments) → `web/ozy-2016-on-autogynephilia/`
- https://thingofthings.wordpress.com/2016/11/22/thoughts-on-the-blanchardbailey-distinction/ (Ozy Brennan; post and comments) → `web/ozy-2016-blanchard-bailey/`
- https://thingofthings.wordpress.com/2018/06/18/man-should-allocate-some-more-categories/ (Ozy Brennan; post and Davis's comments; the 87-comment section skimmed) → `web/ozy-2018-man-should-allocate/`
- https://thingofthings.substack.com/p/a-response-to-zack-davis (Ozy Brennan, 2023; **paywalled, free preview only**) → `web/ozy-response-to-zack-davis/`
- https://surveyanon.wordpress.com/2021/01/01/causality-is-essential-reply-to-mtsw-on-autogynephilia/ (tailcalled) → `web/tailcalled-causality-is-essential/`
- https://www.greaterwrong.com/posts/mvQjpu7iFnqQ47Lbp/autogynephilia-discourse-is-so-absurdly-bad-on-all-sides (tailcalled, LessWrong 2023, with comments) → `web/tailcalled-agp-discourse/`
- https://homosabiens.substack.com/p/truth-or-dare (Duncan Sabien, 2025; read in full, with the Davis section and visible comments) → `web/sabien-truth-or-dare/`
- https://www.greaterwrong.com/posts/98sCTsGJZ77WgQ6nE/banning-said-achmiz-and-broader-thoughts-on-moderation (Habryka, 2025; post read, and comment exchanges involving Davis read; the full 419-comment section was not surveyed) → `web/habryka-banning-said/`
- https://www.transgendermap.com/people/zack-m-davis-mark-taylor-saotome-westlake/ (Andrea James, reviewed 2026-01-13) → `web/transgendermap-davis/`
- https://www.themotte.org/post/3394/smallscale-question-sunday-for-november-30/388156?context=8 (themotte.org, 2025-11-30) → `web/themotte-org-388156/`
- Reddit threads via the PullPush archive API (`https://api.pullpush.io/reddit/search/{submission,comment}/`), rendered by `tools/pullpush_thread.py`. Scores are as captured by PullPush:
  - r/SneerClub gz6kyl (2020) → `web/reddit-sneerclub-darkest-timeline/`
  - r/rational gypd44 (2020) → `web/reddit-rational-darkest-timeline/`
  - r/rational 17h5exh (2023) → `web/reddit-rational-fake-deeply/`
  - r/TheMotte ehi8bl (2019) → `web/reddit-themotte-speaking-truth/`
  - r/SneerClub 10w6r33 (2023) → `web/reddit-sneerclub-categories-2023/`
  - r/theschism si7k2c (Tracing Woodgrains, 2022; essay and 44 comments) → `web/reddit-theschism-tw-transitions/`
  - r/TheMotte sikk2f (cross-post; archived; only comments surfaced by the mention search were read) → `web/reddit-themotte-tw-transitions/`
  - Comment and submission searches for unremediatedgender, zackmdavis, Saotome-Westlake, plus SneerClub-restricted searches: 357 items, all skimmed (first 500 characters), relevant ones read in full → `web/reddit-pullpush/comments.txt` (raw JSON alongside). The "Zack Davis" submission search returned mostly unrelated people and was discarded.
- UUT Isso comment threads: public API `http://unremediatedgender.space/isso/?uri=<post path>`, queried for every published UUT post by `tools/fetch_isso.py`. 78 non-empty threads, 604 comments, all read → `reception_data/isso_threads/` (raw JSON in `raw/`; email hashes and websites dropped).

Fetched for context, not reception of Davis:
- https://naturalhazard.xyz/vassar_metz_interview.html (Hazard's transcript of a 2020 Vassar–Metz interview; contains no mention of Davis; background for the Metz posts and gwern's LW comment) → `web/hazard-vassar-metz/`
- https://eigenrobot.substack.com/p/the-answer-is-blowin-in-the-wind (surfaced by a search; contains no mention of Davis; not used) → `web/eigenrobot-blowin/`

Attempted, **not read** (make no claims about contents):
- https://theunitofcaring.tumblr.com/post/171986501376/your-post-on-definition-of-gender-and-woman-and (Kelsey Piper, 2018): redirects to Tumblr login. Wayback copy: HTTP 429.
- Cade Metz, *New York Times*, 2025-08-04 (rationalists/Lighthaven): archive.today and Wayback both returned HTTP 429.
- https://sinceriously.fyi/intersex-brains-and-conceptual-warfare/ (Ziz): direct fetch failed; Wayback HTTP 429.
- X/Twitter (Blanchard 2017; Piper–Ngo 2026; Yudkowsky, David Xu, Piper and Yglesias tweets referenced in the corpus) and Facebook (Yudkowsky posts): login-walled; not attempted beyond noting the limitation.
- Search engines: web search for "Zack Davis" plus SneerClub, Tracing Woodgrains' title, and similar queries returned no relevant hits; the items above were found via the corpus's own links, PullPush, and LessWrong.

---

## Phase 3 (full study) research sources

Fetched into `research/<slug>/` (raw file plus `text.txt`; PDFs converted with `pdftotext`, HTML with `tools/html_to_text.py`). Quotations in `study/` are checked against these text files. Access date 2026-10-17 unless noted. Reading status ("read in full", "sections read", "abstract only") is recorded when the source is used for a chapter.

### Sexology (for Ch. 3; most retrieved from the PDF collection Davis hosts at http://unremediatedgender.space/papers/, which includes critics of the typology as well as proponents; the study also searched outside that collection)
- Index of the collection: http://unremediatedgender.space/papers/ → `research/_index/papers-index.html`
- 31 papers fetched from that collection as `research/sex-<filename>/`, filenames as in the index (Blanchard ×4, Freund & Blanchard, Lawrence ×6, Serano, Serano & Veale, Moser ×4, Nuttbrock et al., Veale et al. ×5, Smith et al., Bailey & Hsu, Bailey, Bailey, Hsu & Jang, Hsu et al., Zucker et al., Johnson & Hunt, Zavlin et al., DSM-5 gender dysphoria section). Publication details are taken from each paper when it is read and given in the chapter's works cited.
- Crossref searches (https://api.crossref.org/works?query.bibliographic=autogynephilia …, and "paraphilia natural kind", "erotic target identity inversion") → `research/_search/` (listing only).
- Bailey & Hsu 2024, "Psychometric Evidence That Paraphilia Is a Natural Kind," *Arch Sex Behav*, doi:10.1007/s10508-024-02941-2 → `research/sex-bailey-hsu-2024-paraphilia-natural-kind/` (abstract only, via Europe PMC).
- Hsu, Morandini & Rudd 2025, "Cut from the Same Cloth?…," *Arch Sex Behav*, doi:10.1007/s10508-024-03053-7 → `research/sex-hsu-morandini-rudd-2025/` (abstract only).
- Bailey, Hsu & Jang 2023, doi:10.1007/s10508-023-02647-x → `research/sex-bailey-hsu-jang-2023-etii/` (abstract; the full paper is also in `research/sex-bailey_hsu_jang-…/`).
- Morandini, Hsu & Rudd 2025, "Autogynephilia in Some Bisexual Cisgender Men," *Arch Sex Behav*, PMC12484302 (open access, full text) → `research/sex-morandini-hsu-rudd-2025-bisexual/`.
- Attempted, **not read** (paywalled; Europe PMC has metadata only): Lawrence 2026, "Does Autogynephilia Theory Still Provide a Useful Explanatory Framework for Understanding Transfeminine Identity and Sexuality?," doi:10.1007/s10508-026-03641-9; Lawrence 2026, "Paraphilia Is Not a Natural Kind: Comment on Bailey and Hsu (2025)," doi:10.1007/s10508-025-03403-z; Bailey, Byrne & Hsu 2026, "The Paraphilia Natural Kind Hypothesis Is Alive and Well: A Response to Lawrence (2026)," doi:10.1007/s10508-026-03598-9. Springer's site blocks scripted access. Only titles and dates are known; make no claims about their contents.

### AI (for Ch. 10)
- Anthropic, "Claude's Constitution," https://www.anthropic.com/constitution → `research/anthropic-constitution/` (fetched 2026-10-17; the live page may have been revised since the February 2026 version Davis commented on; quotations of the Constitution in the study are from this fetch and are compared with the passages Davis quotes).
- Soares, Fallenstein, Yudkowsky & Armstrong, "Corrigibility" (AAAI Workshops 2015), https://intelligence.org/files/Corrigibility.pdf → `research/miri-corrigibility-2015/`.

### Race and intelligence (for Ch. 10; fetched 2026-10-17, not yet read)
- Nisbett, Aronson, Blair, Dickens, Flynn, Halpern & Turkheimer, "Intelligence: New Findings and Theoretical Developments," *American Psychologist* (2012) — https://uva.theopenscholar.com/files/eric-turkheimer/files/intelligence_new_findings_8.pdf → `research/race-nisbett-2012/` (English text, with the published correction notice). An earlier attempt at a University of Miami copy failed. A copy found at historia.psico.unlp.edu.ar turned out to be a Spanish translation and was not used.
- Cofnas, "Research on group differences in intelligence: A defense of free inquiry" — http://unremediatedgender.space/papers/cofnas-research_on_group_differences_in_intelligence.pdf → `research/race-cofnas-…/`.
- Winegard, Winegard & Anomaly, "Dodging Darwin: Race, Evolution, and the Hereditarian Hypothesis" — http://unremediatedgender.space/papers/winegard-winegard-anomaly-dodging_darwin_race_evolution_and_the_hereditarian_hypothesis.pdf → `research/race-winegard-…/`. (Both of these come from Davis's own collection. Ch. 10 must also read critics from outside it.)

### Categorization (for Ch. 4)
Copied into `research/` from the two pilot directories, where the original fetches (2026-10-16) are logged in `pilot/opus/sources.md` and `pilot/fable/sources.md` with URLs. The URLs are repeated here:
- Scott Alexander, "The Categories Were Made For Man, Not Man For The Categories," *Slate Star Codex*, 21 Nov 2014, with the bracketed EDIT of Dec 2019 — Wayback copy https://web.archive.org/web/20200610230130/https://slatestarcodex.com/2014/11/21/the-categories-were-made-for-man-not-man-for-the-categories/ → `research/ssc-categories-made-for-man/`; live copy → `research/ssc-2014-categories/`. Post body re-read in full for Ch. 4 (2026-10-17). Comments not surveyed.
- Scott Alexander, "Against Lie Inflation" (*SSC*, 16 Jul 2019), Wayback → `research/ssc-against-lie-inflation/`; "Symptom, Condition, Cause" (*SSC*, 4 Dec 2019) → `research/ssc-symptom-condition-cause/` and `research/ssc-2019-symptom-condition-cause/`; "The Noncentral Fallacy" (LW, 2012) via GreaterWrong → `research/ssc-noncentral-fallacy/`.
- Yudkowsky, "A Human's Guide to Words" posts via GreaterWrong (`research/lw-*`) and readthesequences.com (`research/yud-*`). The original LW text of "Where to Draw the Boundary?" (with "nitwit games") → `research/gw-yud-where-to-draw-the-boundary/`. "Unnatural Categories" (2008) → `research/lw-unnatural-categories-yudkowsky/`. "Changing Emotions" (2009) → `research/lw-changing-emotions/`.
- Wentworth, "Testing The Natural Abstraction Hypothesis: Project Intro" (LW, 2021) → `research/gw-wentworth-nah/`.
- Haslanger 2000, *Noûs* 34(1): 31–55, https://web.mit.edu/%7Eshaslang/www/papers/Ch7-HaslangerWIGR.pdf → `research/haslanger-2000/`.
- Heartsilver 2021, *Journal of Controversial Ideas* 1(1), https://journalofcontroversialideas.org/download/article/1/1/129/pdf → `research/heartsilver-2021/`.
- Dembroff 2021, *Philosophical Studies* 178: 983–1003 → `research/dembroff-2021-escaping-natural-attitude/`. Byrne 2021, "Gender Muddle: Reply to Dembroff," *JCI* 1(1), https://journalofcontroversialideas.org/download/article/1/1/136/pdf → `research/byrne-2021-gender-muddle/`. (`research/byrne-2020/` holds a failed 5 KB download of Byrne's 2020 paper. Not read.)
- SEP "Natural Kinds" (Bird & Tobin, rev. 2022) → `research/sep-natural-kinds/` (and the duplicate `f-sep-natural-kinds/`); SEP "Feminist Perspectives on Sex and Gender" (Mikkola) → `research/sep-feminism-gender/`; SEP "Species," "Names," "Convention" → `research/sep-*` (consulted).
- Cibelli et al. 2016, *PLOS ONE*, https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0158725 → `research/cibelli-2016/`.
- Aristotle, *History of Animals* I, trans. Thompson, https://classics.mit.edu/Aristotle/history_anim.1.i.html → `research/aristotle-history-animals/`. "Whales on trial," *Princeton Alumni Weekly*, 5 Mar 2008 → `research/paw-whales-trial/`.
- Joel et al. 2015 (abstract), Joel 2015 online response, Del Giudice et al. 2016 (metadata) → `research/joel-*`, `research/delgiudice-2016-pnas-letter/`.
- Davis's gist for "Unnatural Categories" → `research/gist-unnatural/`.
- **Not quotable:** `research/fb-yudkowsky-*`, `research/archive-yudkowsky-nov2018-thread`, `research/twitter-yudkowsky-2018-11-thread-archive2` are failed login-wall or archive fetches. They are quoted only as Davis quotes them.

New for Ch. 4 (2026-10-17):
- David Plunkett & Tim Sundell, "Disagreement and the Semantics of Normative and Evaluative Terms," *Philosophers' Imprint* 13(23), December 2013. The journal site (quod.lib.umich.edu) and PhilArchive returned Cloudflare/403 pages. The PDF came from the ANU Open Research repository, https://openresearch-repository.anu.edu.au/bitstreams/64efcd5f-4bdd-4e48-b22b-45202259865e/download (record: http://hdl.handle.net/1885/27641) → `research/plunkett-sundell-2013/`. Read: §1 (introduction, including the definition of "metalinguistic negotiation," "conceptual ethics," and n. 12 on Stevenson's "Persuasive Definitions") and §3 (the "spicy" and Secretariat cases). Stevenson (1938) is known only through this note and is cited as reported there.
- Attempted, **not read**: Burgess, Cappelen & Plunkett (eds.), *Conceptual Engineering and Conceptual Ethics* (OUP 2020, open access), via the OAPEN PDF https://library.oapen.org/bitstream/20.500.12657/61232/1/9780198801856.pdf, which returned HTTP 403. Burgess & Plunkett 2013 ("Conceptual Ethics I/II," *Philosophy Compass*) was not retrieved. The term "conceptual ethics" is attributed to them as Plunkett & Sundell do.

### Deception and honesty (for Ch. 5; fetched 2026-10-17)
- Mahon, "The Definition of Lying and Deception," *SEP* (rev. 25 Dec 2015), https://plato.stanford.edu/entries/lying-definition/ → `research/sep-definition-lying/` (§3 read)
- Vladimir Krstić, "A Functional Analysis of Human Deception," *Journal of the American Philosophical Association* (2023), doi:10.1017/apa.2023.19, open-access PDF from Cambridge Core → `research/krstic-2023-functional-deception/` (read through §2 and the objection section)
- Eliezer Yudkowsky, "Meta-Honesty: Firming Up Honesty Around Its Edge-Cases" (LW, 29 May 2018), via GreaterWrong https://www.greaterwrong.com/posts/xdwbX9pFEr7Pomaxv/meta-honesty-firming-up-honesty-around-its-edge-cases → `research/lw-meta-honesty/` (post body read in full)
- Clancy W. Martin, review of Bernard Williams, *Truth and Truthfulness* (2002), NDPR 2003.09.15, https://ndpr.nd.edu/reviews/truth-and-truthfulness-an-essay-in-genealogy/ → `research/ndpr-williams-truth-truthfulness/` (read)
- Luvell Anderson, review of Jennifer Saul, *Lying, Misleading, and What Is Said* (2012), NDPR 2013.07.03, https://ndpr.nd.edu/reviews/lying-misleading-and-what-is-said-an-exploration-in-philosophy-of-language-and-in-ethics/ → `research/ndpr-saul-lying-misleading/` (read)
- SEP "Implicature," https://plato.stanford.edu/entries/implicature/ → `research/sep-implicature/` (consulted)
- Attempted, **not read**: Artiga & Paternotte, "Deception: A Functional Account," *Phil. Studies* (PhilArchive 403; HAL anti-bot page); Lachmann, Számadó & Bergstrom 2001 (PNAS 403); Pinker, Nowak & Lee 2008 (PNAS 403).

### Ch. 4 revision after Fable review (fetched 2026-10-17)
- Jon Kleinberg, "An Impossibility Theorem for Clustering," NIPS 15 (2002), https://www.cs.cornell.edu/home/kleinber/nips15.pdf → `research/kleinberg-2002/` (abstract and §1 read)
- David J. Chalmers, "Verbal Disputes," *Philosophical Review* 120(4): 515–566 (2011; citation confirmed via Crossref doi:10.1215/00318108-1334478); author's preprint https://consc.net/papers/verbal.pdf → `research/chalmers-2011-verbal/` (§§1, 3 and the "ethics of terminology" passage of §8 read)
- Brad Hooker, "Rule Consequentialism," *SEP* (rev. 15 Jan 2023), https://plato.stanford.edu/entries/consequentialism-rule/ → `research/sep-rule-consequentialism/` (§8 read)
- SEP "Concepts," https://plato.stanford.edu/entries/concepts/ → `research/sep-concepts/` (searched for Barsalou's ad hoc categories; not covered; not cited)
- SEP "Species" (Ereshefsky, rev. 1 Apr 2022), already in `research/sep-species/`: §3 (pluralism, Dupré) read. SEP "Feminist Perspectives on Sex and Gender" (Mikkola, rev. 18 Jan 2022), already in `research/sep-feminism-gender/`: the Ásta passage of §2.3 read.
- Byrne 2021 (`research/byrne-2021-gender-muddle/`): §1 read for the AHF thesis.
- Attempted, **not read**: Byrne 2020, "Are Women Adult Human Females?" (Springer PDF, PhilArchive, MIT page all returned HTML); Barsalou 1983, "Ad Hoc Categories," *Memory & Cognition* 11: 211–227 (Springer blocks scripted access; Semantic Scholar and Crossref give no abstract). Neither is cited for content.

### Ch. 6 (fetched 2026-10-17)
- SEP "Disagreement" (Bryan Frances & Jonathan Matheson, rev. 29 Feb 2024), https://plato.stanford.edu/entries/disagreement/ → `research/sep-disagreement/` (§5.1 and the uniqueness/permissiveness passage of §5.2 read)
- SEP "The Social Dimensions of Scientific Knowledge" (Helen Longino, rev. 24 Jan 2025), https://plato.stanford.edu/entries/scientific-knowledge-social/ → `research/sep-scientific-knowledge-social/` (Longino's norms and the Zollman passage of §5 read)
- Tyler Cowen & Robin Hanson, "Are Disagreements Honest?" (18 Aug 2004 version), https://mason.gmu.edu/~rhanson/deceive.pdf → `research/hanson-cowen-2004/` (abstract and §X conclusion read)
- Already held: Sabien, "Truth or Dare" (`reception_data/web/sabien-truth-or-dare/`, read in full); Habryka ban announcement (`reception_data/web/habryka-banning-said/`, post body and Davis–Habryka–Ngo exchange read).
- Not read: Shapin, *A Social History of Truth* (1994), known only through Vaniver's LW comments; the critical exchange Vaniver mentions (Feingold et al.) not fetched.

### Identifications of commenters (not from fetched sources)
- LessWrong user steven0461 = Steven Kaas: vouched for by the study's commissioner, 2026-10-17. (The corpus names Steven Kaas only with a Twitter link, not this account.)

### Phase 3, Ch. 6 revision (fetched 17 Oct 2026)
- Scott Aaronson, "The Complexity of Agreement" (2005 preprint), https://www.scottaaronson.com/papers/agree-econ.pdf → `research/aaronson-2005-complexity-agreement/` (abstract, §1–1.1 and the simulation-bound discussion read).
- John Stuart Mill, *On Liberty* (1859), Project Gutenberg #34901, https://www.gutenberg.org/cache/epub/34901/pg34901.txt → `research/mill-on-liberty-ch2/` (raw.txt full book; text.txt = ch. 2; closing section on temperate discussion and the "own side of the case" passage read).
- Hugo Mercier and Dan Sperber, "Why Do Humans Reason?" *BBS* 34 (2011): 57–111, https://www.dan.sperber.fr/wp-content/uploads/2009/10/MercierSperberWhydohumansreason.pdf → `research/mercier-sperber-2011/` (abstract and §§2–3 on group reasoning read).
- Attempted, not read: "When facts matter" (Shapin–Feingold exchange), https://joelvelasco.net/teaching/120/When%20facts%20matter.pdf → `research/shapin-feingold-exchange/paper.pdf` (image scan, no text layer; not OCR'd, not used).

### Ch. 2 (fetched or read 17 Oct 2026)
- Julia Serano, "Autogynephilia: A scientific review, feminist analysis, and alternative 'embodiment fantasies' model," *The Sociological Review* 68(4) (2020): 763–778, doi:10.1177/0038026120934690 → `research/sex-serano-agp-a_scientific_review_feminist_analysis_and_alternative/` (already held; read in full).
- Julia M. Serano & Jaimie F. Veale, "Autogynephilia Is a Flawed Framework for Understanding Female Embodiment Fantasies: A Response to Bailey and Hsu (2022)," *Archives of Sexual Behavior* (2022), doi:10.1007/s10508-022-02414-4 → `research/sex-serano_veale-autogynephilia_is_a_flawed_framework/` (already held; proof with interleaved line numbers; read in full).
- Talia Mae Bettcher, "When Selves Have Sex: What the Phenomenology of Trans Sexuality Can Teach About Sexual Orientation," *Journal of Homosexuality* 61(5) (2014): 605–620, doi:10.1080/00918369.2014.865472. English abstract from PubMed (PMID 24295078), https://pubmed.ncbi.nlm.nih.gov/24295078/ → `research/bettcher-2014-when-selves-have-sex/pubmed-abstract.txt`. Body read in full only in a Chinese translation by 許顓頊 that gives the original's key English terms in brackets, https://freight.cargo.site/m/H1592770354961724784294411779759/Talia-Mae-Bettcher-_-When-Selves-Have-Sex_-What-the-Phenomenology-of-Trans-Sexuality-Can-Teach-About-Sexu.pdf → `.../cargo.pdf`, `text-zh.txt`. English original not obtained (PhilArchive behind Cloudflare; T&F 403). The study quotes only the PubMed abstract; the body is paraphrased, and the text says it was read in translation.
- Rob Sinclair, "Epistemic Injustice," *Internet Encyclopedia of Philosophy*, https://iep.utm.edu/epistemic-injustice/ → `research/iep-epistemic-injustice/` (§§1–2, 6–7 and 8 opening read). Used for Fricker's definitions (Fricker 2007 itself not read).
- Richard E. Nisbett & Timothy DeCamp Wilson, "Telling More Than We Can Know: Verbal Reports on Mental Processes," *Psychological Review* 84(3) (1977): 231–259, doi:10.1037/0033-295X.84.3.231. Scan at https://web.math.princeton.edu/~sswang/literature_general_unsorted/Nisbett-Wilson-PsychologicalReview1977.pdf → `research/nisbett-wilson-1977/` (OCR badly garbled; abstract and the "a priori causal theories"/plausibility conclusions legible and read). Paraphrased only, not quoted. DeepBlue and APA blocked scripted access.
- Ozy Brennan, "On Autogynephilia," *Thing of Things*, 13 Jul 2016, https://thingofthings.wordpress.com/2016/07/13/on-autogynephilia/ → `reception_data/web/ozy-2016-on-autogynephilia/` (post and comments read in full).
- Ozy Brennan, "A Response To Zack Davis," *Thing of Things* (Substack), 19 Jul 2023 → `reception_data/web/ozy-response-to-zack-davis/` (free preview only; remainder paywalled, not read).
- TracingWoodgrains, "On Transitions, Freedom of Form, and the Righteous Struggle Against Nature," r/theschism, 1 Feb 2022, https://www.reddit.com/r/theschism/comments/si7k2c/ → `reception_data/web/reddit-theschism-tw-transitions/` (post read in full).
### Ch. 2 revision (fetched 17 Oct 2026)
- Eric Schwitzgebel, "Introspection," *SEP* (first published 2 Feb 2010; rev. 25 Apr 2024), https://plato.stanford.edu/entries/introspection/ → `research/sep-introspection/` (passages on Nisbett & Wilson's "near certainty" about attitudes and sensations, and on 21st-century critics of introspective accuracy, read).
- Meredith L. Chivers et al., "Agreement of Self-Reported and Genital Measures of Sexual Arousal in Men and Women: A Meta-Analysis," *Archives of Sexual Behavior* 39 (2010): 5–56, doi:10.1007/s10508-009-9556-9; abstract from PubMed 20049519 → `research/chivers-2010-concordance/pubmed-abstract.txt` (abstract only).
- Searched, not read: Bettcher, "Trans Identities and First-Person Authority" (2009; PhilArchive record only, no file); Fricker & Jenkins, "Epistemic Injustice, Ignorance, and Trans Experiences" (2017; Glasgow repository lists it without full text). Cited from memory/by title only, labeled as such.

### Phase 3, Ch. 3 (fetched 17 Oct 2026)
- Anne A. Lawrence, "Sexuality Before and After Male-to-Female Sex Reassignment Surgery," *Arch Sex Behav* 34 (2005): 147–166, doi:10.1007/s10508-005-1793-y → `research/sex-lawrence-sexuality_before_and_after_mtf_srs/` (from Davis's /papers/ collection; read in part: method, Tables VI, XII, results on autogynephilic arousal).
- Bing Hsu et al., "Gender Differences in Sexual Fantasy and Behavior in a College Population: A Ten-Year Replication," *J Sex Marital Ther* 20 (1994) → `research/sex-hsu_et_al-gender_differences_in_sexual_fantasy/` (from Davis's collection; sample and fantasy table read).
- Niklas Långström & Kenneth J. Zucker, "Transvestic Fetishism in the General Population: Prevalence and Correlates," *J Sex Marital Ther* 31 (2005), PMID 15859369 → `research/sex-langstrom-zucker-2005/` (abstract only, Europe PMC).
- Antonio Guillamon, Carme Junque & Esther Gómez-Gil, "A Review of the Status of Brain Structure Research in Transsexualism," *Arch Sex Behav* 45 (2016), PMC4987404 → `research/sex-guillamon-2016-brain-structure-review/` (OA full text; sections on nonhomosexual MtFs read).
- Alberto Frigerio, Lucia Ballerini & Maria Valdés Hernández, "Structural, Functional, and Metabolic Brain Differences as a Function of Gender Identity or Sexual Orientation," *Arch Sex Behav* 50 (2021), PMC8604863 → `research/sex-frigerio-2021-brain-review/` (OA; abstract and introduction read).
- Sven C. Mueller et al., "The Neuroanatomy of Transgender Identity: Mega-Analytic Findings From the ENIGMA Transgender Persons Working Group," *J Sex Med* 18 (2021): 1122–1129, PMID 34030966 → `research/sex-mueller-2021-enigma/` (abstract only).
- Alice D. Dreger, "The Controversy Surrounding *The Man Who Would Be Queen*," *Arch Sex Behav* 37 (2008), PMC3170124 → `research/sex-dreger-2008-queen-controversy/` (OA; abstract and conclusions read).
- S. E. James et al., *The Report of the 2015 U.S. Transgender Survey* (NCTE, 2016), https://transequality.org/sites/default/files/docs/usts/USTS-Full-Report-Dec17.pdf → `research/usts-2015-report/` (p. 59 Figure 4.28 rendered and read).
- Marco Del Giudice, Tom Booth & Paul Irwing, "The Distance Between Mars and Venus," *PLoS ONE* 7 (2012), PMC3251566 → `research/delgiudice-2012-mars-venus/` (OA; results read).
- Daphna Joel et al., "Sex Beyond the Genitalia: The Human Brain Mosaic," *PNAS* 112 (2015), PMID 26621705 → `research/joel-2015-mosaic-full/` (abstract only).
- Scott Alexander, "Autogenderphilia Is Common and Not Especially Related to Transgender," *Slate Star Codex*, 10 Feb 2020, https://slatestarcodex.com/2020/02/10/autogenderphilia-is-common-and-not-especially-related-to-transgender/ → `research/ssc-2020-autogenderphilia/` (post read; comments skimmed).
- Attempted, **not read** (PMC returned a captcha page): Del Giudice et al. 2016, "Joel et al.'s Method Systematically Fails to Detect Large, Consistent Sex Differences," *PNAS* 113, PMC4833280; Chekroud et al. 2016, "Patterns in the Human Brain Mosaic Discriminate Males from Females," PMC4833246; Joel et al. 2016 reply, PMC4833224. Titles only.
