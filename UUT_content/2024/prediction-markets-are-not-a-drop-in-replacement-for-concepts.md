Title: Prediction Markets Are Not a Drop-In Replacement for Concepts
Date: 2024-12-21 09:35
Category: commentary
Tags: Eliezer Yudkowsky, literary criticism, worldbuilding, prediction markets

In ["Comment on a Scene from _Planecrash_: 'Crisis of Faith'"](http://unremediatedgender.space/2022/Jun/comment-on-a-scene-from-planecrash-crisis-of-faith/), I criticized a scene in which Keltham (a [magical universe-teleportation victim](https://en.wikipedia.org/wiki/Isekai) from an alternate Earth called dath ilan) plays dumb about why a pre-industrial Society would only choose males for military conscription.

_Planecrash_ coauthor [Eliezer Yudkowsky comments](http://unremediatedgender.space/2022/Jun/comment-on-a-scene-from-planecrash-crisis-of-faith/#isso-583): 

> Keltham wouldn't be averse to suggesting that there be prediction markets about military performance, not just predictions based on height. If there's more information to be gained from measuring biological sex than by just measuring height, it'll show up in the military prediction markets. But Keltham knows the uneducated soul to whom he is speaking, does not know what a prediction market is.
>
> And after you've added in prediction markets to actually get all of the information that anybody has, what remains to be gained by creating a law that asymmetrically treats different sapient beings in a way based not on predicted outcomes?

Good question.[^good-question] I'd like to generalize it: in the absence of a reason why "creating a law" and "sapient beings" would change the answer, we can ask: when making a decision about some entities X<sub>i</sub>, after you've added in prediction markets to get all of the information that anybody has, what remains to be gained by using a decision procedure P that asymmetrically treats the X<sub>i</sub> in a way based not on predicted outcomes?

[^good-question]: Not really. I'm being polite.

The answer is: nothing—with two caveats having to do with how the power of prediction markets relies on their being agnostic about how traders make decisions: we assume that whatever the winning answer is, greedy traders have an incentive to figure it out.

Nothing is gained—_if_ you already happen to have sufficiently liquid prediction markets covering all observables relevant to the decisions you need to make. This is logistically nontrivial, and almost certainly much more computationally intensive. (If there are a hundred traders in your market, each of them using their own decision procedure which is on average as expensive as P, then delegating the decision to the market costs Society a hundred times as much as just using P once yourself.)

Nothing is gained—_but_ this can't be an argument against P being a good decision procedure, as the reason we can assume that the market will never underperform P is _because_ traders are free to use P themselves if it happens to be a good procedure. (It would be lying to claim that Society doesn't need to compute P because it has prediction markets, if, "under the hood", the traders in the market are in fact computing P all the time.)

To figure out whether these caveats matter, we can imagine some concrete scenarios.

------

(Okay, this one is a little bit silly, but it's illustrative.)

Imagine being a programmer needing to implement a sorting algorithm: code that takes a list of numbers and rearranges the list to be ordered smallest to largest. You're thinking about using [quicksort](https://en.wikipedia.org/wiki/Quicksort), which involves recursively designating an arbitrary "pivot" element and then partitioning the list into two sublists that are less than and greater than (or equal to) the pivot, respectively.

Your teammate Albert objects to the idea of moving elements based on whether they're greater or less than an arbitrary pivot, rather than whether it will achieve the goal of the list being sorted. "Why are you writing code that asymmetrically treats different numbers differently in a way not based on predicted outcomes?" he asks.

"What would you suggest?" you ask, regretting the question almost as soon as you've finished saying it.

"Well, we have a library that interacts with the [Manifold Markets API](https://docs.manifold.markets/api) ..."

```python
from math import log2
import prediction_markets


def prediction_market_sort(my_list):
    n = len(my_list)
    op_count = 0
    op_budget = n * log2(n)
    is_sorted_market = prediction_markets.create(
        "Is the list sorted?", dynamic_data=my_list
    )

    markets_to_resolve = []

    while is_sorted_market.probability < 0.95:
        next_comparison_markets = {
            (i, j): prediction_markets.create(
                f"Will this list be sorted with no more than {op_budget} comparisons, if the"
                f"next comparison is between indices {i} and {j}?",
                static_data=my_list,
            )
            for i in range(n)
            for j in range(i+1, n)
            if i != j
        }

        next_comparison = max(
            next_comparison_markets.items(), key=lambda m: m[1].probability
        )[0]

        for comparison, market in next_comparison_markets.items():
            if comparison != next_comparison:
                market.cancel()
            else:
                markets_to_resolve.append(market)

        i, j = next_comparison

        should_swap_market = prediction_markets.create(
            f"Will this list be sorted with no more than {op_budget} comparisons if "
            f"the next operation is to swap the elements at indices {i} and {j}?",
            static_data=my_list,
        )
        if should_swap_market.probability > 0.5:
            temp = my_list[i]
            my_list[i] = my_list[j]
            my_list[j] = temp

            markets_to_resolve.append(should_swap_market)
        else:
            should_swap_market.cancel()

        op_count += 1
        op_budget -= 1

    is_sorted_market.resolve(True)

    for market in markets_to_resolve:
        market.resolve(op_count <= op_budget)

    return my_list
```

"No," you say.

"What do you mean, No? Is there a bug in the code? If not, then it should work, right?"

"In _principle_, I suppose, but ..." You're at a loss for words.

"Then what's the problem?" says Albert. "Surely you don't think you're smarter than a prediction market?" he scoffs.

You open a prediction market asking about the company's profits next quarter conditional on Albert being fired.

-----

Or suppose you've been looking forward to going out to dinner with your friend Barbara at your favorite restaurant, Vinnie's. Unfortunately, Vinnie's is closed. You pull out your phone to look for alternatives. "OK Google, Italian restaurants near me."

Barbara objects. "Stop! What are you doing?"

"Well," you explain, "If we can't go to the exact restaurant we were expecting to, we can probably find something similar."

"Then start a Manifold market asking which restaurants we'll enjoy! If there's more information to be gained by classifying cuisine by national origin than by just looking at the specific dishes on the menu, it'll show up in the culinary prediction markets. And after you've added in prediction markets to actually get all of the information that anybody has, what remains to be gained by choosing where to eat in a way that asymmetrically treats different restaurants in a way based not on predicted outcomes?"

----

I wrote this restaurant-choice scenario as an illustrative example for this blog post, but I want you to imagine how you would react if someone _actually behaved that way in real life_: stopped you when you searched for Italian restaurants and insisted you start a prediction market instead. That would be pretty weird, right?

It's not that there's anything particularly wrong with the idea of using prediction markets to get restaurant suggestions. I can easily believe that you might get some good suggestions that way, even in a sparsely-traded play-money market on Earth, _i.e._, the real world. (In a similar vein, Yudkowsky has [a "What books will I enjoy reading?" market](https://manifold.markets/EliezerYudkowsky/what-book-will-i-enjoy-reading).)

The weird part is the implication that the form of reasoning you would use to make a decision in the absence of a prediction market can be dismissed as "a way based not on predicted outcomes" and regarded as obviated by the existence of the market. I don't think anyone really believes this, as contrasted to [believing they believe](https://www.lesswrong.com/posts/CqyJzDZWvGhhFJ7dY/belief-in-belief) it in order to ease the cognitive dissonance of trying to simultaneously adhere to the religious commitments of both _Less Wrong_ "rationalism" and American progressivism.

The `prediction_market_sort` code doesn't obviate standard sorting algorithms like quicksort, because if you run `prediction_market_sort`, the first thing the traders in the market are going to do is run a standard sorting algorithm like quicksort to decide which comparisons to bet on.

The restaurant-enjoyment market doesn't obviate the concept of Italian food, because if you post a market for "Where should we go for dinner given that Vinnie's is closed?", the first thing traders are going to do is search for "Italian restaurants near [market author's location]"—not because they're fools who think that "Italian food" is somehow ontologically fundamental and eternal, but because there contingently do happen to be [approximate conditional independence relationships](https://www.readthesequences.com/Conditional-Independence-And-Naive-Bayes) between the features of meals served by different restaurants. A decision made on the basis of a [statistical compression](https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length) of meal features is based on predicted outcomes insofar as and to the extent that meal features predict outcomes.

To be sure, there are all sorts of nuances and caveats that one could go into here about exactly when and why categorization works or fails as a cognitive algorithm—how categories are sometimes [used for coordination](https://www.lesswrong.com/posts/edEXi4SpkXfvaX42j/schelling-categories-and-simple-membership-tests) [and not](http://unremediatedgender.space/2019/Oct/self-identity-is-a-schelling-point/) [just predictions](http://unremediatedgender.space/2019/Dec/more-schelling/), how categories should [change when the distribution of data in the world changes](https://www.lesswrong.com/posts/WikzbCsFjpLTRQmXn/declustering-reclustering-and-filling-in-thingspace) (_e.g._, if [fusion cuisines](https://en.wikipedia.org/wiki/Fusion_cuisine) become popular), whether categories might perversely distort the territory to fit the map via self-fulfilling prophecies[^self-fulfilling] (_e.g._, if entrepreneurs only open restaurants in established ethnic categories because that's what customers are used to, thereby stifling culinary innovation) ...

[^self-fulfilling]: Although this is _also_ a potential problem for prediction markets [and other cognitive systems](https://www.lesswrong.com/posts/SwcyMEgLyd4C3Dern/the-parable-of-predict-o-matic).

But, bluntly? The kind of person who asks what use there is in "creating a law that asymmetrically treats different sapient beings in a way based not on predicted outcomes" is not interested in the nuances and caveats. (I know because [I used to be this kind of person](/2021/May/sexual-dimorphism-in-the-sequences-in-relation-to-my-gender-problems/#antisexism).) It's not an honest question that expects an answer; it's a rhetorical question asked in the hope that the respondent doesn't have one.[^isolated-demands-for-rigor]

[^isolated-demands-for-rigor]: Which is usually a good bet in the service of the goal of suppressing anti-egalitarian memes. I've specialized in patiently answering [isolated demands for rigor](https://slatestarcodex.com/2014/08/14/beware-isolated-demands-for-rigor/), but most people aren't philosophically sophisticated enough to do that, and the ones that are have competing demands on their time.

"If there's more information to be gained from measuring biological sex than by just measuring height, it'll show up in the military prediction markets," Yudkowsky writes. I agree, of course, that that sentence [is literally true](https://www.lesswrong.com/posts/MN4NRkMw7ggt9587K/firming-up-not-lying-around-its-edge-cases-is-less-broadly), but the conditional mood implies such a bizarre prior. "If"? "Just measuring _height_"? Are we pretending to be uncertain about whether a troop of 5'6" males (15th percentile) or 5'6" females (80th percentile) would prevail in high medieval warfare? (Yes, _on average_—but outlier groups are exponentially[^exponentially] rarer than outlier individuals!) Does anyone want to bet on this?

[^exponentially]: In the size of the group.

-----

Perhaps at this point the advocate of prediction markets will complain that I'm the one performatively missing the point: the claim isn't that sex is useless for predicting military performance or that restaurant category is useless for predicting meal enjoyment; the claim is that prediction markets can do better by incorporating all other sources of information not encapsulated in a crude, lossy categorization only tangentially relevant to the decision being made. Some men would make terrible soldiers. If the only other Italian place in town is lousy, then you and Barbara obviously want to go somewhere else. Therefore, use prediction markets to pick the actually best soldiers/restaurant, don't just pick the ones with a penis or from Italy. Right?

But what's at issue isn't whether making decisions _solely_ on the basis of category membership is a good idea, but whether institutions should be able to take category membership into account as a matter of explicit policy (rather than only implicitly via the black box of a prediction market, whose traders are allowed to notice things that the policy isn't).

Real-world militaries that practice conscription _don't_ just take males indiscriminately with no other requirements than having a Y chromosome, because that would be crazy. The draft board [does](https://en.wikipedia.org/wiki/Selective_Service_System#Classifications) administer fitness tests and psych evals, consider relevant skills, _&c_. (Similarly, real-world diners craving Italian food also take Yelp ratings into account.) But one of the features real-world militaries _do_ consider is sex, because in the real world, the conjunction of the effect sizes of the group differences in various job-relevant traits, cost of individual trait measurements, and error in individual trait measurements,[^measurement-error] makes that an effective policy,[^empirically-contingent] and real-world militaries trying to win wars don't care about running afoul of a principle of not asymmetrically treating different sapient beings in a way (allegedly) "based not on predicted outcomes." For example, [Israel drafts women](https://en.wikipedia.org/wiki/Women_in_the_Israel_Defense_Forces), but [doesn't use them in all combat roles](https://www.ynetnews.com/articles/0,7340,L-5089566,00.html)—and correspondingly, [the קבוצת איכות ("quality group") score used for role placement includes an interview portion for men only, and weights education more highly for women](https://garinmahal.com/kaba-dapar). There are a few mixed-sex battalions, like [the 33rd "Caracal"](https://en.wikipedia.org/wiki/Caracal_Battalion), named after [a species of cat with low sexual dimorphism](https://en.wikipedia.org/wiki/Caracal), but it's an exception rather than the norm.

[^measurement-error]: Measurement error matters because, in Bayesian terms, the less reliable your individual measurements are, the more your posterior depends on your priors rather than the evidence of the measurements. 

[^empirically-contingent]: Obviously, this is empirically contingent: you could get a different answer in a world with different effect sizes and different measurement affordances, but [a world with different stuff in it would admit different categories to describe it](http://unremediatedgender.space/2023/Dec/beyond-the-binary/). "That wouldn't work against a different data distribution" isn't a good argument against the use of some statistical model, because [no model would work against all possible distributions](https://en.wikipedia.org/wiki/No_free_lunch_theorem).

If Keltham's objection to Osiriani patriarchy (which restricts women's education and right to hold property) also condemns real-world Israel (which doesn't), it would appear that something has gone wrong with his reasoning. If the problem is that excluding women from education and property ownership is oppressive and not justified on the empirical merits, Keltham should expect to make that case on the empirical merits: that women's economic liberty works great on dath ilan, and the Osiriani don't seem to be a different species for which the empirical merits would be different.

That's not what we see in the text. Keltham challenges a native to explain things that would go wrong if foreigners imposed a strict Equal Rights Amendment, and when presented with a sensible example (military conscription), rather than saying, "okay, I can see how that one makes pragmatic sense, but that doesn't explain or justify the property thing", he persistently refuses to acknowledge the point. "[H]ow is [unusually strong women being drafted] more terrible than strong men being forced to join an army for less than their self-set wage for that?" [he asks](https://www.projectlawful.com/replies/1817425#reply-1817425), and when he receives sensible answers to _that_ (the women might get taken advantage of sexually, which would have lasting consequences for them), he [objects that truthspell-enabled governance would prevent rapes, and patronizingly wonders whether the Osiriani are aware of the human gestation period](https://www.projectlawful.com/replies/1817432#reply-1817432).

[Word of God](https://tvtropes.org/pmwiki/pmwiki.php/Main/WordOfGod) claims that "Keltham isn't proposing to actually enforce that prohibition [of laws that mention sex] on Osirion, he's trying to figure out _what the laws are trying to do and why_".[^word-of-god] I find this hard to square with the [nearest-unblocked strategy](https://arbital.com/p/nearest_unblocked/) behavior Keltham is displaying in this scene: when presented with a reason for why sexism has good outcomes in some domain, Keltham immediately starts searching for ways to get the good outcomes without the sexism, even at greater expense. (You don't need to buy truthspells for your Title IX compliance officers if you don't have Title IX compliance officers.) However Yudkowsky might "explain" it _post hoc_ in response to criticism, this is the behavior of someone trying to minimize sexism while being sensitive to outcome-based pragmatic constraints, rather than someone trying to optimize performance outcomes without particularly caring whether the means happen to be sexist.

[^word-of-god]: [Eliezerfic Discord server, #dath-ilan channel, 12 June 2022](/images/yudkowsky-keltham_isnt_proposing.png)

Which, to be clear, might be the right way to behave, if those are your true values! (I'm a religiously devout American, too. This is a _heresy_ blog, not an _apostate_ blog.) It's just that one would hope for the literary tradition of rationalist fiction to do a better job of distinguishing between contingent values and convergent strategies. Connoisseurs of diamond-hard science fiction can't help but cringe at the writers' lack of imagination when the heroes of your standard science fantasy space opera come across a planet of supposed aliens who [just happen to look exactly like humans and have produced a verbatim copy of the Constitution of the United States](https://memory-alpha.fandom.com/wiki/The_Omega_Glory_(episode)). It's not out of disdain for the Constitution, which is a fine document,[^fine-document] but out of respect for the complexity of the real physical universe in all its rawness, that ["the beauty that jumps out of one box, is not jumping out of _all_ boxes"](https://www.lesswrong.com/posts/GNnHHmm8EzePmKzPk/value-is-fragile), that values have antecedents. Deluding yourself into thinking that your home culture's sacred traditions fall naturally out of Bayesian decision theory does a disservice to both.

[^fine-document]: From an American perspective, natch.

As I mentioned in ["Comment on a Scene"](http://unremediatedgender.space/2022/Jun/comment-on-a-scene-from-planecrash-crisis-of-faith/), anti-discrimination policy makes sense as game theory: [if you don't trust decisionmakers not to misconstrue group differences in a way that benefits them, forcing them to behave as if all groups were equal is the obvious Schelling point for preventing exploitation](http://unremediatedgender.space/2020/Apr/book-review-human-diversity/#schelling-point-for-preventing-group-conflicts): the government can't oppress people on the basis of sex if the government isn't allowed to see sex. (American progressivism's elevation of antisexism and antiracism to terminal values is probably a reification of this strategy, rather than something that would make sense in the absence of the political problem and an instinct to reify contingent political strategies as terminal values.)

One could try to construe Keltham's line of questioning as deliberately trying to play the anti-oppression Schelling point strategy against Osirion: it's not that Keltham is denying that predictively useful categories are also useful for making decisions; he just doesn't trust Osirion's patriarchal culture to do that fairly and is eager to explain how good decisions can be recovered in terms of lower-level features at some extra expense.

I just don't think the balance of textual evidence supports this interpretation. If Keltham's "dreadful meddling foreigner" thought experiment is only meant to put pressure on Osirion's patriarchal ideology without the implication that dath ilan thinks Governance should be demographic-category-blind as a matter of principle, I would expect the text to clarify this somewhere—and the case that Keltham doesn't get that Bayesianism is not on the meddling foreigner's side is strengthened by the case that Yudkowsky doesn't get it. The effectiveness of the Israel Defense Forces might or might not be improved by incorporating prediction markets for personnel selection, but the notion that the current קבוצת איכות system is obviously foolish for "asymmetrically treat[ing] different sapient beings in a way based not on predicted outcomes" is both hard to take seriously and inconsistent with the general portrayal of Civilization in the dath ilan mythos.

Almost everywhere else in the dath ilan mythos that dath ilan is compared to Earth (_i.e._, the real world) or Golarion, the comparison is unflattering; we're supposed to believe that dath ilan is a superior civilization, a utopia of reason where average intelligence is 2.6 standard deviations higher, where everyone is trained in Bayesian reasoning from childhood. One of the rare places in canon that dath ilan is depicted as not having already thought of something good and useful in the real world is in [the April Fool's Day confession](https://yudkowsky.tumblr.com/post/81447230971/my-april-fools-day-confession), when [NGDP targeting](https://en.wikipedia.org/wiki/Nominal_income_target) is identified as a clever and characteristically un–dath ilani hack. Dath ilan is accustomed to solving coordination problems by the effort of "serious people [...] get[ting] together and try[ing] not to have them be so bad": the mode of thinking that would lead one to propose automatically canceling out the sticky wage effect by printing more money to keep spending constant is alien to them.

Anti-discrimination norms are like NGDP targeting: prohibiting certain probabilistic inferences in order to cancel out widespread irrational bigotry is similar to printing money to cancel out a widespread irrational tendency to fire workers instead of lowering nominal wages in that it's not something you would think of in a world where people are just doing decision Bayesian decision theory—and it's not something you would _portray as superior_ if you came from a world that prides itself on just doing Bayesian decision theory and were trying to enlighten the natives of a strange and primitive culture. If you think prediction markets render this moot, then I have an amazing new sorting algorithm that may interest you ...
