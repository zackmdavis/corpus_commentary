Title: Speaking Truth to Power Is a Schelling Point
LessWrong-URL: https://www.lesswrong.com/posts/tCwresAuSvk867rzH/speaking-truth-to-power-is-a-schelling-point
Posted: 2019-12-30
Fetched: 2026-10-13 (LessWrong GraphQL API; rendered by tools/render_lw_threads.py)
Comments: 19 (commentCount field: 19)

#### [-] Bendini · 8 karma · 2019-12-30 · https://www.lesswrong.com/posts/tCwresAuSvk867rzH/speaking-truth-to-power-is-a-schelling-point?commentId=5ESaeN3dGJZjkbuBJ
I find this theory intuitively plausible, and I expect it will be very important if it's true. Having said that, you didn't provide any evidence for this theory, and I can't think of a good way to validate it using what I currently know.

Do you have any evidence that people could use to check this independently?

#### [-] quanticle · 14 karma · 2019-12-30 · https://www.lesswrong.com/posts/tCwresAuSvk867rzH/speaking-truth-to-power-is-a-schelling-point?commentId=Z8pS35BE9fzrsGxs7
The thing that stops this process from fully sliding down the "slippery slope" towards speaking truth to power unconditionally is that there is a countervailing force: the penalty the coalition pays for its honesty. In the real world, there is not a simple dichotomy between the coalition and the rest of the world. Rather there are many coalitions, all competing for favor and resources. At the same time, the power is not omnipotent -- there is a certain level of truth that it is willing to tolerate, simply because it doesn't have the ability to enforce its ideological line strictly enough to police everyone. This power, of course, varies from place to place. As a result, we get a variety of equilibria, depending on how tolerant the power is. A free, open, democratic society will have a certain threshold for how much truth it is willing to tolerate (when that truth is against "conventional wisdom"). An authoritarian society will have a much different threshold.

#### [-] Chris_Leong · 11 karma · 2019-12-30 · https://www.lesswrong.com/posts/tCwresAuSvk867rzH/speaking-truth-to-power-is-a-schelling-point?commentId=ZEgBiZLb28Q2QL82f
TLDR: When you engage in intellectual dishonesty due to social pressure, you distort your perspective of the world in a way that makes further intellectual dishonesty seem justified. This results in a downwards spiral.

#### [-] Isnasene · 11 karma · 2019-12-30 · https://www.lesswrong.com/posts/tCwresAuSvk867rzH/speaking-truth-to-power-is-a-schelling-point?commentId=6N6oLMfWsZBtzo72k
> Then the coalition faces a choice of the exact value of *x*. Smaller values of *x* correspond to a more intellectually dishonest strategy, requiring only a small inconvenience before resorting to obfuscatory tactics. Larger values of *x* correspond to more intellectual honesty: in the limit as *x* → ∞, we just get, "Speak the truth, even if your voice trembles (full stop)."

I don't think that a one-parameter x% trade-off between truth-telling and social capital accurately reflects the coalitional map for a couple reasons

*   x% is a ratio y:z between intellectual dishonesty and social capital, roughly speaking. The organization would need to reach a shared agreement about what it means y% more intellectually dishonest and what it means to get z% more social capital. Otherwise, there will be too much intra-coalition noise to separate the values of coalition members from the trade-offs they think they are making

*   This also means coalition members can strategically mis-estimate their level of honesty or the value of the gained social capital higher or lower depending on their individual values -- deliberately obfuscating values in the organization

*   Different coalitions have different opportunities for making x% trade-offs and people can generally freely enter and exit coalitions. My impression is that this differential pressure and the observed frequency with which you make x% trade-offs relative to alternative coalitions is what determines of the values of those who enter and exit the coalition -- not x% itself. This means

*   x% isn't a good Schelling point because I don't really think it's the parameter that is affecting the values of those involved in a colaition
*   slippery slopes are more likely to be caused by external things like the kind of trade-offs available to a coalition -- as opposed to the values of the coalition itself

*   social capital with external sources isn't *usually* the main organizational bottle-neck. People might be willing to make an x% trade-off but first they would probably exhaust all opportunities that don't require them to make such a trade-off. And attention is finite. This means that a lot of pressure has to be applied before people actually begin to notice the x% . Maybe it's a Schelling point at equilibrium but I don't think it moves very quickly

> In the absence of distinguished salient intermediate points along the uniformly continuous trade-off between maximally accurate world-models and sucking up to the Emperor, the only Schelling points are *x* = ∞ (tell the truth, the whole truth, and nothing but the truth) and *x* = 0 (do everything short of outright lying to win grants). In this model, the tension between these two "attractors" for coordination may tend to promote coalitional schisms.

I think it's more likely that, as you select for people who make x% trade-offs for your coalition's benefit, you'll also tend to select for people who make x% trade-offs against your coalitions benefit (unless your coalition is exclusively true-believers). This means that there's a point before infinity where you have to maintain some organizational that provides coalition non-members with good world models or else your coalition members will fail to coordinate your coalition into having a good world-model itself.

#### [-] Vaniver · 6 karma · 2019-12-30 · https://www.lesswrong.com/posts/tCwresAuSvk867rzH/speaking-truth-to-power-is-a-schelling-point?commentId=mSE79Ev5orqv5opP3
I think the difference between direct benefit and net benefit is more general. That is, this post outlines a way in which accepting true observations that have already been collected might make the coalition net worse off at finding the truth, because of adversarial action in the external world. But when considering what observations to seek out in the future, the coalition faces tradeoffs (again, imposed by the world, but the practicalities of time and energy and other resources, rather than enemy action). If they document the differing kinds of beetles, that takes time and attention that could have been spent documenting the differing kinds of bees.

Whether beetles or bees are more interesting can of course only be estimated using the coalition's *current* beliefs, rather than their beliefs after they have obtained the data they will obtain. The coalition might reasonably expect that time spent on beetles instead of bees is a 'net waste' even if the additional data on beetles is in fact expected to be useful, because of scarcity and expecting additional data on bees to be more useful.

It seems like there are lots of principles that make sense to apply here, so that they're not just doing naive maximization, since this is a [multi-armed bandit problem](https://en.wikipedia.org/wiki/Multi-armed_bandit). They probably want to [shrink](https://en.wikipedia.org/wiki/Shrinkage_\(statistics\)) estimates towards the mean, have an ensemble of models and have some of the budget directed by each individual model (and reallocate that budget afterwards), and various other things.

So it seems to me like you have to have this sort of ability to do cost-benefit tradeoffs given your current beliefs in order to operate *at all* in an embedded framework.

#### [-] Vaniver · 26 karma · 2019-12-30 · https://www.lesswrong.com/posts/tCwresAuSvk867rzH/speaking-truth-to-power-is-a-schelling-point?commentId=CghQCKHyzw26dKCaK
On slippery slopes specifically, I note that Scott's article points out that there *do* seem to be equilibria besides "all" or "nothing", where "free speech" as legally understood in the US does have lots of exemptions carved out of it, and it doesn't seem to be significantly different whether or not Holocaust Denial is one of those exemptions. (An example that does seem to [matter significantly](https://web.archive.org/web/20130509133717/http://www.manilatimes.net/index.php/news/top-stories/16100-libel-law-violates-freedom-of-expression--un-rights-panel) is whether truth is a defense against libel; interestingly, it was not so for criminal libel cases for a long time in England, whereas it was for civil libel cases.)

One of the differences between Schelling points and general coordination equilibria seems relevant: the former you can reach blind, but the latter you can reach using sight and convergence. Given that we have the ability to establish traditions and reach approximate convergence on standards, it's not obvious that we should abandon that ability in order to have pure standards that are reachable by individual thought. Yes, it's nice to satisfy that constraint also, but is it worth the cost in this case?

#### [-] steven0461 · 27 karma · 2019-12-30 · https://www.lesswrong.com/posts/tCwresAuSvk867rzH/speaking-truth-to-power-is-a-schelling-point?commentId=amfw3f8bTCeLPxCoj
If the slope is so slippery, how come we've been standing on it for over a decade? (Or do you think we're sliding downward at a substantial speed? If so, how can we turn this into a disagreement about concrete predictions about what LW will be like in 5 years?)

#### [>] Zack_M_Davis [AUTHOR] · 0 karma · 2019-12-31 · https://www.lesswrong.com/posts/tCwresAuSvk867rzH/speaking-truth-to-power-is-a-schelling-point?commentId=nZ3ofXWCerKQSz5a8
OP is trying to convey a philosophical idea (which could be wrong, and whose wrongness [would reflect poorly on me](https://www.lesswrong.com/posts/y4bkJTtG3s5d6v36k/stupidity-and-dishonesty-explain-each-other-away), although I think [not _very_ poorly, quantitatively speaking](https://www.lesswrong.com/posts/6dmKBjc7XarcQMRYW/being-wrong-doesn-t-mean-you-re-stupid-and-bad-probably)) about "true maps as a Schelling point." (You can see a prelude to this in the last paragraph of [a comment of mine from two months ago](https://www.lesswrong.com/posts/bSmgPNS6MTJsunTzS/maybe-lying-doesn-t-exist#uZAi9ncHTX9xTui6h).)

I would have thought you'd prefer that I avoid trying to apply the philosophy idea to a detailed object-level special case (specifically, that of this website) in the comment section of a Frontpaged post (as a opposed to a lower-visibility meta post or private conversation)?? (Maybe this is another illustration of [Wei's point that](https://www.lesswrong.com/posts/bFv8soRx6HB94p5Pg/against-premature-abstraction-of-political-issues) our traditional norms just end up encouraging hidden agendas.)

#### [>>] Raemon · 2 karma · 2019-12-31 · https://www.lesswrong.com/posts/tCwresAuSvk867rzH/speaking-truth-to-power-is-a-schelling-point?commentId=hRACAxhcgC7p8NtDu
I replied with some meta-thoughts about my uncertainties and best guesses about current norms [over here on shortform](https://www.lesswrong.com/posts/jL7uDE5oH4HddYq4u/raemon-s-scratchpad#w77DWou2MAvpivyte).

#### [-] Raemon · 8 karma · 2019-12-31 · https://www.lesswrong.com/posts/tCwresAuSvk867rzH/speaking-truth-to-power-is-a-schelling-point?commentId=xkTWCuCYdByhxJMrZ
A thing that's making this discussion harder is the [open problem you listed in your prior post](https://www.lesswrong.com/posts/MN4NRkMw7ggt9587K/firming-up-not-lying-around-its-edge-cases-is-less-broadly).

What *do* you do to ensure you're actually being honest, given the huge array of options one has to share cherry-picked data, vaguely imply things, etc? Esp. if we have reason to think we're subconsciously finding the nearest unblocked strategies?

Right now, I *don't* actually see an "*x* = ∞" option available. I don't have *time* to write every inconvenient thought that pops into my head. I don't even have time to publish the convenient things that I think would definitely improve the world if I communicated more about them. How do I decide which inconvenient things to say out loud? What processes can I follow to write up thoughts in a truly intellectually honest way?

It seems like if we had a good answer, then people aspiring towards Strong Honesty would not only have clearer ideas of how to improve, there could potentially be a new schelling fence to more easily coordinate around.

\[I will attempt to actually try answering this question at some point. If it is The Loosely Defined Future and I haven't responded to this comment, feel free to yell at me until I've at least spent 30 minutes brainstorming and published the result\]

#### [-] SlightlyLessHariyApe · 3 karma · 2019-12-31 · https://www.lesswrong.com/posts/tCwresAuSvk867rzH/speaking-truth-to-power-is-a-schelling-point?commentId=Kd3bXRpmkAwaoSaCu
> In the absence of distinguished salient intermediate points along the uniformly continuous trade-off between maximally accurate world-models and sucking up to the Emperor, the only Schelling points are *x* = ∞

[The Kolmogorov Option](https://www.scottaaronson.com/blog/?p=3376) is another salient intermediate point.

> This is where you build up fortresses of truth in places the ideological authorities don’t particularly understand or care about, like pure math, or butterfly taxonomy, or irregular verbs. You avoid a direct assault on any beliefs your culture considers necessary for it to operate. You even seek out common ground with the local enforcers of orthodoxy.

> \[...\]

> But even if so, you could still be honored by future generations for building your local pocket of truth, and for not giving falsehood any more aid or comfort than was necessary for your survival.

#### [-] jmh · 1 karma · 2019-12-31 · https://www.lesswrong.com/posts/tCwresAuSvk867rzH/speaking-truth-to-power-is-a-schelling-point?commentId=te82YDAvYXRxhHBHE
Another possible implication might be incentives towards defining organizational mission in ways that effectively make the problematic truths "out of mission" so purely private views. Then the truth sayer will only be speaking as an individual -- which could perhaps have them moved out of membership if it the actions were to disrupt the organizational mission. Or simply remove them from any protections some group membership might have otherwise provided.

#### [-] Dagon · 4 karma · 2019-12-31 · https://www.lesswrong.com/posts/tCwresAuSvk867rzH/speaking-truth-to-power-is-a-schelling-point?commentId=xMgo5mCTXaCZpFE3p
> Consider a coalition that wants to build accurate shared world-models (maps that reflect the territory), and then use those models to inform decisions that achieve the coalition's goals.

I think you're hiding a lot of important and unsolved complexity in the phrase "the coalition's goals". Coalitions don't actually share beliefs, world-models, or goals. Members have individual versions of these things, which partly align.

Really separating the motives and desires of a member who only partly trusts other members of a coalition, from the convenient-but-misleading phrasing of a coalition's values or a coalition's behaviors, would likely make this clearer. Note that many of your points remain valid for individual difficulties of action, as a coalition of one.

#### [-] Zack_M_Davis [AUTHOR] · 4 karma · 2019-12-31 · https://www.lesswrong.com/posts/tCwresAuSvk867rzH/speaking-truth-to-power-is-a-schelling-point?commentId=AFxeTwLLpyWcjQpsm
Comment of the week goes to [hillsump at /r/TheMotte](https://www.reddit.com/r/TheMotte/comments/ehi8bl/speaking_truth_to_power_is_a_schelling_point/fcmh51v/) (emphasis mine):

> [T]he text is somewhat incoherent. It claims that in-between positions are not sustainable and also that both extremes are Schelling points, yet the title suggests that the truth-telling extreme is the "right" focus point. I happen to share the author's belief that the extremes may be points of attraction, but the claim at the end that they form dual Schelling points needs further evidence. A system with two points of attraction is inherently unstable, negating the feedback cycle that seems necessary for a Schelling point in the first place, and it is not clear why out of band signalling about the current consensus cannot lead to an in-between position as the "obvious" future consensus point. Keeping in mind the paradigmatic Schelling point that people prefer "heads" in a game involving choice between heads or tails, _I think the fable is trying to create a future consensus around the truth telling extreme via out of band signalling to children, making this extreme a priori more salient to future generations than a socially signalled non-truth position._ In contrast, my takeaway from this piece is that the author is either arguing badly, or the text is meant as a kind of rationality koan, promoting enlightenment via engagement with its flawed argument.

The Straussian reading is definitely _not_ intended on my part—I wouldn't play that kind of mind game with you guys! Or at least, it definitely wasn't _consciously_ intended, but I have to concede that it's _probably not a coincidence_ that the title ended up being "Speaking Truth to Power Is ..." rather than "Preferred Narratives of the Powerful Are ...". Every author should hope to attend [her own funeral](https://tvtropes.org/pmwiki/pmwiki.php/Main/DeathOfTheAuthor).

#### [-] Wei Dai · 7 karma · 2020-01-01 · https://www.lesswrong.com/posts/tCwresAuSvk867rzH/speaking-truth-to-power-is-a-schelling-point?commentId=bTo3NLbRemWwENMD5
>Speak the truth, even if your voice trembles—unless adding that truth to our map would make it x% harder for our coalition to compete for Imperial grant money

Why do you assume that this is the only negative consequence of speaking the truth? In the real world (that I think I live in), speaking some truths might get your child bullied in school (including by the teachers or administrators), or get you unemployed, jailed, or killed. Is this post supposed to have applications in that world?

#### [>] Zack_M_Davis [AUTHOR] · 8 karma · 2020-01-01 · https://www.lesswrong.com/posts/tCwresAuSvk867rzH/speaking-truth-to-power-is-a-schelling-point?commentId=S3WDjfrf2RHBbTDn7
I actually feel okay about letting readers fill in this kind of generalization for themselves? Similarly, in the real world, punishable truths aren't about literal naked Emperors, but I tend to assume most readers are familiar with (or can figure out) the trope of [the famous Hans Christian Andersen story](https://en.wikipedia.org/wiki/The_Emperor%27s_New_Clothes) being used as an allegory for politically-unfavorable truths in general.

I guess you could argue that my choice of illustrative fictitious examples is [algorithmically-dishonestly](https://www.lesswrong.com/posts/fmA2GJwZzYtkrAKYJ/algorithms-of-deception) "rigged": that, as a result of my [ongoing](https://www.lesswrong.com/posts/yaCwW8nPQeJknbCgf/free-speech-and-triskaidekaphobic-calculators-a-reply-to) "People should be braver about saying stuff!" meta-political [campaign](https://www.lesswrong.com/posts/P3FQNvnW8Cz42QBuA/dialogue-on-appeals-to-consequences#ePhNhdZTcLs54B4X7), the [elephant in my brain](http://elephantinthebrain.com/) knew to generate an example (applying for grants) that would make forthrightness seem like the right choice (piggybacking off of [traditional "money is corrupting" moral intuitions](https://en.wikipedia.org/wiki/Love_of_money)), rather than an example that would make conformity seem like the right choice (like protecting one's family)?

I'm not sure what my response to this charge is. The most reliable way of removing such biases would plausibly be to pose everything as an abstract math problem without any illustrative examples, but that seems like it would decrease reading comprehension a lot (and maybe _still_ suffer from the ["encouraging hidden agendas" problem](https://www.lesswrong.com/posts/bFv8soRx6HB94p5Pg/against-premature-abstraction-of-political-issues), only in the form of assumption choices rather than illustrative-example choices).

I guess in future posts, I could try harder to actively look for illustrative examples that _don't_ narratively support my agenda? (I think I'm already unusually good at this when pursuing what _I_ think of as an "object-level" agenda, but it feels less necessary when pursuing something that I construe as an obvious [common interest of many causes](https://www.lesswrong.com/posts/4PPE6D635iBcGPGRy/rationality-common-interest-of-many-causes), like free speech.) But people often do this social move where they _say_ "I should have tried harder" as a way of accepting blame in exchange for not doing work, so you should only give me credit if you actually see me include counter-narrative examples in future posts; I don't get credit (or as much credit) for merely this comment noticing the problem.

#### [-] Pongo · 5 karma · 2020-05-15 · https://www.lesswrong.com/posts/tCwresAuSvk867rzH/speaking-truth-to-power-is-a-schelling-point?commentId=aCcReLhWGLYjLa2p9
This post argues that the Schelling points are x = 0, and x = ∞, but I think that basically no organisations exist at those Schelling points.

Suppose that most people are disinclined to lie, and are not keen to warp their standards of truth-telling for necessary advantage; but, if the advantage *is* truly necessary ... Then, within a given coalition, those who find out inconvenient truths will indeed distort the shared map by omission and possibly active smoke screens (derisive takedowns of the positions), and those who have not encountered the idea will be kept safe by the deception.

If all the major inconvenient truths are covered, then most within the organisation can hold an idealistic standard of truth-telling, which pushes back against the decay of x.

#### [-] patrickdward · 1 karma · 2022-07-17 · https://www.lesswrong.com/posts/tCwresAuSvk867rzH/speaking-truth-to-power-is-a-schelling-point?commentId=mGJ6LhnAZieJugcBa
It would be easier to follow the argument if you wrote x —> 100% instead of x—> ∞, given the way you define x.

#### [-] patrickdward · 1 karma · 2022-07-17 · https://www.lesswrong.com/posts/tCwresAuSvk867rzH/speaking-truth-to-power-is-a-schelling-point?commentId=Bjim9T4YF2wmJsEHC
Language and norms effectively discretize the 0% to 100% scale such that there can be salient intermediate points.

