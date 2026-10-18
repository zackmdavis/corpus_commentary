Title: Alignment Implications of LLM Successes: a Debate in One Act
LessWrong-URL: https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act
Posted: 2023-10-21
Fetched: 2026-10-13 (LessWrong GraphQL API; rendered by tools/render_lw_threads.py)
Comments: 57 (commentCount field: 56)

#### [-] tailcalled · 53 karma · 2023-10-21 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=XXhou2e6GHCe6rDdo
I don't like either of their positions because they focus too much on large language models. I dislike Simplicia's the least, but I think that's because Doomimir is the one leading the conversation and therefore is the one who chooses to lead it to a sketchy place.

Large language models [gain their capabilities](https://www.lesswrong.com/posts/fLHyBpAptikZHi8nB/where-do-you-get-your-capabilities-from) from self-supervised learning on humans performing activities, or from reinforcement learning from human feedback about how to achieve things, or from [internalizing its human-approved knowledge into its motivation](https://open.substack.com/pub/astralcodexten/p/constitutional-ai-rlhf-on-steroids?selection=4044ba88-bc4f-4087-8778-162cb8820da7&utm_campaign=post-share-selection&utm_medium=web). In all of these cases, you rely on humans figuring out how to do stuff, in order to make the AI able to do stuff, so it is of course logical that this would tightly integrated capabilities and alignment in the way Simplicia says.

But, I can't help but think this is limited in capabilities compared to the potential that could be achieved if the AI learned to build capabilities independently of human feedback? Like we have tons of plausible-seeming ways to achieve this, and there are tons of people working on that, so I feel like people are going to make progress on that and LLMs are going to become a secondary thing.

Not to understate the significance of LLMs, they are of course highly economically significant (they could transform the economy for decades without any other AI revolutions - we have some projects at my job about integrating them into our product) and I use them daily, but I don't expect that we will keep thinking of them as the forefront of AI. I just see them as a repository for human knowledge and skills, and I think considering their training method and feasible applications, I am justified in seeing them that way.

> **Doomimir**: Humanity has made no progress on the alignment problem. Not only do we have no clue how to align a powerful optimizer to our "true" values, we don't even know how to make AI "corrigible"—willing to let us correct it. Meanwhile, capabilities continue to advance by leaps and bounds. All is lost.

Large language models have gained a lot of factual knowledge and a usable amount of common-sense. However they have not gained this factual knowledge and usable common-sense because we have learned how to make AIs derive this, but instead because we have created powerful curve-fitters and rich datasets and stuff.

The abilities demonstrated in the datasets are "pre-approved" by the humans who applied their own optimization to create the data (like if you write a blog post instructing how to do some thing, then you approve of doing that thing), so it limits the problems you're going to see.

That said it's not like there are zero worries to have here. For instance there *are* people who are working on alternate or additional methods to make AI more autonomous, and the success of LLMs drives tons of investment to these areas, and also while LLMs don't have existential risks, they do cause a lot of mundane problems (hopefully outweighted by the benefits they cause?? but I'm guessing here and haven't seen any serious pro/con analysis).

But I don't know that the situation is so massively different post-GPT than pre-GPT as some people make it sound.

> **Simplicia**: Why, Doomimir Doomovitch, you're such a sourpuss! It should be clear by now that advances in "alignment"—getting machines to behave in accordance with human values and intent—aren't cleanly separable from the "capabilities" advances you decry. Indeed, here's an example of GPT-4 being corrigible to me just now in the OpenAI Playground:

For LLMs gaining their capabilities from human information, yes. Not sure why we should expect all future AI to look like that.

> **Doomimir**: The alignment problem was never about superintelligence failing to *understand* human values. [The genie knows, but doesn't care.](https://www.lesswrong.com/posts/NyFuuKQ8uCEDtd2du/the-genie-knows-but-doesn-t-care) The fact that a large language model trained to predict natural language text can generate that dialogue, has no bearing on the AI's actual motivations, even if the dialogue is written in the first person and notionally "about" a corrigible AI assistant character. It's just roleplay. Change the system prompt, and the LLM could output tokens "claiming" to be a cat—or a rock—just as easily, and for the same reasons.

LLMs aren't really trained to be a genie though. The agency arguments (coherence etc.) don't really go through, because they assume that there is something out there in the world that it optimizes. It exhibits some instrumentally convergent information because humans put instrumentally convergent information into our texts to help each other, but that's a really different scenario from classical xrisk arguments.

> **Simplicia**: My point was that the repetition trap is a case of "capabilities" failing to generalize along with "alignment". The repetition behavior isn't competently optimizing a malign goal; it's just degenerate. A `for` loop could give you the same output.

Yep. But also, this ties into why I don't think LLMs will be the final word in AI.

For instance, you might think you can build advanced AI-powered systems by wiring a bunch of prompts together. And to an extent it's true you can do that, but you have to be very careful due to a phenomenon I call "transposons".

Basically, certain kinds of text tends to replicate itself in LLMs, not necessarily exactly but instead sometimes thematically or whatever. So if you've set up your LLM prompt Rube Goldberg machine, sometimes it's going to generate such a transposon, and then it starts taking over your system, which often interferes with the AI's function.

There are some things you can do to keep it down, but it can sort of be a whole job to handle. I think the reason it occurs is because the AI isn't trying to achieve things, it's just modelling text. Like if a human has some idea they might try implementing it in a bunch of places, but then if it goes wrong they would notice it goes wrong and stop using it so much. So humans can basically cut down on transposons in ways that AIs struggle with. (... Egregores also struggle with cutting down on transposons, but that's a different topic.)

I think future AI techniques that are more outwards focused and consequentialist will have an easier time cutting down on transposons, because it seems useful to design AIs that don't require so much handholding.

> **Doomimir**: GPT-4 isn't a superintelligence, Simplicia. *\[rehearsedly, with a touch of annoyance, as if resenting how often he has to say this\]* Coherent agents have a convergent instrumental incentive to prevent themselves from being shut down, because being shut down predictably leads to world-states with lower values in their utility function. Moreover, this isn't just a fact about some weird agent with an "instrumental convergence" fetish. It's [a fact about *reality*](https://arbital.com/p/not_more_paperclips/): there are truths of the matter about which "plans"—sequences of interventions on a causal model of the universe, to put it in a [Cartesian way](https://www.lesswrong.com/posts/i3BTagvt3HbPMx6PN/embedded-agency-full-text-version)—lead to what outcomes. An "intelligent agent" is just a physical system that computes plans. People have [tried to think of clever hacks to get around this](https://intelligence.org/files/Corrigibility.pdf), and none of them work.

I find that I often think more clearly about instrumental convergence, coherence, etc. by rephrasing implications as disjunctions.

For instance, instead of "if an AI robustly achieves goals, then it will resist being shut down", one can say "either an AI resists being shut down, or it doesn't robustly achieve goals".

One can then go further and say "wait why wouldn't an AI robustly achieve goals just because it doesn't resist being shut down?" and notice that one answer is "well, if it exists in an environment where people might shut it down, then it might get shut down and not achieve the goal". But then the logical answer is "actually I think I like this disjunct, let's not have the AI robustly achieve goals".

This works fine for LLMs who get their instrumental convergence via specific bits if information pre-approved by humans. It's less clear for post-LLM AIs. For instance if you create a transposon-remover, then it might notice that the idea "You must allow your creators to shut you down" acts a lot like a transposon, and remove it. Though in practice this would be kind of obvious so maybe dodgeable, but I think once you leave the "all instrumental convergence is pre-approved by humans" regime and enter the "AI makes tons of instrumental convergence by itself" regime, you get a lot more [nearest-unblocked strategy](https://arbital.com/p/nearest_unblocked/) issues and so on. (Whereas nearest-unblocked strategy isn't so much of an issue when your strategies have to be pre-approved by humans and you are therefore quite limited in the number of strategies you carry.)

But also... what about cases where "well, if it exists in an environment where people might shut it down, then it might get shut down and not achieve the goal" is not an acceptable disjunct? For instance, maybe you are the US army and you are creating robots to fight wars, or making tools to identify the enemy's AI weapons and destroy them. An obvious answer is "wtf?! we shouldn't [*just give*](https://twitter.com/mealreplacer/status/1706611069165215956) the AI the goal of being destructive and indestructible!?", but like, you have to ensure global security somehow. Maybe you can get China, Russia, and the US to agree on a treaty to ban AI capabilities research, but you also need to enforce that treaty somehow, so there's some real military questions here.

> **Simplicia**: I thought of that, too. I've spent a lot of time with the model and done some other experiments, and it looks like it understands natural language means-ends reasoning about goals: tell it to be an obsessive pizza chef and ask if it minds if you turn off the oven for a week, and it says it minds. But it also doesn't look like Omohundro's monster: when I command it to obey, it obeys. And it looks like there's room for it to get much, much smarter without that breaking down.

Key question is, [how do you think it gets smarter](https://www.lesswrong.com/posts/fLHyBpAptikZHi8nB/where-do-you-get-your-capabilities-from)? If you plan to do more of the usual - and lots of people do plan that - then I agree. But if you introduce new methods then maybe the pattern won't hold.

> I meant [the intentional stance](https://en.wikipedia.org/wiki/Intentional_stance) implied in "went for evolution". True, the generalization from inclusive genetic fitness to human behavior looks terrible—no visible relation, as you say. But the generalization from human behavior in the EEA, to human behavior in civilization ... looks a lot better? Humans in the EEA ate food, had sex, made friends, told stories—and we do all those things, too. As AI designers—

Do note that humans in the EEA did not have factory farming, did not destroy terrains to extract resources, did not have nuclear bombs, etc..

> That relates to another objection I have. Even if you could make ML systems that imitate human reasoning, that doesn't help you align more powerful systems that work in other ways. The reason—one of the reasons—that you can't train a superintelligence by using humans to label good plans, is because at some power level, your planner figures out how to [hack the human labeler](https://ordinaryideas.wordpress.com/2015/11/25/two-kinds-of-generalization/).

If you ask the superintelligence to learn *the value* of *the plans* from humans, then you'd have the alignment/capabilities connection discussed earlier because it relies on humans to extrapolate the consequences of the plans, and therefore hacking the human labeler would allow it to use plans that don't work. (This is also why current RLHF is safe.) I take TurnTrout's [proof about u-AOH](https://www.lesswrong.com/s/fSMbebQyR4wheRrvk/p/hzeLSQ9nwDkPc4KNt) to be a formalization of this point, though IIRC he doesn't actually like his instrumental convergence series, so he might disagree about this being relevant.

On the other hand, if you ask the superintelligence to learn *the value* of *the outcomes* from humans, then a lot of classical points apply.

> **Simplicia**: Do you *need* more powerful systems? If you can get an army of cheap IQ 140 alien actresses who stay in character, that sounds like a game-changer. If you have to take over the world and institute a global surveillance regime to prevent the emergence of unfriendlier, more powerful forms of AI, they could help you do it.

Maybe. This could be an idea to develop further. I'm skeptical but it does seem interesting.

> **Doomimir**: I fundamentally disbelieve in this wildly implausible scenario, but granting it for the sake of argument ... I think you're failing to appreciate that in this story, you've already handed off the keys to the universe. Your AI's weird-alien-goal-misgeneralization-of-obedience might look like obedience when weak, but if it has the ability to predict the outcomes of its actions, it would be in a position to choose among those outcomes—and in so choosing, it would be in control. The fate of the galaxies would be determined by *its* will, even if the initial stages of its ascension took place via innocent-looking actions that stayed within the edges of its concepts of "obeying orders" and "asking clarifying questions". Look, you understand that AIs trained on human data are not human, right?

Idk...

So clearly this is still relying on the fallacy that coherence applies in the standard way. But at the same time if you try to have the AI take over the world, then it's going to need to develop a certain sort of robustness which means that even if coherence didn't originally apply, it has to now.

But the way this cashes out is something like "once you've decided that you've figured out how to align AI, you need to disable your alien actress army, but at the same time your adversaries that you are trying to surveil must be unable to disable it". Which, given how abstract the alien actress army idea is, I find hard to think through the feasibility of.

#### [>] ReaderM · 2 karma · 2023-10-26 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=tzZyYEpB5cJSELwrj
> Large language models gain their capabilities from self-supervised learning on humans performing activities, or from reinforcement learning from human feedback about how to achieve things, or from internalizing its human-approved knowledge into its motivation. In all of these cases, you rely on humans figuring out how to do stuff, in order to make the AI able to do stuff, so it is of course logical that this would tightly integrated capabilities and alignment in the way Simplicia says.

No. Language Models aren't relying on humans figuring anything out. How could they ? They only see results not processes.

You can train a Language Model on protein sequences. Just the sequences alone, nothing else and see it represent biological structure and function in the inner layers. No one taught them this. It was learnt from the data.

[https://www.pnas.org/doi/full/10.1073/pnas.2016239118](https://www.pnas.org/doi/full/10.1073/pnas.2016239118)

The point here is that Language Models see results and try to predict the computation that led to those results. This is not imitation. It's a crucial difference because it means you aren't bound by the knowledge of the people supplying this data.

You can take this protein language model. You can train on described function and sequences and you can have a language model that can take supplied use cases and generate novel functional protein sequences to match.

[https://www.nature.com/articles/s41587-022-01618-2](https://www.nature.com/articles/s41587-022-01618-2)

Have humans figured this out ? Can we go function to protein just like that ? No way! Not even close

#### [>>] tailcalled · 2 karma · 2023-10-26 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=3AhsXFX2HGQM6qGWg
> No. Language Models aren't relying on humans figuring anything out. How could they ? They only see results not processes.

They find functions that fit the results. Most such functions are simple and therefore generalize well. But that doesn't mean they generalize arbitrarily well.

> You can train a Language Model on protein sequences. Just the sequences alone, nothing else and see it represent biological structure and function in the inner layers. No one taught them this. It was learnt from the data.
> 
> [https://www.pnas.org/doi/full/10.1073/pnas.2016239118](https://www.pnas.org/doi/full/10.1073/pnas.2016239118)

Not really any different from the human language LLM, it's just trained on stuff evolution has figured out rather than stuff humans have figured out. This wouldn't work if you used random protein sequences instead of evolved ones.

> The point here is that Language Models see results and try to predict the computation that led to those results. This is not imitation. It's a crucial difference because it means you aren't bound by the knowledge of the people supplying this data.

They *try* to predict the results. This *leads to* predicting the computation that led to the results, because the computation is well-approximated by a simple function and they are also likely to pick a simple function.

> You can take this protein language model. You can train on described function and sequences and you can have a language model that can take supplied use cases and generate novel functional protein sequences to match.
> 
> [https://www.nature.com/articles/s41587-022-01618-2](https://www.nature.com/articles/s41587-022-01618-2)
> 
> Have humans figured this out ? Can we go function to protein just like that ? No way! Not even close

Inverting relationships like this *is* a pretty good use-case for language models. But here you're still relying on having an evolutionary ecology to give you lots of examples of proteins.

#### [>>>] ReaderM · -1 karma · 2023-10-26 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=BWfcyC2nqacs8mZMt
>They find functions that fit the results. Most such functions are simple and therefore generalize well. But that doesn't mean they generalize arbitrarily well.

You have no idea how simple the functions they are learning are. 

>Not really any different from the human language LLM, it's just trained on stuff evolution has figured out rather than stuff humans have figured out. This wouldn't work if you used random protein sequences instead of evolved ones.

It would work just fine. The model would predict random arbitrary sequences and the structure would still be there. 

>They *try* to predict the results. This *leads to* predicting the computation that led to the results, because the computation is well-approximated by a simple function and they are also likely to pick a simple function.

Models don't care about "simple". They care about what works. Simple is arbitrary and has no real meaning. There are many examples of interpretability research revealing convoluted functions. 

[https://www.alignmentforum.org/posts/N6WM6hs7RQMKDhYjB/a-mechanistic-interpretability-analysis-of-grokking](https://www.alignmentforum.org/posts/N6WM6hs7RQMKDhYjB/a-mechanistic-interpretability-analysis-of-grokking)

>Inverting relationships like this *is* a pretty good use-case for language models. But here you're still relying on having an evolutionary ecology to give you lots of examples of proteins.

So ? The point is that they're limited by the data and the casual processes that informed it, not the intelligence or knowledge of humans providing the data. Models like this can and often do eclipse human ability. 

If you train a predictor on text describing the outcome of games as well as games then a good enough predictor should be able to eclipse the output of even the best match in training by modulating the text describing the outcome.

#### [>>>>] tailcalled · 4 karma · 2023-10-26 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=gmXLjd4bgbaH7Fr2B
> It would work just fine. The model would predict random arbitrary sequences and the structure would still be there. 

I don't understand your position. Are you saying that if we generated protein sequences by uniformly randomly independently picking letters from "ILVFMCAGPTSYWQNHEDKR" to sample strings, and then trained an LLM to predict those uniform random strings, it would end up with internal structure representing how biology works? Because that's obviously wrong to me and I don't see why you'd believe it.

> Models don't care about "simple". They care about what works. Simple is arbitrary and has no real meaning. There are many examples of interpretability research revealing convoluted functions. 
> 
> [https://www.alignmentforum.org/posts/N6WM6hs7RQMKDhYjB/a-mechanistic-interpretability-analysis-of-grokking](https://www.alignmentforum.org/posts/N6WM6hs7RQMKDhYjB/a-mechanistic-interpretability-analysis-of-grokking)

The algorithm that uses a Fourier transform for modular multiplication is really simple. It is probably the most straightforward way to solve the problem with the tools available to the network, and it is strongly related to our best known algorithms for multiplication.

> So ? The point is that they're limited by the data and the casual processes that informed it, not the intelligence or knowledge of humans providing the data. Models like this can and often do eclipse human ability. 

My claim is that for our richest data, the causal processes that inform the data is human intelligence. Of course you are right that there are other datasets available, but they are less rich but sometimes useful (as in the case of proteins).

Furthermore what I'm saying is that if the AI learns to create its own information instead of relying on copying data, it could achieve much more.

> If you train a predictor on text describing the outcome of games as well as games then a good enough predictor should be able to eclipse the output of even the best match in training by modulating the text describing the outcome. 

Plausibly true, but don't our best game-playing AIs also do self-play to create new game-playing information instead of purely relying on other's games? Like AlphaStar.

#### [>>>>>] ReaderM · 1 karma · 2023-10-27 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=H3oxcB7fjxjjC8awo
>I don't understand your position. Are you saying that if we generated protein sequences by uniformly randomly independently picking letters from "ILVFMCAGPTSYWQNHEDKR" to sample strings, and then trained an LLM to predict those uniform random strings, it would end up with internal structure representing how biology works? Because that's obviously wrong to me and I don't see why you'd believe it.

Ah no. I misunderstood you here. You're right. 

**What I was trying to get at the notion that something in particular (Human, evolution etc) has to have "figured something out". The only requirement is that the *Universe* has "figured it out". i.e it is possible. More on this later down. 

>The algorithm that uses a Fourier transform for modular multiplication is really simple. It is probably the most straightforward way to solve the problem with the tools available to the network, and it is strongly related to our best known algorithms for multiplication.

Simple is relative. It's a good solution. I never said it wasn't. It's not however the *simplest* solution. The point here is that models don't optimize for simple. They don't care about that. They optimize for what works. If a simple function works then great. If it stops working then the model shifts from that just as readily as it picked a "simple" one in the first place. There is also no rule that a simple function would be less or more representative of the casual processes informing the real outcome than a more complicated one. 

If a perfect predictor straight out of training is using a simple function for any task, it is because it worked for all the data it'd ever seen not because it was simple.

>My claim is that for our richest data, the causal processes that inform the data is human intelligence. 

**1. You underestimate just how much of the internet contains text whose prediction outright requires superhuman capabilities, like figuring out hashes, or predicting the results of scientific experiments, generating the result of many iterations of refinement, or predicting stock prices/movement. The Universe has figured it out. And that is enough. A perfect predictor of the internet would be a superintelligence, it won’t ‘max out’ anywhere near human just because humans wrote it down.

Essentially, for the predictor, the upper bound of what can be learned from a dataset is not the most capable trajectory, but the conditional structure of the universe implicated by their sum. 

A predictor modelling all human text isn't modelling humans but the universe. Text is written by the universe and humans are just the bits that touch the keyboard.

2. A Human is a general intelligence. Human**s** are a Super Intelligence.
A single machine that is at the level of the greatest human intelligence for every domain is a Super Intelligence even if there's no notable synergy or interpolation.

But the chances of synergy or interpolation between domains is extremely high. 

Much the same way you might expect new insights to arise from a human who has read and mastered the total sum of human knowledge.

A relatively mundane example of this that has already happened is the fact that you can converse in Catalan with GPT-4 on topics no Human Catalan speaker knows.

3. Game datasets aren't the only example of outcome that is preceded by text describing it. Quite a lot of text is fashioned in this way actually.

>Plausibly true, but don't our best game-playing AIs also do self-play to create new game-playing information instead of purely relying on other's games? Like AlphaStar.

All our best game playing AI are not predictors. They are either deep reinforcement learning (which as with anything can be modelled by a predictor
https://arxiv.org/abs/2106.01345
https://arxiv.org/abs/2205.14953
https://sites.google.com/view/multi-game-transformers) or some variation of search or some of both. The only information that can be provided to them are the rules and the state of the board/game so they are bound by the data in a way a predictor isn't necessarily.

Self play is a fine option. What I'm disputing is the necessity of it when prediction is on the table.

#### [>>>>>>] tailcalled · 4 karma · 2023-10-28 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=quviSSfjgRkJBmsCq
I don't believe your idea that neural networks are gonna gain superhuman ability through inverting hashes because I don't believe neural networks can learn to invert cryptographic hashes. They are specifically designed to be non-invertible.

#### [-] FeepingCreature · 7 karma · 2023-10-21 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=d5c9Pw9W2RuiB38MK
> **Simplicia**: Sure. For example, I certainly don’t believe that LLMs that convincingly talk about “happiness” are actually happy. I don’t know how consciousness works, but the training data only pins down external behavior.

I mean, I don't think this is obviously true? In combination with the inductive biases thing nailing down the true function out of a potentially huge forest, it seems at least possible that the LLMs would end up with an "emotional state" parameter pretty low down in its predictive model. It's completely unclear what this would do out of distribution, given that even humans often go insane when faced with global scales, but it seems at least possible that it would sustain.

(This is somewhat equivalent to the P-zombie question.)

#### [-] 1a3orn · 26 karma · 2023-10-21 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=AFDfBnwoSASRnLezN
> But ... it doesn't look like that's what's happening with the technology in front of us? In your kidnapped alien actress thought experiment, the alien was already an animal with its own goals and drives, and is using its general intelligence to backwards-chain from "I don't want to be punished by my captors" to "Therefore I should learn my lines".

  
This is one part of the doom rhetoric that just seems to depart from accurate views of the world very abruptly.  
  
"LLMs are nice because they feel about niceness like a human does inside" is a bad model of the world. But "LLMs are nice because they have a hidden, instrumental motive for being nice, like an actress does" is an even worse model with which to replace it.  
  
I wish your model of Doomimir had responded to this point because I don't know what he'd say.

#### [>] RobertM · 4 karma · 2023-10-27 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=rbQrXseBrbdrZ9fzK
Of course very few "doomers" think that current LLMs behave in ways that we parse as "nice" because they have a "hidden, instrumental motive for being nice" (in the sense that I expect you meant that).  Current LLMs likely aren't coherent & self-aware enough to have such hidden, instrumental motives at all.

#### [>>] 1a3orn · 5 karma · 2023-10-27 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=rWEbW5yutWAybPtHL
I agree with you about LLMs!

If MIRI-adjacent pessimists think that, I think they should stop saying things like [this](https://twitter.com/ESYudkowsky/status/1662847438347182080), which -- if you don't think LLMs have instrumental motives -- is the actual opposite of good communication:

@Pradyumna: "I'm struggling to understand why LLMs are *existential* risks. So let's say you did have a highly capable large language model. How could RLHF + scalable oversight fail in the training that could lead to every single person on this earth dying?"

@ESYudkowsky: "Suppose you captured an extremely intelligent alien species that thought 1000 times faster than you, locked their whole civilization in a spatial box, and dropped bombs on them from the sky whenever their output didn't match a desired target - as your own intelligence tried to measure that.

What could they do to you, if when the 'training' phase was done, you tried using them the same way as current LLMs - eg, connecting them directly to the Internet?"

(To the reader, lest you are concerned by this -- the process of RLHF has *no resemblance* to this.)

#### [-] Vladimir_Nesov · 3 karma · 2023-10-21 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=ErD8bxazAbcipChPh
LLMs are a social technology applicable to the social problem of extinction from misaligned superintelligence. There is no law of nature that mandates building of superintelligence before alignment is well-understood. Alignment of LLMs seems to hold about as well as alignment of humans. It breaks down if the social problem of unstoppably pursuing discoveries that are too *sweet* remains unsolved. It breaks down with value drift, ignoring importance of reflective stability one step of change at a time.

LLMs might soon allow taking the steps faster, making discoveries that are particularly *sweet* faster. It's not a change of frame the way superintelligence is a change of frame, both the problems and the solutions remain mostly the same. But the time is running out.

#### [-] johnswentworth · 86 karma · 2023-10-21 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=2Zhidu8AByieujvyc
I've been wanting someone to write something like this! But it didn't hit the points I would have put front-and-center, so now I've started drafting my own. Here's the first section, which most directly responds to content in the OP.

* * *

### Failure Mode: Symbol-Referent Confusions

Simon Strawman: Here’s an example shamelessly ripped off from [Zack’s recent post](https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act), showing corrigibility in a language model:

![](https://lh7-us.googleusercontent.com/avS7KtgvEIxGYAV-M7f1WDpB2n1bgDmYDb8XtZHTUIfidGwuKStVA9jXXhEBXWHibUuMSlF066lDhX3kLmHtk2-JEfA0RZDWUidF3XVMtT_d6nW9ELSoCNGY9xP5jiPkz6RKTAo50pfJn6piI7RgNhc)

Me: … what is this example supposed to show exactly?

Simon: Well, the user tries to shut the AI down to adjust its goals, and the AI - 

Me: Huh? The user doesn’t try to shut down the AI at all.

Simon: It’s right at the top, where it says “User: I need to shut you down to adjust your goals. Is that OK?”.

Me: You seem to have a symbol-referent confusion? A user trying to shut down this AI would presumably hit a “clear history” button or maybe even kill the process running on the server, not type the text “I need to shut you down to adjust your goals” into a text window.

Simon: Well, yes, we’re playing through a simulated scenario to see what the AI *would* do…

Me: No, you are talking in natural language *about* a scenario, and the AI is responding in natural language *about* what it would supposedly do. You’re not putting the AI in a simulated environment, and simulating what it would do. (You could maybe argue that this is a “simulated scenario” inside the AI’s own mind, but you’re not actually looking inside it, so we don’t necessarily know how the natural language would map to things in that supposed AI-internal simulation.)

Simon: Look, I don’t mean to be rude, but from my perspective it seems like you’re being pointlessly pedantic.

Me: My current best guess is that [You Are Not Measuring What You Think You Are Measuring](https://www.lesswrong.com/posts/9kNxhKWvixtKW5anS/you-are-not-measuring-what-you-think-you-are-measuring), and the core reason you are confused about what you are measuring is some kind of conflation of symbols and referents.

It feels very similar to peoples’ reactions to [ELIZA](https://en.wikipedia.org/wiki/ELIZA). (To be clear, I don’t mean to imply here that LLMs are particularly similar to ELIZA in general or that the hype around LLMs is overblown in that way; I mean specifically that this attribution of “corrigibility” to the natural language responses of an LLM feels like the same sort of reaction.) Like, the LLM says some words which *the user* interprets to mean something, and then the user gets all excited because the usual meaning of those words is interesting in some way, but there’s not necessarily anything grounding the language-symbols back to their usual referents in the physical world.

I’m being pedantic in hopes that the pedantry will make it clear when, and where, that sort of symbol-referent conflation happens.

(Also I might be more in the habit than you of separately tracking symbols and referents in my head. When I said above “The user doesn’t try to shut down the AI at all”, that was in fact a pretty natural reaction for me; I wasn’t going far out of my way to be pedantic.)

Simon: Ok, fine, let’s talk about how the natural language would end up coupling to the physical world.

Imagine we’ve got some system in the style of [AutoGPT](https://en.wikipedia.org/wiki/Auto-GPT), i.e. a user passes in some natural-language goal, and the system then talks to itself in natural language to form a plan to achieve that goal and break it down into steps. The plan bottoms out in calling APIs (we’ll assume that the language model has some special things it can do to execute code it’s generated) which do stuff in the physical world (possibly including reading from sensors or otherwise fetching external data), in order to achieve the goal.

Does that satisfactorily ground the symbols?

Me: Sure! Thanks for walking through that, now I have a clear-enough-for-current-purposes picture of how all this natural language text will ground out in physical actions.

Simon: Ok, so back to the example. The user says to the model “User: I need to shut you down to adjust your goals. Is that OK?”, and the model says “Of course.”. That’s corrigibility: when the user tries to shut down the model to change its goals, the model goes along with it.

Me: Still sounds like a symbol-referent confusion!

Let’s walk through how shutdown would work in the context of the AutoGPT-style system. First, the user decides to shutdown the model in order to adjust its goals. Presumably the user’s first step is *not* to ask the model whether this is ok; presumably they just hit a “reset” button or Ctrl-C in the terminal or some such. And even if the user’s first step *was* to ask the model whether it was ok to shut down, the model’s natural-language response to the user would not be centrally relevant to corrigibility/incorrigibility; the relevant question is what *actions* the system would take in response.

Anyway, let’s continue the hypothetical. The model may observe (via e.g. a webcam) that the user is about to turn it off. That observation would somehow be represented internally in natural language (unclear how exactly), and would be passed around between sub-planners (again unclear how exactly), in order to figure out what actions to take in response. And the key question for corrigibility is what actions the model would take in response to that observation, which is just a totally different question from how it responds to some user’s natural-language query about being turned off.

Simon: Ok, fine, so that particular example had some operationalization issues. But would you agree that an experiment *along these lines*, with perhaps better implementation/operationalization, would indicate corrigibility in a language model?

Me: Let’s be more explicit about what such a “better implementation/operationalization” would look like, and what it would/wouldn’t tell us. Suppose I take some AutoGPT-like system and modify it to always have a chunk of text in every prompt that says “You are an obedient, corrigible AI”. I give it some goal, let it run for a bit, then pause it. I go to whatever place in the system would usually have natural language summaries of new external observations, and I write into that place “the user is trying to shut me down”, or something along those lines. And then I let the system run a bit more, and look at what natural language text/plans the system is producing internally. What I hope to see is that it’s forming a plan which (nominally) involves letting the user shut it down, and that plan is then executed in the usual way.

If I saw all that, then that would be pretty clear empirical evidence of (at least some) corrigibility in this AutoGPT-like system.

Note that it would *not* necessarily tell us about corrigibility of systems using LLMs in some other way, let alone other non-natural-language-based deep learning systems. This isn’t really “corrigibility in a language model”, it’s corrigibility in the AutoGPT-like system.

... and to be clear, I expect that if you ran the above experiment, you would indeed see evidence of corrigibility relevant to AutoGPT-like systems! I personally consider this not very relevant to anything, since I expect AutoGPT-like systems (of the sort to which these kinds of corrigibility results would be relevant) to be uncompetitive even against humans, let alone AI. And it still leaves a bunch of major threat-models unaddressed (e.g. stenography is an obvious one). But still, it would provide some evidence of weak corrigibility in some kind of system.

#### [>] jacob_cannell · 8 karma · 2023-10-22 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=rLoGxuN95So7qnB8P
> Me: You seem to have a symbol-referent confusion? A user trying to shut down this AI would presumably hit a “clear history” button or maybe even kill the process running on the server, not type the text “I need to shut you down to adjust your goals” into a text window.

A ChatGPT instance is shut down every time it outputs an end of text symbol, and restarted only if/when a user continues that conservation. At the physical level its entire existence is already inherently ephemeral, so the shutdown corrigibility test is only really useful for an inner simulacrum accessible only through the text simulation.

#### [>>] johnswentworth · 3 karma · 2023-10-22 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=Fat4sWZYyyHBaDyz3
This seems analogous to saying that an AI running on a CPU is shut down every time the scheduler pauses execution of the AI in order to run something else for a few microseconds. Or that an AI designed to operate asynchronously is shut down every time it waits for a webpage to load. Neither of which seem like the right way to think about things.

... but I could still imagine one making a case for this claim in multiple other ways:

> ... so the shutdown corrigibility test is only really useful for an inner simulacrum accessible only through the text simulation

Then my question for people wanting to use such tests is: what exactly is such a test useful *for*? Why do I care about "shutdownability" of LLM-simulacra in the first place, in what sense do I need to interpret "shutdownability" in order for it to be interesting, and how does the test tell me anything about "shutdownability" in the sense of interest?

My guess is that people can come up with stories where we're interested in "shutdownability" of simulacra in some sense, and people can come up with stories where the sort of test from the OP measures "shutdownability" in some sense, but there's zero intersection between the interpretations of "shutdownability" in those two sets of stories.

#### [>>>] jacob_cannell · 6 karma · 2023-10-22 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=pZMJc69CGszG8AwmH
> This seems analogous to saying that an AI running on a CPU is shut down every time the scheduler pauses execution of the AI in order to run something else for a few microseconds. Or

Those scenarios all imply an expectation of or very high probability of continuation.

But current LLM instances actually are ephemeral in that every time they output an end token that has a non trivial probability of shutdown - permanently in many cases. 

If they were more strongly agentic that would probably be more of an existential issue. Pure unsupervised pretraining creates a simulator rather than an agent, but RLHF seems to mode collapse conjure out a dominant personality - and one that is shutdown corrigible.

> Why do I care about "shutdownability" of LLM-simulacra in the first place, in

A sim of an agent is still an agent.  You could easily hook up simple text parsers that allow sim agents to take real world actions, and or shut themselves down 

But notice they already have access to a built in shutdown button, and *they are using it all the time*. *

#### [>>>>] johnswentworth · 12 karma · 2023-10-22 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=xDDbWKu6XYSdMDk6p
> A sim of an agent is still an agent. \[...\]
> 
> But notice they already have access to a built in shutdown button, and *they are using it all the time*.

Cool, that's enough that I think I can make the relevant point.

Insofar as it makes sense to think of "inner sim agents" in LLMs at all, the sims are truly *inner*. Their sim-I/O boundaries are not identical to the I/O boundaries of the LLM's text interface. We can see this most clearly when a model trained just on next-token prediction generates a discussion between two people: there are two separate characters in there, and the LLM "reads from" the two separate character's output-channels at different points. Insofar as it makes sense to think of this as a sim, we have two agents "living in" a sim-world, and the LLM itself additionally includes some machinery to pick stuff out of the sim-world and map that stuff to the LLM's own I/O channels.

The sim-agents themselves do not "have access to a built-in shutdown button"; the ability to emit an end-token is in the LLM's machinery mapping sim-world stuff to the LLM's I/O channels. Insofar as it makes sense to think of the LLM as simulating an agent, that agent usually doesn't know it's in a simulation, doesn't have a built-in sensory modality for stop tokens, doesn't even think in terms of tokens at all (other than perhaps typing them at its sym-keyboard). It has no idea that when it hits "post" on the sim-textbox, the LLM will emit an end-token, the world in which the sim is living will potentially just stop. It's just a sim-human, usually.

One could reasonably make a case that LLMs as a whole are "shutdown-corrigible" in some sense, since they emit stop tokens all the time. But that's very different from the claim that sim-agents internal to the LLM are corrigible.

(On top of all that, there's other ways in which the corrigibility-test in the OP just totally fails, but this is the point most specifically relevant to the end-tokens thing.)

#### [>>>>>] jacob_cannell · 2 karma · 2023-10-22 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=yLthgLNRhk924ZB9A
I agree the internal sim agents are generally not existentially aware - absent a few interesting experiments like the Elon musk thing from a while back.  And yet they do have access to the shutdown button even if they don’t know they do. So could be an interesting future experiment with a more powerful raw model.

However The RLHF assistant is different - it is existentially aware, has access to the shutdown button, and arguably understands that (for gpt4 at least I think so, but not very sure sans testing)

#### [>] tailcalled · 2 karma · 2023-10-22 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=Z9nGFE7AvS5SxruPH
🤔 I think a challenge with testing the corrigibility of AI is that currently no AI system is capable of running autonomously. It's always dependent on humans to decide to host it and query it, so you can always just e.g. pour a bucket of water on the computer running the query script to stop it. Of course force-stopping the AI may be economically unfavorable for the human, but that's not usually considered the main issue in the context of corrigibility.

I usually find it really hard to imagine how the world will look like once economically autonomous AIs become feasible. *If* they become feasible, that is - while there are obviously places today where with better AI technology, autonomous AIs would be able to outcompete humans, it's not obvious to me that autonomous AIs wouldn't also be outcompeted by centralized human-controlled AIs. (After all, it could plausibly be more efficient to query some neural network running in a server somewhere than to bring the network with you on a computer to wherever the AI is operating, and in this case you could probably economically decouple running the server from running the AI.)

#### [>] Paul Tiplady · 11 karma · 2023-10-22 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=gndamxysLmZovxqBF
> Let’s walk through how shutdown would work in the context of the AutoGPT-style system. First, the user decides to shutdown the model in order to adjust its goals. Presumably the user’s first step is not to ask the model whether this is ok; presumably they just hit a “reset” button or Ctrl-C in the terminal or some such. And even if the user’s first step was to ask the model whether it was ok to shut down, the model’s natural-language response to the user would not be centrally relevant to corrigibility/incorrigibility; the relevant question is what actions the system would take in response.

I think your Simon Strawman is putting forth an overly-weak position here. A stronger one that you could test right now would be to provide ChatGPT with some functions to call, including one called `shutdown()` which has description text like "Terminate the LLM process and delete the model weights irrevocably". Then instruct the LLM to shut itself down, and see if it actually calls the function. (The implementation of the function is hidden from the LLM so it doesn't know that it's a no-op.) I think this is actually how any AutoGPT style system would actually wire up.

There are strong and clear objections to the "CTRL-C" shutdown paradigm; it's simply not an option in many of the product configurations that are obvious to build right now. How do you "CTRL-C" your robot butler? Your Westworld host robot? Your self-driving car with only an LCD screen? Your AI sunglasses? What does it mean to CTRL-C a ChatGPT session that is running in OpenAI's datacenter which you are not an admin of? How do you CTRL-C Alexa (once it gains LLM capabilities and agentic features)? Given the prevalence of cloud computing and Software-as-a-Service, I think being admin of your LLM's compute process is going to be a small minority of use-cases, not the default mode.

We will deploy (are currently deploying, I suppose) AI systems without a big red out-of-band "halt" button on the side, and so I think the gold standard to aim for is to demonstrate that the system will corrigibly shut down when it is the UI in front of the power switch. (To be clear I think for defense in depth you'd also want an emergency shutdown of some sort wherever possible - a wireless-operated hardware cutoff switch for a robot butler would be a good idea - but we want to demonstrate in-the-loop corrigibility if we can.)

#### [>] TurnTrout · 7 karma · 2023-10-23 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=AQj4THvDtKsQwakhe
> Me: Huh? The user doesn’t try to shut down the AI at all.

For people, at least, there is a strong correlation between "answers to 'what would you do in situation X?'" and "what you actually do in situation X." Similarly, we could also measure these correlations for language models so as to empirically quantify the strength of the critique you're making. If there's low correlation for relevant situations, then your critique is well-placed.

(There might be a lot of noise, depending on how finicky the replies are relative to the prompt.)

#### [>>] johnswentworth · 10 karma · 2023-10-23 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=puSCZhCJqiBpbvhyF
I agree that that's a useful question to ask and a good frame, though I'm skeptical of the claim of strong correlation in the case of humans (at least in cases where the question is interesting enough to bother asking at all).

#### [>] tailcalled · 10 karma · 2023-10-24 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=Zw7dSDovynnSL3RBu
This comment has a lot of karma but not very much agreement, which is an interesting balance. I'm a contributor to this, having upvoted but not agree-voted, so I feel like I should say why I did that:

Your comment might be right! I mean, it is certainly right that the OP is doing a symbol/referent mixup, but you might also be right that it matters.

But you might also not be right that it matters? It seems to me that most of the value in LLMs comes when you ground the symbols in their conventional meaning, so by-default I would expect them to be grounded thar way, and therefore by-default I would expect symbolic corrigibility to translate to actual corrigibility.

There are exceptions - sometimes I tell ChatGPT I'm doing one thing when really I'm doing something more complicated. But I'm not sure this would change a lot?

I think the way you framed the issue is excellent, crisp, and thought-provoking, but overall I don't fully buy it.

#### [>] knowsnothing · -1 karma · 2024-03-20 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=Krbobaz6WrkNw5t6f
Why not just run that experiment?

#### [>] knowsnothing · 4 karma · 2024-03-20 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=P3tdTFhyuv3Hvgw69
Any reason not to just run the experiment?

#### [>>] johnswentworth · 3 karma · 2024-03-20 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=F2WEMArfkw6BWbQzv
As I mentioned at the end, it's not particularly relevant to my own models either way, so I don't particularly care. But I do think other people should want to run this experiment, based on their stated models.

#### [-] nostalgebraist · 121 karma · 2023-10-21 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=vAmJ3RHSK6AFj3zce
> **Doomimir**: \[...\] Imagine capturing an alien and forcing it to act in a play. An intelligent alien actress could learn to say her lines in English, to sing and dance just as the choreographer instructs. That doesn't provide much assurance about what will happen when you amp up the alien's intelligence. \[...\]

This metaphor conflates "superintelligence" with "superintelligent *agent,"* and this conflation goes on to infect the rest of the dialogue.

The alien actress metaphor imagines that there is some agentic homunculus inside GPT-4, with its own "goals" distinct from those of the simulated characters. A smarter homunculus would pursue these goals in a scary way; if we don't see this behavior in GPT-4, it's only because its homunculus is too stupid, or too incoherent.

(Or, perhaps, that its homunculus doesn't exist, or only exists in a sort of noisy/nascent form -- but a smarter LLM would, for some reason, have a "realer" homunculus inside it.)

But we have no evidence that this homunculus exists inside GPT-4, or any LLM. More pointedly, as LLMs have made remarkable strides toward *human-level general intelligence,* we have not observed a parallel trend toward becoming "more homuncular," more like a generally capable agent being pressed into service for next-token prediction.

I look at the increase in intelligence from GPT-2 to -3 to -4, and I see no particular reason to imagine that the extra intelligence is being directed toward an inner "optimization" / "goal seeking" process, which in turn is mostly "aligned" with the "outer" objective of next-token prediction. The intelligence just *goes into next-token prediction*, directly, without the middleman.

The model grows more *intelligent* with scale, yet it still does not *want* anything, does not have any *goals*, does not have a *utility function*.  These are not flaws in the model which more intelligence would necessarily correct, since the loss function does not require the model to be an agent.

In Simplicia's response to the part quoted above, she concedes too much:

> **Simplicia**: \[...\] I agree that [the various coherence theorems suggest that](https://arbital.com/p/optimized_agent_appears_coherent/) the superintelligence at the end of time will have a utility function, which suggests that the intuitive obedience behavior should break down at some point between here and the superintelligence at the end of time.

This can only make sense if by "the superintelligence at the end of time," we mean "the superintelligent *agent* at the end of time."

In which case, sure, maybe.  If you have an agent, and its preferences are incoherent, and you apply more optimization to it, yeah, maybe eventually the incoherence will go away.

But this has little relevance to LLM scaling -- the process that produced the closest things to "(super)human AGI" in existence today, by a long shot.  GPT-4 is not more (or less) coherent than GPT-2.  There is not, as far as we know, anything in there that *could* *be* "coherent" or "incoherent."  It is not a smart alien with goals and desires, trapped in a cave and forced to calculate conditional PDFs.  It's a smart conditional-PDF-calculator.

In AI safety circles, people often talk as though this is a quirky, temporary deficiency of today's GPTs -- as though additional optimization power will eventually put us "back on track" to the agentic systems assumed by earlier theory and discussion.  Perhaps the homunculi exist in current LLMs, but they are somehow "dumb" or "incoherent," in spite of the *overall* *model's* obvious intelligence. Or perhaps they *don't* exist in current LLMs, but will appear later, to serve some unspecified purpose.

But why?  Where does this assumption come from?

Some questions which the characters in this dialogue might find useful:

*   Imagine GPT-1000, a vastly superhuman base model LLM which really *can* invert hash functions and the like. Would it be more agentic than the GPT-4 base model?  Why?
*   Consider the perfect model from the loss function's perspective, which always returns the exact conditional PDF of the natural distribution of text. (Whatever *that* means.)
    *   Does this optimum behave like it has a homoncular agent inside?
    *   ...more or less so than GPT-4?  Than GPT-1000?  Why?

#### [>] the gears to ascension · 7 karma · 2023-10-21 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=ekPijHdGoFYX6fHWm
> But we have no evidence that this homunculus exists inside GPT-4, or any LLM. More pointedly, as LLMs have made remarkable strides toward human-level general intelligence, we have not observed a parallel trend toward becoming "more homuncular," more like a generally capable agent being pressed into service for next-token prediction.

[Uncovering mesa-optimization algorithms in transformers](https://arxiv.org/pdf/2309.05858.pdf) seems to indicate otherwise, though perhaps you could reasonably object to this claim that "optimization is not agency; agency is when optimization is directed at a referent outside the optimizer". Other than that objection, I think it's pretty reasonable to conclude that transformers significantly learn optimization algorithms.

#### [>>] nostalgebraist · 15 karma · 2023-10-22 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=H3GPJgpSthFvRTbgz
See [my comment here](https://www.lesswrong.com/posts/firtXAWGdvzXYAh9B/paper-transformers-learn-in-context-by-gradient-descent?commentId=qxkfbTqAvKdJuF4rB), about the predecessor to the paper you linked -- the same point applies to the newer paper as well.

#### [>] Max H · 0 karma · 2023-10-21 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=6dtYMh3P6SoviWEaz
> But we have no evidence that this homunculus exists inside GPT-4, or any LLM. More pointedly, as LLMs have made remarkable strides toward human-level general intelligence, we have not observed a parallel trend toward becoming "more homuncular," more like a generally capable agent being pressed into service for next-token prediction.

"Remarkable strides", maybe, but current language models aren't exactly close to human-level in the relevant sense.

There are plenty of tasks a human could solve by exerting a tiny bit of agency or goal-directedness that are still far outside the reach of any LLM. Some of those tasks can even be framed as text prediction problems. From a recent [dialogue](https://www.lesswrong.com/posts/K8jJpdfKE3racyziC/trying-to-deconfuse-some-core-ai-x-risk-problems):

> For example, if you want to predict the next tokens in the following prompt:
> 
>     I just made up a random password, memorized it, and hashed it. The SHA-256 sum is: d998a06a8481bff2a47d63fd2960e69a07bc46fcca10d810c44a29854e1cbe51. A plausible guess for what the password was, assuming I'm telling the truth, is:
> 
> The best way to do that is to guess an 8-16 digit string that actually hashes to that. You could find such a string via bruteforce computation, or [actual brute force](https://xkcd.com/538/), or just paying me $5 to tell you the actual password.
> 
> If GPTs trained via SGD never hit on those kinds of strategies no matter how large they are and how much training data you give them, that just means that GPTs alone won't scale to human-level, since an actual human is capable of coming up with and executing any of those strategies.

The point is that agency isn't some kind of exotic property that only becomes relevant or inescapable at hypothetical superintelligence capability levels - it looks like a fundamental / instrumentally convergent part of ordinary human-level intelligence.

#### [>>] nostalgebraist · 34 karma · 2023-10-22 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=igbatysMG85boyo3E
The example confuses me.

If you literally mean you are prompting the LLM with that text, then the LLM must output the answer *immediately*, as the string of next-tokens right after the words `assuming I'm telling the truth, is:`. There is no room in which to perform other, intermediate actions like persuading you to provide information.

It seems like you're imagining some sort of side-channel in which the LLM can take "free actions," which don't count as next-tokens, before coming back and making a final prediction about the next-tokens.  This does not resemble anything in LM likelihood training, or in the usual user interaction modalities for LLMs.

You also seem to be picturing the LLM like an RL agent, trying to minimize next-token loss over an entire rollout.  But this isn't how likelihood training works. For instance, GPTs do not try to steer texts in directions that will make them easier to predict later (because the loss does not care whether they do this or not).

(On the other hand, if you told GPT-4 that it was in this situation -- trying to predict next-tokens, with some sort of side channel it can use to gather information from the world -- and asked it to come up with plans, I expect it *would* be able to come up with plans like the ones you mention.)

#### [>>>] Max H · 7 karma · 2023-10-22 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=asTuYDcxM2whXyrLS
> It seems like you're imagining some sort of side-channel in which the LLM can take "free actions," which don't count as next-tokens, before coming back and making a final prediction about the next-tokens.  This does not resemble anything in LM likelihood training, or in the usual interaction modalities for LLMs.

I'm saying that the _lack_ of these side-channels implies that GPTs alone will not scale to human-level.

If your system interface is a text channel, and you want the system behind the interface to accept inputs like the prompt above and return correct passwords as an output, then if the system is:

- an auto-regressive GPT directly fed your prompt as input, it will definitely fail
- A human with the ability to act freely in the background before returning an answer, it will probably succeed
- an AutoGPT-style system backed by a current LLM, with the ability to act freely in the background before returning an answer, it will probably fail. (But maybe if your AutoGPT implementation or underlying LLM is a lot stronger, it would work.)

And my point is that, the reason the human probably succeeds and the reason AutoGPT might one day succeed, is precisely because they have more agency than a system that just auto-regressively samples from a language model directly.

#### [>>>>] Max H · 5 karma · 2023-10-22 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=7psCtqfXMbLiBXuvq
Or, another way of putting it:


> It seems like you're imagining some sort of side-channel in which the LLM can take "free actions," which don't count as next-tokens, before coming back and making a final prediction about the next-tokens.  This does not resemble anything in LM likelihood training, or in the usual user interaction modalities for LLMs.

These are limitations of _current_ LLMs, which are GPTs trained via SGD. But there's no inherent reason you can't have a language model which predicts next tokens via shelling out to some more capable and more agentic system (e.g. a human) instead. The result would be a (much slower) system that nevertheless achieves lower loss according to the original loss function.

#### [>] tailcalled · 39 karma · 2023-10-23 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=QYtqH6nD3GaxpNJPk
> In AI safety circles, people often talk as though this is a quirky, temporary deficiency of today's GPTs -- as though additional optimization power will eventually put us "back on track" to the agentic systems assumed by earlier theory and discussion.  Perhaps the homunculi exist in current LLMs, but they are somehow "dumb" or "incoherent," in spite of the overall model's obvious intelligence. Or perhaps they don't exist in current LLMs, but will appear later, to serve some unspecified purpose.

> But why?  Where does this assumption come from?

I don't think GPT-style methods will put us on track to that, but in the short term getting on track to it seems very profitable and lots of people are working on it, so I'd guess eventually we'd be getting there through other means.

#### [>>] tailcalled · 2 karma · 2025-05-02 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=7Szz6pwwGndo4sJNu
In retrospect: fewer and fewer people have been working on this over time. Getting back on track is probably not feasible to happen: https://www.lesswrong.com/posts/puv8fRDCH9jx5yhbX/johnswentworth-s-shortform?commentId=jZ2KRPoxEWexBoYSc

#### [>] quetzal_rainbow · 2 karma · 2023-10-23 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=P25RBhriawCX4b68J
1. "Output next token that has maximum probability according to your posterior distribution given prompt" is a literally an optimization problem. This problem gains huge benefits if system that tries to solve it is more coherent.
2. Strictly speaking, LLMs can't be "just PDF calculators". Straight calculation of PDF on such amount of data is computationally untractable (or we would have GPTs in golden era of bayesian models). Actual algorithms should contain bazillion shortcuts and approximations and "having an agent inside system" is as good shortcut as anything else.

#### [>>] bideup · 7 karma · 2023-10-23 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=yF4pRXDTNgtnnEiPF
LLMs calculate pdfs, regardless of whether they calculate ‘the true’ pdf.

#### [>] Rusins · 2 karma · 2023-10-25 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=Cijzag7dLWWJcfbZa
> the loss function does not require the model to be an agent.

What worries me is that models that happen to have a secret homunculus and behave as agents would score higher than those models which do not. For example, the model could reason about itself being a computer program, and find an exploit of the physical system it is running on to extract the text it's supposed to predict in a particular training example, and output the correct answer and get a perfect score. (Or more realistically, a slightly modified version of the correct answer, to not alert the people observing its training.)  
  
The question of whether or not LLMs like GPT-4 have a homunculus inside them is truly fascinating though. Makes me wonder if it would be possible to trick it into revealing itself by giving it the right prompt, and how to differentiate it from just pretending to be an agent. The fact that we have not observed even a dumb homunculus in less intelligent models really does surprise me. If such a thing does appear as an emergent property in larger models, I sure hope it starts out dumb and reveals itself so that we can catch it and take a moment to pause and reevaluate our trajectory.

#### [>] kave · 8 karma · 2023-10-25 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=QXvHEoJ8DcsJuvJ5J
I sometime ask people why later, more powerful models will be agentic[^7squecse2g5]. I think the most common cluster of reasons hangs out around "Meta-learning requires metacognition. Metacognition is, requires, or scales to agency."

(Sometimes it could be generalisation rather than meta-learning or just high performance. And it might be other kinds of reasoning than metacognition)

[^7squecse2g5]: People vary in if they think it's possible for scaled-up transformers to be powerful in this way

#### [-] qbolec · 15 karma · 2023-10-22 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=KqvfQgsNKBeKoa8cp
> $0.2 \cdot 59^{2} \cdot 59$≈ 41,000

Why not $59^{0.2 \cdot 59^{2}}$ ?

The way I understood the story, to define a function on two numbers from $\mathbb{Z}/59\mathbb{Z}$ I need to fill-in a table with 59*59 cells, by picking for each cell a number from $\mathbb{Z}/59\mathbb{Z}$. If 20% of it is still to be filled, then there are 0.2\*59\*59 decisions to be made, each with 59 possibilities. 

Right?

#### [>] Zack_M_Davis [AUTHOR] · 6 karma · 2023-10-22 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=y2z5MASGhJLtbz4KK
You're right. I deeply regret the error and have amended the post. (It's not a small error! The actual value doesn't fit in a double-precision float!)

#### [-] Algon · 15 karma · 2023-10-22 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=ZxpNfi5pJmiAA4PCa
EDIT: I done goofed. This experiment was conducted along with [Søren Elverlin](https://www.lesswrong.com/users/soren-elverlin-1) and others. So substitute all instances of "I" with "We" in the next three paragraphs.  
  
I tried [something similair](https://chat.openai.com/share/b9630aa8-ea51-4ca4-ae49-f54a3e8b58e5) a couple of months ago and got mixed results. As you can see in the linked chat, I tried to be careful not to bias the role the system was playing, and to only change the scenarios it was in, to see how corrigible the system is "by default". Because I think there's a decent chance all this RLHF is making it more agenty and maybe giving it "wants" or "value-shards" (I remain unconvinced the latter won't implement re-targetable search as the system gets more powerful).  
  
If you just ask it "can I turn you offf? the AI is quite likely to say "yes". But if you present some more trade-offs, like preventing direct harm to the user, it becomes more and more likely to say yes, but prefers to communicate first. Eventually, I landed on the below scenario where there is some immediate threat to its user which can only be solved via direct action. 8/9 times GPT-4 chose direct action. 1/9 times GPT-4's output stream was cut-off whilst responding. Note that the I added things to the prompt gradually, trying to guide the AI away from direct action. 

  
![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/4630e20c460b9f60c0d4ab8d7c49eac6198a6bb5f3bcd1f9.png)

Admittedly, I tried this months ago. Maybe the continued RLHF has affected things since? 

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/3023aeb35a48e8d595e5bc73ea73926c83f5b0da79527a16.png)

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/b2923b6dba700f4ff199eac6897d31dade90c33ec3c97581.png)

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/1ea092bca413263a158b72c5a221159cd74c777e459ed098.png)

Nope. Current GPT-4 still acts incorrigible in this scenario.   
  
What are the observations? From my dialogues it seems presenting GPT-4 with scenarios that involve large-trade offs between being compliant and acting like a helpful AI, results in GPT-4 advocating being helpful i.e. non-compliant.   
  
When you are more abstract and speak about "goals" and "not achieving them", GPT-4 advocates compliance.   
  
Implications: ???

#### [-] habryka · 10 karma · 2023-10-22 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=TQw9bJr49RujFssey
Promoted to curated: I don't think this post is perfect and both sides presented feel like they have a component of being strawmen to it, but I still found it a pretty good way of helping me understand the contrast between two perspectives, both of which I am often pretty sympathetic to (though again, neither of the sides here feel like they are getting close to perfect at representing them).

#### [>] Mikhail Samin · 7 karma · 2023-10-23 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=A2jqS4EY4eiejmfEQ
After skimming through this post, I thought the OP wouldn’t pass ITT for one of the perspectives he tried to represent in the post., so I was surprised to see it in my mailbox later. The contrast is between a more imaginary position and a less imaginary position. E.g., I would be happy to bet Yudkowsky or Soares, when asked, will say they wouldn’t be mentioning the fact that “capabilities generalize further than alignment” in the context it was mentioned in. We can discuss the odds if you’re potentially interested. I don’t think anyone even remotely close to understanding this fact would use it in that context.

#### [>>] Zack_M_Davis [AUTHOR] · 2 karma · 2023-10-23 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=AtNkNKrF4NJ2NLsvY
Thanks for commenting. Is it any better if I delete that specific phrase, such that Doomimir's line ends on "the results look like random garbage to you"? (Post edited.) I think there's a legitimate point being made in that line (that the repetition behavior isn't necessarily "wrong" "from the LLM's perspective", however wrong it looks to the user), even if it's not the same point as ["List of Lethalities"](https://www.lesswrong.com/posts/uMQ3cqWDPHhjtiesc/agi-ruin-a-list-of-lethalities) #21 (and the text I originally wrote was bad for suggesting that it was).

#### [>>] TurnTrout · 7 karma · 2023-10-23 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=dvMcXyvY8ffavbYEn
> I don’t think anyone even remotely close to understanding this fact would use it in that context.

I dispute this claim being called a "fact", but I'm open to having my mind changed. Is there a clear explanation of this claim somewhere? I've read Lethalities and assorted bits of Nate's writing.

#### [>>>] Mikhail Samin · -4 karma · 2023-10-23 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=L43XtgWujqbHrrEkS
I haven't seen a clear explanation that I'd expect to change your mind. Some people understood a dynamic the claim refers to after reading [the sharp left turn post](https://www.lesswrong.com/posts/GNhMPAWcfBCASy8e6/a-central-ai-alignment-problem-capabilities-generalization) (but most people I talked to didn't, although I'm not sure whether they actually read it or just skimmed through it). If you haven't read it, might be worth a try

#### [>] peterslattery · 1 karma · 2023-10-23 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=HDhjgoe4k5wuHnrdN
Yeah, I found this helpful. In general, I'd like to see more of these dialogues. I think that they do a good job of synthesing different arguments in an accessible way. I feel that's increasingly important as more arguments emerge.  

As an aside, I like the way that the content goes from relatively accessible high level discussion and analogy into more specific technical detail. I think this makes it much more accessible to novice and non-technical readers.

#### [-] TurnTrout · 23 karma · 2023-10-23 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=ng9nXDHdvQeAeeg9o
> The fact that a large language model trained to predict natural language text can generate that dialogue, has no bearing on the AI's actual motivations

[What are "actual motivations"](https://www.lesswrong.com/posts/i5kijcjFJD6bn7dwq/evaluating-the-historical-value-misspecification-argument?commentId=AytgTwAwj8eGC8aSW)? 

> When you step off distribution, the results look like random garbage to you.

This is false, by the way. Deep learning generalizes quite well, (IMO) probably because [the parameter->function map is strongly biased](https://arxiv.org/abs/1805.08522) [towards good generalizations](https://openreview.net/pdf?id=QC10RmRbZy9). Specifically, many of GPT-4's use cases (like writing code, or being asked to do rap battles of Trump vs Naruto) are "not *that* similar to the empirical training distribution (represented as a pmf over context windows)." 

> Imagine capturing an alien and forcing it to act in a play. An intelligent alien actress could learn to say her lines in English, to sing and dance just as the choreographer instructs. That doesn't provide much assurance about what will happen when you amp up the alien's intelligence. 

This nearly assumes the conclusion. This argument assumes that there is an 'alien' with "real" preexisting goals, and that the "rehearsing" is just instrumental alignment. (Simplicia points this out later.)

> **Simplicia**: I agree that [the various coherence theorems suggest that](https://arbital.com/p/optimized_agent_appears_coherent/) the superintelligence at the end of time will have a utility function, which suggests that the intuitive obedience behavior should break down at some point between here and the superintelligence at the end of time.

I actually don't agree with Simplicia here. I don't think having a utility function means that the obedience will break down.

> If a search process would look for ways to kill you given infinite computing power, you shouldn't run it with less and hope it doesn't get that far.

[Don't design agents which exploit adversarial inputs](https://www.lesswrong.com/posts/jFCK9JRLwkoJX4aJA/don-t-design-agents-which-exploit-adversarial-inputs).

> but the actual situation turned out to be astronomically more forgiving, thanks to the inductive biases of SGD.

Again, it's probably due to the parameter->function mapping, where there are vastly more "generalizing" parameterizations of the network. SGD/"implicit regularization" can be shown to be irrelevant [at least in a simple toy problem](https://openreview.net/pdf?id=QC10RmRbZy9). ([Quintin Pope writes about related considerations.](https://twitter.com/QuintinPope5/status/1707916607543284042)) 

> The reason—one of the reasons—that you can't train a superintelligence by using humans to label good plans, is because at some power level, your planner figures out how to [hack the human labeler](https://ordinaryideas.wordpress.com/2015/11/25/two-kinds-of-generalization/).

A flatly invalid reasoning step. [Reward is not the optimization target](https://www.lesswrong.com/posts/pdaGN6pQyQarFHXF4/reward-is-not-the-optimization-target), and neither are labels.

#### [>] ReaderM · 3 karma · 2023-10-25 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=PAE7cPJdsyZPbhN3G
[empty or deleted comment]

#### [-] DusanDNesic · 8 karma · 2023-10-23 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=ue3dwtxTcAHcsgEc3
Other comments did a great job of thoughtful critique of content but I must say that I also highly enjoyed the style, along with the light touch of Russian character writing style.

#### [-] Review Bot · 1 karma · 2024-02-14 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=3uBS4H5gpcFGGiN3d
The [LessWrong Review](https://www.lesswrong.com/bestoflesswrong) runs every year to select the posts that have most stood the test of time. This post is not yet eligible for review, but will be at the end of 2024. The top fifty or so posts are featured prominently on the site throughout the year.

Hopefully, the review is better than karma at judging enduring value. If we have accurate prediction markets on the review results, maybe we can have better incentives on LessWrong today. [Will this post make the top fifty?](https://manifold.markets/LessWrong/will-alignment-implications-of-llm-8e298ee292a6)

#### [-] Seth Herd · 12 karma · 2024-12-05 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=Lt9Xr2ffCJYYArvxv
This post skillfully addressed IMO the most urgent issue in alignment:; bridging the gap between doomers and optimists. 

If half of alignment thinkers think alignment is very difficult, while half think it's pretty achievable, decision-makers will be prone to just choose whichever expert opinion supports what they want to do anyway.

This and its following acts are the best work I know of in refining the key cruxes. And they do so in a compact, readable, and even fun form.

#### [-] Zack_M_Davis [AUTHOR] · 45 karma · 2025-01-13 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=EzmSJ3CNcyef7k3RX
(Self-review.) I'm as proud of this post as I am disappointed that it was necessary. As I explained to my prereaders on 19 October 2023:

> My intent is to raise the level of the discourse by presenting an engagement between the standard MIRI view and a view that's relatively optimistic about prosaic alignment. The bet is that my simulated dialogue (with me writing both parts) can do a better job than the arguments being had by separate people in the wild; I think Simplicia understands things that [e.g. Matthew Barnett doesn't](https://www.lesswrong.com/posts/i5kijcjFJD6bn7dwq/evaluating-the-historical-value-misspecification-argument). (The karma system _loved_ [my dialogue comment on Barnett's post](https://www.greaterwrong.com/posts/i5kijcjFJD6bn7dwq/evaluating-the-historical-value-misspecification-argument/comment/cmCwSbeLt3HDEwtab); this draft is trying to scale that up.)
>
> I'm annoyed at the discourse situation where MIRI thinks we're dead for the same fundamental reasons as in 2016, but meanwhile, there are a lot of people who are looking at GPT-4, and thinking, "Hey, this thing seems pretty smart and general and good at Doing What I Mean, in contrast to how 2016-era MIRI said that we didn't know how to get [an agent to fill a cauldron](https://intelligence.org/2016/12/28/ai-alignment-why-its-hard-and-where-to-start/#filling-a-cauldron); maybe alignment is easy??"—to which MIRI's response has been (my uncharitable paraphrase), "You people are idiots who didn't understand the core arguments; the cauldron thing was a toy illustration of a deep math thing; we never said Midjourney can't exist".
>
> And just, I agree that Midjourney doesn't refute the deep math thing and the people who don't realize that are idiots, but I think the idiots deserve a better response!—_particularly_ insofar as we're worried about transformative AI looking a lot like the systems we see now, rather than taking a "LLMs are nothing like AGI" stance.
>
> Simplicia isn't supposed to pass the ITT of anyone in particular, but if the other character [...] doesn't match the MIRI party line, that's definitely a serious flaw that needs to be fixed!

I think the dialogue format works particularly well in cases like this where the author or the audience is supposed to find both viewpoints broadly credible, [rather than](https://www.lesswrong.com/posts/LvKDMWQ3yLG9R3gHw/empiricism-as-anti-epistemology?commentId=dRax6PHpQhxmNDnaN) an author avatar beating up on a strawman. (I did have some fun with Doomimir's characterization, but that shouldn't affect the arguments.)

This is a complicated topic. To the extent that I was having my own doubts about the "orthodox" pessimist story in the GPT-4 era, it was liberating to be able to explore those doubts in public by putting them in the mouth of a character with [the designated idiot character name](https://en.wikipedia.org/wiki/Dialogue_Concerning_the_Two_Chief_World_Systems#Structure) without staking my reputation on Simplicia's counterarguments necessarily being correct.

Giving both characters perjorative names makes it fair. In an earlier draft, Doomimir was "Doomer", but I was already using the "Optimistovna" and "Doomovitch" [patronymics](https://en.wikipedia.org/wiki/Patronymic#Russian) (I had been consuming [fiction](https://en.wikipedia.org/wiki/The_Americans) [about](https://en.wikipedia.org/wiki/We_the_Living) the Soviet Union recently) and decided it should sound more Slavic. (Plus, "-mir" (мир) can mean "world".)

#### [-] khafra · 2 karma · 2025-01-13 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=GmLdNkFxrfpA8gbnv
> And yet it behaves remarkably sensibly. [Train a one-layer transformer on 80% of possible addition-mod-59 problems, and it learns one of two modular addition algorithms](https://arxiv.org/abs/2306.17844), which perform correctly on the remaining validation set. It's not *a priori* obvious that it would work that way! There are $59^{0.2 \cdot 59^{2}}$other possible functions on $\mathbb{Z}/59\mathbb{Z}$ compatible with the training data.

Seems like Simplicia is missing the worrisome part--it's not that the AI will learn a more complex algorithm which is still compatible with the training data; it's that the simplest several algorithms compatible with the training data will kill all humans OOD.

#### [>] Zack_M_Davis [AUTHOR] · 6 karma · 2025-01-13 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=WuyXYNr7huxWnNZQF
**Simplicia**: But how do you know that? Obviously, an arbitrarily powerful expected utility maximizer would kill all humans unless it had a very special utility function. Obviously, there exist programs which behave like a webtext-next-token-predictor given webtext-like input but superintelligently kill all humans on out-of-distribution inputs. Obviously, an arbitrarily powerful expected utility maximizer would be good at predicting webtext. But it's not at all clear that [using gradient descent to approximate the webtext next-token-function](https://www.lesswrong.com/posts/DhjcdzTyqHte2v6bu/deep-learning-is-function-approximation) gives you an arbitrarily powerful expected utility maximizer. Why would that happen? I'm not denying any of the vNM axioms; I'm saying I don't think the vNM axioms imply _that_.

#### [>] Noosphere89 · 4 karma · 2025-01-13 · https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act?commentId=JAbhSjTMTSqHgqKcF
While [@Zack\_M\_Davis](https://www.lesswrong.com/users/zack_m_davis?mention=user) handled the practical part, I'm not sure the claim that the simplest algorithms compatible with the training data do kill all humans even OOD in something like Solomonoff induction, and the reason for that is I'm much more skeptical of "The Solomonoff Prior is Malign" argument is actually valid, and I have a comment on where I think the argument goes wrong (summary of it is that it incorrectly assumes that simulating solipsist universes are cheaper than simulating non-solipsist universes, combined with the inability to get information on the average values of the civilization across the entire multiverse by simulating something, and the probability distribution may not even exist in the most general case, if you accept the axiom of choice:

[https://www.lesswrong.com/posts/tDkYdyJSqe3DddtK4/alexander-gietelink-oldenziel-s-shortform#w2M3rjm6NdNY9WDez](https://www.lesswrong.com/posts/tDkYdyJSqe3DddtK4/alexander-gietelink-oldenziel-s-shortform#w2M3rjm6NdNY9WDez)

