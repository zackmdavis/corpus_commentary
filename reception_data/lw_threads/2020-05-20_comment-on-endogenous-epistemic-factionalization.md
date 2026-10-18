Title: Comment on "Endogenous Epistemic Factionalization"
LessWrong-URL: https://www.lesswrong.com/posts/8cWMX6L8St8k9pPRC/comment-on-endogenous-epistemic-factionalization
Posted: 2020-05-20
Fetched: 2026-10-13 (LessWrong GraphQL API; rendered by tools/render_lw_threads.py)
Comments: 8 (commentCount field: 8)

#### [-] Adele Lopez · 19 karma · 2020-05-20 · https://www.lesswrong.com/posts/8cWMX6L8St8k9pPRC/comment-on-endogenous-epistemic-factionalization?commentId=mK3TeaobiPjZd3GSm
I wonder if this would still happen if say, 1 in 1000 agents will randomly lie about their evidence (always in the same direction), and all agents start with the correct prior on trustworthiness and do the correct update when they disagree. I'd guess that there's some threshold percentage of untrustworthy agents above which you get factions, and below get convergence.

Looking at the picture of the factions, it looks like you can tell (fairly well at least) which corner is correct from the global structure. Maybe there's a some technique you can use in a more general situation to determine what what the correct combination of claims is based on what sort of factions (incl the most likely internal disagreements) are organized around them.

#### [>] gjm · 16 karma · 2020-05-21 · https://www.lesswrong.com/posts/8cWMX6L8St8k9pPRC/comment-on-endogenous-epistemic-factionalization?commentId=cuHiCX6xdavnnrF2W
Relatedly, in the scenario (in some *utterly absurd* counterfactual world *entirely unlike the real world*) where agents sometimes misrepresent the evidence in a direction that favours their actual beliefs, it seems like the policy described here might well do better than the policy of updating fully on all evidence you're presented with.

Given the limitations of our ability to investigate others' honesty, it's possible that the only options are factionalism or naivety and that the latter produces *worse* results than factionalism; e.g., if we happen to start with more people favouring (A,A,A) than (B,B,B) then rejecting "distrust those who disagree" may end up with everyone in the (A,A,A) corner, which is probably worse than having factions in all eight corners if the reality is (B,B,B).

As Zack says, what we want is a degree of trust that matches agents' trustworthiness. But that may be extremely hard to obtain, and if all agents are somewhat untrustworthy (but some happen to be right so that their untrustworthiness does little harm) then having trust matching trustworthiness may produce exactly the sort of factional results reported here.

So I think the most interesting question is: Are there strategies that, even when agents may be untrustworthy in their reporting of the evidence, manage to converge to the truth over a reasonable portion of the space of untrustworthiness and actual-evidence-strength? My guesses: (1) yes, there kinda are, and the price they pay instead of factionalism is slowness; (2) if there is enough untrustworthiness relative to the actual strength of evidence then no strategy will give good results; (3) there are plenty of questions in the real world for which #2 holds. But I'm not terribly confident about any of those guesses.

#### [-] romeostevensit · 10 karma · 2020-05-20 · https://www.lesswrong.com/posts/8cWMX6L8St8k9pPRC/comment-on-endogenous-epistemic-factionalization?commentId=uKwjyqnzKGepL2mBK
Early prior differences based both on genetics and early reinforcement causes low level systems to prioritize sampling over certain domains, time windows, etc. This compounds into paying attention to significantly different aspects of sensory and would still lead to disagreements even if the stimuli subsequently encountered were the same. So most of the polarization is already baked in by the time we get to levels of processing happening within conscious awareness.

Also: agents manipulate access to some forms of evidence in order to collect rents on the information asymmetry.

#### [-] Pongo · 15 karma · 2020-05-21 · https://www.lesswrong.com/posts/8cWMX6L8St8k9pPRC/comment-on-endogenous-epistemic-factionalization?commentId=Z3Npu5ZfWHQxuuRxu
Thank you for sharing your source code! I had fun playing around with it. I decided to see what happened when the agents were estimating B's bias, rather than just if its expectation was higher than A. I started them with a Beta prior, cos it's easy to update.

I found (to my surprise) that when only agents that think B is good try it (as in the setup of the post), [we still only get estimates equal to and below 0.5 + ε!](https://i.imgur.com/73ooGPX.png) This makes sense on reflection: if you look for data when you're one in one direction, you won't end up wrong that way any more (interesting that the factionalization wasn't strong enough to hold people back here; I wonder if this would have been different if the experiments summarised the agent's *updated* beliefs, rather than original beliefs)

Trying to fix this, I decided to think about agents that were trying to establish that B was clearly better or clearly worse than A. One attempt at this was [only testing if B seemed about as good as A in expectation](https://i.imgur.com/3BFimOv.png). This led to a clear cross pointing at the true value. Another attempt was [only testing if the variance in the distribution over B's goodness was high](https://i.imgur.com/kqQBdXv.png). This was very sensitive to the chosen parameters.

#### [-] ligvent · -11 karma · 2020-05-22 · https://www.lesswrong.com/posts/8cWMX6L8St8k9pPRC/comment-on-endogenous-epistemic-factionalization?commentId=D8CyXwz8NrisSodTB
The main direction that has stuck with me is:

"ProGen: Language Modeling for Protein Generation" [https://blog.einstein.ai/progen/](https://blog.einstein.ai/progen/)

#### [-] Raemon · 13 karma · 2020-05-28 · https://www.lesswrong.com/posts/8cWMX6L8St8k9pPRC/comment-on-endogenous-epistemic-factionalization?commentId=uHTPoK9r3awtEzaeG
Curated.

I like that this post took a very messy, complicated subject, and picked one facet of to gain a really crisp understanding of. (MIRI's [2018 Research Direction update](https://intelligence.org/2018/11/22/2018-update-our-new-research-directions/#identifier_5_18363) goes into some thoughts on why you might want to become deconfused on a subject, and the [Rocket Alignment Problem](https://www.lesswrong.com/posts/Gg9a4y8reWKtLe3Tn/the-rocket-alignment-problem) is a somewhat more narrativized version)

I personally suspect that the principles Zack points to here aren't the *primary* principles at play for why epistemic factions form. But, it is interesting to explore that even when you strip away tons of messy-human-specific-cognition (i.e. propensity for tribal loyalty for ingroup protection reasons), a very simple model of purely epistemic agents may still form factions.

I also really liked Zack lays out his reasoning very clearly, with coding steps that you can follow along with. I should admit that I *haven't* followed along all the way through (I got about a third of the way through before realizing I'd need to set aside more time to really process it). So, this curation is not an endorsement that all his coding checks out. The [bar for Curated is, unfortunately, not the bar for Peer Review](https://www.lesswrong.com/posts/brQwWwZSQbWBFRNvh/how-to-use-bureaucracies?commentId=mE6tCDEwPyPZGKnQo#comments). (But! Later on when we get to the 2020 [LessWrong Review](https://www.lesswrong.com/posts/qXwmMkEBLL59NkvYR/the-lesswrong-2018-review), I'd want this sort of thing checked more thoroughly).

It is still relatively uncommon on LessWrong for someone to even rise to the bar of "clearly lays out their reasoning in a very checkable way", and when someone does that while making a point that seems interesting and important-if-true, it seems good to curate it.

#### [>] Zack_M_Davis [AUTHOR] · 4 karma · 2022-01-02 · https://www.lesswrong.com/posts/8cWMX6L8St8k9pPRC/comment-on-endogenous-epistemic-factionalization?commentId=w7XJRcGLphDThj3zr
> lays out his reasoning very clearly [...] the bar for Peer Review

I mean, it's not really _my_ reasoning. This academic-paper-summary-as-blog-post was basically me doing "peer" review for _Synthese_ (because I liked the paper, but was annoyed that someone would publish a paper based on computer simulations without publishing their code).

#### [-] maxflowve2 · 10 karma · 2020-05-29 · https://www.lesswrong.com/posts/8cWMX6L8St8k9pPRC/comment-on-endogenous-epistemic-factionalization?commentId=Et8RcC9XNqkSmCRni
Thanks for the post! I think the ideas here are pretty cool.

However there are some problems with the experiment. 1. The update rule is not bayesian in the sense that if you permute the order of the observations of the experiments, you arrive at different conclusions for each agent (You can test this experimentally easily). This shouldn't happen in a bayesian update. I didn't read the original paper but maybe this is what they meant by the prior of the observations. (ie you probably need a conjugate prior on the belief, which in this case is a beta distribution. But then I'm not sure what the proper way to model the mistrust factor is.)

2\. We allow mistrust factor to be exactly 1, which means that the agent ignores the evidence from that reporter completely. This may or may not be appropriate... I can see both sides of the argument. But if we constrain the mistrust factor to be at most 1-eps, then with enough observations everyone will eventually converge to the correct beliefs.

Note that another way to correct of your own mistaken belief even if you distrust everyone is to do the experiments yourself (You have to trust yourself at least?). It's okay to not directly adjust your belief (ie: action A is better) based on evidence from people you don't like but it still makes sense to let the evidence lower the degree of certainty in your own beliefs (ie: I'm 60% certain that action A is better). Decision making should take into account of this degree of uncertainty. If all agents who currently believe that action A is better give action B a try once in a while, the entire community probably converges a lot faster too.

