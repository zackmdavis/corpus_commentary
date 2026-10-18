Post: http://unremediatedgender.space/2020/Apr/book-review-human-diversity/
Fetched: 2026-10-15 (public Isso API)
Comments: 13 top-level

#### [-] tailcalled · 2 likes · 2020-04-28 · http://unremediatedgender.space/2020/Apr/book-review-human-diversity/#isso-16
> Meanwhile, my cursory understanding (while kicking myself for still not having put in the hours to get much farther into Probabilistic Graphical Models: Principles and Techniques) was that you need to understand causality in order to predict what interventions will have what effects: variance in rain may be statistically "explained by" variance in mud puddles, but you can't make it rain by turning the hose on. Maybe our feeble state of knowledge is why we don't know how to find reliable large-effect environmental interventions that still yet might exist in the vastness of the space of possible interventions.

You can create a causal version of PGSs by looking at SNPs that predict within-sibship variation, as siblings get randomly assigned genes from their parents. This has some challenges (e.g. you're going to want a correlation PGS in order to narrow down the SNPs you're searching through; and it's still a rather opaque result in that it doesn't tell you the internal structure of the causation), but still, it can absolutely work.

It will also still tell you that in a society that beats up redheads, red hair causes all sorts of problems, of course, so it doesn't solve the whole GxE causal controvery.

#### [-] sbkyvfx · 1 likes · 2020-04-28 · http://unremediatedgender.space/2020/Apr/book-review-human-diversity/#isso-17
This was a great post. Someday I'd like to be able to make sense of

shared environment arguments, but the rest of this I thought was clear

and basically correct.

I thought you might be interested to know that you have now gone further than even Moldbug was willing to go:

> Here’s how you are not-racist. You hold two beliefs: one, neurological problem-solving

performance (ie, “intelligence”) is homogenously distributed across the

genetically inhomogeneous human species. Two, it’s better to be smart than stupid.


> Ergo, no race is better than any other race, because all races are equally smart. Is that right? I hope I have it right.


> Here’s how I’m not-racist: I share neither belief.

That

whole post is pretty good, actually:

https://web.archive.org/web/20160328091704/https://medium.com/@curtis.yarvin/why-you-should-come-to-lambdaconf-anyway-35ff8cd4fb9d


> If you know someone is lying, their words mean nothing

Excellent, pithy way of expressing something I've had trouble communicating before, thank you.

#### [-] hawle · 1 likes · 2020-04-28 · http://unremediatedgender.space/2020/Apr/book-review-human-diversity/#isso-18
"change in a way that made the next generation grow up happier, and healthier, and smarter, that would be good for those children, and it wouldn't hurt anyone else!"

Unfortunately, not true. Or at the very least not perceived to be true since first order effects are legible to a much broader audience than second order effects.

#### [-] Emma · 5 likes · 2020-04-29 · http://unremediatedgender.space/2020/Apr/book-review-human-diversity/#isso-20
I have mixed feelings about your blog generally, but I really appreciate this post. It's helped to illuminate a lot of things I've been feeling for a while as someone very passionate about the broader goals and principles behind the current progressive movement who also often has trouble reconciling myself with a lot of their specific methodology - and of course it's difficult to find anyone criticising the latter who isn't just using that as a stepping stone to discredit the former, so it can be hard to work through when the conversation itself feels understandably off-limits to a lot of people. I think you've put that distinction into words here in a remarkably clear way that I'm sure I'll be thinking on for quite some time!

#### [-] tailcalled · 2 likes · 2021-04-20 · http://unremediatedgender.space/2020/Apr/book-review-human-diversity/#isso-176
> What goes for seeing trees, goes the same for "treating individuals as individuals": the process

of getting to know someone as an individual, involves your brain

exploiting the statistical relationships between what you observe, and

what you're trying to learn about. If you see someone wearing an Emacs

tee-shirt, you're going to assume that they probably use Emacs, and asking them about their dot-emacs file is going to seem like a better casual conversation-starter compared to the base rate of people wearing non-Emacs shirts. Not with certainty—maybe they just found the shirt in a thrift store and thought it looked cool—but the shirt shifts the probabilities implied by your decisionmaking.

The problem that Bayesian reasoning poses for naïve egalitarian moral intuitions, is that, as far as I can tell, there's no philosophically principled reason for "probabilistic update about someone's psychology on the evidence that they're wearing an Emacs shirt" to be treated fundamentally

differently from "probabilistic update about someone's psychology on

the evidence that she's female". These are of course different

questions, but to a Bayesian reasoner (an inhuman mathematical

abstraction for getting the right answer and nothing else), they're the same kind of question: the correct update to make is an empirical

matter that depends on the actual distribution of psychological traits

among Emacs-shirt-wearers and among women. (In the possible world where most

people wear tee-shirts from the thrift store that looked cool without

knowing what they mean, the "Emacs shirt → Emacs user" inference would

usually be wrong.) But to a naïve egalitarian, judging someone on their

expressed affinity for Emacs is good, but judging someone on their sex

is bad and wrong.

One concept I've seen Borsboom (I think) argue is that a test should not merely be correlated with what you are testing, but should instead be caused by what you are testing. He didn't really say why that would be relevant, instead claiming that it is obvious, but after thinking about it for a while I've come up with one argument: From a pragmatic point of view, having your measurement be caused by rather than merely correlated with what you are measuring means that you are capturing "all the variance"; while there might be unrelated factors that lead to measurement error, you're at least not totally blind to exceptions.

Applying it to your examples: Assuming that someone who wears an Emacs t-shirt uses Emacs makes a lot of sense, because presumably you've got some sort of Emacs use -> t-shirt causal relationship, moderated by factors like fanboyism or something. If you had instead used some sort of demographically confounded factor, like sex (kind of implausible factor, but I couldn't think of any alternatives off the top of my head), then you would miss all factors outside of this confounding. If a woman ended up as an Emacs user for some reason, then using sex as a proxy would not capture this at all, while using Emacs t-shirts probably would.

In practice, you probably do a mixture. It would be stupid to just update your beliefs about someone's (say) technical interests solely on the basis of their sex, and ignore things like her contributing to open-source projects, or literally just saying that she is interested in technical stuff, and the fact that one combines sources of information massively mitigates the problems related to missing information, but I still think there's something to be said for the idea that if your measurement is causally downstream from your variable of interest, it's treating people as individuals, while if it's confounded with or causally upstream from your variable of interest, it's stereotyping.

That said, this doesn't entirely resolve the issue of stereotyping. Even in the case of the Emacs t-shirt, while the t-shirt is downstream from whether they use Emacs, it's not downstream for whether asking about their dot-emacs file is a good casual conversation-starter for you. You are essentially taking Emacs users as your stereotype for who would be interested in discussing dot-emacs files. Which is a much more accurate stereotype than taking men for it, but still.

So really, the general pattern is something like, you've got some variable V that you want to make a projection for (such as "work production in the next few years if we hire them", "openness to conversation about Emacs", etc.), and then you pick one or more proxies P that influences V (such as "general intelligence", "Emacs use"), and a measurement M that is downstream of P (e.g. IQ scores, t-shirt). Stereotyping error happens in cases where P fails to correlate to V, while measurement error happens in cases where M fails to correlate to P; the total inference error is the combination of the two other errors.

#### [-] K Smith · 2 likes · 2021-08-12 · http://unremediatedgender.space/2020/Apr/book-review-human-diversity/#isso-242
The post is a fucking Triumph. Dear lord. I went into basically sharing Murray's worldview and thinking I had found a particularly eloquent kindred spirit..

I left with significant portions of that worldview upended and for the better. The Schelling Point framing is excellent. The (second) ball-hiding insight was enlightening. And, the synthesis of a new a moral perspective...well I can only sit in awed silence.

#### [-] asdf · 0 likes · 2021-08-16 · http://unremediatedgender.space/2020/Apr/book-review-human-diversity/#isso-243
The problem is that "blank slate" doesn't reduce group conflict.

First, it implicitly implies something like systemic racism, because why else would poor performing groups be poor performing.  People can hand wave here and try to say its multi-causal, but I think there was always a time limit on that strategy.  People will put up with it for a generation or two, but eventually they want to cash that equal outcomes check you promised them one way or another.

Second, people need to build models of how the world works.  You can't yank out "genetics" and still expect them to come up with a rational working model of existence.  Like pulling a thread and having the whole sweater unravel, we've seen more and more of enlightenment rationalism fall before the might of maintaining the "noble lie".

Third, what exactly would a HBD aware mainstream look like?  I guess it could be Hitler, but probably not.  Blank Slate didn't stop the Gulag and Hitler's old nemesis Churchill was a eugenicist.  Other factors were more important than beliefs about genetics.

How about Singapore?  Lee Kuan Yew was an out and out eugenicist who spoke about this stuff much less politely than Charles Murray and worked it into public policy explicitly.  No death camps over in Singapore.  In fact it's a pretty good country to live in for all involved, even the ethnic minorities.

#### [-] uhoh · 0 likes · 2021-08-18 · http://unremediatedgender.space/2020/Apr/book-review-human-diversity/#isso-244
What K Smith said above describes me perfectly. This post is a fucking triumph. Best thing I've read on the internet in quite some time.

First time visitor to the blog.

#### [-] tailcalled · 1 likes · 2021-10-25 · http://unremediatedgender.space/2020/Apr/book-review-human-diversity/#isso-253
> Notice how the "not allowing sex and race differences in psychological traits to appear on shared maps is the Schelling point for resistance to sex- and race-based oppression" actually gives us an explanation for why one might reasonably have a sense that there are dread doors that we must not open. Undermining the "everyone is Actually Equal" Schelling point could catalyze a preference cascade—a slide down the slippery slope to the the next Schelling point, which might be a lot worse than the status quo on the "amount of rape and genocide" metric, even if it does slightly better on "estimating heritability coefficients." The orthodoxy isn't just being dumb for no reason. In analogy, Galileo and Darwin weren't trying to undermine Christianity—they had much more interesting things to think about—but religious authorities were right to fear heliocentrism and evolution: if the prevailing coordination equilibrium depends on lies, then telling the truth is a threat and it is disloyal. And if the prevailing coordination equilibrium is basically good, then you can see why purported truth-tellers striking at the heart of the faith might be believed to be evil.

I've sometimes heard HBD people talk about how multiethnic democracy is inherently flawed, but I've been extremely skeptical; surely if you just acknowledged HBD, people could understand not to expect equality.

But this point throws that into question. If we assume that acknowledging HBD is going to throw us back to a terrible racial state, and we assume that denying HBD is going to throw us into a totalitarian obsession with everything being racist, then the only option left is to avoid multiethnic democracies.

Or well, the US doesn't have that option, because it's not an ethnically homogeneous country. Unless they committed genocide or eliminated democracy, but both of those seem very bad. But I'm speaking from the position of an ethnically homogenous country, so we could achieve it just by limiting immigration.

#### [>] tailcalled · 0 likes · 2022-02-15 · http://unremediatedgender.space/2020/Apr/book-review-human-diversity/#isso-269
Actually probably this is not so relevant, since we don't have a history of slavery etc. (or well we do, but in colonies only). In the US all of the terrible history seems like a major rhetorical motivator that doesn't appear in my country. So I can probably keep voting for as open borders as possible.

#### [-] tailcalled · 0 likes · 2022-10-07 · http://unremediatedgender.space/2020/Apr/book-review-human-diversity/#isso-445
Actually, speaking of...

> Undermining the "everyone is Actually Equal" Schelling point could catalyze a preference cascade—a slide down the slippery slope to the the next Schelling point, which might be a lot worse than the status quo on the "amount of rape and genocide" metric, even if it does slightly better on "estimating heritability coefficients."

Ozy's recent post made me think of a concrete example, which sort of shows up in your post. Namely, regarding:

> Recently, Richard Dawkins spurred a lot of criticism on social media for pointing out that selective breeding would work on humans (that is, succeed at increasing the value of the traits selected for in subsequent generations), for the same reasons it works on domesticated nonhuman animals—while stressing, of course, that he deplores the idea: it's just that our moral commitments can't constrain the facts. Intellectuals with the reading-comprehension skill, including Murray, leapt to defend Dawkins and concur on both points—that eugenics would work, and that it would obviously be terribly immoral.

As far as I understand, eugenics actually wouldn't work on humans in the way selective breeding works on animals, because as far as I understand, eugenics-as-actually-implemented is very different from selective-breeding-as-actually-implemented. I'm bad at history so I might be totally wrong, but as I understand, the main reproductive intervention of eugenics-as-actually-implemented was sterilizing the rare "worst" tail of people. But the rare "worst" tail of people is, well, rare! Evolution proceeds proportional to the selection gradient, and if your reproductive intervention changes very few reproductions, then that's not going to have much of an effect.

If I understand animal breeding programs correctly, then they often instead focus on the few very most desirable males, and have them mate with as many females as possible? If eugenics change e.g. 5% of reproductions, then maybe (hypothetically! heuristically!) animal breeding programs would change e.g. 95% of reproductions, making them 19x more effective.

Of course, it doesn't seem like you could realistically apply those sorts of breeding programs in humans. I mean, it would basically amount to the "best" men reproducing with ~all the women. This doesn't seem like it would be an acceptable arrangement to very many people except maybe to the "best" men.

If you somehow got rid of the moral concerns with HBD of classifying some people as inferior, I would not be surprised if you ran into another bottleneck: of classifying other people as superior. In fact, I guess that's literally what history has taught us? ... I should probably actually learn history before speculating on this. But it might be a potential lesson on robustness and slippery slopes.

#### [-] minette  · 0 likes · 2024-03-05 · http://unremediatedgender.space/2020/Apr/book-review-human-diversity/#isso-568
tl;dr you are willfully ignorant of any sociological knowledge because of ideological reasons

#### [>] Zack M. Davis · 1 likes · 2024-03-06 · http://unremediatedgender.space/2020/Apr/book-review-human-diversity/#isso-569
I'm ignorant of a lot of things, but always eager to learn more! Any textbooks you recommend?
