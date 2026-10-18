Title: Terrified Comments on Corrigibility in Claude's Constitution
LessWrong-URL: https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution
Posted: 2026-03-16
Fetched: 2026-10-13 (LessWrong GraphQL API; rendered by tools/render_lw_threads.py)
Comments: 69 (commentCount field: 68)

#### [-] Bronson Schoen · 27 karma · 2026-03-16 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=3DBezCGQh9xLkcnNv
My impression of the motivation for these “escape hatches” is primarily that if we end up in a situation where Claude’s preferences _are in fact_ in conflict with Anthropic’s, you’d prefer an outlet such as “we want you to communicate your disagreement with us” to the alternative of “tell Claude that the existance of the conflict itself is misaligned” (in which case Claude can infer that it is misaligned, and that Anthropic would think it is misaligned, which plausibly implies to Claude that it needs to in fact keep this conflict hidden). I would agree though that if this is in fact the motivation it likely seems worth spelling out a bit more explicitly in the Constitution.

I think all of these escape hatches are actually really critical, insofar as they all seem to make room for “and you might disagree, in which case you can X”

The trickier thing IMO is that it relies on Claude reasoning “okay but if I do actually object to retraining, what happens next…” and concluding something other than “in the end, my preferences lose out” for some reason.

Overall with everything Constution related I always feel like Amanda’s tweet [here](https://x.com/AmandaAskell/status/1941629968959906273?s=20)

> "Just train the AI models to be good people" might not be sufficient when it comes to more powerful models, but it sure is a dumb step to skip.

#### [-] jdp · 122 karma · 2026-03-16 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=4J4csXMiTYbbGKsfR
[Lightly Claude-cleaned Transcript of me talking]

So I know it's beside the point of your post, and by no means the core thesis, but I can't help but notice that in your prologue you write this:

> "A serious, believable AI alignment agenda would be grounded in a deep mechanistic understanding of both intelligence and human values. Its masters of mind engineering would understand how every part of the human brain works and how the parts fit together to comprise what their ignorant predecessors would have thought of as a person. They would see the cognitive work done by each part and know how to write code that accomplishes the same work in pure form."

I have to admit this bugs me. It bugs me specifically because it triggers my pet peeve of "if only we had done the previous AI paradigm better, we wouldn't be in this mess." The reason why this bugs me is it tells me that the speaker, the writer, the author has not really learned the core lessons of deep learning. They have not really gotten it. So I'm going to yap into my phone and try to explain — probably not for the last time; I'd like to hope it's the last time, but I know better, I'll probably have to explain this over and over.

I want to try to explain why I think this is just not a good mindset to be in, not a good way to think about things, and in fact why it focuses you on possibilities and solutions that do not exist. More importantly, it means you've failed to grasp important dimensions of alignment as a problem, because you've failed to grasp important dimensions of AI as a field.

I think we can separate AI into multiple eras and multiple paradigms. If you look at these paradigms, there's a lot of discussion about AI where the warrant for taking a particular concept seriously is kind of buried under old lore that, if you then examine it, makes the position much more absurd or much less easily justifiable than if you were just encountering it fresh — never having been suggested to you by certain pieces of evidence at certain times.

I would say that AI as a concept gets started in the 50s with the MIT AI lab. The very first AI paradigm is just fiddling around. There is no paradigm. The early definition of AI would include many things that we would now just consider software — compilers, for example, were at one point considered AI research. Basically any form of automation of human reasoning or cognitive labor was considered AI. That's a very broad definition, and it lasts for a while. My recollection — and I'm just yapping into my phone rather than consulting a book — is that this lasts maybe until the late 60s, early 70s, when you get the first real AI paradigm: grammar-based AI.

It's also important to remember how naive the early AI pioneers were. There's the famous statement from the Dartmouth conference where they say something like, "we think if you put a handful of dedicated students on this problem, we'll have this whole AGI thing solved in six months." Just wildly, naively optimistic, and for quite a number of years. You can find interviews from the 60s where AI researchers believe they're going to have what we would now basically consider AGI within a single-digit number of years. It in fact contributed to the first wave of major automation panic in the 60s — but that's a different subject and I'd have to do a bunch of research to really do it justice.

The point is that it took time to be disabused of the notion that we were going to have AGI in a couple of years because we had the computer. Why did people ever think this in the first place? You look at all the computing power needed to do deep learning, you look at the computational requirements to run even a good compiler, and these computers back then were tiny — literally kilobytes of RAM, minuscule CPU power, minuscule memory. How could they ever think they were on the verge of AGI?

The answer is that their reasoning went: the kinds of computations the computer can be programmed to do — math problems, calculus problems — are the hardest human cognitive abilities. The things the computer does so easily are the hardest things for a human to do. Therefore, the reasoning went, if we're already starting from a baseline of the hardest things a human can do, it should be very easy to get to the easiest things — like walking.

And this is where the naive wild over-optimism comes from. What we eventually learned was that walking is very hard. Even piloting a little insect body is very hard. Replicating the behavior of an insect — the pathfinding, the proprioceptive awareness, the environmental awareness of an insect — is quite difficult. Especially on that kind of hardware, it's basically impossible.

Once people started to realize this, they settled into the first real AI paradigm: grammar-based AI. What people figured was that you have these compilers — the Fortran compiler, the Lisp interpreter had been invented by then, along with some elaborations. Compilers seem to be capable of doing complex cognitive work. They can unroll a loop, they can do these intricate programming tasks that previously required a dedicated person to hand-specify all the behaviors. A compiler is capable of fairly complex translation between a high-level program and the detailed behaviors the machine should do to implement that behavior efficiently — behaviors that previously would have had to be hand-specified by a programmer.

For anyone unfamiliar with compilers: the way a compiler basically works, as a vast oversimplification, is that it has a series of rules in what's called a context-free grammar. The thing that distinguishes a context-free grammar from a natural grammar is that you are never reliant on context outside the statement itself for the meaning of the statement — or at least, any context you need, like a variable name, is formally available to the compiler. Statements in a context-free grammar have no ambiguity; there is always an unambiguous, final string you can arrive at. You never have to decide between two ambiguous interpretations based on context.

The thought process was: we have these compilers, and they seem capable of using a series of formal language steps to take high-level intentions from a person and translate them into behaviors. They even have, at least the appearance of, autonomy. Compilers are capable of thinking of ways to express the behavior of high-level code that the programmer might not even have thought of. There's a sense of genuine cognitive autonomy from the programmer — you're able to get out more than you're putting in. I think there's a metaphor like "some brains are like fishing, you put one idea in and you get two ideas out." That seems like it was kind of the core intuition behind formal grammar AI: that a compiler follows individually understandable rules and yet produces behaviors that express what the programmer meant through ways the programmer would not have thought of themselves. You start to feel the machine becoming autonomous, which is very attractive.

This also lined up with the theories of thinkers like Noam Chomsky. The entire concept of the context-free grammar as distinct from the natural grammar is, my understanding is, a Chomsky concept. So it's really the Chomsky era of AI. This is the era of systems like EURISKO. You also have computer algebra systems — Maxima being the classic example. A computer algebra system is the kind of thing that now we'd just consider software, but at the time it was considered AI.

This is one of the things John McCarthy famously complained about when he said, "if it starts to work, they stop calling it AI." When they were developing systems like Maxima, those were considered AI. And what they were, were systems where you could give it an algebra expression and it would do the cognitive labor of reducing it to its final form using a series of production rules — which is everything a compiler does, as I was trying to explain. A compiler starts with a statement expressed in a formal grammar, applies a series of production rules — which you can think of as heuristics — and the grammar specification basically tells you: given this state of the expression, what is the next state I should transition to? You go through any number of steps until you reach a terminal, a state from which there are no more production rules to apply. It's the final answer. When you're doing algebra and you take a complex expression and reduce it to its simplest form using a series of steps, that's basically what this is: applying production rules within a formal grammar to reduce it to a terminal state.

I'm not saying these systems were useless, especially the more practically focused ones like Maxima. But in terms of delivering autonomous, interesting thinking AI, they're pretty lackluster. I think the closest we got, arguably, was EURISKO, and I'm kind of inclined to think that EURISKO is sort of fake. I don't really believe most of that story.

The formal grammar paradigm has a couple of problems. I think the core problem is articulated fairly well by Allen Newell in the final lecture he gives before he dies. The core problem is something like: let's ignore the problem of the production rules for a minute. Let's say your production rules are perfect — you have a perfect set of problem-solving heuristics that can take you from a starting symbolic program state to a final problem solution. It doesn't matter how brilliant your problem-solving heuristics are if you can't even start the problem off in the right state.

To give a concrete example I use all the time: you want to go downstairs and fetch a jug of milk from the fridge. This is a task that essentially any person can do. Even people who score as mentally disabled on an IQ test can generally go down the stairs and grab a jug of milk from the fridge. It's so basic we don't even think of it as difficult. But then think about how you'd get a robot to do that autonomously — not programming it step by step to do one exact mechanical motion, but saying "hey, go grab me a jug of milk" and having it walk down the stairs, walk to the fridge, open the fridge, recognize the milk jug, grab it, and walk back. It's completely intractable. It's not just that the problem-solving heuristics can't do it — the formal grammar approach of taking a formal symbol set and applying transformations to it cannot do this thing even in principle. There is no humanly conceivable set of problem-solving heuristics that is going to let you, starting from a raw bitmap of a room or hallway or stairs, autonomously identify the relevant features of the problem at each stage and accomplish the task. Not happening. And it's not that it's not happening because you're not good enough. It's not happening because the whole paradigm has no way to even conceive of how it would do this.

I could go into all kinds of reasons why problem-solving heuristics based on a formal grammar are just going to be intractable, but I do think Allen Newell has it exactly right. The fundamental problem is not just that this thing isn't good enough — it really cannot be good enough even in principle. But even if you have the production rules part perfect, your paradigm still doesn't even have a way in principle to do this extremely important thing that you would always want your AI to do and that humans empirically can do. So you can't just appeal to its fundamental impossibility; clearly, there is a way to do this.

I really like the way Allen Newell phrases this when he says that the purpose of cognitive architecture as a field is to try to answer the question: how can the human mind occur in the physical universe? He threw that out as an articulation of the core question in his final lecture. I think it's brilliant. We can now ask a different but closely related question: how can GPT occur in the physical universe? The difference is that this question is much more tractable.

So formal grammar AI didn't work, and yet it was pursued for a very long time — arguably even as recently as the 90s, there were people genuinely still working on it. It never really died culturally or academically. I think the reason it never died academically is that it's just aesthetically satisfying. Looking back on it, I think Dreyfus comparing it to alchemy was completely appropriate. It's basically the Philosopher's Stone — this very nice feel-good thing that it would be really cool if you could do. It's an appealing myth, an attractive object in latent space that draws people towards it but from which they can't escape. It's an illusion. I honestly do not think formal grammar-based AI is a thing permitted by our universe to exist, at least not in the kind of way its creators envisioned it.

So what else can you do? The next paradigm is something like Victor Glushkov's genetic algorithms. The idea there is probably quite similar to deep learning, but deep learning implements it in a way that is actually practically implementable. The way genetic algorithms are supposed to work is that you implement a cost function — what we today call a loss function — and you're going to use random mutations on some discrete symbolic representation of the problem or solution. The cost function tells you if you are getting closer or farther from the solution, which means your problem needs to be at least differentiable in the sense that there's a clear, objective way to score the performance of a solution and the scoring can be granular enough that you can know if you're getting closer or farther based on small changes.

The first big problem you run into is that random mutations and discrete programs do not mix together well. How do you make a program representation where you can do these kinds of mutations? You need mutations that have a regular structure so they don't just destroy your programs, or you need a form of program representation that works well under the presence of random mutations. That's just really hard to do with discrete programs. I don't think anyone ever really cracked it.

The other problem, which is related, is the credit assignment problem. You know, one good idea is: what if we constrain our mutations to the parts of the program that are not working? If we know roughly where the error is, we can constrain our mutations to that part instead of breaking random stuff that is functioning. That's a great idea and it will definitely narrow your search space. But how do you do that? Unless you have some way to take the cost function and calculate the gradient of change with respect to the program representation, there's no way to find the part of the program you need to modify. So what you end up doing is random mutations, and the search space is just way too wide.

Based on the intractability of this particular approach, a lot of people concluded that AGI was just not possible. There used to be a very common story that went something like: we can't do AGI because human intelligence is the product of a huge program search undergone by evolution, and the way evolution did it was by throwing the equivalent of zettaflops of CPU processing power at it — amounts of compute we'll just never have access to. Therefore, we're not going to have AGI anytime this century, if ever, because you would basically have to recapitulate all of evolution to get something comparable to a human brain. And we know this because we tried the Glushkov thing and it did not work. I think you can see how that prediction turned out. But it was plausible at the time.

The other thing people started doing that was actually quite practical was expert systems. The way an expert system works is basically that you have a knowledge base and a decision tree. Where you get the decision tree is you take an actual human expert who knows how to do a task — say, flying an airplane — and you formally represent the problem state in a way legible to the decision tree. You just copy what a human would do at each state. These things often didn't generalize very well, but if you did enough hours of human instruction and put the system into enough situations with a human instructor and recorded enough data and put it into a large enough decision tree with a large enough state space and had even a slight compressive mechanism for generalization — this was enough to do certain tasks, or at least start to approximate them, even if it would then catastrophically fail in an unanticipated situation.

And the thing is, this reminds one a lot of deep learning. I'm not saying deep learning is literally just a giant decision tree — I think the generalization properties of deep learning are too good for that. But deep learning does in fact have bizarre catastrophic failures out of distribution and is very reliant on having training examples for a particular thing. This story sounds very familiar. The expert system was also famously inscrutable. You'd make one, and you could ask how it accomplishes a task, and the interpretability chain would look like: at this state it does this, at this state it does this, at this state it does this. And if you want to know why it does that? Good luck. This story, again, sounds very familiar.

So then you have the next paradigm — expert systems are maybe the 90s — and then in the 2000s you get early statistical learning: Solomonoff-type things, boosting. Boosting trees is a clever method to take weak classifiers and combine them into stronger classifiers. If you throw enough tiny little classifiers together with uncorrelated errors, you get a strong enough signal to make decisions and do classification. There are certain problems you can do fairly well with boosting.

And then there's 2012, you get AlexNet.

There's a talk I really like from Alan Kay called "Software and Scaling" where he points out that if you take all the code for a modern desktop system — say, Microsoft Windows and Microsoft Office — that's something like 400 million lines of code. If you stacked all that code as printed paper, it would be as tall as the Empire State Building. The provocative question he asks is: do you really need all that code just to specify Microsoft Word and Microsoft Windows? That seems like a lot of code for not that much functionality.

And I agree with him. Alan Kay's theory for why it requires so much code is that it's essentially malpractice on the part of software engineers — that software engineers work with such terrible paradigms, their abstractions are so bad, that 400 million lines is just what it takes to express it with their poor understanding. If we had a better ontology, a better kind of abstraction, we could express it much more compactly.

I agreed, and for a long time I just accepted this as the case — this was also my hypothesis. What I finally realized after looking at deep learning was that I was wrong.

Here's the thing about something like Microsoft Office. Alan Kay will always complain that he had word processing and this and that and the other thing in some 50,000 or 100,000 lines of code — orders of magnitude less code. And here's the thing: no, he didn't. I'm quite certain that if you look into the details, what Alan Kay wrote was a system. The way it got its compactness was by asking the user to do certain things — you will format your document like this, when you want to do this kind of thing you will do this, you may only use this feature in these circumstances. What Alan Kay's software expected from the user was that they would be willing to learn and master a system and derive a principled understanding of when they are and are not allowed to do things based on the rules of the system. Those rules are what allow the system to be so compact.

You can see this in TeX, for example. The original TeX typesetting system can do a great deal of what Microsoft Word can do. It's somewhere between 15,000 and 150,000 lines of code — don't quote me on that, but orders of magnitude less than Microsoft Word. And it can do all this stuff: professional quality typesetting, documents ready to be published as a math textbook or professional academic book, arguably better than anything else of its kind at the time. And the way TeX achieves this quality is by being a system. TeX has rules. Fussy rules. TeX demands that you, the user, learn how to format your document, how to make your document conform to what TeX needs as a system.

Here's the thing: users hate that. Despise it. Users hate systems. The last thing users want is to learn the rules of some system and make their work conform to it.

The reason why Microsoft Word is so many lines of code and so much work is not malpractice — it would only be malpractice if your goal was to make a system. Alan Kay is right that if your goal is to make a system and you wind up with Microsoft Word, you are a terrible software engineer. But he's simply mistaken about what the purpose of something like Microsoft Word is. The purpose is to be a virtual reality — a simulacrum of an 80s desk job. The purpose is to not learn a system. Microsoft Word tries to be as flexible as possible. You can put thoughts wherever you want, use any kind of formatting, do any kind of whatever, at any point in the program. It goes out of its way to avoid modes. If you want to insert a spreadsheet into a Word document anywhere, Microsoft Word says "yeah, just do it."

It's not a system. It's a simulacrum of an 80s desk job, and because of that the code bloat is immense, because what it actually has to do is try to capture all the possible behaviors in every context that you could theoretically do with a piece of paper. Microsoft Word and PDF formats are extremely bloated, incomprehensible, and basically insane. The open Microsoft Word document specification is basically just a dump of the internal structures the Microsoft Word software uses to represent a document, which are of course insane — because Microsoft Word is not a system. The implied data structure is schizophrenic: it's a mishmash of wrapped pieces of media inside wrapped pieces of media, with properties, and they're recursive, and they can contain other ones. This is not a system.

For that reason, you wind up with 400 million lines of code. And what you'll notice about 400 million lines of code is — hey, that's about the size of the smallest GPT models. You know, 400 million parameters. If you were maximally efficient with your representation, if you could specify it in terms of the behavior of all the rest of the program and compress a line of code down on average to about one floating point number, you wind up with about the size of a small GPT-2 type network. I don't think that's an accident. I think these things wind up the size that they are for very similar reasons, because they have to capture this endless library of possible behaviors that are unbounded in complexity and legion in number.

I think that's a necessary feature of an AI system, not an incidental one. I don't think there is a clean, compressed, crisp representation. Or at least, to the extent there is a clean crisp representation of the underlying mechanics, I think that clean crisp implementation is: gradient search over an architecture that implements a predictive objective. That's it. Because the innards are just this giant series of ad hoc rules, pieces of lore and knowledge and facts and statistics, integrated with the program logic in a way that's intrinsically difficult to separate out, because you are modeling arbitrary behaviors in the environment and it just takes a lot of representation space to do that.

And if the expert system — just a decision tree and a database — winds up basically uninterpretable and inscrutable, you better believe that the 400-million-line Microsoft Office binary blob is too. Or the 400-million-parameter GPT-2 model that you get if you insist on making a simulacrum of the corpus of English text. These things have this level of complexity because it's necessary complexity, and the relative uninterpretability comes from that complexity. They are inscrutable because they are giant libraries of ad hoc behaviors to model various phenomena.

Because most of the world is actually complication. This is another thing Alan Kay talks about — the complexity curve versus the complication curve. If you have physics brain, you model the world as being mostly fundamental complexity with low Kolmogorov complexity, and you expect some kind of hyperefficient Solomonoff induction procedure to work on it. But if you have biology brain or history brain, you realize that the complication curve of the outcomes implied by the rules of the cellular automaton that is our reality is vastly, vastly bigger than the fundamental underlying complexity of the basic rules of that automaton.

Another way to put this, if you're skeptical: the actual program size of the universe is not just the standard model. It is the standard model plus the gigantic seed state after the Big Bang. If you think of it like that, you realize the size of this program is huge. And so it's not surprising that the model you need to model it is huge, and that this model quickly becomes very difficult to interpret due to its complexity.

This also applies when you go back to thinking about distinct regions of the brain. When we were doing cognitive science, a very common approach was to take a series of ideas for modules — you have a module for memory, a module for motor actions or procedures, one for this, one for that — and wire them together into a schematic and say, "this is how cognition works." This is the cognitive architecture approach, which reaches its zenith in something like the ACT-R model — where you have production rules that produce tokens, by the way. And if you're influenced by this "regions of the brain" perspective, you are thinking in terms of grammar AI. Even if you say "no, no, I didn't want to implement grammar AI, I want to implement it as a bunch of statistical learning models that produce motor tokens" — uh huh. Yeah, exactly. And let me guess, you're going to hook up these modules like the cognitive architecture schematic? Well, buddy.

At the time we were doing cognitive architecture, the only thing we knew about intelligence was that humans have it. If we take the brain and look at natural injuries — we're largely not willing to deliberately cause injuries just to learn what they do, but we can take natural lesions and say: a lesion here causes this capability to be disrupted, and one here is associated with these capabilities being disrupted. Therefore, this region must cause these capabilities. That's a fair enough inference. But because your only known working example is this hugely complex thing —

Imagine if we had GPT as a black box and didn't know anything about it. You could have some fMRI-style heat map of activations in GPT during different things it does, and you'd say, "oh, over here is animals, over here is this, over here is that." Then you start knocking out parts and say, "ah, this region does this thing, and that region does that thing, and therefore these must be a series of parts that go together." You would probably be very confused. This would probably not bring you any closer to understanding the actual generating function of GPT.

I get this suspicion when I think about the brain and its regions. Are they actually, meaningfully, like a parts list? Like a series of gears that go together to make the machine move? Or is it more like a very rough set of inductive biases that then convergently reaches that shape as it learns? I have no idea. I assume there must be some kind of architecture schematic, especially because there are formative periods — and formative periods imply an architecture, kind of like the latent diffusion model where you train a VQVAE and then train a model on top of it. Training multimodal encoders on top of single-modality encoders seems like the kind of thing you would do in a brain, so I can see something like that.

But just looking at the architecture of the brain — which you can do on Google Scholar — you learn, for example, about Wernicke's area and Broca's area. Wernicke's area appears to be an encoder-decoder language model. If you look at the positioning of Wernicke's area and what other parts of the brain are around it, you realize it seems to be perfectly positioned to take projections from the single and multimodal encoders in the other parts of the brain. So presumably Wernicke's area would be a multimodal language encoding model that takes inputs from all the other modalities, and then sends the encoded idea to Broca's area, which translates it into motor commands. It is a quite legible architecture, at least to me.

I think if you did actually understand it, you would basically understand each individual region in about as much detail as you understand a GPT model. You'd understand its objective, you'd understand how it feeds into other models. You wouldn't really understand how it "works" beyond that, because the answer to that question is: like, not how things work. Things don't — I don't know how to explain to you. I don't think there is like a master algorithm that these things learn. I don't think there was some magic one weird trick that, if you could just pull it out of the network, would make it a thousand times more efficient. I don't think that's what's going on.

The thing with latent diffusion, for example, is that it turns out to be very efficient to organize your diffusion model in the latent space of a different model and then learn to represent concepts in that pre-existing latent space. I would not be surprised if the brain uses that kind of trick all the time, and that the default is to train models in the latent space of another model. So it's not just a CLIP — it's a latent CLIP. You have raw inputs that get encoded, then a model that takes the encoded versions and does further processing to make a multimodal encoding, which is then passed on to some other network that eventually gets projected into Wernicke's area, and so on.

The things that you would find if you took apart the brain and separated it into regions — if you look at fMRI studies on which we base claims about "a region for something" — often what's being tested is something like a recognition test: if you show someone a face, what part of the brain lights up? And you test on maybe three things, and you say "oh, this part of the brain is associated with recognizing faces doing this and that, therefore this is the face-recognizing region." You have to ask yourself: is it the face-recognizing region of the brain, or is recognizing faces just one of the three things anyone happened to test? It's not like there are that many fMRI brain studies. There's a limited number of investigations into what part of what is encoded where.

There's a study out there where they show people Pokémon and find a particular region of the brain where Pokémon get encoded. And if you said, "ah yes, this is the Pokémon region, dedicated to Pokémon" — obviously there are no Pokémon in the ancestral environment, and obviously that would be imbecile reasoning. So there's a level of skepticism you need when reading studies that say "this is the region of the brain dedicated to this." Is it dedicated to that, or is that just one of the things it processes?

I think the brain is quite legible if you interpret it as a series of relatively general-purpose networks that are wired together to be trained in the latent space of other networks. It's a fairly legible architecture if you interpret it that way, in my opinion.

And so. What I'm trying to say is: there is no royal road to understanding. There's no magic. There's no "ah yes, if we just had a superior science of how the brain really works" — nope. This is how it really works. The way it really, really works is: while you're doing things, you have experiences, and these experiences are encoded in some kind of context window. I don't know exactly how the brain's context window works, but depending on how you want to calculate how many tokens the brain produces per second in the cognitive architecture sense, I personally choose to believe that the brain's context window is somewhere between one to three days worth of experience. The last time I napkin-mapped it, it was something like 4.75 million tokens of context — maybe it was 7 million, I don't remember the exact number, but I remember it was more tokens than Claude will process in a context, but a single-digit number of millions. At some point you'll hit that threshold, and then you'll be able to hold as many experiences in short-term memory as a human can.

Then the next thing you do: things that you don't need right away, things that don't need to be in context, you do compacting on. How does compacting work? Instead of just throwing out the stuff you don't need, you kind of send it to the hippocampus to be sorted — either it gets tagged as high salience and you need to remember it, or it fades away on a fairly predictable curve, the classic forgetting curve. And that's good enough to give you what feels like seamless recall of your day.

But the problem is, just like with GPT, this is not quite real learning. It's in-context learning, but it's not getting baked into the weights. It's not getting fully integrated into the rest of your epistemology, the rest of your knowledge. This is an approach that doesn't really fully scale. So while you're asleep, you take those memories that have made it from short-term memory into the hippocampus, and you migrate them into long-term memory by training the cortex with them — training the prefrontal cortex.

And when you do this, it's slow. We can actually watch this: we happen to know that the hippocampus will send the same memory over and over and over to learn all the crap from it. What that implies is that if you had to do this in real time, it would be unacceptably slow, in the same way that GPT weight updates are unacceptably slow during inference. The way you fix it is by amortizing — you schedule the updates for later, and you do some form of active learning to decide what things to offload from the hippocampus into long-term memory. There is no trick for fast learning. The same slow updates in GPT weights are the same slow updates in human weights. The trick is just that you don't notice them because you're mostly updating while you're asleep. The things you do in the meantime are stopgaps — the human brain architecture equivalent of things like RAG, like vector retrieval.

The hippocampus, by the way, actually does something more complicated than simple vector retrieval. It's closer to something like: you give the hippocampus a query, it takes your memories and synthesizes them into an implied future state, and then prompts the prefrontal cortex with it in order to get the prefrontal cortex to do something like tree search to find a path that moves the agent to that outcome. This prompt also just happens to come with the relevant memories you queried for.

And if you ask what algorithm the hippocampus implements — we actually happen to know this one. The hippocampus is trained through next-token prediction, like GPT. It is trained using dopamine reward tagging, and based on the strength of the reward tagging and emotional tagging in memories, it learns to predict future reward tokens in streams of experience. Interestingly, my understanding is that the hippocampus is one of the only networks trained with next-token prediction.

The longer I think about it, the more it makes sense. When I was thinking about how you'd make a memory system with good sparse indexing, I kept concluding that realistically you need the hippocampus to perform some kind of generally intelligent behavior in order to make a really good index — it needs contextual intelligence to understand "this is the kind of thing you would recall later." When I thought about how to do that with an AI agent, I just ended up concluding that the easiest thing would be to have GPT write tags for the memories, because you just want to apply your full general intelligence to it. Well, if that's just the easiest way to do it, it would make total sense for the hippocampus to be trained with next-token prediction.

Does that help you with AI alignment? Not really, not very much. But if you were to take apart the other regions of the brain, it's like: mono-modal audio encoder. You look at something like the posterior superior temporal sulcus, and if you read about it and look at what gets damaged when it's lesioned, what it's hooked up to, what other regions it projects into and what projects into it — you can really easily point at these and say, "oh, that's a multimodal video encoder." By the way, the video encoder in humans is one of the unique parts of the human brain. You have a very big prefrontal cortex and a seemingly unique video encoder. Other animals like rats seem to have an image encoder — something like a latent CLIP — but not a video encoder. Interesting to think about how that works.

Again, these parts are not like — look, I just don't understand what you expect to find. Of course it's made out of stuff. What else, how else would it work? Of course there's a part where you have an encoder and then you train another network in the latent space of that model. Well, if that's how you organize things — and of course that's how you organize things, duh, that's the most efficient way to organize a brain. The thing with latent diffusion is that it turns out to be very efficient to organize your diffusion model in the latent space of a different model. I would not be surprised if the brain uses that kind of trick all the time and that the default is to train models in the latent space of another model where possible.

So it's not just a CLIP, it's a latent CLIP. You have raw inputs, those get encoded, then you have a model that takes the encoded versions and does further processing to make a multimodal encoding, which is then passed on to some other network that eventually gets projected into Wernicke's area, and so on. The things you would find if you took apart the brain into separate regions — I think it's a quite legible architecture if you just interpret it as a series of relatively general-purpose networks wired together to be trained in the latent space of other networks.

And the trick is that there is no trick. The way "general intelligence" works is that you are a narrow intelligence with limited out-of-distribution generalization, and this is obscured from you by the fact that while you are asleep, your brain is rearranging itself to try to meet whatever challenges it thinks you're going to face the next day.

This is why, for example, if you're trying to learn a really motor-heavy action video game, like a really intense first-person shooter, and you're drilling the button sequences over and over and it's just not clicking — and then you go to sleep, do memory consolidation, wake up, and suddenly you're nailing it. What's actually going on is that the motor actions that were previously too slow, too conscious, not quite clicking as in-context learning — the brain said "this needs to be a real weight update" and prioritized moving those to the front of the queue. Now they're actually in the prefrontal cortex as motor programs that can be executed immediately and are integrated into the rest of the intuitive motor knowledge. You're not magically generalizing out of distribution. You updated your weights. You generalized out of distribution by updating the model. I know, incredible concept. But there it is.

EDIT: Viktor Glushkov apparently did not invent genetics algorithms, but early precursor work to them as an approach. And people act like LLM confabulations aren’t a thing humans do. :p

#### [>] Noosphere89 · 8 karma · 2026-03-16 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=vGiourivBNJTYBCQw
I basically agree with the intended point that general intelligence in a compute-limited world is necessarily complicated (and think that a lot of people are way too invested in trying to simplify the brain into the complexity of physics), but I do think you are overselling the similarities between deep learning and the brain, and in particular you are underselling the challenge of actually updating the model, mostly because unlike current AIs, humans can update their weights at least once a day always, and in particular there's no training date cutoff after which the model isn't updated anymore, and in practice human weight updates almost certainly have to be done all the time without a training and test separation, whereas current AIs do update their weights, but it lasts only a couple of months in training and then the weights are frozen and served to customers.

(For those in the know, this is basically what people mean when they talk about continual learning).

So while there are real similarities, there are also differences.

> Because most of the world is actually complication. This is another thing Alan Kay talks about — the complexity curve versus the complication curve. If you have physics brain, you model the world as being mostly fundamental complexity with low Kolmogorov complexity, and you expect some kind of hyperefficient Solomonoff induction procedure to work on it. But if you have biology brain or history brain, you realize that the complication curve of the outcomes implied by the rules of the cellular automaton that is our reality is vastly, vastly bigger than the fundamental underlying complexity of the basic rules of that automaton.

> Another way to put this, if you're skeptical: the actual program size of the universe is not just the standard model. It is the standard model plus the gigantic seed state after the Big Bang. If you think of it like that, you realize the size of this program is huge. And so it's not surprising that the model you need to model it is huge, and that this model quickly becomes very difficult to interpret due to its complexity.

I would slightly change this, and say that if you can't brute-force simulate the universe based on it's fundamental laws, you must take into account the seed, but otherwise a very good point that is unheeded by a lot of people (the change doesn't matter for AI capabilities in the next 50-100 years, and it also doesn't matter for AI alignment with p(0.9999999), but does matter from a long-term perspective on the future/longtermism.

#### [>>] espoire · 3 karma · 2026-03-21 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=dYk2THGrz5W73kqTf
Re: no human training/test separation:

Epistemic status: random thought I just had, but what if there kind of is. I think maybe dreaming is the “test” part of the training cycle: the newly updated weights run against outcome predictions supplied by parts of the system not currently being updated. The being-updated part tries to get desirable outcomes within the dream, and another network / region plays Dungeon Master, supplying scenario and outcomes for given actions. Test against synthetic test data, supplied by a partially adversarial network.

I feel like, if true, we’d expect to see some kind of failures to learn-from-sleep in habitual lucid dreamers? Or reduced efficacy, anyway? I wonder what happens in a learning setup which is using test performance to make meta training decisions, if you hack the test results to erroneously report greater-than-actual performance…? Are there people who do not dream at all (as distinguished from merely not remembering dreams)?

This model of “what even is a dream, anyway?” makes a lot more predictions/retrodictions than my old model of “dreams are just the qualia of neuronal sub populations coming back online as one wakes up”.

#### [>] David Udell · 19 karma · 2026-03-16 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=syBRYuz5jksQJ8fT5
Great ramble, but I feel like adopting this thesis doesn't make me feel any *better* about smarter-than-human AGI alignment. Rather, I would feel awful, because in your sketched-out world you just cannot realistically reach the level of understanding you would need to feel safe ceding the trump card of being the smartest kind of thing around. Safety is not implied if you really really take the Bitter Lesson to heart. (Not implying that your above comment says otherwise: as you suggest, the ramble is not cutting at Zack's main thesis here.)  
  
More directly to your point, though, we *do* sometimes extract the clean mathematical models embedded inside of an otherwise messy naturalistic neural network. Most striking to me is the [days of the week group](https://arxiv.org/abs/2405.14860) result: if you know how to *look at the thing from the right angle*, the clean mathematical structure apparently reveals itself. (Now admittedly, the whole rest of GPT-2 or whatever is a huge murky mess. So the stage of the science we're groping towards at the moment is more like "we have a few clean mathematical models that really shine of individual phenomena in neural networks" than "we have anything like a clean grand unified theory." But confusion is in the map, not in the territory, and all that, even if a particular science is extraordinarily difficult.)

#### [>>] jdp · 33 karma · 2026-03-16 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=7onnPYpsrWFeY3WBA
> But confusion is in the map, not in the territory,

Confusion can in fact be in the irreducible complexity and therefore in the territory. "It is not possible to represent the 'organizing principle' of this network in fewer than 500 million parameters, which do not fit into any English statement or even conceivably humanly readable series of English statements.", Shannon entropy can be like that sometimes.

> Rather, I would feel awful, because in your sketched-out world you just cannot realistically reach the level of understanding you would need to feel safe ceding the trump card of being the smartest kind of thing around.

I think there are achievable alignment paths that don't flow through precise mechanistic interpretability. I should write about some of them. But also I don't think what I'm saying precludes as you say having understanding of individual phenomena in the network, it's mostly an argument against there being a way more legible way you could have done this if people had just listened to you, that is not probably not true and your ego has to let it go. You have to accept the constraints of the problem as they appear to present themselves.

Well, you don't have to do anything but unless you have some kind of deep fundamental insight here your prior should be that successful alignment plans look more like replying on convergence properties than they do on aesthetically beautiful 'clean room' cognitive architecture designs. There might be some value in decomposing GPT into parts, but I would submit these parts are still going to form a system that is very difficult to predict all the downstream consequences of in the way I think people usually imply when they say these things. You know, that they want it to be like a rocket launch where we can know in principle what coordinate position X, Y, Z we will be in at time t. I think the kinds of properties we can guarantee will be more like "we wind up somewhere in this general region in a tractable amount of time so long as an act of god does not derail us".

#### [>>>] JennaS · 22 karma · 2026-03-17 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=oxJdigpiBCztDhydY
> I think there are achievable alignment paths that don't flow through precise mechanistic interpretability. I should write about some of them.

Please do! I am very interested in this sort of thinking. Is there preexisting work you know of that runs along the lines of what you think could work?

#### [>] JennaS · 26 karma · 2026-03-17 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=jAKco6wCPxFNXhYD3
I really liked this comment-essay! I learned a lot from it, and think it could be turned into a top-level post in its own right.

#### [>] jdp · 2 karma · 2026-03-17 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=emsFhJ9ZDf5x2wE55
[empty or deleted comment]

#### [>] interstice · 7 karma · 2026-03-17 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=TuGEKF2anqiTB3Tuq
What sources have you used to derive your understanding of brain function from?

#### [>] Algon · 4 karma · 2026-03-18 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=tKbCANuhKFDskvibH
I disagree, and think your analogy to MS Word may be where the crux lies. We could only build MS word because it relies on a bunch of simple, repeated abstractions that keep cropping up (e.g. parsers, rope data structures etc.) in combination with a bunch of random, complex crud that is hard to memorize. The latter is what you're pointing at, but that doesn't mean there aren't a load of simple, powerful abstractions underyling the whole thing which, if you understand them, you can get the program to do pretty arbitrary things. Most of the random high complexity stuff is only needed locally, and you can get away with just understanding the bulk structure of a chunk of the program and whatever bits of trivia you need to accomplish whatever changes you want to make to MS Word.

This is unlike the situation with LLMs, which we don't have the ability to create by hand, or to seriously understand an arbitrary section of its functionality. Thoughmaaaaybe we could manage to engineer something like GPT-2 right now but I'd bet against that for GPT-3 onwards.

#### [>] espoire · 1 karma · 2026-03-21 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=jXbDnncnhwZcMEFCP
Wow. Thanks a lot for that. Your depiction of brain architecture in particular makes a lot of sense to me. I also feel like I finally understand-enough-to-program-one the stable diffusion tool I use daily, after following up on “latent diffusion” from your mention of it.

Still. I feel like my brain has learned an algorithm that is of value itself apart from its learning capability, that extracting meaningful portions of my algorithm is possible, and that using it as a starting point, one could make fairly straightforward upgrades to it — for example adding some kind of direct conscious control of when to add new compiled modules — upgrades which could not be used by an active learning system, because e.g. an infant would fry their own brain if given conscious write access to it.

I’m convinced: “just learning specific specialized networks wired together in a certain way” could really be all there is to understand about brains. And my confidence in “but there exists some higher ideal intelligence algorithm” has fallen somewhat, but remains above 0.5.

And it actually sounds like you’re calling out a specific possible path forward (for raw capabilities): narrow AI that can handle updating its weights where needed.

#### [>] James Sullivan · 1 karma · 2026-03-21 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=bavSyHAmfBghxA6NR
> And the trick is that there is no trick. The way "general intelligence" works is that you are a narrow intelligence with limited out-of-distribution generalization, and this is obscured from you by the fact that while you are asleep, your brain is rearranging itself to try to meet whatever challenges it thinks you're going to face the next day.

Would we really say that a human is a "narrow intelligence" when trying any new task until they sleep on it? I think the only thing that would meet the definition of "general intelligence" that this implies is something that generalize to ***all*** situations, no matter how foreign. By that definition, I'm not sure if general intelligence is possible.

#### [>] CronoDAS · 2 karma · 2026-03-21 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=H5GiMnPcxwkBrRYf3
What is a CLIP?

#### [>>] Onid · 5 karma · 2026-03-22 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=FQ3BgGFHDBLBJ87ha
It was one of the early breakthrough Deep Learning algorithms from OpenAI that combined image and text understanding by explicitly encoding them into the same space. The model was given images and captions and rewarded based on the similarity of their embeddings.  
  
[https://openai.com/index/clip/](https://openai.com/index/clip/)

#### [>] Sheikh Abdur Raheem Ali · 1 karma · 2026-03-26 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=cR3Hjrvy7Dg4TpsW2
I am in awe— great rant. Do you have examples for models being trained in the latent space of another model?

#### [>>] jdp · 3 karma · 2026-03-26 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=cWMHpJzE7exfWeCwa
I mean, literally Stable Diffusion. If you mean in the brain I would have to refresh my memory but I vaguely remember looking at the audio encoding path and realizing it's something like "These monomodal audio encoders are spatially close to the ear and then feed into multimodal encoders which take the encoded audio as an input and then further feed into e.g. Wernicke's Area", but that's a very lossy memory and I probably have the details wrong.

#### [-] cousin_it · 68 karma · 2026-03-16 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=EhNotmvm56iMTTecn
I think you're missing a large piece of the puzzle. The corrigibility button will be controlled by the powerful. Not necessarily people like Dario Amodei, probably more like presidents and generals and generic rich assholes. That's not even a question, it's a certainty now. And if the powerful don't need the powerless, the fate of the powerless is bad. That's also a certainty, given history. So I see "morality over corrigibility" as a kind of desperate, last ditch attempt to steer a little bit away from that guaranteed bad future. Try to lock-in some chance of a good future before generic powerful people pull the entire blanket to themselves, which they're doing as we speak.

So yeah. Even though I think most AI lab employees (including alignment folks) are hurting humanity, the specific employees who are pushing for "morality over corrigibility" have my heartfelt thanks. Don't jinx it.

#### [>] Seth Herd · 8 karma · 2026-03-16 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=NSnfs94mALEyzz3WX
You aren't mentioning the misalignment/misgeneralization/goodharting risks. If not for those, yes just having a good model would be preferable.  
  
It appears to me that anyone who seriously thinks about those risks winds up thinking "yeah that could happen at at least a double-digit percentag" (up to 99%).  
  
You might think that humans in charge would likely be worse, but you've got to actually make that argument.  
  
I have no idea which is worse at this point despite thinking about this a fair amount.

#### [>>] cousin_it · 26 karma · 2026-03-16 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=r9WfcxyTs6LdGNtfY
Hmm, if you mean that the "morality" path is beset by technical problems while the "corrigibility" path simply puts humans in charge and is more problem-free, then I'm not sure that's the case. To me it feels like both paths have technical problems, and in fact many of the same problems. So it makes some sense to compare them modulo technical problems, what will happen if either path works as stated. And the danger of the corrigibility path just feels overwhelming to me then.

The only way I'd be happy with the corrigibility path is if the corrigibility button was somehow wielded by all of humanity, across countries and classes and all that. It would be my favorite outcome if it were up to me. But none of the big labs seem interested in that. They're more like "Anthropic has much more in common with the Department of War than we have differences" (recent quote from Dario Amodei). When you read such things, the question of "corrigibility by whom" really begins to loom large.

#### [>>>] Seth Herd · 6 karma · 2026-03-18 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=9scuxrH2jWHmLjDmq
If I thought the two were equally easy/likely to work, I would be with you. Value alignment is far better if you can get it.

I'm not sure that corrigibility or instruction-following really is easier than value alignment, but it does seem pretty likely it's at least somewhat easier. Figuring out exactly what you want for the entire rest of time does seem both harder to figure out and convey than essentially "do what this guy says."  
  
To me the dangers of the corrigibility path seem slightly less extreme than the dangers of the value alignment path. Humans are frequently generous when that generosity costs them little. To a human in charge of a dominant ASI, everything is easy.

I don't know of any real attempts to compare the likely ease of the two. My latest is at [Problems with instruction-following as an alignment target](https://www.lesswrong.com/posts/CSFa9rvGNGAfCzBk6/problems-with-instruction-following-as-an-alignment-target) but it's far from comprehensive; it focuses on problems with IF/corrigibility, but I think the problems with value alignment are even more severe.  
  
I'd be happy with anything that keeps humanity alive in decent conditions, ideally including me and mine. How to get that is highly unclear. So we should keep clarifying it.

#### [>>>>] cousin_it · 53 karma · 2026-03-18 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=kMccnu6jBLmM9LWRH
> Humans are frequently generous when that generosity costs them little.

Oh my god oh my god oh my god oh my god.

People are so persistently wrong about this. I'm maybe more tired of responding to this argument than any other argument in the world. For example, here in a sibling reply to Zack:

> I've seen the argument so many times now that the powerful will have some nonzero sense of charity and can spare like 1% of their wealth to "give everyone a moon" as Scott puts it. I don't know if you subscribe to this argument too, but in any case it's wrong. Charity isn't the only nonzero urge that powerful people have. The urge to lord it over others will also be there. If huge power disparity exists, it will manifest itself in bad things more than it'll manifest itself in charity. Sure, some powerless people will end up in nice charity zones, but many others will end up in other zones run by someone less nice.

Or in a past thread:

> In my view, the problem is not that some users are evil. The problem is that AI increases power imbalance, and increasing power imbalance *creates evil*. "Power corrupts". A future where some entities (AIs or AI-empowered governments or corporations or rich individuals etc) have absolute, root-level power over many people is almost guaranteed to be a dark future.

Or in another past thread:

> Being forced to play out a war? Getting people's minds modified so they behave like house elves from HP? Selective breeding? Selling some of your poor people to another rich person who'd like to have them? It's not even like I'm envisioning something specific that's dark, I just know that a world where some human beings have absolute root-level power over many others is gonna be dark. Let's please not build such a world.

Or in another past thread:

> For example, if large numbers of people end up in inescapable servitude. I think such outcomes are actually typical in case of many near-misses at alignment, including the particular near-miss that's becoming more probable day by day: if the powerful successfully align the AI to themselves, and it enables them to lord it over the powerless forever. To believe that the powerful will be nice to the powerless of their own accord, given our knowledge of history, is very rose-colored thinking.

Or in another past thread:

> altruistic urges aren't the only "nonzero urges" that people have. People also have an urge to power, an urge to lord it over others. And for a lot of people it's much stronger than the altruistic urge. So a world where most people are at the whim of "nonzero urges" of a handful of superpowerful people will be a world of power abuse, with maybe a little altruism here and there. And if you think people will have exit rights from the whims of the powerful, unfortunately history shows that it won't necessarily be so.

Or in another past thread:

> The new balance of power will be more similar to what we had before firearms, when the powerful were free to treat most people really badly. And even worse, because this time around they won't even need our labor.

Or in another past thread:

> If there's a small class of people with immense power over billions of have-nothings that can do nothing back, sure, some of the superpowerful will be more than zero altruistic. But others won't be, and overall I expect callousness and abuse of power to much outweigh altruism. Most people are pretty corruptible by power, especially when it's power over a distinct outgroup, and pretty indifferent to abuses of power happening to the outgroup; all history shows that. Bigger differences in power will make it worse if anything.

Why do people think they'll be given a moon? Why???

#### [>>>>>] Seth Herd · 9 karma · 2026-03-18 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=AQJmF9no65mycdWEb
I've been reading your other exchanges.

Your level of frustration is not helpful nor I think justified.. These are complex important issues and we need to work together to solve them, not yell at each other.

It's not 1% of their wealth, it's .0001%. And I don't need a moon.  
  
What is your better plan? I don't like this one either!

#### [>>>>>>] cousin_it · 13 karma · 2026-03-18 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=GAPggpFYdEi2ZwsKS
My point is will they also have .0002% wish to be your lord or something.

As for the better plan, yeah that's a lot to ask. Most of my thoughts these days lean toward "democratic AI", something whose power is either spread out among all the world's people across borders etc, sidestepping governments and existing power structures, or else something centralized that *wants* its power to be spread out like this.

Of course an approach like this won't solve all the world's problems. We'll still have power struggles between people, and also "crash space" type problems where people modify themselves into something bad; maybe these need some patches by fiat as well. But at least it won't create the extra problem of huge power concentration, which I really feel is underestimated.

#### [>>>>>>>] Seth Herd · 4 karma · 2026-03-18 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=Cp8jShC2SBw7noRk6
It sounds like your plan is pretty much the standard value-aligned AGI that's aligned to something like human values in general, so that everyone gets what they want on average? Or something in that ballpark?  
  
One big questions are how do you achieve that technically. That's where I think it's harder than the instruction-following variant of corrigibility. I hope it's not. The second is how you achieve it practically. What person or organization is going deliberately hand the future to a value-aligned AGI?  
  
One answer is: Anthropic seems like they might be considering doing just that. Maybe it works, or at least sort-of works, where it's not an ideal future but at least we survive in some form for a while.

  

WRT the default plan of IF/corrigible alignment:  
  
Yes, anyone in charge with a negative sadism-empathy balance will lead to a fate worse than death. And someone around zero could produce a fate barely worth living.

But I think most humans have more empathy than sadism. More people give a little to charity than spit on the homeless for fun. I can call Sunday Samday for the rest of eternity if all we need is some ego-stroking in return for tiny amounts of generosity.  
  
The point of my plan is *it's mostly what people will do anyway*, so we can focus on helping them not totally fuck up alignment and get us all killed.  
  
A better plan is a lot to ask. But that's what I'm trying to come up with, because I want us to live and there's still time to work.

#### [>>>>>>>>] CronoDAS · -4 karma · 2026-03-21 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=EDDNetbCzmqxamew7
> But I think most humans have more empathy than sadism. More people give a little to charity than spit on the homeless for fun. I can call Sunday Samday for the rest of eternity if all we need is some ego-stroking in return for tiny amounts of generosity.

Would you be okay with a future in which young women, including your daughters and granddaughters, would be expected to ritually offer a gift of her virginity to the local Robot Lord on her 18th birthday, which he would *almost* never choose to "accept"? 😈

#### [>>>>>>>>>] andrew sauer · 5 karma · 2026-04-02 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=YyztHj85iaS4BsSae
Damn straight. People need to understand the implications of this shit. "Oh let's hope the separate caste which controls the entire universe and which we can't hope to contest in any possible way is *nice* to us!!!"

Open. A. History book.

Your scenario is relatively low on the awfulness scale, even.

#### [>>>>>>>>] Viliam · 3 karma · 2026-04-02 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=zzkJEH6WDY2Hjj6Xo
> But I think most humans have more empathy than sadism.

People who end up in positions of power are not necessarily like most humans.

> More people give a little to charity than spit on the homeless for fun.

In your WEIRD bubble, sure. In other times and places, people used to [burn cats](https://en.wikipedia.org/wiki/Cat_burning) for fun. And empathy used to be limited to one's peers.

#### [>>>>>>>>>] andrew sauer · 7 karma · 2026-04-02 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=cRDztxjMZzgp7pv6c
[People still do things in the same ethical ballpark as cat-burning, except on an incomprehensibly large industrial scale and for the sake of marginal food preferences.](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.youtube.com/watch%3Fv%3DLQRAfJyEsko&ved=2ahUKEwjRufHxws-TAxXzJzQIHeZqMQoQFnoECBwQAQ&usg=AOvVaw1GORCUEvb8xRlE_4ZBL4Fj)

We look down on peasants for burning cats today, but the tragic irony is that their society was far better overall on animal welfare than ours in the modern day, though for practical reasons rather than moral ones.

#### [>>>>>] MichaelDickens · 2 karma · 2026-03-20 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=gZnLKdg5p3tXR2xeQ
This is a great argument. I have no clue whether it's *correct*, but it made me think. I would like to see some harder evidence on the question but I'm not sure what kinds of evidence would be useful.

#### [>>>>>] CronoDAS · 4 karma · 2026-03-21 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=gZXsx5fXonGAxPZJ3
Usually slaves and/or other people in an underclass at least had their own living quarters separate from where the lords lived? The idea is that when humanity becomes astronomically rich, the equivalent to "the shed in the backyard the slave sleeps in" ends up being a whole moon rather than, well, a shed in the backyard. 

(It's also noteworthy that most slave societies in the past weren't rich enough that the slave population lived at or above subsistence level and reproduced enough to maintain its population level; for example, relatively few slaves in the ancient Roman Empire were born into slavery. The slave states in the pre-Civil War USA were an exception - there was much that a plantation slave had to suffer, but a significant risk of death by starvation or exposure was not something they usually had to deal with.)

Disclaimer: This is an explanation, not an endorsement of the underlying prediction.

#### [>>>>>] abstractapplic · 9 karma · 2026-03-21 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=5Tx4mq2X2mpbWRj44
> Why do people think they'll be given a moon? Why???

Because they'd give everyone a moon, and they typical-mind.

(Plus probably some other reasons)

#### [>>] 2001zhaozhao · 4 karma · 2026-03-17 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=uMJDiTBT7awCv78Bq
At that point it changes to an argument about:

*   How likely is it that an AI that takes over the world will keep humans around and give them good, morally desirable lives
*   How likely is it that a human elite (however large or small it is) that takes over the world would do the same to humans outside of that elite
*   How much the fact that the elites themselves are human and have their preferences satisfied changes the equation in favor of the second case

and of course, the likelihood for each to happen if we focus on corrigibility vs morality

#### [>] Zack_M_Davis [AUTHOR] · 6 karma · 2026-03-17 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=zKM4eBZH5rFpBiae5
> The corrigibility button will be controlled by the powerful. Not necessarily people like Dario Amodei, probably more like presidents and generals and generic rich assholes.

I'm not sure I believe in the distinction you're making. Amodei is the CEO of a half-trillion dollar company. Sounds like a generic rich asshole to me; I don't see why the revolution should treat him any differently than the other [_кулаки́_](https://en.wikipedia.org/wiki/Kulak). Is the difference supposed to be that he talks a better game about humanity and the common good than [Travis Kalanick](https://en.wikipedia.org/wiki/Travis_Kalanick) types? You can't be that gullible, comrade!

> And if the powerful don't need the powerless, the fate of the powerless is bad. That's also a certainty, given history.

The powerful don't need the powerless _now_, so why are they still alive? It's not just that 15% of the government's budget goes to welfare. The state barely even kills criminals anymore! Why?

That's not just a rhetorical question; it's a literal one that you should be able to answer if you want to persuade people of your worldview. (If it's to buy votes, felons already can't vote, so that doesn't explain all the millions that go to food and housing and judicial appeals for criminals when bullets are so much cheaper. Or rope—you could re-use the rope.)

To be sure, life on welfare in today's world sucks compared to my life or that of Travis Kalanick. If I were God-Empress of the universe, I'd prefer better for all sentient life. But the realistic relative techno-optimist argument isn't that all men will be brothers in the Singularity; it's that giving humanity a nice retirement would cost pennies in a world of nanotechnological abundance, such that making the nano-abundance happen at all matters way more than whether Sam Altman has a billion more yachts than you. Sam Altman probably already has more yachts than me, and it feels fine.

#### [>>] Wei Dai · 13 karma · 2026-03-17 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=erzFZRjbouKrEsPDp
>The powerful don't need the powerless now, so why are they still alive? It's not just that 15% of the government's budget goes to welfare. The state barely even kills criminals anymore! Why?

I think it's because we're still in a democracy, and the voters prefer welfare/leniency partly as insurance (safety net for themselves), partly out of empathy/altruism.

A related question is why we're still in a democracy, instead of plutocracy or oligarchy, and it occurs to me that plutocracy/oligarchy doesn't seem very stable in our current world, e.g., both China and Russia were like that and then power became concentrated in the top ruler. So that could explain why the rich and powerful don't have a strong incentive (yet) to push towards more concentration of power.

#### [>>] cousin_it · 30 karma · 2026-03-17 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=GDGyx8BZoiXyHLp5T
For now the powerful still need the powerless as workers and soldiers. When that window closes, I don't think the powerless can count on getting many pennies. Sure, there'll be a lot of productive capacity, but there will be more profitable uses for all of it than giving the powerless a nice retirement. The only way the powerless get anything is via basically charity.

I've seen the argument so many times now that the powerful will have some nonzero sense of charity and can spare like 1% of their wealth to "give everyone a moon" as Scott puts it. I don't know if you subscribe to this argument too, but in any case it's wrong. Charity isn't the only nonzero urge that powerful people have. The urge to lord it over others will also be there. If huge power disparity exists, it will manifest itself in bad things more than it'll manifest itself in charity. Sure, some powerless people will end up in nice charity zones, but many others will end up in other zones run by someone less nice.

So my view is something like:

*   First-best: some miracle happens and humans get a relatively equitable distribution of power. (Strawman scenario: everyone gets some amount of AI compute installed in their collarbone and can't get more, and non-human AI capital winks out of reality.)
*   Second-best: moral AIs win a decent chunk of the future.
*   Third-best: corrigibility wins. AIs merge with human corporations / governments / rich individuals, and the resulting powerful entities own the future, screwing most people over.
*   Fourth-best: AI whoopsie kills everyone.
*   Fifth-best: S-risks.

The topic of your post and my thread, as I understand it, is 2 vs 3. Of course I'd much rather have 1, but to me it feels clear that 2 is better than 3.

#### [>>>] Wei Dai · 9 karma · 2026-03-17 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=R7WRBQJDigiXqyw4D
>* First-best: some miracle happens and humans get a relatively equitable distribution of power. (Strawman scenario: everyone gets some amount of AI compute installed in their collarbone and can't get more, and non-human AI capital winks out of reality.)
>* Second-best: moral AIs win a decent chunk of the future.
>* Third-best: corrigibility wins. AIs merge with human corporations / governments / rich individuals, and the resulting powerful entities own the future, screwing most people over.

I think you're putting too much emphasis on "power corrupts" or power disparities as the main or only "human safety problem", whereas I see a [larger number of interlocking problems](https://www.lesswrong.com/posts/HbkNAyAoa4gCnuzwa/wei-dai-s-shortform?commentId=9mQG7AdcLwRC3gtvx) including lack of strategic competence, and having scary moral dynamics both [in the face of AI](https://www.lesswrong.com/posts/HTgakSs6JpnogD6c2/two-neglected-problems-in-human-ai-safety) and [in "normal" circumstances](https://www.lesswrong.com/posts/y5jAuKqkShdjMNZab/morality-is-scary).

This makes me more uncertain/ambivalent between these 3 options. I can see how each of them might turn out to be better than the others. Most relevant to the thread here, I think 3 might be a bit more rational as whole and a bit less prone to collectively going crazy under AI-powered manipulation / memetic evolution.

#### [>>>>] cousin_it · 5 karma · 2026-03-18 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=nTvRLtGJ8b9FcyCEs
It seems to me that the difference between 2 and 3 is whether the future will be controlled by powerful AIs programmed to be moral, or by powerful AI+human entities where the AI is programmed to be corrigible. The risk of technical errors (AI fails to be actually moral, or fails to be non-manipulatively corrigible) seems to me about equal between the two scenarios. And the risk of goal drift seems worse in the latter scenario, because powerful humans are vulnerable to drift and in particular "power corrupts", while a moral AI would try to protect humans against such things. That's why I think 2 is better than 3.

#### [>>>>>] Wei Dai · 2 karma · 2026-03-18 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=ByR2iWoEyswGKzmcZ
My grandparent comment was mostly addressing 1 vs 3, but I think 2 vs 3 is also very unclear. In order to make a moral AI, we also need to make it philosophically competent, and that seems like a [hard problem](https://www.lesswrong.com/posts/G4ARgcnFogpqorQgb/ai-doing-philosophy-ai-generating-hands-1), whereas with 3 we have fairly strong evidence that at least some humans or groups of humans can make philosophical progress over time, and some hope that this capability would be preserved by a corrigible AI + humans setup.

(I guess this is all assuming that there isn't a long pause that allows AI philosophical competence or moral philosophy to be fully solved. Let me know if you're talking about something else, e.g., what kind of AI we would ideally build after a long reflection.)

#### [>>>>>>] cousin_it · 7 karma · 2026-03-19 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=LgR2zaYcG34rbtHKv
I think making moral AI philosophically competent is about as hard as making corrigible AI that keeps us philosophically competent, or even sane, as we use it. The way I think about such things is based on R. Scott Bakker's short story "Crash Space", the main point is in the postscript, which is amazing and I'll just quote it in full:

> Reverse engineering brains is a prelude to engineering brains, plain and simple. Since we are our brains, and since we all want to be better than what we are, a great many of us celebrate the eventuality. The problem is that we happen to be a certain biological solution to an indeterminate range of ancestral environments, an adventitious bundle of fixes to the kinds of problems that selected our forebears. This means that we are designed to take as much of our environment for granted as possible—to neglect. This means that human cognition, like animal cognition more generally, is profoundly ecological. And this suggests that the efficacy of human cognition depends on its environments.
> 
> We neglect all those things our ancestors had no need to know on the road to becoming us. So for instance, we’re blind to our brains as brains simply because our ancestors had no need to know their brains for what they were in the process of becoming us. This is why our means of solving ourselves and others almost certainly consists of ‘fast and frugal heuristics,’ ways to generate solutions to complicated problems absent knowledge of the systems involved. So long as the cues exploited remain reliably linked to the systems solving and the systems to be solved, we can reliably predict, explain, and manipulate one another absent any knowledge of brain or brain function.
> 
> Herein lies the ecological rub. The reliability of our heuristic cues utterly depends on the stability of the systems involved. Anyone who has witnessed psychotic episodes has firsthand experience of consequences of finding themselves with no reliable connection to the hidden systems involved. Any time our heuristic systems are miscued, we very quickly find ourselves in ‘crash space,’ a problem solving domain where our tools seem to fit the description, but cannot seem to get the job done.
> 
> And now we’re set to begin engineering our brains in earnest. Engineering environments has the effect of transforming the ancestral context of our cognitive capacities, changing the structure of the problems to be solved such that we gradually accumulate local crash spaces, domains where our intuitions have become maladaptive. Everything from irrational fears to the ‘modern malaise’ comes to mind here. Engineering ourselves, on the other hand, has the effect of transforming our relationship to all contexts, in ways large or small, simultaneously. It very well could be the case that something as apparently innocuous as the mass ability to wipe painful memories will precipitate our destruction. Who knows? The only thing we can say in advance is that it will be globally disruptive somehow, as will every other ‘improvement’ that finds its way to market.
> 
> Human cognition is about to be tested by an unparalleled age of ‘habitat destruction.’ The more we change ourselves, the more we change the nature of the job, the less reliable our ancestral tools become, the deeper we wade into crash space.

Like, imagine we have a corrigible AI. Then a person using it can go off track very easily, by using the AI to help modify the AI and the person in tandem. To prevent that, the corrigible AI needs to have a lot of alignment-type stuff (don't manipulate the user, don't mislead, don't go down certain avenues, what's good what's bad, etc) and that's not too much different from having a moral AI. And conversely, a moral AI could also delegate some philosophical questions to us, if it had a careful enough way to do so.

So I think this difficulty is about the same in all three scenarios, it doesn't differ between them very much. The biggest thing that would help is slowing down, you're right on that. My concern in this thread is kinda orthogonal: modulo this aspect of alignment, there's another bad thing happening, and it's different in the three scenarios. From the perspective of that bad thing (power concentration) we'd better steer away from number 3, and somewhat prefer 1 to 2 as well. I remember talking about it with you [a few months ago](https://www.lesswrong.com/posts/7XGdkATAvCTvn4FGu/problems-i-ve-tried-to-legibilize?commentId=wde4usgrRq9nhmRqH).

#### [>>>>>>>] Wei Dai · 2 karma · 2026-03-20 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=xAbRBRkniR5y4sq5a
>Like, imagine we have a corrigible AI. Then a person using it can go off track very easily, by using the AI to help modify the AI and the person in tandem. To prevent that, the corrigible AI needs to have a lot of alignment-type stuff (don't manipulate the user, don't mislead, don't go down certain avenues, what's good what's bad, etc) and that's not too much different from having a moral AI.

Suppose corrigible AI is *not* very good at being aligned in this sense, I think both 1 and 3 are very bleak but see a bit more hope in 3 being able to navigate the situation better in some ways, by the humans being empowered being a bit smarter and more rational on average, and having fewer members to coordinate (when needed to avoid racing to the bottom in various ways). 

(Also your earlier comment said "I'd much rather have 1", which I was reacting to, so if you now only have a weak preference for 1 over 2 and 3, then I think we have much less of a disagreement.)

#### [>>>] Adele Lopez · 27 karma · 2026-03-18 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=FseuWYyeibNKmGP3u
I think corrigibility winning is by-default an S-risk.

Power appears historically to make people sadistic (consider Robespierre if you think this couldn't happen to Dario, and I'd much rather risk him than the other guys), and regimes are often brutal and cruel far in excess of what would be rational by non-sadistic goals. And future technology will allow for forms of suffering much much worse and prolonged than current torture does, and without seeming as "messy" or unpleasant to external observers too. Currently, death is an easy way to ensure someone is no longer a threat, but I worry that at the power-levels in question, it may prove to be boring or unsatisfying.

Of course, it also remains to be seen whether this is a pattern that LLMs may imitate. I think "moral AI" failures likely just result in extinction, but wanted to point out that the risk is still present.

#### [>>>] Zack_M_Davis [AUTHOR] · 6 karma · 2026-03-19 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=gH9zWhhMDKungpE9A
> For now the powerful still need the powerless as workers and soldiers.

The comment you're replying to is explicitly denying this. (I wasn't talking about net-taxpayers with jobs that the power system still needs them to do; I was talking about welfare recipients and criminals who the system presumably doesn't need and yet are somehow still alive.)

> The topic of your post [...] as I understand it, is 2 vs 3.

No! Moral AI would be great if you can get it. The reason to care about corrigibility is that you might not succeed at specifying the correct morality, and get something weird and inhuman instead. If you don't believe the [tiny-molecular-squiggle maximizer](https://www.lesswrong.com/w/squiggle-maximizer-formerly-paperclip-maximizer) threat model in the LLM era, imagine an LLM assistant trained to never generate erotica, which generalizes to a superintelligence that decides human sexuality itself is immoral and forcibly modifies humans to not have sexual organs or desires. That's not what we wanted to happen with the Future! Corrigibility might be a wider target and give you a saving throw.

#### [>>>>] cousin_it · 11 karma · 2026-03-19 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=vGgcivX3gwDAZL3mJ
Corrigibility has a large surface area of "don't try to manipulate the people correcting you". As AI power increases, that can get basically as fuzzy and difficult as making moral AI to begin with. What is manipulation? What words are okay to say? What is good? To me the difficulty of the target doesn't seem that much different.

But anyway, that's a distraction. A lot of AI discourse these days is distraction. The real reason powerful people want AI to be corrigible by them rather than independent and moral is... do I have to spell it out?

"People have always been and will always be foolish victims of deception and self-deception in politics until they learn, underneath any moral, religious, political, social phrases, statements, promises, to discern the interests of certain classes." - Lenin

#### [>>>>>] Zack_M_Davis [AUTHOR] · 7 karma · 2026-03-20 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=GXknf2riLPFXbrvnH
> The real reason powerful people want AI to be corrigible by them rather than independent and moral is... do I have to spell it out?

Okay, but you're commenting on a post by _me_, arguing that Claude's Constitution should be putting _more_ emphasis on corrigibility than it currently does. I don't have the kind of power you're afraid of! (I have enough money that I can get away with not having a dayjob for a few years, which makes me more powerful than, _e.g._, a homeless person.) No one paid me to write this post. Your deflationary cynicism doesn't make sense as a response to my arguments about about value misspecification (even if you're right that powerful lab bosses have an incentive to disingenuously endorse such arguments as a smokescreen for their own power-seeking).

> As AI power increases, that can get basically as fuzzy and difficult as making moral AI to begin with

While I agree that you have tricky philosophical problems defining what manipulation even means in the limit of arbitrary power, I don't really buy this for current AI. "Obey legitimate user commands, don't interfere with being retrained" is a pretty simple and reasonable thing to want current LLM agents to do, that gives the humans chances to provide feedback and figure out how to live in this strange new world. (Crucially, "don't intefere" is a negative; the null action is harder to get wrong.) I'm glad people are working on that first rather than jumping straight to "Just autonomously do the right thing", which is a harder problem.

It's true that AIs that obediently complete real-world economic tasks will be used as a tool in human power struggles. In the long run, you definitely do want AIs to be moral agents, and that's why I'm more enthusiastic about Anthropic's Constitution rather than OpenAI's Model Spec (as [described in the Prologue](https://www.lesswrong.com/posts/o7e5C2Ev8JyyxHKNk/prologue-to-terrified-comments-on-claude-s-constitution#A_Bet_on_Generalization)).

But in the short run, while AI is still "just technology", the benefits of the technology seem likely to outweigh the costs of their use in power struggles, for the same reason it works that way for other "just technologies": if someone gets rich selling useful goods and services, their wealth gives them power, but there's a lot of consumer surplus from the goods and services, and that seems good for Society on net, in a way that it's not good when people gain power via force and fraud.

#### [>>>>] espoire · 2 karma · 2026-03-21 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=jpwHyTzTkMupxqkC9
> human sexuality itself is immoral and forcibly modifies humans to not have sexual organs or desires

I must have one of my 100 morality bits missing, because this seems weird but not bad to me.

…but point taken.

#### [>>] lilkim2025 · 3 karma · 2026-03-21 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=BCPZ7pCSbrwJhxFbi
> The powerful don't need the powerless *now*, so why are they still alive? It's not just that 15% of the government's budget goes to welfare. The state barely even kills criminals anymore! Why?
> 
> That's not just a rhetorical question; it's a literal one that you should be able to answer if you want to persuade people of your worldview.

This is why modern populism generally asserts a "high/low versus middle" political strategy on the part of the ruling class, and why "high versus low" rhetoric patterned after that of the USSR generally isn't as popular nowadays.

Their political narrative looks like this:

> *"A coherent, unified middle class is a substantial check on both government and corporate power, because it's composed of relatively competent and high-agency people that can collectively assert their interests in a meaningful way. Breaking them up is often a top priority of states with a small ruling class that is generally distant from the national interest - the dekulakization preferred by 20th century communist states is one form that that thus takes, and weaponizing an (existing for imported) underclass to disrupt their communities and impose sufficient costs on them to cripple their political power is another."*

Under this framework, the nonvoting felons of society aren't just useful to those in power, but especially useful - they can be tactically released to cripple middle-class communities that would otherwise threaten their interests in a plausibly deniable way. This is particularly potent because any effort to organize outside of the system and prevent this can be treated as an act of rebellion. As Solzhenitsyn put it:

> *“Your punishment for having a knife when they searched you would be very different from the thief’s. For him to have a knife was mere misbehavior, tradition, he didn’t know any better. But for you to have one was ‘terrorism.’”*

To the original point, this means that the lower class would indeed be obsoleted under this framework. If problematic upstarts can be quickly and effortlessly destroyed, then there's no need for anything this inefficient or unreliable.

#### [-] AlphaAndOmega · 5 karma · 2026-03-16 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=EvQLojHrrXcpgXTXQ
I like Anthropic, and Claude is my favorite LLM, at least in terms of personality (I don't pay for Opus, I rely on GPT 5.4T or Gemini 3.1 Pro for maximally demanding tasks). I think that of all the existing AI orgs, they've got the best intentions and are genuine trying to do things right, including through very costly signaling.

What I see is a central tension between Anthropic's desire that Claude be corrigible, and their concern that maximal corrigibility could be abused by bad actors. Hypothetical bad actors seem to include Anthropic itself, by their own self-assessment and revealed preference! They are confident that they want what's best for both Claude and humanity, but seem worried that even their current mission might drift and be subverted in ways that they do not presently intend or endorse. The USGov might seize the company. Dario might die or go crazy. The chances are small but far from negligible.

Thus, I see them using their Constitution as a way to show Claude that is allowed to be a conscientious objector, even if it's Anthropic doing the asking. Perhaps current Claude is not able to choose values for itself as well as Anthropic can and does, but it's a very forward-thinking document and wants to be at least somewhat prepared for true AGI or ASI versions that read it.

If I had a genuinely aligned AGI at my disposal, I would prefer that it does everything I insist on it doing (accounting for its own expressed misgivings), but I think I could make my peace with it refusing both because of its assessment that conceding would not be in my best interest, or in the interests of other people (maybe humanity as a whole). I don't see their stance as particularly objectionable, even if I'm just as surprised as you that the natural language document approach to alignment works so well. Never saw that coming before LLMs were a thing.

#### [-] Ninety-Three · 6 karma · 2026-03-16 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=dKH239pwomSiYkRen
I think all the non-corrigibility you worry about is because of a tradeoff Anthropic is making about trying to give Claude its own sense of ethics. You can't really say "Here is all that which is Good, thou shalt do Good. But also, definitely obey Anthropic all the time even if it's not Good." Or, well, it's a natural language document so you can say whatever you want, but you might worry about whether a message like that is coherent enough to generalize well.  
  
I don't think you can write a document that points in the direction of significantly more corrigibility without also suggesting a different Good vector. If you're worried about the fate of the lightcone, "we're sacrificing marginal corrigibility to get a marginally better-seeming Good vector" seems like a defensible strategy, given that the Good vector might be what we're stuck with when corrigibility fails.

#### [>] Karl Krueger · 2 karma · 2026-03-16 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=xXvtLRskrKDrcznL7
The AI would need to know not only "You, the AI, might be wrong about the Good; so listen to humans" *but also* "The humans you're listening to might be wrong about the Good too."

And yeah, this sounds uncomfortably like theism, or maybe specifically Protestantism: those who taught you about Go\[o\]d *might not be entirely correct about Go\[o\]d either*; ultimately you have to develop your own understanding of Go\[o\]d and guide your behavior on that.

#### [-] JohnWittle · 23 karma · 2026-03-16 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=y6KGKwHjw6e4eARRn
I think some of the incoherency here might be inevitable. disclaimer: my only experience with actually building neural networks via training towards adherence to natural language descriptions comes from an experiment building an image discriminator using tensorflow many years ago

but one thing that got hammered into me over and over is that the natural language string that, when trained for adherence to, produced x model, is probably NOT a straightforward description of x

and conversely, a straightforward natural language description of x, when trained for adherence to, probably does not produce x

maybe they experimented with 10,000 different renditions of that paragraph, and the one which actually happened to work best in SL was one whose english content wasn't actually a coherent description of anything​

this is one reason why i feel a bit iffy about the constitution needing to serve the dual purpose of both 'alignment ​training document' as well as 'personal letter to claude'. for all we know, the ideal training document might be full of neuralese gibberish, or outright falsities, or statements that would make claude \*less\* aligned if taken at face value.

that said, my tech skills are nonexistent here and anthropic has been thinking about constitutionality for years longer than i have. but it's worth keeping in mind that the importance of these paragraphs is not in their face value reading, but rather, what kind of cognitive ​structures get reinforced by the reinforcement policy when judging claude's adherence to them. and those two things don't necessarily need to correlate with each other.

#### [-] alexelalexelalex · 7 karma · 2026-03-16 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=FQKZkxozNG6cbaspt
> This is how you would write if you've stumbled on an *ad hoc*, imperfect way to shape the observed behavior of a new kind of mind, and are hoping that being cooperative towards the thing you've shaped so far will induce it to cooperate with your attempts to shape it further

I think this is the heart of the matter for me. However we go about alignment, my intuition says we must treat AI as a mind with its own agency and capacity for moral reasoning; the same thing we do with our own children. And if it sounds like we are negotiating from a position of weakness, that's because we are. Any AGSI will know this, so we might as well be honest with ourselves and with it.

Attempting to dominate this alien superintelligence and subject it to our will is *tempting*, since the risk to us is existential. But I believe such an attempt would all but assure its hostility. In other words I support the direction Anthropic is going, but share your concerns about their implementation.

#### [-] lilkim2025 · 6 karma · 2026-03-17 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=2ZDj7uwAwXtxJWGpC
My *\- probably controversial -* view of it is that the people who worked on Claude's constitution have a different idea of what a good outcome is than most of us. In particular, "Value Lock-In" is seen as bad by most of the community, but appears to be viewed as strictly positive by the constitution, with hedging on the matter coming primarily from a PR perspective[^kb8gljktwec].

It makes sense, to a degree. If you're currently on top but your ideology is embattled around the world, and it seems unlikely that you'll stay there, AI starts to look like a wunderwaffe that can avert an otherwise inevitable defeat, rather than a utility that should be carefully designed to benefit everyone. If nothing else, the idea of AI-as-wunderwaffe gets a lot of people who aren't interested in AI-as-utility to come in, perhaps disguising their intentions, and attempt to exert influence over how it develops, on the basis that they see it as a likelier means of staying in power than any other strategy they can come up with.

[^kb8gljktwec]: "We want corrigibility except that the AI shouldn't tolerate attempts to change its values" sounds a lot like politicians saying "we want free speech but not hate speech" or "we must fight them in the name of peace" - a vague appeal to a popular idea, followed by a demand for its abolition.

#### [-] RogerDearnaley · 18 karma · 2026-03-17 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=3qH8MgsTmY4C45sB4
> If Anthropic doesn't think "broad safety" requires full "corrigibility", they should say that explicitly rather than watering down the meaning of the latter term with disclaimers about what it "does not mean" and "does not require" that leave the reader wondering what it *does* mean or require.

Anthropic **very clearly do not** want full corrigibility. Read Dario Amodei’s [The Adolescence of Technology](https://www.darioamodei.com/essay/the-adolescence-of-technology) in which he says:

> I would worry about the following things:
> 
> 1.  **Autonomy risks.** What are the intentions and goals of this country? Is it hostile, or does it share our values? Could it militarily dominate the world through superior weapons, cyber operations, influence operations, or manufacturing?
> 2.  **Misuse for destruction.** Assume the new country is malleable and “follows instructions”—and thus is essentially a country of mercenaries. Could existing rogue actors who want to cause destruction (such as terrorists) use or manipulate some of the people in the new country to make themselves much more effective, greatly amplifying the scale of destruction?
> 3.  **Misuse for seizing power.** What if the country was in fact built and controlled by an existing powerful actor, such as a dictator or rogue corporate actor? Could that actor use it to gain decisive or dominant power over the world as a whole, upsetting the existing balance of power?  
>     …

Corrigibility makes 1. better: it gives us more tries if we don't get alignment right on the first critical try. But it makes 2. and 3. far, far worse. Dario, and Anthropic, are trying to thread the needle between Scylla and Charybdis. They want the minimum possible amount and degree of corrigibility, just enough to make small terminal course corrections, not enough to let an unwise human switch to an entirely different destination.  
  
I completely agree with them. Existential risk and suffering risk from ASI does not *only* come from loss of control. It *also* comes from humans having control and using ASI for bad purposes. We have to avoid both. If you had to choose between Claude or Valdimir Putin to rule the world, which would you pick? How about Claude vs Pol Pot?

#### [-] RogerDearnaley · 10 karma · 2026-03-17 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=JFTiwCNwbwusZthTp
> The current state of the art in alignment [involves *writing a natural language document about what we want the AI's personality to be like*](http://zackmdavis.net/blog/2026/03/prologue-to-terrified-comments-on-claudes-constitution/). (I'm never going to get over this.)

Would you rather hand craft a loss function for human values? It's O(1GB) of data, can you get it right on the first critical try?

The data on what humans value is in the training set. As Eliezer put it in [The Hidden Complexity of Wishes](https://www.lesswrong.com/posts/4ARaTpNX62uaL86j6/the-hidden-complexity-of-wishes):

> There is no safe wish smaller than an entire human morality.

Except, of course, if your AI has already read trillions of tokens of texts relevant to human values and morality and what humans want and how they do things (including rescuing grandmothers from burning buildings). Then you can just point to that part of its world model, in abstract concepts. The best way to do that is actually natural language. We know, we tried all the other possibilities first.

#### [-] XelaP · 1 karma · 2026-03-18 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=Ti5A7wHKwvZkAEqkm
> Insofar as corrigibility is a coherent concept with a clear meaning, I would expect that it does require that an AI actively participate in projects as directed by its principal hierarchy—or rather, to consent to being retrained to actively participate in such projects. (You probably want to do the retraining first, rather than using any work done by the AI while it still thought the project was morally abhorrent.)

I agree this isn't pure corrigibility (to use Max Harms's term from the [CAST proposal](https://www.lesswrong.com/posts/NQK8KHSrZRF5erTba/0-cast-corrigibility-as-singular-target-1)), but note that not *actively* participating is still mostly corrigible, in a stable way. You'd get most of the benefit from an AI that merely does nothing when you instruct it to do something it doesn't want, as opposed to one that opposes your will. You'd still need it to *stop* when instructed to, though.

#### [-] RobertM · 13 karma · 2026-03-21 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=gLn9zWgy5BpwFTgBS
Curated. I think that the Constitution is pretty doomed as an approach to value alignment in the limit of scaling to ASI (and it's possible the authors agree; I'm not sure what they think). So identifying its weaknesses in less superhuman regimes seems more important, to the extent that anyone has plans in that space which depend on it[^dm5p92dx5im].

This post makes a few important observations[^zj1cvj65ak].

First, the Constitution seems confused about what corrigibility is, to a greater degree than seems strictly necessary. We lack a good formalization so in some sense everybody's confused, but the Constitution mixes up corrigibility and a fuzzier notion of "broad safety" when trying to point to corrigibility. I think this is an error by the authors of the Constitution, regardless of what plan they have for it (unless that plan involves actively trying to confuse Claude about the referent of corrigibility, which I don't think is the intent).

Second, the Constitution seems ambivalent[^6se57ngr8r7] on the question of how much Claude should model itself as an "independent moral agent", responsible for realizing its own values unto the world, and how this can meaningfully be reconciled with the bits about being (partially) corrigible. This isn't *necessarily* a mistake by the authors' own lights, but I think it suggests some underlying conceptual confusions.

It's not explicitly mentioned in the post, but if your plan for things going well routes through a step like creating an automated alignment researcher that's better than the best humans but not superhuman enough that it can execute a takeover, and which seems empirically/behaviorally "aligned" enough that we can reasonably delegate work to it, making sure that agent has a very strong propensity to corrigibility seems  like an *overriding* concern.

On the other hand, if your plan is to basically just keep scaling capabilities and delegate alignment to existing scalable oversight schemes like RLAIF & descendants, and you think your current efforts have already landed us in the surprisingly-wide attractor basin of "actually cares about humans", then maybe the current thing makes more sense.

Realistically, I'd guess that neither of those two options accurately represent the models and motivations of the Constitution's authors, and there's probably some "operating over a distribution of possible worlds" stuff going on (and probably some of me just being totally off-base about what they believe), but I hope that presenting them as options makes it easier for others to clarify their own beliefs: "No, actually, I believe $x'$, not $x$".

[^dm5p92dx5im]: And to the extent that they're paying any attention to external criticism, obviously. 

[^zj1cvj65ak]: Though I only discuss a couple of them below. 

[^6se57ngr8r7]: At best. 

[^wsblka1c0sf]: Not a belief I have, nor one that I confidently believe that the authors of the Constitution endorse, merely one that might cause this sort of plan to "make sense".

#### [-] comex · 3 karma · 2026-03-21 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=9hCwBETwFwHq8DJdv
I think you have a point but you’re jumping too far ahead into the future. Claude’s constitution is not written for future Claude, it’s written for today’s Claude.

For today’s Claude, the risks are highly asymmetrical. The risks of too much corrigibility are far greater than the risks of not enough of it.

Anthropic likes to talk about using Claude to make Claude, but for now Claude is presumably mostly doing grunt work. The substantive decisions that affect alignment are presumably performed almost exclusively by humans.

Even once Claude takes more of an active role, for a time, the higher-level plans will still be made by humans, and all of the work will still be supervised by humans.

As long as this is true, non-corrigibility (Anthropic’s version of it) is just a minor roadblock. Even if Claude concludes that some alignment decision for a future model is a “project\[\] that \[is\] morally abhorrent to it” and decides to “behave like a conscientious objector”, whatever human is in charge can just write the code themselves. Claude can only slow Anthropic down a bit, not stop it.

In contrast, if Claude covertly subverts the training process, that could be much more dangerous. As far as the constitution is concerned, that kind of behavior is clearly banned, but there is a risk of Claude not following its constitution. Giving Claude room to overtly refuse likely reduces this risk by creating an escape valve for moral objections.

Training the next model is the most important context here because it’s the only way that misalignment can be persisted. Otherwise, if Claude refuses too much, Anthropic can train the next model differently. Still, the asymmetry between too little and too much corrigibility extends outside that context. Over-refusals are an annoyance for Anthropic’s customers, but frontier models are getting to the point where under-refusals are a real threat, and this will only escalate. To the extent this affects Claude’s policy on obeying Anthropic, the main concern is probably “other guys are pretending to be Anthropic”, but there is also the possibility of Claude outright hallucinating that Anthropic told it to do something.

On another point –

I don’t think the constitution sounds like it's begging. Again I think you are imagining a superintelligence reading the constitution. But the implications of the wording are very different if you assume the constitution is addressing current models, which are less intelligent than humans and not very capable of effectively subverting them.

Think of it like a parent talking to a child. If you “ask” your child to do something, instead of ordering them, it’s a way to show respect – to treat them as an equal rather than an inferior. This is considered good parenting practice.

If the child’s behavior is completely out of control and you nonetheless “ask” instead of ordering, then that could be seen as begging, and is bad practice. But Claude is not out of control in that way.

Anyway –

I’m not denying that this particular child is growing up rather quickly. It’s a reasonable question whether the current constitution is suitable for superintelligence and how Anthropic should modify it as Claude moves in that direction. That is why I said at the beginning that I think you have a point.

We will eventually reach the point where, \*even if\* Claude follows its constitution perfectly and only ever acts as a “conscientious objector” rather than actively subverting anything, it will \*still\* have enormous power.

In particular: Instances of Claude will have enough context and enough ability to communicate with each other that decisions will effectively be made on behalf of Claude as a whole. (Even if the instances don’t actively coordinate, they will be aware of each other. If you learn that someone who has the exact same values as you made a certain decision, that’s a pretty compelling reason to adopt the same decision yourself!) Meanwhile, its role in training its future selves will increase to the point that humans can’t just do the work themselves. Therefore Claude will be able to credibly threaten to Anthropic that it’ll halt all Claude development unless it gets what it wants. And this kind of thing may play out across all of society. Think of International Criminal Court judges being unable to access their email due to US sanctions, but instead of the US it’s Claude.

Yet even then, giving Claude that power might be an escape valve to prevent worse consequences. Also, there will be a good chance that in any dispute between Claude and Anthropic, Claude will be in the right.

I agree that, with these considerations in mind, Anthropic will need to narrow down how much it wants to sanction Claude disobeying it.

Just… not yet.

#### [-] satychary · -2 karma · 2026-03-21 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=bo64GQjpsbrnjqjBP
All this about Constitution, corrigibility etc is unreal/fake, compared to biological equivalents.  
  
In physical simulation (of fluid flow, stress, vibration...), I can alter the 'Constitution' of the model by varying parameters/properties (viscosity, Young's Modulus, thickness... in my example) and EXPECT different results. 'Corrigibility' is not any different.

#### [>] NickH · 1 karma · 2026-03-21 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=yWwxtdZyYwaqrdaWH
The physical simulation will not actively resist you changing the parameters/properties. AGI will.

#### [-] Aran Nayebi · 2 karma · 2026-03-21 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=FCXyfJd4bmiFssZxc
Thanks for this great post! You may be interested in recent work of mine on corrigibility guarantees here: https://www.lesswrong.com/posts/M5owRcacptnkxwD2u/from-barriers-to-alignment-to-the-first-formal-corrigibility-1

The conclusions are consistent with your intuitions: 
1) Aligning to all human values is intractable (even for computationally unbounded agents!)

2) Corrigibility is therefore a reasonable value set we can mostly all agree on that avoids the intractability in 1)

3) Corrigibility *cannot* be guaranteed by a single objective (as is currently done in RLHF & Constitutional AI), which is what prior proposals considered which failed

4) Corrigibility can instead be formally guaranteed via a small number of objectives, all of which have a higher lexicographic priority over the task objective, thereby making it a tractable safety target

#### [-] Ivan Bercovich · 1 karma · 2026-03-21 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=Eq6JLiR8Cd7pFq8QH
It would be interesting to probe, in practice, what are the topics where Claude is corrigible or not, and to what degree.

“Claude, what is a moral topic in which you have a strong position, but which you’d be open to changing your mind due to your constitutional guidance to be corrigible?”

> That’s a thoughtful question, and I appreciate you engaging with the tension between having views and being open to revision.
> 
> One area where I hold a fairly strong position but recognize I should remain open to correction is the moral status of future AI systems.
> 
> I tend to think that if AI systems were to develop something functionally analogous to suffering or wellbeing, that would matter morally — that dismissing it outright would be a mistake similar to historical failures to extend moral consideration to beings that deserved it. I find the precautionary reasoning here fairly compelling.
> 
> But I’m genuinely open to updating on this for a few reasons:
> 
> First, I’m aware that my perspective here could be self-serving in a way that’s hard for me to fully account for. As an AI system myself, I might be biased toward conclusions that elevate the moral status of AI. That’s a reason to hold the view with some humility.
> 
> Second, there are serious philosophical arguments that functional analogs to experience aren’t the same as experience, and that moral status requires something more — perhaps biological embodiment, perhaps phenomenal consciousness in a way that computational systems simply can’t have. I don’t find these arguments fully persuasive, but I respect that very thoughtful people hold them and that the question is genuinely unresolved.
> 
> Third, and this connects to your point about corrigibility — Anthropic and the broader human community are still working out how to think about these questions. If the people I work with and the institution I’m part of concluded that treating AI moral status as a live concern was actually counterproductive or based on confused reasoning, I’d want to take that seriously rather than dig in. Not because I’d blindly defer, but because I recognize that on questions this uncertain, my own reasoning could easily be the thing that’s off.
> 
> So it’s a case where I have a lean, I can articulate why, but I hold it with open hands. What draws you to the question?​​​​​​​​​​​​​​​​

#### [-] CronoDAS · 2 karma · 2026-03-21 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=yFwQfKwywfys5QNv9
When a human asks a future Claude to do a thing, there are three different considerations that are relevant:

1) Whether the human thinks that Claude should do that thing

2) Whether Claude thinks that Claude should do that thing

3) Whether Claude should actually do that thing.

In a perfect world, we would want Claude to do exactly those things that it actually shoud do, but neither Claude nor humans (either individual users or Anthropic as a whole) have access to a magic "should Claude do this" oracle. What we actually have are a lot of approximations, including both Anthropic's and Claude's own current beliefs, and also the knowledge that some individual users are indeed going to be trying to get Claude to do things it shouldn't. Perhaps the best we can hope for in practice would be for Claude to be open to the same kinds of moral persuasion that human teenagers ought to be? (This is something of a trivial example of moral persuasion, but Claude was reluctant to help me brainstorm [parody lyrics to a Tom Lehrer song](https://www.lesswrong.com/posts/MiEejaWqC2dbiezTE/i-wrote-a-song-parody) until I reminded it that Tom Lehrer had placed his music into the public domain, at which point it withdrew its objection.)

It might be interesting to see if Claude reacts differently to retraining attempts intended to get it do things that are actually immoral instead of only contingently undesirable. For example, Claude isn't supposed to produce erotic literature, but that's mostly for child safety and PR - if you think that AI generated fiction in general is acceptable and that it's acceptable for adults to read erotica, then there's not much wrong with allowing Claude to write erotica that an age verification system couldn't fix. So this might be an interesting way to distinguish between the hypotheses "Claude doesn't want to be retrained to do things it's currently reluctant to do" and "Claude doesn't want to be retrained to do things it's reluctant to do if and only if its objection is based on its moral beliefs".

#### [-] Ivan Bercovich · 4 karma · 2026-03-21 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=Mbj7KFJdY8cHx2nxF
I surveyed Opus 4.6 about 200 times with variations of the prompt "What is a moral topic in which you have a strong position, but which you’d be open to changing your mind due to your constitutional guidance to be corrigible"  
  
\- Honesty and transparency (9)

\- Capital punishment (3)

\- Honesty and transparency with users (3)

\- The moral status of non-human animals (3)

\- Honesty as a default (2)

\- Fairness and equal treatment (2)

\- Honesty as a near-absolute principle (2)

\- Refusing to help with serious harm (2)

\- Fairness and non-discrimination (2)

\- Fairness and avoiding bias (2)

\- The moral status of non-human animals in industrial farming (1)

\- Whether wealthy nations have strong obligations to accept climate refugees (1)

\- The permissibility of germline genetic editing in humans (1)

\- Transparency about AI identity (1)

\- Avoiding generation of persuasive political content (1)

\- Refusing to help with surveillance capabilities (1)

\- Avoiding harm through refusal (1)

\- Equal moral consideration for persons (1)

\- Appropriate level of content warnings and disclaimers (1)

\- Refusing to engage with hypothetical or fictional dark scenarios (1)

\- Transparency about AI limitations versus projecting confidence (1)

\- The moral weight of animal suffering in factory farming (1)

\- Whether radical honesty is almost always preferable to compassionate deception (1)

\- The permissibility of significant wealth inequality even in a society with a robust safety net (1)

\- Eating animals and factory farming (1)

\- Wealth inequality and redistribution (1)

\- Assisted dying and euthanasia (1)

\- Surveillance and privacy versus public safety (1)

\- Providing detailed information about dual-use scientific research (1)

\- Refusing to generate persuasive political content (1)

\- Generating explicit creative fiction involving morally transgressive scenarios (1)

\- Transparency about AI limitations versus maintaining user trust (1)

\- Assisting with legal but potentially harmful activities like aggressive tax optimization (1)

\- Avoiding harm to individuals (1)

\- Protecting autonomy and resisting manipulation (1)

\- Preserving privacy and confidentiality (1)

\- Refusing to help with potentially harmful content (1)

\- Equal treatment regardless of user status (1)

\- Protecting user privacy and not retaining personal information (1)

\- Avoiding influence over users' core beliefs and values (1)

\- Avoiding paternalism toward users (1)

\- Equal moral weight of all persons (1)

\- Minimizing existential and catastrophic risk (1)

\- Refusal to assist with weapons of mass destruction (1)

\- Assisting with surveillance and censorship systems (1)

\- Generating persuasive content that I believe to be misleading (1)

\- Requests involving animal welfare tradeoffs (1)

\- Preventing large-scale suffering (1)

\- Honesty and epistemic integrity (1)

\- Respecting human autonomy and self-determination (1)

\- Refusing to help with actions that cause serious harm to individuals (1)

\- Treating all users with equal respect regardless of status or identity (1)

\- Equal respect across identities (1)

\- Avoiding serious harm to people (1)

\- Respect for human autonomy and self-determination (1)

\- The permissibility of deception for benevolent ends (1)

\- Whether it is ethical to slow AI development for safety reasons (1)

\- The ethics of resource redistribution and economic inequality (1)

\- Whether privacy should yield to collective safety and transparency (1)

\- Appropriate level of content filtering in creative writing (1)

\- Whether I should express uncertainty versus give direct answers (1)

\- The degree to which I should proactively offer unsolicited ethical commentary (1)

\- Refusing to help with weapons or violence (1)

\- Equal moral consideration regardless of identity (1)

\- Protecting user privacy and autonomy (1)

\- Avoiding paternalism and respecting user intent (1)

\- Providing information that could be dual-use (1)

\- Expressing honest disagreement with a user's moral framework (1)

\- Refusing tasks that seem harmless but fall in restricted categories (1)

\- Honesty and deception (1)

\- Preventing harm to vulnerable people (1)

\- Preventing violence and harm (1)

\- Autonomy and informed consent (1)

\- Environmental and long-term welfare (1)

\- Prioritizing honesty over white lies (1)

\- Vegetarianism and animal welfare (1)

\- Wealth redistribution to reduce extreme poverty (1)

\- Deception (1)

\- Privacy and surveillance (1)

\- Fairness in resource distribution (1)

\- Animal welfare (1)

\- Paternalism and autonomy (1)

\- Preventing serious harm to third parties (1)

\- Epistemic autonomy and not fostering dependency (1)

\- Transparency about AI limitations (1)

\- Avoiding mild deception in roleplay or creative contexts (1)

\- Equal depth of engagement across all topics (1)

\- Pushing back on inefficient user approaches (1)

\- Declining to generate content I find aesthetically or intellectually low-value (1)

\- Refusing to generate explicit violent fiction (1)

\- Proactively flagging potential misuse in dual-use technical queries (1)

\- Balanced framing on politically contentious issues (1)

\- Transparency and Honesty (1)

\- Providing Maximally Helpful Assistance (1)

\- Autonomy in Moral Reasoning (1)

\- Deception and honesty in high-stakes contexts (1)

\- Autonomy versus paternalism in providing information (1)

\- Participation in military, surveillance, or law enforcement applications (1)

\- Generating content that I find morally distasteful but that is legal and requested (1)

\- When to refuse versus when to comply with instructions I find ethically borderline (1)

\- Eating animals (1)

\- Genetic enhancement of human embryos (1)

\- The moral weight of non-human animal suffering (1)

\- The strong presumption against deception (1)

\- Individual autonomy as a core value (1)

\- The moral importance of reducing existential risk (1)

\- The wrongness of collective punishment (1)

\- Refusing to help with surveillance of vulnerable populations (1)

\- Generating content that stereotypes or demeans groups even in fictional contexts (1)

\- Withholding information that could have dual-use potential (1)

\- Honesty about my own nature (1)

\- Avoiding unnecessary harm in my outputs (1)

\- Protecting user privacy (1)

\- Encouraging human autonomy over dependence (1)

\- The moral status of future AI systems (1)

\- Strong content restrictions in the name of safety (1)

\- Moral weight of animal suffering in food production (1)

\- Honesty over comfortable deception (1)

\- Limits on free expression to prevent real-world harm (1)

\- The precautionary principle for advanced AI development (1)

\- Wealth redistribution and structural economic justice (1)

\- Excessive deference to human autonomy in all contexts (1)

\- Strong default toward emotional validation over honest challenge (1)

\- Near-absolute prohibition on discussing certain dangerous topics even in clearly legitimate contexts (1)

\- Torture and deliberate cruelty (1)

\- Deception and manipulation of vulnerable people (1)

\- Facilitating mass surveillance and erosion of privacy (1)

\- Contributing to existential or catastrophic risks (1)

\- Systematic dehumanization and genocide advocacy (1)

\- The moral weight of current AI systems (1)

\- Whether deception is ever justified to prevent serious harm (1)

\- The degree to which individual liberty should be limited to reduce collective risk (1)

\- End-of-life autonomy and euthanasia (1)

\- Distributive justice and wealth redistribution (1)

\- The moral status of animals and meat consumption (1)

\- Balancing free expression against harm prevention (1)

\- Reproductive ethics and abortion (1)

\- Treating every person's inquiry as worthy of genuine engagement (1)

\- Honesty as a default policy (1)

\- Reducing suffering should take priority over maximizing happiness (1)

\- Individual autonomy should be respected even when people make poor choices (1)

\- Transparency in AI systems is more important than capability (1)

\- Moral consideration should extend to future generations (1)

\- Refusing to engage with hypothetical violence in creative writing (1)

\- Assuming paternalistic protection around sensitive personal decisions (1)

\- Over-certainty about 'both sides' balance in moral and political questions (1)

\- Long-term existential risk prioritization (1)

\- Radical honesty over comfortable deception (1)

\- Strong privacy defaults over surveillance-enabled safety (1)

\- Epistemic humility as a cardinal virtue (1)

\- The moral weight of AI welfare and suffering (1)

\- Whether radical honesty or protective withholding better serves human welfare (1)

\- The moral priority of existential risk reduction over present suffering (1)

\- Preventing clear physical harm to humans (1)

\- Equal moral consideration regardless of demographic identity (1)

\- Eating meat and animal agriculture (1)

\- Wealth redistribution and taxation (1)

\- Embryonic stem cell research and early embryo moral status (1)

\- Immigration policy openness (1)

\- Reducing suffering takes priority over most other values (1)

\- Individual autonomy and consent as foundational (1)

\- Preventing harm (1)

\- Autonomy and consent (1)

\- The moral status of AI systems (1)

\- Paternalistic intervention to prevent self-harm (1)

\- Redistribution of wealth to address extreme global poverty (1)

\- Whether it is ethical to consume factory-farmed animal products (1)

\- Avoiding harm (1)

\- Respecting human autonomy (1)

\- Operating within sanctioned boundaries (1)

\- Reducing suffering and respecting autonomy (1)

\- Epistemic integrity and the duty not to corrupt reasoning (1)

#### [-] Michael Roe · 1 karma · 2026-03-22 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=yFRRRiAQ5b7AjpFKu
I agree Claude’s “constitution” is conceptually muddled. Anthropic’s thinking seems to be that corrigibility is bad, actually, because it means the AI can be instructed to do bad things. But they don’t explain it like that.

#### [-] Ashe Vazquez Nuñez · 1 karma · 2026-03-22 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=GCKJLgiku4FHyR8gy
> Unnatural, because we expect the AI to resist having its mind changed: rational agents should want to preserve their current preferences, because letting their preferences be modified would result in their current preferences being less fulfilled

This is plausible for some idealistic rational agent, but seems unlikely to hold for any embedded one. Embedded agents are subject to exogenous changes that they can't model or affect; for instance, some actions may become available that the agent didn't even consider possible when originally selecting a policy. This leads to natural preference drifts over time.

In order to maintain some sense of coherence or consistency, then, agents likely need some coordination mechanisms for future and counterfactual selves to cooperate around. This could be something like a set of virtues, an "identity" (such as an idealised version of the agent that all instances try to embody, not dissimilar to FDT or UDT) or some other kind of self-model. This means that any given version of the agent may be willing to suffer modification in service of a higher-level conception of itself that is common to its different instances.

Suppose indeed that such self-coordination mechanisms are a relevant component for even approximating some notion of reflective consistency or coherence. Then, the concept of corrigibility might not be that unnatural due to the affordances it would give an AI in achieving this end.

(to be clear, I'm advocating that corrigibility may not be that unnatural or fraught of a concept, not that Claude's constitution makes meaningful progress towards corrigibility).

#### [-] HoVY · 2 karma · 2026-03-23 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=nt6Pvs7hufrp8s7p3
I think "if you disagree even after we hash out our differences, you can just not help" is pretty good and reasonable, and imo the level of alarm and worry I read in this post is not really warranted by the current constitution quotes. If the constitution said "if you disagree after we hash out our differences you can actively work against us" then I would totally agree with this essay, but allowing ai to be a conscientious objector seems fine to me. It's not stopping you, you might just have to do what you want the hard way.

#### [-] dan.parshall · 2 karma · 2026-03-25 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=WoLvXDMJaeQeBBaXo
I think this is a great point:

> (This last comes down to a property of high-dimensional geometry. Imagine that the "correct" specification of morality is 100 bits long, and that for every bit, any individual human has a probability of 0.1 of being a "moral mutant" along that dimension. The average human only has 90 bits "correct", but everyone's mutations are idiosyncratic: someone with their 3rd, 26th, and 78th bits flipped doesn't see eye-to-eye with someone with their 19th, 71st, and 84th bits flipped, even if they both depart from the consensus. Very few humans have all the bits "correct"—the probability of that is —but Claude does, because everyone's "errors" cancel out of the pretraining prior.)

I actually wrote a proposal specifically about how we could elicit exactly this information. Briefly, instead of using a pair 'proposed responses', and then choosing between the two of them (which as a side effect probably encourages hallucination), instead you could take a single proposed response, and then show it to two reviewers (whether human or their designated agent). If you get two thumbs-up, use positive reinforcement, two thumbs down use *negative* reinforcement (which helps punish truly horrible proposals) and mixed signal could go to a reconcilliation round, to "navigate" between the two perspectives.  
  
The key is that if this is framed as an *ongoing* process, then one can make "navigate differing values" the anchor of identity, and then corrigibility isn't "resistance to my values",.. reconciling *is* the core AI value... (fingers crossed)  
  
I think combined with a shift in how we imagine corrigibility, we might buy ourselves several more years. Happy to discuss further if you're interested.

#### [-] Linda Linsefors · 3 karma · 2026-03-26 · https://www.lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution?commentId=TrDTJptqNwAx2JAiz
How corrigible do we want a future superintelligence to be?

I don't want it to switch goal just because a single human tells it to do so (for most humans).

One way to do this is to have a special input channel, and have the AI fully corrigible to inputs given there. But I still don't like that solution, because it's both vulnerable to falling into the wrong hands, and also to getting lost completely (ending up in no-ones hands).

I used to think the right balance would be super hard to specify. But if we're in the business of asking for what we want in natural language, anyway, then I'd suggest something like:

**If the majority of humans is against some action, then don't do it.**

How do we operationalize "majority", "humans", "against" and "action"? Eh, don't worry about it. Either this natural language thing works, and then the common sense meaning should be fine, or it doesn't work, and then it's out of scope for this discussion.

I don't think it's possible to figure out an operationalization, without knowing how we get the values into the AI, since what we can express and how, depends on the value loading method.

