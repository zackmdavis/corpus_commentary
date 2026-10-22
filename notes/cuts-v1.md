# Cuts in the v1 length pass (2026-10-20)

Length pass on `study/` before the whole-book review (session c653f79f, Opus 5.5). Every cut is listed below with its chapter, section, approximate size, and what a reader loses. Any passage can be restored from commit 38fc8f4, the state before this pass.

**Measure.** Body + numbered notes + Note on method, excluding works cited: each chapter's `<section class="works…">` is stripped, the rest converted with `tools/html_to_text.py`, then `wc -w`. This gives 98,143 for the state at 38fc8f4. PROGRESS-phase3 recorded 97.9k by what was meant to be the same method, so the old figure was probably taken slightly differently. The figures below are internally consistent.

**Result: 98,143 → 95,687 words (−2,456).** That is well short of the pass's 8–10k target. Most of what remains in each chapter is either a step the chapter's conclusion depends on, a concession to Davis or one of his strongest points, or an objection the review handling sections record as adopted, and the drafting model judged those not worth cutting. (Correction, 2026-10-22: these limits were the drafting model's own judgment in that pass, not instructions from the commissioner or the brief; an earlier wording here misattributed them.) The section "Considered and not cut" lists what could still go and what each would cost.

| Chapter | Before | After | Change |
|---|---:|---:|---:|
| Introduction | 5,485 | 5,383 | −102 |
| 1 | 5,421 | 5,147 | −274 |
| 2 | 8,278 | 8,037 | −241 |
| 3 | 10,375 | 10,039 | −336 |
| 4 | 10,989 | 10,795 | −194 |
| 5 | 8,236 | 8,019 | −217 |
| 6 | 8,586 | 8,486 | −100 |
| 7 | 10,793 | 10,344 | −449 |
| 8 | 4,372 | 4,243 | −129 |
| 9 | 7,847 | 7,637 | −210 |
| 10 | 7,086 | 6,946 | −140 |
| 11 | 6,686 | 6,622 | −64 |
| Conclusion | 3,989 | 3,989 | 0 |
| **Total** | **98,143** | **95,687** | **−2,456** |

Word figures in the table of cuts are approximate (counted from the removed HTML text, so a few words of markup or citation are included).

## Cuts

| Chapter | Section | ~Words | What was cut | What the reader loses |
|---|---|---:|---|---|
| Intro | §1 | 95 | the second teaching example, "Bayesian Networks Aren't Necessarily Causal" (2023), and its link to Davis's 2021 concession in sexology; the conjugate-roots example stays | an example of the expository posts reaching interventions as what distinguishes causal graphs, and its cross-reference to Ch. 3. |
| Intro | §3 | 17 | sentence noting that chapter titles quoting Davis say where the phrase comes from | nothing of substance. |
| Ch. 1 | §2 | 75 | "Counterfactual Social Thought" as a precursor of the causal graphs (the post stays in §3, where its argument is used) and the quotation from "Goodhart's World" (Ch. 11 §1 quotes it; a linked mention stays) | repetition, and one forward link to Ch. 3's causal graph. |
| Ch. 1 | §2 | 45 | "Missing Words VI" (2014), two kinds of apology ("Both can be sincere, but they mean different things") | a second 2014 instance of candor about what one is doing. |
| Ch. 1 | §3 | 40 | "The Demandingness Objection" (2013), another promise to "quit philosophy" | one of three posts recording the retreat from philosophy. |
| Ch. 1 | §3 | 85 | "Lethal --force" (2014), the mock-sermon on a forced Git push, and "Pumpkin Spice!" (2014), "the first year of my life"; "non-canon" stays | two illustrations of the engineer phase. |
| Ch. 1 | §5 | 40 | "Concerns II" (Sept 2016), the sequel dialogue citing the argumentative theory of reasoning | one of the 2016 dialogues of exasperation. |
| Ch. 2 | §3 | 75 | the unpublished 2023 draft correcting gender-critical readers over Phil Illy ("the TIMs aren't just lying..."); the published Dec 2016 /r/GenderCritical post making the same correction stays | a second, later instance of Davis correcting his own side. |
| Ch. 2 | §5 | 55 | two reader responses, FeepingCreature (sympathetic) and Muireall (critical); Dipanjan and Rat Analyst remain, one on each side | two further voices in the split reception. |
| Ch. 2 | §6 | 45 | Bettcher 2014's interactional account of attraction and her term "erotic fragments" (compressed to one sentence) | some detail of her theory; the claims the chapter uses stay. |
| Ch. 2 | §7 | 70 | "Promises I Can Keep" (2019), the dialogue line "eggs don't deserve love" | an illustration of what the constraint on transition costs in marriage. |
| Ch. 2 | §7 | 35 | Lawrence 2007, "a variety of romantic love," as a second case of the same causal reading supporting the opposite decision (Ch. 3 quotes the phrase; Sophia's case stays), with its works-cited entry and note-on-method mention | the example of a trans woman sexologist who accepts Blanchard's account. |
| Ch. 3 | §4 | 100 | tailcalled's own argument for the causal direction (sexuality as an early, fixed motive) and his guess that a fitted model would show causation both ways | a sympathetic critic's view that the arrow may run in both directions (the section's verdict, causal claim and rivals both unestablished, stands without it). |
| Ch. 3 | §7 | 12 | sentence noting the Haskell post was corrected on a commenter's objection (already stated in §5) | nothing. |
| Ch. 3 | §8 | 85 | Davis's ideological Turing test result (11 of 18; log score −18.012, "just worse than chance"), offered as evidence of confident misreading of opponents | one piece of the pre-concession baseline, from Davis's own published self-test. |
| Ch. 3 | §8 | 130 | paragraph on the Bailey/Dreger controversy ("J. Michael Bailey did nothing wrong") and the standard the Murray review applied to Murray ("as fact, which I think is basically correct"), which Davis's polemics met least consistently, with the §1 mention of the Bailey-controversy history and Dreger 2008 in works cited and the note on method | Davis's partisanship on the Bailey controversy, and the observation that he held a popularizer to a standard (say why the alternatives fail) his own polemics did not consistently meet. |
| Ch. 4 | §1 | 30 | sentence restating the lede, that the distinction does not settle the dispute over woman | nothing (the lede and §8 state it). |
| Ch. 4 | §3 First critics | 70 | gjm thread restatement of arbitrariness argument (16 Mar 2019) and gjm's agreement | the comment-thread origin of the arbitrariness point, which §4 gives in its canonical form. |
| Ch. 4 | §8 What holds | 110 | "dilemma of redefinition" paragraph (folded one sentence, burden on redefinition, into §4) and "the mathematics" paragraph net | separate verdict lines; the substance stays in §4 and the note on method. |
| Ch. 5 | §1 | 55 | paragraph assigning neighboring topics to Chs. 4, 6 and 7 | a signpost (the cross-references remain at the points of use). |
| Ch. 5 | §2 | 55 | the "Lying Alignment Chart" (LW, 2023), whose center cell answers to the algorithmic account (a length cut an earlier review proposed), with its works-cited entry and the note-on-method sentence about the image | Davis's humorous map of the senses of "lie". |
| Ch. 5 | §3 | 110 | "Conflict Theory of Bounded Distrust" (2023), gjm's objection that it misread Alexander, and Davis's concession that it was "contaminated" by political differences; subsection heading now "Social punishment" | one further application of the account and a concession by Davis. |
| Ch. 6 | §1 | 60 | "'I Have the Honor to Be Your Obedient Servant'" (2016), Davis's earlier defense of diplomacy in writing on grounds of precision | a 2016 contrast to the 2018 policy on offense. |
| Ch. 6 | §6 | 50 | the opening of Davis's essay on the ban, its tribute to Achmiz as "the wisest person I know" and the anecdote of Achmiz talking him out of an analogy ("He was right.") | the essay's personal frame and one small instance of Davis taking Achmiz's criticism. |
| Ch. 7 | §1 | 120 | paragraph on privacy norms gamed through subtext ("leak everything ... as subtext"; "should not be so foolish as to think myself innocent"), with the study's note that it does not read the hypothetical section for subtext | one instance of Davis applying his privacy reasoning to himself (§5 keeps the fuller record of self-application). |
| Ch. 7 | §1 | 50 | Wayback reply "'female human' is a cluster in thingspace" confirming the rejoinder was put to Yudkowsky | a small confirmation that the obvious objection was raised in the 2018 replies. |
| Ch. 7 | §2 | 55 | "The three are taken in order" and two sentences restating why the 2021 proposal's fault is misdescription, not departure (compressed to one clause) | nothing of substance. |
| Ch. 7 | §4 | 35 | count of Davis's fourteen emails to Vassar, Aug 2016–Jan 2017, offered in one draft as evidence Vassar was one influence among many | one of the two pieces of counterfactual evidence (the other, "just as upset," stays). |
| Ch. 7 | §5 | 35 | "suicidally aggressive one-person culture war campaign" and "a really fun part of the æsthetic" | one example in the list of self-incriminating admissions. |
| Ch. 7 | §5 | 30 | "May Is Math and Wellness Month" quotation ("five months in constant emotional pain") | one of three contemporaneous posts recording the campaign's costs. |
| Ch. 7 | §7 | 60 | the "quokka policy" sentence of the Oct 2025 transcript and its gloss from "The Parable of the Scorpion and the Fox" | Davis's self-description of his openness to Metz as a quokka's. |
| Ch. 7 | §7 | 50 | Metz conversations, "contingent fact about flaws in people" and "It's a horrible problem" (deference to leaders) | two lines of Davis's assessment of the movement's failure. |
| Ch. 7 | §7 | 55 | Metz's reply that community members "use the same language" when Davis objected to "near-religious" | the journalist's side of the exchange about religious vocabulary. |
| Ch. 8 | §3 | 45 | the unpublished "Happy Meal" (2021), a deniably-allegorical dialogue about saying "lasagna" rather than "Italian food"; "A Proud Wells Fargo Customer" stays as the late example | one of four pieces carrying the tag. |
| Ch. 8 | §5 | 25 | the 2020 "Poetry Corner" on Raleigh's "The Lie" ("my favorite poem about revealing information about deception!"); the Patmore post stays | one example of Davis reading his themes into poems. |
| Ch. 8 | §6 | 55 | the description of "I, Too, Dislike It" beyond its epigraph (pastiche of Moore; links to four of Davis's captioned images; the plan to claim for a despised genre what Moore claimed for poetry) | what the draft's materials suggest it meant to argue. |
| Ch. 9 | §4 | 90 | paragraph on the 2013 hospitalization ("I asked to go to the hospital! Imagine being that misinformed!"; "physically safe the entire time"), from a 2021 draft and "Relativity" (2013) | two small pieces of evidence that Davis measured the ward against its physical facts and had once sought it out. |
| Ch. 9 | §6 | 60 | from-memory comparison with Thomas Szasz (social control; Davis grants a diagnosable condition and contests the description), with the Szasz mentions in the note on method and works cited | the one comparison with the anti-psychiatry tradition (an earlier review had asked for fuller treatment or omission). |
| Ch. 9 | §6 | 45 | "Wicked Transcendence III" (2017), "The horror is that everything is a cult" | the most extreme early statement of the social-control theory (the Facebook post and the June 2017 memoir state it). |
| Ch. 10 | §2 | 80 | "The Heckler's Veto Is Also Subject to the Unilateralist's Curse" (2020), Davis's argument that a pre-reader's veto is as unilateral as publication, and the study's point that symmetry of agency is not symmetry of expected cost | Davis's partial supply of the argument his footnote asked readers to wait for. |
| Ch. 10 | §5 | 60 | Turkheimer, Harden and Nisbett's criticism of expert-opinion surveys (response rates near five percent; no "cannot yet be estimated" option) | a reply to a hereditarian argument the chapter does not otherwise discuss. |
| Ch. 11 | §1 | 35 | the 2015 song lyric "I Want to Be the One" ("the one who writes the code"), which Ch. 1 also quotes, as an early restatement of the Singularity Institute's teaching | repetition only (Ch. 1 keeps it). |
| Ch. 11 | §4 | 35 | the plot summary of "Feature Selection," compressed to one sentence (Ch. 8 §5 describes the story as form) | repetition only. |

**Knock-on fixes.** Works-cited entries that no longer had a citation in the body were removed (Chs. 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, Introduction); Notes on method edited only where they named removed material (Ch. 2 Lawrence 2007; Ch. 3 Dreger 2008; Ch. 5 the Alignment Chart image; Ch. 8 the images linked from "I, Too, Dislike It"; Ch. 9 Szasz). In Ch. 4 one sentence was added to §4 (the burden on redefinition, from the cut §8 paragraph). In Ch. 7 the religion paragraph's "and he used it before the journalist did" went with the Metz exchange it referred to; in Ch. 2 the /r/GenderCritical sentence was reworded to stand without the cut draft; in Ch. 5 the subsection heading became "Social punishment"; in Ch. 1 "Goodhart's World" keeps a linked mention pointing to Ch. 11. Chronology: the 2013 hospitalization now links to Ch. 9 §1, since §4 no longer discusses it. No numbered note was removed or renumbered. The Conclusion was not changed: nothing it states was cut from the chapters.

## Considered and not cut

Read and weighed during the pass, and kept because cutting would remove an argument step, a concession to Davis or one of his strongest points, or an objection adopted from a review. Sizes are approximate. Any of these could still be cut.

**Candidates named by the cross-chapter pass.**
- **Ch. 4 §8 "Two categories, and the negotiation between them" (~1,000w).** Every paragraph is a step the conclusion uses: two real categories near *woman*; the dispute is first-kind value-dependence (favorable to the framework, unfavorable to the polemic); Davis's strongest reply (social gender estimates developmental sex) and cata's point; Ozy's *reductio* and the handoff to Ch. 3; the demand that the trade be stated, with the fairness caveat on "sucks to be you". Nearly all of it came from the GPT and Fable reviews. Smaller trims possible: the detail of the unpublished reply to Ozy (~90w, but it is Davis's best answer to the *reductio*); the second Plunkett & Sundell quotation (~20w).
- **Ch. 7 §7 (press and religion).** Trimmed ~165w (above). The rest is the adopted Jiro/Ruthenis/orthonormal paragraph (restraint toward Metz as a measure of the role-relative standard), the "failed … so, so much better" paragraph (~75w; candidate), and the religion frame (Davis's own key to the memoir).
- **Ch. 6 §6 (the Achmiz affair, ~1,600w).** Trimmed ~50w. The rest carries the lede's finding (the Salamon coin-room reply as the coordination argument overriding the norm of accounting, with its sound point) and adopted review points: rules vs standards, effort, Habryka's grammatical repair, the author-ban inference being conditional on purpose. Candidates: "On the Normativity of Debate" (~60w, which shows Davis's position was not simply Achmiz's) and the closing list of concessions (~55w).
- **Ch. 10 §6 (the charge against Alexander, ~900w).** Trimmed nothing. The Conclusion and the lede depend on it. Its fairness to Alexander (the functional test applied to his statement) and the noncentral-fallacy sentences (~60w) were kept deliberately in the Fable revision.
- **Ch. 2 §6–7 (injustice; transition as choice).** Trimmed ~150w. The rest is the Fricker reconstruction, Bettcher's two challenges and Davis's possible answer, and the demand-curve argument with the average/marginal point, all of which the conclusion uses. Small candidates: Illy's "epistemic injustice" remark (~25w), the "applied transhumanism" concession (~30w).

**Other passages weighed.**
- Ch. 4: Alexander's sixth-section "biological correlates" parenthetical (~25w; fairness to Alexander); "Beyond the Binary" / "Generic Ontological Finickiness" (~230w; Davis's own concessions and gjm's selection critique); Arnold's "meandering vagueblog" and Hornbein's praise of WTDTB (~60w; reception on both sides).
- Ch. 7: the Bromley genre paragraph (~90w; method caveat with a from-memory label); the RamblinDash "World's Best" analogy (~75w; Davis's concession, referred to in §7); the failed *Planecrash* test (~70w; self-criticism); FoxLisk's objection (~60w); the "Egoist Faith" quotation could lose ~30w.
- Ch. 6: the Steelmanning/ITT paragraph (~260w; Wentworth's objection and the adopted point about the term); Elle Najt's 2019 objection (~95w); Mill (~50w; gives each side an ally); Mercier and Sperber (~180w; scholarship).
- Ch. 5: "Communication and its maintenance" (~280w; Ninety-Three's counterexample as reworked after the GPT review, and Lopez); the commenters on "Explaining away" (~120w; Davis agreed with them).
- Ch. 3: Långström and the "~5% (?)" check (~110w; adopted, "cuts both ways"); the Haskell paragraph with note 2 (~250w; Davis's own data, re-derived); "The Social Construction of Reality" paragraph (~170w; adopted from Fable).
- Ch. 9: "Concerning Frame Control" (~110w; credits Davis with making the claim falsifiable).
- Ch. 10: the COVID draft (~110w; the more careful habit, credited to Davis).
- Ch. 11: the AI Village paragraph (~170w; one of Davis's remarks about Claude, which the positionality rule requires the chapter to treat).
- Ch. 8: "Two Political Short Stories" could be compressed by ~60w.
- Introduction §2: the detail of the 2017 episode and Davis's attribution of it to stress, not the hormones (~55w; appears nowhere else).
- Conclusion §1 (AI) and §4 (sexology) restate the chapters' verdicts (~250w between them), but they were calibrated against the chapters in the Fable revision, and compressing them risks misstating a verdict.

Taken together these come to roughly 3,300 words, which would bring the total to about 92.4k. Getting to 88–90k would also take structural cuts in the named sections above (Ch. 4 §8, Ch. 6 §6, Ch. 10 §6, Ch. 2 §6), which would cost arguments.

## Second length pass (2026-10-22), after the whole-book review

The whole-book GPT-6-Astra review (`notes/reviews/whole-book-gpt.md` §7) proposed 13–16k words of cuts. The user asked the drafting model to use its own academic judgment on them; the decisions below are the drafting model's. Measure as above. Starting point (after the review was processed): 97,563. **Result: 95,157 (−2,406).** Restore from commit 3a07f4c.

**Judgment on the review's diagnosis.** It is right that each verdict was stated up to four times: in the Introduction's preview, the chapter's lede, the chapter's conclusion, and the Conclusion's survey of the chapters. Ledes that state a chapter's argument are standard in a monograph and were kept. Chapter conclusions were cut where they re-listed what the lede and body had just said and kept where they carry the chapter's own synthesis (Chs. 2, 4, 6 and 8, and the second paragraphs of Chs. 3, 7, 9, 10 and 11). The Conclusion was rewritten as synthesis. The review's estimate of the rest does not hold up. It was made without reading the corpus, and a check of the chapters it names (Chs. 1, 5, 6 and 8 read in full, and 7, 11, the Introduction and the Conclusion earlier the same day) found the material to be argument, concessions or evidence the verdicts rest on. A search for long quotations shared between chapters found four, all deliberate cross-references, so the cross-chapter repetition it describes was largely removed already by the cross-chapter pass.

| Review's row | Proposed | Done | Judgment |
|---|---:|---:|---|
| Introduction §§3–6 | 1,200–1,500 | ~140 | Chapter list in the first claim compressed; Murray/retrospective sentences dropped. The scope, positionality and method sections are required by the brief and were kept. |
| Ch. 1 §§2, 5–7 | 700–900 | ~110 | Overlap with Ch. 8 (dialogues, "October Eleventh") and a restated rule cut. §2's early evidence is the chapter's argument. |
| Chs. 2 §§4–6, 3 §§7–9 | 1,400–1,700 | ~90 | Recaps in the two conclusions cut. No duplicated passages found between the chapters; they do different evidential work, as the review itself says. |
| Ch. 4 §§6, 8–10 | 1,500–1,900 | 0 | §8 was already judged argument in the first pass (see above); §9's stealth-reply paragraph is short and Ch. 8 depends on it; §10 states the norm the chapter earns. |
| Ch. 5 §§1, 3–6 | 900–1,200 | ~155 | Agreed on §1's duplicate of the lede; cut. §§3–6 not cut. |
| Ch. 6 §§2, 4, 6–7 | 1,500–1,800 | ~55 | Read in full. The companion essays each carry an objection or a concession, and the Achmiz section carries the lede's finding. One over-detailed passage compressed. |
| Ch. 7 §§1–3, 5–8 | 1,800–2,200 | ~110 net | Conclusion compressed. The rest is the evidence for the three verdicts; §5's record of conduct is what the chapter credits. |
| Ch. 8 §§1, 3, 5–6 | 500–700 | ~140 | Summaries without analysis cut; summaries the analysis uses kept. |
| Ch. 9 §§2, 4–6, 8–9 | 700–900 | ~115 | Conclusion recap cut. |
| Ch. 10 §§2–4, 7 | 500–700 | ~65 | Conclusion compressed. |
| Ch. 11 §§5–7 | 700–900 | ~65 | Conclusion compressed; §5's qualifications are the positionality procedure's substance. |
| Conclusion §§1–6 | 1,600–2,000 | ~1,410 | Agreed; rewritten as synthesis, verdicts unchanged. Open questions kept, compressed (they are the study's, not questions for the author). |

**Where further cuts would come from.** The three longest chapters (Ch. 4, 10.9k; Ch. 7, 10.8k; Ch. 3, 10.0k). Cutting them further would remove evidence or adopted objections. That trade is not worth making while the study is under the brief's ceiling.
