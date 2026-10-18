Title: Unnatural Categories Are Optimized for Deception
LessWrong-URL: https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception
Posted: 2021-01-08
Fetched: 2026-10-13 (LessWrong GraphQL API; rendered by tools/render_lw_threads.py)
Comments: 32 (commentCount field: 32)

#### [-] Zack_M_Davis [AUTHOR] · 6 karma · 2021-01-08 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=WyMavMaZ6iKo9y2XD
***Author's Meta Note***

(I continue to maintain that this is fun and basic hidden-Bayesian-structure-of-language-and-cognition stuff that _shouldn't_ be "political", but—if we need it—the ["Containment Thread on the Motivation and Political Context for My Philosophy of Language Agenda"](https://www.lesswrong.com/posts/5aqumaym7Jd2qhDcy/containment-thread-on-the-motivation-and-political-context) is now available for talking about the elephant in the room.)

(I intend to _eventually_ reply to all substantive critical comments on this post and the containment thread, but I might be very _slow_ to respond due to life events and priorities outside of this website. Your patience is deeply appreciated.)

#### [-] Zack_M_Davis [AUTHOR] · 0 karma · 2021-01-08 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=w4DSBFn5teoPdW8Md
Mods: I'm confused that this isn't showing up in "Latest" even when I set "Personal Blog" to "Required" in a Private-mode window?! Could the algorithm be using "created by" date rather than "published on" date (an earlier version was sitting as a draft for a few months so I could preview some LaTeX), or ...?!

#### [>] Raemon · 2 karma · 2021-01-08 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=LTDLWxqqQdDHLyYrk
Hmm. If you had ever published it briefly that might be why? We’ll look into it.

#### [>] DanielFilan · 2 karma · 2021-01-08 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=2gSTwWGzcZCwkz5sF
FYI it currently shows up for me.

#### [-] Raemon · 5 karma · 2021-01-08 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=dnuBuPeZQNRweSXED
I don’t know how cruxy this is for the main points of the post. I did find this post quite helpful overall. I quite liked that the final section explored real world examples that showed where this actually mattered. 

But fwiw I mostly had _not_ been thinking of the squiggly bordered nations as a metaphor for squiggly bordered concepts. Or, maybe I had, but, *also* I think ‘where is this nations border?’ an actually important question. The section that just dismissed that as metaphor was fairly surprising and disappointing to me, since that was an objection I’d been particularly interested in. (In particular because it was the initial framing question for the post)

#### [-] johnswentworth · 14 karma · 2021-01-08 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=FqjsM2AkEkaBgf2wD
This comment is mostly a placeholder for a post I owe you on how words work, and in particular the "rules of the game" for socially-constructed categories. I'll just give a few quick high-level descriptions on how the models in that eventual post diverge from the models here. Apologies in advance for not-very-good explanations.

First, "clusters in thingspace" is a metaphor. There isn't really a canonical "thingspace" with pre-defined features along the axes; figuring out what features to use is most of the problem from the start. So, what is the (mathematical) concept for which "clusters in thingspace" is a metaphor? I think the main answer here is conditional independence. The defining feature of a cluster (under the usual Bayesian setup) is that the points comprising the cluster are independent *given* the summary statistics of the cluster itself. Likewise for the concepts to which we attach words: the concept-of-tree contains/points to all the summary data about particular trees which is relevant to other trees, making each tree independent *given* the tree-summary-statistics. For complicated real-world objects like trees, those summary statistics are high-dimensional and no human even knows all of them, but they're still a lot lower dimensional then all the atoms in any particular tree.

Now, we combine that with the [natural abstractions hypothesis](https://www.lesswrong.com/posts/Nwgdq6kHke5LY692J/alignment-by-default#Unsupervised__Natural_Abstractions), which in this context basically says that natural-concept-space is (approximately) discrete rather than continuous. Natural concepts are not arbitrarily close together. If the concept of "tree" points to the summary statistics of bunch of correlated chunks of the world, inducing independence between those chunks with minimal extraneous info, then there is not another arbitrarily-close summary/concept which *also* induces independence with minimal extraneous info. This is the key property which lets people reasonably-confidently "talk about the same thing" without needing infinitely many examples to coordinate.

So those are the rough rules governing words.

To talk about "rules of the game" for socially-constructed categories, the next step is [Parable of the Dammed](https://www.lesswrong.com/posts/FbJYEn6eWA5JnGeGP/parable-of-the-dammed) \- I had intended to include that in the eventual post on how words work, but ended up spinning it off. The main idea there is that people can move around Schelling points by changing the underlying territory. In the case of words, the Schelling points are the natural concepts - minimal summary data which induces independence between different chunks of the world. So, the "game" is to move around those natural concepts - i.e. make some other information necessary to induce independence between world-chunks.

In particular, an interesting way to do this is to create new chunks which partially match the old natural concept. In the cluster analogy, this would mean adding new points within the cluster but biased toward one particular side. (In the trees example: we could imagine creating new tree species, or driving old tree species to extinction, or dramatically shifting the mix of trees.) Then humans get to debate whether these new points should "count" or not - the old points are still independent under the old concept-definition, but making the new points also independent requires adding new information to the concept, and some might even advocate for ignoring some of the old points and just making the concept induce independence on the new points.

As for unnatural categories...

Once we have the idea that natural concept space is discrete, and natural concepts are Schelling points for words, then the questions around unnatural categories are:

*   is the unnatural category a Schelling point at all?
*   if so, how are people recognizing the Schelling point, rather than as a natural concept?

In some cases, the unnatural category might just not be a Schelling point at all. We could imagine a variant of the gold/silver bars example where people have actually-different ideas of what the words mean, so maybe there just isn't a Schelling point and people entering contracts will need to meet the legal requirements for a "meeting of minds" some other way - i.e. writing definitions out in excruciating detail.

Alternatively, the Schelling point can be established via some mechanism other than natural concepts - e.g. passing laws about what a word means, establishing norms, etc. (Though note that these mechanisms still need some way of dealing with the very high dimensionality of word-specification space; there still needs to be some efficient way to coordinate on a high-dimensional word-meaning, so it will probably eventually ground out in other natural concepts.)

#### [>] Zack_M_Davis [AUTHOR] · 8 karma · 2021-03-19 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=JhBBeXtNZnNtPZrSh
(Thinking out loud about how my categorization thing will end up relating to [your abstraction thing](https://www.lesswrong.com/posts/vDGvHBDuMtcPd8Lks/public-static-what-is-abstraction) ...)

200-word recap of my thing: I've been relying on our [standard configuration space metaphor](https://www.lesswrong.com/posts/WBw8dDkAWohFjWQSk/the-cluster-structure-of-thingspace), talking about running some "neutral" clustering algorithm on some choice of subspace (which is "value-laden" in the sense that what features you care about predicting depends on your values). This lets me explain [how to think about dolphins](https://www.lesswrong.com/posts/aMHq4mA2PHSM2TMoH/the-categories-were-made-for-man-not-man-for-the-categories): they simultaneously cluster with fish in one subspace, but also cluster with other mammals in a different subspace, no contradiction there. It also lets me explain [what's wrong with a fake promotion to "Vice President of Sorting"](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries): the "what business cards say" dimension is a very "thin" subspace; if it doesn't cluster with anything _else_, then there's no reason we care. As my measurement of what makes a cluster "good", I'm using the squared error, which is pretty "standard"—that's _basically_ what, say, [_k_ means clustering](https://en.wikipedia.org/wiki/K-means_clustering) is doing—but also pretty _ad hoc_: I don't have a proof of why squared error and _only_ squared error is the _right_ calculation to be doing given some simple deciderata, and it probably isn't. (In contrast, we can _prove_ that [if you want a monotonic, nonnegative, additive measure of information, you end up with entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)#Characterization): the only free choice is the base of the logarithm.)

What I'm hearing from the parent and [your reply to my comment on "... _Ad Hoc_ Mathematical Definitions?"](https://www.lesswrong.com/posts/GhFoAxG49RXFzze5Y/what-s-so-bad-about-ad-hoc-mathematical-definitions?commentId=yXKhkvookgLSaCis9): talking about looking for clusters in some pre-chosen subspace of features is getting the actual AI challenge backwards. There are no pre-existing features in the territory; rather, conditional-independence structure in the territory is what lets us construct features _such that_ there are clusters. Saying that we want categories that cluster in a "thick" subspace that covers many dimensions is like saying we want to measure information with ["a bunch of functions like $X^2$, sin(Y), $e^X+2X-1$, _&c._, and require that those _also_ be uncorrelated"](https://www.lesswrong.com/posts/GhFoAxG49RXFzze5Y/what-s-so-bad-about-ad-hoc-mathematical-definitions): it probably _works_, but there has to be some deeper principle that explains _why_ most of the dimensions and _ad hoc_ information measures agree, why we _can construct_ a "thick" subspace.

To explain why "squiggly", "gerrymandered" categories are bad, I said that if you needed to make a decision that depended on how big an integer is, categorizing by parity would be bad: the squared-error score quantifies the fact that 2 is more similar to 3 than 12342. But notice that the choice of feature (the decision quality depending on magnitude, not parity) is doing _all_ the work: 2 _is_ more similar to 12342 than 3 _in the mod-2 [quotient space](https://en.wikipedia.org/wiki/Quotient_space_(linear_algebra))!_

So maybe the exact measure of "closeness" in the space (squared error, or whatever) is a red herring, an _uninteresting_ part of the problem?—like the choice of logarithm in the definition of entropy. We _know_ that there _isn't_ any principled reason why base 2 or base _e_ is better than any others. It's just that we're talking about how uncertainty relates to information, so if we use our standard representation of uncertainty as probabilities from 0 to 1 under which independent events multiply, then we have a homomorphism from multiplication (of probability) to addition (of information), which means you have to pick a base for the logarithm if you want to work with concrete numbers instead of abstract nonsense.

_If_ this is a good analogy, then we're looking for some sort of deeper theorem about "closeness" and conditional independence "and stuff" that explains why the configuration space metaphor _works_—after which we'll be able to show that the choice of metric on the "space" will be _knowably_ arbitrary??

#### [>>] johnswentworth · 12 karma · 2021-03-19 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=k7BQbYSFgkrjwNynp
Yup, this seems basically right.

I have a (still incomplete) draft [here](https://docs.google.com/document/d/1mnVk065HrYFM-P9JAJhfVx5gvtYJrb43o3y9ZqbRwTU/edit?usp=sharing) which specifically addresses why the configuration space metaphor works. Short version: the key property of (Bayesian) clustering is that the points in a cluster are conditionally independent given the summary data of the cluster. For instance, if I have Gaussian clusters, then each point within a given cluster is independent *given* the mean and variance of that cluster. The prototypical "clustering problem" is to assign points to clusters in such a way that this works. So, for instance, the Gaussian clustering problem is to assign points to clusters in such a way that the points in each cluster are independent given the cluster mean and variance. Since the Gaussian distribution is maxentropic subject to mean and variance constraints (i.e. it is the unique distribution for which mean and variance are sufficient statistics), this fully characterizes Gaussian clustering.

Generalizing to the "object type discovery" problem of abstraction, we want to find sets of chunks-of-the-world which are independent given some summary statistics of the chunks. So the analogy is quite strong -  in fact, Bayesian clustering isn't just an analogy, it's an example of the problem (albeit with some additional assumptions typically thrown in, e.g. about the specific forms of the clusters).

BTW, if you buy this view and figure out a good way to explain it, you are more-than-welcome to take whatever you want from that draft and scoop me on it.

#### [>>>] Zack_M_Davis [AUTHOR] · 2 karma · 2021-03-19 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=Lsq6x5GtuuNuZgebb
So, I like this, but I'm still not sure I understand where features come from.

Say I'm an AI, and I've observed a bunch of sensor data that I'm representing internally as the points `(6.94, 3.96), (1.44, -2.83), (5.04, 1.1), (0.07, -1.42), (-2.61, -0.21), (-2.33, 3.36), (-2.91, 2.43), (0.11, 0.76), (3.2, 1.32), (-0.43, -2.67)`.

The part where I look at this data and say, "Hey, these datapoints become approximately conditionally independent if I assume they were generated by a multivariate normal with mean `(2, -1)`, and covariance matrix `[[16, 0], [0, 9]]`[^generation]; let me allocate a new concept for that!" makes sense. (In the real world, I don't know how to write a program to do this _offhand_, but I know how to find what textbook chapters to read to tell me how.)

But what about the part where my sensor data came to me already pre-processed into the list of 2-tuples?—how do I learn _that_? Is it just, like, whatever transformations of a big buffer of camera pixels let me find conditional independence patterns probably correspond to regularities in the real world? Is it "that easy"??

[^generation]: In the real world, I got those numbers from the Python expression `', '.join(str(d) for d in [(round(normal(2, 4), 2), round(normal(-1, 3), 2)) for _ in range(10)])` (using `scipy.random.normal`).

#### [>>>>] johnswentworth · 11 karma · 2021-03-19 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=FXXRMEcQ3GrfFj6Xw
> Is it just, like, whatever transformations of a big buffer of camera pixels let me find conditional independence patterns probably correspond to regularities in the real world? Is it "that easy"??

Roughly speaking, yes.

Features are then typically the summary statistics associated with some abstraction. So, we look for features which induce conditional independence patterns in the big buffer of camera pixels. Then, we look for higher-level features which induce conditional independence between those features. Etc.

#### [>>>>>] Zack_M_Davis [AUTHOR] · 4 karma · 2021-03-20 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=w2kmjTe9E6EqtWztA
This gave me a blog story idea!

#### [>>>>>>] johnswentworth · 6 karma · 2021-03-20 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=djMkgsTupytigKmet
![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/89e990b5978c7c5e298876a252553c82fea762724219c0db.png)

It's not that LW doesn't have emoji reactions. It's just that it has to be worth a BIG emoji reaction.

#### [>>>>>>>] Zack_M_Davis [AUTHOR] · 5 karma · 2021-11-01 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=wM9YLrDCvJQEpteHX
["Feature Selection"](https://www.lesswrong.com/posts/dYspinGtiba5oDCcv/feature-selection)

#### [>>>>>] tailcalled · 3 karma · 2021-03-22 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=co6e6Wvb356L5vcWw
It's funny that you should mention this, because I've considered working on a machine learning system for image recognition using this principle. However, I don't think this is necessarily all of it. I bet we come pre-baked with a lot of rules for what sorts of features to "look for". To give an analogy to machine learning, there's an algorithm called pi-GAN, which comes pre-baked with the assumption that pictures originate from 3D scenes, and which then manages to learn 3D scenes from the 2D images it is trained with. (Admittedly only when the images are particularly nice.)

#### [>>>] tailcalled · 5 karma · 2021-03-22 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=87gfkgetbdRYNM4nj
Your model uses correlational notions like "conditional independence" to make sense of it. But I think one could perhaps come with an alternate model using causal notions?

Specifically: If two variables X and Y are correlated, then they usually are so due to confounding, because there are a lot more ways that things can be confounded than that they can be causally related. So it makes sense to assume that they are confounded.

You could approximate all of the confounders of a suitably chosen set of observable variables by postulating a new variable, which affects all of the observables. This confounder then turns into your feature axis (if continuous) or cluster (if discrete).

#### [>>>>] johnswentworth · 2 karma · 2021-03-22 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=MPGBBTLd3amgq8R5K
This is exactly right; we can interpret the abstraction model essentially along these lines as well.

#### [-] romeostevensit · 4 karma · 2021-01-09 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=KM7nciqH9AFQdgPun
Audio compression libraries aren't image compression libraries. Simulacra level 1 compression libraries aren't Simulacra level 3 libraries. So I might say compression libraries are teleologically situated. Purpose space is upstream of concept and thing-space. This leads to confusion about reductionism vs idealism but that's just because of how we're wired.

#### [-] DanielFilan · 5 karma · 2021-01-09 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=LTj5N8jSpzp2vfYNo
> If we just pay attention to the evidential entanglements instead of being confused by words, then there's no functional difference between saying "I reserve the right to lie p% of the time about whether something belongs to category C", and adopting a new, less-accurate category system that misclassifies p% of instances with respect to the old system.

It is true that there is a version of re-drawing the categories and lying a proportion of the time that are functionally identical. But I think that many cases are in fact not functionally identical. Suppose I say "I've decided to use the word 'book' for what you used to call books, and also vegan chocolate bars". Well now you're less sure what I'm talking about when I say the word 'book' and don't know whether reading or eating is the appropriate response to receiving one, but you still have a decent sense. Now, instead, suppose I say "I'm going to use the word 'book' for what you used to call books, but also a small number of random other things". Now you have much less idea what I'm talking about when I talk about 'books'! Maybe they could kill you! I could change on-the-spot my categorization system without contradicting what I said, and the 'fake books' could be a variety of crazy different things rather than all coming from the same old category. To me, this seems basically like a case of [blatant lies being the best kind](https://www.lesswrong.com/posts/KzAG4yWQJosmEjHe2/blatant-lies-are-the-best-kind).

#### [-] Slider · 0 karma · 2021-01-10 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=uRqG29AJfmZqqHqSv
It seems to me that the reason why the non-gerry mandered concept is preferable is connected to drill wearyness being very linear in original observables. In my own mouth i would say that drill weariness is measured in "toughness" and if eggness is a good proxy for "toughness" then it might make sense to configure the drill to be "expecting" an eggness score. Whether a drill wears out seems to ambivalent about the signaling used. This makes it okay to use to judge a signaling scheme. But how would you balance the dye machine weariness against drill weariness? It would seem there would exist a signaling scheme that is optimal in weariness times the cost of replacement of the machine. And this would not be optimal in respect to only one machine type.

One could also hypothetise that toughness is squiggly in eggness. Maybe even numbered eggnesses are tough and odd numbered eggnesses are soft. Overusing the mean squared error might be making the assumption that small deviation in your sensory organs would correspond to small deviations in your decision efficiency. In a way this might be plausible, it is more easy to be a prosperous animal if you have sensory organs that are easy to make life-promoting choices in. But in another way it is implausible. Sensory organs have trigger conditions defined in conditions that are in respect to their structure while most decisions to be made are structured differently than your bodily organs. It is rare for "see red" -> "eat","see blue"->"don't eat" to be the dominant strategy.

If you are a limited vision seer that hears well (such as a bat) and deal with a four color seer that hears less well (such as a ultraviolet seeing bird) does that mean that bird concepts are deceptive to you as a bat? If one would hope there would be one set of concepts that would be optimal for both bats and birds that might not be the case. But if the bat and the bird agree on what batness is and what birdness is there shouldn't be disagreement about suitability, it just doesn't form a uniform ladder.

#### [-] tailcalled · 2 karma · 2022-07-06 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=2WiQmKYaFbpXjpux9
One problem with mean squared error as a measure of communication accuracy is that it gives no incentive to accurately communicate the variance around the stated outcome. That is, suppose you are creating some precise electronics equipment where it is very important that you work with pure gold. In that case, you don't just want the buyer to choose the description that minimizes the squared error (perhaps "1 kg pure gold"), but instead a description that minimizes e.g. negative log probability (perhaps "0.999-1.001 kg pure gold, 0.001 kg misc contaminants").

Negative log probability is equivalent to squared error when working with univariate normal distributions with a fixed standard deviation/variance structure. (Proof: just take the logarithm of the normal distribution pdf and reduce the expression.) However, when working with distributions with varying variances, or with non-normal distributions, talking about negative log prob could be said to give better incentives for some aspects of information.

(There's probably even better approaches if one e.g. takes into account the likely effects of the information. While your approach fails to give an incentive to accurately communicate uncertainty, your approach is better at incentivizing coming up with a categorization system that doesn't lump things together if they behave differently (assuming the metric chosen in the beginning is sensible), perhaps taking into account the effects of the information could give the best of both worlds, incorporating both uncertainty and lumping.)

#### [>] tailcalled · 2 karma · 2022-07-06 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=beQangk43ANbRfBM4
Most practical purposes that one might have for things probably satisfy some sort of convexity property: if 0.999 kg gold is OK, and 1.001 kg gold is OK, then 1.000 kg gold is also OK.

Insofar as this is true, restricting oneself to some notion of convex probability distribution might be useful.

#### [-] iceman · 37 karma · 2022-12-09 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=eBgiESoE4oprBxoWq
Zack's series of posts in late 2020/early 2021 were really important to me. They were a sort of return to form for LessWrong, focusing on the valuable parts.

What are the parts of The Sequences which are still valuable? Mainly, the parts that build on top of Korzybski's General Semantics and focus hard core on map-territory distinctions. This part is timeless and a large part of the value that you could get by (re)reading The Sequences today. Yudkowsky's credulity about results from the social sciences and his mind projection fallacying his own mental quirks certainly hurt the work as a whole though, which is why I don't recommend people read the majority of it.

The post is long though, but it kind of has to be. For reasons not directly related to the literal content of this essay, people seem to have collectively rejected the sort of map-territory thinking that we should bring from The Sequences into our own lives. This post has to be thorough because there are a number of common rejoinders that have to be addressed. This is why I think this post is better for inclusion than something like [Communication Requires Common Interests or Differential Signal Costs](https://www.lesswrong.com/posts/ybG3WWLdxeTTL3Gpd/communication-requires-common-interests-or-differential), which is much shorter, but only addresses a subset of the problem.

Since the review instructions ask how this affected my thinking, well...

Zack writes generally, but he writes __because__ [he believes people are not correctly reasoning in a current politically contentious topic](https://www.lesswrong.com/posts/5aqumaym7Jd2qhDcy/containment-thread-on-the-motivation-and-political-context). But that topic is sort of irrelevant: the value comes in pointing out that high status members of the rationalist community are completely flubbing lawful thinking. That made it __thinkable__ that actually, they might be failing in other contexts.

Would I have been receptive to Christiano's point that MIRI doesn't actually have a good prediction track record had Zack not written his sequence on this? That's a hard counterfactual, especially since I had already lost a ton of respect for Yudkowsky by this point, in part because of the quality of thought in his other social media posting. But I think it's probable enough and these series of posts certainly made the thought more available.

#### [-] Wei Dai · 9 karma · 2024-01-18 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=bTiqGbH53qH2czjbM
I think there is at least one other, more benign objective that "unnatural categories" are sometimes optimized for. Consider this example. Today we have electrical and fuel burning fireplaces. One day someone invents a "neural fireplace", a device that if installed in a home, remotely induces in everyone a realistic hallucination of a fireplace. Let's say that most people agree that (ignoring costs) these are close substitutes as far as their utility functions are concerned, such that people regularly say to their architects "please include a fireplace in my house" and it's assumed to mean putting in any one of the three types of devices in the building plans while minimizing overall cost. I think you'll agree that "fireplace" here is "unnatural" but also there's no deception happening?

To generalize from this, it seems that when different natural categories are close substitutes in many people's utility functions, it would make sense to assigned them a common codeword, to aid communication efficiency when transmitting instructions. Given this, I think "trans women are women" isn't necessarily motivated by deception of which sex cluster someone belongs to, but instead a signal of local values, trying to imply something like "people around here do not distinguish between trans women and cis women in their values, at least in most circumstances". This could still be a deception (it's costly to use the same codeword for two categories if they're not actually close substitutes, but it could be worth paying this price in order to hide your real values), but it would be mainly a deception about values, not about sex, and it would require investigating people's actual values to determine whether the signal is really deceptive or not.

#### [>] Zack_M_Davis [AUTHOR] · 7 karma · 2024-01-19 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=sdm4doPDBhGFtdQ3f
Right. What's "natural" depends on which features you're paying attention to, which can depend on your values. Electric, wood-burning, and neural fireplaces are similar if you're only paying attention to the subjective experience, but electric and wood-burning fireplaces form a cluster that excludes neural fireplaces if you're also considering objective light and temperature conditions.

The thesis of this post is that people who think neural fireplaces are fireplaces should be arguing for that on the merits—that the decision-relevant thing is having the subjective experience of a fireplace, even if the hallucinations don't provide heat or light. They shouldn't be saying, "We prefer to draw our categories this way because otherwise the CEO of Neural Fireplaces, Inc. will be really sad, and he's our friend."

#### [>>] Wei Dai · 7 karma · 2024-01-19 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=7w5bcscCwEYf68gjx
>The thesis of this post is that people who think neural fireplaces are fireplaces should be arguing for that on the merits—that the decision-relevant thing is having the subjective experience of a fireplace, even if the hallucinations don't provide heat or light. They shouldn't be saying, "We prefer to draw our categories this way because otherwise the CEO of Neural Fireplaces, Inc. will be really sad, and he's our friend."

Hmm, what is the difference between these two types of arguments? I could recast the latter argument in terms of "features to pay attention to" or "what's decision relevant": If we pay attention to the feature of "things that the CEO of Neural Fireplaces wants people to treat as interchangeable to the greatest extent possible" then electric, fuel-burning, and neural fireplaces form a natural cluster. The CEO is our friend so it's highly decision relevant to consider what things he wants us to treat as interchangeable.

In the OP you talk about how redrawing categories for non-epistemic reasons would interfere with Bayesian reasoning, but that applies the former type of argument as well. If we decide to include neural fireplaces in the "fireplace" category based on that the decision-relevant thing is having the subjective experience of a fireplace, it equally interferes with Bayesian reasoning: we can no longer safely infer "generates objective light with high probability" upon hearing "fireplace", and some people may well make erroneous inferences during a transition period before everyone got on the same page.

So hopefully I'm not being willfully obtuse, but I'm not sure what principle you're drawing on to say that the former type of argument is ok but the latter is not.

#### [>>>] Zack_M_Davis [AUTHOR] · 5 karma · 2024-01-20 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=KQxe7hcqEyGyb35js
But presumably the reason the CEO would be sad if people didn't consider neural fireplaces to be fireplaces is because he wants to be leading a successful company that makes things people want, not a useless company with a useless product. Redefining words "in the map" doesn't help achieve goals "in the territory". 

The OP discusses a similar example about wanting to be _funny_. If I think I can get away with changing the definition of the word "funny" such that it includes my jokes by definition, I'm less likely to try interventions that will make people want to watch my stand-up routine, which is one of the consequences I care about that the old concept of _funny_ pointed to and the new concept doesn't.

Now, it's true that, in all metaphysical strictness, the map is part of the territory. "what the CEO thinks" and "what we've all agreed to put in the same category" are real-world criteria that one can use to discriminate between entities. 

But if you're not trying to deceive someone by leveraging ambiguity between new and old definitions, it's hard to see why someone would care about such "thin" categories (simply defined by fiat, rather than pointing to a cluster in a "thicker", higher-dimensional subspace of related properties). [The previous post](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries) discusses the example of a "Vice President" job title that's identical to a menial job in all but the title itself: if being a "Vice President" doesn't imply anything about pay or authority or job duties, it's not clear why I would particularly want to be a "Vice President", except insofar as I'm being fooled by what the term used to mean.

#### [>>>>] Wei Dai · 4 karma · 2024-01-20 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=9kcKahbspGfKKp7kr
>But presumably the reason the CEO would be sad if people didn’t consider neural fireplaces to be fireplaces is because he wants to be leading a successful company that makes things people want, not a useless company with a useless product. Redefining words “in the map” doesn’t help achieve goals “in the territory”.

I see, I think this makes sense, but it depends on the CEO's actual goals/values, right? What if the CEO wants to leverage his friendships to make money, and doesn't mind people buying neural fireplaces partly or wholly out of care/sympathy for him? And everyone is (or most people are) happy to do this out of genuine care/sympathy for the CEO? In that case there is seemingly no deception involved, and redefining words “in the map” does help achieve goals “in the territory”.

Which of these two analogies is closer to the transgender situation involves empirical questions that I lack the knowledge to discuss. But it occurs to me that maybe your disagreement with Eliezer/Scott is based on you thinking that the first analogy is closer, and them thinking that the second analogy is closer? In other words, maybe they think that trans people would be happy enough with people treating them as their preferred sex/gender out of care/sympathy, and not necessarily "on the merits" in some way?

#### [>] Martin Randall · 2 karma · 2024-11-27 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=pLiQuNQFDcTjkzhFX
I find this hypothetical about neural fireplaces curious, because the ambiguity exists in real fireplaces, speculative fiction is not needed. Please excuse any inaccuracies in this brief history of fireplaces:

1. Wood-burning fireplaces
2. Gas-burning fireplaces
3. Central heating
4. Electric heaters
5. Decorative fireplaces (no heat)

The original fireplaces produced both heat and a decorative flame effect. With each new type of invention there was a question of what to do with our previous terms. We've ended up with "heaters" to refer to things that heat a room and "fireplace" to refer to things that have a decorative flame effect. Both of these things are slightly fuzzy natural categories in the sense of this post.

Except... maybe we should say that "decorative" is a privative adjective and so a "decorative fireplace" isn't really a fireplace? For the sake of the thought experiment, let's say that practical rural folk place a higher value on having a secondary heat source because it takes longer to restore electricity after a storm. Meanwhile snobby urbanites place a higher value on decorative flame effects because they value gaining status through conspicuous consumption.

I see that someone could say "well, it's not a real fireplace, is it?" in order to signal that they share the values of practical rural folks. If they're actually a snobby urbanite politician and they don't actually have those practical rural values then they are being deceptive. That would be a deception about values, not about heat sources.

If a practical rural person says "well, it's not a real fireplace, is it?", then that could indeed be a true signal of their values. But my guess is the more restrictive meaning of fireplace came first. The causal diagram is something like:

- Practical Rural Values -> Categorize functional fireplaces separately to decorative fireplaces -> Use the short word "fireplace" for functional fireplaces (for communication and signaling)

Not:

- Practical Rural Values -> Use the short word "fireplace" for functional fireplaces (for signaling) -> Categorize functional fireplaces separately to decorative fireplaces

Because until practical rural folks have settled on a common meaning of "fireplace", they can't reliably use that meaning to signal their values to each other or to outsiders.

Except... maybe if it got caught up in the modern culture war there could be a flood of fireplace-related memes and then everyone would have very strong opinions about the best definition of "fireplace" a few months later for no real reason? Wow, that sure would suck for the CEO of Decorative Fireplaces Inc.

#### [>>] Kenku · 2 karma · 2024-11-27 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=nC5A4XKjujkmSwDfw
[Diogenes voice] This device provides both heat and decorative visual effects, therefore it's a fireplace:
![Desktop computer with high-end graphics card and RGBT lighting](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Das_Innenleben_eines_Gaming-PCs_aus_2021_20211126_HOF08248_RAW-Export_20220714004139.png/7168px-Das_Innenleben_eines_Gaming-PCs_aus_2021_20211126_HOF08248_RAW-Export_20220714004139.jpg)

#### [-] Zack_M_Davis [AUTHOR] · 11 karma · 2025-06-14 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=w9tWkpCBrdgwq6Coc
I think this was excellent work that no one (rounding down) appreciated at the time because I sacrificed readability by optimizing for comprehensiveness. If it helps, I have now composed [a Twitter-optimized summary](https://x.com/zackmdavis/status/1933701378196824431):

> Time for a Twitter-optimized capsule 🧵 of my 2021 philosophy of language thesis about why choosing bad definitions is relevantly similar to lying! If you wouldn't lie, you also shouldn't say, "it's not lying; I'm just defining words in a way that I prefer." 1/24
> 
> Some people say: the borders of a category are like the borders of a country—they have consequences, but there's no sense in which some possible borders can be objectively worse than others. 2/24
> 
> But category "borders" or "boundaries" are just a visual metaphor corresponding to a kind of probabilistic model. Editing the "boundary" means editing the model's predictions. There is a sense in which some models can be objectively worse than others! 3/24
> 
> Imagine having to sort a bunch of blue egg-shaped things (which contain vanadium) & red cubes (that don't). Technically, you don't actually need separate "blue egg" & "red cube" categories. You could just build up a joint probability table over all objects and query that. 4/24
> 
> But that's unwieldy. Thinking about "blue egg" & "red cube" as separate categories and computing the properties of an object conditional on its category is much more efficient. 5/24
> 
> "Computing the properties of an object conditional on its category" can be visualized as category "boundaries" in a picture. 6/24
> 
> But the picture is an illustration of the math; you can't change the picture without changing the math. It's not like national borders at all. The U.S. purchasing Alaska (non-contiguous with the 48 states) wasn't about editing a probabilistic model. 7/24
> 
> In itself, this doesn't yet explain what's wrong with "squiggly", "gerrymandered" categories. You can still make predictions with squiggly categories. 8/24
> 
> But if approximately-correct answers are at all more useful than totally-wrong answers, squiggly categories are mathematically just worse (going by the mean squared error). If your "blue eggs" category contains some red cubes, you'll drill for vanadium where there isn't any. 9/24
> 
> The best categories are subjective in the sense that they depend on what you're trying to predict, but that's not the same thing as the category boundary itself being subjective. Given what you want to predict, the model (and thus the "boundary") is determined by the data. 10/24
>
> Some people say: okay, but what if I really do have a preference for using a particular squiggly boundary, intrinsically, not in a way that arises from desired predictions and the data distribution? That's just how my utility function is! What's irrational about that? 11/24
> 
> Let's interrogate this. What would it mean, to have such an exotic utility function? There is a trivial sense in which any pattern of behavior, however bizarre, could be rationalized in terms of preferring to take the actions that I do in the situation that I face. 12/24
> 
> But a theory that explains everything explains nothing. The explanatory value of the "utility function" formalism isn't that it can justify anything given a choice of "utility", but in the constraints it articulates on coherent behaviors (given, yes, a choice of "utility"). 13/24
> 
> If your gambling behavior violates the independence axiom with respect to money, that doesn't automatically make you irrational, but it does mean that you're acting as if you care about something else besides money—that you'll sacrifice some money for that something else. 14/24
> 
> Similarly, if your communication signals aren't explainable in terms of conveying probabilistic predictions, that does imply that you care about something else than conveying probabilistic predictions—that you'll sacrifice clarity (of predictions) for that something else. 15/24
> 
> But what might that something else be, concretely? It's hard to see where a completely arbitrary, hardwired, "just because" preference for using a particular category boundary would come from! Why would that be a thing? Why?? 16/24
> 
> A much more plausible reason to sacrifice clarity of predictions is because you don't want other agents to make accurate predictions. (Because if those others had better models, they'd make decisions that harm your interests.) That's deception. 17/24
> 
> There's no functional difference between saying "I reserve the right to lie p% of the time about whether something belongs to a category" and adopting a new category system that misclassifies p% of things. The input–output relations are the same. 18/24
> 
> A related reason for unnatural categories: it's tempting to "wirehead" by choosing a map that looks good, instead of the map that reflects the territory (which might be unpleasant to look at). That's self-deception. 19/24
> 
> If I want to believe I'm pretty & funny, it might be tempting to redefine "pretty" & "funny" such that they include me. But that would just be fooling myself; it doesn't actually work for making me pretty & funny (with respect to the usual meanings). 20/24
> 
> Sometimes things resemble another in some but not all aspects. This is mimickry. It's deceptive if the point is for another agent to treat the mimic as the original against the agent's interests—but it's not deceptive if the agent really doesn't care about the difference. 21/24
> 
> If agents sharing a language disagree about which aspects "count", they'll fight over the definitions of words: animal advocates would prefer if plant-based meat substitutes counted as "real" meat, to make it hard for carnivores to insist on the dead-animal kind. 22/24
> 
> Philosophy itself can't determine which definition is right (which depends on the empirical merits), but philosophy does clarify what's happening in this kind of conflict—that departing from the empirical merits extracts a cost in the form of worse predictions. 23/24
> 
> Original post: "Unnatural Categories Are Optimized for Deception" https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception END/24

#### [>] tslarm · 10 karma · 2025-06-14 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=fccJsyMtGTxdLAWEW
> There's no functional difference between saying "I reserve the right to lie p% of the time about whether something belongs to a category" and adopting a new category system that misclassifies p% of things. The input–output relations are the same.

If I'm honest about the boundaries of my new category system, how is this deceptive? You know that my 'blegg' category includes a small number of things that you would prefer to define as rubes, so when I tell you something is a blegg, you know that means it has an X% chance of being a mutually-agreed blegg and a 100-X% chance of being (in your eyes) a rube with properties that I consider definitive of a blegg. From your perspective, I may be *concealing* some relevant information, but I'm doing so openly and allowing you to draw correct probabilistic inferences. 

That's not the same as "I reserve the right to lie p% of the time about whether something belongs to a category"; it's the same as "I will consistently 'lie' about which of these categories some things belong to, because those things have properties that are not part of the usual definitions of the categories but which I consider important, namely <x> or <y>, and I will consistently say that things with <x> belong in category A and things with <y> belong in category B". Which would be a weird way to put it, because I'm not actually lying if the meaning of my words is clear (albeit not informative in exactly the way you would prefer) and I am neither deceiving you nor intending to deceive you.

#### [>>] Zack_M_Davis [AUTHOR] · 2 karma · 2025-07-08 · https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception?commentId=fnP5JTL77W5Ss7zsb
Excellent question, thanks for commenting! (And for your patience.) The part of the original post that that Tweet is summarizing are the paragraphs after "Suppose I'm selling you some number of gold and silver bars [...]". As you observe, whether it's "lying" to use a category label depends on what the label is construed to "canonically" mean. The idea here is that, as far as signal processing goes, there's an isomorphism between "lying p% of the time" _with respect to_ the maximally-informative categories, and choosing different categories that conceal information. So if the new categories aren't deceptive because the receiver knows about them, is lying therefore not deceptive if the speaker already has it "priced in" that the sender lies this-and-such proportion of the time? I discuss this problem further in ["Maybe Lying Can't Exist?!"](https://www.lesswrong.com/posts/YptSN8riyXJjJ8Qp8/maybe-lying-can-t-exist) and ["Comment on 'Deception is Cooperation'"](https://www.lesswrong.com/posts/dJjRSjmH7NNLJDb6v/comment-on-deception-as-cooperation).

