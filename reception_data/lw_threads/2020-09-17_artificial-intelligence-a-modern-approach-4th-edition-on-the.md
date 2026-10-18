Title: Artificial Intelligence: A Modern Approach (4th edition) on the Alignment Problem
LessWrong-URL: https://www.lesswrong.com/posts/BNJx2CqfXyiusoJcK/artificial-intelligence-a-modern-approach-4th-edition-on-the
Posted: 2020-09-17
Fetched: 2026-10-13 (LessWrong GraphQL API; rendered by tools/render_lw_threads.py)
Comments: 12 (commentCount field: 12)

#### [-] TurnTrout · 8 karma · 2020-09-17 · https://www.lesswrong.com/posts/BNJx2CqfXyiusoJcK/artificial-intelligence-a-modern-approach-4th-edition-on-the?commentId=K4BA4XzDGtzfpEcZ8
> In Chapter 16, we show that a machine has a positive incentive to allow itself to be switched off **if and only if** it is uncertain about the human objective.

Surely he only meant *if* it is uncertain?

#### [>] abramdemski · 5 karma · 2020-09-17 · https://www.lesswrong.com/posts/BNJx2CqfXyiusoJcK/artificial-intelligence-a-modern-approach-4th-edition-on-the?commentId=29LPhMRKzpnhAtnZr
If it's certain about the human objective, then it would be certain that it knows what's best, so there would be no reason to let a human turn it off. (Unless humans have a basic preference to turn it off, in which case it could prefer to be shut off.)

#### [>>] TurnTrout · 4 karma · 2020-09-17 · https://www.lesswrong.com/posts/BNJx2CqfXyiusoJcK/artificial-intelligence-a-modern-approach-4th-edition-on-the?commentId=D6fCLbmADAyxz9KKX
We know of many ways to get shut-off incentives, including the indicator utility function on being shut down by humans (which theoretically exists), and the [AUP penalty term, which strongly incentivizes accepting shutdown](https://arxiv.org/pdf/1902.09725.pdf) in certain situations - without even modeling the human. So, it's not an if-and-only-if.

#### [>>>] abramdemski · 2 karma · 2020-09-17 · https://www.lesswrong.com/posts/BNJx2CqfXyiusoJcK/artificial-intelligence-a-modern-approach-4th-edition-on-the?commentId=DkWRn2fNf6gpoX3DC
Sure, but the theorem he proves in the setting where he proves it probably *is* if and only if. (I have not read the new edition, so, not really sure.)

It also seems to me like Stuart Russell endorses the if-and-only-if result as what's desirable? I've heard him say things like "you want the AI to prevent its own shutdown when it's sufficiently sure that it's for the best".

Of course that's not technically the full if-and-only-if (it needs to both be certain about utility *and* think preventing shutdown is for the best), but it suggests to me that he *doesn't* think we should add more shutoff incentives such as AUP.

Keep in mind that I have fairly little interaction with him, and this is based off of only a few off-the-cuff comments during CHAI meetings.

My point here is just that it seems pretty plausible that he meant "if and only if".

#### [>>>>] TurnTrout · 4 karma · 2020-09-17 · https://www.lesswrong.com/posts/BNJx2CqfXyiusoJcK/artificial-intelligence-a-modern-approach-4th-edition-on-the?commentId=eCf4o7WnTaN9DQkyF
> My point here is just that it seems pretty plausible that he meant "if and only if".

Sure. To clarify: I'm more saying "I think this statement is wrong, and I'm surprised he said this". In fairness, I haven't read the mentioned section yet either, but it is a very strong claim. Maybe it's better phrased as "a CIRL agent has a positive incentive to allow shutdown iff it's uncertain \[or the human has a positive term for it being shut off\]", instead of "a machine" has a positive incentive iff.

#### [>>>>>] Zack_M_Davis [AUTHOR] · 6 karma · 2020-09-18 · https://www.lesswrong.com/posts/BNJx2CqfXyiusoJcK/artificial-intelligence-a-modern-approach-4th-edition-on-the?commentId=NrMxmw6gXsJjx9Nps
It is an "iff" in §16.7.2 "Deference to Humans", but the toy setting in which this is shown is pretty impoverished. It's a story problem about a robot Robbie deciding whether to book an expensive hotel room for busy human Harriet, or whether to ask Harriet first.

> Formally, let $P(u)$ be Robbie's prior probability density over Harriet's utility for the proposed action _a_. Then the value of going ahead with _a_ is
>
> $$EU(a) = \int_{-\infty}^{\infty} P(u) \cdot u \; du = \int_{-\infty}^{0} P(u) \cdot u \; du + \int_{0}^{\infty} P(u) \cdot u \; du$$
>
> (We will see shortly why the integral is split up this way.) On the other hand, the value of action _d_, deferring to Harriet, is composed of two parts: if _u_ > 0 then Harriet lets Robbie go ahead, so the value is _us_, but if _u_ < 0 then Harriet switches Robbie off, so the value is 0:
>
> $$EU(d) = \int_{-\infty}^{0} P(u) \cdot 0 \; du + \int_{0}^{\infty} P(u) \cdot u \; du$$
>
> Comparing the expressions for _EU(a)_ and _EU(d)_, we see immediately that
>
> $$EU(d) \ge EU(a)$$
>
> because the expression for _EU(d)_ has the negative-utility region zeroed out. The two choices have equal value only when the negative region has zero probability—that is, when Robbie is already certain that Harriet likes the proposed action.

(I think this is fine as a topic-introducing story problem, but agree that the sentence in Chapter 1 referencing it shouldn't have been phrased to make it sound like it applies to machines-in-general.)

#### [>>>>>] abramdemski · 4 karma · 2020-09-18 · https://www.lesswrong.com/posts/BNJx2CqfXyiusoJcK/artificial-intelligence-a-modern-approach-4th-edition-on-the?commentId=rWsRAvAWw9Rd8N7mj
> Maybe it's better phrased as "a CIRL agent has a positive incentive to allow shutdown iff it's uncertain \[or the human has a positive term for it being shut off\]", instead of "a machine" has a positive incentive iff.

I would further charitably rewrite it as:

"In chapter 16, we analyze an incentive which a CIRL agent has to allow itself to be switched off. This incentive is positive if and only if it is uncertain about the human objective."

A CIRL agent should be capable of believing that humans terminally value pressing buttons, in which case it might allow itself to be shut off despite being 100% sure about values. So it's just *the particular incentive examined* that's iff.

#### [>] habryka · 7 karma · 2020-09-17 · https://www.lesswrong.com/posts/BNJx2CqfXyiusoJcK/artificial-intelligence-a-modern-approach-4th-edition-on-the?commentId=n45udqEEcBYYto6pC
This sentence really makes no sense to me. The proof that it can have an incentive to allow itself to be switched off even if it isn't uncertain is trivial. 

Just create a utility function that assigns intrinsic reward to shutting itself off, or create a payoff matrix that punishes it really hard if it doesn't turn itself off. In this context using this kind of technical language feels actively deceitful to me, since it's really obvious that the argument he is making in that chapter cannot actually be a proof. 

In general, I... really don't understand Stuart Russell's thoughts on AI Alignment. The whole "uncertainty over utility functions" thing just doesn't really help at all with solving any part of the AI Alignment problem that I care about, and I do find myself really frustrated with the degree to which both this preface and Human Compatible repeatedly indicate that it somehow is a solution to the AI Alignment problem (not only like, a helpful contribution, but both this and Human Compatible repeatedly say things that to me read like "if you make the AI uncertain about the objective in the right way, then the AI Alignment problem is solved", which just seems obviously wrong to me, since it doesn't even deal with inner alignment problems, and it also doesn't solve really any major outer alignment problems, but that requires a bit more writing).

#### [>>] peterbarnett · 3 karma · 2020-09-18 · https://www.lesswrong.com/posts/BNJx2CqfXyiusoJcK/artificial-intelligence-a-modern-approach-4th-edition-on-the?commentId=F3JsDHPwv4jerSrYF
My read of Russel's position is that if we can successfully make the agent uncertain about its model for human preferences then it will defer to the human when it might do something bad, which hopefully solves (or helps with) making it corrigible.

I do agree that this doesn't seem to help with inner-alignment stuff though, but I'm still trying to wrap my head around this area.

#### [-] Zack_M_Davis [AUTHOR] · 8 karma · 2020-09-18 · https://www.lesswrong.com/posts/BNJx2CqfXyiusoJcK/artificial-intelligence-a-modern-approach-4th-edition-on-the?commentId=pGoyqBpidcWpLjiTm
Can I also point to this as (some amount of) evidence against concerns that "we" (members of this stupid robot cult that I continue to feel contempt for but [don't know how to quit](https://www.lesswrong.com/posts/xqAnKW46FqzPLnGmH/causal-reality-vs-social-reality?commentId=rFbEJSttPFkmSG6Nw)) shouldn't try to have systematically truthseeking discussions about potentially sensitive or low-status subjects because guilt-by-association splash damage from those conversations will hurt AI alignment efforts, which are the most important thing in the world? (Previously: [1](https://www.lesswrong.com/posts/P3FQNvnW8Cz42QBuA/dialogue-on-appeals-to-consequences?commentId=Z8haBdrGiRQcGSXye) [2](https://www.lesswrong.com/posts/yaCwW8nPQeJknbCgf/free-speech-and-triskaidekaphobic-calculators-a-reply-to) [3](https://www.lesswrong.com/posts/ayTCRYJ7sB65oGuzB/my-dating-plan-ala-geoffrey-miller?commentId=Ffhv7o47cFZb55mFm).)

Like, I agree that some nonzero amount of splash damage exists. But look! _The_ most popular AI textbook, used in almost _fifteen hundred_ colleges and universities, clearly explains the paperclip-maximizer problem, in the _authorial voice_, in the _first chapter_. "_These behaviors are not 'unintelligent' or 'insane'; they are a logical consequence of defining winning as the_ sole _objective for the machine._" Italics in original! I couldn't transcribe it, but there's even one of those pay-attention-to-this triangles (◀) in the margin, in _teal ink_.

![](https://i.imgur.com/xYhTvVr.jpg)

Everyone who gets a CS degree from this year onwards is going to know from the teal ink that there's a problem. If there _was_ a [marketing war](https://www.lesswrong.com/posts/Zvu6ZP47dMLHXMiG3/optimized-propaganda-with-bayesian-networks-comment-on) to legitimize AI risk, we _won_! Now can "we" please stop using the marketing war as an excuse for lying?!

#### [>] steven0461 · 14 karma · 2020-09-18 · https://www.lesswrong.com/posts/BNJx2CqfXyiusoJcK/artificial-intelligence-a-modern-approach-4th-edition-on-the?commentId=6snriTihReFnKJ7tA
some predictable counterpoints: maybe we won because we were cautious; we could have won harder; many relevant thinkers still pooh-pooh the problem; it's not just the basic problem statement that's important, but potentially many other ideas that aren't yet popular; picking battles isn't lying; arguing about sensitive subjects is fun and I don't think people are very tempted to find excuses to avoid it; there are other things that are potentially the most important in the world that could suffer from bad optics; I'm not against systematically truthseeking discussions of sensitive subjects, just if it's in public in a way that's associated with the rationalism brand

#### [>>] Zack_M_Davis [AUTHOR] · 11 karma · 2020-09-28 · https://www.lesswrong.com/posts/BNJx2CqfXyiusoJcK/artificial-intelligence-a-modern-approach-4th-edition-on-the?commentId=FoKz42oeRKd9yfyfj
(This extended runaround on [appeals to consequences](https://www.lesswrong.com/posts/P3FQNvnW8Cz42QBuA/dialogue-on-appeals-to-consequences) is at least a neat microcosm of the reasons we expect unaligned AIs to be [deceptive by default](https://arbital.greaterwrong.com/p/programmer_deception)! Having the [intent to inform](http://benjaminrosshoffman.com/honesty-and-perjury/#Intent_to_inform) other agents of what you know without trying to [take responsibility](http://benjaminrosshoffman.com/against-responsibility/) for controlling their decisions is an [unusually anti-natural shape for cognition](https://www.lesswrong.com/posts/Djs38EWYZG8o7JMWY/paul-s-research-agenda-faq?commentId=79jM2ecef73zupPR4); for generic consequentialists, [influence-seeking behavior](https://www.lesswrong.com/posts/HBxe6wdjxK239zajf/what-failure-looks-like#Part_II__influence_seeking_behavior_is_scary) is the default.)

