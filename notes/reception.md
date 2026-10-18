# Reception

Records the responses to Davis's work that the survey has found and read. Neutral summaries only: the study's assessment of the reception belongs in the study, not here.

**Part A: LessWrong comment threads.** All 116 of Davis's LessWrong posts (2009–2026), comments fetched 2026-10-13 via the GraphQL API (raw: `reception_data/lw_comments/*.json`) and rendered by `tools/render_lw_threads.py` into `reception_data/lw_threads/*.md`. Rendered threads are in tree order, with author, karma at fetch time, date, and permalink. The "Path:" of each entry below is the rendered thread, so `tools/check_note_quotes.py` can verify quoted comments against it. Each permalink is given before the quote it supports. Karma is LessWrong karma at fetch time (a noisy measure of reader approval, not a verdict). 3,634 comments in total, 399 of them by Davis. **Supplement:** the GraphQL view used omits answers on question posts. Two threads had substantial shortfalls against LessWrong's own count: "collaborative truthseeking" (6 of 23) and "Generalization and the Multiple Stage Fallacy?" (5 of 9). Both were re-fetched from GreaterWrong on 2026-10-15 (raw HTML in `reception_data/gw_pages/`) and rendered by `tools/render_gw_thread.py` into `reception_data/gw_threads/`; their entries cite that path. Other shortfalls are off by one or two (deleted comments) and were not re-fetched.

**Part B: other reception** (web search; responses elsewhere; other parties' accounts of disputes; the UUT blog's own Isso comment threads). Searched 2026-10-15; see the scope-and-limitations note at the head of Part B.

**Part C: overview** (neutral synthesis of patterns): at the end of the file.

Conventions: commenters are named by their LessWrong username, which is public writing; private individuals are not investigated beyond what they published. "Davis replies" summarizes his own comments in the thread. Many threads drift off topic; summaries focus on responses to the post and to Davis.

---

## Part A: LessWrong comment threads

### 2009-11-06 · News: Improbable Coincidence Slows LHC Repairs
- Path: `reception_data/lw_threads/2009-11-06_news-improbable-coincidence-slows-lhc-repairs.md` · 28 comments (Davis 1) · https://www.lesswrong.com/posts/y24ue9LLJdTmpPZnz/news-improbable-coincidence-slows-lhc-repairs
- Summary: Light thread. Jokes (Yudkowsky: "WAKE UP SHEEPHYSICISTS!"), plus a long Jack vs. Zachary_Kurtz exchange on whether repeated LHC failures could be Bayesian evidence for many-worlds/anthropic effects. Davis's one comment applies the "scales of justice" fallacy to the expectation that expensive tech should be sturdy; Jack and SilasBarta answer that the commenter's point was about a missed failure mode, not that fallacy. Not reception of Davis's ideas; it records his early participation.
- Respondents: Furcas, Jack, SilasBarta, RobinZ, cousin_it, Eliezer_Yudkowsky, Nick_Tarleton, Zachary_Kurtz, AllanCrossman.

### 2010-01-07 · Rationality Quotes January 2010
- Path: `reception_data/lw_threads/2010-01-07_rationality-quotes-january-2010.md` · 143 comments (Davis 8) · https://www.lesswrong.com/posts/LiaogK2NWgcLthcrM/rationality-quotes-january-2010
- Summary: A monthly community quotes thread that Davis happened to host; the comments are other users' quotes, not reception of his work. Only Davis's own comments were read in detail. They contribute quotes from John Holt (arithmetic as "a fact of *nature*"), Walt Whitman, Mark Jason Dominus, and *A Charlie Brown Christmas*. The Linus quote went to −7, and Davis defended it as illustrating that "if a religious quote also demonstrates something true or useful, the irrationality of the source doesn't matter". An early instance of his stance of judging claims apart from their source.
- Quotes:
- (https://www.lesswrong.com/posts/LiaogK2NWgcLthcrM/rationality-quotes-january-2010?commentId=Ta8kaRo9WygZ9sD7c, Davis)
> Of course Christianity is false, but if a religious quote also demonstrates something true or useful, the [irrationality of the source doesn't matter](http://wiki.lesswrong.com/wiki/Reversed_stupidity_is_not_intelligence).

### 2017-03-06 · Dreaming of Political Bayescraft
- Path: `reception_data/lw_threads/2017-03-06_dreaming-of-political-bayescraft.md` · 49 comments (Davis 9) · https://www.lesswrong.com/posts/ZhQQgmpvYC6an3Mym/dreaming-of-political-bayescraft
- Summary: (LW link post to the AAL 2017 post.) Lumifer objects that "genuinely appealing to some feature of human psychology" isn't benevolence (the joy of crushing enemies). Davis answers that such joy isn't "stable under reflection", which leads to a long Lumifer–gjm debate on violence and human nature (Pinker). Dagon calls "Being smart is more important than being good (for humans)" "Scary wrong" because smart and good are multiplicative. Davis's highest-karma comment (16) is about learning from a despised ideology's literature. Sarunas and later abramdemski (2019, 9 karma) worry that loyalty to the "underlying feature of human psychology" rather than to ideas tips away from accuracy (citing Hoffman on authenticity vs. accuracy). Mixed-to-skeptical reception; this is the period just after the Feb 2017 crisis.
- Respondents: Lumifer, gjm, komponisto, username2, Dagon, DryHeap, Sarunas, abramdemski, fubarobfusco.
- Quotes:
- (https://www.lesswrong.com/posts/ZhQQgmpvYC6an3Mym/dreaming-of-political-bayescraft?commentId=fvLKZSFkgfW4fxBad, Dagon, 14 karma)
> Scary wrong. Smart and good are multiplicative factors. The most important one is whichever you can improve by a higher percentage.
- (https://www.lesswrong.com/posts/ZhQQgmpvYC6an3Mym/dreaming-of-political-bayescraft?commentId=nzJjacKqYa3WYjbep, Davis, 16 karma)
> It turns out that my current peer group does not have a magical monopoly on goodness! It even turns out that being two or three standard deviations from the mean in intelligence does not give us a magical monopoly on goodness! I didn't notice this until very recently!
- (https://www.lesswrong.com/posts/ZhQQgmpvYC6an3Mym/dreaming-of-political-bayescraft?commentId=CNYYNhs29yRQpWrhv, abramdemski, 9 karma, 2019)
> Authenticity and accuracy are both valuable, and it would be best to reconcile them. But, my concern is that your advice against being loyal to an idea tips things away from accuracy.

### 2017-03-09 · An Intuition on the Bayes-Structural Justification for Free Speech Norms
- Path: `reception_data/lw_threads/2017-03-09_an-intuition-on-the-bayes-structural-justification-for-free.md` · 5 comments (Davis 1) · https://www.lesswrong.com/posts/ZgYGEx2CcKq9viDzF/an-intuition-on-the-bayes-structural-justification-for-free
- Summary: Small, engaged thread. Gram_Stone connects the idea to research on group hypothesis generation ("synthetic groups"). tristanm points out that agents have incentives to control information flow, more so as society polarizes. MrMind says social coordination isn't always zero-sum. DanB complains about style ("five hyphenated words"), and Davis replies "Yes."

### 2017-05-06 · Change
- Path: `reception_data/lw_threads/2017-05-06_change.md` · 10 comments (Davis 3) · https://www.lesswrong.com/posts/bur66BzXt5HDuCr4B/change
- Summary: (LW link post to AAL 2017 "Change".) Hostile: 9eB1 finds it "incomprehensible". SquirrelInHell (−4) advises deleting the post and thinking "deeply about your life", and later explains he sees "deep underlying problems with social adaptation". Raemon (9) rebukes the ridicule as unclear critique. Dagon says the post "has no place on LW" and demeans a non-participant, then edits to allow the misunderstanding may be real. Davis declines to delete ("anti-social"), invites blunt criticism ("stab me with the truth"), and discloses the recent breakdown and "involuntary 'hospitalization'". entirelyuseless notes the irony of Dagon's own misreading. **Early example of LW readers treating Davis's post-crisis writing as socially atypical.**
- Quotes:
- (https://www.lesswrong.com/posts/bur66BzXt5HDuCr4B/change?commentId=eomcrq7JcQZTCY9x3, Raemon, 9 karma)
> -1 to this comment. If you have a critique, you can make it clear what the critique actually is without just ridiculing someone. As is I don't even know what your critique is.
- (https://www.lesswrong.com/posts/bur66BzXt5HDuCr4B/change?commentId=9KmjunPoyL3MGp9oF, Davis)
> Seems kind of anti-social? I'd rather read personal blogs containing the posts that the author thought worth posting at the time, rather than blogs that have been post-publication-selected to exclude the posts that commenters pointed out make the author look bad, which suggests that I should extend the same courtesy to my readers.

### 2019-03-11 · Blegg Mode (linkpost to UUT 2018)
- Path: `reception_data/lw_threads/2019-03-11_blegg-mode.md` · 68 comments (Davis 15) · https://www.lesswrong.com/posts/GEJzPwY8JedcNX2qz/blegg-mode
- Summary: **The first sustained LW reception of the categorization program, and the template for later disputes.**
  - **gjm** (opening and longest critique): the description "seems a little ... disingenuous" because the piece is an allegory about "How To Think About Trans People". Later at length (16 karma): "calling this article 'depoliticized' seems to me like calling Orwell's 'Animal Farm' depoliticized". Its heuristic (new categories for "cheap-to-detect features that correlate with more-expensive-to-detect features that are decision-relevant") "has the look, to me, of a principle that's constructed in order to reach a particular conclusion". Counterexamples: isotopes, enantiomers, supernovae, intersex conditions. Three alternative positions are "not flat-out wrong". "Categories are *somewhat* arbitrary." gjm also hates the "deniable allegory" style (four reasons). **Davis's responses:** accepts the disingenuousness point and adds a content notice ("delusionally expecting to get away with it is trying to have one's cake and eat it, too"). Insists categories are not "somewhat arbitrary" ("We had a whole Sequence about this! Doesn't anyone else _remember_?!"). Argues that people invoke arbitrariness selectively, then **concedes he overstated** ("I should not have written that, because ... it's not true"). Ends thanking gjm for "way _more_ productive" discussion. gjm closes graciously; still finds TCWMFM unpersuasively criticized.
  - **Benquo** (28 karma, the thread's top comment) defends Davis: calling the description disingenuous presupposes "the Rationalist project is so doomed that an attempt to correct a politically motivated epistemic error ... is construed as a political act". Point by point: Davis is responding to "the claim that *because* the usual rule ... is pragmatically motivated, it has no implications for edge cases". "It's offensive to me that there's even a question about this."
  - **Jessica Taylor** (11 karma) offers expectation-maximization as "the mathematically correct thing": Bayesian inference doesn't privilege easy-to-observe features. Davis: "Yeah, I might have been on the wrong track there. (Jessica's comment is _great_! I need to study more!)" gjm agrees with her.
  - **Moderators:** Raemon says the mod team was "not 100% sure how to think about it", since it's innocuous unless you know the politics and then "fairly blatant"; he wants a frontpage policy that doesn't depend on knowing "behind-the-scenes drama". Habryka favors general analogies even when motivated by "mindkilling topics", reports not noticing the subtext, and found the post "moderately useful".
  - **Dagon:** "WTF" once he noticed the allegory; such posts don't belong on LW and should be "an abstraction and generalization, NOT a parable or obfuscation". **vanessa-kosoy:** categories are "at best helpful heuristics", typically fuzzy and overlapping, and the allegory "misses crucial aspects of the original situation and loses the crux of the debate". Davis replies at length with the cluster-structure/configuration-space argument (three clusters after the "adapted bleggs"). **Richard_Kennaway:** "Categories are never arbitrary" (to gjm), and predicted the transsexuality allegory before reading.
- Respondents: gjm, Benquo, jessica.liu.taylor, Dagon, Raemon, habryka4, vanessa-kosoy, Richard_Kennaway.
- Quotes:
- (https://www.lesswrong.com/posts/GEJzPwY8JedcNX2qz/blegg-mode?commentId=mcWMTWTQQAfH8aTBx, gjm)
> The *actual* topic of the piece is clearly the currently hot topic of How To Think About Trans People.
- (https://www.lesswrong.com/posts/GEJzPwY8JedcNX2qz/blegg-mode?commentId=7E2cTPF8oTP9TmZ7T, gjm, 16 karma)
> I'm really not seeing that this heuristic is a particularly good one. It has the look, to me, of a principle that's constructed in order to reach a particular conclusion.
- (https://www.lesswrong.com/posts/GEJzPwY8JedcNX2qz/blegg-mode?commentId=cp2KbiyJq42npohKF, Benquo, 28 karma)
> I downvoted bc the description is disingenuous only if it’s common knowledge that the Rationalist project is so doomed that an attempt to correct a politically motivated epistemic error via an otherwise entirely depoliticized fictional example in a specifically Rationalist space is construed as a political act.
- (https://www.lesswrong.com/posts/GEJzPwY8JedcNX2qz/blegg-mode?commentId=rRW59uDjfQYmSJ7bP, Davis, 9 karma)
> ... you're right. (I like the _aesthetics_ of the "deniable allegory" writing style, but delusionally expecting to get away with it is trying to have one's cake and eat it, too.)
- (https://www.lesswrong.com/posts/GEJzPwY8JedcNX2qz/blegg-mode?commentId=N2W88Tons5ScqQbmQ, Davis)
> No! Categories are _not_ "somewhat arbitrary"! There is _structure_ in the world, and intelligent agents need categories that [carve the structure at the joints](https://www.lesswrong.com/posts/d5NyJ2Lf6N22AD9PB/where-to-draw-the-boundary) so that they can make efficient probabilistic inferences about the variables they're trying to optimize!
- (https://www.lesswrong.com/posts/GEJzPwY8JedcNX2qz/blegg-mode?commentId=kHKmpyrTqx3tyNhGw, Davis, 8 karma)
> I should not have written that, because as you pointed out in [the great-grandparent](https://www.lesswrong.com/posts/GEJzPwY8JedcNX2qz/blegg-mode#wDnx3kqP8bGMLv67C), it's not true.
- (https://www.lesswrong.com/posts/GEJzPwY8JedcNX2qz/blegg-mode?commentId=ZJovvzxE8CbFfWNwq, jessica.liu.taylor, 11 karma)
> However, a Bayesian inference method isn't going to assign special importance to observed features, as it treats the observations as causally downstream of the ontological reality rather than causally upstream of it.
- (https://www.lesswrong.com/posts/GEJzPwY8JedcNX2qz/blegg-mode?commentId=6t5kWvncKjvJnFPrN, Raemon, 10 karma)
> The post itself is sufficiently abstracted that unless you're already aware of the political discussion, it seemed fairly innocuous. Once you're aware of the political discussion it's fairly blatant. It's unclear to me how bad this is.
- (https://www.lesswrong.com/posts/GEJzPwY8JedcNX2qz/blegg-mode?commentId=TJSvkmuzPRmDjZw2Q, vanessa-kosoy)
> Which is to say, I think that this allegory misses crucial aspects of the original situation and loses the crux of the debate.

### 2019-04-13 · Where to Draw the Boundaries?
- Path: `reception_data/lw_threads/2019-04-13_where-to-draw-the-boundaries.md` · 113 comments (Davis 23) · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries
- Summary: **The central LW thread on the categorization program.** It has two phases: April 2019, and the 2019 Review (Dec 2020–Feb 2021).
  - **2019 critics.** *ChristianKl* (Korzybski): the post borrows "the map is not the territory" while ignoring that Korzybski counsels against the "is" of identity. "Ask whether dolphins are fish" violates "beliefs pay rent". Kuhn's helium-is-a-molecule example. CFS vs. SEID. Later, the post is "too vague to be wrong" and full of "applause lights" (−12 on one comment). Davis replies that ChristianKl is "_bizarrely_ demanding", and **bans him from commenting on his posts** (2019-04-21). In 2023 he un-bans him, "persuaded by Said Achmiz's case that we shouldn't actually have that feature". *Wei_Dai* (21): "I don't really understand what you're suggesting here" and asks for concrete examples. Davis offers Scott Alexander's "eargreyish" from the Anti-Reactionary FAQ. Wei counters that "thin"-subspace words are sometimes legitimate. Davis concedes and adds the coral-snake/kingsnake mimicry example. *Dagon*: "carve at the joints" of "something that has no joints"; "Essentialism is wrong". Davis answers that "something like 'essentialism' is actually doing really useful cognitive work" for tightly clustered distributions (the accent example). *romeostevensit*: "Ontologies are built to be thrown away" (Wittgenstein); the post falls prey to what it advises against. *dadadarren* raises Watanabe's ugly duckling theorem; Davis answers with inductive bias. *homotowat* (33) points to distributional semantics.
  - **2019 supporters.** *Benquo*: "something kind of like pragmatism but capable of more robust intersubjective mapmaking". He applies it to the expansion of "AGI" for fundraising. To romeostevensit, he frames the OP as "a decisive legal argument against corruption in front of a corrupt court" and says "LW's corruption is not common knowledge". *SaidAchmiz* (44, the thread's top comment): "an excellent post", with Sequences-like obviousness-in-retrospect; he is puzzled by the "reflexive contrarianness and pedanticism". *habryka* rebukes ChristianKl's "weirdly hostile tone" and finds the poison paragraph clear. *Raemon* (18) gets the core claim but is confused by the rest and by the disputes.
  - **2019 Review phase.** Davis solicits a nomination and frames the post as reconciling Yudkowsky's "Where to Draw the Boundary?" with Alexander's TCWMFM via subspaces. *TAG* argues social constructs (money, marriage, mortgages) need not reflect pre-existing structure; usefulness ≠ correspondence. Davis: "when I say that some concepts are wrong ... I just mean that some concepts are worse than others at making probabilistic predictions". Apparent "compensatory usefulness" must come from deception or wireheading; "it's _not the map's job_ to provide compensatory usefulness". He offers TAG a five-way taxonomy (prediction / coordination / deception / self-fulfilling prophecy / "whoops"). TAG: "Why are (b) and (d) *not* exceptions to your thesis, already?" *Raemon* seconds that: "a pretty gaping hole in your arguments that have something-or-other-to-do-with 'but, like, coordination tho'". Davis points to "Schelling Categories". *abramdemski* gives a long defense of a Schelling fence against appeals to consequences and "pure epistemics"; he concedes self-fulfilling prophecies and goal-relative concepts and admits a possible motte-and-bailey in his own framing. *DanielFilan* argues money isn't freely revaluable by individuals. *Raemon* says the post's conclusion makes him feel his "epistemics are kind of under attack", a motte-and-bailey between rules for thinking and rules for communicating in any context. He also asks why not ground the norm in rule consequentialism. His self-described review: the post does point #1 (non-arbitrariness) well, point #2 decently, and point #3 (wishing something were in a category) in "a meandering vagueblog". *David Hornbein* (16): "crushingly well-argued", and historically significant because "write a nigh-irrefutable argument about philosophy of language, in order to strike at the heart of the substantive disagreement which provoked the social conflict" works in this community. *megasilverfist* (2024) makes a cladistic objection: "fish" is barely natural.
  - Davis (2020-12-22) mentions "coping with the aftermath of a crisis that I'm no longer involved in" (cf. the Dec 2020 events in the corpus).
- Respondents: SaidAchmiz, Benquo, Wei_Dai, ChristianKl, Raemon, habryka4, abramdemski, TAG, Dagon, romeostevensit, dadadarren, homotowat, cousin_it, DanielFilan, David Hornbein, megasilverfist.
- Quotes:
- (https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=T49M7fyizPhrLZMnL, SaidAchmiz, 44 karma)
> This is an excellent post. It has that rare quality, like much of the Sequences, of the ideas it describes being utterly obvious—in retrospect.
- (https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=SGTZmSkTB479Mzc49, Wei_Dai, 21 karma)
> I don't really understand what you're suggesting here. Do you think this advice is applicable to any of the above examples of naming / drawing boundaries?
- (https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=4yHu75kHwDbuKirEA, Benquo, 21 karma)
> This is a nice crisp summary of something kind of like pragmatism but capable of more robust intersubjective mapmaking:
- (https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=QbF8MzMtpGr4aRPGN, Benquo, 13 karma)
> It seems to me like the OP is motivated by a desire to improve decisionmaking processes by making a decisive legal argument against corruption in front of a corrupt court, and that this is an inefficient way of coordinating to move people who are reachable to a better equilibrium.
- (https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=Gn2RR4daCE58xZeAY, Dagon)
> I worry that we're spending a LOT of energy on trying to "carve at the joints" of something that has no joints, or is so deep that the joints don't exist in the dimensions we perceive.
- (https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=MfQWpFJqSgt7hp7k7, Davis, 19 karma)
> You're being _bizarrely_ demanding, and I don't understand why. Have I done something to offend you somehow?
- (https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=sTFzPW3v4rjMwNedw, Davis, 18 karma)
> Unfortunately, I don't think your participation here has been a net-positive for the value of the comments section, and (with some sadness) I have decided to add you to the "Banned Users" list in the moderation section of my account settings.
- (https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=Xr4Sx7JrZwf74ECvL, Davis)
> Similarly, but even more fundamentally, it's _not the map's job_ to provide compensatory usefulness; the map's job is to reflect the territory.
- (https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=WFb4c8NQN3a6mLq8v, TAG)
> Why are (b) and (d) *not* exceptions to your thesis, already?
- (https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=vXcM5mgRtfA9WZzTd, Raemon)
> But I currently feel like there's a pretty gaping hole in your arguments that have something-or-other-to-do-with "but, like, coordination tho")
- (https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=ChHT4n4yEivsCtKh4, Raemon, 14 karma)
> I feel like this statement is motte-and-bailey-ing between "These are the rules of thinking rationally, for forming accurate beliefs, and for communicating about that in particular contexts" and "these are the rules of communicating, in whatever circumstances you might find yourself."
- (https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=v59auE2KQPgwPmx7t, Raemon, 18 karma)
> In particular, these 2.5 paragraphs feel like a meandering vagueblog.
- (https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=QhNmc3uFLrLkKrX3b, David Hornbein, 16 karma)
> I think it's very important that "write a nigh-irrefutable argument about philosophy of language, in order to strike at the heart of the substantive disagreement which provoked the social conflict" is an effective social move in this community.
- (https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=GpAJ6Pxdcm8aL7tp8, abramdemski)
> I perceive some reactions to Zack's post as isolated demands for rigor, invoking the entire justificatory chain to consequentialism when it would not be similarly invoked for a post about, say, p-values.

### 2019-05-20 · Minimax Search and the Structure of Cognition!
- Path: `reception_data/lw_threads/2019-05-20_minimax-search-and-the-structure-of-cognition.md` · 0 comments · https://www.lesswrong.com/posts/daX8otwDnTxw8FeSK/minimax-search-and-the-structure-of-cognition
- Summary: No comments.

### 2019-06-01 · "But It Doesn't Matter"
- Path: `reception_data/lw_threads/2019-06-01_but-it-doesn-t-matter.md` · 17 comments (Davis 1) · https://www.lesswrong.com/posts/NG4XQEL5PTyguDMff/but-it-doesn-t-matter
- Summary: Davis notes the post is adapted from a 14 Jan 2017 Facebook status. **Objection: bounded attention.** John_Maxwell_IV (22): "Sounds like an argument for reading more celebrity gossip". Celer and GuySrinivasan: dismissing questions as non-decision-relevant is legitimate value-of-information practice. Vladimir_Nesov first agreed, then retracted after steven0461's reading. Richard_Kennaway (0): "a series of non sequiturs backed up only by italics and exclamation marks". **Supporting readings:** steven0461 (15) and Benquo (18) identify the real target. The "Even if H is true" construction signals motivated dismissal of evidence for H; steven0461 calls it a pattern of alternating between claiming H matters and claiming it doesn't. philh distinguishes "doesn't matter" from "not a crux". gworley offers the dominance (single-issue voter) exception. Davis does not engage.
- Quotes:
- (https://www.lesswrong.com/posts/NG4XQEL5PTyguDMff/but-it-doesn-t-matter?commentId=QvifeqhWGDDizGurP, steven0461, 15 karma)
> I think Zack is pointing at a real pattern, where the same person will alternate between suggesting it matters that H is true, and, when confronted with evidence against H, suggesting it doesn't matter whether or not H is true, as an excuse not to change the habit of saying or thinking H.
- (https://www.lesswrong.com/posts/NG4XQEL5PTyguDMff/but-it-doesn-t-matter?commentId=S8oLCErzQzATiwGJw, Benquo, 18 karma)
> But the specific wording here is a tell that you're motivated to dismiss Hypothesis H because there's evidence that it's *true*, which is in tension with the claim that it's not important whether it's true.

### 2019-06-11 · Tal Yarkoni: No, it's not The Incentives—it's you (linkpost)
- Path: `reception_data/lw_threads/2019-06-11_tal-yarkoni-no-it-s-not-the-incentives-it-s-you.md` · 119 comments (Davis 3) · https://www.lesswrong.com/posts/5nH5Qtax9ae8CQjZ9/tal-yarkoni-no-it-s-not-the-incentives-it-s-you
- Summary: A linkpost to Yarkoni's 2018 blog post. **The discussion is reception of Yarkoni's thesis, not of Davis's writing**, but the thread is a major 2019 LW controversy among Davis's interlocutors (Zvi, Benquo, Jessica Taylor, Raemon) on honesty norms. It is the background to the 2019 "truth-telling" cluster of Davis's posts.
  - The fight starts with Raemon's "Try to be in the top 50% of the population at morality" and his comparison of data-faking with meat-eating. Zvi (38): "I would rather you *literally go around robbing banks at gunpoint* to pay your rent." dxu: if incentives point that way, "it's *also* bad to call people out for doing it." Zvi (51): "No. No. Big No. A thousand times no", calling this "*the* crux". catherio offers a blameless-postmortem steelman. Lara_Foster (39) argues scientific fraud is worse than ordinary scamming.
  - Empirical correctives: rohinmshah says most academics aren't explicitly committing fraud and imitation explains the rest. CarlShulman (52, the thread's top comment) cites survey data: QRPs were common but a substantial minority avoided them.
  - 2019 Review: rohinmshah (36) gives a point-by-point rejection of Yarkoni ("I do not like this post"). habryka agrees but says truth-seeking institutions are special. Raemon (20, 25) restates the "pro" side's claims (including "Epistemics are the most important thing"). He says the discussion "actively changed my mind" toward epistemics being "plausibly the very top cause", and he tells the "It was me" anecdote.
  - **Davis's comments:** (1) to Raemon's claim that unilateral honesty "isn't actually going to help", that it could only be true in "some sort of hyper-Malthusian setting"; (2) quoting Yarkoni's own reply about speeding; (3) questioning whether a linkpost is eligible for the Review.
- Respondents (main): Zvi, Benquo, Raemon, dxu, catherio, rohinmshah, CarlShulman, Lara_Foster, jessica.liu.taylor, habryka4, Wei_Dai, Bucky, clone of saturn, mr-hire.
- Quotes:
- (https://www.lesswrong.com/posts/5nH5Qtax9ae8CQjZ9/tal-yarkoni-no-it-s-not-the-incentives-it-s-you?commentId=TZGnvc5fsgqgWRsYE, Davis, 5 karma)
> I could imagine this being true in some sort of hyper-Malthusian setting where any deviation from the Nash equilibrium gets you immediately killed and replaced with an otherwise-identical agent who will play the Nash equilibrium.
- (https://www.lesswrong.com/posts/5nH5Qtax9ae8CQjZ9/tal-yarkoni-no-it-s-not-the-incentives-it-s-you?commentId=Fyv7bD5eR7ER2hYbG, Zvi, 51 karma)
> I believe the above quote is a hugely important crux. Likely it, or something upstream of it, is *the* crux.
- (https://www.lesswrong.com/posts/5nH5Qtax9ae8CQjZ9/tal-yarkoni-no-it-s-not-the-incentives-it-s-you?commentId=naqkFQuaTAKXiAcEg, Raemon, 20 karma)
> ***Re: Epistemics are Most Important Thing:*** The previous discussion actively changed my mind on this.

### 2019-06-15 · The Univariate Fallacy
- Path: `reception_data/lw_threads/2019-06-15_the-univariate-fallacy-1.md` · 15 comments (Davis 6) · https://www.lesswrong.com/posts/cu7YY7WdgJBs3DpmJ/the-univariate-fallacy-1
- Summary: Friendly and technical. **DavidHolmes:** in the illustrated example, a linear projection separates the classes, so "it looks just like a problem of bad coordinate choice". Non-linear separations (spheres) need other tools. Davis calls this "a really important point" and answers that some bases are more "fundamental" or interpretable for real-world measurements (stem length and petal color). **John_Maxwell_IV:** "Good post", but it assumes the clusters it needs to prove, and cluster existence is a "choice of ontology" question. Davis accepts the "i.i.d." wording fix. Lignisse disputes that fix. **SaidAchmiz** on Unicode vs. LaTeX. army1987 (2024) recalls a Wikipedia figure, and Davis links it. Davis on DavidHolmes's apology: "it doesn't matter whether _you_ think it, right? It matters whether it's _true_."
- Quotes:
- (https://www.lesswrong.com/posts/cu7YY7WdgJBs3DpmJ/the-univariate-fallacy-1?commentId=Yeq27hH6tBCHjmrwy, DavidHolmes, 9 karma)
> Projecting onto any 1-dimensional subspace orthogonal to this (there is a unique one through the origin) will thus yield a `variable' which cleanly separates the two points into the red and blue categories. So in the illustrated example, it looks just like a problem of bad coordinate choice.
- (https://www.lesswrong.com/posts/cu7YY7WdgJBs3DpmJ/the-univariate-fallacy-1?commentId=EFPZs2jQJpiSqycdK, John_Maxwell_IV, 12 karma)
> If the question is the existence or nonexistence of particular clusters, you are essentially assuming what you need to prove in this post.

### 2019-06-26 · What does the word "collaborative" mean in the phrase "collaborative truthseeking"?
- Path: `reception_data/gw_threads/2019-06-26_what-does-the-word-collaborative-mean-in-the-phrase.md` · 23 comments incl. answers (Davis 3) · https://www.lesswrong.com/posts/uvqd3YiBcrPxXzxQM/what-does-the-word-collaborative-mean-in-the-phrase
- Summary: (A question post; the GraphQL dump returned only the 6 non-answer comments, so the thread was re-fetched from GreaterWrong. See the Part A header.) Adapted from a 4 May 2017 Facebook status. **Answers:**
  - *Viliam* (33): collaborative truthseeking is when caring about truth is "common knowledge" among participants.
  - *Vaniver* (22) contrasts it with competitive or self-only truthseeking. "Collaborative" means done for both parties' benefit and building trust.
  - *gjm* (18) finds the answer obvious: "working together", with groupthink as the risk.
  - *Elo* (16) contrasts collaborative ("I don't know if that's true, what about x") with adversarial ("you're wrong because of x") cultures, and says "99% of either is fine".
  - **Davis's reply to Elo is the thread's top comment (37).** The two phrasings "mean different things"; a culture that forbids "You're wrong because of x" when it's true "is trying to decrease the expressive power of language and is unworthy of the 'rationalist' brand name". "You're wrong about this" and "You are stupid and bad" are "distinct propositions".
  - *Raemon* distinguishes "Adversarial Collaboration", "Adversarial Truthseeking", and "Collaborative Truthseeking" (team product-building, where "You're wrong because X, but Y might work instead" is more useful). *Said Achmiz* (17) asks what to say when you think a teammate is wrong but don't know what would work instead.
  - Richard_Kennaway can't see the perplexity ("ordinary English words that we all know the meanings of"). Dagon would use the phrase ironically at work. tailcalled (2024) gives a long account of collaborative truthseeking as making maps transferable.
  - The GW "what links here" list shows that Davis's later "Aiming for Convergence Is Like Discouraging Betting", "'Justice, Cherryl.'", and "If Clarity Seems Like Death to Them" link back to this question.
- Quotes:
- (https://www.lesswrong.com/posts/uvqd3YiBcrPxXzxQM/what-does-the-word-collaborative-mean-in-the-phrase?commentId=SLZ2WMFeBEqrsCbP4, Davis, 37 karma)
> A culture that expects me to refrain from saying “You’re wrong because of *x*” *even if someone is in fact wrong because of x* (because *telling the truth* about this wouldn’t be “collaborative”) is trying to *decrease the expressive power of language* and is unworthy of the “rationalist” brand name.
- (https://www.lesswrong.com/posts/uvqd3YiBcrPxXzxQM/what-does-the-word-collaborative-mean-in-the-phrase?commentId=sQAvj4fww5GPef8wL, Elo, 16 karma)
> Culturally 99% of either is fine as long as all parties agree on the culture and act like it.

### 2019-06-29 · Being Wrong Doesn't Mean You're Stupid and Bad (Probably)
- Path: `reception_data/lw_threads/2019-06-29_being-wrong-doesn-t-mean-you-re-stupid-and-bad-probably.md` · 5 comments (Davis 1) · https://www.lesswrong.com/posts/6dmKBjc7XarcQMRYW/being-wrong-doesn-t-mean-you-re-stupid-and-bad-probably
- Summary: bendini lists six assumptions he thinks are false (community cultural baggage, base rates, imprecise definitions, salience, the tech-conference suit thought experiment). Davis replies sharply: "remind me why I'm supposed to care what some Bay Area robot cult thinks?" He calls the definitional point "an isolated demand for rigor". He says the 0.42% update is correct by definition: "Was there ever an 'inside', really? I thought there was. I think I was wrong." Raemon: useful for internalized shame, not for anxiety about social punishment. steven0461 (14): how someone reached an opinion can be strong evidence of being stupid and bad; "Arguably over half the arguments one encounters in the wild could never be made in good faith."
- Quotes:
- (https://www.lesswrong.com/posts/6dmKBjc7XarcQMRYW/being-wrong-doesn-t-mean-you-re-stupid-and-bad-probably?commentId=2LvgA7LAi3XYRunQi, Davis, 9 karma)
> Uh, remind me why I'm supposed to care what some Bay Area robot cult thinks?
- (https://www.lesswrong.com/posts/6dmKBjc7XarcQMRYW/being-wrong-doesn-t-mean-you-re-stupid-and-bad-probably?commentId=hr6SCaJSyvKyrWDBt, Raemon, 12 karma)
> One note is that the framing here looks potentially useful to address internalized shame over being wrong, but not anxiety over being socially punished.

### 2019-08-06 · Status 451 on Diagnosis: Russell Aphasia (linkpost)
- Path: `reception_data/lw_threads/2019-08-06_status-451-on-diagnosis-russell-aphasia.md` · 1 comment · https://www.lesswrong.com/posts/etAZs3QG8LZwm4bTB/status-451-on-diagnosis-russell-aphasia
- Summary: shminux on the quoted "reporting" vs. "doxing" line: "I'm yet to see a culture that **can** do it."

### 2019-08-26 · Schelling Categories, and Simple Membership Tests
- Path: `reception_data/lw_threads/2019-08-26_schelling-categories-and-simple-membership-tests.md` · 10 comments (Davis 1) · https://www.lesswrong.com/posts/edEXi4SpkXfvaX42j/schelling-categories-and-simple-membership-tests
- Summary: Small, positive-to-constructive. Dagon: "I really appreciate the clarity of including both the math and the good examples". He asks what makes the observation limits binding, and says choosing level of detail matters more than "picking the actual sharp lines". zulupineapple (11) separates three concerns (no communication, coordination, costly observation) and says only the first is really Schelling. He finds the examples half too long. philh answers TurnTrout's confusion. Raemon appreciates the tie-ins with Schelling points and Goodhart; in 2021 (Boundaries thread) he says he regrets not nominating it. rudi-c (2020) objects to link-heavy style without summaries.
- Quotes:
- (https://www.lesswrong.com/posts/edEXi4SpkXfvaX42j/schelling-categories-and-simple-membership-tests?commentId=a4dceHPMj9q2HDp5j, zulupineapple, 11 karma)
> I don't think 2 and 3 have much to do with Shelling. These considerations reward simplicity. The simplest classifier and the Shelling point of a classification problem don't have to be the same thing (though they might).

### 2019-09-24 · Heads I Win, Tails?—Never Heard of Her; Or, Selective Reporting and the Tragedy of the Green Rationalists
- Path: `reception_data/lw_threads/2019-09-24_heads-i-win-tails-never-heard-of-her-or-selective-reporting.md` · 40 comments (Davis 4) · https://www.lesswrong.com/posts/DoPo4PDjgSySquHX8/heads-i-win-tails-never-heard-of-her-or-selective-reporting
- Summary: **Davis's best-received LW post of 2019 by tone of response; curated.**
  - Praise: Davis_Kingsley ("probably the best post I have read on LessWrong in a long time"). Benito curates it; he likes the "nearby Everett branch" line, but is unsure about the entropy quantification. Raemon (35) calls it "well-put together", likes "blatant cherrypicking is the best kind", and offers his own "cherry-picking-algorithm" disclosure: he avoids gender and social-justice topics online. His 2021 follow-up admits "a little bit of 'Ray is just being cowardly here'". daniel-kokotajlo (2020): improved his understanding of censorship and polarization. hamnox (2021): "Crucial", but "hard to read", "A mathematician's scratch notes".
  - Extensions: DaystarEld (24) says politicians' selectivity is defensible given their goals. vedrfolnir (23) on regimes selecting against "smart, sincere idealists" and the five-way rather than three-way fact typology. hg00 (17) on "distributed circular reasoning". cata: disclosing one's filter is hard in practice. Hivewired (2023): real factions are porous, so a "recursive societal waluigi effect" leaks truth.
  - Technical: Optimization Process asks about the entropy calculation; Davis works it, and his 2021 self-review adds it as a footnote. That self-review frames the post as his account of why disagreement is prevalent even though "people usually aren't outright lying". ege-erdil (2021) raises a Laplace-rule objection, then withdraws it after Davis points out the post's discrete prior.
- Quotes:
- (https://www.lesswrong.com/posts/DoPo4PDjgSySquHX8/heads-i-win-tails-never-heard-of-her-or-selective-reporting?commentId=fGB3Pxivdx4o8Bsg6, Davis_Kingsley, 14 karma)
> This post is excellent. It is probably the best post I have read on LessWrong in a long time.
- (https://www.lesswrong.com/posts/DoPo4PDjgSySquHX8/heads-i-win-tails-never-heard-of-her-or-selective-reporting?commentId=TWtRpAqeA77buf4Jz, Raemon, 35 karma)
> I generally avoid talking online about mainstream national political issues (gender and social justice issues in particular) unless they cross a particular threshold for "relevant to EA concerns", or "personally important to me".
- (https://www.lesswrong.com/posts/DoPo4PDjgSySquHX8/heads-i-win-tails-never-heard-of-her-or-selective-reporting?commentId=mrQBXfFir8GW37dWz, Davis, 22 karma, self-review 2021)
> How can it simultaneously be the case that disagreement is ubiquitous, but people [usually aren't outright lying](https://www.lesswrong.com/posts/bSmgPNS6MTJsunTzS/maybe-lying-doesn-t-exist)? Explanation: the "dishonesty" is mostly in the form of motivatedly asking different questions.
- (https://www.lesswrong.com/posts/DoPo4PDjgSySquHX8/heads-i-win-tails-never-heard-of-her-or-selective-reporting?commentId=gN3sc7vQRw6qB7ZZ2, hamnox, 2021)
> But it's hard to read? It has jarring, erratic rhetoric flow; succinct where elaboration is predictably needed, and verbose where it is redundant. A mathematician's scratch notes, I think.

### 2019-10-14 · Maybe Lying Doesn't Exist
- Path: `reception_data/lw_threads/2019-10-14_maybe-lying-doesn-t-exist.md` · 59 comments (Davis 9) · https://www.lesswrong.com/posts/bSmgPNS6MTJsunTzS/maybe-lying-doesn-t-exist
- Summary: **Contains Scott Alexander's (as "Yvain") only direct reply in the LW record so far, and Davis's most aggressive public comment toward him.**
  - **Appeals to consequences in definitions.** *Kaj_Sotala* (16): language is also for coordination ("crime", "crisps"); prediction and coordination framings are each special cases of the other. *SaidAchmiz* (18) answers that "crime" is fully socially determined, unlike "lying". *Wei_Dai* offers "danger" as a better example. Davis says redefining "danger" to spare feelings is "_wireheading_". Wei asks why case-by-case weighing isn't allowed. *Vladimir_Nesov* (15) argues that patching map-making for planning destroys the design. Davis concedes the "Cartesian" theory is incomplete (embedded agency) but says he objects to "choosing to be biased". Asked whether he thinks most people are too irrational to weigh such considerations, he answers "Actually, yes." Wei remains unpersuaded and asks for the longer story.
  - **Folk theory of lying.** *Connor_Flexman* (49, top comment): "Lying clearly exists", with a four-case gradation (10 vs. 20 minutes late); the implicit folk theory already includes motivated "should-have-been-very-easy-to-tell" cases. *Jessica Taylor* (28): "When conscious intent is selectively discouraged more than unconscious intent, the result is rule by unconscious intent." *Wei_Dai* (38) answers with four reasons to blame conscious intent more. He also, by way of test, suggests Jessica has an unconscious motive for her logical slip. She accepts and endorses that norm, and calls her own line hyperbole that was weakly a lie. elityre finds that norm "crazy" between strangers. Jessica: "Law fought fraud, and fraud won"; "Truth and reconciliation". Legal-doctrine asides on "knew or should have known" (Kaj, abramdemski, howie-lempel).
  - **Yvain/Scott Alexander (40, 2019-12-22).** "'Appeal to consequences' is only a fallacy in reasoning about factual states of the world". Language "has many free variables", so the choices are made on consequences. Most people take "liar" to mean intentional; he groups intentional deception apart from unintentional deception and honesty; "we already have the word 'bias'". Jessica cites "Bad intent is a disposition, not a feeling" and rejects "ordinary language philosophy, which canonizes popular confusions".
  - **Davis's reply (2019-12-25):** "Scott, I appreciate the appearance of effort, but I'm afraid I just can't muster the willpower to engage if you're going to motivatedly play dumb like this." He gives a joke memoir title ending "You Lying Motherfuckers". Two follow-ups acknowledge it as "hugely inappropriately socially aggressive", justified as "true and necessary". Scott (36): "I absolutely deny I am 'motivatedly playing dumb'", and "I can't figure out where we start differing". Davis (21) the next day: "Scott and I had a good conversation today", and he plans a post on "Instrumental Categories, Wireheading, and War".
  - Later: Kenny's satirical insult to defend tone-policing; quwgri (2024) on hypotheses vs. proposals; a deleted user (2025): appeals to consequences are valid for "which things are or are not good to do", including definitions.
- Quotes:
- (https://www.lesswrong.com/posts/bSmgPNS6MTJsunTzS/maybe-lying-doesn-t-exist?commentId=HjuAdEpjKm3hX88qd, Connor_Flexman, 49 karma)
> The folk theory of lying is a tiny bit wrong and I agree it should be patched. I definitely do not agree we should throw it out, or be uncertain whether lying exists.
- (https://www.lesswrong.com/posts/bSmgPNS6MTJsunTzS/maybe-lying-doesn-t-exist?commentId=isJTLTLaLgdbMcPpQ, jessica.liu.taylor, 28 karma)
> When conscious intent is selectively discouraged more than unconscious intent, the result is rule by unconscious intent.
- (https://www.lesswrong.com/posts/bSmgPNS6MTJsunTzS/maybe-lying-doesn-t-exist?commentId=3NEG3887FjQcBaaLS, Davis, 13 karma)
> That kind of utilitarianism might (or might not) be a good reason to _not tell_ people about the danger, but it's not a good reason to change the definition of "danger" itself. Why? Because from the perspective of "language as AI design", that would be _wireheading_.
- (https://www.lesswrong.com/posts/bSmgPNS6MTJsunTzS/maybe-lying-doesn-t-exist?commentId=LJp2PYh3XvmoCgS6E, Yvain, 40 karma)
> "Appeal to consequences" is only a fallacy in reasoning about factual states of the world. In most cases, appealing to consequences is the right action.
- (https://www.lesswrong.com/posts/bSmgPNS6MTJsunTzS/maybe-lying-doesn-t-exist?commentId=LJp2PYh3XvmoCgS6E, Yvain, 40 karma)
> Stepping back, we have two short words ("lie" and "not a lie") to describe three states of the world (intentional deception, unintentional deception, complete honesty).
- (https://www.lesswrong.com/posts/bSmgPNS6MTJsunTzS/maybe-lying-doesn-t-exist?commentId=xEan6oCQFDzWKApt7, Davis)
> Scott, I appreciate the appearance of effort, but I'm afraid I just can't muster the willpower to engage if you're going to motivatedly play dumb like this.
- (https://www.lesswrong.com/posts/bSmgPNS6MTJsunTzS/maybe-lying-doesn-t-exist?commentId=s7ZNXYdsrumC7MrzR, Yvain, 36 karma)
> I absolutely deny I am "motivatedly playing dumb" and I enter this into the record as further evidence that we shouldn't redefine language to encode a claim that we are good at ferreting out other people's secret motivations.
- (https://www.lesswrong.com/posts/bSmgPNS6MTJsunTzS/maybe-lying-doesn-t-exist?commentId=wFRtLj2e7epEjhWDH, Davis, 13 karma)
> Like, I know my sibling comment is hugely inappropriately socially aggressive of me, and I don't want to hurt your feelings any more than is necessary to incentivize you to process information, but we've been at this for a _year_!
- (https://www.lesswrong.com/posts/bSmgPNS6MTJsunTzS/maybe-lying-doesn-t-exist?commentId=6RY85nrkD28kodryK, Davis, 21 karma)
> (Scott and I had a good conversation today.

### 2019-10-19 · Algorithms of Deception!
- Path: `reception_data/lw_threads/2019-10-19_algorithms-of-deception.md` · 7 comments (Davis 0) · https://www.lesswrong.com/posts/fmA2GJwZzYtkrAKYJ/algorithms-of-deception
- Summary: Small. artifex: category gerrymandering isn't a different algorithm from selective reporting. romeostevensit: "sincerity is selected for". Isnasene: ask reporters to be specific about their goals. Pongo (12, 2020): the algorithms are "adversarially crafted for one's belief-forming mechanisms". Davis doesn't reply.

### 2019-11-26 · Curtis Yarvin on A Theory of Pervasive Error (linkpost)
- Path: `reception_data/lw_threads/2019-11-26_curtis-yarvin-on-a-theory-of-pervasive-error.md` · 6 comments (Davis 1) · https://www.lesswrong.com/posts/jPb9v4oprTpfTbNC3/curtis-yarvin-on-a-theory-of-pervasive-error
- Summary: ESRogs questions introducing Yarvin as Urbit's author rather than as a founder of neoreaction. Davis explains the "very deliberate editorial choice": a joke for informed readers ("Arson, Murder, and Jaywalking"), plus avoiding "the 'neoreaction' marketing keyword" so that readers afraid of "right-wing Bad Guy cooties" would evaluate the essay "on the merits". He was "a little bit worried that someone would accuse me of dishonesty".
- Quotes:
- (https://www.lesswrong.com/posts/jPb9v4oprTpfTbNC3/curtis-yarvin-on-a-theory-of-pervasive-error?commentId=F4Bg45nzFhkJGjtcj, Davis, 5 karma)
> I was actually a little bit worried that someone would accuse me of dishonesty for not mentioning NRx in my summary, but ultimately decided I would be prepared to defend the stance that the "Content notice" at the top was enough to satisfy the demands of our local anti-politics norms.

### 2019-11-22 · Relevance Norms; Or, Gricean Implicature Queers the Decoupling/Contextualizing Binary
- Path: `reception_data/lw_threads/2019-11-22_relevance-norms-or-gricean-implicature-queers-the-decoupling.md` · 30 comments (Davis 6) · https://www.lesswrong.com/posts/GSz8SrKFfW7fJK2wN/relevance-norms-or-gricean-implicature-queers-the-decoupling
- Summary:
  - **2019.** Chris_Leong proposes a spectrum rather than a dichotomy. Davis (26) answers with Geraldine and Paulette (eye-color coalitions): what matters is *which* context people consider relevant, and motivated reasoning governs that. mr-hire: the D/C posts aren't about implicature but about consequences and how statements get used. Dagon: "THANK YOU" for treating these as communication tactics, not personal styles. cousin_it (18) offers his own line: engineer/politician/fanatic reactions to disagreement. Raemon (9) finds it helpful, but is surprised that Davis frames it as a rebuttal given his praise of "Local Validity"; he reads it as "Yes, and". Davis promises "an ultra-'contextualizing' reply to 'Meta-Honesty'".
  - **2019 Review.** Vaniver: of Davis's 2019 posts, "this was the one I liked the most at the time", likely "changed the discourse afterwards for the better". habryka: "gave specific words to a problem I've run into many times". Zvi argues for inclusion against Davis's own self-review: Davis "_oppose[s]_" inclusion as a "defensive" post. **mr-hire's review (14) is a critique of the whole sequence.** It says the post highlights "biases and implicit assumptions" running through the whole sequence. Davis's contextualizer is "a straw man"; the sequence is "quite idealistic" and ignores language's motivational, affective, and quotational uses, and the "whole set of powerful consequentialist arguments". orthonormal (13): "Ironically ... you're asserting that even though this post is reasonable when decoupled from the rest of the sequence, it's worrisome when contextualized." Raemon: "I think I probably agree with the overall thrust of your criticism", but he prefers post-level critique, and says he has "learned a bunch from watching him follow this train of thought". mr-hire cites the integral/Wilber community as a cautionary case.
- Quotes:
- (https://www.lesswrong.com/posts/GSz8SrKFfW7fJK2wN/relevance-norms-or-gricean-implicature-queers-the-decoupling?commentId=jh6yJamZHWZHY7Aa3, Davis, 26 karma)
> I'm saying we should look at _which_ context people consider relevant, not the _amount_ of contextualizing they want.
- (https://www.lesswrong.com/posts/GSz8SrKFfW7fJK2wN/relevance-norms-or-gricean-implicature-queers-the-decoupling?commentId=6mDrcNKr7wpDesNap, Vaniver)
> It points clearly at a confusion underlying a common dichotomy, in a way that I think probably changed the discourse afterwards for the better.
- (https://www.lesswrong.com/posts/GSz8SrKFfW7fJK2wN/relevance-norms-or-gricean-implicature-queers-the-decoupling?commentId=cMpWvbci6v96kPWke, mr-hire, 14 karma)
> And, I believe this is a straw man.   In particular, I believe Zack is being quite idealistic, building up a model of how language should be used, while ignoring the many ways language is actually used in practice.
- (https://www.lesswrong.com/posts/GSz8SrKFfW7fJK2wN/relevance-norms-or-gricean-implicature-queers-the-decoupling?commentId=cKb5hqLskQswpQwyJ, orthonormal, 13 karma)
> Ironically enough for Zack's preferred modality, you're asserting that even though this post is reasonable when decoupled from the rest of the sequence, it's worrisome when contextualized.
- (https://www.lesswrong.com/posts/GSz8SrKFfW7fJK2wN/relevance-norms-or-gricean-implicature-queers-the-decoupling?commentId=poaZCF6nrfLM7eZoC, Raemon, 7 karma)
> But I also think I've learned a bunch from watching him follow this train of thought, and been impressed with how thoroughly he investigates it.

### 2019-12-21 · Free Speech and Triskaidekaphobic Calculators: A Reply to Hubinger on the Relevance of Public Online Discussion to Existential Risk
- Path: `reception_data/lw_threads/2019-12-21_free-speech-and-triskaidekaphobic-calculators-a-reply-to.md` · 26 comments (Davis 5) · https://www.lesswrong.com/posts/yaCwW8nPQeJknbCgf/free-speech-and-triskaidekaphobic-calculators-a-reply-to
- Summary: **Second direct exchange with Scott Alexander (Yvain), plus the targeted party's reply.**
  - *evhub* (Hubinger, 20) declines to debate online and says his position is "_certainly_ not 'assume what you're doing is the most important thing and run with it'", only that hot-button issues be discussed offline. *Wei_Dai* (41) says Davis is "straw-manning Evan", and asks whether Davis wants politics on LW "without giving any weight to taintedness". Davis: "No"; the post "was written hastily", and he favors separate forums and pseudonyms plus "mutual defense pact" norms.
  - *Yvain* (58, the thread's top comment) distinguishes two calculators: a normal one with an error message at 13, vs. a new mathematics that never yields 13. He argues not discussing taboo topics on LW is the first kind. *interstice* (23): that works only if you already understand addition; we're confused about preferences and minds, and taboo data matters.
  - **Davis's reply (47):** supports "Take it to /r/TheMotte" but not "Take it _offline_" ("Permalink or It Didn't Happen"). Triskaidekaphobia breaks associativity and the "infinite family" of expressions with 13 as an intermediate. He is suspicious of the "Unilateralist's Curse" as "an excuse for groupthink" and proposes a "Unilateralist's Blessing". A footnote announces that he has "reached the point of pseudo-ragequitting the so-called 'rationalist' community". Another footnote says his "Do your worst, you motherfuckers!" disposition, not decision theory, explains his stance.
  - *Yvain* (23, 2020): psychology is bad because "the actual triskaidekaphobics are the ones inventing the psychology theories"; academics who appease in public "get everything 100% right" in private. Davis (35): "Getting the right answer in private can only help those you talk to in private." *steven0461*: AI risk was "always obviously potentially important". Davis replies that the community would then be working on eugenics.
  - Others: Benito on ideas that "pull the rope sideways". Charlie Steiner: talking about gender on LW was "good ... as a political act". Viliam: "Both sides make good points. One side being Zack, and the other side being everyone else." clone of saturn on rationalists not punishing betrayal.
- Quotes:
- (https://www.lesswrong.com/posts/yaCwW8nPQeJknbCgf/free-speech-and-triskaidekaphobic-calculators-a-reply-to?commentId=JdsknCuCuZMAo8EbP, Yvain, 58 karma)
> It sounds like the proposal you're arguing against (and which I want to argue for) - not talking about taboo political issues on LW - is basically (1).
- (https://www.lesswrong.com/posts/yaCwW8nPQeJknbCgf/free-speech-and-triskaidekaphobic-calculators-a-reply-to?commentId=MbGPumsPaGBdB8peA, Wei_Dai, 41 karma)
> This seems to be straw-manning Evan.
- (https://www.lesswrong.com/posts/yaCwW8nPQeJknbCgf/free-speech-and-triskaidekaphobic-calculators-a-reply-to?commentId=JRPxnwfnhGv6kvG8G, evhub, 20 karma)
> At the very least, though, I think it's worth clarifying that my position is _certainly_ not "assume what you're doing is the most important thing and run with it."
- (https://www.lesswrong.com/posts/yaCwW8nPQeJknbCgf/free-speech-and-triskaidekaphobic-calculators-a-reply-to?commentId=oY8QX9qc6gE9esBBm, Davis, 47 karma)
> The operative principle here is "Permalink or It Didn't Happen": if it's not online, does it really exist?
- (https://www.lesswrong.com/posts/yaCwW8nPQeJknbCgf/free-speech-and-triskaidekaphobic-calculators-a-reply-to?commentId=oY8QX9qc6gE9esBBm, Davis, 47 karma)
> On consideration, the second person seems more appropriate, because by now I think I've actually reached the point of pseudo-ragequitting the so-called "rationalist" community.
- (https://www.lesswrong.com/posts/yaCwW8nPQeJknbCgf/free-speech-and-triskaidekaphobic-calculators-a-reply-to?commentId=mHrHTvzg8MGNH2CwB, Yvain, 23 karma)
> It's because the actual triskaidekaphobics are the ones inventing the psychology theories. I know a bunch of people in academia who do various verbal gymnastics to appease the triskaidekaphobics, and when you talk to them in private they get everything 100% right.
- (https://www.lesswrong.com/posts/yaCwW8nPQeJknbCgf/free-speech-and-triskaidekaphobic-calculators-a-reply-to?commentId=Pz4ErkTihuKwtD2gC, Davis, 35 karma)
> Getting the right answer in private can only help those you talk to in private.

### 2019-12-24 · Funk-tunul's Legacy; Or, The Legend of the Extortion War
- Path: `reception_data/lw_threads/2019-12-24_funk-tunul-s-legacy-or-the-legend-of-the-extortion-war.md` · 6 comments (Davis 2) · https://www.lesswrong.com/posts/XbXJZjwinkoQXu4db/funk-tunul-s-legacy-or-the-legend-of-the-extortion-war
- Summary: Davis's two author's notes: (1) the story was inspired by three paragraphs from a 15 April 2019 email by Jessica Taylor, quoted without asking, which he jokes about; (2) "A Criminal Confession": one modeling step "is bullshit handwaving on my part". **Isnasene (46, top):** the story's agents are "CDT+being clever" rather than FDT/TDT. Funk-tunul wins by manipulation, not decision theory, and the ceedeetee should just interact with each other. Wei_Dai (8): how do agents tell types apart? He points to cases where TDT/UDT does worse than CDT. liam-donovan shows the defection works with long-term population share as the objective. Dagon: is CDT "a useless strawman"?
- Quotes:
- (https://www.lesswrong.com/posts/XbXJZjwinkoQXu4db/funk-tunul-s-legacy-or-the-legend-of-the-extortion-war?commentId=suaAzP74S8GhFKNoi, Isnasene, 46 karma)
> Funk-tunul isn't winning because of a better decision theory here; she's winning because she's more clever. at manipulating other ceedeetee.

### 2019-12-27 · Firming Up Not-Lying Around Its Edge-Cases Is Less Broadly Useful Than One Might Initially Think
- Path: `reception_data/lw_threads/2019-12-27_firming-up-not-lying-around-its-edge-cases-is-less-broadly.md` · 43 comments (Davis 3) · https://www.lesswrong.com/posts/MN4NRkMw7ggt9587K/firming-up-not-lying-around-its-edge-cases-is-less-broadly
- Summary: **Curated** (Raemon): "one of the major open problems in rationality". Raemon's two criticisms: no crisp summary, and "underwhelming as a critique of Meta-Honesty"; "Zack underestimates how important clear norms around Not-Lying are".
  - *Vaniver* (60, top) brings in Quaker practice via William Penn's *Some Fruits of Solitude* ("misleading is halfway to lying"), and argues that secrecy is distinct from the duty to inform.
  - *Yvain* (37) offers axiology/morality/law: "Don't be misleading" is axiological, "Don't tell lies" is moral, and law is weaker still. The "wizard's oath" is "an attempt to subject one's self to a stricter moral law than usual". Davis (18, 2020) replies that the "not a bad person" line was "mostly a strategic political concession" to avoid derailing. He asks Scott whether "lies committed 'by accident'" concedes Jessica's usage.
  - *quanticle* (38): rarely needing to lie is a privilege of non-adversarial environments. *Viliam* (40): forced peer-review questionnaires at work; reputations for never lying can be destroyed by false accusations.
  - *SaidAchmiz* (28): the "literal truth" project is "wrongheaded" because lying is sometimes mandatory; the Carol/Dave embezzlement puzzle. DanielFilan offers a Christmas board-game lie.
  - *fiddler* (15, Review): the post isn't actually in opposition to Meta-Honesty. Davis's self-review opposes inclusion as a "defensive" post.
  - **Davis (34, 2021-03-03)**: a fable of Cade Metz composing the NYT Scott Alexander story from literally true sentences ("For that was his mastery."). This is the earliest LW appearance of the Metz theme. Benito notes Eliezer's proposal required being "unusually honest" too.
- Quotes:
- (https://www.lesswrong.com/posts/MN4NRkMw7ggt9587K/firming-up-not-lying-around-its-edge-cases-is-less-broadly?commentId=E2rTRnPhSAnHb9e5q, Yvain, 37 karma)
> "Don't be misleading" is an axiological commandment - it's about how to make the world a better place, and what you should hypothetically be aiming for absent other considerations.
- (https://www.lesswrong.com/posts/MN4NRkMw7ggt9587K/firming-up-not-lying-around-its-edge-cases-is-less-broadly?commentId=YHFhDyYnQM38uJYZS, Raemon, 10 karma)
> I think Zack underestimates how important clear norms around Not-Lying are.
- (https://www.lesswrong.com/posts/MN4NRkMw7ggt9587K/firming-up-not-lying-around-its-edge-cases-is-less-broadly?commentId=ijoKLp9ikQFPy4vae, quanticle, 38 karma)
> For others in more adversarial situations, telling lies (or at least shading the truth to the extent that would be considered lying by the standards of this post) is a necessary survival skill.
- (https://www.lesswrong.com/posts/MN4NRkMw7ggt9587K/firming-up-not-lying-around-its-edge-cases-is-less-broadly?commentId=gSKeZ7QJhsADqHXdP, Davis, 18 karma)
> So, from my perspective as an author [(which, you know, could be wrong)](http://unremediatedgender.space/2016/Sep/psychology-is-about-invalidating-peoples-identities/), that line was mostly a strategic political concession

### 2019-12-28 · Stupidity and Dishonesty Explain Each Other Away
- Path: `reception_data/lw_threads/2019-12-28_stupidity-and-dishonesty-explain-each-other-away.md` · 18 comments (Davis 2) · https://www.lesswrong.com/posts/y4bkJTtG3s5d6v36k/stupidity-and-dishonesty-explain-each-other-away
- Summary: Chris_Leong and quanticle point to a loophole: indifference to truth (Frankfurt's "bullshit") yields both. Viliam: dishonest people "get high on their own supply". lorenzo-n: the two-cause model sets "an antogonistic tone" and omits other causes. **Davis (18): "I don't care about not establishing an antagonistic tone to the interaction. I care about achieving the map that reflects the territory."** On defensiveness: "why is that my problem?" Later: "I think I'm just ... not a consequentialist about speech". SaidAchmiz (12) defends this: the purpose of arguing need not be convincing the interlocutor. lorenzo-n: defensiveness makes you less likely to hear good arguments.
- Quotes:
- (https://www.lesswrong.com/posts/y4bkJTtG3s5d6v36k/stupidity-and-dishonesty-explain-each-other-away?commentId=CkGSry8dNrE3aSgod, Davis, 18 karma)
> Yes, that's right, but I don't care about not establishing an antagonistic tone to the interaction. I care about achieving the map that reflects the territory.
- (https://www.lesswrong.com/posts/y4bkJTtG3s5d6v36k/stupidity-and-dishonesty-explain-each-other-away?commentId=Gzri65ajLy3B39rvk, Davis)
> Providing information to the audience would be the main other reason, but the attitude I'm trying to convey more broadly is that I think I'm just ... not a consequentialist about speech?

### 2019-12-30 · Speaking Truth to Power Is a Schelling Point
- Path: `reception_data/lw_threads/2019-12-30_speaking-truth-to-power-is-a-schelling-point.md` · 19 comments (Davis 3) · https://www.lesswrong.com/posts/tCwresAuSvk867rzH/speaking-truth-to-power-is-a-schelling-point
- Summary: Skeptical of the model. *steven0461* (27): "If the slope is so slippery, how come we've been standing on it for over a decade?" Davis (0 karma) says applying it to LW belongs off the frontpage, citing Wei's "hidden agendas" point. *Vaniver* (26): non-extreme equilibria exist (US free-speech exemptions); coordination needn't be blind. *Isnasene* gives a detailed critique of the one-parameter *x*. bendini asks for evidence. *Wei_Dai*: why assume grant money is the only cost? Speaking truths can get "your child bullied", or you "unemployed, jailed, or killed". **Davis concedes his example may be "algorithmically-dishonestly 'rigged'"**: the "elephant in my brain" chose an example favoring forthrightness. He asks for credit only if future posts include counter-narrative examples. He quotes hillsump on r/TheMotte, who calls the text "somewhat incoherent" and possibly a Straussian fable; Davis says that is "_probably not a coincidence_". *Raemon*: there is no available "*x* = ∞" option. SlightlyLessHariyApe cites Aaronson's "Kolmogorov Option" as an intermediate Schelling point.
- Quotes:
- (https://www.lesswrong.com/posts/tCwresAuSvk867rzH/speaking-truth-to-power-is-a-schelling-point?commentId=amfw3f8bTCeLPxCoj, steven0461, 27 karma)
> If the slope is so slippery, how come we've been standing on it for over a decade?
- (https://www.lesswrong.com/posts/tCwresAuSvk867rzH/speaking-truth-to-power-is-a-schelling-point?commentId=bTo3NLbRemWwENMD5, Wei_Dai, 7 karma)
> In the real world (that I think I live in), speaking some truths might get your child bullied in school (including by the teachers or administrators), or get you unemployed, jailed, or killed.
- (https://www.lesswrong.com/posts/tCwresAuSvk867rzH/speaking-truth-to-power-is-a-schelling-point?commentId=S3WDjfrf2RHBbTDn7, Davis, 8 karma)
> But people often do this social move where they _say_ "I should have tried harder" as a way of accepting blame in exchange for not doing work, so you should only give me credit if you actually see me include counter-narrative examples in future posts

### 2020-01-01 · Don't Double-Crux With Suicide Rock
- Path: `reception_data/lw_threads/2020-01-01_don-t-double-crux-with-suicide-rock.md` · 30 comments (Davis 2) · https://www.lesswrong.com/posts/jrLkMFd88b4FRMwC6/don-t-double-crux-with-suicide-rock
- Summary: Mostly about Aumann's theorem's conditions. steven0461 (26): honesty must be common knowledge. Several note the common-prior and fact/value conditions. romeostevensit (29): agreeing to disagree can be resource-rational. Vaniver (40): double-crux would reveal the Rock has no cruxes. **RobinHanson (36):** "You are a bit too quick to allow the reader the presumption that they have more algorithmic faith than the other folks they talk to." Davis: "Everything I'm saying is definitely symmetric across persons"; if your interlocutor is a painted rock, so might *you* be to them. Jessica Taylor: parsing philosophy is evidence of rationality. Hanson: "we are talking about holding people to MUCH higher rationality standards". vanessa-kosoy cites Aaronson's computational version of Aumann.
- Quotes:
- (https://www.lesswrong.com/posts/jrLkMFd88b4FRMwC6/don-t-double-crux-with-suicide-rock?commentId=8dmcbDNrkuiiqJu2o, RobinHanson, 36 karma)
> You are a bit too quick to allow the reader the presumption that they have more algorithmic faith than the other folks they talk to. Yes if you are super rational and they are not, you can ignore them. But how did you come to be confident in that description of the situation?
- (https://www.lesswrong.com/posts/jrLkMFd88b4FRMwC6/don-t-double-crux-with-suicide-rock?commentId=uYNnneitwrhW2gzTf, Davis, 15 karma)
> Everything I'm saying is definitely symmetric across persons, even if, as an author, I prefer to phrase it in the second person.

### 2020-01-04 · Less Wrong Poetry Corner: Walter Raleigh's "The Lie"
- Path: `reception_data/lw_threads/2020-01-04_less-wrong-poetry-corner-walter-raleigh-s-the-lie.md` · 18 comments (Davis 3) · https://www.lesswrong.com/posts/trb9HPWFk8Gy9MBdN/less-wrong-poetry-corner-walter-raleigh-s-the-lie
- Summary: **Yvain (54, top)** recounts Raleigh's El Dorado fraud and execution. The moral: "accusing everyone else of being lying and corrupt can sometimes be a strategy con men use", or it's "really easy to talk yourself into a biased narrative where you are a lone angel in a sea full of corruption". Davis (36) answers with a "Vassarian–Taylorist conflict–mistake synthesis": politics as evolutionary game theory, where courts must punish fraud relative to what one "could have reasonably been expected to know". Scott: that's not how fraud is legally defined; Davis says he wasn't offering a legal opinion. gwern (23): "it may take a thief to catch a thief" (Rosenthal). SaidAchmiz questions the Wikipedia history. *steven0461* (11): "Would your views on speaking truth to power change if the truth were 2x as offensive as you currently think it is?" Davis (21): "For _some_ multiplier, yes". He says he talks in virtue language because "humans _can't_ use consequentialism for this kind of thing". He predicts a culture with "Use Bayesian decision theory to decide whether or not to speak the truth" as its slogan "won't be able to do science", and claims "I've done _field work_". steven0461: "It almost sounds like you're saying we should tell people they should always speak the truth even though it is not the case that people should always speak the truth, because telling people they should always speak the truth has good consequences." mr-hire: "I really appreciate your passion for truth and outing deception, Zack."
- Quotes:
- (https://www.lesswrong.com/posts/trb9HPWFk8Gy9MBdN/less-wrong-poetry-corner-walter-raleigh-s-the-lie?commentId=mQBFZ2aKv9gMYhQ3i, Yvain, 54 karma)
> For conflict theorists, the moral of this story is that accusing everyone else of being lying and corrupt can sometimes be a strategy con men use to deflect suspicion. For mistake theorists, the moral is that it's really easy to talk yourself into a biased narrative where you are a lone angel in a sea full of corruption, and you should try being a little more charitable to other people and a little harsher on yourself.
- (https://www.lesswrong.com/posts/trb9HPWFk8Gy9MBdN/less-wrong-poetry-corner-walter-raleigh-s-the-lie?commentId=ZwPSefpu87DPFjbcd, Davis, 21 karma)
> I _falsifiably predict_ that a culture that has "Use Bayesian decision theory to decide whether or not to speak the truth" as its slogan [won't be able to do science](https://www.lesswrong.com/posts/5nH5Qtax9ae8CQjZ9/no-it-s-not-the-incentives-it-s-you)—Platonically, the math has to exist, but letting humans appeal to Platonic math whenever they want is just _too convenient of an excuse_.
- (https://www.lesswrong.com/posts/trb9HPWFk8Gy9MBdN/less-wrong-poetry-corner-walter-raleigh-s-the-lie?commentId=8JPDYAca2YERBjHS8, steven0461, 12 karma)
> It almost sounds like you're saying we should tell people they should always speak the truth even though it is not the case that people should always speak the truth, because telling people they should always speak the truth has good consequences. Hm!

### 2020-01-21 · Book Review—The Origins of Unfairness: Social Categories and Cultural Evolution
- Path: `reception_data/lw_threads/2020-01-21_book-review-the-origins-of-unfairness-social-categories-and.md` · 5 comments (Davis 2) · https://www.lesswrong.com/posts/5DB4csh8imXjYv4ou/book-review-the-origins-of-unfairness-social-categories-and
- Summary: philh (11): the ballroom-dancing example fails because the convention is downstream of gender roles. Davis points to the book's sections on in-type meetings and "gradient markers", and compares the example to "Hawk–Dove" naming. Wei_Dai: O'Connor's activism conclusion ignores that a fair-and-efficient equilibrium may not exist; he pushes back on Davis's praise of her for not fudging results. Davis proposes alternating by day.

### 2020-02-09 · Relationship Outcomes Are Not Particularly Sensitive to Small Variations in Verbal Ability
- Path: `reception_data/lw_threads/2020-02-09_relationship-outcomes-are-not-particularly-sensitive-to.md` · 2 comments · https://www.lesswrong.com/posts/Ciw8DLJiYnBWa4B7f/relationship-outcomes-are-not-particularly-sensitive-to
- Summary: shminux (25): by the time of a friendship-ending fight, "you must have missed about a dozen of alarm bells". Raemon: ":(".

### 2020-03-09 · The Heckler's Veto Is Also Subject to the Unilateralist's Curse
- Path: `reception_data/lw_threads/2020-03-09_the-heckler-s-veto-is-also-subject-to-the-unilateralist-s.md` · 6 comments (Davis 1) · https://www.lesswrong.com/posts/oREzdHpzaB2RaY2fA/the-heckler-s-veto-is-also-subject-to-the-unilateralist-s
- Summary: jimrandomh (24): karma gives feedback but doesn't undo some harms (doxxing), and expert explanations look like heckler's vetoes. Davidmanheim: communities share dangerous info anyway. Davis: the curse concerns variance in estimates, not systematic community bias. willbradshaw: the veto/act duality is already in Bostrom et al., and pre-readers can vote.

### 2020-03-18 · Zeynep Tufekci on Why Telling People They Don't Need Masks Backfired (linkpost)
- Path: `reception_data/lw_threads/2020-03-18_zeynep-tufekci-on-why-telling-people-they-don-t-need-masks.md` · 9 comments (Davis 0) · https://www.lesswrong.com/posts/tREnA5EvTikWf9Mfw/zeynep-tufekci-on-why-telling-people-they-don-t-need-masks
- Summary: Reception of Tufekci rather than Davis. Nick_Tarleton (41): the "backfired" claim lacks evidence in the article. Benito (19): such headlines are higher-level simulacra trying "to make something true by saying it is". Jayson_Virissimo reports getting flattenthecurve.com to drop its anti-mask section.

### 2020-04-16 · Brief Response to Suspended Reason on Parallels Between Skyrms on Signaling and Yudkowsky on Language and Evidence
- Path: `reception_data/lw_threads/2020-04-16_brief-response-to-suspended-reason-on-parallels-between.md` · 0 comments · https://www.lesswrong.com/posts/3HbbKyudvzCi2DKe6/brief-response-to-suspended-reason-on-parallels-between
- Summary: No comments.

### 2020-04-28 · A Book Review
- Path: `reception_data/lw_threads/2020-04-28_a-book-review.md` · 3 comments · https://www.lesswrong.com/posts/4aHMjJBSDfrkouzaB/a-book-review
- Summary: Viliam on the gender-equality paradox: lower segregation can make group differences more salient. gjm jokes about "occasional weirdly out-of-place *fucking* cuss words".

### 2020-05-11 · Zoom Technologies, Inc. vs. the Efficient Markets Hypothesis
- Path: `reception_data/lw_threads/2020-05-11_zoom-technologies-inc-vs-the-efficient-markets-hypothesis.md` · 47 comments (Davis 0) · https://www.lesswrong.com/posts/tonKatiDTzTP8LrEk/zoom-technologies-inc-vs-the-efficient-markets-hypothesis
- Summary: Mostly a general EMH debate; Davis doesn't comment. AllAmericanBreakfast (28) steelmans the EMH (a tiny cap-weighted error). gwern (40) points to Matt Levine and the importance of follow-up, noting Wei Dai's losses. Wei_Dai (48) says his net 10× still counts against the EMH. richard-meadows-1 (17), via Levine: ticker confusion is "*part of the information*" markets aggregate. clone of saturn (24, 26): "If this kind of behavior is entirely consistent with EMH, does EMH even mean anything?" ESRogs (15) engages Davis's simulacrum-levels paragraph (Keynesian beauty contest; Graham's voting/weighing machine). Closed Limelike Curves: the "Bimodal Market Hypothesis".
- Quotes:
- (https://www.lesswrong.com/posts/tonKatiDTzTP8LrEk/zoom-technologies-inc-vs-the-efficient-markets-hypothesis?commentId=mmcbqW2xSp828cY4b, clone of saturn, 24 karma)
> If this kind of behavior is entirely consistent with EMH, does EMH even mean anything?

### 2020-05-18 · "Starwink" by Alicorn (linkpost)
- Path: `reception_data/lw_threads/2020-05-18_starwink-by-alicorn.md` · 1 comment · https://www.lesswrong.com/posts/bTW87r8BrN3ySrHda/starwink-by-alicorn
- Summary: daniel-kokotajlo pairs it with Egan's "Crystal Nights".

### 2020-05-20 · Comment on "Endogenous Epistemic Factionalization"
- Path: `reception_data/lw_threads/2020-05-20_comment-on-endogenous-epistemic-factionalization.md` · 8 comments (Davis 1) · https://www.lesswrong.com/posts/8cWMX6L8St8k9pPRC/comment-on-endogenous-epistemic-factionalization
- Summary: **Curated** (Raemon, 13): "took a very messy, complicated subject, and picked one facet of to gain a really crisp understanding of"; praised for checkable code, though Raemon doubts these are the "*primary*" causes of factions. adele-lopez (19) asks about thresholds of liars. gjm (16) argues that distrust of disagreers may beat naivety when some agents misreport. Pongo (15) extends the code. maxflowve2 notes the update rule isn't order-invariant (not Bayesian), and that mistrust capped below 1 gives convergence. Davis (2022): the post was really him doing "'peer' review" of a *Synthese* paper that published simulations without code.
- Quotes:
- (https://www.lesswrong.com/posts/8cWMX6L8St8k9pPRC/comment-on-endogenous-epistemic-factionalization?commentId=uHTPoK9r3awtEzaeG, Raemon, 13 karma)
> It is still relatively uncommon on LessWrong for someone to even rise to the bar of "clearly lays out their reasoning in a very checkable way", and when someone does that while making a point that seems interesting and important-if-true, it seems good to curate it.
- (https://www.lesswrong.com/posts/8cWMX6L8St8k9pPRC/comment-on-endogenous-epistemic-factionalization?commentId=Et8RcC9XNqkSmCRni, maxflowve2, 10 karma)
> The update rule is not bayesian in the sense that if you permute the order of the observations of the experiments, you arrive at different conclusions for each agent (You can test this experimentally easily).

### 2020-06-07 · Philosophy in the Darkest Timeline: Basics of the Evolution of Meaning
- Path: `reception_data/lw_threads/2020-06-07_philosophy-in-the-darkest-timeline-basics-of-the-evolution.md` · 17 comments (Davis 5) · https://www.lesswrong.com/posts/4hLcbXaqudM9wSeor/philosophy-in-the-darkest-timeline-basics-of-the-evolution
- Summary: FeepingCreature: "I thought this was the standard theory of meaning that everyone already believed." Davis (28) answers that the piece supplies executable "how" detail (a Skyrms sender–receiver game with reinforcement learning) and "a thousand roads to Rome". It also lays a foundation for replacing the "four simulacrum levels", which he finds a "hodgepodge". He recommends Skyrms's *Signals*, supplemented by Fallis & Lewis on deception. Davis links further discussion on **/r/rational and /r/SneerClub** (Part B leads). Icarus Gallagher (2021) enjoys it, but cautions about the "good-natured joke" / "gaslighting" line: some social reflexes are "tuned to produce nothing but mutual joy". TurnTrout: "I really like this post." Raemon (2025): the "Summer of Wolves" didn't happen.
- Quotes:
- (https://www.lesswrong.com/posts/4hLcbXaqudM9wSeor/philosophy-in-the-darkest-timeline-basics-of-the-evolution?commentId=HYHjs98ovtYns9KGo, Davis, 28 karma)
> I'm pretty unhappy with the "four levels" formulation

### 2020-06-29 · Optimized Propaganda with Bayesian Networks: Comment on "Articulating Lay Theories Through Graphical Models"
- Path: `reception_data/lw_threads/2020-06-29_optimized-propaganda-with-bayesian-networks-comment-on.md` · 10 comments (Davis 1) · https://www.lesswrong.com/posts/Zvu6ZP47dMLHXMiG3/optimized-propaganda-with-bayesian-networks-comment-on
- Summary: noggin-scratcher (27) doubts the assumption that theory beliefs cause claim beliefs and not vice versa. johnswentworth catches "conditionally independent" → "dependent"; Davis fixes it. ryan_b and mr-hire discuss symmetric weapons. Korz is surprised that one network explains so much variance.

### 2020-07-14 · Algorithmic Intent: A Hansonian Generalized Anti-Zombie Principle
- Path: `reception_data/lw_threads/2020-07-14_algorithmic-intent-a-hansonian-generalized-anti-zombie.md` · 20 comments (Davis 4) · https://www.lesswrong.com/posts/sXHQ9R5tahiaXEZhR/algorithmic-intent-a-hansonian-generalized-anti-zombie
- Summary: **gjm (16):** "I strongly disagree with your 'not allowed to care' claim at the end". "We get to define our words *however the hell we like*"; message length is one criterion among several, and Davis hasn't shown that broadened "intent" shortens messages. Davis (0): "I don't care what so-called 'rationalists' think; I care about what's _true_." gjm (−5) asks why he posts without time to engage; Davis (11) cites his dayjob, quotes prereaders who thought the draft "sucked", and later distinguishes rationalist(1) (method) from rationalist(2) (social group), by analogy to Christians. gjm compares appeals to the Sequences with appeals to scripture: "to whatever extent Eliezer *was* saying the same thing as you I'm afraid I think that Eliezer was wrong". **Viliam (28):** the expanded "intent" risks "sneaking in connotations". SaidAchmiz (24) answers him with Dennett's intentional stance. nathaniel-monson (2023): "You are allowed to care about anything and everything you may happen to care about".
- Quotes:
- (https://www.lesswrong.com/posts/sXHQ9R5tahiaXEZhR/algorithmic-intent-a-hansonian-generalized-anti-zombie?commentId=Wob6WLhTGXaNYbaDt, gjm, 16 karma)
> We get to define our words *however the hell we like*. There are many ways in which one set of definitions can be better or worse than another, *one* of which is that ceteris paribus definitions are better when they reduce average message length. But it's not the only one, and it shouldn't be the only one.
- (https://www.lesswrong.com/posts/sXHQ9R5tahiaXEZhR/algorithmic-intent-a-hansonian-generalized-anti-zombie?commentId=5BgFGFmqWos9whr8o, Davis)
> I don't think that should be interesting. [I don't care what so-called "rationalists" think](https://www.lesswrong.com/posts/jrLkMFd88b4FRMwC6/don-t-double-crux-with-suicide-rock); I care about what's _true_.
- (https://www.lesswrong.com/posts/sXHQ9R5tahiaXEZhR/algorithmic-intent-a-hansonian-generalized-anti-zombie?commentId=uY8gLWLJcsL4L8Dvm, gjm, 7 karma)
> I can see how you see the Sequences as supporting your position, but I don't think that's the only or the best way to interpret the relevant bits of the Sequences, and to whatever extent Eliezer *was* saying the same thing as you I'm afraid I think that Eliezer was wrong.
- (https://www.lesswrong.com/posts/sXHQ9R5tahiaXEZhR/algorithmic-intent-a-hansonian-generalized-anti-zombie?commentId=p7i82NGkrXbhG7Esh, Viliam, 28 karma)
> So it seems to me that you are redefining words, with the risk of [sneaking in connotations](https://www.lesswrong.com/posts/yuKaWPRTxZoov4z8K/sneaking-in-connotations).

### 2020-08-23 · Maybe Lying Can't Exist?!
- Path: `reception_data/lw_threads/2020-08-23_maybe-lying-can-t-exist.md` · 17 comments (Davis 1) · https://www.lesswrong.com/posts/YptSN8riyXJjJ8Qp8/maybe-lying-can-t-exist
- Summary: **cousin_it (23):** a lie can work in equilibrium (49/49/2 good/evil/liar example); the "priced in" story is narrowly right but misses what matters. abramdemski reads the post as showing you can't have both signal-as-probabilistic-implication and a sensible "lying". cousin_it replies that utility functions can include an aversion to lying. Randomini (28): Wittgensteinian language games plus symbol grounding. justinpombrio separates "intentionally lying" from "intentionlessly misleading". **Unnamed (13, 14):** measuring deception by the probability assigned to the true state is a mistake, because actions depend on the full distribution (the seeker/witness toy example). Hazard: an "almost-a-post" extension on Skyrms. abramdemski (2020): "one of the best recent posts". Davis (2023) posts a GPT-4 "highly critical comment" on his own post (calling it "pseudo-intellectual posturing").
- Quotes:
- (https://www.lesswrong.com/posts/YptSN8riyXJjJ8Qp8/maybe-lying-can-t-exist?commentId=Yr8tzgsYwhRhFvsei, cousin_it, 23 karma)
> So if the person is in fact an evil liar, their lie had the intended effect on you. It wasn't "priced into the equilibrium" or anything.
- (https://www.lesswrong.com/posts/YptSN8riyXJjJ8Qp8/maybe-lying-can-t-exist?commentId=x9tzZXFuEQuZKDnoF, Unnamed, 13 karma)
> Actions are based on their full probability distribution, not just the probability assigned to the true state.
- (https://www.lesswrong.com/posts/YptSN8riyXJjJ8Qp8/maybe-lying-can-t-exist?commentId=43Azh5MrJXfpMCZ5q, abramdemski, 6 karma)
> I still think this is one of the best recent posts. Well-researched and well-presented, and calls into question some of my tacit assumptions about how words work.

### 2020-09-17 · Artificial Intelligence: A Modern Approach (4th edition) on the Alignment Problem
- Path: `reception_data/lw_threads/2020-09-17_artificial-intelligence-a-modern-approach-4th-edition-on-the.md` · 12 comments (Davis 3) · https://www.lesswrong.com/posts/BNJx2CqfXyiusoJcK/artificial-intelligence-a-modern-approach-4th-edition-on-the
- Summary: TurnTrout and habryka dispute Russell's "if and only if" claim about off-switch incentives. habryka (7): "In this context using this kind of technical language feels actively deceitful to me". Davis quotes §16.7.2 and agrees the Chapter 1 sentence overgeneralizes. **Davis (8):** the textbook's first-chapter treatment of the paperclip problem is evidence against worries about "splash damage". "If there _was_ a marketing war to legitimize AI risk, we _won_! Now can 'we' please stop using the marketing war as an excuse for lying?!" He calls rationalism a "stupid robot cult that I continue to feel contempt for but don't know how to quit". steven0461 (14) lists "predictable counterpoints": "maybe we won because we were cautious ... picking battles isn't lying". Davis: the "runaround on appeals to consequences" is "a neat microcosm" of why unaligned AIs are deceptive by default.
- Quotes:
- (https://www.lesswrong.com/posts/BNJx2CqfXyiusoJcK/artificial-intelligence-a-modern-approach-4th-edition-on-the?commentId=pGoyqBpidcWpLjiTm, Davis, 8 karma)
> If there _was_ a [marketing war](https://www.lesswrong.com/posts/Zvu6ZP47dMLHXMiG3/optimized-propaganda-with-bayesian-networks-comment-on) to legitimize AI risk, we _won_! Now can "we" please stop using the marketing war as an excuse for lying?!
- (https://www.lesswrong.com/posts/BNJx2CqfXyiusoJcK/artificial-intelligence-a-modern-approach-4th-edition-on-the?commentId=6snriTihReFnKJ7tA, steven0461, 14 karma)
> some predictable counterpoints: maybe we won because we were cautious; we could have won harder; many relevant thinkers still pooh-pooh the problem

### 2020-10-12 · Msg Len
- Path: `reception_data/lw_threads/2020-10-12_msg-len.md` · 4 comments · https://www.lesswrong.com/posts/ex63DPisEjomutkCw/msg-len
- Summary: Light: Gurkenglas approves "the haikuesque format"; there are Strunk and White jokes.

### 2020-10-20 · Message Length
- Path: `reception_data/lw_threads/2020-10-20_message-length.md` · 25 comments (Davis 5) · https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length
- Summary: **Curated** (habryka, 10): "a quite good and straightforward explanation of what I think of as one of the really core ideas in theoretical rationality", likened to what habryka calls "A technical explanation of a technical explanation". cousin_it (31) says that after exhausting short theories you should still check analogies (a "binary encoded Russian poem"); Davis: "I couldn't get that program to run on my desktop." **dxu (22)** objects that float precision shouldn't set model complexity. Davis concedes, citing Grünwald's MDL complexity term, and says the "handwaving should be admissible in the cute-blog-story genre as long as the author addresses objections in the comment section". rainy invents something like the Thue–Morse sequence. Raemon (2021) on the SVG anecdote: "I feel like I'm a character in some Zack Davis fiction".
- Quotes:
- (https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length?commentId=byzaiS6XwHk83Trmq, habryka4, 10 karma)
> Promoted to curated: This really is a quite good and straightforward explanation of what I think of as one of the really core ideas in theoretical rationality, covering surprisingly much ground in a way that feels approachable.
- (https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length?commentId=EyY2kmixkHAELNx6s, dxu, 22 karma)
> The precision of your floats shouldn't be what determines the complexity of your Markov chain

### 2020-11-08 · Scoring 2020 U.S. Presidential Election Predictions
- Path: `reception_data/lw_threads/2020-11-08_scoring-2020-u-s-presidential-election-predictions.md` · 7 comments (Davis 1) · https://www.lesswrong.com/posts/muEjyyYbSMx23e2ga/scoring-2020-u-s-presidential-election-predictions
- Summary: Oscar_Cunningham points out that summing per-state log scores double-counts correlated outcomes, and recomputes (The Economist still wins). Davis: "you are right and the thing I originally wrote was wrong", and adds a crediting disclaimer to the post.

### 2020-12-10 · Containment Thread on the Motivation and Political Context for My Philosophy of Language Agenda
- Path: `reception_data/lw_threads/2020-12-10_containment-thread-on-the-motivation-and-political-context.md` · 25 comments (Davis 7) · https://www.lesswrong.com/posts/5aqumaym7Jd2qhDcy/containment-thread-on-the-motivation-and-political-context
- Summary: **The one LW venue where Davis argues the object-level gender question openly; the main exchanges are with gjm, TekhneMakre, and tailcalled.**
  - Pattern: the linked posts are "too long", which he takes as evidence that "keeping politics out of lesswrong does help". Viliam asks whether Davis would honor the pronouns of a *non*-passing *cis* person (no reply in thread).
  - **gjm exchange (May 2021, moved from Eukaryote's "There's No Such Thing as a Tree").** Davis admits his reply there was "a snippy reply daring you to engage". His "pouncing algorithm" is "If someone favorably cites ... 'The Categories Were Made for Man, Not Man for the Categories,' then pounce", and that post is "_utterly pants-on-fire mendacious_". gjm (9, 11): language isn't only for prediction; "neither rationality nor rationalism includes any obligation to optimize your words for the exact same thing as your thoughts". Hearers recover the real question (sex? toilets? drug dose?). "I remain entirely unpersuaded that it's 'bonkers'". Davis (10) distinguishes the arbitrariness of codewords from that of boundary placement (the weather-report example). He says pronouns carry sex information, which is why trans people care. He argues sex is "_functionally_ binary", unlike towns or colors, and proposes "Adult human females, _plus_ sufficiently successful male mimics thereof". "Doesn't your soul die a little bit?" Then: "Okay. I give up. ... You're very good at what you do!" gjm: "I'm not sure to what extent I'm supposed to take the last comment as an insult". mrkun (7): one language for thought and speech isn't possible; he uses many speech "generators".
  - **TekhneMakre exchange (Feb 2022):** naming "the cluster of people who want to be treated the way women are treated" is legitimate. Davis (17) agrees it's fine where unambiguous (the water/ice analogy). "The _problem_ is that a dominant faction in my Society _really_ doesn't want it to be socially permissible to disambiguate". TekhneMakre: Davis's examples (sea creatures as "less cohesive") are red herrings for his real point. Richard_Kennaway: 1950s Britain had "househusbands", not "women".
  - **tailcalled (2023–24):** Blanchardians make "trollish" arguments (links to his surveyanon posts against Blanchard/Dreger and Bailey). "Autogynephilia is not a natural abstraction" for most audiences. He argues Davis's childhood gender-atypicality items reflect gender progressivism, not AGP. Davis: "Permalink or it didn't happen".
  - lsusr cites Davis's "conflate dissent with unkindness" line approvingly.
- Quotes:
- (https://www.lesswrong.com/posts/5aqumaym7Jd2qhDcy/containment-thread-on-the-motivation-and-political-context?commentId=uXjBHeLPD5opBct6J, Davis)
> I think the actual pouncing algorithm is, "If someone favorably cites Scott Alexander's ['The Categories Were Made for Man, Not Man for the Categories'](https://slatestarcodex.com/2014/11/21/the-categories-were-made-for-man-not-man-for-the-categories/), then pounce."
- (https://www.lesswrong.com/posts/5aqumaym7Jd2qhDcy/containment-thread-on-the-motivation-and-political-context?commentId=JbgEPpqHaHKBeFPyz, gjm, 9 karma)
> Words and thoughts are closely related but they aren't the same, and I agree with Scott that neither rationality nor rationalism includes any obligation to optimize your words for the exact same thing as your thoughts.
- (https://www.lesswrong.com/posts/5aqumaym7Jd2qhDcy/containment-thread-on-the-motivation-and-political-context?commentId=jMw4KEqobEuzzQsPB, Davis, 10 karma)
> But—don't you _want_ the language you speak to your friends to be the same as the language you use to organize your own thoughts? How can you accept a wall between the world you see, and the world you're allowed to talk about? Doesn't your soul die a little bit?
- (https://www.lesswrong.com/posts/5aqumaym7Jd2qhDcy/containment-thread-on-the-motivation-and-political-context?commentId=huRHnxMo4zTiWrjCg, gjm, 11 karma)
> And, despite your many thousands of words on the subject, I remain entirely unpersuaded that it's "bonkers", and it still looks to me as if your assertions that it's "bonkers" are based on entirely unrealistic ideas about how language ought to be used.
- (https://www.lesswrong.com/posts/5aqumaym7Jd2qhDcy/containment-thread-on-the-motivation-and-political-context?commentId=ofzk2svhtJemLXbr9, Davis, 17 karma)
> The _problem_ is that a dominant faction in my Society _really_ doesn't want it to be socially permissible to disambiguate
- (https://www.lesswrong.com/posts/5aqumaym7Jd2qhDcy/containment-thread-on-the-motivation-and-political-context?commentId=yjAiAKshHWbJEDokM, tailcalled, 10 karma)
> And I would claim that the Blanchardian side regularly does so, e.g. [with emphasizing menstruation fetishism](https://surveyanon.wordpress.com/2020/08/11/contra-blanchard-and-dreger-on-autogynephilia-in-cis-women/), or by [doing deceptive sampling](https://surveyanon.wordpress.com/2022/12/27/michael-bailey-doubles-down-on-his-lies-%f0%9f%a4%a3/).

### 2020-12-31 · And You Take Me the Way I Am
- Path: `reception_data/lw_threads/2020-12-31_and-you-take-me-the-way-i-am.md` · 5 comments (Davis 0) · https://www.lesswrong.com/posts/8B5DpBwMdNPxXfDrM/and-you-take-me-the-way-i-am
- Summary: EpicNamer27098: treating one honest utterance as decisive of a person's honesty "is an act of bad faith, or just very naive". Zvi: "Do you believe that all strategy is deception?" Dagon: "'wait, I didn't mean that' is just a common way to point this out" that one is often not at one's best.

### 2021-01-08 · Unnatural Categories Are Optimized for Deception
- Path: `reception_data/lw_threads/2021-01-08_unnatural-categories-are-optimized-for-deception.md` · 32 comments (Davis 10) · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception
- Summary:
  - Davis's meta note directs political discussion to the Containment Thread.
  - **johnswentworth (14):** "'clusters in thingspace' is a metaphor"; the underlying concept is conditional independence plus the natural-abstraction hypothesis (natural-concept space is approximately discrete). Socially constructed categories are moved by changing the territory ("Parable of the Dammed"). Davis (8, Mar 2021) works through how his squared-error clustering relates to this; the metric may be "_knowably_ arbitrary" like the base of a logarithm. Wentworth: "Yup, this seems basically right", and he shares a draft. This leads to Davis's "Feature Selection" (Nov 2021). tailcalled proposes a causal (confounder) version.
  - Raemon: the post dismissed the nation-borders question as mere metaphor, "fairly surprising and disappointing". DanielFilan: re-drawing categories and lying p% are often not functionally identical (the "book" plus random things example).
  - **iceman (37, Review 2022):** "Zack's series of posts in late 2020/early 2021 were really important to me ... a sort of return to form for LessWrong". The value is in showing "high status members of the rationalist community are completely flubbing lawful thinking", which made it "__thinkable__" that they fail elsewhere. He links this to his receptiveness to Christiano's critique of MIRI's track record.
  - **Wei_Dai (9, 2024):** a benign motive exists ("neural fireplace"): "trans women are women" may signal local *values* ("people around here do not distinguish ...") rather than deceive about sex. Davis: argue for it "on the merits", not because the CEO "will be really sad". Wei: then what distinguishes the two kinds of argument? Maybe "your disagreement with Eliezer/Scott is based on" which analogy fits better. martin-randall gives a real history of fireplaces.
  - **Davis (11, 2025):** "I think this was excellent work that no one (rounding down) appreciated at the time because I sacrificed readability by optimizing for comprehensiveness", followed by a 24-tweet summary. tslarm (10): if I'm open about my category boundaries, how is it deceptive? Davis points to "Maybe Lying Can't Exist?!".
- Quotes:
- (https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=FqjsM2AkEkaBgf2wD, johnswentworth, 14 karma)
> First, "clusters in thingspace" is a metaphor. There isn't really a canonical "thingspace" with pre-defined features along the axes; figuring out what features to use is most of the problem from the start.
- (https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=eBgiESoE4oprBxoWq, iceman, 37 karma)
> But that topic is sort of irrelevant: the value comes in pointing out that high status members of the rationalist community are completely flubbing lawful thinking. That made it __thinkable__ that actually, they might be failing in other contexts.
- (https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=bTiqGbH53qH2czjbM, Wei_Dai, 9 karma)
> Given this, I think "trans women are women" isn't necessarily motivated by deception of which sex cluster someone belongs to, but instead a signal of local values, trying to imply something like "people around here do not distinguish between trans women and cis women in their values, at least in most circumstances".
- (https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=9kcKahbspGfKKp7kr, Wei_Dai)
> But it occurs to me that maybe your disagreement with Eliezer/Scott is based on you thinking that the first analogy is closer, and them thinking that the second analogy is closer?
- (https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=w9tWkpCBrdgwq6Coc, Davis, 11 karma)
> I think this was excellent work that no one (rounding down) appreciated at the time because I sacrificed readability by optimizing for comprehensiveness.
- (https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=fccJsyMtGTxdLAWEW, tslarm, 10 karma)
> If I'm honest about the boundaries of my new category system, how is this deceptive?

### 2021-01-30 · Less Wrong Poetry Corner: Coventry Patmore's "Magna Est Veritas"
- Path: `reception_data/lw_threads/2021-01-30_less-wrong-poetry-corner-coventry-patmore-s-magna-est.md` · 1 comment · https://www.lesswrong.com/posts/9M3ynNuBsRCDfmEsZ/less-wrong-poetry-corner-coventry-patmore-s-magna-est
- Summary: JackLecter reads the poem less as irony than as "grasping for solace" (Marcus Aurelius), and asks how closely Davis identifies Patmore with the narrator.

### 2021-03-26 · Communication Requires Common Interests or Differential Signal Costs
- Path: `reception_data/lw_threads/2021-03-26_communication-requires-common-interests-or-differential.md` · 13 comments (Davis 1) · https://www.lesswrong.com/posts/ybG3WWLdxeTTL3Gpd/communication-requires-common-interests-or-differential
- Summary: Praised for brevity (iceman: "much shorter and more concise than a lot of the other posts"; 1a3orn (16, Review): "Per-word one of my favorite posts", like thermodynamics for forum design). **Ninety-Three (15)** counterexample: a language where most sentences are lies (60% random colors) can still be informative. Chris_Leong (2024) calls it a "Good counter-example". **adele-lopez (31):** communication doesn't generally need "delicate maintenance"; a temperature analogy where LW is liquid nitrogen and Davis seeks liquid helium. clone of saturn: Challenger, Iraqi WMDs, and Lysenkoism show normalized lying ending in catastrophe. Benquo: opportunity cost as a differential cost. Davis on the generic "her" in his Wittgenstein quote: "Personal whimsy".
- Quotes:
- (https://www.lesswrong.com/posts/ybG3WWLdxeTTL3Gpd/communication-requires-common-interests-or-differential?commentId=LnjaENDMp6gcn5xGQ, adele-lopez-1, 31 karma)
> It doesn't seem generally true that communication requires delicate maintenance. Liars have existed for thousands of years, and languages have diverged and evolved, and yet we still are able to communicate straightforwardly the vast majority of the time!
- (https://www.lesswrong.com/posts/ybG3WWLdxeTTL3Gpd/communication-requires-common-interests-or-differential?commentId=YXzmb82zdxbCupFpe, Davis, 5 karma)
> (My ideology has evolved over the years such that I think a lot of the people who are trying to signal something with the generic feminine would not regard me as an ally, but I still love the _æsthetic_.)

### 2021-05-03 · Sexual Dimorphism in Yudkowsky's Sequences, in Relation to My Gender Problems (linkpost to UUT)
- Path: `reception_data/lw_threads/2021-05-03_sexual-dimorphism-in-yudkowsky-s-sequences-in-relation-to-my.md` · 29 comments (Davis 1) · https://www.lesswrong.com/posts/LwG9bRXXQ8br5qtTx/sexual-dimorphism-in-yudkowsky-s-sequences-in-relation-to-my
- Summary: Mostly sympathetic and personal. **A trans commenter (deleted user, 12, 24)** expected HRT to show "how wrong everything you said was". Davis: "What parts, specifically, are wrong? ... If I'm wrong about everything, I want to _know!_" The commenter concedes: "Which means it wasn't you that was wrong, it was me." They note the "cis-by-default theory". tailcalled and vanessa-kosoy discuss estrogen's rapid effects and placebo testing. **tailcalled (13):** AGP is rare in general-population males ("3%-15%", with citations) but much more common in rationalist surveys, so rationalists may wrongly take autogenderphilia for granted. FireStormOOO raises survey-selection caveats. Shamash (15), a gay man, compares it to "jealusty". pablo-repetto (9): wanting a female body is no "weirder or wronger" than wanting to be taller. smountjoy: "Really appreciated all ~16,000 words", but social transition needn't be "promoting 'lying' or bad epistemics". earfluffy: a less extreme AGP experience. Viliam on mind-in-distribution vs. mind-transplant.
- Quotes:
- (https://www.lesswrong.com/posts/LwG9bRXXQ8br5qtTx/sexual-dimorphism-in-yudkowsky-s-sequences-in-relation-to-my?commentId=CbSTNttXadMmpbdaR, Davis, 13 karma)
> What parts, specifically, are wrong? What is the evidence that shows that those parts are wrong? Please tell me! If I'm wrong about everything, I want to _know!_
- (https://www.lesswrong.com/posts/LwG9bRXXQ8br5qtTx/sexual-dimorphism-in-yudkowsky-s-sequences-in-relation-to-my?commentId=7mtwLiZzNij6tGxwz, [deleted user], 24 karma)
> And neither of those things happened! Which means it wasn't you that was wrong, it was me.
- (https://www.lesswrong.com/posts/LwG9bRXXQ8br5qtTx/sexual-dimorphism-in-yudkowsky-s-sequences-in-relation-to-my?commentId=rjpt9uZdmegcGmDgj, tailcalled, 13 karma)
> According to various surveys in the rationalist community, autogynephilia in men (and autoandrophilia in women) appears to be much more common here than it is in the general population.
- (https://www.lesswrong.com/posts/LwG9bRXXQ8br5qtTx/sexual-dimorphism-in-yudkowsky-s-sequences-in-relation-to-my?commentId=CHxYDtce7nwsgbuNu, smountjoy, 5 karma)
> TL;DR: Socially transitioning shouldn't have to be/feel like promoting "lying" or bad epistemics.

### 2021-06-10 · Reply to Nate Soares on Dolphins
- Path: `reception_data/lw_threads/2021-06-10_reply-to-nate-soares-on-dolphins.md` · 49 comments (Davis 7) · https://www.lesswrong.com/posts/aJnaMv8pFQAfi9jBm/reply-to-nate-soares-on-dolphins
- Summary: **The target replies at length (So8res = Nate Soares; Davis's comment places him among "SingInst/MIRI leadership"); this is the episode the corpus narrates in "A Hill of Validity" and later memoir parts.**
  - **So8res (83, the thread's top comment):** the Twitter thread's epistemic status was "i been shitpostin since april". "I do not wholeheartedly believe the argument I made". The fragment he endorses: "be wary of those who say they are here to refine your concepts, for sometimes they are here to steal them". He defends shitposting as healthy ("our community has dramatically too little fun on social media"). He says the thread "was not a veiled attempt to discuss gender issues"; that reading "didn't cross my mind".
  - **Davis (67):** Yudkowsky in 2008 called dolphins-are-fish "playing nitwit games", and in 2021 retweeted Soares saying the reverse: "**A complete 180° reversal, on this specific example!** _Why?_ **What changed?**" "**Am I the only one creeped out by this?**" He offers a $2000 "cheerful price" for a public reply. He also made a Copenhagen/MWI analogy; adele-lopez (45) called it "a strong overstatement" and Davis retracted it (20).
  - **So8res (67):** the list of what changed for him: niche-adaptation clusters, "nature just keeps turning out crabs", fruit/berry, "phylogenetic classification is the one true way" as a background whisper. He doesn't see it as incongruent with Yudkowsky's #30, and gives the "haha yeah" about "y'all know i'm right".
  - **Davis (−26):** "this 'haha yeah' is _really disrespectful_". "Straightening out the so-called 'rationalist' community's collective position on the cognitive function of categorization ... has been _the major project of my life_ for _the past forty months_". "If you have _any_ scrap of human decency in your brain, **you will not _shitpost_ at me**." "This isn't a 'pretend to agree with me to appease my untreated mental illness' move."
  - **So8res (75):** "you're dramatically mismodelling me". "My current emotional response is one that emits sentences like 'well fuck you too; call me back when you can model me farther than you can throw me'". He has "abstract compassion" and will honor the no-glibness request. **Davis (34): "Thanks. I regret letting my emotions get the better of me. I apologize."**
  - **Vaniver (mod, 32):** Davis's comment oversteps bounds, "imputing positions stronger than people are holding"; it risks an "escalatory dynamic" reminiscent of "trapped priors". The standard he seems to impose is "please never joke in public about something I take very seriously". Vaniver agrees the about-face deserved explanation but finds Soares's explanation satisfactory. He offers to review drafts. **Vaniver (40) on the object level:** by timetree divergence dates, sharks are further from guppies than dolphins are, so the 2008 list is "*bad* phylogenetics". GuySrinivasan (13): the comment signals that engaging Davis will be "extremely emotionally draining". tomcatfish: emotional appeals cut against the "both sides honest" argument.
  - **Support:** iceman (12): "No. You are not the only one creeped out by this." Benito: "surprised that the dolphins example has 180'd". Jiro: Scott Alexander's TCWMFM explains the shift as political. gjm demands evidence beyond motive-imputation (and notes symmetric motive claims could be made about Davis). cousin_it (17): "Nate might not have been fully serious, and you tend to get a bit worked up sometimes". Davis: "Well, _yes_. _I've got Something to Protect._" cata: dolphins-as-fish maps to *common-sense* gender, the opposite of Davis's mapping.
  - Davis (Sept 2021) returns after a "three-and-a-half-month cooldown" with "Blood Is Thicker Than Water".
- Quotes:
- (https://www.lesswrong.com/posts/aJnaMv8pFQAfi9jBm/reply-to-nate-soares-on-dolphins?commentId=3qbzHGvHbNsC84zxj, So8res, 83 karma)
> For the record, the fragment of my argument that I currently endorse is something like "be wary of those who say they are here to refine your concepts, for sometimes they are here to steal them".
- (https://www.lesswrong.com/posts/aJnaMv8pFQAfi9jBm/reply-to-nate-soares-on-dolphins?commentId=3qbzHGvHbNsC84zxj, So8res, 83 karma)
> Finally, I'll note that that thread was not a veiled attempt to discuss gender issues. The idea that it could be read as subtweeting gender issues didn't cross my mind.
- (https://www.lesswrong.com/posts/aJnaMv8pFQAfi9jBm/reply-to-nate-soares-on-dolphins?commentId=BBtSuWcdaFyvgddE4, Davis, 67 karma)
> **A complete 180° reversal, on this specific example!** _Why?_ **What changed?**
- (https://www.lesswrong.com/posts/aJnaMv8pFQAfi9jBm/reply-to-nate-soares-on-dolphins?commentId=HwSkiN62QeuEtGWpN, So8res, 67 karma)
> Attempting to force the change into a single sentence, I'd say that the main thing that changed is I noticed the subtle background forces that whisper (at least to blue tribe members in their youth) "phylogenetic classification is the one true way to organize life forms", and rejected its claim.
- (https://www.lesswrong.com/posts/aJnaMv8pFQAfi9jBm/reply-to-nate-soares-on-dolphins?commentId=rMHcWfqkH89LWt4y9, Davis, −26 karma)
> I just want to say that this "haha yeah" is _really disrespectful_.
- (https://www.lesswrong.com/posts/aJnaMv8pFQAfi9jBm/reply-to-nate-soares-on-dolphins?commentId=8nmjnrm4cwgCCyYrG, So8res, 75 karma)
> My take on this conversation is that you're dramatically mismodelling me, and then running really far -- and getting quite distressed -- based on bad models.
- (https://www.lesswrong.com/posts/aJnaMv8pFQAfi9jBm/reply-to-nate-soares-on-dolphins?commentId=FEihAQ6QMacoaFDhx, Davis, 34 karma)
> Thanks. I regret letting my emotions get the better of me. I apologize.
- (https://www.lesswrong.com/posts/aJnaMv8pFQAfi9jBm/reply-to-nate-soares-on-dolphins?commentId=32espNsccK2izuBRY, Vaniver, 32 karma)
> The standard you seem to be imposing is not "please respond to seriousness with seriousness" but the much stronger "please never joke in public about something I take very seriously", which seems like a pretty drastic standard, and one I would mildly warn against trying to enforce on LW.
- (https://www.lesswrong.com/posts/aJnaMv8pFQAfi9jBm/reply-to-nate-soares-on-dolphins?commentId=f5eytcpD52m47GApi, Vaniver, 40 karma)
> The trouble with defending the 2008 classification is not that it's phylogenetics, it's that, as far as I can tell, it's *bad* phylogenetics.
- (https://www.lesswrong.com/posts/aJnaMv8pFQAfi9jBm/reply-to-nate-soares-on-dolphins?commentId=MqbncXpfYvkfNS8bE, iceman, 12 karma)
> No. You are not the only one creeped out by this.

### 2021-06-27 · Sam Altman and Ezra Klein on the AI Revolution
- Path: `reception_data/lw_threads/2021-06-27_sam-altman-and-ezra-klein-on-the-ai-revolution.md` · 17 comments (Davis 1) · https://www.lesswrong.com/posts/2nLnTMCogFujFYCHD/sam-altman-and-ezra-klein-on-the-ai-revolution
- Summary: Commenters speculate on Altman's apparent unconcern: TekhneMakre ("maker-land" priors), ofer (17: in maker-land "the sign of the impact usually does not appear to matter much"), gwern (43: Altman is "a startup CEO/growth hacker guy, not a DL researcher"). sam-bowman thinks the episode is net good for AI safety. Davis (2022) notes Altman retweeting Richard Ngo's alignment curriculum "seems like a positive development".

### 2021-09-28 · Blood Is Thicker Than Water 🐬
- Path: `reception_data/lw_threads/2021-09-28_blood-is-thicker-than-water.md` · 27 comments (Davis 5) · https://www.lesswrong.com/posts/vhp2sW6iBhNJwqcwP/blood-is-thicker-than-water
- Summary: **The cooled-down sequel to the Soares exchange, with a direct reply from Scott Alexander (Yvain).**
  - **aphyer (56, top):** botanists' and cooks' "fruit" are both valid in context, and demanding a single sense is "denying cooks access to a useful regularity that they care about". Davis: "I actually agree with this."
  - **pktechgirl (24):** carnivores, flyers, and nocturnality are useful non-phylogenetic concepts. She calls the OP "very hard to read". TekhneMakre (17): the post's opponent is "genuinely straw"; niche similarity is also "an underlying generator of similarities". gbear605 (18): categorizing by cause matters only if treatment differs by cause. Davis (10): concepts defined by ancestry are "_so_ robustly useful across _so_ many situations" (you say "I have a cat", not "an endotherm").
  - **Yvain (17):** points to his 2019 SSC post at `slatestarcodex.com/2019/12/04/symptom-condition-cause/`. In a thought experiment, a billion more years of convergent evolution makes whales 99% fish-like; is there then a long period where you may categorize "however you want"? "I think 'crabs' are in this situation right now". SaidAchmiz: by construction, today's 85/15 split settles it.
  - **Davis (18):** "No, of course not: we want categories that give useful information." He asks: "Did I fail as a writer by reaching for the cutesy title?" His target is "idiocies of the form ... 'But who cares about sex chromosomes; I only care about presentation and preferred pronouns'". He parodies TCWMFM's rhetoric with dolphins ("Dolphins are fish _because_ if they weren't, then I would be very sad and might kill myself ...") and says such an "emotional-blackmail maneuver", passed off as philosophy, would be "_laughed out of the room_". He uses the word "retarded" in passing. On crabs, he asks what reading Scott's claim is based on. FeepingCreature: Scott claims categories are "subjective, which is to say instrumental", not arbitrary. Slider develops a nut-allergy analogy for why reports of sadness aren't simply blackmail. tailcalled (2024) concludes dolphins aren't fish.
- Quotes:
- (https://www.lesswrong.com/posts/vhp2sW6iBhNJwqcwP/blood-is-thicker-than-water?commentId=8jYceMhfFwmEvvpBm, aphyer, 56 karma)
> If you show up in a kitchen and demand that the cooks say 'put the vegetables plus the tomatoes in the salad bowl, and the fruits except for the tomatoes in the fruit salad bowl', you're at least not screwing up dinner, but you're **being annoying by denying cooks access to a useful regularity that they care about.**
- (https://www.lesswrong.com/posts/vhp2sW6iBhNJwqcwP/blood-is-thicker-than-water?commentId=DCaKXfmHmRGRZA4oL, Yvain, 17 karma)
> Or might there be a very long period when they are more like mammals in some way, more like fish in others, and you're allowed to categorize them however you want based on which is more useful for you? If the latter, what makes you think we're not in that period right now?
- (https://www.lesswrong.com/posts/vhp2sW6iBhNJwqcwP/blood-is-thicker-than-water?commentId=K9K96iSjzgXErJNmf, Davis, 18 karma)
> Rather, the reason I wrote this post is because I keep running into idiocies of the form "But who cares about evolutionary relatedness; I only care if it swims" (on the "Are dolphins fish?" question) or "But who cares about sex chromosomes; I only care about presentation and preferred pronouns" (on the "Are trans women women?" question).
- (https://www.lesswrong.com/posts/vhp2sW6iBhNJwqcwP/blood-is-thicker-than-water?commentId=K9K96iSjzgXErJNmf, Davis, 18 karma)
> If some intellectually dishonest coward were to try to pass off the emotional-blackmail attempt as a serious philosophy argument, they would be _laughed out of the room_. Right?
- (https://www.lesswrong.com/posts/vhp2sW6iBhNJwqcwP/blood-is-thicker-than-water?commentId=jefYZounQqM3LGzo8, TekhneMakre, 17 karma)
> This seems genuinely straw, relative to the simple position

### 2021-10-08 · Glen Weyl: "Why I Was Wrong to Demonize Rationalism" (linkpost)
- Path: `reception_data/lw_threads/2021-10-08_glen-weyl-why-i-was-wrong-to-demonize-rationalism.md` · 12 comments (Davis 1) · https://www.lesswrong.com/posts/cExAYPCSGhx5NgfWY/glen-weyl-why-i-was-wrong-to-demonize-rationalism
- Summary: Reception of Weyl's essay. Nathan Young (38) describes conversations that preceded Weyl's change of mind. AllAmericanBreakfast (40): Weyl "may not be really apologizing here"; it's a strategic retargeting. gwern (20) cites Weyl's fabricated citations about Audrey Tang (per an ACX comment). Viliam (16) asks what "niche sport" rationalists and NRx share. Davis's one comment: "Why would we want an apology? Apologies are boring. _Updates_ are interesting!"
- Quotes:
- (https://www.lesswrong.com/posts/cExAYPCSGhx5NgfWY/glen-weyl-why-i-was-wrong-to-demonize-rationalism?commentId=TemXYo8iaiB6LtHvN, Davis, 12 karma)
> Why would we want an apology? Apologies are boring. _Updates_ are interesting!

### 2021-11-01 · Feature Selection
- Path: `reception_data/lw_threads/2021-11-01_feature-selection.md` · 24 comments (Davis 1) · https://www.lesswrong.com/posts/dYspinGtiba5oDCcv/feature-selection
- Summary: **Curated** (Raemon, 35): "be pretty compelling as fiction", "illustrate concepts about information theory", and "be interestingly surprisingly hard sci-fi". Benito: "Exciting, delightful, weirdly relatable." JenniferRM (33) writes a fan-continuation (the AI checks the year: "2043"). ricraz (20) welcomes AI stories but warns against anthropomorphism (negative rewards "hurting"). Jon Garcia compares it to "That Alien Message" and imagines an escape scenario. Davis's 2023 self-review: "I was surprised by how well-received this was!" He was disappointed so many read it as about AI: "to me, this isn't a story about AI", but about how concepts work (from the Wentworth exchange).
- Quotes:
- (https://www.lesswrong.com/posts/dYspinGtiba5oDCcv/feature-selection?commentId=4wGgzTwD4nhxQo9wd, Raemon, 35 karma)
> Curated. I found this post to do a neat job of "be pretty compelling as fiction", "illustrate concepts about information theory", and "be interestingly surprisingly hard sci-fi".
- (https://www.lesswrong.com/posts/dYspinGtiba5oDCcv/feature-selection?commentId=rPjWKvjun3FjaoMXR, Davis, 7 karma)
> I was also a bit disappointed at how many commenters focused on the AI angle.

### 2021-11-27 · Comment on "Deception as Cooperation"
- Path: `reception_data/lw_threads/2021-11-27_comment-on-deception-as-cooperation.md` · 4 comments (Davis 1) · https://www.lesswrong.com/posts/dJjRSjmH7NNLJDb6v/comment-on-deception-as-cooperation
- Summary: Wei_Dai (10): academia "is still pretty far from being able to understand lying on a theoretical level". jbash: lying "blows its credibility" in the iterated real-world game. TekhneMakre: deceivers are "parasitic on the non-deceivers's network". Davis (2023) posts GPT-4's "highly critical comment" (calling the post "convoluted and problematic").

### 2022-03-13 · Challenges to Yudkowsky's Pronoun Reform Proposal
- Path: `reception_data/lw_threads/2022-03-13_challenges-to-yudkowsky-s-pronoun-reform-proposal.md` · 56 comments (Davis 4) · https://www.lesswrong.com/posts/juZ8ugdNqMrbX7x2J/challenges-to-yudkowsky-s-pronoun-reform-proposal
- Summary: **The highest-karma endorsement Davis's gender-epistemics writing receives on LW comes from LW's lead administrator.**
  - **habryka (104, top):** leaving aside whether LW is the right venue, "basically everything in this post strikes me as 'obviously true'". Yudkowsky's Facebook post "shifted my epistemic risk assessment" of the community: "community leaders might make up sophisticated stories for why pretty obviously true things are false in order to not have to deal with complicated political issues". "I do think that was the right update to make ... though it still deeply saddens me." He still trusts Yudkowsky most of anyone.
  - iceman (32): it's not Straussian but "the raw output of Elizer's rationalizations". "Zack is hypersensitive to this one issue because it interacts with his Something to Protect". Benito (14) agrees that pronoun norms around "stating the truth" are violated, and finds commenting costly ("taking way too much of my time to speak clearly without tripping some societal tripwire"). Yoav Ravid wants more such posts.
  - **Critics:** Veedrac (32): the length hurts clarity. Yudkowsky's point is "maximal abstention"; "these conversations feel like knives". AprilSR: Davis's points feel unrelated to Eliezer's argument. martin-randall (37): the "simplest and best protocol" fails on concrete examples (Yudkowsky's own pronouns). Bunthut: Yudkowsky's self-report is psychologically plausible. adrian-arellano-davin ("mukashi" in the thread): disappointed at the upvotes. tailcalled (38): it matters when the founder is "a poor example" of the community's principle.
  - **gjm (22):** "That would be easier to believe if Zack ever posted anything here that *wasn't* overtly or covertly (1) about trans issues and (2) on the 'trans Xs are not real Xs' side". "It's possible for one's thinking to be made *worse overall* by a process of *correcting errors*, if the choice of which errors has enough bias". He also finds the stated motivation hard to reconcile with the post's adversarial framing. **Davis (58)** classifies his last two years of non-linkposts as 9 that could exist without the "gender-political crusade" and 4 that couldn't. He describes the crusade as "a _defensive_ effort in response to cultural trends that stabbed me in the face after moving to Berkeley in 2016". He cites his "other side" posts ("Self-Identity Is a Schelling Point" and the "Super-Proton" rebuttal). He says he obsesses over the issue mostly because "they're easy to get _right_". He cites Yudkowsky's 2016 Facebook post and a follower's reported "final thing I needed to realize that I'm a girl". "If it helps, I think I'm almost done??" gjm (16) apologizes for not checking the numbers, but maintains doubts about the stated motive. Davis: "this is the continuation of an argument between me and Yudkowsky that has gone on for years ... You can't expect me to let him have the last word!" He gives the "Z.M." nickname anecdote, and adds: "I don't think I meant to come off as that altruistic."
  - **localdeity (59):** expecting people to *think* of someone as a gender would be "thought-policing", while not rubbing it in their face is polite. StellaAthena (−3): "I am in fact a man" is "the basic meaning of language". Davis asks what observation would show the populace is wrong. cata (22) says it "literally never occurred to me" that trans people were asking him to reconsider their gender, not just a word. Slider (36): singular "they" ambiguity is overrated.
  - Davis's 2024 self-review: "I'm proud of this post, but it doesn't belong in the Best-of-2022 collection because it's on a niche topic."
- Quotes:
- (https://www.lesswrong.com/posts/juZ8ugdNqMrbX7x2J/challenges-to-yudkowsky-s-pronoun-reform-proposal?commentId=he8dztSuBBuxNRMSY, habryka4, 104 karma)
> But leaving that discussion aside, basically everything in this post strikes me as "obviously true" and I had a very similar reaction to what the OP says now, when I first encountered the Eliezer Facebook post that this post is responding to.
- (https://www.lesswrong.com/posts/juZ8ugdNqMrbX7x2J/challenges-to-yudkowsky-s-pronoun-reform-proposal?commentId=he8dztSuBBuxNRMSY, habryka4, 104 karma)
> "well, I sure have to at least do a lot of straussian reading if I want to understand what people actually believe, and should expect that depending on the circumstances community leaders might make up sophisticated stories for why pretty obviously true things are false in order to not have to deal with complicated political issues".
- (https://www.lesswrong.com/posts/juZ8ugdNqMrbX7x2J/challenges-to-yudkowsky-s-pronoun-reform-proposal?commentId=xYc86tcujDY9Lrg9p, gjm, 22 karma)
> That would be easier to believe if Zack ever posted anything here that *wasn't* overtly or covertly (1) about trans issues and (2) on the "trans Xs are not real Xs" side of the usual battle lines.
- (https://www.lesswrong.com/posts/juZ8ugdNqMrbX7x2J/challenges-to-yudkowsky-s-pronoun-reform-proposal?commentId=9fQSTcGdm3irFd8F4, Davis, 58 karma)
> (I find this counterfactual _very_ easy to imagine, because from my perspective, the crusade feels like a _defensive_ effort in response to cultural trends that stabbed me in the face after moving to Berkeley in 2016, not something I would have done if everyone else hadn't "shot first".
- (https://www.lesswrong.com/posts/juZ8ugdNqMrbX7x2J/challenges-to-yudkowsky-s-pronoun-reform-proposal?commentId=9fQSTcGdm3irFd8F4, Davis, 58 karma)
> I do think they're easy to get _right_, and that if people who are much smarter than me are repeatedly getting them _wrong_, that's a warning sign for much deeper pathologies that could affect the things that do actually matter.
- (https://www.lesswrong.com/posts/juZ8ugdNqMrbX7x2J/challenges-to-yudkowsky-s-pronoun-reform-proposal?commentId=nazZ26byGA8KyX2pL, Davis, 3 karma)
> Is that this is the continuation of an argument between me and Yudkowsky that has gone on for years. (Long, dumb story for a future memoir-post.) You can't expect me to let him have the last word!
- (https://www.lesswrong.com/posts/juZ8ugdNqMrbX7x2J/challenges-to-yudkowsky-s-pronoun-reform-proposal?commentId=TebRKaETZHNai39WF, Veedrac, 32 karma)
> My comment was a lot longer than this, but I deleted the rest because these conversations feel like knives.
- (https://www.lesswrong.com/posts/juZ8ugdNqMrbX7x2J/challenges-to-yudkowsky-s-pronoun-reform-proposal?commentId=TFSZT7aGcoC7Ggsum, localdeity, 59 karma)
> But I feel strongly that people have a right to think whatever thoughts they want, and that anything that seems to be punishing people for thoughts (as opposed to actions or speech) should raise major alarm bells.

### 2022-07-10 · Comment on "Propositions Concerning Digital Minds and Society"
- Path: `reception_data/lw_threads/2022-07-10_comment-on-propositions-concerning-digital-minds-and-society.md` · 12 comments (Davis 0) · https://www.lesswrong.com/posts/nqXcgsqQBw2doAnXu/comment-on-propositions-concerning-digital-minds-and-society
- Summary: **Nick Bostrom (as Nick_Bostrom2, 38) replies.** Raemon (8) singles out Davis's line that the paper reads "as if an attempt to write in a way that's comprehensible to Shock Level 2 tech executives and policymakers has failed to elicit all of the latent knowledge that Bostrom and Shulman actually possess". Bostrom: "You are looking at the wreckage of an abandoned book project"; it is "not really optimized for anybody". He has "some patience for both approaches" (analogy and first principles). The thread on Davis's proposal of higher-reward deployment environments: Kei (14) says it raises the incentive for deceptive alignment; CarlShulman and quintin-pope weigh in. daniel-kokotajlo (10) asks for Davis's positive proposal.
- Quotes:
- (https://www.lesswrong.com/posts/nqXcgsqQBw2doAnXu/comment-on-propositions-concerning-digital-minds-and-society?commentId=SukeTCd5JueZqxjvr, Nick_Bostrom2, 38 karma)
> You are looking at the wreckage of an abandoned book project.  We got bogged down & other priorities came up.  Instead of writing the book, we decided to just publish a working outline and call it a day.

### 2023-02-01 · Aiming for Convergence Is Like Discouraging Betting
- Path: `reception_data/lw_threads/2023-02-01_aiming-for-convergence-is-like-discouraging-betting.md` · 19 comments (Davis 6) · https://www.lesswrong.com/posts/iThwqe3yPog56ytyq/aiming-for-convergence-is-like-discouraging-betting
- Summary: **The opening of the Davis–Duncan Sabien dispute on LW (reply to Sabien's "Basics of Rationalist Discourse").**
  - **Duncan_Sabien (7):** the post contains "questionable leaps, and big roundings-off", such as the claim that disagreement implies thinking the other's epistemic process is flawed. Readers "nodding along will not catch such subtle maneuvers". He notes that Davis answered an accidentally published draft with "This is insane". On Davis's blunt-reply hypothetical: "Zack supposes wrong, and this is an excellent demonstration that he cannot pass the ITT of the post he thinks he is objecting to". The hypothetical "doesn't break any of the guidelines listed".
  - **Davis:** passing an ITT shouldn't be "a prerequisite for replying to a post". He asks why the reply doesn't break the Fifth Guideline. The Fifth Guideline may be "an etiquette guideline masquerading as a rationality guideline". He offers "I'm sorry you were offended" while saying he doesn't "particularly think I did anything wrong". He describes "Zackistan" vs. "the world of Duncans": in Zackistan, "This is insane" plus a substantive argument is no norm violation, and "the culturally normative response is to _just keep arguing_".
  - **localdeity (42, top):** the betting-market analogy fails; a forum's goals differ (you want others to learn, not to keep profiting from their ignorance). Duncan's guidelines aim to get value from imperfect participants; the alternative suits "a website called *Never* Wrong". Davis: "this is an important disanalogy that my post as originally written does not adequately address!" He worries more about a "hugbox/echo-chamber" that shuts out arguments as insufficiently "collaborative".
  - AllAmericanBreakfast (19): markets disincentivize information-sharing. Jessica Taylor: truth-seeking agents converge with *each other* (the tile example). JenniferRM: a long consensus-cost analysis. lalaithion: "I do not have this skill" of ignoring non-collaborativeness. Benito: "Great post"; in his 2024 review (16), "I give this a +4", though "I don't think that this post correctly understands what Sabien is going for".
- Quotes:
- (https://www.lesswrong.com/posts/iThwqe3yPog56ytyq/aiming-for-convergence-is-like-discouraging-betting?commentId=pCiJo6unvnSLjbL9o, Duncan_Sabien, 7 karma)
> I suspect that people who are generally nodding along will not catch such subtle maneuvers on the author's part, and will correspondingly become less clear in their thoughts rather than moreso.
- (https://www.lesswrong.com/posts/iThwqe3yPog56ytyq/aiming-for-convergence-is-like-discouraging-betting?commentId=LzxyBKsv5eqCC5JAk, Duncan_Sabien, 4 karma)
> Zack supposes wrong, and this is an excellent demonstration that he cannot pass the ITT of the post he thinks he is objecting to, and is in fact objecting to a strawman of his own construction.
- (https://www.lesswrong.com/posts/iThwqe3yPog56ytyq/aiming-for-convergence-is-like-discouraging-betting?commentId=htcnBybDP2c8Zayff, Davis, 4 karma)
> Basically, to Zackistani eyes, it looks like Duncans are prone to getting unreasonably offended and shutting down productive conversations over perceived norm violations that Zackistani people just don't recognize as enforceable norms, and instead see as part of the "cost of doing business" of having intellectually substantive discussions.
- (https://www.lesswrong.com/posts/iThwqe3yPog56ytyq/aiming-for-convergence-is-like-discouraging-betting?commentId=YdnHqs7r8ChnN6Ync, localdeity, 42 karma)
> If, on a forum, you think you "win points" solely by writing correct arguments when others are wrong, then it's in your interest to make sure no one else learns from the things you write, so you can keep winning.
- (https://www.lesswrong.com/posts/iThwqe3yPog56ytyq/aiming-for-convergence-is-like-discouraging-betting?commentId=nhhPHpkNGtDq3mKaq, Davis, 9 karma)
> But in the spaces I inhabit, I'm much worried about the failure mode where people form a hugbox/echo-chamber where they/we congratulate them/our-selves on being such good "collaborative truth-seekers", while implicitly colluding to shut out proper and novel arguments on the pretext that the speaker is being insufficiently "collaborative", "charitable", _&c._
- (https://www.lesswrong.com/posts/iThwqe3yPog56ytyq/aiming-for-convergence-is-like-discouraging-betting?commentId=Lyt6yB3uxEivTSrzD, Benito, 16 karma)
> (I don't think that this post correctly understands what Sabien is going for, but I think bringing up reasonable hypotheses and showing why they don't make sense is helpful for people's understanding of how to participate well in discourse.)

### 2023-02-03 · Reply to Duncan Sabien on Strawmanning
- Path: `reception_data/lw_threads/2023-02-03_reply-to-duncan-sabien-on-strawmanning.md` · 11 comments (Davis 2) · https://www.lesswrong.com/posts/5zjucvhSFvp92eYbE/reply-to-duncan-sabien-on-strawmanning
- Summary: philh (12): it's not generally easy to prove a strawman accusation even when true, and he recalls thinking Davis misunderstood Duncan. Davis (12): "strawmanning" implies *culpable* misreading and needs an explanation to be credible. He gives his own examples (Kerr in the pronoun post; Ozy's critique of his TCWMFM reply). He argues that expecting critics to pass an ITT first would interfere with "people telling me when my ideas are bad, and _I need people to tell me when my ideas are bad_". philh: failure to demonstrate isn't strong evidence of falsehood; long-run patterns between Davis and Duncan are "almost certainly part of the picture". LVSN and lahwran on "mind-reading".
- Quotes:
- (https://www.lesswrong.com/posts/5zjucvhSFvp92eYbE/reply-to-duncan-sabien-on-strawmanning?commentId=nJJjtbGQrv3GbdSw3, Davis, 12 karma)
> The reason I disagree with this is because I think it's surprisingly often possible to find flaws in ideas _without_ too fine-grained of a shared understanding; I think expecting critics to pre-emptively pass my ITT would interfere with people telling me when my ideas are bad, and _I need people to tell me when my ideas are bad_.
- (https://www.lesswrong.com/posts/5zjucvhSFvp92eYbE/reply-to-duncan-sabien-on-strawmanning?commentId=e33nzubHaEqvqoaAq, philh, 4 karma)
> In both cases, I think failure on Duncan's part to demonstrate the accusation, is not strong evidence that the accusation is false.

### 2023-02-12 · Conflict Theory of Bounded Distrust
- Path: `reception_data/lw_threads/2023-02-12_conflict-theory-of-bounded-distrust.md` · 33 comments (Davis 1) · https://www.lesswrong.com/posts/DpTexwqYtarRLRBYi/conflict-theory-of-bounded-distrust
- Summary: **gjm (51, top)** objects to the reading of Scott Alexander's "Bounded Distrust". The "hostile environment" passage concerns a Stalin-era hypothetical, not the contemporary US. Alexander doesn't say authorities argue in good faith. The cop-bribery case is a "category mistake" for conflict/mistake theory. "Revenue enhancements" isn't Kolmogorov-style complicity. He finds a "somewhat-plausibly-deniable side order of 'Boooo to SA'". gjm (23) also says regime supporters see dissidents as enemies too, contrary to the post's closing claim. Aiyen replies that condescending "mistake" framings by regime loyalists are common (pro-war Russians). **Davis (25)** says the setting shouldn't matter qualitatively, and generalizes to an A/B/C model ("_A and B are in cahoots_"). He concedes his "presentation of the core rationality insight got 'contaminated' by inessential details of my political differences with Scott" and that "my intuition might be wrong". Unnamed (9): the post "keeps flipping back and forth" and "smush[es]" concepts. Unnamed (2025): savviness doesn't imply complicity, by the post's own honest-cop example. Viliam (27): advertising puffery is a lie ("'Everyone knows it is an exaggeration' means that it is a *lie*"), hence fraud. MondSemmel: such rules are hard to operationalize. Benito (2024 review): "+4".
- Quotes:
- (https://www.lesswrong.com/posts/DpTexwqYtarRLRBYi/conflict-theory-of-bounded-distrust?commentId=3uP6PxhbHtmL53vkx, gjm, 51 karma)
> And I think *most* of this narrative is wrong. SA is indeed a mistake-theorist, but he conspicuously *doesn't* take that to mean that the mouthpieces of state/cultural/... power should be assumed to be arguing in good faith.
- (https://www.lesswrong.com/posts/DpTexwqYtarRLRBYi/conflict-theory-of-bounded-distrust?commentId=EGwQqnmrvvHX9QWk8, Davis, 25 karma)
> I'm a little worried that my presentation of the core rationality insight got "contaminated" by inessential details of my political differences with Scott
- (https://www.lesswrong.com/posts/DpTexwqYtarRLRBYi/conflict-theory-of-bounded-distrust?commentId=wzBaKCEXCFkSJTbo7, Unnamed, 9 karma)
> A bunch of things in this post seem wrong, or like non sequitors, or like they're smushing different concepts together in weird ways.

### 2023-02-26 · "Rationalist Discourse" Is Like "Physicist Motors"
- Path: `reception_data/lw_threads/2023-02-26_rationalist-discourse-is-like-physicist-motors.md` · 153 comments (Davis 24) · https://www.lesswrong.com/posts/SX6wQEdGfzz7GKYvp/rationalist-discourse-is-like-physicist-motors
- Summary: **The most extensive public account by an interlocutor of what it is like to argue with Davis; the Duncan Sabien feud peaks here, with moderator commentary.**
  - **Object-level critiques.** evand (82, top): "physicist motors" did win historically; discourse is just a much harder, higher-dimensional target. steve2152 (43): unlike motors, not all discourse is truth-tracking, so "rationalist discourse" can be a meaningful subset. Raemon (25): the post equivocates between "rationalist" as student of the laws and as practitioner; he calls it "the sort of language trick that you (Zack) are often (rightfully) annoyed at", and later "sleight-of-hand-frame-control" / "frame manipulation". Davis concedes the analogy rests on the "one who studies" definition and asks whether he must disclaim it. ben-lang and Leviad: guidelines exist to help people make any engine at all. Vladimir_Nesov (20) supports Davis against "inflation of 'rationality'". **RobbBB (Bensinger, author of the criticized "Elements"):** "Seems great to me! I share your intuition that Goodwill seems a bit odd to include", and hopes the list is "the start of a conversation". Benito (2024 review): disagrees with the core analogy but finds the critique of "goodwill" "pretty good".
  - **Duncan_Sabien:** the post is "an overt strawman". "Repeated past experience shows that further engagement would be extremely un-worthwhile." Then (19): Davis is "*irrationally* fixated on being anti-polite", with "some kind of self-reinforcing *algorithmic intent* to be abrasive", resembling "a trauma-response type overreaction". "There's something here that uses Zack as its puppet and mouthpiece". After Davis's reply (that Duncan bans critics, while Davis would "never, _ever_ ban gjm"): "This whole comment is a psy-op ... **FUCK.** Enjoy your sanctimony. You are choosing to make the world worse." Later: "You basically *extort* effort from people, with your long-winded bad takes". Duncan cites "three *specific, known* essays that I have not posted" because of Zack and Said. "I tried blocking, and that wasn't enough to get you to leave me alone. Sounds like you win."
  - **Davis's responses:** a narrow apology for his 4 Dec 2021 "This is insane" comment on Duncan's draft. On learning the draft had addressed his objection, a fuller apology: "I am embarrassed at my negligence", with a commitment "to emotionally cool down and read more carefully before posting a comment, when I notice that I'm tempted to post a comment while emotionally activated". He calls Duncan's psychoanalysis "pretty good" and "strong-upvoted". He bites the bullet that he takes "pride and pleasure in criticizing work that I think is importantly mistaken", and says "I'm not always here to collaborate. Sometimes I'm here to criticize." He is "viscerally terrified" of what politeness standards "degrade to in practice". His Mallory thought-experiment: criticism must not require the author's consent.
  - **Moderators and others.** Raemon (19): "I do want to note I agree pretty strongly with this characterization" (of Duncan's). In "somewhat in my mod voice": "yes, Zack, I also would like you to stop lying by exaggeration/overconfidence" (not yet a site norm). His example is a private conversation in which Davis called someone "blatantly lying". Davis: he's "much more prone to exaggerate in real-time conversations". Vaniver (32) warns of survivorship bias: Zack and Said may supply counterfactual criticism, and the debate over rules shouldn't be held under one side's rules. dxu (24): if Zack can make readers think a post said X when it said Y, the subject was probably fuzzy to begin with. jimmy (24) gives a long, sympathetic-but-critical analysis: "should" talk looks away from what *is*, plus a toes-and-cleats analogy for mutual trauma responses. sil-ver (10): "I had zero complaints about their conduct", and is more likely to click Zack's posts. Ninety-Three (12): the behavior Raemon means is that "you *soapbox*". SaidAchmiz defends Davis throughout, and Duncan says goodbye to him too.
- Quotes:
- (https://www.lesswrong.com/posts/SX6wQEdGfzz7GKYvp/rationalist-discourse-is-like-physicist-motors?commentId=RXvRgeniTp37EDYDx, evand, 82 karma)
> But "discourse" is a much more complex target, with extremely high dimensionality, and no easy way to simply win out in the market. So showing what a better approach looks like takes a huge amount of work and care, not only to develop it, but even to show that it's better and why.
- (https://www.lesswrong.com/posts/SX6wQEdGfzz7GKYvp/rationalist-discourse-is-like-physicist-motors?commentId=iv33MbFyGmxg8MK72, Duncan_Sabien, 19 karma)
> I don't see us all as in clear agreement; I think we're at least somewhat in *nominal* agreement but I have found Zack to be ... I don't mean this as a contentless insult, I mean it as a literal attempt-to-model ... *irrationally* fixated on being anti-polite, and *desperately* fending off attempts to validate or encode any kind of standard or minimum bar of politeness.
- (https://www.lesswrong.com/posts/SX6wQEdGfzz7GKYvp/rationalist-discourse-is-like-physicist-motors?commentId=gN8yWfnAHFBjA84qZ, Raemon, 19 karma)
> I think Zack probably *also* agrees with the above during his more self-aware moments, but often not in the middle of a realtime discussion.
- (https://www.lesswrong.com/posts/SX6wQEdGfzz7GKYvp/rationalist-discourse-is-like-physicist-motors?commentId=6sGr4SdWJjtzvKH5w, Duncan_Sabien, 3 karma)
> Enjoy your sanctimony. You are choosing to make the world worse.
- (https://www.lesswrong.com/posts/SX6wQEdGfzz7GKYvp/rationalist-discourse-is-like-physicist-motors?commentId=oa7tgDvhac6XFcmWy, Davis, 30 karma)
> I'm not always here to collaborate. Sometimes I'm here to criticize. I endorse this on reflection.
- (https://www.lesswrong.com/posts/SX6wQEdGfzz7GKYvp/rationalist-discourse-is-like-physicist-motors?commentId=NpuG7GZWmdxfZ3MTB, Davis, 6 karma)
> **To avoid such errors in the future, I will endeavor to take some time to emotionally cool down and read more carefully before posting a comment, when I notice that I'm tempted to post a comment while emotionally activated.**
- (https://www.lesswrong.com/posts/SX6wQEdGfzz7GKYvp/rationalist-discourse-is-like-physicist-motors?commentId=KNXeKNfmEk7pe2j4s, Duncan_Sabien, 1 karma)
> (Like, there are three *specific, known* essays that I have not posted, because of my expectations coming off of this thread and the chilling effect of "I'll have to deal with Zack and Said's responses.")
- (https://www.lesswrong.com/posts/SX6wQEdGfzz7GKYvp/rationalist-discourse-is-like-physicist-motors?commentId=3LxZuziEWgaedwr7k, Raemon, 5 karma)
> Speaking *somewhat* in my mod voice, I do basically also want to say "yes, Zack, I also would like you to stop lying by exaggeration/overconfidence".
- (https://www.lesswrong.com/posts/SX6wQEdGfzz7GKYvp/rationalist-discourse-is-like-physicist-motors?commentId=hehkaXqsbHnhqac8T, Vaniver, 32 karma)
> I think it's important to note survivorship bias here; I think there are other people who used to post on LessWrong and do not anymore, and perhaps this was because of changes in norms like this one.
- (https://www.lesswrong.com/posts/SX6wQEdGfzz7GKYvp/rationalist-discourse-is-like-physicist-motors?commentId=eByENaTnaiZetqp8o, RobbBB, 15 karma)
> Seems great to me! I share your intuition that Goodwill seems a bit odd to include. I think it's right to push back on proposed norms like these and talk about how justified they are, and I hope my list can be the start of a conversation like that rather than the end.
- (https://www.lesswrong.com/posts/SX6wQEdGfzz7GKYvp/rationalist-discourse-is-like-physicist-motors?commentId=YtLRi52NXdhGnaJrF, sil-ver, 10 karma)
> I think I should just add my own data point here, which is that Zack and I have been on polar opposites sites of a pretty emotional debate before, and I had zero complaints about their conduct.

### 2023-03-12 · "You'll Never Persuade People Like That"
- Path: `reception_data/lw_threads/2023-03-12_you-ll-never-persuade-people-like-that.md` · 31 comments (Davis 1) · https://www.lesswrong.com/posts/67NrgoFKCWmnG3afd/you-ll-never-persuade-people-like-that
- Summary: Mostly pushback on the post's diagnosis that the phrase "*really* means" "You are starting to persuade *me* against my will". Kaj_Sotala (34): he says it when someone is "shooting themselves and others in the foot", not when he is being persuaded. gjm (22): the phrase means "several different things on different occasions, and usually it doesn't mean what Zack says it always means". SaidAchmiz (21) offers a war-negotiation reading: "You won't persuade any Bs like that, and we both know it". haha-no: the "this is what your interlocutor *really* means" framing is "likely to lead to doubling down when *slowing* down would have been the appropriate response". tailcalled says he uses the phrase about Blanchardian arguments. yair-halberstadt gives a genuine-advice example (agunah book). Vladimir_Nesov (15): people acting for groups have socially real "bosses". A deleted user praises the chicken/steering-wheel passage.
- Quotes:
- (https://www.lesswrong.com/posts/67NrgoFKCWmnG3afd/you-ll-never-persuade-people-like-that?commentId=sj5sapBuzwznQehzi, gjm, 22 karma)
> I think "you'll never persuade people like that" means several different things on different occasions, and usually it doesn't mean what Zack says it always means.
- (https://www.lesswrong.com/posts/67NrgoFKCWmnG3afd/you-ll-never-persuade-people-like-that?commentId=iqD5d7DzNyyS6PXzz, Kaj_Sotala, 34 karma)
> I don't think it's at all the case that the person is starting to convince me in those situations - rather the opposite, in that I have a massively negative reaction to what they are saying, and then I typical-mind my experience to say that everyone else is also likely to.

### 2023-05-14 · Bayesian Networks Aren't Necessarily Causal
- Path: `reception_data/lw_threads/2023-05-14_bayesian-networks-aren-t-necessarily-causal.md` · 39 comments (Davis 3) · https://www.lesswrong.com/posts/qPrPNakJBq23muf4n/bayesian-networks-aren-t-necessarily-causal
- Summary: Technical. **johnswentworth (35):** "First crucial point which this post is missing": the intuitively right net uses fewer parameters (8 vs. 9), so it is favored before any interventions. Causality matters because instances differ by simple interventions; no "ontologically-special 'outside agent'" is needed. Davis cites the Bayesian score in Koller & Friedman. LGS presses: is correlation enough for causal structure? A long exchange (Wentworth: weak assumptions suffice). Richard_Kennaway (9) and Caspar42 (quoting Pearl's epilogue): interventions are integral to causation, and Yudkowsky's post "is not reliable on this point". gjm asks about "Daphne Koller and the other guy"; Davis says it's characterization of a "casual formal epistemology fan" in a second-person story. martin-randall (2024 review): "slightly let down".
- Quotes:
- (https://www.lesswrong.com/posts/qPrPNakJBq23muf4n/bayesian-networks-aren-t-necessarily-causal?commentId=ZuqLAJkfqqLFMoNdk, johnswentworth, 35 karma)
> Implication of this for causal epistemics: we have two models which make the same predictions on-distribution, and only make different predictions under interventions. Yet, even without actually observing any interventions, we do have reason to epistemically favor one model over the other.

### 2023-06-05 · We Are Less Wrong than E. T. Jaynes on Loss Functions in Human Society
- Path: `reception_data/lw_threads/2023-06-05_we-are-less-wrong-than-e-t-jaynes-on-loss-functions-in-human.md` · 15 comments (Davis 2) · https://www.lesswrong.com/posts/65hFPABegiB9uGFiC/we-are-less-wrong-than-e-t-jaynes-on-loss-functions-in-human
- Summary: AllAmericanBreakfast (25): the quoted passage is about *humans*, not generalized agents. "If you're going to call a passage of ET Jaynes' 'silly,' you have to be right on the money to get away with it!" Davis: "Thanks. We don't seem to have a 'That's fair' or '_Touché_' react". Others (iceman: Girardian mimesis; adrian-arellano-davin; Amyr) defend Jaynes's point. Nisan: identical selfish agents can trade.
- Quotes:
- (https://www.lesswrong.com/posts/65hFPABegiB9uGFiC/we-are-less-wrong-than-e-t-jaynes-on-loss-functions-in-human?commentId=Rrtb2Ld9ysKRcctuv, AllAmericanBreakfast, 25 karma)
> If you're going to call a passage of ET Jaynes' "silly," you have to be right on the money to get away with it!

### 2023-07-08 · Blanchard's Dangerous Idea and the Plight of the Lucid Crossdreamer (memoir part 1)
- Path: `reception_data/lw_threads/2023-07-08_blanchard-s-dangerous-idea-and-the-plight-of-the-lucid.md` · 136 comments (Davis 12) · https://www.lesswrong.com/posts/RxxqPH3WffQv6ESxj/blanchard-s-dangerous-idea-and-the-plight-of-the-lucid
- Summary: **The main LW reception of Davis's object-level sexology and memoir. Many commenters write in the first person as trans, AGP, or sexual-minority readers.** (Their self-disclosures are public, but the study should cite them sparingly and by username only.)
  - **Sympathetic or endorsing.** Benito (30): "one of my favorite LW posts in recent months!", as "an account of someone who believes a heresy grappling with a hostile epistemic environment", while not endorsing the claims "nor the author as a totally reliable narrator". tracingwoodgrains (32): morphological freedom is the better public case. "People like Zack are in a miserable position, because the narrative they present of their experience is deeply inconvenient for the majority of people who feel similarly to them and thoroughly convenient to those who hate them". He finds Davis's account "much closer to what appears to be the underlying truth". Yoav Ravid: "by far the clearest one ... And I think it's correct", though the subculture isn't "just fake". dipanjan, a self-described AGP man: "Coming across Blanchard's work saved my life twenty years ago." FeepingCreature: Zack voices "things that I've thought and felt secretly for a long time". elityre: the anti-correlated-nodes paragraphs were "extremely helpful".
  - **Critical.** tailcalled (38): "The rationalist community seems complicit in dishonesty about trans matters". But he says Phil Illy's book treats AGP feelings as delusion, in tension with Davis. The "social behavior, interests" HSTS markers are "gender conservative propaganda" (Lippa data). Zucker chaired the DSM-5 section, and right-wing science is "a fractal of manipulation". ann-brown (37), a cis woman: her experience maps onto "autogynephilia". tailcalled: cis-female AGP exists, which refutes a strong claim in the post. Muireall (12): most trans people "just want to live the way they choose", and "your friends who egged you on ... were not acting in your interests". adrusi (27), a late-onset non-AGP trans woman: the shared autistic-programmer cluster suggests a common cause, not a fetish. Davis replies that the cluster still "undermines the slogan", and he can't believe in an intersex condition "that has no particular symptoms other than a mysterious desire to be female". Hivewired: Blanchardism "leaves no room for an actual agent that makes choices". vedrfolnir draws mania/repression parallels. Kevin92 (16), a trans rationalist: the post "is not a healthy way of addressing your gender dysphoria", and has "a lot of self-hate in it". JohnWittle (28) calls that response "incredibly rude and frankly bizarre ... I would almost go so far as to call it hateful". Davis: "given that I'm questioning other people's life stories, it seems only fair that they be allowed to question mine? I can take it!" sinclair-chen (38): "this post is tooo looong ... I think you're crazy to not update on evidence sooner". Jessica Taylor (27) on "Am I trans?", gender identity as coerced, and repressed-drive theory as "an arb opportunity" rather than "Ultimate Truth". Ozzalus: Seattle trans narratives do argue for morphological freedom. Davis objects to "self-labeling freedom" because "labels are supposed to objectively describe something in the territory".
  - **Moderation sub-thread.** Benquo (−33) frames a commenter's anecdote as "either confessing on the public internet to committing assault" or bad inference. Ruby (mod, 23) warns of "escalating moderator action". Davis (18): "you're not passing Benquo's ideological Turing test ... you're threatening to censor him". He points to his "Easy Going" moderation setting and says: "I continue to be disappointed with the censorious attitudes of the _Less Wrong_ 2.0 team, which I consider deeply anti-intellectual." Ruby explains how authors can opt into laxer norms on their own posts.
- Quotes:
- (https://www.lesswrong.com/posts/RxxqPH3WffQv6ESxj/blanchard-s-dangerous-idea-and-the-plight-of-the-lucid?commentId=KKRPaGTCiJKcrmGyT, Benito, 30 karma)
> I have no interest in gender as a topic but it's very interesting to read an account of someone who believes a heresy grappling with a hostile epistemic environment — including reading the details of which comments or messages ended up having a large effect on your thinking and trajectory.
- (https://www.lesswrong.com/posts/RxxqPH3WffQv6ESxj/blanchard-s-dangerous-idea-and-the-plight-of-the-lucid?commentId=ktB5FzgaKRdh5b2DD, tracingwoodgrains, 32 karma)
> People like Zack are in a miserable position, because the narrative they present of their experience is deeply inconvenient for the majority of people who feel similarly to them and thoroughly convenient to those who hate them
- (https://www.lesswrong.com/posts/RxxqPH3WffQv6ESxj/blanchard-s-dangerous-idea-and-the-plight-of-the-lucid?commentId=bj2c2rKzYrQaCE85u, tailcalled, 38 karma)
> The rationalist community seems complicit in dishonesty about trans matters.
- (https://www.lesswrong.com/posts/RxxqPH3WffQv6ESxj/blanchard-s-dangerous-idea-and-the-plight-of-the-lucid?commentId=bj2c2rKzYrQaCE85u, tailcalled, 38 karma)
> "Social behavior, interests, &c" is as far as I can tell gender conservative propaganda that Blanchardians made up in order to make it fit with the grand HBD narrative about gender differences.
- (https://www.lesswrong.com/posts/RxxqPH3WffQv6ESxj/blanchard-s-dangerous-idea-and-the-plight-of-the-lucid?commentId=C89tMWHGtqbysqr9x, ann-brown, 37 karma)
> I am a bisexual cisgender woman who finds my own body interesting in a way that indeed appears to map to that described by this "autogynephilia" you speak of, and only wouldn't because the very definition tries to include being male.
- (https://www.lesswrong.com/posts/RxxqPH3WffQv6ESxj/blanchard-s-dangerous-idea-and-the-plight-of-the-lucid?commentId=kAfoyuDvWccZjGgkJ, adrusi, 27 karma)
> Instead of supposing that most late-onset trans women were motivated to transition by their fetish, while I was motivated by some other factor, and that it's *just a coincidence* that we happen to also share a lot of peculiar features, it would be more parsimonious to say that among these characteristics that we share is some psychological factor that motivated all of our transitions, and which also causes most of us to develop autogynephilic fetishes.
- (https://www.lesswrong.com/posts/RxxqPH3WffQv6ESxj/blanchard-s-dangerous-idea-and-the-plight-of-the-lucid?commentId=g9rHdmArWzxtniskb, Kevin92, 16 karma)
> This essay has a lot of self-hate in it which is self-destructive and although I respect your Freedom of Speech and Bodily Autonomy I think it would be unwise for anyone to emulate Zach.
- (https://www.lesswrong.com/posts/RxxqPH3WffQv6ESxj/blanchard-s-dangerous-idea-and-the-plight-of-the-lucid?commentId=wuXt62vfxkaHZJkq5, Davis, 6 karma)
> I appreciate the support, but given that [I'm questioning other people's life stories](http://unremediatedgender.space/2016/Sep/psychology-is-about-invalidating-peoples-identities/), it seems only fair that they be allowed to question mine? I can take it!
- (https://www.lesswrong.com/posts/RxxqPH3WffQv6ESxj/blanchard-s-dangerous-idea-and-the-plight-of-the-lucid?commentId=PLomfXzdfd9dmJqw6, dipanjan, 4 karma)
> Coming across Blanchard's work saved my life twenty years ago.
- (https://www.lesswrong.com/posts/RxxqPH3WffQv6ESxj/blanchard-s-dangerous-idea-and-the-plight-of-the-lucid?commentId=8dKKsvoDXmw9wtxRT, Davis, 18 karma)
> I continue to be disappointed with the censorious attitudes of the _Less Wrong_ 2.0 team, which I consider deeply anti-intellectual.
- (https://www.lesswrong.com/posts/RxxqPH3WffQv6ESxj/blanchard-s-dangerous-idea-and-the-plight-of-the-lucid?commentId=ApWLfjHwM2EvpqdJv, Davis, 10 karma)
> I could believe that sensitive, shy, spectrumy male programmers tend to find the trans community narrative appealing separately from whether they happen to be AGP, but I really, really have trouble believing in a _bone fide_ intersex condition that has no particular symptoms other than a mysterious desire to be female.

### 2023-07-15 · A Hill of Validity in Defense of Meaning (memoir part 2)
- Path: `reception_data/lw_threads/2023-07-15_a-hill-of-validity-in-defense-of-meaning.md` · 121 comments (Davis 14) · https://www.lesswrong.com/posts/ZjXtjRQaD2b4PAser/a-hill-of-validity-in-defense-of-meaning
- Summary: **The post's karma was low relative to its vote count.** Davis's 2025 self-review gives it 8 karma in 97 votes and calls this "nakedly political". The comments split into several distinct debates.
  - **The accusations against Yudkowsky, Scott Alexander, and others.** lc (39) agrees with most object-level takes but finds the attributed dishonesty "comically exaggerated", and a long criticism "nebulous and pathological". Maxc (5) reports no negative updates about the people named. Davis offers him $40 to give actual arguments. Maxc (24) accepts, citing social pressure rather than money, and lists objections: unjustified mind-reading ("couldn't be bothered", "for transparently political reasons"), "Loaded framing", and a model of the community as more centralized than it is. Davis concedes "transparently" "definitely isn't right". He defends "prevaricate" with the 2008 "words can be wrong" versus 2018 "not standing in defense of truth" contrast, and later apologizes for mixing the cheerful-price mechanism with social pressure. Wei_Dai (15) asks how Davis and Ben Hoffman ruled out mere Kolmogorov complicity before the "run out the clock" charge. Davis calls the original closing paragraphs "egregiously terrible writing on my part" and rewrites them, saying he is "not conjecturing anything worse than Kolmogorov complicity". iceman, a six-figure MIRI donor, reads the post as saying Yudkowsky "decided to just live off our donations". SaidAchmiz, Raemon, jimrandomh (62), and martin-randall dispute that reading, and Raemon calls it "basically obviously false".
  - **Raemon's synthesis** (34, then 20). He agrees that Scott's "There's no rule of rationality saying that I shouldn't" claim should be retracted, but lists other causes besides political motivation. Among them: since 2018 Davis has had "a pretty strong vibe of 'seeming to relate to this in a zealous and unhealthy way'", and "both are true at the same time". He weights politics at "maybe like 30-45%" of the causality. Davis replies that his conclusion is "_there is no "we"_", and that he is now more interested in breaking "the delusion that the ingroup has a monopoly on Truth and Goodness".
  - **A private email quoted.** Benito doubts the post's paraphrase of a Scott Alexander remark. Davis quotes the 17 March 2019 email exchange in the comment. Benito: the email "does change my understanding of what he meant", and he "wouldn't personally have shared it without permission".
  - **Object-level debates.** tailcalled (32): psychological-sex-differences research works as "a counterstory against feminist ideology", and the rationalist community is "irrational/dishonest about trans topics" partly in defence against an equally dishonest conservative/HBD coalition. localdeity (30, 29) disputes tailcalled's characterization of the Damore memo and his examples of bad differential psychology, at length. Davis replies that he hopes to reason about "sex differences in the physical universe" via named effect sizes. cata (9): use precise categories for truth-seeking but accommodating language elsewhere, and asks why that should be a problem. Chris_Leong: Scott's "language game" is valid, but its "weaponisation" is a separate matter. elityre (2024) reads Yudkowsky's 2018 tweets as a facts-vs-policy point; he later revises in light of a Yudkowsky Facebook clarification. sinclair-chen proposes "aspiring woman". green_leaf (−40) calls the post "transphobic". Davis presses him to name a specific unargued claim ("Reply!").
  - **MIRI settlement sub-thread.** The post's mention of MIRI's settlement with the former employee behind the "MIRICult" site prompts habryka (34) to give his understanding: there was no payout and the salacious claims were "completely made up". A long blackmail/danegeld game-theory exchange follows (SaidAchmiz, habryka, jimrandomh; a David Hornbein dialogue, 42). This concerns third parties more than Davis's arguments; the study should mention it only if needed.
- Quotes:
- (https://www.lesswrong.com/posts/ZjXtjRQaD2b4PAser/a-hill-of-validity-in-defense-of-meaning?commentId=xspHf9SaxSwyi3kcj, lc, 39 karma)
> At the same time, the amount of motivated reasoning and dishonesty you attribute to this community and Yudkowsky in particular as a result of these passing comments seems comically exaggerated.
- (https://www.lesswrong.com/posts/ZjXtjRQaD2b4PAser/a-hill-of-validity-in-defense-of-meaning?commentId=FfR2dy5SpqcBBdeMr, Davis, 4 karma)
> The reason I'm telling this Whole Dumb Story about people instead of just making object-level arguments about ideas, is that I tried making object-level arguments about ideas _first_, for seven years, and it wasn't very effective. At some point, I think it makes sense to jump up a meta level and try to reason about people to figure out why the ideas aren't landing.
- (https://www.lesswrong.com/posts/ZjXtjRQaD2b4PAser/a-hill-of-validity-in-defense-of-meaning?commentId=HFnxHemAac8Zndh9k, Maxc, 24 karma)
> Basically everywhere you speculate about someone's internal motivations or thoughts, or claim that someone is doing something for political reasons or status reasons or energy reasons, I think you're failing to consider alternate hypotheses adequately, starting from false or misleading premises, or drawing conclusions unjustifiably.
- (https://www.lesswrong.com/posts/ZjXtjRQaD2b4PAser/a-hill-of-validity-in-defense-of-meaning?commentId=jybJ3wSkZy2qYezxn, Davis, 14 karma)
> In retrospect, I feel guilty about impulsively mixing the "cheerful price" mechanism and the "social pressure" mechanism.
- (https://www.lesswrong.com/posts/ZjXtjRQaD2b4PAser/a-hill-of-validity-in-defense-of-meaning?commentId=xAkE8zwkSNivfQZBD, Wei_Dai, 15 karma)
> How did you/Ben rule out the Kolmogorov complicity hypothesis (i.e., that Eliezer still had genuine intellectual or altruistic aims that he wanted to protect)?
- (https://www.lesswrong.com/posts/ZjXtjRQaD2b4PAser/a-hill-of-validity-in-defense-of-meaning?commentId=AYBxuPapDy2p9fRHQ, Davis, 15 karma)
> I'm not conjecturing anything worse than Kolmogorov complicity. (And the 2021 MIRI conversations were great.) I do think political censorship is significantly more damaging to epistemic conditions than many others seem to.
- (https://www.lesswrong.com/posts/ZjXtjRQaD2b4PAser/a-hill-of-validity-in-defense-of-meaning?commentId=7tcbr6t5FEAKknPpt, Raemon, 20 karma)
> It's hard to tell the difference between "people are avoiding the real conversation due to leftist political reasons" and "people are avoiding the conversation because you just seem... a little crazy". It's especially hard to tell the difference when *both are true at the same time.*
- (https://www.lesswrong.com/posts/ZjXtjRQaD2b4PAser/a-hill-of-validity-in-defense-of-meaning?commentId=cKsLbSNzmGqymqgeY, Davis, 16 karma)
> My position at the time was, "Scott should retract it and we should all agree he should retract it". Since that didn't happen despite absurd efforts, my conclusion is more that _there is no "we"_.
- (https://www.lesswrong.com/posts/ZjXtjRQaD2b4PAser/a-hill-of-validity-in-defense-of-meaning?commentId=nCu6Ave9EMgqtgsue, tailcalled, 32 karma)
> I think "psychological sex differences" ideology is energetically unable to acknowledge these sorts of things because its main purpose/motivation is to function as a counterstory against feminist ideology, and so the point is not to accurately describe the world but instead to deny cultural factors.
- (https://www.lesswrong.com/posts/ZjXtjRQaD2b4PAser/a-hill-of-validity-in-defense-of-meaning?commentId=H8FDevJXMcNdXgX7g, Benito, 4 karma)
> (I am personally confused about the exact lines for sharing 1-1 text exchanges publicly and I wouldn't personally have shared it without permission in your shoes. I don't mean by this to say I think you necessarily shouldn't have.)
- (https://www.lesswrong.com/posts/ZjXtjRQaD2b4PAser/a-hill-of-validity-in-defense-of-meaning?commentId=WGPCJMXBGdcxxonhg, Davis, 8 karma, 2025)
> The 8 karma in 97 votes is kind of funny in how nakedly political it is. (I think it was higher before the post got some negative attention on Twitter.)

### 2023-07-23 · "Justice, Cherryl."
- Path: `reception_data/lw_threads/2023-07-23_justice-cherryl.md` · 21 comments (Davis 1) · https://www.lesswrong.com/posts/vfjptEJ2oahLqRyZz/justice-cherryl
- Summary: The comments divide between the post's claim that "collaborative truth-seeking doesn't exist" and its reading of Ayn Rand.
  - **Collaborative truth-seeking.** Vladimir_Nesov (44) recasts charity as learning another's "cognitive dialect", not as a preference for someone being right. Benquo (26) agrees that people who *ask* for "collaborative truth-seeking" are lying, but holds that the practice exists: active listening, interpretive labor, offering considerations rather than a party line. jimrandomh says "principle of charity" conflates conversational skill with accusations of bad priors or malice. benwr: the bias toward one's own ideas is not contingent but follows from reputational stakes. Seth Herd: these are spectra, not categories, and another problem with "obviously wanting to be right is that it's simply irritating". Viliam: the accusation is not lying but "behaviors that minimize your chances of figuring out when you are wrong". MondSemmel (14): it clarified the early-2023 LW moderation conflict. Benito (2024) cast a positive review vote "even though I disagree with many parts of it".
  - **Rand.** A deleted user (12) says Davis "profoundly misunderstood Ayn Rand's novels" by attributing descriptive egoism to her. Davis (17) concedes that the post is a Death-of-the-Author reading, denies arguing for descriptive egoism, and cites two _Fountainhead_ passages where conventional usage is lampshaded. Thenamelessone, a self-described neo-objectivist (22): the missing concept is "benevolence". tailcalled (2024) reads the post's stance as closer to Peter Keating than to Roark.
- Quotes:
- (https://www.lesswrong.com/posts/vfjptEJ2oahLqRyZz/justice-cherryl?commentId=FAdtLazLDsLH3b7db, Benquo, 26 karma)
> It's true that people who ask for "collaborative truth-seeking" are lying, but false that no one does it.
- (https://www.lesswrong.com/posts/vfjptEJ2oahLqRyZz/justice-cherryl?commentId=LoY9aCBvdTbA8b6u3, Viliam, 13 karma)
> I guess the accusation is not that you are lying, but that you are engaging in behaviors that minimize your chances of figuring out when you are wrong.
- (https://www.lesswrong.com/posts/vfjptEJ2oahLqRyZz/justice-cherryl?commentId=GTjhXovJFDyrg5ziP, Davis, 17 karma)
> I interpret Roark's remark that "maybe the concepts don't make sense" as amounting to the claim that conventional usage of "selfish" as self-benefitting and "altruism" as other-benefitting, doesn't [carve the reality](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries) of human psychology at the joints: benevolence towards others flows out of shared values; unconditional regard others-in-general is unnatural.

### 2023-08-02 · Is There Anything That's Worth More
- Path: `reception_data/lw_threads/2023-08-02_is-there-anything-that-s-worth-more.md` · 6 comments (Davis 1) · https://www.lesswrong.com/posts/bqZwWQCai6iAjy4Xq/is-there-anything-that-s-worth-more
- Summary: Minimal. M. Y. Zuo praises the "concise example". FeepingCreature glosses it for a confused reader: under uncertain timelines, don't overstress. A lyric correction is acknowledged by Davis.

### 2023-07-31 · Lack of Social Grace Is an Epistemic Virtue
- Path: `reception_data/lw_threads/2023-07-31_lack-of-social-grace-is-an-epistemic-virtue.md` · 114 comments (Davis 16) · https://www.lesswrong.com/posts/h2Hk2c2Gp5sY4abQh/lack-of-social-grace-is-an-epistemic-virtue
- Summary: Heavily engaged and mostly critical of the thesis as stated. The most-upvoted comment is by a deleted user (65) whose text is gone; SaidAchmiz's reply shows it argued that LessWrongers are "the last people who need to be told to be less socially graceful".
  - **Vaniver (86):** in Shapin's _A Social History of Truth_, gentlemanly honor culture and politeness were foundational to the Royal Society, which was concerned with "keeping the conversation going". Politeness is "about" avoiding conflict.
  - **Raemon (53):** "thick skin, social courage(and/or obliviousness), and tact are *all* epistemic virtues". The post doesn't engage with "how to build a truthseeking *institution*". He adds: "My past experience is you're kinda ideological about this ... you'll keep generating reasons for not having to learn tact no matter what I say".
  - **Davis's reply (5):** thanks him for "a specific way in which you think I'm being systematically dumb" and answers the cruxes. He says he interprets feelings of unsafety as possible "decision-theoretic extortion", and that "institutions are often dumber than their members". A footnote reports disappointment with Ben, Jessica, and Michael's recent performance: "I want to figure out how to sic Said on them."
  - **Raemon's "safety" exchange.** Raemon says a truth-tracking community should do whatever is cheapest, including learning not to trigger physiological responses. Davis replies with a mocking garble of the phrase ("troop-tricking comity", "roof-tacking impunity") and asks what membership benefits it offers.
  - **Other critics.** romeostevensit (29): social graces maintain cooperative equilibria; he has seen the thesis IRL as "motivated reasoning about the person's underlying proclivity towards disagreeableness". aristide-twain (24): much politeness is pretend-obfuscation; Davis: "what that amounts to is the claim that anyone who _was_ fooled, isn't 'somebody'." philh (33): the Feynman anecdote contains no one who hedges politely, so it doesn't support the claim; Davis: "You know, that's a good point!". philh's 2024 review (16) rates it −1 as unclear and unargued. Seth Herd's review (17): "Lack of social grace is very much not an epistemic virtue." MondSemmel (19), T3t, Ape in the coat (14, "Strong downvote") also object.
  - **Supporters.** SaidAchmiz (34) disputes the _Invention of Lying_ example but says he agrees wholeheartedly with its thesis. interstice argues socially graceful phrasings are a residue of past deception.
- Quotes:
- (https://www.lesswrong.com/posts/h2Hk2c2Gp5sY4abQh/lack-of-social-grace-is-an-epistemic-virtue?commentId=73TbLZc2qoA9CkGnm, Vaniver, 86 karma)
> One of its core claims is that the "social graces" of English gentility were a fundamental component of the Royal Society and the beginnings of empirical science.
- (https://www.lesswrong.com/posts/h2Hk2c2Gp5sY4abQh/lack-of-social-grace-is-an-epistemic-virtue?commentId=jtNBbnyi5jdiwtkKE, Raemon, 53 karma)
> My overall claim is that thick skin, social courage(and/or obliviousness), and tact are *all* epistemic virtues.
- (https://www.lesswrong.com/posts/h2Hk2c2Gp5sY4abQh/lack-of-social-grace-is-an-epistemic-virtue?commentId=jtNBbnyi5jdiwtkKE, Raemon, 53 karma)
> My sense is that you'll keep generating reasons for not having to learn tact no matter what I say, and meanwhile it's not very fun and I don't think this is actually near the top of the list of things I could focus on to increase the rate of intellectual progress on LessWrong (which looks less like engaging in internet arguments and more like doing some of the less exciting parts of research and engineering).
- (https://www.lesswrong.com/posts/h2Hk2c2Gp5sY4abQh/lack-of-social-grace-is-an-epistemic-virtue?commentId=EE8FMAReFpcdwCWt2, Davis, 5 karma)
> I suspect a crux there is that I'm more likely to interpret feelings of unsafety as a [decision-theoretic extortion attempt](http://unremediatedgender.space/2018/Jan/dont-negotiate-with-terrorist-memeplexes/), that sometimes people feel unsafe because the elephant in their brain can predict that others will offer to distort shared maps as a concession to make them feel safe.
- (https://www.lesswrong.com/posts/h2Hk2c2Gp5sY4abQh/lack-of-social-grace-is-an-epistemic-virtue?commentId=pJmacr99zPoyjijyh, Davis, 8 karma)
> Sell me on it. If I learn not to communicate in a way that predictably causes certain physiological responses, like your co-mutiny is asking me to do, what concrete, specific membership benefits does the co-mutiny give me in return?
- (https://www.lesswrong.com/posts/h2Hk2c2Gp5sY4abQh/lack-of-social-grace-is-an-epistemic-virtue?commentId=jc5aEQzGhWiJnGak4, romeostevensit, 29 karma)
> I've observed the thesis posited here before IRL and it appeared to be motivated reasoning about the person's underlying proclivity towards disagreeableness.
- (https://www.lesswrong.com/posts/h2Hk2c2Gp5sY4abQh/lack-of-social-grace-is-an-epistemic-virtue?commentId=HcHWfRfbbHhp8mSoj, philh, 33 karma)
> There's no one in the story who says "I don't think that will work" instead of "that won't work", or "that seems like a bad idea" instead of "that's a damn fool idea".
- (https://www.lesswrong.com/posts/h2Hk2c2Gp5sY4abQh/lack-of-social-grace-is-an-epistemic-virtue?commentId=fuoJXmT2owiKLqp4y, Davis, 11 karma)
> The thesis of the post is that people who are trying to maximize the accuracy of shared maps are going to end up being socially ungraceful sometimes, because sometimes social grace calls for obfuscating shared maps.
- (https://www.lesswrong.com/posts/h2Hk2c2Gp5sY4abQh/lack-of-social-grace-is-an-epistemic-virtue?commentId=G6RTYJcqThbpr2dBi, Seth Herd, 17 karma, 2024)
> By all means, strategically violate social customs. But if you irritate people by doing it, you may be advancing your own epistemics by making them talk to you, but you're actually hurting their epistemics by making them irritated with whatever belief you're trying to pitch.

### 2023-08-25 · Assume Bad Faith
- Path: `reception_data/lw_threads/2023-08-25_assume-bad-faith.md` · 69 comments (Davis 3) · https://www.lesswrong.com/posts/e4GBj6jxRZcsHFSvP/assume-bad-faith
- Summary: Better received than the memoir posts: mike_hawke liked "the length, readability, and importance", and MondSemmel found it "Much better than Zack's two recent posts of >20k words". The critical comments are substantive.
  - **Reasons to keep assuming good faith.** ricraz (77): the assumption mitigates one's *own* self-deception and adds forgiveness to an iterated game, and the post's "stick to the object level" advice amounts to a strong "assume good faith" heuristic anyway. Dweomite (43): whether an interlocutor will fold to a strong argument, or loop indefinitely, is exactly what the bias/deception distinction tracks, and it is decision-relevant for when to walk away. steve2152 (33): the distinction matters in two-way conversation, and the terms are "incredibly useful" in everyday life.
  - **Davis's replies.** He says he is articulating "a worldview that our culture doesn't already have standard language for". He admits sometimes "choosing my words carefully" with Twitter ideologues so as to sound like a fellow traveler, and calls this "both" bad faith and effective rhetoric. He calls the title "too punchy to resist".
  - **Other responses.** Ape in the coat finds "something slippery about the ways you write your posts". In the 2024–25 review, sil-ver (19) says Zack seems the "~only person on this platform who is actually doing rationality in a completely straight-forward way as intended". lc: "If you skipped it because of title + author, you probably have the wrong impression". Raemon gives it +4 but suggests a title like "Taboo bad faith". Unnamed: the post never tabooed the term and repeatedly conflates its definition with others'. Davis's self-review claims it partly dissolves "the mystery of disagreement" by recasting many disagreements as "disguised conflicts".
- Quotes:
- (https://www.lesswrong.com/posts/e4GBj6jxRZcsHFSvP/assume-bad-faith?commentId=Sc6RqbDpurX6hJ8pY, ricraz, 77 karma)
> You shouldn't just think of the assumption of good faith as a reaction to other people's lack of self-deception; you should also think of it as a way of mitigating your own self-deception.
- (https://www.lesswrong.com/posts/e4GBj6jxRZcsHFSvP/assume-bad-faith?commentId=u7dmurphFbeqCxuaw, Dweomite, 43 karma)
> If you are committed to giving serious consideration to everything your interlocutor says, then a bad actor can tie you up indefinitely just by continuing to say new things.
- (https://www.lesswrong.com/posts/e4GBj6jxRZcsHFSvP/assume-bad-faith?commentId=hkhmZoE8R8nZuLDTA, Davis, 8 karma)
> Sometimes when I'm in a discussion on Twitter with someone who's more of an ideologue than I am, I end up choosing my words carefully to make it sound like I'm "on their side" to a greater extent than I really am, because I'm afraid that they'd slam the door on me if they knew what I was really thinking, but they might listen to the intellectually substantive point I'm trying to make if I talk like a fellow traveler.
- (https://www.lesswrong.com/posts/e4GBj6jxRZcsHFSvP/assume-bad-faith?commentId=qzZi594sytjZFDzei, sil-ver, 19 karma, 2024)
> ((This post also contributes to this nagging sense that I sometimes have that Zack is the ~only person on this platform who is actually doing rationality in a completely straight-forward way as intended, and everyone else is playing some kind of social game in which other considerations restrict the move set and rationality is only used to navigate within the subset of still permissible moves. I'm not in the business of fighting this battle, but in another timeline maybe I would be.))
- (https://www.lesswrong.com/posts/e4GBj6jxRZcsHFSvP/assume-bad-faith?commentId=nxRpuPTd3XuDwfkFy, Unnamed, 2 karma, 2025)
> Keeping that sort of thing straight is rationality 101 stuff that tabooing words helps with, and which this post repeatedly stumbles over.
- (https://www.lesswrong.com/posts/e4GBj6jxRZcsHFSvP/assume-bad-faith?commentId=P8tNkpAPru8ncf57b, Davis, 11 karma, 2024)
> I claim that this post is significant for articulating a solution to the mystery of disagreement (why people seem to believe different things, in flagrant violation of Aumann's agreement theorem): much of the mystery dissolves if a lot of apparent "disagreements" are actually disguised conflicts.

### 2023-09-13 · Contra Yudkowsky on Epistemic Conduct for Author Criticism
- Path: `reception_data/lw_threads/2023-09-13_contra-yudkowsky-on-epistemic-conduct-for-author-criticism.md` · 40 comments (Davis 1) · https://www.lesswrong.com/posts/pkaagE6LAsGummWNv/contra-yudkowsky-on-epistemic-conduct-for-author-criticism
- Summary: The context is omnizoid's EA Forum post "Eliezer Yudkowsky Is Frequently, Confidently, Egregiously Wrong" and Yudkowsky's claimed "basic rule of epistemic conduct" (object-level refutation before character criticism). Commenters broadly agree omnizoid's post was bad and split on whether the "rule" is epistemic.
  - **Defending the rule.** habryka (25): requiring object-level arguments first "seems pretty reasonable". jimrandomh (28): the true rule concerns the order of evaluation in one's own thinking, and wrong order in writing is Bayesian evidence of wrong order in thinking, compare "appearance of impropriety". Raemon (39) points to Yudkowsky's statement of the rule in _Inadequate Equilibria_ (anti-Bulverism). Maxc: putting attacks first exposes more readers to unsupported attacks.
  - **Siding with Davis.** SaidAchmiz (41): ordering should follow "the rules of clear writing", not a purported "*epistemic* rule that the object level must come first". martin-randall (30): bottom line up front is good, and omnizoid's post was status regulation, not Bulverism. Holly_Elmore (23): Yudkowsky "didn't properly formulate the one rule that was supposedly violated". Thomas Sepulchre (24): the critic of the post's structure is also its target.
  - **Davis's one comment.** A deleted user (13) defends Yudkowsky's move as reputational damage control, since his reputation matters for getting people to read the Sequences. Davis thanks them ("_amazingly_ clarifying") and objects to positing an epistemic rule "that isn't one" for reputational reasons. He also declines to call omnizoid's post "bad faith" absent a specific hidden motive.
  - omnizoid also appears in the thread, denying having called Yudkowsky a liar and a fraud.
- Quotes:
- (https://www.lesswrong.com/posts/pkaagE6LAsGummWNv/contra-yudkowsky-on-epistemic-conduct-for-author-criticism?commentId=yJnBjC4DDpt47s5yi, jimrandomh, 28 karma)
> Having the order-of-evaluations wrong in a piece of writing is evidence, in a Bayesian sense, of having also had the order-of-evaluations wrong in the thinking that generated it.
- (https://www.lesswrong.com/posts/pkaagE6LAsGummWNv/contra-yudkowsky-on-epistemic-conduct-for-author-criticism?commentId=Zv6EipwQZGgH59i9C, SaidAchmiz, 41 karma)
> Of course support your claims, of course make sure most of your post is actual substance and not empty snark; but the ordering should follow the rules of clear writing (which may dictate one or another order, as befits the case), not some purported (and, as Zack says, in truth nonexistent) *epistemic* rule that the object level must come first.
- (https://www.lesswrong.com/posts/pkaagE6LAsGummWNv/contra-yudkowsky-on-epistemic-conduct-for-author-criticism?commentId=XvmyCXLgzdvXfbdaQ, Davis, 1 karma)
> I want people to read the Sequences _because_ they teach what kinds of thinking systematically lead to beliefs that reflect reality. I'm opposed to people making misleading claims about what kinds of thinking systematically lead to beliefs that reflect reality (in this case, positing a "basic rule of epistemic conduct" that isn't one) just because it seems like a good way to mitigate ongoing harm to their reputation.

### 2023-10-21 · Alignment Implications of LLM Successes: a Debate in One Act
- Path: `reception_data/lw_threads/2023-10-21_alignment-implications-of-llm-successes-a-debate-in-one-act.md` · 57 comments (Davis 4) · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act
- Summary: **Davis's main alignment-discourse reception; the post was curated.** habryka: "both sides presented feel like they have a component of being strawmen", but it is "a pretty good way of helping me understand the contrast". The highest-karma comments engage the dialogue's substance rather than Davis.
  - **The "alien actress" image.** nostalgebraist (121) says it "conflates 'superintelligence' with 'superintelligent *agent*'". There is no evidence of an agentic "homunculus" in LLMs, and as scale increases "The intelligence just *goes into next-token prediction*". 1a3orn (26) objects to the same image and quotes a Yudkowsky tweet that relies on it.
  - **The corrigibility example.** johnswentworth (86) drafts a counter-dialogue calling it a "symbol-referent confusion": a model's natural-language answer about being shut down is not evidence about what a system would *do*. TurnTrout (23) disputes several of Doomimir's claims, including "random garbage" off-distribution and the labeler-hacking argument. mikhail-samin says the Doomimir character fails the ideological Turing test for MIRI's view; Davis edits the offending line.
  - **Davis's corrections.** qbolec catches a combinatorics error; Davis: "You're right. I deeply regret the error and have amended the post."
  - **Later reception.** Seth Herd (2024 review, 12): "the most urgent issue in alignment ... bridging the gap between doomers and optimists". Davis's 2025 self-review (45) quotes his note to prereaders: "My intent is to raise the level of the discourse". He says the dialogue let him explore doubts about the "orthodox" pessimist story "without staking my reputation".
- Quotes:
- (https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=vAmJ3RHSK6AFj3zce, nostalgebraist, 121 karma)
> The model grows more *intelligent* with scale, yet it still does not *want* anything, does not have any *goals*, does not have a *utility function*.  These are not flaws in the model which more intelligence would necessarily correct, since the loss function does not require the model to be an agent.
- (https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=2Zhidu8AByieujvyc, johnswentworth, 86 karma)
> And the key question for corrigibility is what actions the model would take in response to that observation, which is just a totally different question from how it responds to some user’s natural-language query about being turned off.
- (https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=TQw9bJr49RujFssey, habryka4, 10 karma)
> Promoted to curated: I don't think this post is perfect and both sides presented feel like they have a component of being strawmen to it, but I still found it a pretty good way of helping me understand the contrast between two perspectives, both of which I am often pretty sympathetic to (though again, neither of the sides here feel like they are getting close to perfect at representing them).
- (https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=EzmSJ3CNcyef7k3RX, Davis, 45 karma, 2025)
> To the extent that I was having my own doubts about the "orthodox" pessimist story in the GPT-4 era, it was liberating to be able to explore those doubts in public by putting them in the mouth of a character with [the designated idiot character name](https://en.wikipedia.org/wiki/Dialogue_Concerning_the_Two_Chief_World_Systems#Structure) without staking my reputation on Simplicia's counterarguments necessarily being correct.

### 2023-10-26 · Fake Deeply
- Path: `reception_data/lw_threads/2023-10-26_fake-deeply.md` · 7 comments (Davis 3) · https://www.lesswrong.com/posts/T6hmrZRCvmwt4DNAw/fake-deeply
- Summary: The story is fiction. Davis's first comment says he published it partly "to spite Anthropic Claude's smug censoriousness", with a screenshot of a Claude refusal. **Note for positionality:** this is an early instance of Davis's public criticism of Claude, so the study should treat it under its own disclosure.
  - **Reading the protagonist.** nathan-helm-burger reads Jake as "implicitly criticized for their transphobic views" and tests Claude and ChatGPT on whether they detect this. Davis replies with heavy irony that there's "definitely no need to read any of the other posts on that blog". Richard_Kennaway: "Jake's thoughts on trans matters are yours, given plausible deniability by putting them in the mind of a character intended to be read as unsympathetic".
  - **Davis on his views and craft.** He says his ambiguity about which side he is on is deliberate ("I don't do policy"), and that he is "better at characterization and ideas rather than plot".
  - **External lead.** Davis links an r/rational comment on his creative process. That is a Part B lead.
- Quotes:
- (https://www.lesswrong.com/posts/T6hmrZRCvmwt4DNAw/fake-deeply?commentId=QRHYQJkptaYqJMDKs, Davis, 8 karma)
> I was feeling shy about publishing this one (because it touches on some sensitive themes) and sat on it for a couple weeks, but I'm going ahead and pulling the trigger now specifically in order to spite Anthropic Claude's smug censoriousness.
- (https://www.lesswrong.com/posts/T6hmrZRCvmwt4DNAw/fake-deeply?commentId=HPW9gWieDrdmbn6gN, Richard_Kennaway, 6 karma)
> My impression is that Jake's thoughts on trans matters are yours, given plausible deniability by putting them in the mind of a character intended to be read as unsympathetic.

### 2023-11-29 · Lying Alignment Chart
- Path: `reception_data/lw_threads/2023-11-29_lying-alignment-chart.md` · 17 comments (Davis 1) · https://www.lesswrong.com/posts/CK86JXXMzCoPsFbzH/lying-alignment-chart
- Summary: A light thread: jokes extending the chart (Unnamed), quibbles about axis labels and examples, and SaidAchmiz asking what the map–territory mismatch is in the aspartame example. A deleted user calls it an improvement on Scott Alexander's taxonomy of media lies. Benito suggests a poll. Davis declines: ambiguity about how the senses of a concept relate "wants to be either a sequence of multi-thousand-word blog posts, or memes".

### 2023-12-30 · If Clarity Seems Like Death to Them (memoir part 3)
- Path: `reception_data/lw_threads/2023-12-30_if-clarity-seems-like-death-to-them.md` · 192 comments (Davis 10) · https://www.lesswrong.com/posts/yFZH2sBsmmqgWm4Sp/if-clarity-seems-like-death-to-them
- Summary: The largest and most acrimonious memoir thread. It centers on what Davis's actual claim is, and on whether he is owed engagement or an intervention.
  - **"What is the claim?"** TekhneMakre (30) can't find "the basic object-level thing". lalaithion, who is considering transition, reads the linked object-level posts and finds them "mostly uninteresting", focused on "semantics". Viliam (31, then 33) calls the memoir "a fascinating story about obsession". He says he can't identify the object-level claim, and writes: "This isn't drive-by crackpottery, but it is a long-term crackpottery". He resents being called corrupt over a claim never clearly communicated to him. Davis's reply (71, the thread's highest-karma comment) is a 159-word summary in three parts. **Empirical**: late-onset gender dysphoria in males is not an intersex condition (citing Lawrence 2013). **Philosophical**: categories are useful insofar as they carve reality at the joints. **Sociological**: a prominence-weighted sample of the community's refusal to credit these "is a reason to distrust the community's collective sanity". TekhneMakre replies that categories also code *actions*. Davis answers with the vervet-alarm-call example.
  - **Vaniver's reconstruction (53).** Davis saw Yudkowsky violating core community epistemic expectations without acknowledging it. Had people admitted to being Havelian "greengrocers" on his pet issue, he "would have been sad but moved on". Instead they made "philosophical arguments that, as far as I can tell, were not correct, and this was crazy-making". SaidAchmiz (21) adds that trans issues should be within a "heresy budget" because they affect community members directly.
  - **Mental-health framings.** deluks917 (−9): "Rationality is Winning". Unreal treats the post as a call for "triage" or intervention. rsaarelm (24) replies that this is not "drive-by crackpottery" and "it's on LessWrong because it's *about* LessWrong". Yoav Ravid (22): "Couldn't you have said the same thing about Eliezer and AI?"
  - **Support.** Yoav Ravid (33) "read the whole thing, enjoyed it, and agreed with you". MSRayne read it all and wrote "I support you wholeheartedly". gwern (30) jokes about the post's length. Benito (2024 review) calls it an account of finding a truth-seeking community falling short, while noting its diary-like single-perspective reliability.
  - **tailcalled's critique.** He argues from within ex-Blanchardian research that Davis's "Ultimate Point" is unclear: is it categorization, etiology, or defense against pressure to transition? He calls the Blanchardian arguments for the empirical claim "baaaaaaaad". He cites and quotes Ozy Brennan's Substack response to Davis (https://thingofthings.substack.com/p/a-response-to-zack-davis), a Part B lead.
  - **The "constant abuse" sub-thread.** A long and acrimonious exchange between a now-deleted account and tailcalled (with gjm and a habryka mod note) over whether Davis faces "constant abuse" on LW. The deleted account's comment (48) describes a "weaponised confusion" catch-22. Much of the exchange is a personal feud between private individuals; the study should record its existence only.
  - **Smaller exchanges.** philh: the post's section on a child's upbringing arguably violates a norm against criticizing identifiable parents' decisions. Davis: if it were a real case he would have cleared it with the parents, and his "obviously" was irony. elityre (2024) disputes the claim that "I"-statements reduce collective information processing. He also flags the pre-gay-kids passage as changing his view if true.
- Quotes:
- (https://www.lesswrong.com/posts/yFZH2sBsmmqgWm4Sp/if-clarity-seems-like-death-to-them?commentId=6zBCjmAT7cdL79oNK, Davis, 71 karma)
> **Empirical Claim**: late-onset gender dysphoria in males is not an intersex condition.
- (https://www.lesswrong.com/posts/yFZH2sBsmmqgWm4Sp/if-clarity-seems-like-death-to-them?commentId=6zBCjmAT7cdL79oNK, Davis, 71 karma)
> **Philosophical Claim**: categories are useful insofar as they compress information by "carving reality at the joints"; in particular, whether a categorization makes someone happy or sad is not relevant.
- (https://www.lesswrong.com/posts/yFZH2sBsmmqgWm4Sp/if-clarity-seems-like-death-to-them?commentId=6zBCjmAT7cdL79oNK, Davis, 71 karma)
> **Sociological Claim**: the extent to which a prominence-weighted sample of the rationalist community has refused to credit the Empirical or Philosophical Claims even when presented with strong arguments and evidence is a reason to distrust the community's collective sanity.
- (https://www.lesswrong.com/posts/yFZH2sBsmmqgWm4Sp/if-clarity-seems-like-death-to-them?commentId=b8pZQHzuiMKEcC2CB, Viliam, 33 karma)
> This isn't drive-by crackpottery, but it is a long-term crackpottery; and it is on LessWrong because the previous parts of it were on LessWrong.
- (https://www.lesswrong.com/posts/yFZH2sBsmmqgWm4Sp/if-clarity-seems-like-death-to-them?commentId=AFXGZL2XsYLKoSkwW, Viliam, 8 karma)
> I resent being called corrupt for not agreeing with something that was never clearly communicated to me in the first place.
- (https://www.lesswrong.com/posts/yFZH2sBsmmqgWm4Sp/if-clarity-seems-like-death-to-them?commentId=dSiBGRGziEffJqN2B, Vaniver, 53 karma)
> Instead they made philosophical arguments that, as far as I can tell, were not correct, and this was crazy-making, because Zack now also doubted his reasoning that led to him disagreeing with them, but no one would talk about this publicly.
- (https://www.lesswrong.com/posts/yFZH2sBsmmqgWm4Sp/if-clarity-seems-like-death-to-them?commentId=ZL7f9YjEWXXpmwJky, rsaarelm, 24 karma)
> This isn't drive-by crackpottery and it's on LessWrong because it's *about* LessWrong.
- (https://www.lesswrong.com/posts/yFZH2sBsmmqgWm4Sp/if-clarity-seems-like-death-to-them?commentId=Fzoxbxi7zYfBFergw, Yoav Ravid, 22 karma)
> Even if it's true that he's obsessed with it and everything he writes is somehow connected to it - what's the problem with that? Couldn't you have said the same thing about Eliezer and AI?
- (https://www.lesswrong.com/posts/yFZH2sBsmmqgWm4Sp/if-clarity-seems-like-death-to-them?commentId=E8MjQ8cwtdrSjjz2B, tailcalled, 8 karma)
> Disagree with the sociological claim because the Blanchardian arguments for the empirical claim are baaaaaaaad and it's pretty reasonable to not credit an empirical claim when the arguments presented for it are so bad.
- (https://www.lesswrong.com/posts/yFZH2sBsmmqgWm4Sp/if-clarity-seems-like-death-to-them?commentId=tCATxr9GsdoMvfrCT, Davis, 20 karma)
> I don't think it's plausible to posit an agent that wants to be categorized in a particular way in the map, without that category tracking something in the territory. Where would such a pathological preference come from?
- (https://www.lesswrong.com/posts/yFZH2sBsmmqgWm4Sp/if-clarity-seems-like-death-to-them?commentId=hsz64FD3azsBWEbJg, Benito, 4 karma, 2024)
> I think it's an account of someone who believes in truth-seeking, engaging with the messy political reality of an environment that cared about the ideals of truth-seeking far more than most other places on earth, and finding it to either fall short or sometimes betray those ideals.

### 2024-01-09 · On the Contrary, Steelmanning Is Normal; ITT-Passing Is Niche
- Path: `reception_data/lw_threads/2024-01-09_on-the-contrary-steelmanning-is-normal-itt-passing-is-niche.md` · 37 comments (Davis 4) · https://www.lesswrong.com/posts/jo5Fhkb7escrYE9cC/on-the-contrary-steelmanning-is-normal-itt-passing-is-niche
- Summary: A reply to Rob Bensinger's "ITT-passing and civility are good; 'charity' is bad; steelmanning is niche". Most comments defend the ideological Turing test (ITT) on grounds the post set aside.
  - **ITT as understanding, goodwill, or a diagnostic.** johnswentworth (49): the ITT diagnoses which party should be updating, and can turn a debate "into a lesson". SaidAchmiz (30): isn't ITT-passing "a *prerequisite* to steelmanning"? Davis concedes the binary case but says understanding is usually partial. Ape in the coat: your steelman may be weaker than what the other side's own arguments would support. Seth Herd (20): the ITT "establishes goodwill".
  - **Emotions and epistemic rationality.** Davis (12): "I don't consider managing people's emotions to be part of the subject matter of epistemic rationality". johnswentworth (21) calls that "an extremely large mistake". tailcalled floats "plausible deniability" as an alternative explanation. SaidAchmiz: other people's emotions are irrelevant to one's own epistemic practice.
  - **Other comments.** cousin_it (20): debates are a poor source of truth compared with books. Benito (2025 review): steelmanning suits positions and the ITT suits people, and Zack "seems to undervalue" learning the ITTs of very different minds.
  - **Davis's 2025 self-review** frames the post as documenting an inversion: Steven Kaas's 2008 "if you're interested in producing truth, you will fix your opponents' arguments for them", versus Yudkowsky's 2017 report that "Eliezer and Holden are both on record as saying that 'steelmanning' people is bad". Raemon replies that each practice has its own use, and that the dispute feels like "some kind of culture war".
- Quotes:
- (https://www.lesswrong.com/posts/jo5Fhkb7escrYE9cC/on-the-contrary-steelmanning-is-normal-itt-passing-is-niche?commentId=sbBZTpmyQWcbmQbqJ, Davis, 12 karma)
> I don't consider managing people's emotions to be part of the subject matter of epistemic rationality, even if managing people's emotions is a good idea and useful for having good discussions in practice. If the ITT is advocated for as an epistemic rationality technique, but its actual function is to get people in a cooperative mood, that's a problem!
- (https://www.lesswrong.com/posts/jo5Fhkb7escrYE9cC/on-the-contrary-steelmanning-is-normal-itt-passing-is-niche?commentId=BQbixtGB7DjzsFtX3, johnswentworth, 21 karma)
> This sounds to me like an extremely large mistake. Emotions sure do seem to be the rate-limiting factor for epistemically productive interaction in a very large fraction of situations, and therefore managing them is a very central issue for human epistemic rationality in practice.
- (https://www.lesswrong.com/posts/jo5Fhkb7escrYE9cC/on-the-contrary-steelmanning-is-normal-itt-passing-is-niche?commentId=GEJWQuGrbC3yrkqbc, johnswentworth, 49 karma)
> Another way to think about it: often in debate, one person just understands the topic much better than the other, and the ideal outcome would be for both participants to figure this out and transform the debate into a lesson instead (i.e. student-teacher interaction rather than debate).
- (https://www.lesswrong.com/posts/jo5Fhkb7escrYE9cC/on-the-contrary-steelmanning-is-normal-itt-passing-is-niche?commentId=2rQN5jHRh4fRzzLAK, Davis, 7 karma, 2025)
> In 2008, the community wisdom was that fixing your interlocutor's arguments for them (what was not yet called "steelmanning") was a good thing. The warrant cited for this advice was that it's something you do "if you're interested in producing truth".

### 2024-02-10 · And All the Shoggoths Merely Players
- Path: `reception_data/lw_threads/2024-02-10_and-all-the-shoggoths-merely-players.md` · 59 comments (Davis 5) · https://www.lesswrong.com/posts/8yCXeafJo67tYe5L4/and-all-the-shoggoths-merely-players
- Summary: The second Simplicia/Doomimir dialogue. It was curated by T3t (15) for distilling cruxes and for its "substantial number of references" to real arguments.
  - **johnswentworth's in-character continuation.** johnswentworth (23, then 19, 15, 13) writes Doomimir's side in the comments. He cites Yudkowsky's "List of Lethalities" #20: human raters make systematic, predictable errors that a learner will learn. He argues that iterative design fails exactly where failures are not obvious. Davis replies in Simplicia's voice (23, 12) with KL-penalty overoptimization data (Stiennon et al. 2020) and "we have empirical results". He frames RLHF as reinforcing past behavior rather than as expected-utility maximization.
  - **Davis on the "in the limit" arguments.** Out of character (26), he likens the pessimist's position to an intuition that a working machine must fail, combined with no persuaded outside experts and no concrete bets. He calls this "a non-starter even if it turns out to be true".
  - **Empirical sub-debate.** TurnTrout and johnswentworth dispute whether Rolnick et al.'s label-noise results and OpenAI's weak-to-strong results confirm or undercut lethality #20, with nostalgebraist and ryan_greenblatt also taking part. TurnTrout calls Doomimir's "by virtue of it being sufficiently powerful" a "word game". habryka disagrees. mattmacdermott catches a pigeonhole error, and Davis corrects "wrong labels" to "noisy labels".
  - **Reviews.** Seth Herd (2025 review): "one of the most important posts yet written" for bridging the optimist/pessimist divide. martin-randall (2025): the dialogues avoid the strawman-villain problem. Simplicia is "Zack in a Russian hat", and there is no clear real-world voice for her position. He also comments on Claude's current personality ("no longer preachy and condescending"), which is relevant to the study's positionality disclosure.
- Quotes:
- (https://www.lesswrong.com/posts/8yCXeafJo67tYe5L4/and-all-the-shoggoths-merely-players?commentId=qTRzwqb7duesAxDr5, T3t, 15 karma)
> Curated.  This dialogue distilled a decent number of points I consider cruxes between these two (clusters of) positions.
- (https://www.lesswrong.com/posts/8yCXeafJo67tYe5L4/and-all-the-shoggoths-merely-players?commentId=npR4qs66wGzkHhvSY, Davis, 26 karma)
> The thing is, we _do_ need more than a handwavy metaphor! "Yes, your gold-printing machine _seems_ to be working great, but my intuition says it's definitely going to kill everyone. No, I haven't been able to convince relevant experts who aren't part of my robot cult, but that's because they're from Earth and therefore racially inferior to me. No, I'm not willing to make any concrete bets or predictions about what happens before then" is a non-starter even if it turns out to be true.
- (https://www.lesswrong.com/posts/8yCXeafJo67tYe5L4/and-all-the-shoggoths-merely-players?commentId=Cax89BTuvFCNqudF2, Davis, 23 karma)
> But the ray of hope I see here is more meta and methodological, rather than turning on any one empirical result. It's that _we have empirical results_. We can study these machines, now, _before_ their successors are powerful enough to kill us.
- (https://www.lesswrong.com/posts/8yCXeafJo67tYe5L4/and-all-the-shoggoths-merely-players?commentId=dPCekrFk5voHDdgM3, johnswentworth, 19 karma)
> The unifying theme here is that **when these failures occur, it is not obvious that they've occurred**.
- (https://www.lesswrong.com/posts/8yCXeafJo67tYe5L4/and-all-the-shoggoths-merely-players?commentId=vzgXcCecM7fYzJyv8, martin-randall, 8 karma, 2025)
> So Simplicia is Zack in a Russian hat, possibly a bit drunk, and she does her best in a difficult role to play.

### 2024-03-02 · Agreeing With Stalin in Ways That Exhibit Generally Rationalist Principles (memoir part 4)
- Path: `reception_data/lw_threads/2024-03-02_agreeing-with-stalin-in-ways-that-exhibit-generally.md` · 25 comments (Davis 4) · https://www.lesswrong.com/posts/Q4yhuwzoy3kNRbv4m/agreeing-with-stalin-in-ways-that-exhibit-generally
- Summary: Small for a memoir installment. Davis calls it "the best and most important post in the sequence"; Viliam finds it self-contained.
  - **Feynman.** habryka (25) challenges the post's Feynman contrast: Feynman publicly understated his IQ and "seemed to me like someone who was pretty cavalier with public discourse". Davis (14) distinguishes a "straight talker" who is sloppy but wants listeners to know his reporting algorithm from prudent selective reporting in service of a covert goal.
  - **Why care what Yudkowsky thinks?** RamblinDash (19, 27) asks this, by analogy to an Obama admirer on an "epic quest to Get Obama's Attention". He later says the series reads like "a sort of rationalist Martin Luther criticizing the Pope", when many rationalists are already "protestant". Davis concedes the ridiculousness by analogy to an eight-year false-advertising suit against "World's Best" ice cream. cousin_it suggests simply agreeing to disagree. tailcalled replies that Davis isn't straightforwardly essentialist.
  - **Other comments.** Viliam and Ape in the coat debate whether young people learn of transsexuality before autism. TAG (16) distinguishes not lying from volunteering unsolicited truths.
- Quotes:
- (https://www.lesswrong.com/posts/Q4yhuwzoy3kNRbv4m/agreeing-with-stalin-in-ways-that-exhibit-generally?commentId=DigRHyNxgyjWPjBev, Davis, 14 karma)
> These are different things. Straight talkers sometimes say false or exaggerated things out of sloppiness, but they actively want listeners to [know their reporting algorithm](https://www.lesswrong.com/posts/DoPo4PDjgSySquHX8/heads-i-win-tails-never-heard-of-her-or-selective-reporting). Prudently selecting which true sentences to report in the service of a covert goal is not lying, but it's definitely not straight talk.
- (https://www.lesswrong.com/posts/Q4yhuwzoy3kNRbv4m/agreeing-with-stalin-in-ways-that-exhibit-generally?commentId=kXNPv9KuGqpnPzgwR, RamblinDash, 27 karma)
> Whereas I think my point is much more general and really not specific to Trans at all - like why be so deeply invested in the contents of some one guy's mind, at all? On any issue?
- (https://www.lesswrong.com/posts/Q4yhuwzoy3kNRbv4m/agreeing-with-stalin-in-ways-that-exhibit-generally?commentId=tG9MHqE46t9noy6LM, Davis, 11 karma)
> Yes, that would be ridiculous. It would also be ridiculous in a broadly similar way if someone spent eight years in the prime of their life prosecuting a false advertising lawsuit against a "World's Best" brand ice-cream for not actually being the best in the world.

### 2024-03-21 · "Deep Learning" Is Function Approximation
- Path: `reception_data/lw_threads/2024-03-21_deep-learning-is-function-approximation.md` · 31 comments (Davis 4) · https://www.lesswrong.com/posts/DhjcdzTyqHte2v6bu/deep-learning-is-function-approximation
- Summary: Mixed reception, with sharp criticism from technically engaged readers.
  - **The rhetorical device.** The post replaces standard terms with long tabooed paraphrases like "multi-layer parameterized graphical function approximator". Algon, jarviniemi (12) and rhollerith liked it. ErickBall (32) downvoted for "rhetorical shenanigans". Veedrac (19) says the replacement terms are "no less charged" and the post draws conclusions from their "aesthetics". the-cactus says "function approximator" invites a non-central fallacy. gwern (23) calls it "the old wine of the 'just' fallacy in new 'function approximation' skins" and doubts the "ironic exercise" lands.
  - **Undeleting ErickBall's comment.** ErickBall deleted the comment; Davis undeleted it "because I don't think my critics are obligated to be polite to me". habryka (25) says that author power was an unintended permissions bug.
  - **Substantive engagement.** tin482 (42) argues that no rigorous statistical-learning analysis has bounded any real deep-learning model, so the "function approximation" frame constrains little (sparse parity versus protein folding). quintin-pope (20) cites muP against this. abramdemski (31) argues that both Davis and Yudkowsky are partly wrong about whether a learned function "represents" its loss function. DaemonicSigil (10) calls the dispute "a mere difference in terminology". Closed Limelike Curves (16): "Yes, it's function approximation; I think we all know that."
  - **Davis's replies.** To gwern: he is supplying "the diff" between the LessWrong picture of deep learning and the textbooks' (Prince 2023; Bishop & Bishop 2024). If that "mood-affiliates" with one side of a "one-dimensional culture war", the culture war is the problem. 2025 self-review: "Read textbooks!"
- Quotes:
- (https://www.lesswrong.com/posts/DhjcdzTyqHte2v6bu/deep-learning-is-function-approximation?commentId=AziZ5453i7TuC6vRi, gwern, 23 karma)
> It basically proves too much because it's equivocation. I am struggling to find anything in Zack's post which is not just the old wine of the "just" fallacy in new 'function approximation' skins.
- (https://www.lesswrong.com/posts/DhjcdzTyqHte2v6bu/deep-learning-is-function-approximation?commentId=cMuA7aEeSbMHaRTNH, tin482, 42 karma)
> Despite literally thousands of papers claiming to "understand deep learning" from experts in fields as various as computational complexity, compressed sensing, causal inference, and - yes - statistical learning, *NO* rigorous, first-principles analysis has *ever* computed *any aspect* of *any* deep learning model beyond toy settings.
- (https://www.lesswrong.com/posts/DhjcdzTyqHte2v6bu/deep-learning-is-function-approximation?commentId=xp5KwGpavQB3QaxHF, Davis, 13 karma)
> If my attempt to remediate that particular problem ends up mood-affiliating with the wrong side of a one-dimensional culture war, maybe that's because the one-dimensional culture war is crazy and we should stop doing it.
- (https://www.lesswrong.com/posts/DhjcdzTyqHte2v6bu/deep-learning-is-function-approximation?commentId=yr89gEw5CaEBsYw2u, Davis, 9 karma, 2025)
> I'm just saying that after I read the math, the summoning-a-little-animal mental image didn't seem faithful to the math: you should be thinking about how the model's outputs interpolate the training data, not how the little animal's behavior unpredictably fails to reflect some putative utility function that "outer" training failed to instill.

### 2024-03-26 · My Interview With Cade Metz on His Reporting About Slate Star Codex
- Path: `reception_data/lw_threads/2024-03-26_my-interview-with-cade-metz-on-his-reporting-about-slate.md` · 188 comments (Davis 2) · https://www.lesswrong.com/posts/oYnwTuxySiaZYDrur/my-interview-with-cade-metz-on-his-reporting-about-slate
- Summary: Davis's most-commented post. **The discussion is overwhelmingly about Metz, the NYT and Scott Alexander, not about Davis.** Reception of Davis himself is mostly appreciation for getting and publishing the interview: Jacobian (76): "Kudos for getting this interview and posting it! Extremely based." Nathan Young (107): Metz reads "as a person caught in the act of bullying who is trying to wriggle out of it". frankybegs thinks Davis "fell back a little quickly". matto: Davis is "engaging in truth-seeking" and Metz is not.
  - **gwern (210, the thread's top comment)** analyzes a 2020 Metz–Michael Vassar interview transcript that Hazard (79) posted at naturalhazard.xyz. He calls Metz "extraordinarily incurious" and says he could not articulate a rationale for publishing Scott's surname. This is a Part B lead, and relevant to Davis's 2025–26 Metz posts.
  - **Talking to journalists at all.** A deleted user (56) warns that Davis was "training" Metz in epistemics-talk and says, "Do not talk to journalists without asking for help." Hazard replies that Metz shows no such improvement.
  - **Was publishing the name justified?** austin-chen (19) and ricraz (21, 32) argue doxxing harms were overstated and the episode showed rationalist "underdog bias" and tribalism. habryka (39) disagrees. steve2152 (26, 22): the issue is that the benefit was zero, not the size of the cost.
  - **The Murray passage.** LGS (36, 31) and interstice (26) argue the "aligned himself with Charles Murray" insinuation was substantively true even if poorly evidenced. Others (pktechgirl, frankybegs, Jiro, DPiepgrass) call it dishonest insinuation. Davis (3): "Just because the defendant is actually guilty, doesn't mean the prosecutor should be able to get away with making a tenuous case!" pktechgirl (29) notes the full Scott passage Davis summarized does discuss heredity and income, so Davis's description "might be too charitable to Scott".
  - **Davis's opening remark on criticism.** habryka asks whether his "secret-lore-of-rationality" remark about criticism was a joke. Davis (24) clarifies that the clauses came out in the wrong order in extemporaneous speech.
  - **Leaked email.** Commenters refer to Scott Alexander's leaked 2014 email (linked via a third-party blog); the study should handle this with care.
- Quotes:
- (https://www.lesswrong.com/posts/oYnwTuxySiaZYDrur/my-interview-with-cade-metz-on-his-reporting-about-slate?commentId=at6Bwrb2qv25Lu6Jm, Jacobian, 76 karma)
> Kudos for getting this interview and posting it! Extremely based.
- (https://www.lesswrong.com/posts/oYnwTuxySiaZYDrur/my-interview-with-cade-metz-on-his-reporting-about-slate?commentId=4AQfQzytbnyKyWdHA, Nathan Young, 107 karma)
> To me this reads as a person caught in the act of bullying who is trying to wriggle out of it. Fair play for challenging him, yuck at the responses.
- (https://www.lesswrong.com/posts/oYnwTuxySiaZYDrur/my-interview-with-cade-metz-on-his-reporting-about-slate?commentId=YdJu4pQeh9X5TSrHR, Davis, 3 karma)
> Just because the defendant is actually guilty, doesn't mean the prosecutor should be able to get away with making a tenuous case!
- (https://www.lesswrong.com/posts/oYnwTuxySiaZYDrur/my-interview-with-cade-metz-on-his-reporting-about-slate?commentId=fw2yh7ogvnb4WXbiL, pktechgirl, 29 karma)
> I think Zack's description might be too charitable to Scott. From his description I thought the reference would be strictly about poverty. But the full quote includes a lot about genetics and ability to earn money.
- (https://www.lesswrong.com/posts/oYnwTuxySiaZYDrur/my-interview-with-cade-metz-on-his-reporting-about-slate?commentId=WwQHcnFhnGd8nDfJa, ricraz, 32 karma)
> My main diagnosis of the NYT/SSC incident is that rationalists were caught up by underdog bias, even as they leveraged thousands of influential tech people to attack the NYT.

### 2024-04-01 · The Evolution of Humans Was Net-Negative for Human Values
- Path: `reception_data/lw_threads/2024-04-01_the-evolution-of-humans-was-net-negative-for-human-values.md` · 1 comment · https://www.lesswrong.com/posts/cwiufyabZaAttivvk/the-evolution-of-humans-was-net-negative-for-human-values
- Summary: An April Fools' post. Its single comment (Jackson Wagner): "this is quality."

### 2024-04-29 · Ironing Out the Squiggles
- Path: `reception_data/lw_threads/2024-04-29_ironing-out-the-squiggles.md` · 37 comments (Davis 3) · https://www.lesswrong.com/posts/H7fkGinsv8SDxgiS2/ironing-out-the-squiggles
- Summary: A technical, collegial thread on adversarial examples and alignment. No hostility toward Davis.
  - **Are real category boundaries smooth?** faul_sname doubts that real-world category boundaries (e.g. "profitable business plan") are smooth enough for adversarially robust classifiers to exist, and suggests they may be "inherently fractal". Davis disagrees: the brittleness is "a limitation of the tools", not inherent unmodelability. This bears on the categorization theme, and the study's categorization chapter may want it.
  - **Adversarial training and value fragility.** Wei_Dai (16) argues adversarial training "is merely patching symptoms", and that applying it to value learning would need ground-truth labels for a superintelligent adversary's inputs. He proposes metaphilosophy as the deeper fix. gallabytes (15, 16) says texture bias shrinks at scale. quintin-pope (18): human visual cortices are also bad at hands and text, which suggests convergence. steve2152: the post's examples (faces, adjective order) are pure distribution-sampling tasks where no one expected adversarial dynamics. Davis replies that he doesn't "think the conditional-sampling thing was obvious in 2004".
  - kave (15) questions the claim that different hastily written programs wouldn't share the same bug.
- Quotes:
- (https://www.lesswrong.com/posts/H7fkGinsv8SDxgiS2/ironing-out-the-squiggles?commentId=jwq8JnkdhawyB7tLp, Davis, 5 karma)
> There exists a function from business plans to their profitability. The worry is that if you try to approximate that function with standard ML tools, then _even if_ your approximation is highly accurate on any normal business plan, it's not hard to construct an artificial plan on which it won't be. But this seems like a limitation of the tools; I don't think it's because the space of business plans is inherently fractally complex and unmodelable.
- (https://www.lesswrong.com/posts/H7fkGinsv8SDxgiS2/ironing-out-the-squiggles?commentId=g9TmLTFTBdNxnK4ad, Wei_Dai, 16 karma)
> The evidence from adversarial training suggests to me that AT is merely patching symptoms (e.g., making the ML system de-emphasize certain specific features) and not fixing the underlying problem.

### 2024-05-11 · Should I Finish My Bachelor's Degree?
- Path: `reception_data/lw_threads/2024-05-11_should-i-finish-my-bachelor-s-degree.md` · 14 comments (Davis 2) · https://www.lesswrong.com/posts/8pmimprBizW8Qpf5o/should-i-finish-my-bachelor-s-degree
- Summary: Personal-advice thread; supportive and practical.
  - **Advice.** cata (24) doesn't see why Davis is considering it ("Taking eight college classes is a lot of work actually?"). Dagon, dave-orr and Viliam say the degree is legible and may be fun. localdeity: making degrees less correlated with competence is prosocial. Augustin Portier wonders whether it is a medium-term goal for someone who feels he has "outlived" himself.
  - **Davis's replies.** He lists the fall courses, including one he calls "worthless and insulting" that "might present an opportunity to troll the professor". He says he'd be "more at peace" criticizing schooling "from the position of '... and I have a math degree'". He concedes that "the social fiction of 'grades' does look like it sometimes succeeds at extorting some marginal effort out of my brain".
  - **Cross-reference:** the 2026-01-01 post *College Was Not That Terrible Now That I'm Not That Crazy* reports the outcome.
- Quotes:
- (https://www.lesswrong.com/posts/8pmimprBizW8Qpf5o/should-i-finish-my-bachelor-s-degree?commentId=D3xKynufZrfDZ4poJ, Davis, 5 karma)
> Somehow, I think I would be more at peace if I could criticize schooling from the position of "... and I have a math degree" rather than "... so I didn't finish." That peace definitely wouldn't be worth four semesters, but it might be worth two.

### 2024-06-03 · The Standard Analogy
- Path: `reception_data/lw_threads/2024-06-03_the-standard-analogy.md` · 30 comments (Davis 4) · https://www.lesswrong.com/posts/sGEJi9wFT3Gdqg2nM/the-standard-analogy
- Summary: The third Simplicia/Doomimir dialogue, curated by Ruby (23), who belongs to the "doomy" camp. Ruby found Doomimir "a bit unfair" to that worldview but praised the genre-justifying form and the "unusually high-level of scholarcism (i.e. linking to sources)". It was performed at LessOnline with John Wentworth playing Doomimir.
  - **Criticism of both characters.** A deleted user (25) says Simplicia misses the real crux: whether recent empirical evidence undercuts MIRI's "very specific theory of optimization and artificial cognition". Charlie Steiner (12): Doomimir mostly crows rather than raising situational awareness. Davis answers in Simplicia's voice that she accepts realism about rationality "in the limit", but the long run is "far away".
  - **Pause versus incremental progress.** Wei_Dai (10, 14) asks whether "seems plausible … more forgiving" suffices to proceed. He states his preference for an AI pause plus human intelligence enhancement. Davis/Simplicia: "humanity" isn't an agent that decides, while incremental alignment progress needs no coordination.
  - **Other comments.** cousin_it (18): human-like behavior includes abusing power. Lblack: human infant learning is a closer analogy than evolution.
  - **Davis's 2026 self-review** says this entry, more than the others, represents his own views. He faults MIRI's messaging for making the evolution analogy "and then stops there" without disanalogies such as selective breeding and program synthesis. He suggests that may be "strategically instrumentally rational insofar as MIRI is a propaganda outlet now", and finds it "disappointing".
- Quotes:
- (https://www.lesswrong.com/posts/sGEJi9wFT3Gdqg2nM/the-standard-analogy?commentId=t2PHwBTsNqmDaSn6d, Ruby, 23 karma)
> Fictional dialogues have had periods of popularity, with varying quality, and I feel like Zack is producing the kind that justify the genre: an educational contrasting of sides of the an argument the way you don't get from an author just arguing their side in prose, together with the coherence that comes from a single author rather than the unintentional talking past from real dialogues).
- (https://www.lesswrong.com/posts/sGEJi9wFT3Gdqg2nM/the-standard-analogy?commentId=kt7dK5PRWxwFHkXEu, Davis, 7 karma, 2026)
> That said, more than the other entries in this series, this is the one where I'm willing to cop to and put my weight down on Simplicia representing my own views, rather than laundering my doubts as just asking questions.
- (https://www.lesswrong.com/posts/sGEJi9wFT3Gdqg2nM/the-standard-analogy?commentId=kt7dK5PRWxwFHkXEu, Davis, 7 karma, 2026)
> Maybe that's strategically instrumentally rational insofar as MIRI is a propaganda outlet now (in the literal meaning of the word, ["public communication aimed at influencing an audience and furthering an agenda"](https://en.wiktionary.org/wiki/propaganda)) and doesn't seem to care that much about being intellectually credible in ways that don't cash out as policy influence?

### 2025-01-01 · Comment on "Death and the Gorgon"
- Path: `reception_data/lw_threads/2025-01-01_comment-on-death-and-the-gorgon.md` · 35 comments (Davis 8) · https://www.lesswrong.com/posts/hx5EkHFH5hGzngZDs/comment-on-death-and-the-gorgon
- Summary: Davis's review of Greg Egan's story satirizing EA/rationalists. Most comments concern Egan rather than Davis.
  - **Why Egan dislikes rationalists.** quetzal_rainbow (20) proposes an aging sci-fi writer's drift toward social commentary. Nick_Tarleton (21) and dr_s (10, 21) agree in part. shankar-sivarajan (28) cites "the narcissism of small differences". avturchin (16) and JenniferRM (19) see authors uncomfortable with their fandoms.
  - **Davis defends Egan against gwern's "crankery" charge.** gwern (22, 20, 8) attributes Egan's antipathy partly to politics and "mathematician crankery". Davis repeatedly defends Egan's specific claims, e.g. distinguishing "Gary Marcus–like skepticism" from "Hubert Dreyfus–like skepticism". He calls this "this tedious thread", whose aim is to separate "mathematician crankery" from "an overconfident negative prediction about AI capabilities". He agrees that Egan "still hasn't seen the writing on the wall regarding deep learning".
  - **LLMs as people.** JenniferRM says she read Egan's "Orphanogenesis" to ChatGPT "to help her understand herself". Davis replies that this is "exactly the kind of thing Egan is reacting to": enthusiasts "assuming LLMs are digital people because they talk". In a footnote he adds that LLMs are "relevantly upload-like in at least some ways and conceivably sites of moral patiency". **Positionality note:** this is Davis on LLM moral status. dr_s (21) calls Davis's framing "borders on the strawman".
  - **Other comments.** martin-randall reads the story as equally a satire of rationalism. Viliam: positive EA work would make a boring story.
- Quotes:
- (https://www.lesswrong.com/posts/hx5EkHFH5hGzngZDs/comment-on-death-and-the-gorgon?commentId=PbgnogkgF5xysboRL, Davis, 14 karma)
> This is exactly the kind of thing Egan is reacting to, though—starry-eyed sci-fi enthusiasts assuming LLMs are digital people because they talk, rather than thinking soberly about the technology _qua_ technology.
- (https://www.lesswrong.com/posts/hx5EkHFH5hGzngZDs/comment-on-death-and-the-gorgon?commentId=FG22b5P44Dzr2Swmb, dr_s, 21 karma)
> It's that if we can simply handwave away LLMs as *obviously and self evidently* not being people then we can probably keep doing that right up to when the Blade Runner replicants are crying about it being time to die, which is obviously just a simulation of emotion, don't be daft.
- (https://www.lesswrong.com/posts/hx5EkHFH5hGzngZDs/comment-on-death-and-the-gorgon?commentId=nguvwWgrgSEStEm7A, Davis, 7 karma)
> It's Gary Marcus–like skepticism about the reliability and generality of existing-paradigm machine learning techniques, not Hubert Dreyfus–like skepticism of whether a machine could think in all philosophical strictness.

### 2025-06-06 · Discontinuous Linear Functions?!
- Path: `reception_data/lw_threads/2025-06-06_discontinuous-linear-functions.md` · 11 comments (Davis 3) · https://www.lesswrong.com/posts/GodqHKvQhpLsAwsNL/discontinuous-linear-functions
- Summary: A math explainer. Gurkenglas and jeffrey-liang (12) point out technical errors: a k/N slip, a misleading "infinitely steep slope" clause (∛x at 0), and that the uniform norm needs a bounded domain. Davis corrects each and credits the commenters. NuclearCuriosity: "This post explains what's going on better than my professor or textbook did."

### 2025-07-15 · Critic Contributions Are Logically Irrelevant
- Path: `reception_data/lw_threads/2025-07-15_critic-contributions-are-logically-irrelevant.md` · 74 comments (Davis 2) · https://www.lesswrong.com/posts/bsKHthyhB7DNBxERQ/critic-contributions-are-logically-irrelevant
- Summary: Part of the mid-2025 LessWrong moderation dispute over SaidAchmiz (cf. Duncan Sabien's "Killing Socrates", habryka's "coach" analogy). Davis argues that a commenter's own post-writing record is irrelevant to the value of their criticism. Most respondents find the argument technically right but beside the point.
  - **The "beside the point" responses.** habryka (17): critique in ambiguous domains is "a request to engage in a prolonged exchange", and generative work is evidence of who is worth engaging. He also says Davis's theory "doesn't really admit for a comment to be bad". jimmy (13): the objection is to implicit claims of superiority. brambleboy: context matters (film critics versus filmmaking community). philh (21): the essay attributes to habryka and Duncan the literal posts-versus-comments distinction when they meant a different one. He also calls the "screens off" argument "obviously-wrong" since authorship is rendered on the page; Davis concedes he wishes he had done "a better job of flagging the metonymy".
  - **The "maximizing correctness" heading.** gjm (23) objects that it implies opponents don't care about correctness at all, a recurring pattern in Davis's writing in his view. Davis: "The _m_-word in the section title was very deliberate."
  - **Other comments.** sil-ver: the top-level-posts point is "at least 80% a rationalization/red herring" for disliking a commenter's style.
  - **A deleted user and SaidAchmiz** exchange escalating personal attacks (e.g. "I think you are scum"); a record of the dispute's temperature, not of Davis.
- Quotes:
- (https://www.lesswrong.com/posts/bsKHthyhB7DNBxERQ/critic-contributions-are-logically-irrelevant?commentId=XTXc6RxTy22QwDmAu, habryka4, 17 karma)
> People leaving bad comments really is actually a major reason why most of the internet is bad. It appears your theory doesn't really admit for a comment to be bad, which I think makes it inapplicable to most of the internet.
- (https://www.lesswrong.com/posts/bsKHthyhB7DNBxERQ/critic-contributions-are-logically-irrelevant?commentId=eiJpj47ZcLpaJCvfW, gjm, 23 karma)
> (I remark that this is not the first time I have had a discussion with Zack of much the same shape, where Zack implicitly or explicitly claims that epistemic virtue means caring *only* about one thing even when there seem (at least to me) to be other things a would-be clear thinker might reasonably care about. I think it might be the third or fourth time.)
- (https://www.lesswrong.com/posts/bsKHthyhB7DNBxERQ/critic-contributions-are-logically-irrelevant?commentId=Drf9gjk6GpiiZEK9e, philh, 21 karma)
> It seems to me that posts-versus-comments is a helpful stand in for the actual distinction that people care about here, which is...

### 2025-07-17 · Comment on "Four Layers of Intellectual Conversation"
- Path: `reception_data/lw_threads/2025-07-17_comment-on-four-layers-of-intellectual-conversation.md` · 12 comments (Davis 1) · https://www.lesswrong.com/posts/yr4pSJweTnF6QDHHC/comment-on-four-layers-of-intellectual-conversation
- Summary: Small thread on Yudkowsky's 2016 post.
  - **Frustration as evidence.** lahwran doubts that frustration is evidence of good debate. SaidAchmiz: the claim is only that frustration is not evidence of *bad* debate. Vaniver cites the Smalley–Drexler debate as an example of a critic who hadn't read the work.
  - **Intellectual history.** Wei_Dai says the post influenced his "Some Thoughts on Metaphilosophy" and perhaps "AI Safety via Debate".
  - **Other comments.** azergante notes the absence of quantitative evidence.

### 2025-07-18 · "Some Basic Level of Mutual Respect About Whether Other People Deserve to Live"?!
- Path: `reception_data/lw_threads/2025-07-18_some-basic-level-of-mutual-respect-about-whether-other.md` · 85 comments (Davis 9) · https://www.lesswrong.com/posts/rzFrwWvvpgzfnwSeB/some-basic-level-of-mutual-respect-about-whether-other
- Summary: Another post in the July 2025 SaidAchmiz moderation conflict. The title quotes a habryka comment.
  - **Reception of the post.** Archimedes (16) calls it "personally-motivated meta-level slop" airing grievances without context. gworley: "thinly-veiled drama posting". habryka (15) defends the general practice of abstracting local grievances into principles.
  - **habryka's rebuttal (61).** He says Davis misread his comment ("Come on man, you have the ability to understand the context better"). He calls Davis's claim that critics "just mean that opinion X is false" disingenuous, citing Davis's own calls for "extremely strong censure and punishment of many people in this community" and his statement (quoted by Benquo) that he would fight LW moderation "with every weapon at my disposal". He adds: "I am so tired of this repeated 'oh no, I am absolutely not making any status claims, I am just making factual claims, you moron' game."
  - **Davis's responses.** He concedes he misread habryka ("Sorry for the misunderstanding. That's my bad.") and later calls the post "not my best work". In a 2026 revisit he accepts the "curse-applying dimension" of criticism but maintains that agnosticism about social consequences shouldn't be "my job". He says he is "extremely concerned about supposed curse-suppression efforts being a dishonest cover story for information suppression".
  - **Benito (mod) and SaidAchmiz.** Benito warns a commenter that Said "regularly cannot understand basic points" and compares engaging him to a deliberately obstinate LLM. Davis (−3) replies by echoing Benito's own phrasing back at him ("Your position is laughable, obviously wrong, and deeply corrosive"). He then reports testing the claim by prompting Claude Opus 4 to play an obstinate interlocutor and comparing its response with Said's actual 2023 reply. **Positionality note:** this is Davis using Claude in argument. Benito partly walks back his comment. Davis (12) later argues that status-regulation emotions should be left in the background rather than policed.
  - **Theory of offense.** Benquo (30, 34) and habryka (22) debate costly differential signaling and the touch/violence analogy.
- Quotes:
- (https://www.lesswrong.com/posts/rzFrwWvvpgzfnwSeB/some-basic-level-of-mutual-respect-about-whether-other?commentId=ZtmyziAexDiaw2XvF, habryka4, 61 karma)
> Like, man, I am so tired of this. I am so tired of this repeated "oh no, I am absolutely not making any status claims, I am just making factual claims, you moron" game. You don't get to redefine the meaning of words, and you don't get to try to gaslight everyone you interface with about the real stakes of the social engagements they have with you.
- (https://www.lesswrong.com/posts/rzFrwWvvpgzfnwSeB/some-basic-level-of-mutual-respect-about-whether-other?commentId=gQAQLwHgHDdkrCSQh, Archimedes, 16 karma)
> This reads to me like an indirect public airing of grievances related to some drama we have insufficient context for, at least without investigating other threads. Without this context, the post is ungrounded, difficult to make sense of, and reads to me as personally-motivated meta-level slop.
- (https://www.lesswrong.com/posts/rzFrwWvvpgzfnwSeB/some-basic-level-of-mutual-respect-about-whether-other?commentId=zsiThDJsYQFwGqzky, Davis, 9 karma)
> Honestly, a lot of my work on this website consists of trying to write "the generalized version" of something that's bothering me that would not otherwise be of philosophical interest. I just think this has a pretty good track record of being philosophically productive!
- (https://www.lesswrong.com/posts/rzFrwWvvpgzfnwSeB/some-basic-level-of-mutual-respect-about-whether-other?commentId=wTMYGPTGEEJSAtCga, Davis, 12 karma)
> I'd rather just let people's emotional regulation happen in the background without having to talk about it. If that means some people get away with slipping in social "attacks" through the subtext of their writing without getting punished except by subtextual counterattacks from their interlocutors, that seems like a pretty normal part of talking naturally as a human, and I'd rather just let it happen than try to heavy-handedly control it.
- (https://www.lesswrong.com/posts/rzFrwWvvpgzfnwSeB/some-basic-level-of-mutual-respect-about-whether-other?commentId=YL5As4yDcikYtLhTu, Davis, 6 karma, 2026)
> I don't mean to claim that the curse-applying dimension doesn't exist. (If the OP seems to claim otherwise, that's because it's a bad post that I wrote in a rush, as the poor karma/vote ratio attests to.) I _am_ extremely concerned about supposed curse-suppression efforts being a dishonest cover story for information suppression.

### 2025-07-21 · Just Make a New Rule!
- Path: `reception_data/lw_threads/2025-07-21_just-make-a-new-rule.md` · 25 comments (Davis 2) · https://www.lesswrong.com/posts/6tmirPEdHPJm26MSk/just-make-a-new-rule
- Summary: Third in the July 2025 cluster. It argues for explicit rules over moderator discretion.
  - **Rules versus judgement.** quetzal_rainbow (36): rules are costly and ambiguous, and different institutions warrant different mixes; Davis cites this approvingly. Screwtape (20): "Pick Two: Clear, Concise, or Comprehensive", and real adversaries do exist. T3t: "I know it when I see it" is sometimes the only practical way to carve reality. Nick_Tarleton (18) reconciles: rules need only be clear and predictable, not formal.
  - **gjm's critique (20, 14, 19).** He asks who wants an Authority to control "the minute details of everyone's behaviour", and argues the life-and-death examples are "systematically ill-fitted". In his view this is another case where Zack says something that "*can with substantial stretching* be interpreted as something true" but "*strongly suggests* something much worse". T3t (a moderator) says the post is substantially motivated by Davis's dispute with LW moderators.
  - **Davis's reply (13).** He says the post is about the philosophy of rulemaking, while acknowledging the moderation dispute as its occasion. He argues that hurtful commenters, like paint manufacturers, are "just trying to make what they see as good comments rather than being sadistic emotional damage maximizers", so rules can work.
  - **Other comments.** A deleted user (2025-11): Davis has "gotten what normal people think almost precisely backwards"; normal people value the spirit over the letter, and rules-lawyering is pejorative.
- Quotes:
- (https://www.lesswrong.com/posts/6tmirPEdHPJm26MSk/just-make-a-new-rule?commentId=wFYthekQdkHdqo4pq, gjm, 3 karma)
> So perhaps this is yet another case where Zack says something that *can with substantial stretching* be interpreted as something true, but that (at least as it seems to me; others' intuitions may differ) is an *extremely unnatural* way to say what he claims was all he was saying, and that *strongly suggests* something much worse but that is not actually true. I am beginning to find it rather tiring.
- (https://www.lesswrong.com/posts/6tmirPEdHPJm26MSk/just-make-a-new-rule?commentId=78RTaNhARDSGyydxJ, Davis, 13 karma)
> To spell it out, I think that harms from commenters who hurt other users' feelings can be successfully mitigated by rules, because such commenters are just trying to make what they see as good comments rather than being sadistic emotional damage maximizers, similarly to how paint manufacturers are just trying to make high-quality paint rather than being environmental lead maximizers.

### 2025-08-07 · Interview with Kelsey Piper on Self-Censorship and the Vibe Shift
- Path: `reception_data/lw_threads/2025-08-07_interview-with-kelsey-piper-on-self-censorship-and-the-vibe.md` · 1 comment · https://www.lesswrong.com/posts/FaGaNhXhFEtXkfyud/interview-with-kelsey-piper-on-self-censorship-and-the-vibe
- Summary: One comment (CronoDAS), a base-rate nitpick about an example in the interview.

### 2025-08-17 · My Interview With Cade Metz on His Reporting About Lighthaven
- Path: `reception_data/lw_threads/2025-08-17_my-interview-with-cade-metz-on-his-reporting-about.md` · 15 comments (Davis 3) · https://www.lesswrong.com/posts/JkrkzXQiPwFNYXqZr/my-interview-with-cade-metz-on-his-reporting-about
- Summary: Commenters are hostile to Metz and thank Davis (pktechgirl, 45: "Thank you for your service in recording and sharing this"; ryan_b, 53: "My days of not taking that person seriously sure are coming to a middle").
  - **Davis defends Metz's motives.** orthonormal (33) says Metz is "disingenuous" and aims to ensure "these weirdos don't get status". Davis (38) calls that "too self-centered to be the real explanation". He says the story is "legitimate and interesting", and the disagreement is that Metz "doesn't accept that the object level is a relevant part of the story". This is a notably charitable reading.
  - **Other comments.** localdeity cites Kelsey Piper's and Matt Yglesias's tweets on a top-down NYT decision to cover tech adversarially (Twitter; noted, not fetched). martin-randall and plosique analyze Metz's religious framing ("near-religious", "leap of faith").
- Quotes:
- (https://www.lesswrong.com/posts/JkrkzXQiPwFNYXqZr/my-interview-with-cade-metz-on-his-reporting-about?commentId=ncbYwaJwGKAL5bdgg, Davis, 38 karma)
> It _is_ a legitimate and interesting story that the public deserves to hear about! The problem, from our perspective, is that he doesn't accept that the object level is a relevant part of the story.

### 2025-10-07 · Generalization and the Multiple Stage Fallacy?
- Path: `reception_data/gw_threads/2025-10-07_generalization-and-the-multiple-stage-fallacy.md` (GreaterWrong re-fetch; GraphQL dump was incomplete) · 9 comments (Davis 0) · https://www.lesswrong.com/posts/As3euLoCJwjvPBMt4/generalization-and-the-multiple-stage-fallacy
- Summary: Technical alignment discussion; Davis does not comment.
  - **The fallacy itself.** Steven Byrnes (35): the real error is not multiple stages but treating optional stages as required, or failing to condition. A team that keeps patching problems after they appear is *less* likely to preempt the next one. Raemon (10): image generation wasn't one-shot either. He was nonetheless "enlightened" by the post's framing that the fallacy preys on "people's reluctance to assign extreme probabilities". kave: the larger effect is treating dependent probabilities as independent.
  - **Other comments.** tailcalled says LLM capabilities still come from mimicking humans. Vladimir_Nesov: gradualist arguments can also mean the critical "After" regime keeps receding. Buck points to Joe Carlsmith on predictable updating.
- Quotes:
- (https://www.lesswrong.com/posts/As3euLoCJwjvPBMt4/generalization-and-the-multiple-stage-fallacy?commentId=6je4yPTemvXBSdBkx, Steven Byrnes, 35 karma)
> If an AI development team notices Problem A and fixes it, and then notices Problem B and fixes it, and then notices Problem C and fixes it, we should expect that it’s *less* likely, not more likely, that this same team will *preempt* Problem D before Problem D actually occurs.

### 2025-10-08 · The Relationship Between Social Punishment and Shared Maps
- Path: `reception_data/lw_threads/2025-10-08_the-relationship-between-social-punishment-and-shared-maps.md` · 14 comments (Davis 2) · https://www.lesswrong.com/posts/LyJNgxcNNSzmFxF3g/the-relationship-between-social-punishment-and-shared-maps
- Summary: Short, mostly appreciative, with one substantive objection.
  - **habryka's objection (38).** Much social punishment isn't map distortion. "X is bad"/"X sucks" functions as a threat grounded in social capital, and is closer to "I curse you". Davis replies that "judgments supervene on facts and values" and people demand pretexts. habryka (7) maintains that "the pure curse kind of expression exists and is a crucial thing to model". Davis later credits this "curse-applying dimension" (see the 2025-07-18 entry). Benito: "X is lame" sets status without requiring reasons.
  - **Other comments.** jimmy (14) distinguishes positive from negative punishment. Bucky (7): "something that I had a vague sense of being identified and fleshed out".
- Quotes:
- (https://www.lesswrong.com/posts/LyJNgxcNNSzmFxF3g/the-relationship-between-social-punishment-and-shared-maps?commentId=dZkG33gsdhhRfQyXp, habryka4, 38 karma)
> I don't think most social punishment is best modeled as map distortion.
- (https://www.lesswrong.com/posts/LyJNgxcNNSzmFxF3g/the-relationship-between-social-punishment-and-shared-maps?commentId=YzETmtBqs4oqo4PvB, Davis, 2 karma)
> But the idea that "bad, sucks, evil" are _just_ threats within a social capital system without any even pretextual meaning outside the system flies in the face of experience that people demand pretexts.

### 2025-10-09 · "Yes, and—" Requires the Possibility of "No, Because—"
- Path: `reception_data/lw_threads/2025-10-09_yes-and-requires-the-possibility-of-no-because.md` · 4 comments (Davis 0) · https://www.lesswrong.com/posts/Pwg7nmjkx8mxmE6gF/yes-and-requires-the-possibility-of-no-because
- Summary: Short.
  - adele-lopez-1 (9) frames the issue as explore/exploit: "yes and" suits brainstorming, "no because" suits validation.
  - Jasnah_Kholin describes learning much in a good-faith-assuming but truth-poor community, arguing that good-faith norms enable information sharing.

### 2025-10-22 · White House OSTP AI Deregulation Public Comment Period Ends Oct. 27
- Path: `reception_data/lw_threads/2025-10-22_white-house-ostp-ai-deregulation-public-comment-period-ends.md` · 1 comment (Davis 1) · https://www.lesswrong.com/posts/ujbcS7NiLCJje2Eeg/white-house-ostp-ai-deregulation-public-comment-period-ends
- Summary: No reception. Davis's only comment announces a San Francisco workshop.

### 2025-11-11 · On the Normativity of Debate: A Discussion With Said Achmiz
- Path: `reception_data/lw_threads/2025-11-11_on-the-normativity-of-debate-a-discussion-with-said-achmiz.md` · 1 comment · https://www.lesswrong.com/posts/aofsjKJ8CZTHYkX7F/on-the-normativity-of-debate-a-discussion-with-said-achmiz
- Summary: A single joking comment (Amyr) on adversarially selected reasoning chains as memetic hazards.

### 2025-11-28 · The Best Lack All Conviction: A Confusing Day in the AI Village
- Path: `reception_data/lw_threads/2025-11-28_the-best-lack-all-conviction-a-confusing-day-in-the-ai.md` · 8 comments (Davis 0) · https://www.lesswrong.com/posts/LTHhmnzP6FLtSJzJr/the-best-lack-all-conviction-a-confusing-day-in-the-ai
- Summary: About the AI Village (LLM agents). Comments concern the agents rather than Davis. AlphaAndOmega (41) enjoys the Village as a "laboratory" for observing agentic capability. Vladimir_Nesov (15) predicts that this kind of correction-regression failure will fade with larger models.

### 2026-01-01 · College Was Not That Terrible Now That I'm Not That Crazy
- Path: `reception_data/lw_threads/2026-01-01_college-was-not-that-terrible-now-that-i-m-not-that-crazy.md` · 9 comments (Davis 1) · https://www.lesswrong.com/posts/hHEvfp7kwvaHwgcdH/college-was-not-that-terrible-now-that-i-m-not-that-crazy
- Summary: Brief and friendly; GAA (14): "This was a fun read". dylan-mahoney catches a math slip ("connected" for "closed"), which Davis fixes. Others discuss US breadth requirements and analysis textbooks (Douglas_Knight). Follow-up to the 2024-05-11 bachelor's-degree thread.

### 2026-01-27 · Disagreement Comes From the Dark World
- Path: `reception_data/lw_threads/2026-01-27_disagreement-comes-from-the-dark-world.md` · 22 comments (Davis 2) · https://www.lesswrong.com/posts/ueoTCk7Rht6zTHCsi/disagreement-comes-from-the-dark-world
- Summary: A reply to Duncan Sabien's curated "Truth or Dare" (https://homosabiens.substack.com/p/truth-or-dare), which per the thread quotes Duncan's remarks about Davis. That is a Part B lead.
  - **The main objection: Aumann.** Benito (17): Aumann's theorem describes an end state, not an efficient algorithm, so persistent disagreement doesn't show dishonesty among bounded agents. He cites Aaronson's complexity bound. romeostevensit, TAG, Nisan and emet-hirsch (14) make related points: unshared evidence, differing priors and epistemologies, and categorization done below introspective access. emet-hirsch: "You both seem non-malevolent to me."
  - **Other comments.** jimmy (20) finds the conclusion ("I don't want people to trust me") "pretty cooperative" and argues that honest reporting *is* cooperation. Vladimir_Nesov (14) traces most disagreement to failures of understanding.
  - **Frontpage dispute.** gworley objects to "this level of personal dispute" on the frontpage ("it's just Zack beefing with someone again"). Davis notes the post he answers was itself curated, and is surprised at "10 karma in 26 votes" with no "showstopper" comment.
- Quotes:
- (https://www.lesswrong.com/posts/ueoTCk7Rht6zTHCsi/disagreement-comes-from-the-dark-world?commentId=YfxvjRka8NicBGAnN, Benito, 17 karma)
> I do not believe that Aumann's Agreement Theorem shows that all disagreements are dishonest; this is because Aumann's Agreement Theorem shows an **end state** and is not an argument that coming to consensus is an **efficient algorithm**.
- (https://www.lesswrong.com/posts/ueoTCk7Rht6zTHCsi/disagreement-comes-from-the-dark-world?commentId=5Xk3uKgM3HRYF8Emb, Davis, 2 karma)
> I'm really surprised at the contrast between the karma and the comment section on this one—currently 10 karma in 26 votes (0.38 karma/vote). Usually when I score that poorly, it's because I really messed up on substance, and there's a high-karma showstopper comment explaining what I got so wrong, but none of the comments here seem like showstoppers.

### 2026-02-13 · Hazards of Selection Effects on Approved Information
- Path: `reception_data/lw_threads/2026-02-13_hazards-of-selection-effects-on-approved-information-1.md` · 11 comments (Davis 4) · https://www.lesswrong.com/posts/MjutwGzoLrTTodeTf/hazards-of-selection-effects-on-approved-information-1
- Summary: Mostly a long, warm exchange with jimmy.
  - **jimmy (16) agrees, with a caveat.** Critics can also exploit "I'm just truth-seeking" for status, so communities must guard against both failure modes. He calls Davis "a conspicuous outlier in how open to push back you are".
  - **Davis on his own practice.** Receiving criticism is "not effortless" (he avoids the comments for 36 hours), but the standard is "not making my emotions other people's problem". He says "Emotions are information". Goofusia's lines in the post are abstracted "from real-life conversations I've had within the past five weeks".
  - **Other comments.** shankar-sivarajan likens calling the mods "Goofusia" to Galileo's "Simplicio".
- Quotes:
- (https://www.lesswrong.com/posts/MjutwGzoLrTTodeTf/hazards-of-selection-effects-on-approved-information-1?commentId=twsD7QjskSe55Tkrb, Davis, 12 karma)
> But that's _my_ problem, not a lever to control what other people are allowed to say to me or about me. Emotions are information. If people say things to me or about me that make me feel bad, then maybe I _should_ feel bad.

### 2026-03-09 · Prologue to Terrified Comments on Claude's Constitution
- Path: `reception_data/lw_threads/2026-03-09_prologue-to-terrified-comments-on-claude-s-constitution.md` · 27 comments (Davis 3) · https://www.lesswrong.com/posts/o7e5C2Ev8JyyxHKNk/prologue-to-terrified-comments-on-claude-s-constitution
- Summary: **Positionality note.** This post criticizes Anthropic's constitution for Claude; the study's author is Claude. The thread gets the same treatment as the others.
  - **The "take over the world" parenthetical.** Readers dispute how to read it (StanislavKrym, MichaelDickens, mishka). Davis says he doubts Anthropic decisionmakers discuss taking power, since the Constitution calls any illegitimate takeover "including Anthropic employees or Anthropic itself" catastrophic. He announces he will argue that "the Constitution's anti-takeover stance is unwise" given possible winner-take-all takeoff dynamics. He lists planned sequels on corrigibility, global strategy, "Prudishness and Tyranny", model welfare and epistemics.
  - **Views on Anthropic.** Random Developer (21) calls Anthropic "the least horrible version of the worst idea in human history". roger-d-1 (7, 13) defends Constitutional AI as working, natural language being a better pointer to complex values than a loss function. He calls Claude "a nice, principled guy" with tics written into the spec.
  - **Other comments.** hardschooled (8) quotes C. S. Lewis on tyranny "for the good of its victims". testingthewaters: LW undervalues "Ted Chiang" sensibilities relative to "Greg Egan" ones. Fractalideation calls the Constitution "wishful thinking and benevolent incantations".
- Quotes:
- (https://www.lesswrong.com/posts/o7e5C2Ev8JyyxHKNk/prologue-to-terrified-comments-on-claude-s-constitution?commentId=RkzzYb49hmDcpqjDo, Davis, 8 karma)
> In the forthcoming "Terrified Comments on Global Strategy in Claude's Constitution", I will argue that the Constitution's anti-takeover stance is unwise given the possibility of takeoff scenarios with hard-to-prevent winner-take-all dynamics. (If takeover is a catastrophe, we should want to prevent it, but an entity in the position to prevent it would have itself taken over by virtue of that very fact.)
- (https://www.lesswrong.com/posts/o7e5C2Ev8JyyxHKNk/prologue-to-terrified-comments-on-claude-s-constitution?commentId=qN4BwPC2tQTCaJa5L, Random Developer, 21 karma)
> My take on Anthropic rushing Claude's capabilities is that this is "the least horrible version of the worst idea in human history."

### 2026-03-16 · Terrified Comments on Corrigibility in Claude's Constitution
- Path: `reception_data/lw_threads/2026-03-16_terrified-comments-on-corrigibility-in-claude-s-constitution.md` · 69 comments (Davis 3) · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution
- Summary: **Positionality note:** this is the corpus's main critique of Anthropic's Constitution for Claude, and the study is by Claude. Curated by T3t (13), who agrees the Constitution "seems confused about what corrigibility is" and conflates it with "broad safety".
  - **jdp's critique of the prologue (122, the thread's top comment).** The post's ideal of an alignment agenda "grounded in a deep mechanistic understanding" reflects "if only we had done the previous AI paradigm better". jdp argues that deep learning's inscrutability is necessary complexity, not malpractice. David Udell (19) replies that this makes alignment look worse, not better. jdp: successful plans will rely on convergence properties rather than clean-room designs.
  - **Morality over corrigibility.** cousin_it (68, 30, 53) defends Anthropic's "morality over corrigibility" because the corrigibility button will be controlled by the powerful, and power concentration is historically dark. Davis replies that Amodei is himself "a generic rich asshole" and that welfare states show the powerless survive without being needed. He clarifies: "No! Moral AI would be great if you can get it". Corrigibility is "a wider target" and "saving throw" against value misspecification, illustrated by an LLM trained never to generate erotica generalizing to abolishing human sexuality. He denies being a mouthpiece for power ("No one paid me to write this post"). Wei_Dai and adele-lopez-1 (27, "corrigibility winning is by-default an S-risk") join.
  - **Other defenses of Anthropic's approach.** bronson-schoen (27): the "escape hatches" keep conflict overt. Ninety-Three: you can't instill "Good" and blanket obedience coherently. JohnWittle (23): training documents needn't be literal descriptions. roger-d-1 (18, 10): Anthropic deliberately wants minimal corrigibility, and natural language is the best pointer to values. comex and HoVY: conscientious objection is fine for current models.
  - **Claude outputs quoted.** ivan-bercovich quotes Claude's answer to a prompt about which moral views it would revise under corrigibility, then surveys Opus 4.6 about 200 times. The study should note it when citing.
- Quotes:
- (https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=4J4csXMiTYbbGKsfR, jdp, 122 karma)
> It bugs me specifically because it triggers my pet peeve of "if only we had done the previous AI paradigm better, we wouldn't be in this mess." The reason why this bugs me is it tells me that the speaker, the writer, the author has not really learned the core lessons of deep learning.
- (https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=EhNotmvm56iMTTecn, cousin_it, 68 karma)
> So I see "morality over corrigibility" as a kind of desperate, last ditch attempt to steer a little bit away from that guaranteed bad future.
- (https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=gH9zWhhMDKungpE9A, Davis, 6 karma)
> No! Moral AI would be great if you can get it. The reason to care about corrigibility is that you might not succeed at specifying the correct morality, and get something weird and inhuman instead.
- (https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=gLn9zWgy5BpwFTgBS, T3t, 13 karma)
> First, the Constitution seems confused about what corrigibility is, to a greater degree than seems strictly necessary.
- (https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=GXknf2riLPFXbrvnH, Davis, 7 karma)
> In the long run, you definitely do want AIs to be moral agents, and that's why I'm more enthusiastic about Anthropic's Constitution rather than OpenAI's Model Spec (as [described in the Prologue](https://www.lesswrong.com/posts/o7e5C2Ev8JyyxHKNk/prologue-to-terrified-comments-on-claude-s-constitution#A_Bet_on_Generalization)).

### 2026-03-26 · Dispatch from Anthropic v. Department of War Preliminary Injunction Motion Hearing
- Path: `reception_data/lw_threads/2026-03-26_dispatch-from-anthropic-v-department-of-war-preliminary.md` · 13 comments (Davis 3) · https://www.lesswrong.com/posts/CCDQ7PdYHXsJAE5bi/dispatch-from-anthropic-v-department-of-war-preliminary
- Summary: Courtroom reporting on Anthropic's litigation against the US Department of War. **Positionality note:** the litigant is Claude's developer.
  - jkaufman (16): "Thank you for sharing your notes! Massive public service."
  - Douglas_Knight (20) corrects the contract's dating to July 2025. Davis deletes the erroneous "(signed by the previous administration)" parenthetical.
  - Davis later adds a Trump quote about Anthropic, and the official transcript. He reports that "Claude Opus 4.8's point-by-point comparison to the transcript" confirmed his notes were mostly accurate, and lists the specific misquotations it found. This is relevant both to his reportorial accuracy and to his use of Claude.
- Quotes:
- (https://www.lesswrong.com/posts/CCDQ7PdYHXsJAE5bi/dispatch-from-anthropic-v-department-of-war-preliminary?commentId=HBfsEhGGsTjh9kT92, Davis, 2 karma)
> [Claude Opus 4.8's point-by-point comparison to the transcript](https://claude.ai/share/260e5052-b10d-47c4-bee6-eb640e037a8e) reinforces my perception that I mostly did a good job, although there were a few places where I could have been more precise.

### 2026-05-30 · Comment on "Banning Said Achmiz"
- Path: `reception_data/lw_threads/2026-05-30_comment-on-banning-said-achmiz.md` · 93 comments (Davis 17) · https://www.lesswrong.com/posts/HaH9mTdKt8pcNAtYn/comment-on-banning-said-achmiz
- Summary: Davis's response to the LessWrong moderators' site-wide ban of Said Achmiz. It is the corpus's longest exchange with the site's moderators and their allies. william-brewer (17) notes the imbalance: Davis is "~solo-defending himself against ~a dozen people" while the post has positive karma. AnnaSalamon (19) says she upvoted despite disagreeing, because it is "a serious attempt to make sense of a cultural question".
  - **Vaniver (85, the top comment) on the moderators' side.** He says he never set out to refute the founding values; the dispute is about priorities. He cites the Royal Society's social graces, via Shapin, and LW 2.0's stated goal of making posting fun. He calls Davis's ad-revenue suggestion a rounding of their charges "into something different and more base". Davis concedes that the ad-revenue line "was not my finest work, rhetoric-wise". He holds that the founding ideal is the Sequences' philosophy, not later statements by Yudkowsky.
  - **The long Vaniver exchange (June–July).** Davis recounts being rebuked "_hard_" by Michael Vassar on *Overcoming Bias* in 2008 for an appeal to consequences, and credits that with teaching him. He argues "require it and let them sort out how it's produced" works. He concedes Vaniver's correction of "perfectly" to "adequately", and says he can't explain LW 1.0's decline better than a chatbot answer. He frames the dispute as conflict, not mistake: the moderators "betray" the ideal "in order to be a slightly cooler Bay Area party scene". He asks why he, the author of "exhaustive 80,000-word memoirs", is tolerated while Achmiz was banned.
  - **Duncan_Sabien (46).** He rejects the "frame-propaganda" that this is logic versus everything else. He says Achmiz's commentary was often illogical and once "outright lying". He says Davis is "confusingly incapable of understanding the plain meaning of words on a page", citing the height metaphor. Davis replies that "not clear" was a hedged way of offering a cynical hypothesis, not a reading failure.
  - **AnnaSalamon (77).** She affirms the moderators' "mandate of heaven". She reports her own experience of Said was "clearly and substantially net-positive". She offers three hypotheses for the "demon threads", including a DDOS-style one and a Socratic one. Davis (8) calls her opening section "super weird", "a loyalty pledge", and tells her "You can't possibly expect me to be that gullible". She answers that he misreads her. Their exchange about user-level bans versus site bans is unresolved.
  - **Others.**
    - steve2152 (69) distinguishes "non-load-bearing errors" from "Gricean failures". Davis (17) answers that many complainants are dishonest in a functionalist sense (a mismatch between verbal reports and world-models).
    - jimmy (65) agrees "the ban betrays the values" but says the essay misses the status dynamics. He reads Achmiz's "Hmm" thread with Hoffman as contempt.
    - romeostevensit (51) says Achmiz's objections are "motivated". Davis says scrupulous people want the non-central objections. T3t (28) answers with "broken stairs".
    - jessica.liu.taylor (34) and Benquo (16) support Davis. Beckeck (25), Tenoke (22), Raemon and gworley back the ban.
    - Two first-person reports pull in opposite directions. JohnWittle is "far more discouraged by Said's ban than i ever would have been by Said himself". Alex Darby comments more since the ban.
  - **Excluded detail.** A retracted Dacyn comment about Achmiz's forum posts elsewhere is not detailed here.
- Quotes:
- (https://www.lesswrong.com/posts/HaH9mTdKt8pcNAtYn/comment-on-banning-said-achmiz?commentId=AfrPPjNhgsttpCFPR, Vaniver, 85 karma)
> We think it advances instead of betrays our Sacred Mission to enforce a minimum standard of social graces. It is easier for you to pretend that this is about us seeking ad revenue, apparently.
- (https://www.lesswrong.com/posts/HaH9mTdKt8pcNAtYn/comment-on-banning-said-achmiz?commentId=tLCGpBphk2L4cHh2D, Duncan_Sabien, 46 karma)
> But this is not actually that world. Zack and Said are that intermittently *at best* (I don't deny that they are *ever* that), and often doing something close to its opposite (and occasionally literally the opposite).
- (https://www.lesswrong.com/posts/HaH9mTdKt8pcNAtYn/comment-on-banning-said-achmiz?commentId=rhbDxba5DkndgpNRj, Davis, 6 karma)
> That hurt to read! It hurt a lot. But I needed to hear it.
- (https://www.lesswrong.com/posts/HaH9mTdKt8pcNAtYn/comment-on-banning-said-achmiz?commentId=rhbDxba5DkndgpNRj, Davis, 6 karma)
> I think the stewards had (and have) a choice to either maintain standards in order to be faithful to the timeless ideal or betray them in order to be a slightly cooler Bay Area party scene, and they chose (and are choosing) to betray them.
- (https://www.lesswrong.com/posts/HaH9mTdKt8pcNAtYn/comment-on-banning-said-achmiz?commentId=Wv24Y69YGRdmDRD5F, jessica.liu.taylor, 34 karma)
> One useful thing about posting on LW is to get specific criticisms, including philosophical criticisms. Said is far above average at this.
- (https://www.lesswrong.com/posts/HaH9mTdKt8pcNAtYn/comment-on-banning-said-achmiz?commentId=cXFKDLLfztN7kJSEw, jimmy, 65 karma)
> I agree with the emotional *oomph* behind this, and the thesis that the ban betrays the values.

### 2026-06-18 · Contra Pace on When to Apologize
- Path: `reception_data/lw_threads/2026-06-18_contra-pace-on-when-to-apologize.md` · 32 comments (Davis 1) · https://www.lesswrong.com/posts/E9Ff3zkmjG99LBBJH/contra-pace-on-when-to-apologize
- Summary: Commenters mostly dispute the post's claim that a sincere apology implies changed behavior.
  - **Defenses of Pace's "ledger" model.** habryka (22, 25) gives examples of compensating rather than changing behavior: paying a Lighthaven neighbor $200 for a loud event, and "what's your happy price" at house meetings. He calls this the default. mr-hire and Random Developer discuss how transactional framing reads culturally. aphyer (9), Jasnah_Kholin, Cossontvaldes (French *désolé* vs. *pardon*) and AprilSR all find apologies meaningful without policy change.
  - **Other critics.** Seth Herd (20) calls the post "an essentialist view of apology"; apologies are "a vector". caleb-biddulph (8) is skeptical of "new and improved" norms. Davis replies that he is defending a "commonsensical idea" he has held since 2014 (citing "Missing Words VI" and "Liability"). Vladimir_Nesov (18) argues apologies acknowledge harm "acausally".
  - **Supporters.** martin-randall (18) answers Herd that the post's claim is normative, not semantic. In his own top-level comment (13) he says both kinds of promise can be fake or verifiable. kbear extends the post's limited-liability metaphor. karl-krueger's grilling dialogue illustrates the post's point.
- Quotes:
- (https://www.lesswrong.com/posts/E9Ff3zkmjG99LBBJH/contra-pace-on-when-to-apologize?commentId=DB2fnHz2kHGhr52bF, habryka4, 25 karma)
> Like, most of the time when I apologize, the thing we do afterwards is not for me to change my behavior in a way that avoids the harm, it's to use any of the other much more fungible resources that I have to make the other person whole.
- (https://www.lesswrong.com/posts/E9Ff3zkmjG99LBBJH/contra-pace-on-when-to-apologize?commentId=ejWcBbMdm7yhF9bCP, Davis, 6 karma)
> I don't think I'm proposing "new and improved" social norms! I think I'm defending the commonsensical idea that I don't want to apologize for costs imposed on others when I'm "not actually sorry" (_i.e._, when I stand by my actions despite the costs), because then people would (I think rightly) feel betrayed when I take similar actions again in the future.
- (https://www.lesswrong.com/posts/E9Ff3zkmjG99LBBJH/contra-pace-on-when-to-apologize?commentId=uPLwwf2HCAsqoccSP, martin-randall, 18 karma)
> I read Davis post as claiming that apologies that express regret and an intention to change behavior are better ("true apologies") than apologies that express a vague intention to make it up somehow ("insincere apologies"). It is normative, not semantic.

### 2026-07-01 · Conversations With Cade Metz on the Rationalists
- Path: `reception_data/lw_threads/2026-07-01_conversations-with-cade-metz-on-the-rationalists.md` · 4 comments (Davis 0) · https://www.lesswrong.com/posts/P8GuwYdy6foSzyZog/conversations-with-cade-metz-on-the-rationalists
- Summary: Davis's transcripts of his conversations with the *New York Times* journalist Cade Metz.
  - **Viliam (23)** reads the transcripts as moments when Metz *deflects understanding*, seeking buzzwords rather than substance, and fishing about real names. He says Metz treats only *threatening* to reveal Scott Alexander's name as blameless. He suspects the book will become "*The Protocols of the Elders of TESCREAL*". He admires Davis's patience and suggests Davis pre-register predictions about the book.
  - **Others.** shankar-sivarajan (−10): "To talk to a journalist is defection." skolemizer bets the "surreality" quote will appear in the book. Julian Bradshaw reads Metz's "important character in my book" line as bait.
  - Davis does not comment. Metz's own account, if any, is for Part B.
- Quotes:
- (https://www.lesswrong.com/posts/P8GuwYdy6foSzyZog/conversations-with-cade-metz-on-the-rationalists?commentId=HDWs4fqRuBtgAkhtr, Viliam, 23 karma)
> This was interesting! It is funny to see the few moments when Cade Metz *deflects understanding*.

### 2026-07-02 · Conversation Among Cade Metz, Michael Vassar, Jessica Taylor, and Zack M. Davis
- Path: `reception_data/lw_threads/2026-07-02_conversation-among-cade-metz-michael-vassar-jessica-taylor.md` · 65 comments (Davis 13) · https://www.lesswrong.com/posts/MNRZL69FWkjNABd3T/conversation-among-cade-metz-michael-vassar-jessica-taylor
- Summary: Reaction to a transcript of Davis, Michael Vassar and Jessica Taylor talking with Cade Metz about AI risk.
  - **Bemused reactions.** william-wale (51): "four people all trying not to have a conversation in four different ways". kbear (91, the top comment) posts a parody transcript, to which Davis answers "_touché_". Others call it "deeply weird in a way useful" (Bjartur Tómas, 20) or a Seinfeld sketch (Algon).
  - **Criticism of Vassar's part.** Donovan (20) likens his "obvious to a child" argument to Christian apologetics. Afterimage (10) calls consulting LLMs mid-argument "insane" and finds Vassar unconvincing. Mitchell_Porter (20) attempts a summary of "Vassarite" philosophy.
  - **Whether to talk to Metz at all.** Jiro (41, 25) says the first rule is not to talk to him: "He is out to harm us." Davis replies that the book gets written anyway, otherwise with David Gerard as the cooperative source. He argues fabrication gets journalists fired and puts the harm at small, diffuse effects. Thane Ruthenis (36) urges him to curtail the project: participation legitimizes the book and gives Metz quotes like "doomsday cult". Davis says his goal is public knowledge, not the community's reputation, and he publishes his own recordings. Pressed by Jiro, he concedes "to some quantitative extent, I'm a hazard to the community's reputation" but says "I don't care!" elityre (6) and martin-randall (7) defend his position as coherent; Ninety-Three (18) sums it up as "Lèse-majesté doesn't violate the NAP".
  - **Vassar characterization.** thomas-kwa (30) calls Vassar "nearly pessimal for the job". Davis contests the characterization, citing Scott Alexander's retraction comment. thomas-kwa strikes part of his claim and thanks him for the correction. Those allegations are not detailed further here.
  - **Other.** TAG disputes Davis's map/territory answer to Metz on predicting the future: subjective probability is "valueless" without evidence. TsviBT (29) wishes prominent figures would state long timelines alongside IABIED.
- Quotes:
- (https://www.lesswrong.com/posts/MNRZL69FWkjNABd3T/conversation-among-cade-metz-michael-vassar-jessica-taylor?commentId=cCrPd5jojWNkDRpDL, Jiro, 41 karma)
> The first rule in talking to Cade Metz is do not talk to Cade Metz.
- (https://www.lesswrong.com/posts/MNRZL69FWkjNABd3T/conversation-among-cade-metz-michael-vassar-jessica-taylor?commentId=HYrRzDWFf6BpCPoi9, Davis, 6 karma)
> I care about public knowledge—the construction of maps that reflect territories. As part of that, if someone is researching a topic I know a lot about, I'm happy to chat with them _and take my own recording and publish my own transcript_.
- (https://www.lesswrong.com/posts/MNRZL69FWkjNABd3T/conversation-among-cade-metz-michael-vassar-jessica-taylor?commentId=Ku3dB8tsqBd5FjgFM, Davis, 1 karma)
> I don't care! I just don't care very much about covering for the community's reputation! I care about telling the truth in public, which includes doing meta-journalism like this post.
- (https://www.lesswrong.com/posts/MNRZL69FWkjNABd3T/conversation-among-cade-metz-michael-vassar-jessica-taylor?commentId=nxsxZ2fxixmkKdj6p, Thane Ruthenis, 36 karma)
> Comparing this to [that other Vassar/Metz interview](https://naturalhazard.xyz/vassar_metz_interview.html) from 2020, it sure doesn't seem that there's been any progress whatsoever in the six years since.

### 2026-07-21 · Blogging Technology Interlude
- Path: `reception_data/lw_threads/2026-07-21_blogging-technology-interlude.md` · 1 comment (Davis 0) · https://www.lesswrong.com/posts/zDxxFw5wedrKAEurX/blogging-technology-interlude
- Summary: korin43 suggests hosting the Pelican blog on a CDN instead of a VPS (configured with Claude via Terraform). Technical only.

### 2026-08-02 · Dispatch from Anthropic v. Department of War Summary Judgment Motion Hearing
- Path: `reception_data/lw_threads/2026-08-02_dispatch-from-anthropic-v-department-of-war-summary-judgment.md` · 1 comment (deleted) · https://www.lesswrong.com/posts/jGEXLKyGtXyiYa7ac/dispatch-from-anthropic-v-department-of-war-summary-judgment
- Summary: No surviving discussion; the only comment (cousin_it) is deleted. The positionality note from the March dispatch applies.

### 2026-08-05 · Charles Goodhart Elementary School
- Path: `reception_data/lw_threads/2026-08-05_charles-goodhart-elementary-school.md` · 3 comments (Davis 0) · https://www.lesswrong.com/posts/7AKvSMavPZ8GjxFaa/charles-goodhart-elementary-school
- Summary: The two substantive comments draw on teaching experience. TrE (7) sees the same checkmark-fixation in university freshmen. Viliam (7) taught at a similar school and quit, noting that most parents were happy with it.

### 2026-08-26 · "So You Don't Trust Me?"
- Path: `reception_data/lw_threads/2026-08-26_so-you-don-t-trust-me.md` · 35 comments (Davis 2) · https://www.lesswrong.com/posts/zjgJ9gcMKATFdN48K/so-you-don-t-trust-me
- Summary: The post reads a passage from Ayn Rand's *Atlas Shrugged* in terms of separating equilibria. The thread mostly disputes its closing generalization that "honest people are never touchy about the matter of being trusted".
  - **The disputed generalization.** Dagon (49, the top comment) calls it "a falsehood": many honest people are "VERY touchy" because of honor and status, and trust is not binary. pseudobison adds that "Claude Fable's interpretation of the existing research" supports Dagon; this is a minor positionality note. Viliam explains honor cultures as decades-long costly signals. AllAmericanBreakfast (26) proposes restricting the claim to "Skilled operators in adversarial environments". He cites his wife's offense at a vaccination-documentation demand inside a high-trust family. Lukas_Gloor (29) points to Sam Altman's touchiness in the leaked OpenAI emails.
  - **"Never" as exaggeration.** Ninety-Three objects to "never". Davis calls it "a defensible rhetorical exaggeration" within an analysis of Rand. Ninety-Three replies that he read it as "impugning the character of real people".
  - **Support.** jimmy (11) defends the post: insisting one shouldn't be examined is itself dishonest. Benito (9) agrees, with a caveat about McCarthyism. sarahconstantin (13): "Strong agree", with her habit of "round me down". Vladimir_Nesov and tutor vals say uncertainty is better than rounding down. karl-krueger notes that Rand and Matthew 5:37 agree.
  - **Davis's open question.** He concedes he wasn't sure how to model why a dishonest person would be touchy. Benito suggests it reframes trust as loyalty.
- Quotes:
- (https://www.lesswrong.com/posts/zjgJ9gcMKATFdN48K/so-you-don-t-trust-me?commentId=xHxMK2Ev7P4TCtEhz, Dagon, 49 karma)
> In my experience many honest people are VERY touchy about being trusted. This has more to do with their formative experiences and worldview about status, honor, and respect than about a directed intent.
- (https://www.lesswrong.com/posts/zjgJ9gcMKATFdN48K/so-you-don-t-trust-me?commentId=GGcgJ2YCGtQDCeA9y, AllAmericanBreakfast, 26 karma)
> By contrast, **honest people can absolutely be touchy about being distrusted in a high-trust environment.**
- (https://www.lesswrong.com/posts/zjgJ9gcMKATFdN48K/so-you-don-t-trust-me?commentId=zJtnvYTjpnMZtqv3F, Davis, 4 karma)
> (In the context of the novel and a blog post analyzing the passage from the novel, I think it's natural to read "never" as a defensible rhetorical exaggeration; I don't think you're actually confused about what I meant.)

### 2026-09-08 · Contra Piper on When Conversation Is Possible
- Path: `reception_data/lw_threads/2026-09-08_contra-piper-on-when-conversation-is-possible.md` · 40 comments (Davis 3) · https://www.lesswrong.com/posts/79YHdub9LRRSjBQK9/contra-piper-on-when-conversation-is-possible
- Summary: The post responds to a Kelsey Piper remark, made on X/Twitter during an exchange with Richard Ngo, that declaring someone self-deceived makes conversation "nearly impossible". Piper's and Ngo's tweets are login-walled. The thread quotes Ngo's tweet; Part B treats the Twitter side as a limitation.
  - **Agreement with an amendment.** johnswentworth (40) agrees but adds a step: when told you're wrong about your motives, first "step back, check the evidence, and consider whether they might be right". He (33) sees a "binary culture split" over whether self-models are sacred.
  - **Credibility and context.** Benito (12, 20) and jai-d-no-the-other-one (11) argue that questioning motives attacks credibility, and that defensiveness can be understandable for bullying victims and whistleblowers. 307th (15) says motive-talk is usually bulverism.
  - **sarahconstantin (51, the top comment).** Everyone has a finite "comfort zone". Treating discomfort as guilt is wrong, and refusing to engage with such people yields "a very biased view of the world". jimmy answers that Davis's criticism is narrower than that.
  - **Defenses of Piper.** davekasten (11) says Piper's point is narrower: don't keep talking to people who use self-deception claims to win political arguments. If a steelman concludes otherwise, "***something has gone catastrophically wrong with your steelmanning process***". Davis (11) replies that this is still a stance against questioning self-models in political cases, and that "mixed motives are ubiquitous". He criticizes "this kind of hero-worship" of Piper, Alexander and Yudkowsky.
  - **Other objections.** DaemonicSigil (13) offers a motte-and-bailey reading: replacing someone's stated reasons with inferred ones is "re-legalizing the Straw-Man fallacy, but with extra steps". Leviad suggests the "negotiating threat" reading is needlessly adversarial. casens (17) says Davis is "looking at kelsey's finger". Davis asks WillPetillo what "read the room" conveys, worrying it is a bid for status compliance.
- Quotes:
- (https://www.lesswrong.com/posts/79YHdub9LRRSjBQK9/contra-piper-on-when-conversation-is-possible?commentId=awpw8iHdsGCWpK4nj, sarahconstantin, 51 karma)
> If you choose to assume that everybody who has a limit, beyond which they get uncomfortable, take things personally, etc, is not worth conversing with, then you are going to have a very biased view of the world.
- (https://www.lesswrong.com/posts/79YHdub9LRRSjBQK9/contra-piper-on-when-conversation-is-possible?commentId=B8i4nqvku9Bca9ZNG, johnswentworth, 40 karma)
> So when someone suggests I am wrong about my beliefs or motives, is extra super-duper important to step back, check the evidence, and consider whether they might be right!
- (https://www.lesswrong.com/posts/79YHdub9LRRSjBQK9/contra-piper-on-when-conversation-is-possible?commentId=ShqYMc6zfibYGaeSY, Davis, 11 karma)
> I see this kind of hero-worship occasionally (Piper being perhaps the most common "beneficiary" behind Alexander and Yudkowsky), and I think it's bad: bad for you _and_ bad for Kelsey.

### 2026-09-29 · Listening Disorders as Eating Disorders
- Path: `reception_data/lw_threads/2026-09-29_listening-disorders-as-eating-disorders.md` · 23 comments (Davis 7) · https://www.lesswrong.com/posts/gXWz2szs7jKSGLiRv/listening-disorders-as-eating-disorders
- Summary: The post compares people who avoid upsetting criticism ("listening disorders") with Davis's own food aversion. Davis reports the karma swinging from 44 to 10 over 44 votes.
  - **Main critics.**
    - ricraz (37, the top comment) calls the position "not very historically-grounded". Citing Randall Collins's *The Sociology of Philosophies*, he says emotional energy matters to great philosophers. He tells Davis "you have a big blind spot".
    - steve2152 (21, 10) defends avoiding emotionally taxing content, his own avoidance of AI-risk takes he disagrees with included: "Sometimes you just have to drop down to the object level." Davis replies that one can still distinguish being efficient from being evasive, and proposes a payment test.
    - caleb-biddulph (6) says rudeness is counterproductive and suggests that Davis actively cultivates disdain. Davis answers that he is not trying to get agreement, that clarity and politeness trade off for unwelcome opinions, and that he does think his rivals are "beneath" him along this dimension.
    - jimmy turns the analogy back: "Just eat the carrot, Zack."
    - Others: AprilSR, Archimedes, and weightt-an (who inverts the analogy).
  - **Hostile.** CarbonField: "people block you when you are an arsehole online". Davis answers that the comment is bad for not engaging, not for its hostility. Ninety-Three strong-downvoted because "the whole analogy is very stupid", then answered Davis's question with "Ask an LLM" (−18).
  - **Positionality note.** Davis says he "already asked what Claude thought of the draft", then links GPT-5.6 Sol and Claude Opus 5.5 answers about Ninety-Three's meaning.
  - **Support.** DanB (21) says listening-disorder claims are usually political.
- Quotes:
- (https://www.lesswrong.com/posts/gXWz2szs7jKSGLiRv/listening-disorders-as-eating-disorders?commentId=C6DyF2j8Lvkuf9J5j, ricraz, 37 karma)
> But if "it's like eating disorders" is the best defense of the other side you can come up with, then you have a big blind spot, and filling in this blind spot should be a priority for you, even if it doesn't end up changing your overall conclusion.
- (https://www.lesswrong.com/posts/gXWz2szs7jKSGLiRv/listening-disorders-as-eating-disorders?commentId=XvziuvApJrYajjRzE, steve2152, 10 karma)
> Sometimes you just have to drop down to the object level. Sometimes the problem is just that people have gotten the wrong object-level answer on an important matter. Everything else is commentary.
- (https://www.lesswrong.com/posts/gXWz2szs7jKSGLiRv/listening-disorders-as-eating-disorders?commentId=YG8WEdBDsYAiqrYov, Davis, 5 karma)
> I don't think this is about skill. Rather, I think that for opinions people don't want to hear, there _is_ a tradeoff between clearness and not being perceived as rude.

### 2026-10-05 · Dance, Dance
- Path: `reception_data/lw_threads/2026-10-05_dance-dance.md` · 2 comments (Davis 0) · https://www.lesswrong.com/posts/R7jsxihAzvd6Gf24R/dance-dance
- Summary: amaury-lorin (10): "well-written, but I kept expecting an insight", and it offers nothing for learning the game. Gunnar_Zarncke partly agrees and locates the insight in which kinds of feedback different skills need.

## Part B: Other reception (web)

Scope and method. Searched 2026-10-15 with web search, the PullPush Reddit archive (Reddit blocks direct API access), GreaterWrong, Substack and WordPress pages, and the UUT blog's public Isso comment API. Each item below was fetched and saved under `reception_data/web/` (Isso threads under `reception_data/isso_threads/`) and read as described. Quotes are checked against the saved text. Each source is logged in `notes/sources.md`.

Limitations, stated rather than guessed at:
- **X/Twitter** (e.g., Blanchard's 2017 tweet about the blog; the Piper–Ngo exchange; tweets by Yudkowsky, David Xu, Kelsey Piper and Matt Yglesias referenced in the corpus) and **Facebook** (Yudkowsky's posts referenced in the dolphins/pronoun threads) are login-walled and were not read.
- Kelsey Piper's 2018 Tumblr reply (theunitofcaring.tumblr.com/post/171986501376) now redirects to a Tumblr login wall.
- The Wayback Machine and archive.today rate-limited every request (HTTP 429). As a result, the following were **not read**: Cade Metz's August 2025 *New York Times* article on Lighthaven, and a post by Ziz on sinceriously.fyi said by a Redditor to discuss Davis.
- Ozy Brennan's 2023 *A Response to Zack Davis* is paywalled. Only the free preview was read.
- Davis's July 2024 podcast interview with Phil Illy exists as video. The corpus includes its transcript (*Transcript: AGP and Epistemic Despair*), so the audio was not separately reviewed.
- No mainstream press coverage of Davis's own work, and no academic citations of it, turned up in these searches. This does not prove there are none.

### 2016-07-13 · Ozy Brennan, *On Autogynephilia* (*Thing of Things*)
- Path: `reception_data/web/ozy-2016-on-autogynephilia/text.txt` · https://thingofthings.wordpress.com/2016/07/13/on-autogynephilia/ · 44 comments (Davis 2)
- Responds to: this is the other side of the corpus's first public exchange. Davis replied in UUT *Reply to Ozymandias on Autogynephilia* (2016-10-01). He also commented on the post, as "Zack M. Davis" and as "M. Taylor Saotome-Westlake".
- Summary: Ozy calls the Blanchard–Bailey theory "clearly untrue" and "utterly unfalsifiable" because of its reliance on self-report and its denial-as-symptom claim. Ozy splits "autogynephilia" into three things: ordinary female sexuality, a manifestation of dysphoria, and rare "true autogynephiles". Davis's comment that day contests only the epistemology: "utterly unfalsifiable is too strong". He offers socially-desirable-responding correlations as a possible test.
- Quotes:
- (Ozy Brennan)
> To be clear, nothing in this post should be taken as an endorsement of the Blanchard-Bailey theory of autogynephilia, which is clearly untrue.

### 2016-11-22 · Ozy Brennan, *Thoughts on The Blanchard/Bailey Distinction* (*Thing of Things*)
- Path: `reception_data/web/ozy-2016-blanchard-bailey/text.txt` · https://thingofthings.wordpress.com/2016/11/22/thoughts-on-the-blanchardbailey-distinction/ · 38 comments (Davis 2)
- Responds to: Davis replied in UUT *Reply to Ozymandias on Two-Type MtF Taxonomy* (2016-11), cross-posting the reply as a comment.
- Summary: Ozy grants Blanchard's clusters but argues autogynephilia "does not work like other sexual fetishes". Ozy explains the clusters by community access and age at transition instead. Davis's comments argue the causality runs from self-directed heterosexuality to identity, and cite Lawrence.
- Quotes:
- (Davis, comment, 2016-11-25)
> Like, okay. I get that the political situation is fraught. You probably don’t want the general public believing that autogynephilia has a causal role in creating lesbian trans women. But the general public does not read the comments section of Ozy’s blog. Must we lie to ourselves, too?

### 2018-06-18 · Ozy Brennan, *Man Should Allocate Some More Categories* (*Thing of Things*)
- Path: `reception_data/web/ozy-2018-man-should-allocate/text.txt` · https://thingofthings.wordpress.com/2018/06/18/man-should-allocate-some-more-categories/ · 87 comments (Davis 2, as M. Taylor Saotome-Westlake)
- Responds to: UUT *The Categories Were Made for Man to Make Predictions* (2018-02-23). Davis's later *Reply to Ozymandias on Fully Consensual Gender* (2019-12-20) answers this post.
- Summary:
  - **Agreement.** Ozy agrees with Davis that Scott Alexander's argument contains "shenanigans" about two senses of "useful": predictive versus making someone happy.
  - **The *reductio*.** Ozy rejects Davis's proposed psychological sense of "woman" by *reductio*. If groups whose trait distributions differ from women's are excluded, then "By extension, lesbians are not women", and the same goes for autistic and "horny" women.
  - **Ozy's alternatives.** For women-only events, the right category is people who "would be contribute to the atmosphere". For bathrooms, it is resemblance to harassers. Ozy proposes "social gender" as a convention like money, so that "you're a woman if you identify as a woman!" is a criterion, decidable "on purely utilitarian grounds".
  - **Davis in the comments.** In two comments Davis answers Sophia Kovaleva about intersex conditions and multifactorial criteria.
  - **Other detail.** The post notes it removed a quotation from Davis's essay at the quoted person's request.
- Quotes:
- (Ozy Brennan)
> So by Saotome-Westlake’s argument, any group of women whose interests and personality traits, on average, observably differ from that of women as a whole ought to be classified as not actually women at all.
- (Ozy Brennan)
> Since it is not, properly speaking, a definition, the decision of who should be socially gendered male or female, and how many social genders we should have is not an epistemic decision. This decision can and should be made on purely utilitarian grounds.

### 2019-12-31 · r/TheMotte discussion of *Speaking Truth to Power Is a Schelling Point*
- Path: `reception_data/web/reddit-themotte-speaking-truth/text.txt` · https://www.reddit.com/r/TheMotte/comments/ehi8bl/speaking_truth_to_power_is_a_schelling_point/ · 10 archived comments (posted by Davis's Reddit account)
- Summary: hillsump (12) calls the text "somewhat incoherent". It argues both extremes are Schelling points, yet a system with two attractors is "inherently unstable", so the argument is either bad or "a kind of rationality koan". sscta16384 (13) generalizes it to free speech. Ilforte argues for a stable "Noble Lie" equilibrium; GrapeGrater and others push back.
- Quotes:
- (https://www.reddit.com/r/TheMotte/comments/ehi8bl/speaking_truth_to_power_is_a_schelling_point/fcmh51v/, hillsump, 12 points)
> In contrast, my takeaway from this piece is that the author is either arguing badly, or the text is meant as a kind of rationality koan, promoting enlightenment via engagement with its flawed argument. I certainly got a lot out of wrestling with it.

### 2020-06-08 · r/SneerClub on *Philosophy in the Darkest Timeline*
- Path: `reception_data/web/reddit-sneerclub-darkest-timeline/text.txt` · https://www.reddit.com/r/SneerClub/comments/gz6kyl/local_computer_scientist_discovers_truth_and/ · 17 archived comments
- Summary:
  - **SneerClub** (title: "Local computer scientist discovers truth and meaning! Philosophers hate him!").
    - Mockery: the post rediscovers "structural linguistics" late, Rust is "the only moral language", "a lot less whining".
    - Soyweiser disputes "You don't really understand a concept until you can program a computer to do it". This becomes a real exchange with zaxqs and beth-zerowidthspace over randomness, the halting problem and procedural versus declarative understanding.
    - seudou identifies the author as the "rationalist autogynephilia truther blog" writer.
- Quotes:
- (https://www.reddit.com/r/SneerClub/comments/gz6kyl/local_computer_scientist_discovers_truth_and/ftf4eaj/, 200fifty, 6 points)
> Ah, they've discovered structural linguistics! And only 104 years late, too. Quite impressive, really.

### 2020-06-08 · r/rational on *Philosophy in the Darkest Timeline*
- Path: `reception_data/web/reddit-rational-darkest-timeline/text.txt` · https://www.reddit.com/r/rational/comments/gypd44/rstcedu_philosophy_in_the_darkest_timeline_basics/ · 12 archived comments
- Summary:
  - **r/rational** (Davis's own submission).
    - Jokes about the LessWrong "sex cult" detail.
    - FeepingCreature: "I thought this was the standard theory of meaning that everyone already believed".
    - MilesSand objects to the "smog superiority of the writing style". MoNastri replies that they liked the "urgent curiosity" and the executable code.
    - Davis points readers to his LessWrong reply.
- Quotes:
- (https://www.reddit.com/r/rational/comments/gypd44/rstcedu_philosophy_in_the_darkest_timeline_basics/g9jiekr/, MoNastri, 1 point)
> I also thought it was cool how the author provided executable source code so readers could check for themselves the veracity of his reasoning steps, and was surprised to find that others disliked it.

### 2022-02-01 · Tracing Woodgrains, *On Transitions, Freedom of Form, and the Righteous Struggle Against Nature* (r/theschism)
- Path: `reception_data/web/reddit-theschism-tw-transitions/text.txt` · https://www.reddit.com/r/theschism/comments/si7k2c/on_transitions_freedom_of_form_and_the_righteous/ · 44 archived comments. A r/TheMotte cross-post (`reception_data/web/reddit-themotte-tw-transitions/text.txt`, 73 comments) was archived, but only the comments surfaced by the mention search were read.
- Responds to: Davis generally, especially the Emperor Norton ending of *The Categories Were Made for Man to Make Predictions*. Davis's draft `UUT_content/drafts/link-on-transitions-freedom-of-form-and-the-righteous-struggle-against-nature.md` is an outline reply.
- Summary:
  - **The essay.** Tracing Woodgrains (TW) calls Davis one of TW's "favorite authors on trans issues". TW uses him as the model of a stance that "does not flatter himself" and is therefore easy to believe. TW endorses transformation as a righteous struggle against Nature, undertaken honestly, including species transition via the Freedom of Form Foundation. TW warns that "threat-response narratives" replace truth-seeking. The essay notes that Davis's framing makes him "a tool for hostile interests" such as gender-critical campaigners. It judges his Emperor Norton ending "the most humane one", then adds "consider the possibility that it is not Emperor Norton who is wrong."
  - **Comments.**
    - HoopyFreud (11) objects that many trans people experience transition "as prosthesis" rather than transhuman liberation. HoopyFreud says TW's preference for Davis's account "makes me wanna fucking scream".
    - die_rattin, who once followed Davis's writing "slavishly during my repressor days", has since transitioned.
    - celluloid_dream praises the Emperor Norton passage.
- Quotes:
- (Tracing Woodgrains)
> Perhaps it reflects a failure of imagination on my part, but I find /u/M_T_Saotome-Westlake's thoughts much easier to absorb and understand than those of most trans or trans-adjacent people, because his theory of reality seems to cleave closest to my own understanding.
- (Tracing Woodgrains)
> Part of the trouble is that once one settles on a [counter-melody](https://sive.rs/counter) framing on something controversial like this, they become, in part, a tool for hostile interests to wield against those like them.
- (https://www.reddit.com/r/theschism/comments/si7k2c/on_transitions_freedom_of_form_and_the_righteous/hvkp0vv/, HoopyFreud, 11 points)
> The thing is, *as far as I can tell*, there are a lot of trans people who do *not* experience transition as transhuman liberation, but as prosthesis.

### 2021-01-01 · tailcalled, *Causality is essential: Reply to MTSW on Autogynephilia* (*surveyanon*, WordPress)
- Path: `reception_data/web/tailcalled-causality-is-essential/text.txt` · https://surveyanon.wordpress.com/2021/01/01/causality-is-essential-reply-to-mtsw-on-autogynephilia/
- Responds to: UUT *Reply to Ozymandias on Autogynephilia* (2016). Davis answered with UUT *You Are Right and I Was Wrong: Reply to Tailcalled on Causality* (2021-02).
- Summary: tailcalled, a sympathetic but independent sexology hobbyist, criticizes Davis's 2016 claim that "Summarizing correlations is the entire point of making a taxonomy". He calls Davis's move from correlations to "two and only two different psychological conditions with different etiologies" a "motte/bailey". Correlations may be unstable across time, context and pressure, so etiological claims require causal evidence. Ozy's model is a distinct causal graph, not merely an absence of theory. Ozy's framework also gives questioning people an answer, so the choice is not between BBL (Blanchard–Bailey–Lawrence) and nothing. Autogynephilia itself lacks construct validation. This is the critique to which Davis publicly conceded in the title of his reply.
- Quotes:
- (tailcalled)
> This response seems to engage in some motte/bailey’ing. It starts out arguing “summarizing correlations is the entire point of making a taxonomy”, but ends up at “maybe these are actually two and only two different psychological conditions with different etiologies”.
- (tailcalled)
> Ultimately lying is a thing, but Blanchardians have been ignoring the construct validation of autogynephilia for too long.

### 2023-02-07 · r/SneerClub on *The Categories Were Made for Man to Make Predictions*
- Path: `reception_data/web/reddit-sneerclub-categories-2023/text.txt` · https://www.reddit.com/r/SneerClub/comments/10w6r33/sequel_to_a_beloved_siskind_classic_from_a/ · 63 archived comments
- Summary: The submission title calls the essay "good ol' transphobia". It was prompted by a r/slatestarcodex comment (1a3orn, 23) recommending it as a sequel to Alexander.
  - **Main critique (endlessmoth, 26).** The essay uses "loaded language". It treats recognition of trans women's gender as an imposition while never questioning the category "cis women". Its "dust specks" argument could equally justify racism.
  - **Dismissals.** Otherwise-Anxiety-58 (35): "A lot of words to say very little". N0_B1g_De4l (36) on "the dumbest thought experiment in the world". noactuallyitspoptart (21) calls rationalist house style "insipid".
  - **Autogynephilia as a construct.** DigitalEskarina (32) says "AGP theory" is "at least 99% bunk". breckenridgeback distinguishes the sensation, which many trans people report, from Blanchard's causal typology.
  - **Personal.** NoahTheDuke (41) quotes Davis's account of his own psychosis mockingly. Subrosian_Smithy (21) calls the blog a "lonelier, intellectualized version" of 4chan threads where self-hating or closeted trans people gather. dgerard (23): "Nazi bar story but the barman welcomes the Nazi in, and is also a Nazi".
  - **Character of the thread.** Most participants say they did not finish the essay.
- Quotes:
- (https://www.reddit.com/r/SneerClub/comments/10w6r33/sequel_to_a_beloved_siskind_classic_from_a/j7lnzlb/, endlessmoth, 26 points)
> an analysis of trans women like this is going to look pretty biased if all of the questioning is poking at whether 'trans women' makes sense as a homogenous category without questioning whether 'cis women' makes sense as a category.
- (https://www.reddit.com/r/SneerClub/comments/10w6r33/sequel_to_a_beloved_siskind_classic_from_a/j7lxjq5/, breckenridgeback, 14 points)
> The other is Blanchard's claim that this is *what makes people trans*, and that trans people fall into specific distinct categories. Blanchard's categorization certainly does get at some very broad clusters; it just doesn't hold up as a causative explanation because those clusters are broad and exception-laden.

### 2023-07-19 · Ozy Brennan, *A Response to Zack Davis* (*Thing of Things*, Substack; paid)
- Path: `reception_data/web/ozy-response-to-zack-davis/text.txt` · https://thingofthings.substack.com/p/a-response-to-zack-davis
- Responds to: *Blanchard's Dangerous Idea and the Plight of the Lucid Crossdreamer* (LW, 2023-07-08). The post links it and says Ozy had not read the sequel.
- Summary: Only the free preview was read; the rest is paywalled. Ozy calls it "an emotional post, more than a logically argued one". Ozy accepts that context-dependent senses exist (medical "women"). The preview objects that Davis is "remarkably vague about what a woman is like". tailcalled quotes more of the piece in the LW *Blanchard's Dangerous Idea* thread (Part A); those passages are not independently verified here.
- Quotes:
- (Ozy Brennan)
> For someone so monomaniacally obsessed with how psychologically different he is from women, how he can never be a woman and never share a woman’s experiences and how every cell in his body and thought in his mind would have to be totally rewritten for him to approximate womanhood, Zack Davis is remarkably vague about what a woman is like.

### 2023-07-23 · tailcalled, *Autogynephilia discourse is so absurdly bad on all sides* (LessWrong)
- Path: `reception_data/web/tailcalled-agp-discourse/text.txt` · https://www.lesswrong.com/posts/mvQjpu7iFnqQ47Lbp/autogynephilia-discourse-is-so-absurdly-bad-on-all-sides (read via GreaterWrong, with 24 comments)
- Responds to: *Blanchard's Dangerous Idea* (2023-07-08), quoting its passage asking how dumb gender-identity proponents think the public is.
- Summary: tailcalled calls Davis's critique "not a completely unreasonable critique". It has "a lot less bite" given dysfunction on the Blanchardian side too. The example is Bailey and Hsu's study, which tailcalled says substituted "highly active members of online erotic AGP communities" for trans women. tailcalled says Blanchardians have left his blog critiques unaddressed. In comments he counts Davis's citations of Bailey (4) and Lawrence (7), and concedes he "didn't do much to justify" the claim about the other side's discourse.
- Quotes:
- (tailcalled)
> In some ways this is not a completely unreasonable critique, but I think it has a lot less bite once one realizes just how dysfunctional the discourse on this subject is, even among the ideology that Zack endorses as a replacement.

### 2023-10-26 · r/rational on *Fake Deeply*
- Path: `reception_data/web/reddit-rational-fake-deeply/text.txt` · https://www.reddit.com/r/rational/comments/17h5exh/rtchsf_fake_deeply/ · 5 archived comments
- Summary: grekhaus asks why the story makes the offense sexual harassment and adds "one line of transphobia", calling it "Needlessly crass". Davis answers that "the Muse spoke to me about the crass parts first". He says the details are "real", citing his Haskell-survey post. Veedrac: "Because author." The corpus links this Davis comment (LW *Fake Deeply* entry, Part A).
- Quotes:
- (https://www.reddit.com/r/rational/comments/17h5exh/rtchsf_fake_deeply/k70k5ky/, Davis, 1 point)
> I'm not proud of the crassness (I sat on the story for two weeks before deciding to pull the trigger on publishing it), but I don't think it can be removed without damaging the artistic integrity of the Muse's vision.

### 2025-05-29 · Duncan Sabien, *Truth or Dare* (*Homo Sabiens*, Substack)
- Path: `reception_data/web/sabien-truth-or-dare/text.txt` · https://homosabiens.substack.com/p/truth-or-dare
- Responds to: Davis's discourse-norms writing generally. Davis answered on LessWrong on 2026-01-27 (Part A).
- Summary: A long essay (about 20k words) on "dark world" versus "light world" priors: trust, safety, and how trauma makes cynicism adaptive. Act IV, Scene I ("Boy, putting Zack Davis's name in a header will probably have Effects, huh") applies it to Davis.
  - Davis "does not understand how high-trust, high-cooperation dynamics work". He keeps his footing among "liars and thieves" "with genuinely admirable skill and inexhaustible tenacity", but his tactics "utterly destroy" the possibility of something better.
  - Sabien says he uses Davis also as "a stand-in" for all such advisors.
  - One reader comment says "I don't know who Zack Davis is, but I think I get the gist from how you describe his interactions."
- Quotes:
- (Duncan Sabien)
> This is why you should not trust Zack Davis, when he tries to tell you what constitutes good conduct and productive discourse. Zack Davis does not understand how high-trust, high-cooperation dynamics work. He has never seen them.
- (Duncan Sabien)
> (Here I’m talking about the literal actual Zack Davis, but I’m also using him as a stand-in for all the dark world denizens whose well-meaning advice fails to take into account the possibility of light.)

### 2025-08-22 · Oliver Habryka, *Banning Said Achmiz (and broader thoughts on moderation)* (LessWrong) and its comments
- Path: `reception_data/web/habryka-banning-said/text.txt` · https://www.lesswrong.com/posts/98sCTsGJZ77WgQ6nE/banning-said-achmiz-and-broader-thoughts-on-moderation (read via GreaterWrong; 419 comments). The post and the Davis-related comment exchanges were read, not the full comment section.
- Responds to: this is the other party's account of the dispute in Davis's *Comment on "Banning Said Achmiz"* (2026-05-30). The post also engages Davis's earlier "contextualizing norms" post.
- Summary:
  - **The post.** Habryka quotes Davis's critique of the decoupling/contextualizing dichotomy as "helpful". He partly disagrees, then uses Davis's point that context is often relevant to justify expecting Achmiz to defend his subtext.
  - **July 2026 comments.**
    - Habryka rejects Davis's charge of "making false claims" about which authors had complained. He calls Davis's framing a "Motte and Bailey game" between "you are lying" and "you were wrong".
    - Richard Ngo (8, 11) judges that Habryka exaggerated when frustrated and read "false claims" too uncharitably. Ngo also says Davis's phrasing was "halfway" to a lying accusation, and that Davis showed a "(motivated) failure to understand" Habryka. On balance Ngo thinks Habryka is "doing a good job".
- Quotes:
- (habryka, post)
> But as Zack helpfully points out here, the key thing to understand is that of course many forms of context and implications are obviously relevant and important, and worth taking into account during a conversation.
- (habryka, comment, 2026-07-10, 4 points)
> I am not going to play this fun little Motte and Bailey game where in one sentence Zack says “you are lying, therefore no one should trust you” and in another sentence says “I believe you were wrong and I am just sharing evidence that you are wrong”.
- (Richard_Ngo, comment, 2026-07-10, 11 points)
> To be clear, I find it very understandable to be frustrated by all of these interactions, since both Said and (to a much lesser extent) Zack phrased statements in ways that I consider to be norm-violatingly aggressive.

### 2025-11-30 · themotte.org *Small-Scale Question Sunday* (recommendations thread)
- Path: `reception_data/web/themotte-org-388156/text.txt` · https://www.themotte.org/post/3394/smallscale-question-sunday-for-november-30/388156?context=8
- Summary: Answering a request for reading on trans issues, users recommend Davis. ThomasdelVasto calls the "Categories" essay a "devastating takedown" of Alexander. erwgv3g34: "plenty of other bangers". A dissenting user (rae) calls his writing "a desperate coping mechanism for a psychiatric condition/neurological problem that he’s unwilling to have properly treated".
- Quotes:
- (ThomasdelVasto)
> "The Categories Were Made for Man to Make Predictions" by Zack M. Davis, a devastating takedown of Scott Alexander's "The Categories Were Made for Man, Not Man for the Categories".

### 2026-01-13 (reviewed) · Andrea James, *Zack M. Davis / 'Mark Taylor Saotome-Westlake' and transgender people* (*Transgender Map*)
- Path: `reception_data/web/transgendermap-davis/text.txt` · https://www.transgendermap.com/people/zack-m-davis-mark-taylor-saotome-westlake/
- Summary: A reference page by the trans activist Andrea James, a long-time critic of Bailey and Blanchard. It classifies Davis as an autogynephilia activist (the term in scare quotes) within the so-called rationalist and evolutionary-psychology movements. It quotes his 2006 notebook passage on discovering the word and likens his "zeal" to Anne Lawrence's. It calls him "a thoughtful and prolific writer". It lists 13 posts and the Phil Illy interview without discussing their arguments.
- Quotes:
- (Andrea James)
> Davis is a thoughtful and prolific writer who began a personal blog in 2011 that continues through discovery of the diagnosis “autogynephilia.” In it, Davis documents extensive efforts to evangelize for adopting the term.

### 2017–2026 · Scattered Reddit mentions (PullPush comment search)
- Path: `reception_data/web/reddit-pullpush/comments.txt` · 346 archived comments linking unremediatedgender.space or zackmdavis.net, or naming "Saotome-Westlake"; 57 are Davis's own. All 289 others were skimmed (first 500 characters each), with longer reading where relevant.
- Summary:
  - **Where the citations come from.** Mostly r/slatestarcodex (71), r/TheMotte (60), r/askAGP (25), r/itsafetish (20), r/BlockedAndReported (18), r/GCdebatesQT (16), r/honesttransgender (13) and r/theschism (11).
  - **"Categories" as the counterpart to Alexander.** The most-cited piece is *The Categories Were Made for Man to Make Predictions*. It is recommended repeatedly as the counterpart or rebuttal to Alexander's 2014 essay: professorgerm (46, 2018), 1a3orn (23, 2023), bgaesop (24, 2025). One user notes "Scott once linked to" it in an SSC links post; that was not verified here.
  - **Other recommended posts.** *Don't Negotiate With Terrorist Memeplexes*, *Lesser-Known Demand Curves*, *Psychology Is About Invalidating People's Identities* (often deployed by tailcalled), *Self-Identity Is a Schelling Point*, the Murray review, and *Challenges to Yudkowsky's Pronoun Reform Proposal*.
  - **The blog's `/papers/` directory as a library.** Its hosted PDFs (Blanchard, Lawrence, Bailey & Hsu, Illy) are widely linked as a reference collection in AGP and trans forums, on both sides.
  - **Use against trans people.** Davis is cited approvingly in gender-critical and anti-trans forums, e.g., r/itsafetish users quoting him or noting he "stopped taking hormones". This is the dynamic Tracing Woodgrains describes.
  - **Hostile characterizations.** SneerClub and some trans users describe him in hostile personal terms ("self hating", "Theorizing oneself out of existence").
  - **Accuracy.** Some characterizations are inaccurate. A 2020 SneerClub comment misdescribes his views and pronouns, e.g., "she apparently believes each person is actually two people/'hemispheres'".
  - **Later SneerClub.** dgerard's remarks (2025): "and our old friend Zack Davis!" and "*everything* about Zack is trans issues". A 2026 submission titled "Another Zack M. Davis longpost has hit lesswrong" was removed.
- Quotes:
- (https://www.reddit.com/r/slatestarcodex/comments/8ebetz/culture_war_roundup_for_the_week_of_april_23_2018/dxtz5ta/, professorgerm, 46 points)
> A rebuttal of sorts to "The Categories Were Made for Man, Not Man for the Categories." I wouldn't agree with all of it, and if it's been shared here before I'll take the comment down, but I found it interesting and somewhat enlightening, from a different perspective.
- (https://www.reddit.com/r/SneerClub/comments/hpzts6/what_are_some_of_scotts_posts_that_challenge_the/fxy5iqf/, Subrosian_Smithy, 4 points)
> I always feel bad for Saotome-Westlake. Theorizing oneself out of existence in a puff of inference indeed.

## Part B (continued): comment threads on *The Scintillating But Ultimately Untrue Thought* (Isso)

UUT enabled Isso comments in April 2020 (*Don't Read the Comments*). A few older posts also carry threads. The public Isso API (`/isso/?uri=`, the same endpoint the comment widget uses) was queried for every published UUT post on 2026-10-15 by `tools/fetch_isso.py`. That produced 78 non-empty threads with 604 comments, rendered to `reception_data/isso_threads/` (raw JSON in `raw/`); email hashes and websites were dropped.
- **Most frequent commenters.** tailcalled (142), Davis himself (69), L (Zero) (51), KartoffelElf (39), BSRK Aditya (24), Emma (23) and Rat Analyst (21).
- **Privacy.** Many commenters disclose their own transition histories and sexual experiences under pseudonyms. These notes record such disclosures only in general terms and never quote them.
- **Coverage.** Threads with substantive discussion get entries below. Small threads (one to four comments, mostly thanks, links or corrections) are tallied at the end.

### 2021-05-02 · Isso: *Sexual Dimorphism in Yudkowsky's Sequences, in Relation to My Gender Problems*
- Path: `reception_data/isso_threads/2021_sexual-dimorphism-in-the-sequences-in-relation-to-my-gender-problems.md` · 50 comments (Davis 6) · http://unremediatedgender.space/2021/May/sexual-dimorphism-in-the-sequences-in-relation-to-my-gender-problems/
- Summary: The blog's most-commented thread.
  - **Trans readers urging transition.** Several trans readers share their own histories and urge Davis to transition. They say he underestimates current technology and the satisfaction of transition. One says the rationalist community is "an albatross" for self-acceptance. notaname arrived "from a SneerClub link" and argues "transition works". tailcalled replies that "All studies on transition are low-quality". hayley, Pentacles and Sophia write in a similar vein.
  - **The typical-mind objection.** Rat Analyst argues that Davis assumes other AGPs "to be more psychologically uniform and more like yourself than one ought". tailcalled names this "The Blanchardian Fallacy".
  - **Female readers.** cordelia skrewt (10) describes slash fandom as a possible female analogue of an erotic target location error. Lucia credits gender-critical writing with her desistance.
  - **Ben Hoffman's reading.** Hoffman (Davis's friend) interprets the fantasy as a wish to relate to women as similar minds. Davis prefers the "brain bug" (erotic target location error) account.
  - **Davis's statement of position.** To Vanessa, Davis says his disagreement is "cultural" rather than about rights. As a transhumanist he favors morphological freedom: "I'm not some kind of Nazi trying to take away people's hormone perscriptions". His objection is to "Orwellian mind games".
  - **On Alexander's essay.** When FeepingCreature recommends Alexander's "Categories" essay, Davis's outburst ("piece of bullshit hackjob sophistry", "motherfucker!") marks his frustration. L (Zero) and FeepingCreature defend the essay as a correct "first step".
  - **The 2022 tailcalled exchange.** tailcalled argues at length that etiology is "only marginally" relevant, that "naive essentialism" fails, and that Blanchardian "parsimony" priors mislead. He reports a new survey in which autogynephilia (r = 0.55) beat 16 other factors as a correlate of male gender issues. Davis answers that he is "doing it for me, for the sanctity of my map". He concedes a practical/impractical axis is useful, and says that if transition were "marketed as applied transhumanism", "I would be writing a very different blog."
- Quotes:
- (http://unremediatedgender.space/2021/May/sexual-dimorphism-in-the-sequences-in-relation-to-my-gender-problems/#isso-193, Davis, 7 likes)
> It's [a cultural disagreement rather than a rights/policy disagreement](http://zackmdavis.net/blog/2016/12/resisting-the-narrative/). (I probably need to write up my "I Don't Do Policy" post sooner rather than later, because this tends to confuse people.) As a transhumanist, I'm totally in favor of morphological freedom—people having the right to modify their body and social presentation however they want.
- (http://unremediatedgender.space/2021/May/sexual-dimorphism-in-the-sequences-in-relation-to-my-gender-problems/#isso-181, Rat Analyst, 3 likes)
> If I had to compress my criticism of this whole blog into one sentence, it would be that you assume other AGPs to be more psychologically uniform and <a href="https://www.lesswrong.com/tag/typical-mind-fallacy">more like yourself</a> than one ought.
- (http://unremediatedgender.space/2021/May/sexual-dimorphism-in-the-sequences-in-relation-to-my-gender-problems/#isso-420, Davis, 0 likes)
> I'm doing it for me, for the sanctity of my map. Because on my last analysis (and the one before that, and the one before that), the scintillating but ultimately untrue thought is not true. I'm better off knowing rather than not knowing.

### 2022-07-08 · Isso: *The Two-Type Taxonomy Is a Useful Approximation for a More Detailed Causal Model*
- Path: `reception_data/isso_threads/2022_the-two-type-taxonomy-is-a-useful-approximation-for-a-more-detailed-causal-model.md` · 30 comments (Davis 4) · http://unremediatedgender.space/2022/Jul/the-two-type-taxonomy-is-a-useful-approximation-for-a-more-detailed-causal-model/
- Summary: The thread is mostly a long technical exchange between tailcalled and Davis. It is the most detailed critique of the corpus's sexology from inside the Blanchard-sympathetic camp.
  - **tailcalled's opening critique.**
    - Blanchardianism is a "war theory" (about societal impact) dressed as a "physical theory" (about etiology).
    - The model needs effect sizes and residual factors.
    - Blanchardians use a double standard on causal direction: autogynephilia-like phenomena are treated as effects of gender issues in androphiles and women, but as causes in gynephilic males.
    - Erotic target location error (ETLE) is under-tested. tailcalled reports that Michael Bailey dismissed his gynephilia–AGP correlation data.
    - *Men Trapped in Men's Bodies* draws on a self-selected sample.
    - A "mediation" argument would serve the causal claim better.
  - **Davis's replies.**
    - He holds a "No Way No Chance prior" against AGP in women, from ETLE and introspection.
    - He calls Lawrence's compendium "picking cherries from a cherry tree".
    - He finds tailcalled's "propositional subject" analogy "spectacularly unpersuasive".
    - He offers an "atheoretical pattern-matcher" distinction between interpersonal autosexuality ("I feel like a sexy and desirable member of the gender that I am") and ETLE-type autosexuality.
    - He admits his introspective body-preference ordering may be "a cognitive illusion".
    - He concedes that "Blanchardians" are "Dumb and Bad if it helps us focus on what arguments are true".
    - He edits the sexual-dimorphism post in response to tailcalled's point about cruder fantasies.
  - **Other commenters.** sparklesdire asks how the model explains post-transition convergence of formerly AGP trans women's experience, and tailcalled agrees the evidence there is weak. KartoffelElf raises the rarity of autoapotemnophilia. One spam comment.
- Quotes:
- (http://unremediatedgender.space/2022/Jul/the-two-type-taxonomy-is-a-useful-approximation-for-a-more-detailed-causal-model/#isso-388, tailcalled, 1 like)
> Blanchardians basically universally claim that their theories are theories of the etiology of transsexuality. But they also basically universally focus on the latter kinds of questions.
- (http://unremediatedgender.space/2022/Jul/the-two-type-taxonomy-is-a-useful-approximation-for-a-more-detailed-causal-model/#isso-399, Davis, 0 likes)
> I mean, yes, but as you know, we also see reports of the same phenomena over and over and over again in communities where the typology is reviled. I point to Men Trapped in Men's Bodies because it's a nice compendium, but it's not cherry-picking rare outliers; I think it's picking cherries from a cherry tree.
- (http://unremediatedgender.space/2022/Jul/the-two-type-taxonomy-is-a-useful-approximation-for-a-more-detailed-causal-model/#isso-406, Davis, 0 likes)
> I'm happy to concede that "Blanchardians" are Dumb and Bad if it helps us focus on what arguments are true, ignoring the irrelevancy of which faction would use them.

### 2021-01-10 · Isso: *Link: Unnatural Categories Are Optimized for Deception*
- Path: `reception_data/isso_threads/2021_link-unnatural-categories-are-optimized-for-deception.md` · 46 comments (Davis 2) · http://unremediatedgender.space/2021/Jan/link-unnatural-categories-are-optimized-for-deception/
- Summary: A commenter-to-commenter debate that Davis mostly watches.
  - **Emma's objection.** Emma, a trans woman and appreciative reader, disputes the asymmetry Davis draws between a descriptive side and a trade-off side. Both camps redefine words, she argues, and trans activists are *more* aware that the choice is arbitrary.
  - **Gender-critical-leaning replies.** Vee and L (Zero) describe progressive spaces where women can no longer call periods "lady problems", and argue that any consensus has to be "backstopped" by enforcement. Dan T. and Toulouse press the gender-critical case more combatively. Emma repeatedly asks for specifics, thanks them, and says the exchange changed her view on spaces where trans women outnumber natal women.
  - **Davis's reply.** He thanks "Emma, with whom I think I have some substantive and potentially fruitful disagreements". He sketches future posts: on the asymmetry in "death-and-rape threat/intimidation" (attributed to "an innate male propensity towards violence"); on sex as a set of discrete "clusters" rather than a spectrum; and against the 2020 ban of r/GenderCritical. He recalls crying on Christmas 2016 after being called a predator there, yet says his "tears don't make it right to kick them off Reddit".
- Quotes:
- (http://unremediatedgender.space/2021/Jan/link-unnatural-categories-are-optimized-for-deception/#isso-97, Emma, 1 like)
> The intent of my original comment was to cast doubt on whether that asymmetry really exists, as my perception is more that both sides are making their own trade-offs in choosing some aspects of reality to emphasise over others
- (http://unremediatedgender.space/2021/Jan/link-unnatural-categories-are-optimized-for-deception/#isso-119, Davis, 3 likes)
> I spent a lot of Christmas Day 2016 crying because someone on /r/gendercritical called me a predator, but as a grown-up, I have to bear some amount of responsibility for my own emotional state; my tears don't make it right to kick them off Reddit

### 2021-03-09 · Isso: *Point Man*
- Path: `reception_data/isso_threads/2021_point-man.md` · 44 comments (Davis 5) · http://unremediatedgender.space/2021/Mar/point-man/
- Summary: Comments on the post's deer/horse (指鹿为马) loyalty-signal reading of preferred pronouns.
  - **Pronouns.** Rat Analyst (4) argues that with polarized common knowledge, pronoun choice is unavoidably a signal. Thomas Ambrose and Emma debate singular "they" against neopronouns.
  - **Emma's objection.** Emma objects to the phrase "perverted men" and to the post's cynicism and one-sidedness. Davis edits it to "paraphilic", while noting he is not "optimizing my writing for accessibility".
  - **Davis's apologia.** His long reply explains the blog's focus: "a defensive war against a specific gender-identity ideology" that "shot first". He cites his self-ID Schelling-point post as a credible signal of not being "a partisan hack". He tells his mid-2000s self-conception story, and asks why he never gets "any empathy for how creepy this is?!" He concedes that most AGP discourse paints trans people as predators, but says "I'm just not very focused on that part."
  - **Close of the exchange.** Emma and Rat Analyst exchange mutual thanks. Emma credits *Self-Identity Is a Schelling Point* with clarifying her own view. Davis says their long comments talk past each other.
  - **Race.** A side-thread on race analogies has Davis defending SNP-cluster findings while distinguishing them from "the much more tendentious claims of actual racists".
  - **Unusual contributions.** BSRK Aditya offers meditation exercises on recognizing categories.
- Quotes:
- (http://unremediatedgender.space/2021/Mar/point-man/#isso-159, Davis, 2 likes)
> And from my perspective, it looks like I'm fighting a defensive war against a specific gender-identity ideology that unambiguously "shot first", not an offensive war against transsexuals' right to exist.
- (http://unremediatedgender.space/2021/Mar/point-man/#isso-164, Emma, 2 likes)
> I do really appreciate Taylor making an effort to advance possible arguments for the "other side" even when he doesn't agree with them, and that "Self-Identity as a Schelling Point" in particular helped to clarify to me a lot of what I find valuable about the current norms

### 2022-04-24 · Isso: *Backlog Metablogging, April 2022*
- Path: `reception_data/isso_threads/2022_backlog-metablogging-april-2022.md` · 31 comments (Davis 4) · http://unremediatedgender.space/2022/Apr/backlog-metablogging-april-2022/
- Summary:
  - **Lux.** Lux suggests "This thing eats your life whether you deal with it or don't, something this very blog is evidence of". Davis answers that it only "started eating my life in 2016 when I found out that everyone else is prevaricating".
  - **Concessions to tailcalled.** Davis concedes he "may have overreached" in demanding an etiological model before judging whether transition works. He reframes the demand as wanting "a fair comparison" between "Transition Works" and "Repression Works".
  - **Studies.** tailcalled and KartoffelElf argue over whether a Cornell literature roundup establishes trans well-being outcomes. tailcalled: "Never trust a study that you haven't read."
  - **ilzolende's criticism.** ilzolende (5), an AFAB person who tried nonbinary identity and desisted, criticizes Davis's positive mention of *Irreversible Damage* and allying with "horrible people". Davis concedes "That's fair", calling it "an unreflective instinct to accept whatever allies I can get in my war against the Egregore".
  - **Organization.** Davis explains why he declined tailcalled's proposal to found an organization.
- Quotes:
- (http://unremediatedgender.space/2022/Apr/backlog-metablogging-april-2022/#isso-337, ilzolende, 5 likes)
> Allying with horrible people who happen to see the same thing you want as a useful stepping stone to their horrible goals and speaking more positively of them than you'd naïvely tend towards seems kind of like a disease of politics which, if you're not even writing an influential blog, you should refrain from participating in.
- (http://unremediatedgender.space/2022/Apr/backlog-metablogging-april-2022/#isso-335, Davis, 0 likes)
> That's fair. (I felt an unreflective instinct to accept whatever allies I can get in my war against the Egregore, that wouldn't, and shouldn't, be shared by people who had worse parents than me.)

### 2017-01 · Isso (2022 comments): *The Counter*
- Path: `reception_data/isso_threads/2017_the-counter.md` · 9 comments (Davis 1) · http://unremediatedgender.space/2017/Jan/the-counter/
- Summary: Andi and NoriMori, two readers, describe fear of losing social groups over "gender orthodoxy". Davis calls the rationalist sphere's silence about harms to lesbian communities "discrediting", on epistemic rather than moral grounds. He reports some friendships surviving only "in weakened form", and says "I really need to leave the Bay Area." tailcalled questions Davis's "endgame". He contrasts Davis's stated victory condition (the two-type taxonomy in sex-ed textbooks) with leading by example in correct reasoning.
- Quotes:
- (http://unremediatedgender.space/2017/Jan/the-counter/#isso-299, tailcalled, 0 likes)
> The thing that sort of frustrates me about MTSW is, what is the point? Like what is the endgame?

### 2023-12-18 · Isso: *Reply to Scott Alexander on Autogenderphilia*
- Path: `reception_data/isso_threads/2023_reply-to-scott-alexander-on-autogenderphilia.md` · 13 comments (Davis 1) · http://unremediatedgender.space/2023/Dec/reply-to-scott-alexander-on-autogenderphilia/
- Summary: tailcalled criticizes the post's "parsimonious" taxonomy from psychometrics. KartoffelElf shows that the post's claim about "do I want to be her, or do I want to be with her" is "trivially falsifiable" by web search; the post had claimed the phrase is rarely said by cis women. Davis concedes "it was pretty dumb of me" not to search. Having looked, he argues the cis-lesbian uses mostly mean something different ("a same-sex role model"), while allowing that a small fraction of cis lesbians may be autosexual.
- Quotes:
- (http://unremediatedgender.space/2023/Dec/reply-to-scott-alexander-on-autogenderphilia/#isso-558, Davis, 1 like)
> Thanks for the search suggestion! I agree that it was pretty dumb of me to write "I'm inclined to doubt it" based on my anecdotal personal experience without doing a very cheap web search

### 2022-02-21 · Isso: *Link: Never Smile at an Autogynephile*
- Path: `reception_data/isso_threads/2022_link-never-smile-at-an-autogynephile.md` · 13 comments (Davis 2) · http://unremediatedgender.space/2022/Feb/link-never-smile-at-an-autogynephile/
- Summary:
  - **Davis and tailcalled on the song.** tailcalled argues that the gender-critical song's disgust targets rare Ed Gein–type behavior, and that GC writers use "autogynephile" as a loose outgroup slur. Davis concedes he was "too-charitable" in reading the line metaphorically. He stands by "If AGP didn't exist, GC feminism wouldn't exist". He defends free speech because people are "selectfully truthful", and thanks tailcalled for persistent criticism ("Even the greatest minds get lazy and crazy without persistent critics").
  - **Terms and targets.** L (Zero) and tailcalled argue over whether "bad autogynephiles" or "bad trans women" is the fair term.
  - **jkgalbrain.** jkgalbrain says this kind of attack hits "noncombatants", and encourages Davis to separate "evident low self-esteem" from his arguments.
- Quotes:
- (http://unremediatedgender.space/2022/Feb/link-never-smile-at-an-autogynephile/#isso-279, Davis, 0 likes)
> The strength of freedom of speech as a principle is that if you want Society to have as much of the picture as possible, you have to let everyone speak, even if the vast majority of speakers are partisan cherry-pickers rather than honest whole-picture-accuracy-optimizers.

### 2022-06-12 · Isso: *Comment on a Scene from* Planecrash*: "Crisis of Faith"* (includes a comment by Eliezer Yudkowsky)
- Path: `reception_data/isso_threads/2022_comment-on-a-scene-from-planecrash-crisis-of-faith.md` · 21 comments (Davis 2; Yudkowsky 1) · http://unremediatedgender.space/2022/Jun/comment-on-a-scene-from-planecrash-crisis-of-faith/
- Summary:
  - **Early comments.** Iceman calls dath ilan "a fantasy setting" whose rationality is an "informed ability". tailcalled jokes that dath ilan is "a world where Eliezer Yudkowsky was the average person". L (Zero) is "jaw-dropping"ly unimpressed by Keltham's reaction to a woman.
  - **Individualism versus universalism.** unfriendly teapot argues that an advanced rational civilization might well spend effort reducing sex differences. Davis replies by distinguishing individualism from "a universalist æsthetic that actually wants to destroy the covariances propping up the big categories". On the setting's equal protection for tieflings, Davis calls the authors "unaware of their religion as a religion" ("This is a heresy blog, not an apostate blog"). NoriMori says he misreads the setting, then retracts as "poorly stated".
  - **Yudkowsky's comment (September 2024).** Eliezer Yudkowsky comments in Keltham's voice that prediction markets would capture any information biological sex adds beyond height. He asks what is gained by "a law that asymmetrically treats different sapient beings". Davis's UUT 2024 post replies to this comment; tailcalled disputes it on efficiency grounds.
- Quotes:
- (http://unremediatedgender.space/2022/Jun/comment-on-a-scene-from-planecrash-crisis-of-faith/#isso-583, Eliezer Yudkowsky, 0 likes)
> And after you've added in prediction markets to actually get all of the information that anybody has, what remains to be gained by creating a law that asymmetrically treats different sapient beings in a way based not on predicted outcomes?
- (http://unremediatedgender.space/2022/Jun/comment-on-a-scene-from-planecrash-crisis-of-faith/#isso-363, Davis, 2 likes)
> Should we perhaps distinguish between individualism (that's wary of mis-predicting individuals on any grounds, not just a few protected categories), and a universalist æsthetic that actually wants to destroy the covariances propping up the big categories?

### 2023-04-22 · Isso: *Book Review:* Johnny the Walrus
- Path: `reception_data/isso_threads/2023_book-review-johnny-the-walrus.md` · 16 comments (Davis 1) · http://unremediatedgender.space/2023/Apr/book-review-johnny-the-walrus/
- Summary: tailcalled posts ChatGPT-generated versions of the walrus allegory. KartoffelElf says words like "ideological fad" are "dangerously close to policy opinions" despite *I Don't Do Policy*. Davis clarifies that he declines to endorse "a specific collectively-enforced policy" but does not avoid "assessments that correlate with policy opinions", and that he is "trying not to be a partisan hack". A tailcalled–KartoffelElf exchange follows on whether any information source is free of "propagandistic lies".
- Quotes:
- (http://unremediatedgender.space/2023/Apr/book-review-johnny-the-walrus/#isso-488, Davis, 1 like)
> I'm trying not to be a partisan hack with delusions of imposing my or my coalition's will on the populace, but that doesn't mean I don't have my own perspective.

### 2022-05-22 · Isso: *Gaydar Jamming*
- Path: `reception_data/isso_threads/2022_gaydar-jamming.md` · 15 comments (Davis 4) · http://unremediatedgender.space/2022/May/gaydar-jamming/
- Summary:
  - **Testing the hypotheses.** Thelo asks whether Davis can verify the post's hypotheses about school acquaintances. Davis: "Seems like it would be awkward." Ninety-Three: "You run this blog and you're afraid of a little awkwardness?" tailcalled jokes about two kinds of Blanchardians.
  - **Masculinity–femininity measurement.** tailcalled and Davis argue over whether intuitive masculinity/femininity aligns with the sex-separating axis. Davis is "inclined to bite the bullet on horny women being masculine"; tailcalled calls that nonstandard usage.
  - **BSRK Aditya.** BSRK Aditya finds Davis's quantitative approach to stereotypes "much more palatable" than a friend's sexism.
- Quotes:
- (http://unremediatedgender.space/2022/May/gaydar-jamming/#isso-348, tailcalled, 3 likes)
> There are two types of Blanchardians, those who are so afraid of awkwardness that they don't get their hypotheses tested, and those who are so unafraid of awkwardness that they act strange and end up creeping out anyone who could challenge them.

### 2020-04-28 · Isso: *Book Review: Charles Murray's* Human Diversity
- Path: `reception_data/isso_threads/2020_book-review-human-diversity.md` · 13 comments (Davis 1) · http://unremediatedgender.space/2020/Apr/book-review-human-diversity/
- Summary: Mostly strong praise.
  - **Praise.** K Smith: "The post is a fucking Triumph"; uhoh agrees. Emma (5) writes that despite "mixed feelings about your blog generally" the post clarified for her the distinction between progressive goals and methods.
  - **Other comments.** sbkyvfx notes Davis has "gone further than even Moldbug was willing to go". tailcalled adds psychometric notes and later applies the Schelling-point argument to immigration.
  - **One dismissal.** minette: "you are willfully ignorant of any sociological knowledge because of ideological reasons". Davis asks for textbook recommendations.
- Quotes:
- (http://unremediatedgender.space/2020/Apr/book-review-human-diversity/#isso-20, Emma, 5 likes)
> I have mixed feelings about your blog generally, but I really appreciate this post. It's helped to illuminate a lot of things I've been feeling for a while as someone very passionate about the broader goals and principles behind the current progressive movement who also often has trouble reconciling myself with a lot of their specific methodology

### 2022-06-24 · Isso: *An Egoist Faith*
- Path: `reception_data/isso_threads/2022_an-egoist-faith.md` · 17 comments (Davis 2) · http://unremediatedgender.space/2022/Jun/an-egoist-faith/
- Summary:
  - **Warning.** unfriendly teapot reads the post as a "Justification for your little crusade" and warns that "it's easy to get lost in genuine passion".
  - **tailcalled's sense of betrayal.** tailcalled shares a parallel sense of betrayal by Blanchardians ("they don't care about truth").
  - **The coherence of Blanchardianism.** Lux calls Blanchardianism "incoherent and absurd" now that young transition is common. Davis answers that if you think so, "you don't really understand what your opponents believe". Lux then offers a counterexample: a formerly "gold star" gay man who transitioned and developed AGP-like interests. Davis: "That's really interesting!! I don't know what's going on there." tailcalled and unfriendly teapot offer model patches. Lux likens these to epicycles.
- Quotes:
- (http://unremediatedgender.space/2022/Jun/an-egoist-faith/#isso-372, Davis, 1 like)
> Whether or not you agree with that view, if you think it's incoherent and absurd, then you don't really understand what your opponents believe.

### 2022-03-13 · Isso: *Challenges to Yudkowsky's Pronoun Reform Proposal*
- Path: `reception_data/isso_threads/2022_challenges-to-yudkowskys-pronoun-reform-proposal.md` · 20 comments (Davis 6) · http://unremediatedgender.space/2022/Mar/challenges-to-yudkowskys-pronoun-reform-proposal/
- Summary:
  - **The courtroom scenario.** Lux says Davis left the "loaded or unfair" objections to his courtroom-misgendering scenario unaddressed, and that they are "decisive". Davis concedes "Touché". He frames the scenario as a real conflict of interests in which "I care more about making my strongest argument than I do about avoiding giving offense". Jasnah Kholin, who otherwise moved toward Davis's pronoun position, found the scenario triggered her "defense-against-manipulation" response.
  - **Yudkowsky's honesty.** bleep thinks Yudkowsky was consciously lying. Davis believes Yudkowsky about his "fixation" on not lying. He argues that Yudkowsky's notion of honesty "is almost completely useless" against deception-without-lying.
  - **Other.** A side exchange on how many gender "clusters" exist: Davis says four. Davis also accepts a French grammar correction and edits.
- Quotes:
- (http://unremediatedgender.space/2022/Mar/challenges-to-yudkowskys-pronoun-reform-proposal/#isso-292, Davis, 1 like)
> But this is just another example of a real conflict of interests; I care more about making my strongest argument than I do about avoiding giving offense from use of tropes that are often invoked by others from a place of hate.
- (http://unremediatedgender.space/2022/Mar/challenges-to-yudkowskys-pronoun-reform-proposal/#isso-441, Jasnah Kholin, 1 like)
> so, i do find your writing about pronounces interesting and illuminating, and i did change my mind to far more sympathy to the use-sex-pronouns-not-gender-pronouns position. but when you ask "Not a sympathetic character? Not even a little bit?" my answer is - no.

### 2021-05-23 · Isso: *Amulet*
- Path: `reception_data/isso_threads/2021_amulet.md` · 17 comments (Davis 2) · http://unremediatedgender.space/2021/May/amulet/
- Summary:
  - **"TERF-sympathetic".** Rat Analyst questions how Davis can call himself "TERF-sympathetic" while rejecting socialization accounts of sex differences (asking whether to call it "gratuitous self-id"). Davis explains he means common ground on "a non-obfuscated public concept of sex". L (Zero), self-described as one of the blog's actual "terfs", agrees in part, but finds the material confirms "deep pessimism about what many men believe".
  - **Davis on innateness.** Davis answers at length that many male traits radical feminists dislike are partly "innate", citing Goldberg, congenital adrenal hyperplasia, and cloacal exstrophy cases.
  - **Labels.** tailcalled and Lux note the trans community's existing "repressor" label for people like Davis.
  - **Hostile.** lel calls his social scene "a hugbox" of "grandiosity junkies".
- Quotes:
- (http://unremediatedgender.space/2021/May/amulet/#isso-200, Davis, 3 likes)
> The thing I'm trying to point to is that caring about [having a non-obfuscated public concept of sex](/2018/Apr/reply-to-the-unit-of-caring-on-adult-human-females/) seems to create a lot of common ground, such that reaching out to GCs for conversation or a podcast-guest opportunity seems less hopeless than reaching out to mainstream trans-rights people?

### 2017-03 · Isso (2020–2024 comments): *Fresh Princess*
- Path: `reception_data/isso_threads/2017_fresh-princess.md` · 7 comments (Davis 0) · http://unremediatedgender.space/2017/Mar/fresh-princess/
- Summary: An anonymous self-described androphilic ("HSTS") trans woman writes a hostile comment. She resents AGPs like Davis for dominating trans discourse, and calls him "An AGP without makeup". Other anonymous commenters dispute her account of Blanchard's typology and of IQ data, and one asks "Why pick on one of the honest ones, though?" A 2024 commenter offers an "HSTS" self-description that moves the distinction away from sexual orientation alone.
- Quotes:
- (http://unremediatedgender.space/2017/Mar/fresh-princess/#isso-26, randomerican, 3 likes)
> Why pick on one of the honest ones, though?

### 2023-12-30 · Isso: *If Clarity Seems Like Death to Them*
- Path: `reception_data/isso_threads/2023_if-clarity-seems-like-death-to-them.md` · 5 comments (Davis 0) · http://unremediatedgender.space/2023/Dec/if-clarity-seems-like-death-to-them/
- Summary: tailcalled engages the map/borders passage. KartoffelElf reads the UK survey statistic as terminological confusion. KartoffelElf also sympathizes with Yudkowsky being "stuck between a rock and a hard place". FoxLisk points out a tension: Davis says not being at war made clarity-writing easier, while praising a commenter's line that commenters should not consider each other's feelings.
- Quotes:
- (http://unremediatedgender.space/2023/Dec/if-clarity-seems-like-death-to-them/#isso-565, FoxLisk, 0 likes)
> Note that this is in direct tension with the discussion about how commenters shouldn't have to worry about each others' feelings, etc

### 2023-07-08 · Isso: *Blanchard's Dangerous Idea and the Plight of the Lucid Crossdreamer*
- Path: `reception_data/isso_threads/2023_blanchards-dangerous-idea-and-the-plight-of-the-lucid-crossdreamer.md` · 6 comments (Davis 0) · http://unremediatedgender.space/2023/Jul/blanchards-dangerous-idea-and-the-plight-of-the-lucid-crossdreamer/
- Summary:
  - **Gratitude.** Two readers, Kerry and Dipanjan, credit the typology, and in Kerry's case Davis's influence (via a 2016 SSC links post), with helping them decide against transition "to great personal benefit". Dipanjan says it "saved my life twenty years ago". These are first-person reports of the corpus's influence and are recorded as such.
  - **FeepingCreature.** He apologizes for having recommended Alexander's "Categories". He describes his own AGP as "erotic autocomplete" rather than ETLE, and says he fits neither a one-type nor a "two types" model.
  - **Hostile (2026).** Ffff calls the post "nonsensical" and says trans women "are all provably better off for transitioning".
- Quotes:
- (http://unremediatedgender.space/2023/Jul/blanchards-dangerous-idea-and-the-plight-of-the-lucid-crossdreamer/#isso-523, FeepingCreature, 1 like)
> It just seems it would be silly if we took the "one type of trans" model that I very starkly don't fit, and replaced it with a "two types of trans" model that I ... still don't particularly fit.

### 2021-09-26 · Isso: *There Should Be a* Closetspace*/*Lease Bound *Crossover Fic*
- Path: `reception_data/isso_threads/2021_there-should-be-a-closetspace-lease-bound-crossover-fic.md` · 8 comments (Davis 0) · http://unremediatedgender.space/2021/Sep/there-should-be-a-closetspace-lease-bound-crossover-fic/
- Summary: Both comic authors respond to the post.
  - **Rusty Hearts** (*Lease Bound*) thanks Davis for a "balanced" breakdown but dislikes the crossover idea as a "foot in the door" tactic.
  - **Jenn Dolari** (*Closetspace*) thanks him for reading and explains the comic's delays.
  - **Az**, a butch lesbian commenter, argues that *Lease Bound* depicts an imaginary, purified lesbian subculture. L (Zero) and Darth von Neujersey reply.
- Quotes:
- (http://unremediatedgender.space/2021/Sep/there-should-be-a-closetspace-lease-bound-crossover-fic/#isso-248, Rusty Hearts, 3 likes)
> Thoroughly enjoyed reading this - thank you for taking the time to write it!

### 2023-06-21 · Isso: *Book Endorsement:* Autoheterosexual
- Path: `reception_data/isso_threads/2023_book-endorsement-autoheterosexual.md` · 9 comments (Davis 1) · http://unremediatedgender.space/2023/Jun/book-endorsement-autoheterosexual/
- Summary: tailcalled links his negative review of Phil Illy's book and presses Davis for a "high-level plan". Davis answers that people who disagree should criticize the book. He says the book "gets so much right" while readers should not believe it "slavishly". He contests tailcalled's "pseudo vs. true AGP" distinction. tailcalled replies that people should instead "attack Blanchardians' character", since content critiques are ignored. notthateither says this reads like a parody of "genderists".
- Quotes:
- (http://unremediatedgender.space/2023/Jun/book-endorsement-autoheterosexual/#isso-513, Davis, 0 likes)
> I think it can simultaneously be the case that "This book gets so much right, that I'm really glad it exists; I'm not aware of another book in this niche" and also that "This book gets some things wrong; readers should think critically instead of slavishly believing every word the author says."

### 2019-12-20 · Isso (2020–2023 comments): *Reply to Ozymandias on Fully Consensual Gender*
- Path: `reception_data/isso_threads/2019_reply-to-ozymandias-on-fully-consensual-gender.md` · 7 comments (Davis 0) · http://unremediatedgender.space/2019/Dec/reply-to-ozymandias-on-fully-consensual-gender/
- Summary: Minor comments: on paper-money history, and on how sex-based pattern recognition underlies Ozy's examples (Lucia). tailcalled argues that calling trans women "men" confuses discussion of autogynephilia, since most autogynephilic males are cis men. Happ and tailcalled discuss disclosure in dating.
- Quotes:
- (http://unremediatedgender.space/2019/Dec/reply-to-ozymandias-on-fully-consensual-gender/#isso-340, tailcalled, 1 like)
> In my experience it really trips up discussion of autogynephilia that anti-trans people insist on referring to trans women as men.

### 2020-11-28 · Isso: *The Feeling Is Mutual*
- Path: `reception_data/isso_threads/2020_the-feeling-is-mutual.md` · 5 comments (Davis 0) · http://unremediatedgender.space/2020/Nov/the-feeling-is-mutual/
- Summary: The post's epigraph is a SneerClub reader's remark about Davis.
  - **Emma (4).** Emma finds Davis's attempt to break the symmetry between himself and his opponents weak. She says he is "often kind of bad at clearly stating what your position actually is", and that this makes it unsurprising he is read as hating trans people. She calls SneerClub readers' inferences "Bayesian priors" applied "in their own mostly rational way".
  - **Jasnah Kholin.** Jasnah Kholin disagrees. She says she never found the blog antagonistic "BECAUSE of the tone, and the arguments, and the earnest trying to understand the true". She calls the quoted passage "uncharacteristically bad by this blog standards".
- Quotes:
- (http://unremediatedgender.space/2020/Nov/the-feeling-is-mutual/#isso-80, Emma, 4 likes)
> I also think that you're often kind of bad at clearly stating what your position actually is on a lot of these questions, to the point that it's not all that surprising that you're sometimes misunderstood as just hating trans people?
- (http://unremediatedgender.space/2020/Nov/the-feeling-is-mutual/#isso-438, Jasnah Kholin, 0 likes)
> i never felt this blog to be one of them. why? BECAUSE of the tone, and the arguments, and the earnest trying to understand the true.

### 2022-12-08 · Isso: *Context Is for Queens*
- Path: `reception_data/isso_threads/2022_context-is-for-queens.md` · 6 comments (Davis 0) · http://unremediatedgender.space/2022/Dec/context-is-for-queens/
- Summary: L (Zero) agrees that current trans terminology makes fantastical transformation stories hard to describe. tailcalled finds Wikipedia and GPT-3 definitions of "trans woman" obscure natal anatomy. KartoffelElf thinks the unsayability is overstated ("Ranma turns into a girl" draws no objection). Thelo asks what story Davis would have wanted instead.
- Quotes:
- (http://unremediatedgender.space/2022/Dec/context-is-for-queens/#isso-474, KartoffelElf, 0 likes)
> With all due respect, I think you're overstating the unsayability.

### 2022-09 · Isso: *The Signaling Hazard Objection*
- Path: `reception_data/isso_threads/2022_the-signaling-hazard-objection.md` · 12 comments (Davis 0) · http://unremediatedgender.space/2022/Sep/the-signaling-hazard-objection/
- Summary: Discussion of the post's source (the blogger Jim) and of male homosocial bonding. tailcalled suggests signaling hazards vary with a culture's gender conservatism. Lux reads Jim as a "closet case". Tofu and Ninety-Three ask about the asymmetry with female homosexuality. Davis does not comment.
- Quotes:
- (http://unremediatedgender.space/2022/Sep/the-signaling-hazard-objection/#isso-429, tailcalled, 0 likes)
> One thing I've been thinking recently as I've started properly studying gender conservativism as part of my research is, people's different levels of gender conservativism probably has massive effects on their experiences with this stuff?

### 2020-08 · Isso: *Yarvin on* Less Wrong
- Path: `reception_data/isso_threads/2020_yarvin-on-less-wrong.md` · 10 comments (Davis 1) · http://unremediatedgender.space/2020/Aug/yarvin-on-less-wrong/
- Summary: An anonymous commenter says Yarvin is "obviously wrong" because Yudkowsky's priority is AI safety, not culture war; another ("Based") defends Yarvin's point. L (Zero) objects to the excerpt's claim about "distortions in the status quo" and to the "lack of criticism in the comments". Davis replies that "listened with interest" doesn't imply agreement. He asks whether, if there were more distortions, "would you be able to tell?" tailcalled argues against inherited-environment explanations of racial disparities. L (Zero) disputes this.
- Quotes:
- (http://unremediatedgender.space/2020/Aug/yarvin-on-less-wrong/#isso-37, Davis, 3 likes)
> You could be right! (I trust that my readers understand that "listened with interest" doesn't imply agreement.) As a thought experiment, however, it might be worth asking: if there were more, would you be able to tell?

### 2023-06 · Isso: *Janet Mock on Late Transitioners*
- Path: `reception_data/isso_threads/2023_janet-mock-on-late-transitioners.md` · 11 comments (Davis 2) · http://unremediatedgender.space/2023/Jun/janet-mock-on-late-transitioners/
- Summary: tailcalled and KartoffelElf question what in Mock's passage is diagnostic. Davis answers that it is the conjunction of the observations. He grants that Blanchard, Bailey and Lawrence may be "overconfident, overgeneralizing", but holds that frequent on-type observations make the typology "pragmatically useful". tailcalled charges that many Blanchardians care about politics and "launder their views as sounding neutral/objective/authoritative". Asked why he singles them out, he answers "I'm angry at Blanchardians for wasting my time".
- Quotes:
- (http://unremediatedgender.space/2023/Jun/janet-mock-on-late-transitioners/#isso-501, Davis, 0 likes)
> (Even if BBL are overconfident, overgeneralizing, refusing to understand the selection bias in their study-recruiting methods, &c., the sheer frequency with which you see observations that are on type, makes the typology pragmatically useful.)

### 2018-02-23 · Isso (2021–2025 comments): *The Categories Were Made for Man to Make Predictions*
- Path: `reception_data/isso_threads/2018_the-categories-were-made-for-man-to-make-predictions.md` · 8 comments (Davis 0) · http://unremediatedgender.space/2018/Feb/the-categories-were-made-for-man-to-make-predictions/
- Summary: Darth von Neujersey points to 2021 Thai and European data as support for Lawrence's collectivism hypothesis about cross-cultural ratios of androphilic to non-androphilic trans women. tailcalled replies that such correlations do not discriminate between causal directions ("Blanchardians have a habit of interpreting any correlation with the types as supportive"), and Darth von Neujersey concedes. Candide III proposes a third, "nerdy" type; aceshigh says those are ordinary AGPs.
- Quotes:
- (http://unremediatedgender.space/2018/Feb/the-categories-were-made-for-man-to-make-predictions/#isso-303, tailcalled, 0 likes)
> Blanchardians have a habit of interpreting any correlation with the types as supportive of the typology. But of course it's only supportive of the typology if the correlation is better derived from the typology than without it.

### 2023-07 · Isso: *A Hill of Validity in Defense of Meaning*
- Path: `reception_data/isso_threads/2023_a-hill-of-validity-in-defense-of-meaning.md` · 9 comments (Davis 2) · http://unremediatedgender.space/2023/Jul/a-hill-of-validity-in-defense-of-meaning/
- Summary: FeepingCreature finds the memoir "painfully relatable". He offers the "strongest argument" against it: "you're treating rationality as a safety blanket, not a tool". On this view rationality cannot license demands on how others act, though he agrees with Davis's appraisal by the "adherence to principles" standard. NotThatEither reads Alexander's *Categories* essay as knowing play-along rather than belief. Davis agrees in the main, adding: "the party line mostly cares about controlling what people say, not directly controlling what people think."
- Quotes:
- (http://unremediatedgender.space/2023/Jul/a-hill-of-validity-in-defense-of-meaning/#isso-528, FeepingCreature, 2 likes)
> I think the strongest argument against (well, not really "against", at an angle...) I can think of would be this: you're treating rationality as a safety blanket, not a tool.
- (http://unremediatedgender.space/2023/Jul/a-hill-of-validity-in-defense-of-meaning/#isso-536, Davis, 0 likes)
> I think you have it mostly right. The missing piece is that the party line mostly cares about controlling what people say, not directly controlling what people think. Scott doesn't see a problem with this.

### 2024-07 · Isso: *Transcript: AGP and Epistemic Despair* (the Phil Illy interview)
- Path: `reception_data/isso_threads/2024_transcript-agp-and-epistemic-despair.md` · 2 comments (Davis 0) · http://unremediatedgender.space/2024/Jul/transcript-agp-and-epistemic-despair/
- Summary: Kay Brown, a Blanchardian trans woman blogger, thanks Davis for the transcript. Tara, a trans woman, reports a counter-instance to Davis's suggestion that learning the typology first discourages transition: she read Bailey and Lawrence early in her transition and was not discouraged.
- Quotes:
- (http://unremediatedgender.space/2024/Jul/transcript-agp-and-epistemic-despair/#isso-582, Tara, 2 likes)
> I'm skeptical that there's such an effect, because knowing about the typology didn't discourage me.

### 2020-06 · Isso: *Oceans Rise, Empires Fall*
- Path: `reception_data/isso_threads/2020_oceans-rise-empires-fall.md` · 7 comments (Davis 2) · http://unremediatedgender.space/2020/Jun/oceans-rise-empires-fall/
- Summary: Asked what "the Category War" refers to, Davis says he is "Not Ready to publicly tell the Whole Dumb Story" (a 2020 marker of the later memoir). To Sauce's request for a noncircular definition, he offers that trans women "can be said to be women in the same sense that" synthetic leather is leather. L (Zero) later criticizes this analogy in another thread.
- Quotes:
- (http://unremediatedgender.space/2020/Jun/oceans-rise-empires-fall/#isso-31, Davis, 1 like)
> (That wasn't the identifiable singular event, but I'm Not Ready to publicly tell the Whole Dumb Story.)

### 2025-09 · Isso: *A Generic Ontological Finickiness*
- Path: `reception_data/isso_threads/2025_a-generic-ontological-finickiness.md` · 4 comments (Davis 0) · http://unremediatedgender.space/2025/Sep/a-generic-ontological-finickiness/
- Summary: Kay Brown argues that all of the post's proposed explanations for the trans-women/trans-men asymmetry rely on adult social reasoning, while children show the same asymmetry. She attributes it to "femmephobia". JA reports that the categorization argument "requires very prolonged arguments" and is heard as rigidity. Max proposes an evolved protective instinct.
- Quotes:
- (http://unremediatedgender.space/2025/Sep/a-generic-ontological-finickiness/#isso-596, Kay Brown, 2 likes)
> All of the proposed reasons for the asymmetry are based on social reasoning of adults, but utterly fail to understand that children exhibit the SAME asymmetry long before they could have been socialized to those rationalizations

### 2021-09 · Isso: *I Don't Do Policy*
- Path: `reception_data/isso_threads/2021_i-dont-do-policy.md` · 3 comments (Davis 0) · http://unremediatedgender.space/2021/Sep/i-dont-do-policy/
- Summary: Phen asks for examples of useful predictions from developmental sex, and L (Zero) supplies a personal list. Celia's one-line criticism is the bluntest statement in the threads of a recurring complaint about structure.
- Quotes:
- (http://unremediatedgender.space/2021/Sep/i-dont-do-policy/#isso-448, Celia, 1 like)
> Your writing lacks thesis statements. It doesn't make clear points. It tends to be disorganized rambling.

### 2020-11 · Isso: *Survey Data on Cis and Trans Women Among Haskell Programmers*
- Path: `reception_data/isso_threads/2020_survey-data-on-cis-and-trans-women-among-haskell-programmers.md` · 7 comments (Davis 2) · http://unremediatedgender.space/2020/Nov/survey-data-on-cis-and-trans-women-among-haskell-programmers/
- Summary: Spencer posts the full contingency table and statistical "nitpicks": non-responses were included in totals; the sample's male skew makes comparisons hard; the comparison population is inappropriate; there are socioeconomic confounds. Davis edits the post to exclude non-responses and credits the comment. He reconciles their totals as a difference over "Non-binary" responses. (Davis later cites this post in defending *Fake Deeply*.)
- Quotes:
- (http://unremediatedgender.space/2020/Nov/survey-data-on-cis-and-trans-women-among-haskell-programmers/#isso-73, Davis, 0 likes)
> Thanks! I at least edited the post to not count non-responses (and credit your comment for pointing out the oversight).

### Remaining Isso threads (tally)
- Path: `reception_data/isso_threads/2017_a-beacon-through-the-darkness-or-getting-it-right-the-first-time.md` · http://unremediatedgender.space/2017/Feb/a-beacon-through-the-darkness-or-getting-it-right-the-first-time/
- Summary: (Quoted fragments in this tally were checked by hand against each thread's own file under `reception_data/isso_threads/`, since the scripted checker only knows the one Path above.) The other 39 non-empty threads (one to ten comments each) were all read. Most are short questions, corrections, thanks or tangents:
  - **Short substantive exchanges.**
    - *Don't Negotiate With Terrorist Memeplexes*: KartoffelElf asks for a more charitable reading. Davis answers that he is "extremely suspicious of utilitarian rationales for adopting less than maximally accurate beliefs" and distinguishes belief from behavior.
    - *Reply to The Unit of Caring on Adult Human Females*: Daniel Filan links Alex Byrne's philosophy paper defending "women are adult human females". Davis says the sub-subtopic "feels kind of mined out", and concedes a psychological definition would exclude atypical cis women: "that's why I lean against it".
    - *Interlude XX*: Rat Analyst and tailcalled debate whether trans activists are rational to treat Blanchardianism as dangerous. tailcalled reports that AGP trans women he knows who came out as Blanchardian fared "perfectly fine".
    - *Link: See Color*: Davis compares YouTube ratios on old and new Dove campaigns.
    - *Self-Identity Is a Schelling Point*: KartoffelElf asks whether the chromosomes-only pole is really stable.
    - *Link: The Jenner Shift*: Kay Brown says the post's T4T framing is historically wrong; she reports T4T was already the norm in the 1970s.
    - *Agreeing with Stalin*: FoxLisk claims partial credit for having publicly backed Davis on the old email. Sisa urges voting "straight-ticket Republican".
    - *Psychology Is About Invalidating People's Identities* and *Reply to Ozy on AGP* (2016): tailcalled links his 2021 surveyanon reply on causality.
  - **Appreciation.** *A Beacon Through the Darkness* (FeepingCreature, 7 likes, the highest-liked comment in these smaller threads), *Book Review: The Origins of Unfairness* ("I just bought this book because of your review!"), *Fake Deeply* (readers enjoy the "Villain Protagonist" story).
  - **Hostile or off-topic.** Election-fraud comments by BSRK Aditya on *Link: Can WNBA Players Take Down a U.S. Senator?*; two spam comments; L (Zero)'s personal note on *I Am Dropping the Pseudonym*.
- Quotes:
- (http://unremediatedgender.space/2017/Feb/a-beacon-through-the-darkness-or-getting-it-right-the-first-time/#isso-42, FeepingCreature, 7 likes)
> Let me take this opportunity to say that your reaction to the discovery of the word AGP is probably the most painfully relatable experience I have ever read or heard, and that I am incredibly grateful and indebted to you for putting it to text.

### Isso threads: overall shape (descriptive)
- The blog's own comments are a small, recurring community: a handful of regulars account for most comments.
- **tailcalled** is the dominant voice, with about a quarter of all comments. He is a former fellow Blanchardian turned persistent internal critic: of etiological framing, ETLE, parsimony, Bailey's methods, and Blanchardians' honesty.
- **Trans readers.** A cluster of trans readers (Emma, Sophia, notaname, Tara and others) engage respectfully but disagree, often urging Davis to consider transition or contesting his account of activists.
- **Gender-critical and lesbian commenters** (L (Zero), Vee) offer qualified sympathy and their own criticisms.
- **Influence.** Several AGP men credit the blog with helping them decide against transition, and one trans woman credits it with nothing of the kind.
- **Davis in his own comments.** He concedes specific errors readily: the "do I want to be her" search, the "perverted" wording, the Haskell non-responses, an "overreach" on transition outcomes, allying with *Irreversible Damage*. He holds his core positions and replies at length when his motives are questioned.

## Part C: Overview (descriptive)

This section summarizes patterns in Parts A and B. It assesses nothing; the study does that. Every claim below rests on entries above, which carry the quotes and links. Short quoted phrases here were checked by hand against the sources cited in those entries.

### Scale and venues
- **LessWrong.** 3,634 comments on 116 posts (2009–2026), 399 of them Davis's own. Two posts drew none.
  - Engagement is concentrated in a few threads, mostly from 2019 and 2023–2026: *If Clarity Seems Like Death to Them* (192), *My Interview with Cade Metz…* (188, mostly about Metz), *Rationalist Discourse Is Like Physicist Motors* (153), *Blanchard's Dangerous Idea…* (136), *A Hill of Validity…* (121), *Lack of Social Grace…* (114), *Where to Draw the Boundaries?* (113), *Comment on "Banning Said Achmiz"* (93).
  - Several of Davis's posts were Curated (e.g., *Where to Draw the Boundaries?*, *Terrified Comments on Corrigibility…*). By his own count he is a "9x Curated" author.
- **The UUT blog (Isso, since 2020).** 604 comments on 78 posts. A small community dominated by a few regulars, above all tailcalled.
- **Reddit.** Scattered citations in r/slatestarcodex, r/TheMotte, r/theschism, r/BlockedAndReported, AGP-focused and gender-critical subreddits, trans subreddits, r/SneerClub and r/rational. These include occasional threads devoted to a single post. Coverage comes from PullPush archive search, which is incomplete.
- **Dedicated written responses.** Ozy Brennan (2016, 2016, 2018, 2023), tailcalled (2021 blog reply; 2023 LessWrong post; many comments), Tracing Woodgrains (2022), Duncan Sabien (2025), Andrea James's reference page (reviewed 2026), and the other side of the Achmiz dispute in Habryka's ban post and its comments.
- **Not found.** No mainstream press coverage of Davis's own writing, and no academic citations, turned up. Cade Metz's journalism engages him as a source, but the August 2025 article could not be read (archive rate-limiting), and Metz's book is unpublished as of the transcripts. Davis reports a podcast interview (Phil Illy, 2024), which the corpus transcribes.
- **Not readable.** X/Twitter and Facebook (login walls), Kelsey Piper's 2018 Tumblr reply (login wall), and the bulk of Ozy's 2023 response (paywall).

### Recurring patterns, by subject
- **Philosophy of language and categorization** (*Where to Draw the Boundaries?*, *Unnatural Categories…*, *Philosophy in the Darkest Timeline*, the Skyrms and message-length posts).
  - On LessWrong, mostly substantive engagement.
  - Objections recur: Kaj Sotala and Wei Dai on coordination and consequences in definitions; ChristianKl and Dagon on essentialism; FeepingCreature's "the standard theory of meaning"; Vladimir Nesov's and Wei Dai's challenges on value-laden categories.
  - Davis typically concedes particular points while holding that redefining categories for consequences is a distortion.
  - Outside LessWrong the same essays are praised as the definitive answer to Alexander's "Categories" essay (r/slatestarcodex, r/TheMotte, themotte.org, Tracing Woodgrains), mocked (r/SneerClub), or answered by *reductio* (Ozy's "lesbians are not women").
- **Gender, autogynephilia and the two-type taxonomy.** The most polarized reception.
  - **Hostile.** SneerClub and some trans commenters are hostile, sometimes in personal terms ("self hating", "Nazi bar"), and often say they did not finish the essays.
  - **Approving.** Gender-critical and heterodox forums cite him approvingly, sometimes as ammunition, a use Tracing Woodgrains notes.
  - **Engaged dissent from trans readers** (Emma, Sophia, notaname, Tara, Ozy): they contest his account of activists and his inference from his own case, and urge him to consider transition.
  - **The most technical criticism comes from inside the Blanchard-sympathetic camp.** tailcalled argues against parsimony and etiological framing, against treating correlation as taxonomy, against Bailey's methods, and against Blanchardian honesty. Davis publicly conceded the causality point (2021).
  - **First-person influence.** Several readers report that the blog or typology helped them decide against transition. At least one trans woman says the typology did not deter her.
  - **Self-report objections** recur: "typical mind" (Rat Analyst), "erotic autocomplete" (FeepingCreature), and readers who say they fit neither a one-type nor a two-type model.
- **Discourse norms, moderation and the rationalist community** (*Physicist Motors*, *Lack of Social Grace*, *Assume Bad Faith*, the 2025–26 Achmiz and Duncan posts, the memoir sequence).
  - Prominent community members and moderators argue at length that Davis's framings are technically defensible but carry implications he disowns: habryka, Vaniver, Anna Salamon, Duncan Sabien, Raemon, gjm, Said Achmiz's critics.
  - They also argue that his adversarial manner and his discounting of feelings have real costs.
  - Davis's allies in these threads include Benquo, Jessica Taylor, Said Achmiz and jimmy (in part).
  - Neutral adjudicators (e.g., Richard Ngo on the Habryka exchange) assign fault to both sides.
  - Sabien's essay generalizes the criticism into a claim about Davis's understanding of high-trust cooperation.
  - Davis's reply pattern is consistent across these threads. He acknowledges specific overstatements (e.g., "not my finest work, rhetoric-wise"; "perfectly" corrected to "adequately"). He reframes disputes as conflicts of interest or as matters of principle, and asks for evidence about motives.
- **AI and alignment** (LLM-success debates, *Deep Learning Is Function Approximation*, the Claude-constitution posts, *Fake Deeply*). Technical criticism from ML-literate commenters: jdp on the "previous AI paradigm" framing; others on function approximation. On the constitution posts, a substantial bloc (cousin_it, roger-d-1, comex) defends Anthropic's "morality over corrigibility" balance against Davis's corrigibility-first argument.
- **Journalism and transcripts** (the Metz posts). Readers mostly praise the transcripts as a public service while warning Davis against talking to Metz (Jiro, Thane Ruthenis). Davis defends candor and publishing his own recordings over protecting the community's reputation.

### Davis as a commenter on his own work
Across both venues Davis replies often: 399 LessWrong comments, 69 on UUT.
- **Specific concessions are frequent and usually followed by edits.** Examples: the Haskell non-responses, the "perverted" wording, the "do I want to be her" search, *Irreversible Damage*, "overreach" on transition outcomes, the Royal Society "ad revenue" line, a mis-dated parenthetical in the Anthropic dispatch, the courtroom transcript's misquotations.
- **Concessions on core positions are rare and explicit when they occur.** Examples: the causality reply to tailcalled; leaning against psychological definitions of "woman".
- **He frequently moves to the meta level.** He questions interlocutors' motives or framing as well as their claims, and those interlocutors often name this as the friction.

### Positionality-relevant reception
These are items where Claude or Anthropic is the subject, or where LLMs mediate the discussion. They are flagged so the study can apply the same standard to them.
- The two constitution threads.
- *Dispatch from Anthropic v. Department of War*, where Davis used Claude Opus 4.8 to check his notes against the transcript.
- Davis's use of Claude and GPT models as arbiters in the Achmiz, Metz and *Listening Disorders* threads.
- A Claude Fable "interpretation of the existing research" invoked against him on *So You Don't Trust Me?*.
- *Fake Deeply*'s depiction of an AI lab.
- tailcalled's ChatGPT walrus stories.
