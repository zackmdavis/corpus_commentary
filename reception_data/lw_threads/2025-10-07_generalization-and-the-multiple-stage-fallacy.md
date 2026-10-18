Title: Generalization and the Multiple Stage Fallacy?
LessWrong-URL: https://www.lesswrong.com/posts/As3euLoCJwjvPBMt4/generalization-and-the-multiple-stage-fallacy
Posted: 2025-10-07
Fetched: 2026-10-13 (LessWrong GraphQL API; rendered by tools/render_lw_threads.py)
Comments: 5 (commentCount field: 9)

#### [-] Raemon · 10 karma · 2025-10-07 · https://www.lesswrong.com/posts/As3euLoCJwjvPBMt4/generalization-and-the-multiple-stage-fallacy?commentId=AmE9Ah6EqeGPBxueB
> In analogy, someone who wanted to argue that it's infeasible to build text-to-image generative models that make art that humans enjoy, could partition their prediction of failure into disjunctive failure modes: the model has to generalize what hands look like; it has to generalize what birds look like. It has to generalize which compositions and color combinations are pleasing—which is arguably an "ought"/steering problem, not an "is"/prediction problem! One-shotting all of those separate problems isn't something that human beings can do in real life, the argument would go. But of course, the problems aren't independent, and text-to-image generators do exist.

Isn't part of the deal here that we didn't one-shot image generation, though? 

The first image generators were crazy, we slowly iterated on them, and image generation is "easy" because unlike superintelligence or even self-driving cars or regular ol' production code, nothing particularly bad happens if a given image is bad.

#### [>] Raemon · 2 karma · 2025-10-07 · https://www.lesswrong.com/posts/As3euLoCJwjvPBMt4/generalization-and-the-multiple-stage-fallacy?commentId=DTtTHDDW3ktRtB9LN
That said, FYI I was kind of enlightened by this phrasing:

> That is, in the multiple stage fallacy, someone who wishes to portray a proposition as unlikely can **prey on people's reluctance to assign extreme probabilities** by spuriously representing the proposition as a conjunction of sub-propositions that all need to be true.

I'd been feeling sus about why the multiple stage fallacy was even a fallacy at all, apart from "somehow in practice people fuck it up." Multiplying probabilities together is... like, how else are you supposed to do any kind of sophisticated reasoning?

But, "because people are scared of (or bad at) assigning extreme probabilities" feels like it explains it to me.

#### [>>] kave · 5 karma · 2025-10-08 · https://www.lesswrong.com/posts/As3euLoCJwjvPBMt4/generalization-and-the-multiple-stage-fallacy?commentId=uJyLjX6byyb8qyfyG
I think the larger effect is treating the probabilities as independent when they're not.

Suppose I have a jar of jelly beans, which are either all red, all green or all blue. You want to know what the probability of drawing 100 blue jelly beans is. Is it $\frac{1}{3}^{100} \approx 2⋅10^{-48}$? No, of course not. That's what you get if you multiply 1/3 by itself 100 times. But you should condition on your results as you go. P(jelly1 = blue)⋅P(jelly2=blue|jelly1=blue)⋅P(jelly3=blue|jelly1=blue,jelly2=blue) ...  
  
Every factor but the first is 1, so the probability is $\frac{1}{3}$.

#### [-] Vladimir_Nesov · 4 karma · 2025-10-07 · https://www.lesswrong.com/posts/As3euLoCJwjvPBMt4/generalization-and-the-multiple-stage-fallacy?commentId=ewyifkaPqbvvwnTrq
There are two different issues with "the first critical try" (the After regime), where misalignment is lethal. First, maybe alignment is sufficiently solved, and so when you enter After, that's why it doesn't kill you. But second, maybe After never arrives.

Gradualist arguments press both issues, not just alignment of After. Sufficient [control](https://www.lesswrong.com/posts/d9FJHawgkiMSPjagR/ai-control-improving-safety-despite-intentional-subversion) makes increasingly capable AIs non-lethal if misaligned, which means that an AI that would bring about the After regime today wouldn't do so in the future where better countermeasures (that are not about alignment) are in place. Which is to say this particular AI won't enter the After regime yet, because the world is sufficiently different and this AI's capabilities are now insufficient for lethality, an even more capable AI would be necessary for that.

This is different from an ASI Pause delaying the After regime until ASI-grade alignment is solved, because the level of capabilities that counts as After keeps changing. Instead of delaying ASI at a fixed level of capabilities until alignment is solved, After is being pushed into the future by increasing levels of control that make increasingly capable AIs non-critical. As a result, After never happens at all, instead of only happening once alignment at a relevant level is sufficiently solved.

(Of course the feasibility of ASI-grade control is as flimsy as the feasibility of ASI-grade alignment, when working on a capabilities schedule without an AGI/ASI Pause, not to mention [gradual disempowerment](https://www.lesswrong.com/posts/pZhEQieM9otKXhxmd/gradual-disempowerment-systemic-existential-risks-from) in the gradualist regime without an AGI Pause. But the argument is substantially different, and a proponent of gradualist development of ASI-grade control might feel that there is no fixed After, and maybe that After never actually arrives even as capabilities keep increasing. The arguments against feasibility of gradualist development of ASI-grade alignment on the other hand feel like they are positing a fixed After whose arrival remains inevitable at some point, which doesn't *acknowledge* the framing from gradualist arguments about development of ASI-grade control.)

#### [-] Buck · 4 karma · 2025-10-08 · https://www.lesswrong.com/posts/As3euLoCJwjvPBMt4/generalization-and-the-multiple-stage-fallacy?commentId=pf7pJhh7P5zBZo784
I liked Joe Carlsmith's discussion of this [here](https://joecarlsmith.com/2023/05/08/predictable-updating-about-ai-risk).

