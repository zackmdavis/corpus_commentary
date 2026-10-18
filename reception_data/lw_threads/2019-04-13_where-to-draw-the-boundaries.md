Title: Where to Draw the Boundaries?
LessWrong-URL: https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries
Posted: 2019-04-13
Fetched: 2026-10-13 (LessWrong GraphQL API; rendered by tools/render_lw_threads.py)
Comments: 113 (commentCount field: 111)

#### [-] dadadarren · 9 karma · 2019-04-14 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=uKnY4tT9HLAqQhAtB
Interesting article. I dare not say I understand it fully. But to argue for some categories as more or less wrong than others is it fair to say you are arguing against [the ugly duckling theorem](https://en.wikipedia.org/wiki/Ugly_duckling_theorem)?

#### [>] Zack_M_Davis [AUTHOR] · 14 karma · 2019-04-15 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=uihmswXHj3748qjTi
Well, I usually try not to argue against _theorems_ (as contrasted to arguing that a theorem's premises don't apply in a particular situation)—but in spirit, I guess so! Let me try to work out what's going on here—

The boxed example on the _Wikipedia_ page you link, following Watanabe, [posits](https://en.wikipedia.org/w/index.php?title=Ugly_duckling_theorem&oldid=881589781#Mathematical_formula) a universe of three ducks—a White duck that comes First, a White duck that is not First, and a nonWhite duck that is not First—and observes that every pair of ducks agrees on half of the possible logical predicates that you can define in terms of Whiteness and Firstness. Generally, [there are sixteen](https://en.wikipedia.org/wiki/Truth_table#Binary_operations) possible truth functions on two binary variables (like Whiteness or Firstness), but here only eight of them are distinct. (Although really, only eight of them _could_ be distinct, because that's the number of possible subsets of three ducks (2³ = 8).) In general, we can't measure the "similarity" between objects by counting the number of sets that group them together, because that's the same for any pair of objects. We also get [a theorem](https://en.wikipedia.org/w/index.php?title=Ugly_duckling_theorem&oldid=881589781#Boolean_functions) on binary vectors: if you have some _k_-dimensional vectors of bits, you can use Hamming distance to find the "most dissimilar" one, but if you extend the vectors into 2^_k_-dimensional vectors of all _k_-ary boolean functions on the original _k_ bits, then you can't.

Watanabe concludes, "any objects, in so far as they are distinguishable, are equally similar" (!!).

So, I _think_ the reply to this is going to have to do with [inductive bias](https://www.lesswrong.com/posts/H59YqogX94z5jb8xx/inductive-bias) and the "coincidence" that we in fact live in a low-entropy universe where some cognitive algorithms actually do have an advantage, even if they wouldn't have an advantage averaged over all possible universes? Unfortunately, I don't think I understand this in enough detail to explain it well _(mumble mumble, [new riddle of induction](https://en.wikipedia.org/wiki/New_riddle_of_induction), blah blah, no canonical universal Turing machine for Solomonoff induction)_, but the main point I'm trying to make in _my_ post is actually much narrower and _doesn't_ require us to somehow find non-arbitrary canonical categories or reason about all possible categories.

I'm saying that _which_ "subspace" of properties a rational agent is interested in will depend on the agent's values, but _given_ such a choice, the categories the agent ends up with is going to be the result of running some clustering algorithm on the actual distribution of things in the world, which depends on the world, not the agent's values. In terms of Watanabe's ducks: you might not _care_ about a duck's color or its order, but redefining Whiteness to include the black duck is cheating; it's wireheading yourself; it can't help you optimize the ducks.

#### [-] homotowat · 33 karma · 2019-04-14 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=d8RPDWmR5yuwKTrpM
Considering how much time is spent here on this subject, I'm surprised at how little reference to [distributional](https://en.wikipedia.org/wiki/Distributional_semantics) [semantics](https://en.wikipedia.org/wiki/Distributional_semantics) is made. It's already a half-century long tradition of analyzing word meanings via statistics and vector spaces. It may be worthwhile to reach into that field to bolster and clarify some of these things that come up over and over.

#### [>] Zack_M_Davis [AUTHOR] · 7 karma · 2019-04-15 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=d393hE9aNr4nGCsiB
Thanks for the pointer! I've [played with](https://github.com/zackmdavis/Review_Alliance/blob/821ec2564b/united.py) word2vec and similar packages before, but had never thought to explore how those algorithms connect with the content of ["A Human's Guide to Words"](https://www.lesswrong.com/s/SGB7Y5WERh4skwtnb).

#### [-] ChristianKl · 12 karma · 2019-04-14 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=3v8JTuLJNksptekHf
> Similarly, the primary thing when you take a word in your lips is your intention to reflect the territory, whatever the means

This sentence sounds to me like you want to use Korzybski's metaphor while ignoring the point of his argument. After him language is supposed to be used to create semantic reactions in the audience and the *is a* of identity is to be avoided.

The essay feels like you struggle with is a but are neither willing to go Korzybski's way nor are you willing to provide a good argument for why we should use the *is a* of identity.

> Do not ask whether there's a rule of rationality saying that you shouldn't call dolphins fish. Ask whether dolphins are fish.

That feels to me very wrong. Beliefs are supposed to pay rent in anticipated experiences and discussing whether dolphins are fish in the abstract is detached from anticipated experiences.

Context matters a great deal for what words mean. Thomas Kuhn asked both physicists and chemists whether helium is a molecule:

> Both answered without hesitation, but their answers were not the same. For the chemist the atom of helium was a molecule because it behaved like one with respect to the kinetic theory of gases. For the physicist, on the other hand, the helium atom was not a molecule because it displayed no molecular spectrum.

If you use either notion of a molecule in the wrong community you are going to run into problems. Asking is 'Is helium a molecule?' in the abstract is not helpful.

#### [>] Benquo · 10 karma · 2019-04-14 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=JczstvwfcxakLsJEe
In standard English the statement "X is a Y" often means that within the relevant classification system X is a member of category Y. Which classification system is relevant often differs by context, but the OP deals with that explicitly:

> in order for a proposed category boundary to *not* be wrong, it needs to capture some statistical structure in reality, even if [reality is surprisingly detailed](http://johnsalvatier.org/blog/2017/reality-has-a-surprising-amount-of-detail) and there can be *more than one* such structure.

#### [>>] ChristianKl · 11 karma · 2019-04-15 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=HGSKc7SMJpMGDa7qk
When quoting *the map is not the territory* which is a slogan that was created to criticize this usage of *is a* within a dense 750 page book where on of the main messages is that *is a* shouldn't be used, I think that paragraph fails to adequately make a case that this common language usage is desirable and if so when it's desirable.

Saying that the primary intention which which language is used isn't to create some effect in the recipient of the language act is a big claim and Zack simply states it without any reflection.

My first reaction to the text was like WaiDai's *I don't really understand what you're suggesting here* where I'm unsure about the implication that are supposed to be made for practical language use. The second is noting that the text gets basics* like the primary intention of why words are used wrong.

*: I mean basic in the sense of fundamental and not as in easy to understand

#### [>>>] Zack_M_Davis [AUTHOR] · 5 karma · 2019-04-15 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=qQYyWk5cXuCA5gHfi
> Saying that the primary intention which which language is used isn't to create some effect in the recipient of the language act

It's notable to me that both of the passages from this post that you quoted in [the great-grandparent comment](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries#3v8JTuLJNksptekHf) were from the final section. Would your assessment of the post change if you pretend it had ended just before the Musashi quote, with the words "resulting in fallacies of compression"?

I was trying to create an effect in the recipients of the language act by riffing off Yudkowsky's riff off Musashi in ["Twelve Virtues of Rationality"](http://yudkowsky.net/rational/virtues/), which I expected many readers to be familiar with (and which is the target of the hyperlink with the text "is quoted"). My prereaders seemed to get it, but it might have been the wrong choice if too many readers' reactions were like yours.

#### [>>>>] ChristianKl · 0 karma · 2019-04-16 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=M62G4jQEBtBAtGxv5
I don't think it's hard to "get" the text in a certain way for a person who doesn't have strong opinions about terminology. It's internally consistent and doesn't conflict with other LW writing. I see how most people at my dojo would likely say "yeah, right".

The problem is that if you want to make inferences based on the text, it doesn't seem to be that the concepts pay rent. I don't think your prereaders read it while asking themselves "Does this pay rent?" That's also likely why WeiDei's request to get practical examples went unanswered.

The objection I voiced isn't to the Musashi quote. It's a stylistic choice which is defensible. My objection the text afterwards that reads to me like a summary of the point you want to make.

The values that Yudkowsky writes in the linked article are about empiricism but your post is detached from any empiricsm but about the search of essenses of words.

The search for transcendend essenses should be generally done with caution and you should get clear about why you search transcence from context.

#### [>>>>>] Zack_M_Davis [AUTHOR] · 8 karma · 2019-04-16 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=xRvua7bDwjQqLkRKL
> That's also likely why WeiDei's request to get practical examples went unanswered.

Alternative explanation: that comment was made on a Sunday afternoon in my timezone, I have a Monday-through-Friday dayjob that occupies a lot of my attention, and I wanted to set aside a larger block of time to read through the four comments (and surrounding context) Wei linked ([1](https://www.lesswrong.com/posts/xCpuSfT5Lt6kkR3po/my-take-on-agent-foundations-formalizing-metaphilosophical#5r6kKBoEiX6hQC4ks) [2](https://www.lesswrong.com/posts/pu3ddLSZjjmiiqQfh/another-take-on-agent-foundations-formalizing-zero-shot#TJtwakAfL7wwoaDKS) [3](https://www.lesswrong.com/posts/pZhDWxDmwzuSwLjou/asymptotically-benign-agi#4TaT6yR3FCiS34FZQ) [4](https://www.lesswrong.com/posts/ZeE7EKHTFMBs8eMxn/clarifying-ai-alignment#RrvmhuqvxsGwG45Yv)) and think carefully about them before composing a careful reply. (I spent my Sunday afternoon writing budget on [my reply to dadadarren](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries#uihmswXHj3748qjTi), which took a while because I had to study the "Ugly duckling theorem" _Wikipedia_ page he linked.) In contrast, a reply like this one, or my [reply to Dagon](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries#dpv9gAbyaeTowp9rs) don't require additional studying time to compose, which is why I can manage to type something like this now without being _too_ late to my dayjob.

> your post is detached from any empiricsm but about the search of essenses of words.

I don't think this is a fair characterization of the post.

I need to go get dressed and catch a train now. I'll ping you when my reply to Wei is up.

#### [>>>>>>] ChristianKl · -12 karma · 2019-04-17 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=5uzb3opQBMXfK2vF5
If a concept is well worked out, people who read a post should be able to apply it to practical examples themselves.

I would generally think that people who write a long post on a new concept should spend time thinking about how it applies to practical examples before presenting the concept and your suggestion that this needs additional studying time in indicative of the thesis that how the concept pays rent is not well studied.

#### [>>>>>>>] Zack_M_Davis [AUTHOR] · 19 karma · 2019-04-18 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=MfQWpFJqSgt7hp7k7
You're being _bizarrely_ demanding, and I don't understand why. Have I done something to offend you somehow? (If I have accidentally offended and there's some way I could make amends, feel free to PM me.)

I agree that authors advocating an idea should provide examples. That's why the OP does, in fact, provide some examples (about dolphins, abstract points in ℝ³, and job titles). I also have a couple other [cached](https://www.lesswrong.com/posts/2MD3NMLBPCqPfnfre/cached-thoughts) "in the wild" examples in mind that I intend to include in my reply to Wei (_e.g._, search for the word _eargreyish_ in Scott Alexander's ["Anti-Reactionary FAQ"](https://slatestarcodex.com/2013/10/20/the-anti-reactionary-faq/)). But, as the grandparent mentions, Wei specifically asked if I had any thoughts on four of his comments (which I still haven't read, incidentally). I _can't possibly_ have cached such thoughts in advance!

Writing _good_ comments takes nontrivial time and mental energy and given that at least some _Less Wrong_ readers probably have things like jobs (!) or possibly even families (?!), I _really_ don't think it's reasonable to infer that someone is _incapable_ of offering a satisfactory reply just because they haven't replied within a couple days.

I had a _really stressful_ day yesterday. I just got home today. After posting this comment, I want to make dinner and relax and read [the new Greg Egan novel](https://publishing.tor.com/perihelionsummer-gregegan/9781250313775/) for a while. After that, I intend to spend some time writing blog comment replies—to Wei, to [Dagon](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries#Kdp8eAKYuYg8MmHRD) again, to someone on Reddit—and then _maybe_ to some [of](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries#MJLYHq8v35KGquT3G) [your](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries#d7Z5hK5AQGgbPSoGw) [comments](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries#d63iwa9Nf6FLB4Gjm), if I still have time. (I also need to look up what I need to bring to my DMV appointment tomorrow.) Please be patient with me—although if you're so dissatisfied by both the post, and my comments so far, then I fear my future comments are unlikely to be _that_ much more to your liking, so it's not clear why you should be so eager to see them be posted faster.

In conclusion, I'm sorry you didn't like my blog post about the information theory of dolphins. Please feel free to downvote it if you haven't already.

#### [>>>>>>>] Zack_M_Davis [AUTHOR] · 18 karma · 2019-04-21 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=sTFzPW3v4rjMwNedw
(continued from sister comment)

My [reply to Wei is now up](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries#9SeYXBqX8H2zKGNBs). (I finally looked at his four links and didn't end up engaging with them, but I endorse [Benquo's comment on #4](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries#uuLqLCLYszqTYdpZq).)

I also left a brief [reply to your comment about chronic fatigue syndrome](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries#vDAoYFimBp87q2gxs), and a [reply to your comment critiquing the paragraph about "poison."](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries#8qH2vzeik988hsjbF) I hope this helps clarify what I'm trying to communicate.

Unfortunately, I don't think your participation here has been a net-positive for the value of the comments section, and (with some sadness) I have decided to add you to the "Banned Users" list in the moderation section of my account settings.

#### [>>>>>>>] Zack_M_Davis [AUTHOR] · 6 karma · 2023-02-19 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=JwdWnAQGmT3aFEucp
I've now un-banned you from commenting on my posts, because I've been persuaded by [Said Achmiz](https://www.lesswrong.com/users/saidachmiz?mention=user)'s case that we shouldn't actually have that feature.

#### [>>>>>>>>] Zack_M_Davis [AUTHOR] · 2 karma · 2023-04-13 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=MTWhWqwFEJHiRaBWH
Huh, I happened to glance at the [moderation page](https://www.lesswrong.com/moderation), and the ban was still there; I guess I must have forgotten to click "Submit" when I tried to remove it the other month? It should be fixed now, [ChristianKI](https://www.lesswrong.com/users/christiankl?mention=user).

#### [>] abramdemski · 8 karma · 2020-12-13 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=WkYZMDYzo6HTX56xM
> This sentence sounds to me like you want to use Korzybski's metaphor while ignoring the point of his argument. After him language is supposed to be used to create semantic reactions in the audience and the *is a* of identity is to be avoided.
> 
> The essay feels like you struggle with is a but are neither willing to go Korzybski's way nor are you willing to provide a good argument for why we should use the *is a* of identity.

I would think this unsurprising, as most of lesswrong is ***very*** happy to take Korzybski's metaphor while ignoring the point of his argument. I have never heard what I take to be a real argument for actually eliminating "is a" as a *possible thing to mean*, only arguments that in English, "is" and related words cause some problems due to ambiguities, missing information, and unwanted implications. I have rarely seen LW-cluster aspiring rationalists avoid forms of "is", and never heard a serious endorsement of such avoidance on LW.

I'm curious if you think "is a" should be eliminated as a possible thing to mean. I would be interested in hearing your argument!

#### [-] Wei Dai · 21 karma · 2019-04-14 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=SGTZmSkTB479Mzc49
As someone who seems to care more about terminology than most (and as a result probably gets into more terminological debates on LW than anyone else (see [1](https://www.lesswrong.com/posts/xCpuSfT5Lt6kkR3po/my-take-on-agent-foundations-formalizing-metaphilosophical#5r6kKBoEiX6hQC4ks) [2](https://www.lesswrong.com/posts/pu3ddLSZjjmiiqQfh/another-take-on-agent-foundations-formalizing-zero-shot#TJtwakAfL7wwoaDKS) [3](https://www.lesswrong.com/posts/pZhDWxDmwzuSwLjou/asymptotically-benign-agi#4TaT6yR3FCiS34FZQ) [4](https://www.lesswrong.com/posts/ZeE7EKHTFMBs8eMxn/clarifying-ai-alignment#RrvmhuqvxsGwG45Yv))), I don't really understand what you're suggesting here. Do you think this advice is applicable to any of the above examples of naming / drawing boundaries? If so, what are its implications in those cases? If not, can you give a concrete example that might come up on LW or otherwise have some relevance to us?

#### [>] cousin_it · 5 karma · 2019-04-15 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=ekcGJyJGaremBD7Ex
This makes me curious - have you found that terminological debates often lead to interesting ideas? Can you give an example?

#### [>>] ChristianKl · 4 karma · 2019-04-16 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=d7Z5hK5AQGgbPSoGw
Whether to call something dephlogisticated air or oxygen was a very important terminological debate in chemisty even when the correlational cluster was the same. It matters if you conceptualize it as absense of something or as positive existence.

In medicine the recent debate about renaming chronic fatigue syndrome (CFS) into systemic exertion intolerance disease (SEID) is a quite interesting one.

With CFS it's a quite unclear where to draw the boundary. With SEID you can let someone exercise and then observe how long their body needs to recover and when they take much longer to recover from the exertion you can put the SEID diagnosis on them.

CFS and SEID are both cases where certain states correlate with each other Zacks post doesn't help us at all to reason about whether we should prefer CFS or SEID as a term.

#### [>>>] Zack_M_Davis [AUTHOR] · 12 karma · 2019-04-21 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=vDAoYFimBp87q2gxs
> CFS and SEID are both cases where certain states correlate with each other Zacks post doesn't help us at all to reason about whether we should prefer CFS or SEID as a term. 

I'm definitely _not_ claiming to have the "correct" answer to all terminological disputes. (As the post says, "Of course, there isn't going to be a unique way to encode the knowledge into natural language.") 

Suppose, hypothetically, that it were discovered that there are actually two or more _distinct_ etiologies causing cases that had historically been classified as "chronic fatigue syndrome", and cases with different etiologies responded better to different treatments. In this hypothetical scenario, medical professionals would want to split what they had previously called "chronic fatigue syndrome" into two or more categories to reflect their new knowledge. I think someone who insisted that "chronic fatigue syndrome" was still a good category given the new discovery of separate etiologies would be making a mistake (with respect to the goals doctors have when they talk about diseases), even if the separate etiologies had similar symptoms (which is what motivated the _CFS_ label in the first place).

In terms of the configuration space visual metaphor, we would say that while "chronic fatigue syndrome" is a single cluster in the "symptoms" subspace of Diseasespace, more variables than just symptoms are decision-relevant to doctors, and the _CFS_ cluster doesn't help them reason about those other variables.

#### [>>] Wei Dai · 18 karma · 2019-04-16 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=kEwyyW2m53DdEYWi8
My interest in terminological debates is usually not to discover new ideas but to try to prevent confusion (when readers are likely to infer something wrong from a name, e.g., because of different previous usage or because a compound term is defined to mean something that's different from what one would reasonably infer from the combination of individual terms). But sometimes terminological debates can uncover hidden assumptions and lead to substantive debates about them. See [here](https://www.lesswrong.com/posts/xCpuSfT5Lt6kkR3po/my-take-on-agent-foundations-formalizing-metaphilosophical#BK68tZ9gwK7SGgApk) for an example.

#### [>] Benquo · 14 karma · 2019-04-16 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=g9MKi4MrB6LLGmQwm
Sometimes people redraw boundaries for reasons of local expediency. For instance, the category of AGI seems to have been expanded implicitly in some contexts to include what might previously have just been called a really good machine learning library that can do many things humans can do. This allows AGI alignment to be a bigger-tent cause, and raise more money, than it would in the counterfactual where the old definitions were preserved.

This article seems to me to be outlining a principled case that such category redefinitions can be systematically distinguished from purely epistemic category redefinitions, with the implication that there's a legitimate interest in tracking which is which, and sometimes in resisting politicized recategorizations in order to defend the enterprise of shared mapmaking.

#### [>>] ChristianKl · 5 karma · 2019-04-17 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=MJLYHq8v35KGquT3G
I don't see how this article argues against a wider AGI definition. The wider definition is still a correlational cluster.

The article doesn't say that it's worthwhile to keep historical meaning of a term like AGI. It also doesn't say that it's good to draw the boundaries in a way that a person can guess where the boundary is based on understanding the words *artificial*, *general* and *intelligence*.

It's not a thinner boundary so that *"38\. Your definition draws a boundary around a cluster in an inappropriately 'thin' subspace of Thingspace that excludes relevant variables, resulting in [fallacies of compression](https://www.lesswrong.com/posts/y5MxoeacRKKM3KQth/fallacies-of-compression)."* might be violated.

#### [>>>] Benquo · 2 karma · 2019-04-18 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=HZ8hcHSp3AY8HTdjT
The article didn't "argue against" a wider AGI definition. It implied a more specific claim than "for" or "against."

#### [>>>>] ChristianKl · 2 karma · 2019-04-18 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=zRGw4Go9sxkkwwqW8
The article starts by speaking about " *It is what people* should *be trying to do* ", say in it's middle "This leaves aspiring instructors of rationality in something of a predicament: in order to *teach* people how categories can be more or (ahem) [less wrong](https://tvtropes.org/pmwiki/pmwiki.php/Main/TitleDrop)," and ends with speaking about what people must do.

That does appear to me like an article that intends to make a case that people should prefer certain definition over other definitions.

If your case is rather that the value of the article is about classification of how boundaries are drawn to distinct ways those boundaries are drawn, it seems to me surprising that you read out of the article that certain claims should be classified as *redrawing boundaries for reasons of local expediency* that seems odd to me given that the article neither speaks about *redrawing boundaries nor redefining boundaries* nor about classifying anything under the suggested category of "*local expediency*".

#### [>>>>>] Benquo · 4 karma · 2019-04-18 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=cWuy86gwYB2EFofc8
Rationality discourse is necessarily about specific contexts and purposes. I don't think the Sequences imply that a spy should always reveal themselves, or that actors in a play should refuse to perform the same errors with the same predictable bad consequences two nights in a row. Discourse about how to speak the truth efficiently, on a site literally called "Less Wrong," shouldn't have to explicitly disclaim that it's meant as advice within that context every time, even if it's often helpful to examine what that means and when and how it is useful to prioritize over other desiderata.

#### [>>>>>>] ChristianKl · 3 karma · 2019-04-18 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=DxWP3ASis7t4BPPNi
I'm not sure what your position happens to be. Is it "This post isn't advice. It's wrong for you (ChristianKl) to expect that the author explicitely disclaims giving advice when he doesn't intent to give advice."?

If that's the case, it seems strange to me. This post contains explicit statemensts about what people should/must do. It contains those in the beginning and in the end, which are usually the places where an essay states it's purpose.

It's bad to be too vague to be wrong.

Postmodern writing about how to speak truth efficiently that's to vague to be wrong is problematic and I don't think having a bunch of LW signaling and cheers for rationalists make it better.

#### [>] Benquo · 9 karma · 2019-04-16 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=uuLqLCLYszqTYdpZq
The article seems indirectly relevant to example 4, in which an epistemic dispute about how to divide up categories is getting mixed with a prudential dispute on which things to prioritize. Once a category is clearly designated as "that which is to be prioritized," it becomes more expensive to improve the expressive power of your vocabulary by redrawing the conceptual boundaries, since this might cause your prioritization to deteriorate.

Possibly the right way to proceed in that case would be to work out a definition of the original category which more explicitly refers to the reasons you think it's the right category to prioritize, perhaps assigning this a new name, so that these discussions can be separated.

#### [>] Zack_M_Davis [AUTHOR] · 20 karma · 2019-04-21 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=9SeYXBqX8H2zKGNBs
Hi, Wei—thanks for commenting! (And sorry for the arguably somewhat delayed reply; it's been a really tough week for me.)

> can you give a concrete example that might come up on LW or otherwise have some relevance to us?

Is _Slate Star Codex_ close enough? In his ["Anti-Reactionary FAQ"](https://slatestarcodex.com/2013/10/20/the-anti-reactionary-faq/), Scott Alexander writes—

> Why use this made-up word ["demotism"] so often?

> Suppose I wanted to argue that mice were larger than grizzly bears. I note that both mice and elephants are "eargreyish", meaning grey animals with large ears. We note that eargreyish animals such as elephants are known to be extremely large. Therefore, eargreyish animals are larger than noneargreyish animals and mice are larger than grizzly bears.

> As long as we can group two unlike things together using a made-up word that traps non-essential characteristics of each, we can prove any old thing.

This post is mostly just a longer, more detailed version (with some trivial math) of the point Scott is making in these three paragraphs: mice and elephants form a cluster if you [_project_](https://en.wikipedia.org/wiki/Projection_(linear_algebra)) into the subspace spanned by "color" and "relative ear size", but using a word to point to a cluster in such a "thin", impoverished subspace is a dishonest rhetorical move when your interlocutors are trying to use language to mostly talk about the _many_ other features of animals which don't covary much with color and relative-ear-size. This is obvious in the case of mice and elephants, but Scott is arguing that a similar mistake is being made by reactionaries who classify Nazi Germany and the Soviet Union as "demotist", and then argue that liberal democracies suffer from the same flaws on account of being "demotist." Scott had previously [dubbed this kind of argument the "noncentral fallacy" and analyzed how](https://www.lesswrong.com/posts/yCWPkLi8wJvewPbEp/the-noncentral-fallacy-the-worst-argument-in-the-world) it motivates people to argue over category boundaries like "murder" or "theft."

Downthread, you [wrote](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries#kEwyyW2m53DdEYWi8)—

> My interest in terminological debates is usually not to discover new ideas but to try to prevent confusion (when readers are likely to infer something wrong from a name, e.g., because of different previous usage or because a compound term is defined to mean something that's different from what one would reasonably infer from the combination of individual terms).

I agree that preventing confusion is the main reason to care about terminology; it only takes a moderate amount of good faith and philosophical sophistication for interlocutors to negotiate their way past terminology clashes ("I wouldn't use that word because I think it conflates these-and-such things, but for the purposes of this conversation ..." _&c._) and make progress discussing actual ideas. But I wanted to have this post explaining _in detail_ a particular thing that can go wrong when philosophical sophistication is lacking or applied selectively, which was _mostly_ covered by Eliezer's ["A Human's Guide to Words"](https://www.lesswrong.com/s/SGB7Y5WERh4skwtnb), but of which I hadn't seen the "which subspace to pay attention to / do clustering on" problem treated anywhere in such terms.

#### [>>] Wei Dai · 19 karma · 2019-04-21 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=i9h9RhRmJrhgCBQ93
Thanks, I think I have a better idea of what you're proposing now, but I'm still not sure I understand it correctly, or if it makes sense.

>mice and elephants form a cluster if you project into the subspace spanned by “color” and “relative ear size”, but using a word to point to a cluster in such a “thin”, impoverished subspace is a dishonest rhetorical move when your interlocutors are trying to use language to mostly talk about the many other features of animals which don’t covary much with color and relative-ear-size.

But there are times when it's *not* a dishonest rhetorical move to do this, right? For example suppose an invasive predator species has moved into some new area, and I have an hypothesis that animals with grey skin and big ears might be the only ones in that area who can escape being hunted to extinction (because I think the predator has trouble seeing grey and big ears are useful for hearing the predator and only this combination of traits offers enough advantage for a prey species to survive). While I'm formulating this hypothesis, discussing how plausible it is, applying for funding, doing field research, etc., it seems useful to create a new term like "eargreyish" so I don't have to keep repeating "grey animals with relatively large ears".

Since it doesn't seem to make sense to *never* use a word to point to a cluster in a "thin" subspace, what is your advice for when it's ok to do this or accept others doing this?

#### [>>>] Zack_M_Davis [AUTHOR] · 3 karma · 2019-04-29 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=uMxqzdYbs3tEqA6dw
(I continue to regret my slow reply turnaround time.)

> But there are times when it's _not_ a dishonest rhetorical move to do this, right?

Right. In Scott's example, the problem was using the "eargrayish" concept to [imply](https://www.lesswrong.com/posts/4FcxgdvdQP45D6Skg/disguised-queries) (bad) inferences about size, but your example isn't guilty of this.

However, it's also worth emphasizing that the inferential work done by words and categories is often spread across _many_ variables, including things that aren't as easy to observe as the features that were used to perform the categorization. You can infer that "mice" have very similar genomes, even if you never actually sequence their DNA. Or if you lived before DNA had been discovered, you might _guess_ that there exists some sort of molecular mechanism of heredity determining the similarities between members of a "species", and you'd be _right_ (whereas similar such guesses based on concepts like "eargrayishness" would probably be wrong).

(As it is written: ["Having a word for a thing, rather than just listing its properties, is a more compact code precisely in those cases where we can infer some of those properties from the other properties."](https://www.lesswrong.com/posts/yLcuygFfMfrfK8KjF/mutual-information-and-density-in-thingspace))

> Since it doesn't seem to make sense to _never_ use a word to point to a cluster in a "thin" subspace, what is your advice for when it's ok to do this or accept others doing this?

Um, watch out for cases where the data clusters in the "thin" subspace, but doesn't cluster in other dimensions that are actually relevant in the context that you're using the word? (I wish I had a rigorous reduction of what "relevant in the context" means, but I don't.)

As long as we're talking about animal taxonomy (dolphins, mice, elephants, _&c._), a concrete example of a _mechanism_ that systematically produces this kind of distribution might be [Batesian](https://en.wikipedia.org/wiki/Batesian_mimicry) or [Müllerian mimicry](https://en.wikipedia.org/wiki/M%C3%BCllerian_mimicry) (or [convergent evolution](https://en.wikipedia.org/wiki/Convergent_evolution) more generally, as with dolphins' likeness to fish). If you're working as a wildlife photographer and _just_ want some cool snake photos, then a concept of "red-'n'-yellow stripey snake" that you formed from observation (abstractly: you noticed a cluster in the subspace spanned by "snake colors" and "snake stripedness") might be completely adequate for your purposes: as a photographer, you just don't care whether or not there's more structure to the distribution of snakes than what looks good in your pictures. On the other hand, if you actually have to handle the snakes, suddenly the difference between the harmless [scarlet kingsnake](https://en.wikipedia.org/wiki/Scarlet_kingsnake) and the poisonous [coral snake](https://en.wikipedia.org/wiki/Coral_snake) ("red on yellow, kill a fellow; red on black, venom lack") is very relevant and you want to be modeling them as separate species!

#### [-] Benquo · 21 karma · 2019-04-14 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=4yHu75kHwDbuKirEA
This is a nice crisp summary of something kind of like pragmatism but capable of more robust intersubjective mapmaking:

> Everything we identify as a joint is a joint not "because we care about it", but because it *helps us think about* the things we care about.

To expand this a bit, when deciding on category boundaries, one should assess the effect on the cost-adjusted expressive power of all statements and compound concepts that depend on it, not just the direct expressive power of the category in question. Otherwise you can't get things like Newtonian physics and are stuck with the Ptolemaic or Copernican systems. (We REALLY don't care about Newton's laws of motion for their own sake.)

#### [-] romeostevensit · 5 karma · 2019-04-15 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=4N3EnvjQhYXrseLnZ
treating reality as fixed and self as fixed and the discovery of the proper mapping between self concepts and reality concepts is doomed to failure because both your own intentions are fluid depending on what you are trying to do and your own sense of reality is fluid (including self model). Ontologies are built to be thrown away. They break in the tails. Fully embracing and extending the Wittgensteinian revolution prevents you from wasting effort resisting this.

#### [>] Benquo · 13 karma · 2019-04-18 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=XPBtuNACFMAGgXn9f
This seems technically true but not relevant. Important classes of intersubjective coordination require locally stable category boundaries, and some ontologies have more variation we care about concealed in the tails than others.

There are *processes* that tend towards the creation of ontologies with stable expressive power, and others that make maps worse for navigation. It's not always expedient to cooperate with the making of a map that lets others find you, but it's important to be able to track which way you're pushing if you want there to *sometimes* be good maps.

#### [>>] romeostevensit · 11 karma · 2019-04-18 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=bmSbGG4kvuu7PHFJ5
I'm saying that this post itself is falling prey to the thing it advises against. Better to point at a cluster that helps navigate, like Hanson's babblers than to talk about the information theoretic content of aggregate clusters.

#### [>>>] Benquo · 13 karma · 2019-04-18 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=QbF8MzMtpGr4aRPGN
It seems to me like the OP is motivated by a desire to improve decisionmaking processes by making a decisive legal argument against corruption in front of a corrupt court, and that this is an inefficient way of coordinating to move people who are reachable to a better equilibrium.

Does that seem like substantively the same objection to you?

I found parts of the post object-level helpful, like the bit I directly commented on, but overall agree it's giving LW too much credit for coordinating towards "Rationality." But people like Zack will *correctly* believe that LW's corruption is not common knowledge if people like us aren't willing to state the obvious explicitly.

#### [>>>>] romeostevensit · 10 karma · 2019-04-19 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=5QBFjvTwL4pXT5JPA
Yeah, pointing at the same stuff. That clarification helped.

#### [-] Dagon · 3 karma · 2019-04-15 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=Gn2RR4daCE58xZeAY
I worry that we're spending a LOT of energy on trying to "carve at the joints" of something that has no joints, or is so deep that the joints don't exist in the dimensions we perceive. Categories, like all models, can be better or worse for a given purpose, but they're never actually right.

The key to this is "for a purpose". Models are useful for predictions of something, and sometimes for shorthand communication of some kinds of similarity.

Don't ask whether dolphins are fish. Don't believe or imply that category is identity. Ask whether this creature needs air. Ask how fast it swims. etc. When talking with people of similar background and shared context, call it a fish or an aquatic mammal, depending on what you want to communicate.

#### [>] Zack_M_Davis [AUTHOR] · 13 karma · 2019-04-15 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=dpv9gAbyaeTowp9rs
We agree that models are only better or worse for a purpose, but ...

> Ask whether this creature needs air. Ask how fast it swims. etc.

If there are systematic correlations between _many_ particular creature-features like whether it needs air, how fast it swims, what it's shaped like, what its genome is, _&c._, then it's adaptive to have a [short code](https://www.lesswrong.com/posts/soQX8yXLbKy7cFvy8/entropy-and-short-codes) for the conjunction of those _many_ features that such creatures [have in common](https://www.lesswrong.com/posts/yLcuygFfMfrfK8KjF/mutual-information-and-density-in-thingspace).

Category isn't identity, but the cognitive algorithm that makes people _think_ category is identity actually performs pretty well when things are tightly-clustered in configuration space rather than evenly distributed, which actually seems to be the case for a lot of things! (_E.g._, while there are (or were) transitional forms between species related by evolutionary descent, it makes sense that we have separate words for cats and dogs rather than talking about individual creature properties of ear-shape, _&c._, because there aren't any half-cats in our real world.)

#### [>>] Dagon · 2 karma · 2019-04-15 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=Kdp8eAKYuYg8MmHRD
Sure, casual use of categories is convenient and pretty good for a lot of purposes. For unimportant cases (including cases where the exceptions don't come into play, like sailors calling dolphin "fish"), go for it. Use whatever words minimize the cognitive load on your conversational partners and allow them to best navigate the world they're in.

Where precision matters, though, you're better off using more words. Don't try to cram so much inferential power into a categorization that's not a good fit for the domain of predictions you're making.

And because these are different needs, be aware that different weights and rigor will be applied. If someone is casually using a category "wrong", you have to decide if the exceptions matter enough to point them out (that is, use more words to get more precision), or if they're just optimizing for brevity on a different set of dimensions than you prefer. Worse, they (and you!) may not fully know what dimensions are important, so your compression may be more wrong than the one you're trying to improve.

#### [>>>] Zack_M_Davis [AUTHOR] · 7 karma · 2019-04-18 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=nnCtCijLmCJhJovP5
> Sure, casual use of categories is convenient and pretty good for a lot of purposes. [...] Where precision matters, though, you're better off using more words. Don't try to cram so much inferential power into a categorization that's not a good fit for the domain of predictions you're making.

So, I actually don't think "casual" _vs._ "precise" is a good characterization of the distinction I was trying to make in the grandparent! I'm saying that for "sparse", tightly-clustered distributions in high-dimensional spaces, something like "essentialism" is actually doing really useful cognitive work, and using more words to describe more basic, lower-level ("precise"?) features doesn't actually get you better performance—it's not just about minimizing cognitive load.

A good example might be the recognition of accents. Which description is more useful, both for your own thinking, and for communicating your observations to others—

 * "She has a British accent"; or
 * ["She only pronounces the phoneme /r/ when it is immediately followed by a vowel, and her speech has three different open back vowels, and ..."](https://en.wikipedia.org/wiki/Comparison_of_General_American_and_Received_Pronunciation)?

At the level of consciousness, it's much easier to correctly recognize accents than to characterize and articulate all the individual phoneme-level features that your brain is picking up on to make the categorization. Categories let you make inferences about hidden variables that you haven't yet observed in a particular case, but which are known to correlate with features that you have observed. Once you hear the [non-rhoticity](https://en.wikipedia.org/wiki/Rhoticity_in_English) in someone's speech, your brain also knows how to anticipate how they'll pronounce vowels that they haven't yet said—and where the person grew up! I think this is a pretty impressive AI capability that shouldn't be dismissed as "casual"!

#### [>>>>] Dagon · 2 karma · 2019-04-18 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=aeytzBFZa8Szcosb9
Accents are a good example. It's easy to offend someone or to make incorrect predictions based on "has a British accent", when you really only know some patterns of pronunciation. In some contexts, that's a fine compression; way easier to process, communicate and remember. In other contexts, you're better off highlighting and acknowledging that your data supports many interpretations, and you should be preserve that uncertainty in your communication and predictions.

"casual" vs "precise" are themselves lossy compression of fuzzy concepts, and what I really mean is that the use of compression is valid and helpful sometimes, and harmful and misleading at other times. My point is that the distinction is \_NOT\_ primarily about how tight the cluster or how close the match to some dimensions of reality in the abstract. The acceptability of the compression is about context and uses for the compressed or less-compressed information, and whether the lost details are important for the purpose of the communication or prediction. It's whether it meets the needs of the model, not how close it is to "reality".

Note also that I recognize that no model and no communication is actually full-fidelity. Everything any agent knows is compressed and simplified from reality. The question is how much further compression is valuable for what purposes.

Essentialism is wrong. Conceptual compression and simplified modeling is always necessary, and sometimes even an extreme compaction is good enough for a purpose.

#### [-] ChristianKl · 1 karma · 2019-04-17 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=d63iwa9Nf6FLB4Gjm
> There is an *important difference* between "identifying this pill as not being 'poison' allows me to [focus my uncertainty](https://www.lesswrong.com/posts/GJ4ZQm7crTzTM6xDW/focus-your-uncertainty) about what I'll observe after administering the pill to a human (even if [most possible minds](https://www.lesswrong.com/posts/tnWRXkcDi5Tw9rzXw/the-design-space-of-minds-in-general) have never seen a 'human' and would never waste cycles imagining administering the pill to one)" and "identifying this pill as not being 'poison', because if I publicly called it 'poison', then the manufacturer of the pill might sue me."

What is that sentence supposed to tell me? It's not clear whether or not that important difference is supposed to imply to the reader that one is better then the other. Given that there seems to be a clear value judgement in the others, maybe it does here?

Reading it leaves me as a reader with constructed an example where you might be pointing.

You might run standard tox tests and your mice are dead. Mice differ from humans, so you might want to not use the term poison in contrast to the general way people think about tox testing, because you don't care about mice? Is a general critique of the way we do tox testing intended or not?

The part about most possible minds never having seen a human feels like a disgression to me, made with words that are unnecessarily obscure (most people in society won't understand what wasting cycles is about) when it would be quite easy to say that you care about human more then mice.

Is the claim that it's bad to use words in a way to conform to the standards of a powerful institution that enforces certain expectations of what people can expect when they hear a certain word? Boo Brussels? Boo journals who refuse to publish papers that use words when community standards of when certain words should be used aren't meet?

To those people who proofread and appeartly didn't find an issue in that sentence, is it really necessary to mix all those different issues into a 6-line sentence?

#### [>] habryka · 13 karma · 2019-04-18 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=nKPzn95ARJrPMYjJk
I do find myself somewhat confused about the hostility in this comment. It's hard to write good things, and there will always be misunderstandings. Many posts on LessWrong are unnecessarily confusing, including many posts by Eliezer, usually just because it takes a lot of effort, time and skill to polish a post to the point where it's completely clear to everyone on the site (and in many technical subjects achieving that bar is often impossible).

Recommendations for how to phrase things in a clear way seem good to me, and I appreciate them on my writing, but doing so in a way that implies some kind of major moral failing seems like it makes people overall less likely to post, and also overall less likely to react positively to feedback.

#### [>>] ChristianKl · 5 karma · 2019-04-18 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=FJDiWTLXXX5y6G5cZ
You seem to pose a model where a post is either saying good things or saying things uncleanly in a way that's easily misunderstood. A model whereby it's not important to analyses which claims happen to be made which are wrong.

My first answer was pointing out statements in the post that I consider to be clearly wrong and important (it's something many people believed that holds back intellectual progress in the topic). The response seemed to be along the lines of:

*"I didn't mean to imply that what I claimed to be true (" Similarly, the primary thing when you take a word in your lips is your intention to reflect the territory, whatever the means"), I said that because it seems to send the right tribal signals because it looks similar to what EY wrote.*

*Besides the people in my tribe that I showed my draft liked it."*

Defending the post as being tribally right instead of either allowing claims to be falsified or defending the claims on their merits feels to me like a violation of debate norms that raises emotional hostility.

I feel that it's bad to by default assume that any disagreement is due to misunderstandings and not substance.

I do think that emotion is justified in the sense that if we get a lot of articles that are full of tribal signaling and attempts to look like EY posts but endorse misconceptions, that would be problematic to LW in a way that posts that are simply low quality because writing good is hard wouldn't be (and that wouldn't trigger emotions).

#### [>>>] habryka · 11 karma · 2019-04-18 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=iXroKR48h4qGKrBb6
After rereading the post a few times, I think you are just misunderstanding it?

Like, I can't make sense of your top-level comment in my current interpretation of the post, and as such I interpreted your comment as asking for clarification in a weirdly hostile tone (which was supported by your first sentence being "What is that sentence supposed to tell me?"). I generally think it's a bad idea to start substantive criticisms of a post with a rhetorical question that's hard to distinguish from a genuine question (and probably would advise against rhetorical questions in general, but am less confident of that).

To me the section you quoted seems relatively clear, and makes a pretty straightforwardly true point, and from my current vantage point I fail to understand your criticism of it. I would be happy to try to explain my current interpretation, but would need a bit more help understanding what your current perspective is.

#### [>>>>] ChristianKl · 5 karma · 2019-04-19 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=HAZm3gamb3eoEGnvR
I have written multiple post in this thread and I wouldn't expect you to make sense of the tone by treating this post in isolation.

In a way it's true straightforwardly true point to say that apples are significantly different from tomatoes. It's defensibly true in a certain sense.

At the same time if a reader wants to learn something from the statement and transfer the knowledge to another case, they need to model of what kind of significant difference is implied.

You might read the statement as being about how tomatoes are vegetables purposes for tariff or for cooking purposes and how scientific taxonomy isn't the only taxonomy that matters but it's very bailey-and-motte about that issue. The bailey-and-motteness then makes it hard to falsify the claims.

#### [>>>>>] Raemon · 1 karma · 2019-04-19 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=hjCaZJn6jPGreNpQb
Are you saying people should never casually make such claims about apples and tomatoes? I haven’t tried to parse your comments in detail, apologies if I'm misunderstanding. But they seem to be implying a huge amount of friction on conversation that does not seem practical to me. (i.e. only discuss things if you're going to take the time to clarify details of your model. The reasons we have clusters and words and shorthand is because that's a lot of effort that most of the time isn't worth it)

#### [>>>>>>] ChristianKl · 2 karma · 2019-04-20 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=z7NnXzZsscKbTYeHi
A model should generally be clear enough to be falsifiable. It might be okay for a paragraph to not expand an idea in enough detail for that but when there's a >3800 word essay about a model that avoids being falsifiable and instead is full with applause lights I do consider that bad.

#### [>] Zack_M_Davis [AUTHOR] · 17 karma · 2019-04-21 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=8qH2vzeik988hsjbF
> It's not clear whether or not that important difference is supposed to imply to the reader that one is better then the other. Given that there seems to be a clear value judgement in the others, maybe it does here?

All three paragraphs starting with "There's an _important difference_ [...]" are trying to illustrate the distinction between choosing a model because it reflects value-relevant parts of reality (which I think is good), and choosing a model because of some non-reality-mapping consequences of the choice of model (which I think is generally bad).

> words that are unnecessarily obscure (most people in society won't understand what wasting cycles is about)

The primary audience of this post is longtime _Less Wrong_ readers; as an author, I'm not concerned with trying to reach "most people in society" with this post. I expect _Less Wrong_ readers to have trained up [generalization](https://en.wikipedia.org/wiki/Generalization) instincts motivating the leap to thinking about AIs or minds-in-general even though this would seem weird or incomprehensible to the general public.

> To those people who proofread and appeartly didn't find an issue in that sentence, is it really necessary to mix all those different issues into a 6-line sentence?

It's true that I tend to have a "dense" writing style (with lots of nested parentheticals and subordinate clauses), and that I should probably work on writing more simply in order to be easier to read. Sorry.

#### [-] Raemon · 18 karma · 2019-04-18 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=WcvzjL4hAbqw2jKY9
> When rationalists say that definitions can be wrong, we don't mean that there's a *unique* category boundary that is the True floating essence of a word, and that all other possible boundaries are wrong. We mean that in order for a proposed category boundary to *not* be wrong, it needs to capture some statistical structure in reality, even if [reality is surprisingly detailed](http://johnsalvatier.org/blog/2017/reality-has-a-surprising-amount-of-detail) and there can be *more than one* such structure.

So, I got this part. And it seemed straightforwardly true to me, and seemed like a reasonably short inferential step away from other stuff LW has talked about. Categories are useful as mental compressions. Mental compressions should map to *something.* There are multiple ways you might want to cluster and map things. So far so straightforward.

And then the rest of the article left me more confused, and the disagreements in the comments got me even more confused.

Is the above claim the core claim of the article? If so, I'm confused what other people are objecting to. If not, I'm apparently still confused about the point of the article.

\[edit: fwiw, I am aware of the subtext/discussion that the post is an abstraction of, and even taking that into account still feel fairly confused about some of the responses\]

#### [-] Said Achmiz · 44 karma · 2019-04-21 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=T49M7fyizPhrLZMnL
This is an excellent post. It has that rare quality, like much of the Sequences, of the ideas it describes being utterly obvious—in retrospect. (I also appreciate the similarly Sequence-like density of hyperlinks, exploiting the not-nearly-exploited-enough-these-days power of hypertext to increase density of ideas without a concomitant increase in abstruseness.)

… which is why I find it so puzzling to see all these disagreeing comments, which seem to me to contain an unusual, and puzzling, level of reflexive contrarianness and pedanticism.

#### [>] romeostevensit · 0 karma · 2019-04-22 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=uu3DNjstfR84QLGtQ
I think my sense of miscommunication with you is that you don't seem to have a sense of the law of equal and opposite advice + meta-contrarianism. Different things seem useful at different stages, and principle of charity means at least trying to see why what people are saying might be useful from their perspective.

#### [>>] Said Achmiz · 2 karma · 2019-04-22 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=ysXb3t4BZeCkiFikG
Er, sorry, did you mean to post this as a reply here? I’m not quite seeing the relevance…

#### [>] Zack_M_Davis [AUTHOR] · 10 karma · 2020-12-06 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=GBiZnFYKz3HSTyskm
Excellent enough to be worthy of your nomination for the [2019 Review](https://www.lesswrong.com/posts/QFBEjjAvT6KbaA3dY/the-lesswrong-2019-review), perhaps??

#### [>>] Said Achmiz · 10 karma · 2020-12-06 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=aavhiqGdshMyh9fA6
Oh yeah, totally. I guess that’s going on now, then? I will try and figure out how one nominates things…

#### [-] Said Achmiz · 12 karma · 2020-12-07 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=ebSxGtpFiYJNsq8SK
[My earlier comment](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries#T49M7fyizPhrLZMnL) explains why I think this post is one of last year’s best. (My opinion of its quality remains unchanged, after ~1.5 years.)

#### [-] Zack_M_Davis [AUTHOR] · 11 karma · 2020-12-10 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=i79Ju9vQJiEgRiJDj
Is anyone interested in giving this a second nomination?

I argue that this post is significant for filling in a gap in our canon: in ["Where to Draw the Boundary?"](https://www.lesswrong.com/posts/d5NyJ2Lf6N22AD9PB/where-to-draw-the-boundary) (note, "boundary", singular), Yudkowsky contemptuously dismisses the idea that dolphins could be considered fish. However, [Scott Alexander has argued that it may very well make sense to consider dolphins fish](https://slatestarcodex.com/2014/11/21/the-categories-were-made-for-man-not-man-for-the-categories/). So ... which is it? Is Yudkowsky right that categories must "carve reality at the joints", or is Alexander right that "[a]n alternative categorization system is not an error, and borders are not objectively true or false"?

In this post, "Where to Draw the Boundaries?" (note, boundaries, plural), I argue that Yudkowsky is right that categories _must_ carve reality at the joints; however, I reconcile this with Alexander's case that dolphins could be fish with a simple linear-algebraic intuition: entities might cluster in a smaller _subspace_ of configuration space, while failing to cluster in a larger subspace. Clusters in particularly "thin" subspaces (like a fake job title that nevertheless makes predictions on the "what's printed on business cards" dimension) may fail to be useful.

(Perhaps also of significance is that the job title example from this post [ended up inspiring the local work on simularcum levels](https://www.lesswrong.com/posts/8XDZjfThxDxLvKWiM/excerpts-from-a-larger-discussion-about-simulacra).)

If people are wary of the political context in which this was written, I [put up a non-Frontpage containment thread](https://www.lesswrong.com/posts/5aqumaym7Jd2qhDcy/containment-thread-on-the-motivation-and-political-context) in case anyone wants to complain or ask questions there.

#### [>] Raemon · 4 karma · 2020-12-10 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=kj8rDERqacsiKrP8y
I'm expecting to probably nominate this, but first want to re-read both the post and it's predecessors and think about it a bit. 

(My recollection is that I wasn't bothered by the political context, but feel like the post is a bit confusingly structured and I would probably recommend a significant rewrite to make it's point more clear and more clearly motivated. It takes a long time before the post gets to a point where I understand why I might care about any of this. I think the fake-job-titles is actually a pretty good example without being especially controversial, which should maybe be more front-and-center?)

#### [>>] Zack_M_Davis [AUTHOR] · 4 karma · 2020-12-11 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=98JRTp4F2MboukhvR
I'm hoping the sequel (forthcoming later this month) will be a lot clearer!

#### [-] TAG · 3 karma · 2020-12-10 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=nN4AkvMW5pZJtwojk
> But in order for your map to be useful in the service of your values, it needs to reflect the statistical structure of things in the territory—which depends on the territory, not your values.

In order for your map to be useful , it needs to reflect the statistical structure of things to the extent required by the value it is in service to.

That can be zero. There is a meta category of things that are  created by humans without any footprint in pre existing reality. These include money, marriages, and mortgages 

Since useful categories can have no connection to ore existing reality , they can also have low connection. Which means there is no generic argument against a category for not reflecting reality enough, only for not reflecting reality enough for its purpose.

It is still possible to criticise scienticific categories, since they are supposed to reflect reality

#### [>] Zack_M_Davis [AUTHOR] · 9 karma · 2020-12-11 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=aFwWP53eQYXNM9mp3
Thanks for commenting! I think I disagree with your analysis of socially-constructed concepts such as money, marriages, and mortgages. It's true that these things only exist in the context of Society, but given a Society that already exists, an observer is going to want to use the _same_ rules to describe things happening inside that Society, as they would for "scientific" subjects. No [separate magesteria](https://en.wikipedia.org/wiki/Non-overlapping_magisteria)!

Take money: ["any item or verifiable record that is generally accepted as payment for goods and services"](https://en.wikipedia.org/wiki/Money). If I'm observing a foreign Society from behind a Cartesian veil, this "money" concept is useful for making predictions about and [compressing my observations of](https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length) trade interactions in that Society. For example, if I'm just watching the people trade items, but I don't yet know which (if any) of the items are "money", then when I hypothesize that a particular kind of item—say, those small metal disks with an image of a person's face stamped on them—is "money", then I predict that the metal disks will usually be offered on exactly one side of most transactions.

I do think there are a few ways that socially-constructed categories behave differently from others. I'm not sure I understand exactly how this works yet, but I wrote about my current ideas in ["Schelling Categories, and Simple Membership Tests"](https://www.lesswrong.com/posts/edEXi4SpkXfvaX42j/schelling-categories-and-simple-membership-tests), and [an answer to to Swentworth's call for abstraction problems](https://www.lesswrong.com/posts/XArPqdkwCtEekgYxv/problems-involving-abstraction?commentId=qaPhpHjd7fj4hHaCN).

#### [>>] TAG · 1 karma · 2020-12-11 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=CaJSFqwhg7wPQJATg
>an observer is going to want to use the same rules to describe things happening inside that Society, as they would for “scientific” subjects. No separate magesteria!

They would be wrong to do so, because different rules apply. For instance, you can't change the speed of light, but you can revalue your currency .

>No separate magesteria!

That doesn't give me any reason to reject separate magisteria.


>If I’m observing a foreign Society from behind a Cartesian veil, this “money” concept is useful for making predictions about and compressing my observations of trade interactions in that Society. For example, if I’m just watching the people

But it remains a fundamental fact that the society you are observing can change their money. What you are demonstrating is that constructs can be treated as pre-existing things in  a special case ... but they are still different in the general case.

>I do think there are a few ways that socially-constructed categories behave differently from others

Great. So the rest of the argument follows: the existence of social constructs means that there is more to usefulness than correspondence to reality.

#### [>>>] Zack_M_Davis [AUTHOR] · 3 karma · 2020-12-12 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=5fh3MMfoLWtfLRN9j
> Great. So the rest of the argument follows

Did you read the links in the paragraph you're responding to? Again, that's ["Schelling Categories, and Simple Membership Tests"](https://www.lesswrong.com/posts/edEXi4SpkXfvaX42j/schelling-categories-and-simple-membership-tests), and [an answer to "Problems Involving Abstraction"](https://www.lesswrong.com/posts/XArPqdkwCtEekgYxv/problems-involving-abstraction?commentId=qaPhpHjd7fj4hHaCN), which together total to about 2600 words.

If you did read it, and you still disagree, than I'm very eager to write more to clarify my position! But I think I'll be able to do a better job of it if I get more specific feedback about what's wrong with the 2600 words I already wrote.

#### [>>>>] TAG · 1 karma · 2020-12-12 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=mrjRCMSYhyk4eh7na
>My work-in-progress take: an agent outside Society observing from behind a Cartesian veil, who only needs to predict, but never to intervene, can treat socially-constructed concepts the same as any other: “Christmas” is just a pattern of behavior in some humans, just like “trees” are a pattern of organic matter. 

But that isn't relevant to what you are saying, because you are making a normative point: you are saying some concepts are wrong.


> What makes social construction special is that it’s a case where a “map” is exerting control over the “territory”: whether I’m considered an “adult” isn’t just putting a semi-arbitrary line on the spectrum of how humans differ by age (although it’s also that); which Schelling point the line settles on is used as an input into decisions—therefore, predictions that depend on those decisions also need to consider the line, a self-fulfilling prophecy. Alarmingly, this can give agents an incentive to fight over shared maps!

You're one of them. 

The argument against your point is that scientifically inaccurate maps can have, other, compensatory, kinds of usefulness. You haven't refuted that.

#### [>>>>>] abramdemski · 5 karma · 2020-12-13 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=WXZXdYZdMJyQjGwcn
It seems, perhaps, that your main point is that usefulness can come apart from correspondence:

> Great. So the rest of the argument follows: the existence of social constructs means that there is more to usefulness than correspondence to reality.

> The argument against your point is that scientifically inaccurate maps can have, other, compensatory, kinds of usefulness. You haven't refuted that.

I don't believe that Zack disagreed with this? Indeed, Zack mentions several examples where the two come apart:

> There is an *important difference* between "not including mountains on a map because it's a political map that doesn't show any mountains" and "not including Mt. Everest on a geographic map, because my sister died trying to climb Everest and seeing it on the map would make me feel sad."
> 
> There is an *important difference* between "identifying this pill as not being 'poison' allows me to [focus my uncertainty](https://www.lesswrong.com/posts/GJ4ZQm7crTzTM6xDW/focus-your-uncertainty) about what I'll observe after administering the pill to a human (even if [most possible minds](https://www.lesswrong.com/posts/tnWRXkcDi5Tw9rzXw/the-design-space-of-minds-in-general) have never seen a 'human' and would never waste cycles imagining administering the pill to one)" and "identifying this pill as not being 'poison', because if I publicly called it 'poison', then the manufacturer of the pill might sue me."

These are both examples where "useful" is importantly different from "corresponds to reality".

#### [>>>>>>] TAG · 2 karma · 2020-12-13 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=ZQb9mu98mR3eaKo89
> I don’t believe that Zack disagreed with this

He's disagreeing with someone over something. In think my point is the same as Scott's, and he seems to be responding to Scott.

Edit:

If you read back, I'm responding to the point that:
"...in order for your map to be useful in the service of your values, it needs to reflect the statistical structure of things in the territory—which depends on the territory, not your values."

That's a pretty clear rejection of useful-but-not-corresponding even if there are examples of  useful-but-not-corresponding  further down. 

>These are both examples where “useful” is importantly different from “corresponds to reality”.

Yes, but they are examples with negative connotations.

#### [>>>>>>>] abramdemski · 3 karma · 2020-12-13 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=3Fad9QeD2cCLgR22j
> If you read back, I'm responding to the point that: "...in order for your map to be useful in the service of your values, it needs to reflect the statistical structure of things in the territory—which depends on the territory, not your values."

That's fair.

> Yes, but they are examples with negative connotations.

I also *agree* with the negative connotations. There's something special, worth defending, about epistemics focusing only on reflecting the territory, screening off other considerations as much as possible.

#### [>>>>>>>>] TAG · -2 karma · 2020-12-13 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=dsLmrtbcTHtBj9XmB
> There’s something special, worth defending, about epistemics focusing only on reflecting the territory, screening off other considerations as much as possible.

That's quite a vague claim. Are you saying that realistic epistemology is special in some sense that it should be applied to everything, or that everything should be reduced to it?

#### [>>>>>>>>>] abramdemski · 11 karma · 2020-12-14 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=iSdCo7xnijW2qQdvg
I'm saying that epistemics focused on usefulness-to-predicting is *broadly* useful in a way that epistemics optimized in other ways is not. It is more *trustworthy* in that the extent to which it's optimized for some people at the expense of other people must be very limited. (Of course it will still be more useful to some people than others, but the Schelling-point-nature means that we tend to take it as the gold standard against which other things are judged as "manipulative".)

Another defense of this Schelling point is that *as we depart from it*, it becomes increasingly difficult to objectively judge whether we are benefiting or hurting as a result. We get a web of [contagious lies](https://www.lesswrong.com/posts/wyyfFfaRar2jEdeQK/entangled-truths-contagious-lies) spreading through our epistemology.

I'm *not* saying this is a Schelling fence which has held firm through the ages, by any means; indeed, it is rarely held firm. But, speaking very roughly and broadly, this is a fight between "scientists" and "politicians" (or, as Benquo has put it, between [engineers and diplomats](https://www.lesswrong.com/posts/m7v3vtbRv82mQP5uo/the-engineer-and-the-diplomat)).

#### [>>>>>>>>>>] TAG · 0 karma · 2020-12-19 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=gmBGtfaPA744k7Cty
>I’m saying that epistemics focused on usefulness-to-predicting is broadly useful in a way that epistemics optimized in other ways is not

That's still not very clear. As opposed to other epistemics being useless, or as opposed to other epistemics having specialized usefulness?

>It is more trustworthy in that the extent to which it’s optimized for some people at the expense of other people must be very limited.

Why assume it's necessarily conflictual and zero sum? For one thing, there's a lot of social constructs and unscientific semantics out there.

>the gold standard against which other things are judged as “manipulative”.)

Why assume anything unscientific is manipulative?

>We get a web of contagious lies spreading through our epistemology.

If you are going to use a contagion metaphor, why not use an immune system metaphor? Which would be a metaphor for critical thinking.

>Another defense of this Schelling point is that as we depart from it

We were never there!

ETA: I don't buy that a unscientific concept is necessarily a lie, but even so, if lies are contagious, and no process deletes them, then we should already be in a sea of lies.

>But, speaking very roughly and broadly, this is a fight between “scientists” and “politicians” (or, as Benquo has put it, between engineers and diplomats).

Why? Science and politics do not have to fight over the same territory.

#### [>>>>>>>>>>>] abramdemski · 3 karma · 2020-12-20 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=bhFomrXKRm2sfjHR6
> >I’m saying that epistemics focused on usefulness-to-predicting is broadly useful in a way that epistemics optimized in other ways is not  
>   
> That's still not very clear. As opposed to other epistemics being useless, or as opposed to other epistemics having specialized usefulness?

What I meant by "broadly useful" is, having usefulness in many situations and for many people, rather than having usefulness in one specific situation or for one specific person.

For example, it's often more useful to have friends who optimize their epistemics mostly based on usefulness-for-predicting, because those beliefs are more likely to be useful to you as well, rather than just them.

In contrast, if you have friends who optimize their beliefs based on a lot of other things, then you will have to do more work to figure out whether those beliefs are useful to you as well. Simply put, their beliefs will be less trustworthy.

Scaling up from "friends" to "society", this effect gets much more pronounced, so that in the public sphere we *really* have to ask who benefits from claims/beliefs, and uncontaminated beliefs are *much more* valuable (so truly unbiased science and journalism are quite valuable as a social good).

Similarly, we can go to the smaller scale of one person communicating with themselves over time. If you optimize your beliefs based on a lot of things other than usefulness-for-predicting, the usefulness of your beliefs will have a tendency to be very situation-specific, so your may have to rethink things a lot more when situations change, compared with someone who left their beliefs unclouded.

> Why assume it's necessarily conflictual and zero sum? For one thing, there's a lot of social constructs and unscientific semantics out there.

Because when it is not, then beliefs optimized for predictive value only are optimal. If several agents have sufficiently similar goals such that their only focus is on achieving common goals, then the most predictively accurate beliefs are also going to be the highest utility.

For example, if there is a high social incentive in a community to believe in some specific deity, it could be because there is low trust that people without that belief would act cooperatively. This in turn is because people are assumed to have selfish (IE non-shared) goals. Belief in the deity aligns goals because the deity is said to punish selfish behavior. So, given the belief, everyone can act cooperatively.

> Why assume anything unscientific is manipulative?

I'll grant you one caveat: self-fulfilling prophecies. In situations where those are possible, there are several equally predictively accurate beliefs with different utilities, and we should choose the "best" according to our full preferences.

It's a pretty large concession, since it includes all sorts of traditions and norms.

Aside from that, though, optimizing for something else that predictive value is *very probably* manipulative for the reason I stated above: if you're optimizing for something else, it suggests you're not working in a team with shared goals, since assuming shared goals, the best collective beliefs are the most predictive.

> ETA: I don't buy that a unscientific concept is necessarily a lie, but even so, if lies are contagious, and no process deletes them, then we should already be in a sea of lies.

I think this part is just a misunderstanding. The post I linked to argues that lies are contagious not in the sense that they spread, but rather, in the sense that in order to justify one lie, you often have to make more lies, so that the lie spreads throughout your web of beliefs. Ultimately, under scrutiny, you would have to lie (eg to yourself) about epistemology itself, since you would need to justify where you got these beliefs from (so for example, Christian scholars will tend to disagree with Bayesians about what constitutes justification for a belief).

> Why? Science and politics do not have to fight over the same territory.

I think this has to do with our [other disagreement](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=GB8p2uYknJumezu3m), so I'll just say that in an ordinary conversation (which I think normally has some mix between "engineer culture" and "diplomat culture"), I personally think there is ***a lot*** of overlap in the territory those two modes might be concerned with.

#### [>>>>>>>>>>>>] TAG · 1 karma · 2020-12-27 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=ecA2zQAbvGFMTgyWT
[empty or deleted comment]

#### [>>>>>>>>>>>>] TAG · 0 karma · 2020-12-27 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=giMgdewHTxEhSyeth
>What I meant by “broadly useful” is, having usefulness in many situations and for many people, rather than having usefulness in one specific situation or for one specific person.

That still didn't tell me whether specialised purposes are  non existent , ineffective, or morally wrong.


>For example, it’s often more useful to have friends who optimize their epistemics mostly based on usefulness-for-predicting, because those beliefs are more likely to be useful to you as well, rather than just them.

So..ineffective?

What you are saying would be true if people chose friends and projects at random. And if you can only use one toolkit for everything. Neither assumption is realistic. People gather over common interests, and common interests lead to specialised vocabulary. That's as true of rationalism as anything else. 

>In contrast, if you have friends who optimize their beliefs based on a lot of other things, then you will have to do more work to figure out whether those beliefs are useful to you as well.

Assuming friends are as randomly distributed as strangers.

>Scaling up from “friends” to “society”, this effect gets much more pronounced, so that in the public sphere we really have to ask who benefits from claims/beliefs, and uncontaminated beliefs are much more valuable (so truly unbiased science and journalism are quite valuable as a social good).

Yes, but it's been that way forever. It's not like something recently  happened to kick us out if the garden if Eden, and it's not like we never developed any ways of coping.

>Similarly, we can go to the smaller scale of one person communicating with themselves over time. If you optimize your beliefs based on a lot of things other than usefulness-for-predicting, the usefulness of your beliefs will have a tendency to be very situation-specific, so your may have to rethink things a lot more when situations change, compared with someone who left their beliefs unclouded.

And if you use generic concepts for everything  you lose the advantages of specialised ones.


Why assume it’s necessarily conflictual and zero sum? For one thing, there’s a lot of social constructs and unscientific semantics out there.

>Because when it is not, then beliefs optimized for predictive value only are optimal. If several agents have sufficiently similar goals such that their only focus is on achieving common goals, then the most predictively accurate beliefs are also going to be the highest utility.

Assuming that everything is prediction. If several agents have sufficiently similar goals such that their only focus is on achieving common goals,the most optimal concepts will be ones that are specialised for achieving the goal. 


For examplee, in cookery school, you will be taught the scientific untruth that tomatoes are vegetables. The manipulates them into into putting them into savoury dishes instead of deserts. This is more efficient than discovering by trial and error what to do with them.


>For example, if there is a high social incentive in a community to believe in some specific deity, it could be because there is low trust that people without that belief would act cooperatively. This in turn is because people are assumed to have selfish (IE non-shared) goals. Belief in the deity aligns goals because the deity is said to punish selfish behavior. So, given the belief, everyone can act cooperatively.

There isn't just one kind of unscientific concept. Shared myths can iron out differences in goals, as in your example, or they can optimise the achievement of shared goals, as in mine.

>I’ll grant you one caveat: self-fulfilling prophecies. In situations where those are possible, there are several equally predictively accurate beliefs with different utilities, and we should choose the “best” according to our full preferences.

Assuming, wrongly, that everything is prediction.


>Aside from that, though, optimizing for something else that predictive value is very probably manipulative for the reason I stated above:

So...evil?

Low level manipulation is ubiquitous. You need to argue for "manipulative in an egregiously bad way" separately

>if you’re optimizing for something else, it suggests you’re not working in a team with shared goals, since assuming shared goals, the best collective beliefs are the most predictive.

No, see above.

#### [>>>>>>>>>>>>>] abramdemski · 3 karma · 2020-12-28 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=86yhzs75eftWD8u9i
> What you are saying would be true if people chose friends and projects at random. And if you can only use one toolkit for everything. Neither assumption is realistic. People gather over common interests, and common interests lead to specialised vocabulary. That's as true of rationalism as anything else.  
>   
> >In contrast, if you have friends who optimize their beliefs based on a lot of other things, then you will have to do more work to figure out whether those beliefs are useful to you as well.  
>   
> Assuming friends are as randomly distributed as strangers.

I agree that in practice, people choose friends who share memes (in particular, these "optimized for reasons other than pure accuracy" memes) -- both in that they will select friends on the basis of shared memes, and in that other ways of selecting friends will often result in selecting those who share memes.

But remember my point about agents with fully shared goals. Then, memes optimized to predict what they mutually care about *will be* optimal for them to use.

So if your friends are using concepts which are optimized for other things, then either (1) you've got differing goals and you now would do well to sort out which of their concepts have been gerrymandered, (2) they've inherited gerrymandered concepts from *someone else* with different goals, or (3) your friends and you are all cooperating to gerrymander *someone else's concepts* (or, (4), someone is making a mistake somewhere and gerrymandering concepts unnecessarily).

I'm not saying that any of these are fundamentally ineffective, untenable, or even morally reprehensible (though I do think of 1-3 as a bit morally reprehensible, it's not really the position I want to defend here). I'm just saying there's something special about avoiding these things, whenever possible, which has good reason to be attractive to a math/science/rationalist flavored person -- because if you care deeply about clear thinking, and don't want the overhead of optimizing your memes for political ends (or de-optimizing memes from friends from those ends), this is the way to do it. So for that sort of person, fighting against gerrymandered concepts is a very reasonable policy decision, and those who have made that choice will find allies with each other. They will naturally prefer to have their own discussions in their own places.

I do, of course, think that the LessWrong community should be and to an extent is such a place.

> >>Why assume it’s necessarily conflictual and zero sum?
> 
> >Because when it is not, then beliefs optimized for predictive value only are optimal. If several agents have sufficiently similar goals such that their only focus is on achieving common goals, then the most predictively accurate beliefs are also going to be the highest utility.
> 
> Assuming that everything is prediction. If several agents have sufficiently similar goals such that their only focus is on achieving common goals,the most optimal concepts will be ones that are specialised for achieving the goal.
> 
> For examplee, in cookery school, you will be taught the scientific untruth that tomatoes are vegetables. The manipulates them into into putting them into savoury dishes instead of deserts. This is more efficient than discovering by trial and error what to do with them.

This point was dealt with in the OP. This is why Zack refers to optimizing for prediction *of things we care about*. Zack is ruling in things like classifying tomatoes as vegetables for culinary purposes, and fruits for biological purposes.$^1$ A cook cares about whether something goes well with savory dishes, whereas a biologist cares about properties relating to the functioning and development of an organism, and its evolutionary relationships with other organisms. So each will use concepts optimized for predicting those things.

So why sanction this sort of goal-dependence, while leaving other sorts of goal-dependence unsanctioned? Can't I apply the same arguments I made previously, about this creating a lot of friction when people with different goals try to use each other's concepts?

I think it *does* create a lot of friction, but the cost of *not* doing this is simply too high. To live in this universe, humans have to focus on predicting things which are useful to them. Our intellect is not so vast that we can predict things in a completely unbiased way and still have the capacity to, say, cook a meal.

Furthermore, although this does create some friction between agents with different goals, what it *doesn't* do (which conceptual gerrymandering *does* do) is cloud your judgement when you are doing your best to figure things out on your own. By definition, your concepts are optimized to help you predict things you care about, ie, think as clearly as possible. Whereas if your concepts are optimized for other goals, then you must be *sacrificing* some of your ability to predict things you care about, *in order to* achieve other things. Yes, it might be worth it, but it must be recognized as a sacrifice. And it's natural for some people to be unwilling to make that sort of sacrifice.

I imagine that, perhaps, you aren't fully internalizing this cost because you are imagining *using gerrymandered concepts in conversation* while internally thinking in clear concepts. But I see the argument as about how to think, not how to talk (although both are important). If you use a gerrymandered concept, you may have no understanding of the non-gerrymandered versions; or you may have some understanding, but in any case not the fluency to think in them. Otherwise you'd risk not achieving your purpose, like a Christian who shows too much fluency in the atheist ontology, thus losing credibility as a Christian. (If they think in the atheist ontology and only speak in the Christian one, that just makes them a liar, which is a different matter.)

> There isn't just one kind of unscientific concept. Shared myths can iron out differences in goals, as in your example, or they can optimise the achievement of shared goals, as in mine.

To summarize, I continue to assume a somewhat adversarial scenario (not necessarily zero sum!) because I see Zack as (correctly) ruling in mere *optimization of concepts to predict the things we care about*, but ruling out other forms of optimization of concepts to be useful. I believe that this rules in all the non-adversarial examples which you would point at, leaving only the cases where something adversarial is going on.

> Low level manipulation is ubiquitous. You need to argue for "manipulative in an egregiously bad way" separately

I'm arguing that Zack's definition is a very good Schelling fence to put up.

One of Zack's recurring arguments is that *appeal to consequences is an invalid argument* when considering where to draw conceptual boundaries. "We can't define Vargaths as anyone who supports Varg, because the President would be a Vargath by that definition, which she would find offensive; and we don't want to offend the president!" would be, by Zack's lights, transparent conceptual gerrymandering and an invalid argument. 

Zack's argument is not itself conceptual gerrymandering because this argument is being made *on epistemic grounds*, IE, pointing out that accepting "appeals to consequences" arguments reduces your ability to predict things you care about.

My argument in support of Zack's argument appeals to consequences, but does so in service of the normative question of whether a community of truth-seekers should adopt norms against appeals to consequences. Being a normative question, this is precisely where appeals to consequences are valid and desired.

I think you should think of the validity/invalidity of appeals to consequences as the main thing at stake in this argument, in so far as you are wondering what it's all about (ie trying to ask me exactly what kind of claim I'm making). Fighting against ubiquitous low-level manipulation would be nice, but there isn't really a proposal on the table for accomplishing that.

***1**: For the record, I believe the classical "did you know tomatoes aren't vegetables, they're fruits?" is essentially an urban legend with no basis in scientific classification. Vegetable is essentially a culinary term. If you want to speak in biology terms, then yes, it's also a fruit, but that's not mutually exclusive with it being a vegetable. But in any case, it's clear that there can be terminological conflicts like this, even if "vegetable" isn't one of them; and "tomato" is a familiar example, even if it's spurious. So we can carry on using it as an example for the sake of argument.*

#### [>>>>>>>>>>>>>>] TAG · 0 karma · 2020-12-31 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=8RwDXpcZY8MTcD5e4
>So if your friends are using concepts which are optimized for other things, then either (1) you’ve got differing goals and you now would do well to sort out which of their concepts have been gerrymandered, (2) they’ve inherited gerrymandered concepts from someone else with different goals, or (3) your friends and you are all cooperating to gerrymander someone else’s concepts (or, (4), someone is making a mistake somewhere and gerrymandering concepts unnecessarily).

So? That's a very particular set of problems. If you try to solve them by banning all unscientific concepts, then you lose all the usefulness they have in other contexts.

>I’m just saying there’s something special about avoiding these things, whenever possible,

Wherever possible, or wherever beneficial? Does it make the world a better place to keep pointing out that tomatoes are fruit?


>because if you care deeply about clear thinking, and don’t want the overhead of optimizing your memes for political ends (or de-optimizing memes from friends from those ends), this is the way to do it.

You personally can do what you like. If you don't assume that everyone has to have the same solution, then there is no need for conflict.


>If you use a gerrymandered concept, you may have no understanding of the non-gerrymandered versions; or you may have some understanding, but in any case not the fluency to think in them.

I'm not following you any more. Of course unscientific concepts can go wrong -- anything can. But if you're not saying everyone should use scientific conceotts all the time, what are you saying?

>I see Zack as (correctly) ruling in mere optimization of concepts to predict the things we care about, but ruling out other forms of optimization of concepts to be useful.

I think that is Zacks argument, and that it s fallacious. Because we do things other than predict.


>>Low level manipulation is ubiquitous. You need to argue for “manipulative in an egregiously bad way” separately

>I’m arguing that Zack’s definition is a very good Schelling fence to put up


You are arguing that it is *remotely possible* to eliminate *all* manipulation???

>One of Zack’s recurring arguments is that appeal to consequences is an invalid argument when considering where to draw conceptual boundaries

Obtaining  good consequences is a very good reason to do a lot of things.

#### [>>>>>>>>>>>>>>>] abramdemski · 3 karma · 2021-01-21 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=7yPx48fibFFz9tfSi
>> So if your friends are using concepts which are optimized for other things, then either (1) you’ve got differing goals and you now would do well to sort out which of their concepts have been gerrymandered, (2) they’ve inherited gerrymandered concepts from someone else with different goals, or (3) your friends and you are all cooperating to gerrymander someone else’s concepts (or, (4), someone is making a mistake somewhere and gerrymandering concepts unnecessarily).
>
> So? That’s a very particular set of problems. If you try to solve them by banning all unscientific concepts, then you lose all the usefulness they have in other contexts.

It seems like part of our persistent disagreement is:

* I see this as *one of very few pathways, and by far the dominant pathway*, by which beliefs can be beneficial in a different way from useful-for-prediction
* You see this as *one of many many pathways*, and very much a corner case

I frankly admit that I think you're just wrong about this, and you seem quite mistaken in many of the other pathways you point out. The argument you quoted above was supposed to help establish my perspective, by showing that there would be no reason to use gerrymandered concepts *unless* there was some manipulation going on. Yet you casually brush this off as a very particular set of problems.

>> I’m just saying there’s something special about avoiding these things, whenever possible,
>
> Wherever possible, or wherever beneficial? Does it make the world a better place to keep pointing out that tomatoes are fruit?

As a general policy, I think that yes, frequently pointing out subtler inaccuracies in language helps practice specificity and gradually refines concepts. For example, if you keep pointing out that tomatoes are fruit, you might eventually be corrected by someone pointing out that "vegetable" is a culinary distinction rather than a biological one, and so there is no reason to object to the classification of a tomato as a vegetable. This could help you develop philosophically, by providing a vivid example of how we use multiple overlapping classification systems rather than one; and further, that scientific-sounding classification criteria don't always take precedence (IE culinary knowledge is just as valid as biology knowledge).

>> If you use a gerrymandered concept, you may have no understanding of the non-gerrymandered versions; or you may have some understanding, but in any case not the fluency to think in them.
> 
> I’m not following you any more. Of course unscientific concepts can go wrong—anything can. But if you’re not saying everyone should use scientific conceotts all the time, what are you saying?

In what you quoted, I was trying to point out the distinction between *speaking a certain way* vs *thinking a certain way*. My overall conversational strategy was to try to separate out the question of whether you should speak a specific way from the question of whether you should think a specific way. This was because I had hoped that we could more easily reach agreement about the "thinking" side of the question.

More specifically, I was pointing out that *if we restrict our attention to how to think*, then (I claim) the cost of using concepts for non-epistemic reasons is very high, because you usually cannot *also* be fluent in the more epistemically robust concepts, without the non-epistemic concepts losing a significant amount of power. I gave an example of a Christian who understands the atheist worldview in too much detail.

>> I see Zack as (correctly) ruling in mere optimization of concepts to predict the things we care about, but ruling out other forms of optimization of concepts to be useful.
>
> I think that is Zacks argument, and that it s fallacious. Because we do things other than predict.

I need some kind of map of the pathways you think are important here. 

I 100% agree that we do things other than predict. Specifically, we act. However, the effectiveness of action seems to be very dependent on the accuracy of predictions. We either (a) come up with good plans by virtue of having good models of the world, or (b) learn how to take effective actions "directly" by interacting with the world and responding to feedback. Both of these rely on good epistemics (because learning to act "directly" still relies on our understanding of the world to interpret the feedback -- ie the same reason ML people sometimes say that reinforcement learning is essentially learning a classifier).

That view -- that by far the primary way in which concepts influence the world is via the motor output channels, which primarily rely on good predictions -- is the foundation of my view that most of the benefits of concepts optimized for things other than prediction must be manipulation.

>>> Low level manipulation is ubiquitous. You need to argue for “manipulative in an egregiously bad way” separately
>>
>> I’m arguing that Zack’s definition is a very good Schelling fence to put up
>
> You are arguing that it is remotely possible to eliminate all manipulation???

Suppose we're starting a new country, and we are making the decision to outlaw theft. Someone comes to you and says "it isn't remotely possible to eliminate all theft!!!" ... you aren't going to be very concerned with their argument, right? The point of laws is not to entirely eliminate a behavior (although it would be nice). The point is to help make the behavior uncommon enough that the workings of society are not too badly impacted.

In Zack's case, he isn't even suggesting criminal punishment be applied to violations. It's more like someone just saying "stealing is bad". So the reply "you're saying that we can eliminate all theft???" seems even less relevant.

>> One of Zack’s recurring arguments is that appeal to consequences is an invalid argument when considering where to draw conceptual boundaries
>
> Obtaining good consequences is a very good reason to do a lot of things.

Again, I'm going to need some kind of map of how you see the consequences flowing, because I think the main pathway for those "good consequences" you're seeing is manipulation.

#### [>>>>>>>>>>>>>>>>] TAG · 1 karma · 2021-02-07 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=qsg8RWY8cXKs6EnSH
> I frankly admit that I think you’re just wrong about this, and you seem quite mistaken in many of the other pathways you point out

I dont think you have shown that.  

>>Wherever possible, or wherever beneficial? Does it make the world a better place to keep pointing out that tomatoes are fruit?

> As a general policy, I think that yes, frequently pointing out subtler inaccuracies in language helps practice specificity and gradually refines concepts. Everything else is Manipulation, and Manipulation is always bad".

I agree that gaining a meta level undertanding of jargons and the assumptions behind them is useful. I don't agree that, once you have such an understanding, it reduces to, "everything is or should be passive reflection of statistical regularities in pre-existing reality.

> In what you quoted, I was trying to point out the distinction between speaking a certain way vs thinking a certain way. My overall conversational strategy was to try to separate out the question of whether you should speak a specific way from the question of whether you should think a specific way. This was because I had hoped that we could more easily reach agreement about the “thinking” side of the question.

Arguing against whom? I dont believe that ones thinking should be constrained by some narrow set of interests. I have never said it should.  On the contrary, I have been arguing against the narrowness of "everything is or should be passive reflection of statistical regularities in pre existing reality".

>More specifically, I was pointing out that if we restrict our attention to how to think, then (I claim) the cost of using concepts for non-epistemic reasons is very high, because you usually cannot also be fluent in the more epistemically robust concepts, without the non-epistemic concepts losing a significant amount of power.

That is yet another surreptitious appeal to the unproven assumption that passive reflection is the only game in town. The agument can easilly be inverted: assuming that what we are doing is constructing a better world or ourselves, then we would be hampered by only using concepts that are"epistemic" in the sense of being restricted to restricted to labelling what is already there.

Of course, construction isnt the only game in town either.

>I need some kind of map of the pathways you think are important here.

what has been offered already are the ideas of:-

1) self-fulffilling prophecies, AKA blueprints AKA social constructs

2) co-ordination.

3) fuctionality. Treating a tomato as a vegeable tells you wha to do with it for culinary puposes.

What hasn't been offered is any reason to think those things don't exist, or aren't important, or aren't useful. My 1) and 2) are Zack's b) and d). Zack dismissed b) and d) without argument.

>We either (a) come up with good plans by virtue of having good models of the world, 

Of course, you can't come up with a plan for making the world better that consists of nothing but a passive model of the world, however accurate it might be. 

You seem to be confusing necessity and sufficiency.

>That view—that by far the primary way in which concepts influence the world is via the motor output channels, which primarily rely on good predictions—is the foundation of my view that most of the benefits of concepts optimized for things other than prediction must be manipulation

There's nothing anyone can say to you that would change the automatic and unconscious operation of your motor channels.

>In Zack’s case, he isn’t even suggesting criminal punishment be applied to violations. It’s more like someone just saying “stealing is bad”. So the reply “you’re saying that we can eliminate all theft???” seems even less relevant.

You are arguing that not wanting to eliminate all manipulation is compatible with believing all manipulation to be bad. That falls short of showing that all manipulation is bad. (We're holding a debate. So, you're trying to change my mind, and I yours..isn't that manipulation?)

>I think the main pathway for those “good consequences” you’re seeing is manipulation.

I don't think you have shown that either. And it wouldn't matter unless All Manipulation is Bad.

You haven't refuted the counterexamples to everything-that-isnt-reflection-is-manipulation, and  you havent shown that all manipulation is bad, either.

#### [>>>>>>>>>>>>>>>>>] abramdemski · 5 karma · 2021-02-15 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=4zkT8qqd4dMFEANCG
> I dont think you have shown that.

I feel like you're taking my attempts to explain my position and requiring that each one be a rigorous defense. Sometimes we just have to spend some time trying to understand each other before we can bring the knives out or whatever, yeah? Sorry if I'm guilty of the same thing -- I tried to unpack some more details after my flat statement that I thought you were wrong, but it probably came off as just being argumentative.

> >>>If you use a gerrymandered concept, you may have no understanding of the non-gerrymandered versions; or you may have some understanding, but in any case not the fluency to think in them.

> >>I’m not following you any more. Of course unscientific concepts can go wrong—anything can. But if you’re not saying everyone should use scientific conceotts all the time, what are you saying?
> 
> >In what you quoted, I was trying to point out the distinction between speaking a certain way vs thinking a certain way. My overall conversational strategy was to try to separate out the question of whether you should speak a specific way from the question of whether you should think a specific way. This was because I had hoped that we could more easily reach agreement about the “thinking” side of the question.
> 
>   
> Arguing against whom? I dont believe that ones thinking should be constrained by some narrow set of interests. I have never said it should. On the contrary, I have been arguing against the narrowness of "everything is or should be passive reflection of statistical regularities in pre existing reality".

(Sorry, I just don't get how this is relevant to the quote you're apparently responding to; I didn't use the words 'arguing against' there, and was describing my conversational goal, rather than arguing something. So I'm going to try to make some more clarifying remarks which may not answer your question:)

You ask "if you're not saying everyone should use scientific concepts all the time, what are you saying?"

I have attempted to separately argue the following:

1.  ***Much*** of the time, using "unscientific concepts" is a mistake. In particular, by trying to separate thinking vs speaking, I was trying to point out that even in cases where it's plausible that you are better off speaking in epistemically unhygenic ways, it's not plausible that you're better off *thinking* in those ways: there's a high cost to pay in not understanding the world. (**Note the weak "much of the time" qualifier here -- I endorse this point and think it's important to the discussion, but I'm endorsing a rather weak statement, on purpose.**)
2.  ***Most*** of the time, using "unscientific concepts" is useful only for manipulative purposes. My argument here is based on the idea that agents with shared goals will communicate in a way which shares as much information as possible (in the bits communicated -- IE, modulo communication costs, redundancy built into the language to ensure communication over noisy channels, etc). Therefore, behavior contrary to this must be either uncooperative or simply sub-optimal. This doesn't mean it's irrational (a consequentialist might manipulate others), but I presume that you would be less happy to argue in favor of unscientific concepts if you conceded that they were almost always manipulative. Your response to this was to call my argument a "very special case". I do not concede this; I think it is a very general case. (I do not currently understand why you called it a very special case.)
3.  ***Very nearly all of the time***, it makes sense to separate out pure epistemic quality and consider it as a coherent goal, talk about how to achieve it, etc. (Not *pursue it singlemindedly*, but *distinguish it as a comprehensible thing*.) In particular, it makes sense to have this discussion about nearly any statement. I perceive you as having a large disagreement with me about this, thinking that it makes a lot less sense for some statements, EG those about marriage and money.
4.  ***Some of the time***, it makes sense to have a social norm against appeals to consequences (as an argument for changing epistemic stances), in order to safeguard 'scientific' thought-processes against distortion. In particular, I think it makes sense on lesswrong. This is not a claim that all conceptual gerrymandering can be eliminated, but rather, that we should make the attempt (at least in specific arenas of discourse).

> what has been offered already are the ideas of:-
> 
> 1) self-fulffilling prophecies, AKA blueprints AKA social constructs
> 
> 2) co-ordination.
> 
> 3) fuctionality. Treating a tomato as a vegeable tells you wha to do with it for culinary puposes.
> 
> What hasn't been offered is any reason to think those things don't exist, or aren't important, or aren't useful. My 1) and 2) are Zack's b) and d). Zack dismissed b) and d) without argument.

I fully conceded #1 earlier in our discussion -- I have no qualms with this pathway, and I think it's important. I don't think it entails accepting less-accurate beliefs (a self-fulfilling prophecy is, after all, true!), but I do think it entails valid appeals-to-consequences for what might otherwise seem like purely epistemic questions. Furthermore I think this is relatively common.

I fully concede #3, and also perceive Zack as explicitly doing so, as part of his central argument.

I am not trying to defend a norm against #1 or #3, nor am I defending a concept of "pure epistemics" which regards #1 or #3 as impurities, in my own points 1-4 earlier. I think "pure epistemics" without your #1 would be very limited, because it becomes ill-defined in the presence of self-fulfilling prophecies or other predictions which are relevant to their own outcomes. I think "pure epistemics" without your #3 is very nearly useless, due to a lack of focus on useful questions. Both of these things are coherent things to talk about, but not very useful to agents, and therefore less *descriptively* apt for *discussing and understanding* agents, nor as *normatively* apt for a community of agents.

As for #2, I think some of this is covered by #1. Everything else, I claim is manipulative, like EG promising a good afterlife if you help build a pyramid in the middle of the desert. Manipulation works, but I continue to presume it's not what you're defending when you defend 'unscientific concepts'.

So I suppose either (a) we can agree on all of that, and don't have any remaining disagreement, or (b) our main disagreement is with #2, and we should focus on my argument that epistemic impurities are going to be manipulative, or (c) your 1-3 don't cover all the bases you think are important, and we should talk about what other channels make unscientific concepts useful. (Or perhaps some mix of a-c.)

#### [>>>>>>>>>>>>>>>>>>] TAG · 0 karma · 2021-03-20 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=yNQyiBhWP9iCmDdka
>I feel like you’re taking my attempts to explain my position and requiring that each one be a rigorous defense. 

If someone has made a position clear, they need to move onto defending it at some stage, or else it's all just opinion.

You clearly think that some concepts lack objectivity .. that's been explained a great length with equations and diagrams...and you think that the very existence of scientific objectivity is in danger. But between these two claims there are any number of intermediate steps that have not been explained or defended.

>Much of the time, using “unscientific concepts” is a mistake

I don't see why. It's not a mistake to use special purpose or value laden concepts *appropriately*. So how can it be usually be a mistake to use them? Are you saying that they are usually used inappropriately?

>Most of the time, using “unscientific concepts” is useful only for manipulative purposes. My argument here is based on the idea that agents with shared goals will communicate in a way which shares as much information as possible (in the bits communicated—IE, modulo communication costs, redundancy built into the language to ensure communication over noisy channels, etc).

No. If they have shared goals, they will already have a lot of shared information ( ie. small inferential distance) *and* they will already use a special purpose jargon. 
Special interest groups always have special language. Objective, scientific language is what scientists use, and not that many people are scientists, so it is not the default.

In any case, how is that evidence of manipulation?

>but I presume that you would be less happy to argue in favor of unscientific concepts if you conceded that they were almost always manipulative. 

I don't concede that they are always manipulative, in an objectionable sense. We are at the stage where you need to clarify that.

>Your response to this was to call my argument a “very special case”. I do not concede this; I think it is a very general case. (I do not currently understand why you called it a very special case).

How common is manipulation? If you set the bar on what constitutes manipulation very low, then it is very common, even including this discussion. But if it is very common, how can it be very bad? If you think that all gerrymandered concepts are "manipulative" in the sense of micro manipulations, where's the problem?

I think this a central weakness of your case: you need to choose one of "manipulation common", and "manipulation bad".

>Very nearly all of the time, it makes sense to separate out pure epistemic quality and consider it as a coherent goal, talk about how to achieve it, etc. 

Why? And for whom?

>Some of the time, it makes sense to have a social norm against appeals to consequences (as an argument for changing epistemic stances), in order to safeguard ‘scientific’ thought-processes against distortion

Well, if it's only some of the time, you can achieve that by saying that scientists are special people who do have an obligation to be as objective as possible , but no obligation to be consequentialist. But that's not novel.

>As for #2, I think some of this is covered by #1. Everything else, I claim is manipulative, like EG promising a good afterlife if you help build a pyramid in the middle of the desert

That seems like a weakman to me. What about cases where coordination is of benefit to the people doing the coordinating...like obeying traffic laws? A speed limit is a gerrymandered concept.

#### [>>>>>>>>>>>>>>] Raemon · 14 karma · 2021-01-21 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=ChHT4n4yEivsCtKh4
> I do, of course, think that the LessWrong community should be and to an extent is such a place.

Something about this has been bugging me and I maybe finally have a grasp on it. 

It's perhaps somewhat entangled with this older Benquo comment elsewhere in this thread. I'm not sure if you endorse this phrasing but your prior paragraph seems similar:

> Discourse about how to speak the truth efficiently, on a site literally called "Less Wrong," shouldn't have to explicitly disclaim that it's meant as advice within that context every time, even if it's often helpful to examine what that means and when and how it is useful to prioritize over other desiderata.

Since a couple-years-ago, I've updated "yes, LessWrong should be a fundamentally truthseeking place, optimizing for that at the expense of other things." (this was indeed an update for me, since I came here for the Impact and vague-appreciation-of-truthseeking, and only later updated that yes, [Epistemics are one of the most important cause areas](https://www.lesswrong.com/posts/5nH5Qtax9ae8CQjZ9/no-it-s-not-the-incentives-it-s-you?commentId=naqkFQuaTAKXiAcEg))

But, one of the most important things I want to get out of LessWrong is a clear map of how the rest of the world works, and how to interface with it.

So when I read the conclusion here...

> Similarly, the primary thing when you take a word in your lips is your intention to reflect the territory, whatever the means. Whenever you categorize, label, name, define, or draw boundaries, you must cut through to the correct answer in the same movement. If you think only of categorizing, labeling, naming, defining, or drawing boundaries, you will not be able actually to reflect the territory.

...I feel like my epistemics are kind of under attack. 

I feel like this statement is motte-and-bailey-ing between "These are the rules of thinking rationally, for forming accurate beliefs, and for communicating about that in particular contexts" and "these are the rules of communicating, in whatever circumstances you might find yourself."

And it's actually a pretty big *epistemic* deal for a site called LessWrong to not draw that distinction. "How coordination works, even with non-rationalists", is as really big deal, not a special edge case, and I want to be maintaining an accurate map of it the entire time that I'm building out my theory of rationality.

#### [>>>>>>>>>>>>>>>] Raemon · 7 karma · 2021-01-21 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=SDFrKzy9WDCFH8baK
Sort of relatedly, or on the flipside of the coin:

In these threads, I've seen a lot of concern with using language "consequentially", rather than rooted in pure epistemics and map-territory correspondence. 

And those arguments have always seemed weird to me. Because... what could you possibly be grounding this all out in, other than consequences? It seems useful to have a concept of "appeals to consequence" being logically invalid. But in terms of what norms to have on as public forum, the key issue on a public forum is that appeals to *shortsighted* consequences are bad, for the same reason shortsighted consequentialism is often bad.

If you don't call the president a Vargath (despite them obviously supporting Varg), because they'd be offended, it seems fairly straightforward to argue that this has bad consequences. You just have to model it out more steps.

I would agree with the claim "if you're constantly checking 'hey, in this particular instance, maybe it's net positive to lie?' you end lying all the time, and end up in a world where people can't trust each other", so it's worth treating appeals to consequences as forbidden as part of a Rule Consequentialism framework. But, why not just say that?

#### [>>>>>>>>>>>>>>>>] Raemon · 4 karma · 2021-01-21 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=HzsD4NXiHHri2cBSv
(I say all of this largely agreeing with the thrust of what the post and your (Abram's) comments are pointing at, but feeling like something about the exact reasoning is off. And it feeling consistently off has been part of why I've taken awhile to come around to the reasoning)

#### [>>>>>>>>>>>>>>>>] abramdemski · 6 karma · 2021-02-15 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=GpAJ6Pxdcm8aL7tp8
> Because... what could you possibly be grounding this all out in, other than consequences?

In my mind, it stands as an open problem whether you can "usually" expect an intelligent system to remain "agent-like in design" under powerful self-modification. By "agent-like in design" I mean having subcomponents which transparently contribute to the overall agentiness, such as true beliefs, coherent goal systems, etc.

The argument in favor is: it becomes really difficult to self-optimize as your own mind-design becomes less modular. At some point you're just a massive policy with each part fine-tuned to best shape the future (a future which you had some model of at some point in the past); at some point you have to lose general-purpose learning. Therefore, agents with complicated environments and long time horizons will stay modular.

The argument against is: it just isn't very probable that the nice clean design is the most optimal. Even if there's only a small incentive to do weird screwy things with your head (ie a small chance you encounter Newcomblike problems where Omega cares about aspects of your ritual of cognition, rather than just output), the agent will follow that incentive where it leads. Plus, general self-optimization can lead to weird, non-modular designs. Why shouldn't it?

So, in my mind, it stands as an open problem whether purely consequentialist arguments tend to favor a separate epistemic module "in the long term".

Therefore, I *don't* think we can always ground pure epistemic talk in consequences. At least, not without further work.

However, I *do* think it's a coherent flag to rally around, and I *do* think it's an important goal in the short term, and I think it's particularly important for a large number of agents trying to coordinate, and it's also possible that it's something approaching a terminal goal for humans (ie, curiosity wants to be satisfied by truth).

So I *do* want to defend pure epistemics as its own goal which doesn't continuously answer to broad consequentialism. I perceive some reactions to Zack's post as isolated demands for rigor, invoking the entire justificatory chain to consequentialism when it would not be similarly invoked for a post about, say, p-values.

(A post about p-values vs bayesian hypothesis testing *might* give rise do discussions of consequences, but not questions of whether the whole argument about bayes vs p-values *makes sense* because *isn't epistemics ultimately consequentialist anyway* or similar.)

> I would agree with the claim "if you're constantly checking 'hey, in this particular instance, maybe it's net positive to lie?' you end lying all the time, and end up in a world where people can't trust each other", so it's worth treating appeals to consequences as forbidden as part of a Rule Consequentialism framework. But, why not just say that?

I would respond:

1.  Partly for the same reason that a post on Bayes' Law vs p-values wouldn't usually bother to say that; it's at least one meta level up from the chief concerns. Granted, unlike a hypothetical post about p-values, Zack's post *was* about the appeal-to-consequences argument from its inception, since it responds to an inappropriate appeal to consequences. However, Zack's primary argument is on the object level, pointing out that how you define words *is* of epistemic import, and therefore *cannot* be chosen freely without making epistemic compromises.
2.  TAG and perhaps other critics of this post are *not* conceding that much; so, the point you make doesn't seem like it's sufficient to address the meta-level questions which are being raised.

I would concede that there is, perhaps, something funny about the way I've been responding to the discussion -- I have a sense that I might be doing some motte/bailey thing around (motte:) this is an isolated demand for rigor, and we should be able to talk about pure epistemics as a goal without explicitly qualifying everything with "if you're after pure epistemics"; vs (bailey:) we should pursue pure epistemics. In writing comments here, I've attempted to carefully argue the two separately. However, I perceive TAG as not having received these as separate arguments. And it is quite possible I've blurred the lines at times. They are pretty relevant to each other.

#### [>>>>>] Zack_M_Davis [AUTHOR] · 7 karma · 2020-12-13 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=Xr4Sx7JrZwf74ECvL
> But that isn't relevant to what you are saying, because you are making a normative point: you are saying some concepts are wrong.

You know, I think I agree that the reliance on normativity intuitions is a weakness of the original post as written in April 2019. I've thought a lot more in the intervening 20 months, and have been working on a sequel that I hope to finish very soon (working title "Unnatural Categories Are Optimized for Deception", current draft sitting at 8,650 words) that I think does a _much_ better job at [reducing that black box](https://www.lesswrong.com/posts/HnS6c5Xm9p9sbm4a8/grasping-slippery-things). (That is, I think the original normative claim is basically "right", but I now have a deeper understanding of what that's even supposed to mean.)

In summary: when I say that some concepts are wrong, or more wrong than others, I just mean that some concepts are worse than others at making probabilistic predictions. We can formalize this with specific calculations in simple examples (like the Foos clustered at [1, 2, 3] in ℝ³ in the original post) and be confident that the underlying mathematical principles apply to the real world, even if the real world is usually too complicated for us to do explicit calculations for.

This is _most_ straightforward in cases where the causal interaction between "the map" and "the territory" goes only in the one direction "territory → map", and where where we only have to consider _one_ agent's map. As we relax those simplifying assumptions, the theory has to get more complicated.

First complication: if there are _multiple_ agents with aligned perferences but limited ability to communicate, then they potentially face coordination problems: that's what "Schelling Categories" is about.

Second complication: if there are multiple agents whose preferences _aren't_ aligned, then they might have an incentive to decieve each other, making the other agent have a worse map in a way that will trick it into making decisions that benefit the first agent. (Or, a poorly-designed agent might have an incentive to deceive itself, "wireheading" on making the map look good, instead of using a map that reflects the territory to formulate plans that make the territory better.) This is what my forthcoming sequel post is about.

Third complication: if the map can affect the territory, you can have self-fulfilling (or partially-self-fulfilling, or self-negating) prophecies. I'm not sure I understand the theory of this yet.

The sense in which I deny that scientifically inaccurate maps can have compensatory kinds of usefulness, is that I think they have to fall into the second case: the apparent usefulness has to derive from deception (or wireheading). Why _else_ would you want a model/map that makes worse predictions rather than better predictions? (Note: self-fulfilling prophecies _aren't_ inaccurate!)

> You're one of them.

Well, yes. I mean, _I_ think I'm fighting for more accurate maps, but that's (trivially) still fighting! I don't doubt that [the feeling is mutual](http://unremediatedgender.space/2020/Nov/the-feeling-is-mutual/).

I'm reminded of discussions where one person argues that a shared interest group (for concreteness, let's say, a chess club) should remain politically neutral (as opposed to, say, issuing a collective condemnation of [puppy-kicking](https://tvtropes.org/pmwiki/pmwiki.php/Main/KickTheDog)), to which someone responds that everything is political and that therefore neutrality is just supporting the status quo (in which some number of puppies per day will continue to be kicked). There's a sense in which it's _true_ that everything is political! (As it is written, refusing to act is like refusing to allow time to pass.)

I think a better counter-counter reply is not to repeat that Chess Club should be "neutral" (because I don't know what that means, either), but rather to contend that it's _not Chess Club's job_ to save the puppies of the world: we can save more puppies with a division of labor in which Chess Club focuses on Society's chess needs, and an Anti-Puppy-Kicking League focuses on Society's interest in saving puppies. (And if you think Society should care more about puppies and less about chess, you should want to _defund_ Chess Club rather than having it issue collective statements.)

Similarly, but even more fundamentally, it's _not the map's job_ to provide compensatory usefulness; the map's job is to reflect the territory. In a world where agents are using maps to make decisions, you probably _can_ affect the territory by distorting the map for purposes that aren't about maximizing predictive accuracy! It's just _really bad AI design_, because by the very nature of the operation, [you're sabotaging your ability to _tell_ whether your intervention is actually making things better](https://www.lesswrong.com/posts/Hs3ymqypvhgFMkgLb/doublethink-choosing-to-be-biased).

#### [>>>>>>] TAG · 1 karma · 2020-12-22 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=67EKSTSqAWkv32u2i
[empty or deleted comment]

#### [>>>>>>] TAG · 0 karma · 2020-12-22 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=qM9Z2Cj7NaGsTEA6t
>In summary: when I say that some concepts are wrong, or more wrong than others, I just mean that some concepts are worse than others at making probabilistic predictions. 

That would be true if the only useful thing, or the only thing anyone does, is making probability calculations.

>We can formalize this with specific calculations 

You can formalise the claim that some concepts are worse than others at making probabilistic predictions, as such, but that doesnt give you the further claim that " the only useful thing, or the only thing anyone does, is making probability calculations".

#### [>>>>>>] TAG · 1 karma · 2020-12-22 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=CRT6gBtGBiHHoAXxM
>In summary: when I say that some concepts are wrong, or more wrong than others, I just mean that some concepts are worse than others at making probabilistic predictions. 


That would be true if the only useful thing, or the only thing anyone does, is making probability calculations

>The sense in which I deny that scientifically inaccurate maps can have compensatory kinds of usefulness, is that I think they have to fall into the second case: the apparent usefulness has to derive from deception (or wireheading). Why else would you want a model/map that makes worse predictions rather than better predictions? 

Because you are doing something other than prediction.

#### [>>>>>>>] Zack_M_Davis [AUTHOR] · 3 karma · 2020-12-22 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=FdMFttMvkue7r3roq
What _specific_ other thing are you doing besides prediction? If you can give me a specific example, I think I should be able to reply with either (a) "that's a prediction", (b) "that's coordination", (c) "here's an explanation of why that's deception/wireheading in the technical sense I've described", (d) "that's a self-fulfilling prophecy", or (e) "whoops, looks like my philosophical thesis isn't quite right and I need to do some more thinking; thanks TAG!!".

(I should be able to reply _eventually_; no promises on turnaround time because I'm coping with the aftermath of a crisis that I'm no longer involved in, but for which I have both a moral responsibility and selfish interest to reflect and repent on my role in.)

#### [>>>>>>>>] TAG · 2 karma · 2020-12-31 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=WFb4c8NQN3a6mLq8v
Why are (b) and (d) *not* exceptions to your thesis, already?

You surely need to argue that exceptions to everything-is-prediction are i) non existent, or ii) minor or iii) undesirable, normatively wrong. 

But co ordination is extremely valuable. 

And "self fulfilling prophecy" is basically looking at creation and construction through the lens of prediction. 
Making things is important. If you build something according to a blueprint, it will happen to be the case that once it is built, the blueprint describes it, but that is incidental.

You can make predictions about money, but that is not the central purpose of money.

#### [>>>>>>>>] Raemon · 3 karma · 2021-01-11 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=vXcM5mgRtfA9WZzTd
Seconding TAG's:

> Why are (b) and (d) *not* exceptions to your thesis, already?

FYI I am also pretty confused about this. Have you (Zack) previously noted something somewhere about "that's coordination"... and... somehow wrapping that around to "but words are just for prediction anyway?". 

"That's deception/wireheading" feels like a reasonable, key thing to be aware of. I think you're maybe trying to build towards something like "and a lot of coordination is oriented around deception, and that's bad, or suboptimal, or at least sad", but not sure.

The newer "Unnatural Categories" post seemed to build towards that, but then completely ignored the question of nation-border category boundaries which seemed pretty key.

(Overall I feel pretty happy to watch you explore this entire line of reasoning deeply over the years and learn from it. I think intellectual progress depends a lot on people picking a bunch of assumptions and running with them deeply and then reporting their findings publicly. But I currently feel like there's a pretty gaping hole in your arguments that have something-or-other-to-do-with "but, like, coordination tho")

#### [>>>>>>>>>] Zack_M_Davis [AUTHOR] · 5 karma · 2021-01-12 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=SAc3vBuENePzyLsC4
> Have you (Zack) previously noted something somewhere about "that's coordination"... and... somehow wrapping that around to "but words are just for prediction anyway?". 

[Yes!](https://www.lesswrong.com/posts/edEXi4SpkXfvaX42j/schelling-categories-and-simple-membership-tests) [You commented on it!](https://www.lesswrong.com/posts/edEXi4SpkXfvaX42j/schelling-categories-and-simple-membership-tests?commentId=uKvghBhL7gFF5YDfh)

#### [>>>>>>>>>>] Raemon · 3 karma · 2021-01-12 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=bQazeDTTjnM9CaYe2
Whelp! Off to re-read. Thank you sir.

#### [>>>>>>>>>>] Raemon · 3 karma · 2021-01-12 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=ZwrEZYcpz834MXCDK
Have now re-read. Am actually a bit sad I didn't notice that post to nominate it.

#### [>>>] DanielFilan · 8 karma · 2020-12-13 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=LZNRtdk5ffCje5vcQ
> For instance, you can't change the speed of light, but you can revalue your currency

Note that I personally can't actually revalue the US dollar (the currency that I mostly use), except the small revaluation that would happen were I to tear up a $20 note. If I were to personally decide to use a different 'money' concept, I imagine I'd get a bunch of predictions wrong or fail to obtain food or something. Perhaps I could convince all my compatriates to use FilanBucks instead, but I'd expect that most relative prices would stay the same, indicating that there are some facts of the matter that this 'money' thing is reflecting that aren't just about our shared opinions about 'money'.

I also think that this doesn't really divide 'social constructs' and 'scientific subjects'. For instance, my mass is probably a scientific subject, and yet I can change it, and yet I still want to use basically the same epistemology to understand my mass as I do to understand other physical traits of things.

#### [>] abramdemski · 7 karma · 2020-12-12 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=GB8p2uYknJumezu3m
This comment just seems utterly wrong to me.

> In order for your map to be useful , it needs to reflect the statistical structure of things to the extent required by the value it is in service to.
> 
> That can be zero. There is a meta category of things that are created by humans without any footprint in pre existing reality. These include money, marriages, and mortgages

Obviously these things have a great deal of structure. There are multiple textbooks worth of information about how money works. A human can't just decide arbitrarily that they want those things to be different, change their usage of the word, and make it so.

Your argument might work better for someone making their own board game, because this is a case where one person really has the ability to set all of the rules on their own. 

But *even in that case,* it seems like words need to reflect statistical structures. If they don't, then they're not useful for anything.

It's just that the structures in question are made up by a human. They can still be described in better or worse ways.

#### [>>] TAG · 0 karma · 2020-12-12 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=En4Gd9FGh3RZm6hxn
> Obviously these things have a great deal of structure. 

Obviously they do. There's no obvious upper limit to the strutural compexity of a human creation. However, I was talking about *pre existing reality*.

There are constraints on what could be used as money -- Ice cubes and leaves are both bad ideas -- but they don't constrain it down to a natural kind.

 Money or marriage or mortgages are all things that need to work work in certain ways, but there aren't pre-existing Money or Marriage or Mortgage objects, and their working well isn't a degree of correspondence to something pre-existing -- what realists usually mean by "truth" -- it's more like usefulness.

> It’s just that the structures in question are made up by a human. 

So they are not pre-existing.

#### [>>>] abramdemski · 13 karma · 2020-12-12 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=bhNs2rZrReEJjDRDH
> Obviously they do. There's no obvious upper limit to the strutural compexity of a human creation. However, I was talking about *pre existing reality*.

I question whether "pre-existing" is important here. Zack is discussing whether words *cut reality at the joints,* not whether words cut *pre-existing* reality at the joints. Going back to the example of creating a game -- when you're writing the rulebook for the game, it's obviously important in ***some*** sense that you are the one who gets to make up the rules... but I argue that this does not change the whole question of how to use language, what makes a description apt or inept, etc.

For example, if I invented the game of chess, calling rooks a type of pawn and reversing the meaning of king/queen for black/white would be *poor map craftsmanship*.

> Money or marriage or mortgages are all things that need to work work in certain ways, but there aren't pre-existing Money or Marriage or Mortgage objects, and their working well isn't a degree of correspondence to something pre-existing -- what realists usually mean by "truth" -- it's more like usefulness.

None of these examples are convincing on their face, though -- there are all sorts of things we can say about each of these examples which seem to have truth values rather than usefulness values.

> There are constraints on what could be used as money -- Ice cubes and leaves are both bad ideas -- but they don't constrain it down to a natural kind.

Really though? Grains work much better than root vegetables, and metals work much better than grains. And these sorts of considerations end up being important for how history unfolds.

#### [>>>>] TAG · 0 karma · 2020-12-13 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=2KgrZBYW9JXK5xx5J
>I question whether “pre-existing” is important here. Zack is discussing whether words cut reality at the joints, not whether words cut pre-existing reality at the joints.

There are wider issues. 

>Going back to the example of creating a game—when you’re writing the rulebook for the game, it’s obviously important in some sense that you are the one who gets to make up the rule 

It's important in the sense that words can usefully refer to human constructs and concerns.

>but I argue that this does not change the whole question of how to use language, what makes a description apt or inept, etc.

It's not supposed to change the whole issue. It's supposed to address the inference from "does not reflect reality" to "useless, wrong do not use".

>None of these examples are convincing on their face, though—there are all sorts of things we can say about each of these examples which seem to have truth values rather than usefulness values

In loose and popular senses of "truth". But reductionist and elimiinativist projects take correspondence to pre existing reality as the gold standard of truth...that narrow sense is the one I am contrasting with usefulness.

>Really though? Grains work much better than root vegetables, and metals work much better than grains

To can you also use numbers and algorithms. You're not going to get a natural kind out of that lot.

#### [>>>>>] abramdemski · 4 karma · 2020-12-13 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=9q2qrr3QCQtdLaime
> It's not supposed to change the whole issue. It's supposed to address the inference from "does not reflect reality" to "useless, wrong do not use".

I think this is the wrong way to think about it. When we play a game of chess, the things we are referring to are still part of reality. This includes the physical reality of the board and pieces, various parts of mathematical reality related to strategies and positions, historical reality of various rules and games, etc. 

The map is part of the territory, and so the map will sometimes end up referring to itself, in an ungrounded sort of way. This can create strange situations.

For example, if I say "I welcome you", then saying so makes the sentence true.

This *does not* mean the concept of true and false fails to apply to "I welcome you".

Even though I have complete control over whether to welcome you, the inference from "does not reflect reality" to "wrong" is still perfectly valid.

> In loose and popular senses of "truth". But reductionist and elimiinativist projects take correspondence to pre existing reality as the gold standard of truth...that narrow sense is the one I am contrasting with usefulness.

This seems like a kind of reductive eliminativist approach which would reject logic, as logic does not correspond to anything in the physical world. After all, logic refers to the operations of the map, and *we draw the map*, so it is not pre-existing...

OK, that's a bit extreme and I shouldn't uncharitably put wolds in your mouth. But it seems like this kind of reductive eliminativism would declare sociology unscientific *by definition,* since sociology studies things humans do, not "pre-existing" reality. Similarly for economics (you've repeatedly mentioned money as outside the realm "true" applies to!), psychology, anthropology, etc.

Your reductive eliminativist notion of truth also seems to oddly insist that statements about the future (especially about the speaker's future actions) cannot be true or false, since clearly the future is not "pre-existing".

We are self-making maps which sit within the world we are mapping. Truth is correspondence to territory. Not "correspondence to parts of the territory outside of us map-makers". Not "correspondence to territory so long as that territory wasn't touched by us yet". Not "correspondence to parts of the territory we have no control over".

#### [>>>>>>] TAG · 1 karma · 2020-12-19 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=B6bQucCCMHByEWyvh
>I think this is the wrong way to think about it. When we play a game of chess, the things we are referring to are still part of reality.

Not in any important sense. Physical instantiations can be very varied..they don't have to look like a typical chess set...and you can play chess in your head if you're smart enough. Chess is a lot more like maths than it is like ichthyology.

>Even though I have complete control over whether to welcome you, the inference from “does not reflect reality” to “wrong” is still perfectly valid

In that one case.

>But it seems like this kind of reductive eliminativism would declare sociology unscientific by definition, since sociology studies things humans do, not “pre-existing” reality.

We already categorise sociology, etc, as *soft* sciences. Meaning that they are not completely unscientific...and also that they are not reflections of pre existing reality.

>Your reductive eliminativist notion of truth also seems to oddly insist that statements about the future (especially about the speaker’s future actions) cannot be true or false, since clearly the future is not “pre-existing”.

Assuming deteminism, statements about the future can be logically  inferred from a pre existing state of the universe plus pre existing laws.

>Truth is correspondence to territory.

Correspondence-truth is correspondence to the territory. Which is a tautology. Which is another kind of truth .

#### [>>>>>>>] abramdemski · 2 karma · 2020-12-20 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=pLYTf3E7HT8gtfBF2
> Not in any important sense. Physical instantiations can be very varied..they don't have to look like a typical chess set...and you can play chess in your head if you're smart enough. Chess is a lot more like maths than it is like ichthyology.

Lots of physical things can have varied instantiations. EG "battery". That in itself doesn't seem like an important barrier.

> >Even though I have complete control over whether to welcome you, the inference from “does not reflect reality” to “wrong” is still perfectly valid
> 
> In that one case.

OK, here's a more general case: I'm looking at a map you're holding, and making factual claims about where the lines of ink are on the paper, colors, etc.

This is very close to your money example, since I can't just make up the numbers in my bank account.

Again, the inference from "does not reflect reality" to "wrong" is perfectly valid.

It's true that I can change the numbers in my bank account by EG withdrawing/depositing money, but this is very similar to observing that I can change a rock by breaking it; it doesn't turn the rock into a non-factual matter.

> We already categorise sociology, etc, as *soft* sciences. Meaning that they are not completely unscientific...and also that they are not reflections of pre existing reality.

True, but it seems like "soft" is due to the fact that we can't get very precise predictions, or even very calibrated probabilities (due to a lot of distributional shift, poor reference classes, etc). NOT due to the concept of prediction failing to be meaningful.

As a thought experiment, imagine an alien species observing earth without interfering with it in any way. Surely, for them, our "social constructs" could be a matter of science, which could be predicted accurately or inaccurately, etc?

Then imagine that the alien moves to the shoulder of a human. It could still play the role of an impartial observer. Surely it could still have scientific beliefs about things like how money works at that point.

Then imagine that the alien occasionally talks with the human whose shoulder it is on. It does not try to sway decisions in any way, but it does offer the human its predictions if the human asks. In cases where events are contingent *on the prediction itself* (ie the prediction alters what the human does, which changes the subject matter being predicted), the alien does its best to explain that relationship to the human, rather than offer a specific prediction.

I would argue that the alien can still have scientific beliefs about things like how money works at this point.

Now imagine that the "alien" is just a sub-process in the human brain. For example, there's a hypothesis that the cortex serves a purely predictive role, while the rest of the brain implements an agent which uses those predictions. 

Again, I would argue that it's still possible for this sub-process to have factual/scientific/impartial predictions about EG how money works.

> Assuming deteminism, statements about the future can be logically inferred from a pre existing state of the universe plus pre existing laws.

Right, agreed. So I'd ask what your notion of "pre-existing" is, such that you made your initial statement (emphasis mine):

> In order for your map to be useful , it needs to reflect the statistical structure of things to the extent required by the value it is in service to.
> 
> That can be zero. There is a meta category of things that are created by humans without any footprint in ***pre existing reality***.

I understand your thesis to be that if something is not pre-existing reality, a map does not need to "reflect the statistical structure". I'm trying to understand what your thesis means. Based on what you said so far, I hypothesized that "pre-existing" might mean "not effected (causally) by humans". But this doesn't seem to be right, because as you said, the future can be predicted from the past using the ("pre-existing") state and the ("pre-existing") laws.

#### [>>>>>>>>] TAG · 0 karma · 2020-12-30 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=GtMawKefnmZ2myZXa
>It’s true that I can change the numbers in my bank account by EG withdrawing/depositing money, but this is very similar to observing that I can change a rock by breaking it; it doesn’t turn the rock into a non-factual matter.

Rocks existed before the concept of rocks. Money did not exist before he concept of money.

>As a thought experiment, imagine an alien species observing earth without interfering with it in any way. Surely, for them, our “social constructs” could be a matter of science, which could be predicted accurately or inaccurately, etc?

If the alien understands the whole picture, it will notice the causal arrow from human concerns to social constructs. For instance, if you want gay marriage to be a thing, you amend the marriage construct so that is.

#### [>>>>>>>>>] abramdemski · 2 karma · 2021-01-21 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=iXiTJ3k9q8WMQQonu
> If the alien understands the whole picture, it will notice the causal arrow from human concerns to social constructs. For instance, if you want gay marriage to be a thing, you amend the marriage construct so that is.

The point of the thought experiment is that, for the alien, all of that is totally mundane (ie scientific) knowledge. So why can't that observation count as scientific for us?

IE, just because we have control over a thing doesn't -- in my ontology -- indicate that the concept of map/territory correspondence no longer applies. It only implies that we need to have conditional expectations, so that we can think about what happens *if* we do one thing or another. (For example, I know that if I think about whether I'm thinking about peanut butter, I'm thinking about peanut butter. So my estimate "am I thinking about peanut butter?" will always be high, when I care to form such an estimate.)

> Rocks existed before the concept of rocks. Money did not exist before he concept of money.

And how is the temporal point at which something comes into existence relevant to whether we need to track it accurately in our map, aside from the fact that things temporally distant from us are less relevant to our concerns?

Your reply was very terse, and does not articulate very much of the model you're coming from, instead mostly reiterating the disagreement. It would be helpful to me if you tried to unpack more of your overall view, and the logic by which you reach your conclusions.

I know that you have a concept of "pre-existing reality" which includes rocks and not money, and I *believe* that you think things which aren't in pre-existing reality don't need to be tracked by maps (at least, something resembling this). What I don't see is the finer details of this concept of pre-existing reality, and why you think we don't need to track those things accurately in maps.

The point of my rock example is that *the smashed rock* did not exist before we smashed it. Or we could say "the rock dust" or such. In doing so, we satisfy your temporal requirement (the rock dust did not exist until we smashed it, much like money did not exist until we conceived of it). We also satisfy the requirement that we have complete control over it (we can make the rock dust, just like we can invent gay marriage).

I know *you don't think the rock example counts*, but I'm trying to ask for a more detailed model of *why* it doesn't. I gave the rock example because, presumably, you *do* agree that bits of smashed rock are the sort of thing we might want accurate maps of. Yet they seem to match your criteria.

Imagine for a moment that we had perfect control of how the rock crumbles. Even then, it would seem that we still might want a place in our map for the shape of the rock shards. Despite our perfect control, we might want to remember that we shaped the rock shards into a key and a matching lock, etc.

Remember that the original point of this argument was your assertion: 

> In order for your map to be useful , it needs to reflect the statistical structure of things to the extent required by the value it is in service to.
>
> That can be zero. There is a meta category of things that are created by humans without any footprint in pre existing reality. These include money, marriages, and mortgages

So -- to the extent that we are remaining relevant to the original point -- the question is why, in your model, there is zero need to reflect the statistical structure of money, marriage, etc.

#### [>>>>>>>>>>] TAG · 1 karma · 2021-01-22 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=XZnF7keoPFFR7HYca
>The point of the thought experiment is that, for the alien, all of that is totally mundane (ie scientific) knowledge. So why can’t that observation count as scientific for us?

The point is that the rule "if it is not in the territory it should not be in the map" does not apply in cases where we are constructing reality, not just reflecting it.

If you are drafting a law  to introduce gay marriage, it isn't objection to say that it doesn't already exist.

>IE, just because we have control over a thing doesn’t—in my ontology—indicate that the concept of map/territory correspondence no longer applies

I didn't say it doesn't apply at all.  But theres a major difference between maps where the causal arrow goes t->m (science, reflection) and ones where it goes m->t (culture,construction)

*Once* you have constructed something according to a map (blueprint), you can study it scientifically, as anthropologists and scociologists do. But once something has been constructed, the norms of social scientists are that they just describe it. Social scientists don't have a norm that social constructs have to be rejected because they don't reflect  pre existing reality.

#### [>>>>>>>>] TAG · 1 karma · 2020-12-31 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=swRrvXf6go5NfGxjA
>Lots of physical things can have varied instantiations. EG “battery”. That in itself doesn’t seem like an important barrier.

If the question "is thing X an instance if type T" is answered by human concerns, then passive reflection of pre existing reality isn't the only game in town.

If type T is not a natural kind, then science is not the only game in town.

#### [-] abramdemski · 8 karma · 2020-12-12 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=8Zo85fhesFqaFwobQ
[As Said mentioned](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=T49M7fyizPhrLZMnL), this is original-Sequences-like quality.

#### [-] David Hornbein · 16 karma · 2020-12-17 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=QhNmc3uFLrLkKrX3b
As has been mentioned elsewhere, this is a crushingly well-argued piece of philosophy of language and its relation to reasoning. I will say this post strikes me as somewhat longer than it needs to be, but that's also my opinion on much of the Sequences, so it is at least traditional.

Also, this piece is historically significant because it played a big role in litigating a community social conflict (which is no less important for having been (being?) mostly below the surface), and set the stage for a lot of further discussion. I think it's very important that "write a nigh-irrefutable argument about philosophy of language, in order to strike at the heart of the substantive disagreement which provoked the social conflict" is an effective social move in this community. This is a very unusual feature for a community to have! Also it's an absolutely crucial feature for any community that aspires to the original mission of the Sequences. I don’t think it’s a coincidence that so much of this site’s best philosophy is motivated by efforts to shape social norms *via correct philosophical argument*. It lends a sharpness and clarity to the writing which is missing from a lot of the more abstract philosophizing.

#### [-] Zack_M_Davis [AUTHOR] · 4 karma · 2021-01-08 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=2KrJ2dQWitCmwzBgv
(Self-review.)

Argument for significance: [earlier comment](https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=i79Ju9vQJiEgRiJDj)

Sequel: ["Unnatural Categories Are Optimized for Deception"](https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception)

#### [-] Raemon · 18 karma · 2021-01-20 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=v59auE2KQPgwPmx7t
I've alluded to this in other comments, but I think worth spelling out more comprehensively here.

I think this post makes a few main points:

1.  Categories are not arbitrary. You might need different categories for different purposes, but categories are for helping you think about the things you care about, and a category that doesn't correspond to the territory will be less helpful for thinking and communciating.
2.  Some categories might *sort of* look like they correspond to something in reality, but they are gerrymandered in a way optimized for deception. 
3.  You might sometimes wish something were a member of a category that it isn't, and it is better to admit that so that you can actually communicate about the current state of reality.

I realize the three points cleave together pretty closely in the author's model, and make sense to think about in conjunction. But I think trying to introduce them all at once makes for more confusing reading.

I think the followup post [Unnatural Categories Are Optimized For Deception](https://www.lesswrong.com/posts/onwgTH6n8wxRSo2BJ/unnatural-categories-are-optimized-for-deception) does a pretty good job of spelling out the details of points #2 and #3. I think the current post does a good job at #1, a decent job at #2, but a fairly confused job at #3.

In particular, these 2.5 paragraphs feel like a meandering vagueblog. I know what point they're trying to make, but by trying to avoid the object level political disagreement, the post leaves me very confused about why I might be making these particular mistakes, or what to do about it.

> If what you want isn't currently true in reality, maybe there's some action you could take to make it *become* true. To search for that action, you're going to need accurate beliefs about what reality is *currently* like. To enlist the help of others in your planning, you're going to need precise terminology to *communicate* accurate beliefs about what reality is currently like. Even when—*especially* when—the current reality is inconvenient.
> 
> Even when [it hurts](https://www.lesswrong.com/posts/dHQkDNMhj692ayx78/avoiding-your-belief-s-real-weak-points).
> 
> (Oh, and if you're actually trying to optimize other people's models of the world, rather than the world itself—you could just *lie*, rather than playing clever category-gerrymandering mind games. It would be a lot simpler!)

(By contrast, the Unnatural Categories gives concrete real world examples that explain why you'd make this particular class of mistake. Somewhat oddly, it *does* use some politically charged examples, but I think it does a good job of laying out in as gearsy, not-too-politicized fashion. I think it actually could probably have gotten away with directly involving the original motivating example for the series)

If the point of Unnatural Categories is to *replace* this post, and this post is more like a first draft, then... seems potentially fine for Unnatural Categories to become the new canonical version of it and not worry overmuch about this one. 

But, I think there's a lot of distinct concepts here. Breaking them into multiple posts that deal with theseems worthwhile to me.

If this post is appearing in the 2019 Review as a standalone piece, I think it'd be clearer if it just cut the paragraphs I listed (and then reorganized itself slightly), rather than doing a rough, vague job of explaining them. When I got to like "even if it hurts" my reaction was "what? why would it hurt? what are you talking about? I think I know what the underlying political argument is and I'm *still* kinda confused about what's going on here."

I've also mentioned elsethread that I think the Bob the Vice President of Sorting example would be helpful to have earlier in the piece, to give a clearer example of when this whole problem might come up. But I realize people may vary in what pedagogy works best for them.

...

A sidepoint I notice while thinking about this: when I go back to the older sequence posts that this essay is referencing...

...well, they totally are vague and don't spell out what real world examples you might run into that would motivate the philosophical confusion. But they are also much shorter, usually focus on one idea at a time instead of three, and are intermixed with other posts that do lay out more of the motivating-examples.

#### [-] megasilverfist · 6 karma · 2024-11-05 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=qkqTu2buo245uC2eH
> So, there is a legitimate complaint here. It's true that sailors in the ancient world had a legitimate reason to want a word in their language whose [extension](/posts/HsznWM9A7NiuGsp28/extensions-and-intensions) was `{salmon, guppies, sharks, dolphins, ...}`. (And modern scholars writing a translation for present-day English speakers might even translate that word as *fish*, because [most](/posts/4mEsPHqcbRWxnaE5b/typicality-and-asymmetrical-similarity) members of that category are what we would call fish.) It indeed would not necessarily be helping the sailors to tell them that they need to exclude dolphins from the extension of that word, and instead include dolphins in the extension of their word for `{monkeys, squirrels, horses ...}`. Likewise, most modern biologists have little use for a word that groups dolphins and guppies together.

Ok, but salmon and guppies are *more* closely related to dolphins than sharks. Like I get where you are going with this, but "fish" is barely a natural category and it isn't obviously more of one than all descendants of the last common ancestor of the actinopterygians. Even if you limit it to marine descendants it still lets you predict bone vs cartilaginous skeletal system.

#### [>] Said Achmiz · 2 karma · 2025-06-01 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=dt943CozLDRthPm8D
I read your comment several times, and looked up [some Wikipedia articles](https://en.wikipedia.org/wiki/Gnathostomata) about this (fascinating!) taxonomic fact (which I appreciate you noting).

However, I don’t actually see how what you wrote disagrees with what Zack wrote? (Or was that not your intention?)

#### [>>] megasilverfist · 1 karma · 2025-06-06 · https://www.lesswrong.com/posts/esRZaPXSHgWzyB2NL/where-to-draw-the-boundaries?commentId=pLfcqMF5vMcWdd5qj
It has been long enough that I don't fully remember my thought process and may have just been looking for an excuse to talk about taxonomy. But I think I was pointing out that his implicit definition was also something 'most modern biologists have little use for'.

