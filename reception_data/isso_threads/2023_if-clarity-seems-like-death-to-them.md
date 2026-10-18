Post: http://unremediatedgender.space/2023/Dec/if-clarity-seems-like-death-to-them/
Fetched: 2026-10-15 (public Isso API)
Comments: 5 top-level

#### [-] tailcalled · 0 likes · 2023-12-30 · http://unremediatedgender.space/2023/Dec/if-clarity-seems-like-death-to-them/#isso-561
> A two-dimensional political map tells you which areas of the Earth's surface are under the jurisdiction of which government. In contrast, category "boundaries" tell you which regions of very high-dimensional configuration space correspond to a word/concept, which is useful because that structure can be used to make probabilistic inferences. You can use your observations of some aspects of an entity (some of the coordinates of a point in configuration space) to infer category-membership, and then use category membership to make predictions about aspects that you haven't yet observed.


> But the trick only works to the extent that the category is a regular, non-squiggly region of configuration space: if you know that egg-shaped objects tend to be blue, and you see a black-and-white photo of an egg-shaped object, you can get close to picking out its color on a color wheel. But if egg-shaped objects tend to blue or green or red or gray, you wouldn't know where to point to on the color wheel.


> The analogous algorithm applied to national borders on a political map would be to observe the longitude of a place, use that to guess what country the place is in, and then use the country to guess the latitude—which isn't typically what people do with maps. Category "boundaries" and national borders might both be illustrated similarly in a two-dimensional diagram, but philosophically, they're different entities. The fact that Scott Alexander was appealing to national borders to defend gerrymandered categories, suggested that he didn't understand this.

I would add that it probably is relatively easy to get squiggly national borders from a clustering of variables associated with a location, you just have to pick the right variables. Instead of latitude and longitude, consider variables such as:

If you were stabbed or robbed here, which organization should you report it to?
And who decides what rules there are to report to this organization?
What language is spoken here?
What forces prevent most states from grabbing the resources here?
What kind of money can I use to pay with here?
What phone companies provide the cheapest coverage here?
...


> I still had some deeper philosophical problems to resolve, though. If squiggly categories were less useful for inference, why would someone want a squiggly category boundary? Someone who said, "Ah, but I assign higher utility to doing it this way" had to be messing with you. Squiggly boundaries were less useful for inference; the only reason you would realistically want to use them would be to commit fraud, to pass off pyrite as gold by redefining the word "gold".


> That was my intuition. To formalize it, I wanted some sensible numerical quantity that would be maximized by using "nice" categories and get trashed by gerrymandering. Mutual information was the obvious first guess, but that wasn't it, because mutual information lacks a "topology", a notion of "closeness" that would make some false predictions better than others by virtue of being "close".


> Suppose the outcome space of X is {H, T} and the outcome space of Y is {1, 2, 3, 4, 5, 6, 7, 8}. I wanted to say that if observing X=H concentrates Y's probability mass on {1, 2, 3}, that's more useful than if it concentrates Y on {1, 5, 8}. But that would require the numerals in Y to be numbers rather than opaque labels; as far as elementary information theory was concerned, mapping eight states to three states reduced the entropy from log2 8 = 3 to log2 3 ≈ 1.58 no matter which three states they were.


> How could I make this rigorous? Did I want to be talking about the variance of my features conditional on category membership? Was "connectedness" what I wanted, or was it only important because it cut down the number of possibilities? (There are 8!/(6!2!) = 28 ways to choose two elements from {1..8}, but only 7 ways to choose two contiguous elements.) I thought connectedness was intrinsically important, because we didn't just want few things, we wanted things that are similar enough to make similar decisions about.


> I put the question to a few friends in July 2020 (Subject: "rubber duck philosophy"), and Jessica said that my identification of the variance as the key quantity sounded right: it amounted to the expected squared error of someone trying to guess the values of the features given the category. It was okay that this wasn't a purely information-theoretic criterion, because for problems involving guessing a numeric quantity, bits that get you closer to the right answer were more valuable than bits that didn't.

Variance is a commonly chosen metric to optimize for these sorts of algorithms yes, for essentially this reason. That said, most of the interesting discussion is in the exact nature of the Y, rather than in the metric used to measure it. When you are creating a classification system X which summarizes lots of noisy indicators Y₁, Y₂, ..., the algorithms that optimize for information (e.g. Latent Class Analysis, Latent Dirichlet Allocation, ...) usually seek the minimal amount of information that makes the indicators independent. When the indicators are noisy, the information in low-variance causes gets destroyed by the noise, so what remains to generate dependencies is the information in high-variance factors, and therefore seeking minimal shared information becomes equivalent to explaining maximum correlations. (And correlations are squared error based.) It's a standard empirical finding that different latent variable methods yield essentially the same latents when applied to essentially the same data.

> And yet, somehow, "have accurate beliefs" seemed more fundamental than other convergent instrumental subgoals like "seek power and resources". Could this be made precise? As a stab in the dark, was it possible that the theorems on the ubiquity of power-seeking might generalize to a similar conclusion about "accuracy-seeking"? If it didn't, the reason why it didn't might explain why accuracy seemed more fundamental.

The only robust way to avoid wireheading is that instead of taking actions which maximize your reward (or your expectation of your utility, or ...), you should 1) have a world-model, 2) have a pointer into the value in the world-model, 3) pick actions which your model thinks increases the-thing-pointed-to-by-the-value-pointed and then execute those actions in reality.

This would prevent yourself from e.g. modifying your brain to believe that you had a high value, because if ahead of time you ask your world-model "would this lead to a lot of value?", the world model can answer "no, it would lead to you falsely believing you had a lot of value".

This system is usually built into utility maximization models since in those models the utility function can be any random variable, but it is not usually built into reinforcement learning systems since those systems often assume value to be a function of observations.

#### [-] KartoffelElf · 0 likes · 2023-12-31 · http://unremediatedgender.space/2023/Dec/if-clarity-seems-like-death-to-them/#isso-562
> On this point, it may be instructive to note that a 2023 survey found that only 60% of the UK public knew that "trans women" were born male.

That seems more like confusion about terminology than facts, i.e. being unclear about whether "trans X" refers to where they started or where they're aiming for.

#### [-] KartoffelElf · 0 likes · 2023-12-31 · http://unremediatedgender.space/2023/Dec/if-clarity-seems-like-death-to-them/#isso-563
> I think gay men and lesbians are different things that need to be studied separately.

Clarification question: Do you mean this in the trivial sense that homosexual males and homosexual females are different for the trivial reason that males and females are different, or in the sense that you have some reason to expect the causes of male and female homosexuality to be substantially non-symmetrical?

#### [-] KartoffelElf · 0 likes · 2024-01-02 · http://unremediatedgender.space/2023/Dec/if-clarity-seems-like-death-to-them/#isso-564
I'll also add that while I agree that Yudkowsky's prevarication is annoying, I can at least understand if he feels like he's stuck between a rock and a hard place: being too tolerant of bad reasoning damages the group's ability to reason but being too nice to heretics and heresy damages the group's reputation (and therefore ability to interact with the rest of the world). I'm not sure what I'd do in that position.

#### [-] FoxLisk · 0 likes · 2024-01-02 · http://unremediatedgender.space/2023/Dec/if-clarity-seems-like-death-to-them/#isso-565
> not being at war actually made it emotionally easier to do clarity-creation writing

Note that this is in direct tension with the discussion about how commenters shouldn't have to worry about each others' feelings, etc; i.e. you link with praise to a comment that says commenters should "[a]bsolutely not ... consider each other’s feelings"

you can of course bite that bullet, and say that commenters shouldn't consider each others' feelings even though it would produce more clarity-creation writing to do so. Or I suppose you could argue that your experience of "being at war" is qualitatively different in some way from the pressures of feeling attacked in a comment chain. But it seems relevant to me.


> What does the word "collaborative" mean in the phrase "collaborative truthseeking"?

If we're being charitable: "truthseeking" can be a solo activity (e.g. dissecting a bug to learn about its organs). "Collaborative" truthseeking is the process of multiple people working toward seeking truth together; i.e. when I post a comment trying to aid your search for the truth. You could imagine me taking other actions instead: not posting a comment (in which case you're still truth seeking, but I'm not collaborating); or posting a misleading comment (in which case you're truthseeking but I'm hampering it).

But more realistically, you need unique (ish) 2+ word phrases to serve as identifiers. c.f. "Social Distancing", "Lived Experience", "he/him".  In this sense, it serves mostly to mean "commenting on a rationalist blog," with perhaps some side benefit of reminding people who hear it that they are supposed to follow certain norms that are at least de jure related to Truth.

Anyway, this was a gripping read. I love the foreshadowing on Vassar. Can't wait to find out what happens next!
