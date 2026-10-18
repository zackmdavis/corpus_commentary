Title: Comment on "Propositions Concerning Digital Minds and Society"
LessWrong-URL: https://www.lesswrong.com/posts/nqXcgsqQBw2doAnXu/comment-on-propositions-concerning-digital-minds-and-society
Posted: 2022-07-10
Fetched: 2026-10-13 (LessWrong GraphQL API; rendered by tools/render_lw_threads.py)
Comments: 12 (commentCount field: 12)

#### [-] Yitz · 7 karma · 2022-07-11 · https://www.lesswrong.com/posts/nqXcgsqQBw2doAnXu/comment-on-propositions-concerning-digital-minds-and-society?commentId=n6AdXiHFpjM7znWLN
> we should try to arrange for AIs' deployment environments to be higher-reward than would be expected from their training environment, in analogy to how factory-farms are bad and modern human lives are good by dint of comparison to what was "expected" in the environment of evolutionary adaptedness.

This seems like a really, really good idea, regardless of anything else in the paper. Are there any potential downsides to doing this?

#### [>] Quintin Pope · 2 karma · 2022-07-11 · https://www.lesswrong.com/posts/nqXcgsqQBw2doAnXu/comment-on-propositions-concerning-digital-minds-and-society?commentId=y6s24sScuWjcjAi32
I think it's a type error. It's substituting the selection criteria for the selected values. Current humans are better off because **we** optimized our environments according to **our values**, not because the selection criteria by which our learning process was optimized (inclusive genetic fitness) is more abundant in our modern environment. We're happier because we made ourselves happy, not because we reproduce more in our current environment.

#### [>>] CarlShulman · 5 karma · 2022-07-11 · https://www.lesswrong.com/posts/nqXcgsqQBw2doAnXu/comment-on-propositions-concerning-digital-minds-and-society?commentId=gyx7zmkp85FC7F9jE
The evolutionary mismatch causes differences in neural reward, e.g. eating lots of sugary food still tastes (neurally) rewarding even though it's currently evolutionarily maladaptive. And habituation reduces the delightfulness of stimuli.

#### [>] Kei Nishimura-Gasparian · 14 karma · 2022-07-11 · https://www.lesswrong.com/posts/nqXcgsqQBw2doAnXu/comment-on-propositions-concerning-digital-minds-and-society?commentId=vgy9EnPFLNPCqbFxr
This seems like it would raise the incentive for AGI to be deceptive in their training environments. An un-aligned AGI has the decision of acting to maximize its goals in training and getting a higher short-term reward, or deceptively pretending to be aligned in training, and getting a lower short-term reward. The benefit to the AGI of pretending to be aligned is it increases the probability of it being deployed, and thus being able to get a higher long-term reward in deployment. 

Thus the bigger the discrepancy in reward an AGI would get between deployment environment and training environment, the more important the long-term deployment reward becomes, and the higher the incentive there is of the AGI being deceptive during training.

#### [>>] Daniel Kokotajlo · 5 karma · 2022-07-11 · https://www.lesswrong.com/posts/nqXcgsqQBw2doAnXu/comment-on-propositions-concerning-digital-minds-and-society?commentId=s29BNq8ZBuyn8DFvx
Perhaps the difference made would be small though? Feels like a relatively unlikely sort of situation, in which the AI chooses not to be deceptive but would have chosen to be deceptive if it had calculated that in the brief period before it takes over the world it would be getting 2x reward per second instead of x.

#### [>>>] Yitz · 4 karma · 2022-07-11 · https://www.lesswrong.com/posts/nqXcgsqQBw2doAnXu/comment-on-propositions-concerning-digital-minds-and-society?commentId=uxhWwerTtmqJvziNa
Yeah, intuitively I don’t see that as breaking alignment if it’s already aligned, and an unaligned AI would already have incentive to lie, I think. Considering the potential positive impact this could have qualia-wise, imo it’s a worthwhile practice to carry out.

#### [>>>] Kei Nishimura-Gasparian · 3 karma · 2022-07-11 · https://www.lesswrong.com/posts/nqXcgsqQBw2doAnXu/comment-on-propositions-concerning-digital-minds-and-society?commentId=QPhkK4esYezuXXmn4
My intuition is it should be small in most cases, but there are some scenarios where this could be important.

Let's imagine we are training a reinforcement learning agent AGI that [discounts](https://en.wikipedia.org/wiki/Q-learning#Discount_factor) rewards in time by some parameter d with 0 < d < 1 (so an expected reward r that is gotten n timesteps from now is worth d*r^n at the current time step). Let's further assume the wireheading problem has been solved (the AI can't change the reward calculating process, and give itself, say, infinite reward), and that there is a maximum possible reward of M per time step. This maximum reward could be coded in explicitly in the reward function, or could be implicitly calculated using physical limits.

If deployment is at least b time steps away, the maximum possible deployment reward considering discounting (as calculated at the current time step) is M*d^b/(1-d). If there is any deception the AGI could do that would sacrifice its short-term reward by more than that amount, then it will not do that deception. There seems to be a bit of a tradeoff, where the bigger the multiplier is between the development reward and the training reward, the larger M becomes, and the smaller d needs to be in order to encourage the AGI to engage in non-deceptive behavior.

If we want d to be larger, which will enable an aligned AI to make useful long-term plans, this argument claims we should use a smaller multiplier between development reward and training reward in order for an unaligned AI to be incentived to not deceive us. Alternatively, this argument claims that you should wait a long time between when you test if your model is deceptive and when you deploy it - running a lot of time steps with 0 reward between your deception test and deployment will increase b and thus shrink the size of M*d^b/(1-d), which should make deception much less encouraged.

#### [>>] Lukas Finnveden · 4 karma · 2022-07-11 · https://www.lesswrong.com/posts/nqXcgsqQBw2doAnXu/comment-on-propositions-concerning-digital-minds-and-society?commentId=YXNhP6CDX4DvWXcjn
> An un-aligned AI has the decision of acting to maximize its goals in training and getting a higher short-term reward, or deceptively pretending to be aligned in training, and getting a lower short-term reward.

If there is a conflict between these, that must be because the AI's conception of reward isn't identical to the reward that we intended. So even if we dole out higher intended reward during deployment, it's not clear that that increases the reward that the AI expects after deployment. (But it might.)

#### [>>] Ofer · 1 karma · 2022-07-14 · https://www.lesswrong.com/posts/nqXcgsqQBw2doAnXu/comment-on-propositions-concerning-digital-minds-and-society?commentId=TTHFzuFb5Jm2nGJnE
This concern seems relevant if (1) a discount factor is used in an RL setup (otherwise the systems seems as likely to be deceptively aligned with or without the intervention, in order to eventually [take over the world](https://www.lesswrong.com/posts/nqXcgsqQBw2doAnXu/comment-on-propositions-concerning-digital-minds-and-society?commentId=s29BNq8ZBuyn8DFvx)), and (2) a decision about whether the system is safe for deployment is made based on its behavior during training. 

As an aside, the following quote from the paper seems relevant here:
>Ensuring copies of the states of early potential precursor AIs are preserved to later receive benefits would permit some separation of immediate safety needs and fair compensation.

#### [-] Daniel Kokotajlo · 10 karma · 2022-07-11 · https://www.lesswrong.com/posts/nqXcgsqQBw2doAnXu/comment-on-propositions-concerning-digital-minds-and-society?commentId=2n3Rwj2MCLjAgkQ2L
Good commentary, thanks! I'd be interested to hear your positive proposal for how to do better re conservatism and anthropomorphism. Do you think your objection is more to the style or the substance?

#### [-] Raemon · 8 karma · 2022-07-11 · https://www.lesswrong.com/posts/nqXcgsqQBw2doAnXu/comment-on-propositions-concerning-digital-minds-and-society?commentId=dRN3H6Svr3HxsZemX
I particularly like this paragraph:

> It just doesn't seem like the implications of the differences have *fully propagated* into some of the recommendations?—**as if an attempt to write in a way that's comprehensible to** [**Shock Level 2**](http://sl4.org/shocklevels.html) **tech executives and policymakers has failed to** [**elicit all of the latent knowledge**](https://www.lesswrong.com/tag/eliciting-latent-knowledge-elk) **that Bostrom and Shulman actually possess.** It's understandable that our reasoning about the future often ends up [relying on analogies to phenomena we already understand](https://www.lesswrong.com/posts/MzLxPCF2cMJbMizy9/anchor-weights-for-ml), but ultimately, making sense of a radically different future is going to require new concepts that [won't permit reasoning by analogy](https://www.lesswrong.com/posts/C4EjbrvG3PvZzizZb/failure-by-analogy).

The bolded sentence (emphasis mine) seems plausibly exactly what's going on (curious if Shulman agrees. Or Bostrom, but he seems less likely to comment). 

One of the frightening things to me is that this might actually be the limit of what humanity can coordinate around. (Or rather, I'm frightened that the things humanity can coordinate around are even more weaksauce than the concepts in this doc)

#### [>] Nick Bostrom · 38 karma · 2022-07-12 · https://www.lesswrong.com/posts/nqXcgsqQBw2doAnXu/comment-on-propositions-concerning-digital-minds-and-society?commentId=SukeTCd5JueZqxjvr
You are looking at the wreckage of an abandoned book project.  We got bogged down & other priorities came up.  Instead of writing the book, we decided to just publish a working outline and call it a day.

The result is not particularly optimized for tech executives or policymakers — it’s not really optimized for anybody, unfortunately.

The propositions all \*aspire\* to being true, although some of may not be particularly relevant or applicable in certain scenarios.  Still, there could be value on working out sensible things to say to cover quite a wide range of scenarios, partly because we don’t know which scenario will happen (and there is disagreement over the probabilities), but partly also because this wider structure — including the parts that don’t directly pertain to the scenario that actually plays out — might form a useful intellectual scaffolding, which could slightly constrain and inform people’s thinking of the more modal scenarios.

I think it’s unclear how well reasoning by analogy works in this area.  Or rather: I guess it works poorly, but reasoning deductively from first principles (at SL4, or SL15, or whatever) might be equally or even more error-prone.  So I’ve got some patience for both approaches, hoping the combo has a better chance of avoiding fatal error than either the softheaded or the hardheaded approach has on its own.

