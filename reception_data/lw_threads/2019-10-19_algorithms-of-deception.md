Title: Algorithms of Deception!
LessWrong-URL: https://www.lesswrong.com/posts/fmA2GJwZzYtkrAKYJ/algorithms-of-deception
Posted: 2019-10-19
Fetched: 2026-10-13 (LessWrong GraphQL API; rendered by tools/render_lw_threads.py)
Comments: 7 (commentCount field: 7)

#### [-] artifex · 1 karma · 2019-10-19 · https://www.lesswrong.com/posts/fmA2GJwZzYtkrAKYJ/algorithms-of-deception?commentId=dD8DoxRwZKMcmrcEf
Category gerrymandering doesn’t seem like a different algorithm from selective reporting. In both cases, the reporter is providing only part of the evidence.

#### [-] Trinley Goldenberg · 2 karma · 2019-10-20 · https://www.lesswrong.com/posts/fmA2GJwZzYtkrAKYJ/algorithms-of-deception?commentId=WQNt97PH6DvP7vy4Q
This is interesting! The straightforward research program here seems to just be to study heuristics and biases, yes? I'm curious if you're going in a different direction.

#### [-] romeostevensit · 7 karma · 2019-10-20 · https://www.lesswrong.com/posts/fmA2GJwZzYtkrAKYJ/algorithms-of-deception?commentId=tvwsBepFeYgMvQuzy
I might summarize the hansonian/elephant in the brain position thusly: sincerity is selected for.

#### [-] Pattern · 1 karma · 2019-10-20 · https://www.lesswrong.com/posts/fmA2GJwZzYtkrAKYJ/algorithms-of-deception?commentId=MbCAyTfst53opS28Y
> *very similar*

The same for 4 significant digits.

> \[a\] perfectly sincere.

> \[b\] In a peaceful world where most falsehood was due to random mistakes, there would be little to be gained by studying processes that systematically create erroneous maps.

Systematic error is conflated with conflict (in b), following sections (in the vicinity of a) which claim error is not conscious. Even if I accept b,

> \[c\] . In a world of [conflict](https://slatestarcodex.com/2018/01/24/conflict-vs-mistake/), where there are [forces trying to slash your tires](https://www.lesswrong.com/posts/XTWkjCJScy2GFAgDt/dark-side-epistemology), one would do well do study these—*algorithms of deception!*

why should c follow? Why not tune out what can't be verified, or isn't worth verifying? (I say this as someone who intends to vote on this post only after running the code.)

#### [>] Isnasene · 2 karma · 2019-10-20 · https://www.lesswrong.com/posts/fmA2GJwZzYtkrAKYJ/algorithms-of-deception?commentId=ZGReMw2YezeyqvAd3
> why should c follow? Why not tune out what can't be verified, or isn't worth verifying? (I say this as someone who intends to vote on this post only after running the code.)

Because of things like [selective reporting](https://www.lesswrong.com/posts/DoPo4PDjgSySquHX8/heads-i-win-tails-never-heard-of-her-or-selective-reporting), the vast majority of information reported to us tends to be misleading, but not without some level of useful information (and sometimes a lot of useful information). Instead of tuning out information or spending exhaustive amounts of time attempting to verify it, a faster solution is often to figure out ways to adjust the (inaccurate) information for deception to get only the useful information and a better understanding of uncertainty within it.

Of course, if there is a 100% un-deceptive source for a given piece of information, there's not much value in trying to use deceptive sources for that same piece of information (unless the former source is much more expensive than the latter).

#### [-] Isnasene · 6 karma · 2019-10-20 · https://www.lesswrong.com/posts/fmA2GJwZzYtkrAKYJ/algorithms-of-deception?commentId=pRjtC2hT3Ts39KztH
This is the kind of issue that [being really specific](https://www.lesswrong.com/posts/FfrWGCEhZJbkeFgww/the-power-to-demolish-arguments) can be used to resolve. If the Reporters were specific about what they were trying to do in their reporting, the Audience would not have used their reports. If this is unfeasible, the Audience could still specifically ask the Reporters to clarify whether they think she will be able to figure out the specific things she is trying to figure out using their reports. If they mislead her here, Audience can credibly claim that either she was lied to or that the reporters are not competent enough to be relied on for information. Pragmatically, both these possibilities imply a course-of-action that involved not using the reporters as reporters.

To illustrate in detail:

> So, too, imagine each of our possible Reporters as a person: loyal, responsible—and, entirely coincidentally, the supplier of a good that Audience's careful plans call for in proportion to the value of P(X=4).

In this context, the audience has an explicit goal of estimating how frequently X=4 occurs. Keeping this in mind, the problem the audience is having can be understood in the context of interacting with reports with misaligned goals.

> Sure, I'm not a perfect program free from all bias, but everything I said was true—every outcome I reported corresponded to one of the Xi. [You can't call that misleading!](https://www.lesswrong.com/posts/DoPo4PDjgSySquHX8/heads-i-win-tails-never-heard-of-her-or-selective-reporting)"

Reporter 2's goal seems to be "report values that correspond to one of the Xi." This is misaligned with a goal associated with estimating the distribution of X.

> I told you the truth, the whole truth, and nothing but the truth: everything I saw, I reported. When I said an outcome was a oneorfour, it actually was a oneorfour. Perhaps you have a different category system, such that what *I* think of as a 'oneorfour', appears to you to be any of several completely different outcomes, which you think my 'oneorfour' concept is conflating.

Reporter 3's goal seems to be "report values but conflate ones and fours into a 'oneorfour' category" (in the actual programming, this is a misrepresentation of course. Reporting a one *or* a four as a one *and* a four isn't the same thing). This is misaligned with the goal of figuring out how frequently fours are specifically.

If Reporter 2 or Reporter 3 had explicitly specified what they were trying to do, the Audience wouldn't have used them as an information source.

If Reporter 2 had told Audience that he believed Alice could determine probabilities just from his reporting, he would be lying, or too incompetent to trust.

If Reporter 3 had told Audience that he believed Alice could distinguish the probability of fours separate from the probabilities of ones, he would be lying, or too incompetent to trust.

#### [-] Pongo · 12 karma · 2020-05-06 · https://www.lesswrong.com/posts/fmA2GJwZzYtkrAKYJ/algorithms-of-deception?commentId=ncAv4bPDMAfn8dTHG
> If true "beliefs" are models that [make accurate predictions](https://www.lesswrong.com/posts/a7n8GdKiAZRX86T5A/making-beliefs-pay-rent-in-anticipated-experiences), then *deception* would presumably be communication that systematically results in *less* accurate predictions (by a listener applying the same inference algorithms that would result in more accurate predictions when applied to direct observations or "honest" reports).

This helped me clarify that these *algorithms of deception* are not just adversarially attempting to deceive, but in fact adversarially crafted for one's belief-forming mechanisms.

