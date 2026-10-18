Title: Does General Intelligence Deflate Standardized Effect Sizes of Cognitive Sex Differences?
Date: 2019-09-01 22:50
Category: commentary
Tags: statistics, Python, sex differences

Marco del Giudice[ref]I was telling friend of the blog [Tailcalled](https://surveyanon.wordpress.com/) the other week that we really need to start a Marco del Guidice Fan Club![/ref] points out[ref]Marco del Giudice, ["Measuring Sex Differences and Similarities"](https://marcodgdotnet.files.wordpress.com/2019/04/delgiudice_measuring_sex-differences-similarities_pre.pdf), §2.3.3, "Measurement Error and Other Artifacts"[/ref] that in the presence of measurement error, standardized effect size measures like [Cohen's _d_](https://rpsychologist.com/d3/cohend/) will underestimate the "true" effect size.

The effect size _d_ tries to quantify the difference between two distributions by reporting the difference between the distributions' means in _standardized_ units—units that have been scaled to take into account how "spread out" the data is. This gives us a common reference scale for _how big_ a given statistical difference is. Height is measured in meters, and "Agreeableness" in the [Big Five personality model](https://en.wikipedia.org/wiki/Big_Five_personality_traits) is an abstract construct that doesn't even have natural units, and yet there's still a meaningful sense in which we can say that the sex difference in height (_d_≈1.7) is "about three times larger" than the sex difference in Agreeableness (_d_≈0.5).[ref]Yanna J. Weisberg, Colin G. DeYoung, and Jacob B. Hirsh, ["Gender Differences in Personality across the Ten Aspects of the Big Five"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3149680/), Table 2[/ref]

Cohen's _d_ is computed as the difference in group means, divided by the square root of the pooled variance. Thus, holding _actual_ sex differences constant, more measurement error means more variance, which means smaller values of _d_. Here's some toy Python code illustrating this effect:[ref]Special thanks to Tailcalled for [catching a bug](http://unremediatedgender.space/source?p=Ultimately_Untrue_Thought.git;a=commitdiff;h=c5158d9a6feaa7ed5c770e6ace83d7e7ba2451e6) in the initially published version of this code.[/ref]

```python
from math import sqrt
from statistics import mean, variance

from numpy.random import normal, seed

# seed the random number generator for reproducibility of figures in later
# comments; commment this out to run a new experiment
seed(1)  # https://en.wikipedia.org/wiki/Nothing-up-my-sleeve_number

def cohens_d(X, Y):
    return (
        (mean(X) - mean(Y)) /
        sqrt(
            (len(X)*variance(X) + len(Y)*variance(Y)) /
            (len(X) + len(Y))
        )
    )

def population_with_error(μ, ε, n):
    def trait():
        return normal(μ, 1)
    def measurement_error():
        return normal(0, ε)
    return [trait() + measurement_error() for _ in range(n)]


# trait differs by 1 standard deviation
true_f = population_with_error(1, 0, 10000)
true_m = population_with_error(0, 0, 10000)

# as above, but with 0.5 standard units measurment error
measured_f = population_with_error(1, 0.5, 10000)
measured_m = population_with_error(0, 0.5, 10000)

true_d = cohens_d(true_f, true_m)
print(true_d)  # 1.0069180384313943 — d≈1.0, as expected!

naïve_d = cohens_d(measured_f, measured_m)
print(naïve_d)  # 0.9012430127962895 — deflated!
```

But doesn't a similar argument hold for non-error sources of variance that are "orthogonal" to the group difference? Suppose performance on some particular cognitive task can be modeled as the sum of the general intelligence factor (zero or negligible sex difference), and a special ability factor that does show sex differences.[ref]Arthur Jensen, _The g Factor_, Chapter 13: "Although no evidence was found for sex differences in the mean level of _g_ or in the variability of _g_, there is clear evidence of marked sex differences in group factors and in test specificity. Males, on average, excel on some factors; females on others. [...] But the best available evidence fails to show a sex difference in _g_."[/ref] Then, even with zero measurement error, _d_ would underestimate the difference between women and men _of the same general intelligence_—

```python
def performance(μ_g, σ_g, s, n):
    def general_ability():
        return normal(μ_g, σ_g)
    def special_ability():
        return normal(s, 1)
    return [general_ability() + special_ability() for _ in range(n)]

# ♀ one standard deviation better than ♂ at the special factor
population_f = performance(0, 1, 1, 10000)
population_m = performance(0, 1, 0, 10000)

# ... but suppose we control/match for general intelligence
matched_f = performance(0, 0, 1, 10000)
matched_m = performance(0, 0, 0, 10000)

population_d = cohens_d(population_f, population_m)
print(population_d)  # 0.7413662423265308 — deflated!

matched_d = cohens_d(matched_f, matched_m)
print(matched_d)  # 1.0346898918452228 — as you would expect
```
