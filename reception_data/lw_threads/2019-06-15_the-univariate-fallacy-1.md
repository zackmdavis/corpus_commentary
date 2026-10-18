Title: The Univariate Fallacy
LessWrong-URL: https://www.lesswrong.com/posts/cu7YY7WdgJBs3DpmJ/the-univariate-fallacy-1
Posted: 2019-06-15
Fetched: 2026-10-13 (LessWrong GraphQL API; rendered by tools/render_lw_threads.py)
Comments: 15 (commentCount field: 15)

#### [-] Zack_M_Davis [AUTHOR] · 2 karma · 2019-06-15 · https://www.lesswrong.com/posts/cu7YY7WdgJBs3DpmJ/the-univariate-fallacy-1?commentId=LzuEMSgN5Fh2qyrE5
(I wonder how a "-1" ended up in the canonical URL [slug](https://en.wikipedia.org/wiki/Clean_URL#Slug) (/cu7YY7WdgJBs3DpmJ/the-univariate-fallacy-1)?  Did someone else have a draft of the same name, and the system wants unique slugs??)

#### [>] Pattern · 3 karma · 2019-06-16 · https://www.lesswrong.com/posts/cu7YY7WdgJBs3DpmJ/the-univariate-fallacy-1?commentId=tjXMn46xJYwJihmoF
Perhaps it anticipates that you will write a sequel.

#### [-] Said Achmiz · 6 karma · 2019-06-15 · https://www.lesswrong.com/posts/cu7YY7WdgJBs3DpmJ/the-univariate-fallacy-1?commentId=o83q7orxDXosR6Dk9
FYI, one of the symbols in this post is not rendering properly. It appears to be [U+20D7 COMBINING RIGHT ARROW ABOVE](http://www.fileformat.info/info/unicode/char/20d7/index.htm) (appearing right after the ‘x’ characters) but, at least on this machine (Mac OS 10.11.6, Chrome 74.0.3729.131), it renders as a box:

![Screenshot of character incorrectly rendered as a box](https://dl.dropboxusercontent.com/s/ripi2wdov1v84ke/Screenshot%202019-06-15%2019.18.16.png?dl=0)

It is probably a good idea to use LaTeX to encode such symbols.

**UPDATE:** It does work properly in Firefox 67.0.2 (on the same machine):

![Screenshot of character rendered correctly as right arrow above](https://dl.dropboxusercontent.com/s/0iib7g9v8ori02k/Screenshot%202019-06-15%2019.21.53.png?dl=0)

#### [>] Zack_M_Davis [AUTHOR] · 4 karma · 2019-06-16 · https://www.lesswrong.com/posts/cu7YY7WdgJBs3DpmJ/the-univariate-fallacy-1?commentId=chQcjQEqMMuKxGddw
Thanks for the bug report; I edited the post to use LaTeX `\vec{x}`. (The combining arrow worked for me on Firefox 67.0.1 and was kind-of-ugly-but-definitely-renders on Chromium 74.0.3729.169, on Xubuntu 16.04)

> It is probably a good idea to use LaTeX to encode such symbols.

I've been doing this thing where I prefer to use "plain" Unicode where possible (where, _e.g._, the subscript in "_x₁_" is [0x2081 SUBSCRIPT ONE](https://www.fileformat.info/info/unicode/char/2081/index.htm)) and only resort to "fancy" (and therefore suspicious) LaTeX when I really need it, but the reported Chrome-on-macOS behavior does slightly alter my perception of "really need it."

#### [>>] Said Achmiz · 6 karma · 2019-06-16 · https://www.lesswrong.com/posts/cu7YY7WdgJBs3DpmJ/the-univariate-fallacy-1?commentId=es7CDJKiY3SPpXQS4
> I’ve been doing this thing where I prefer to use “plain” Unicode where possible

I *entirely* sympathize with this preference!

Unfortunately, proper rendering of Unicode depends on the availability of the requisite characters in the fallback fonts available in a user’s OS/client combination (which vary unpredictably). This means that the more exotic code points cannot be relied on to properly render with acceptable consistency.

Now, that having been said, and availability and proper rendering aside, I cannot endorse your use of such code points as U+2081 SUBSCRIPT ONE. Such typographic features as subscripts ought properly to be encoded via OpenType metadata[^1], not via Unicode (and indeed I consider the existence of these code points to be a necessary evil at best, and possibly just a bad idea). In the case where OpenType metadata editing[^2] is not available, the proper approach is either LaTeX, or “low-tech” approximations such as brackets.

[^1]: Which, in turn, ought to be generated programmatically from, e.g., HTML markup (or even higher-level markup languages like Markdown or wiki markup), rather than inserted manually. This is because the output generation code must be able to decide whether to use OpenType metadata or whether to instead use lower-level approaches like the HTML+CSS layout system, etc., depending on the capabilities of the output medium in any given case.

[^2]: That is, the editing of the requisite markup that will generate the proper OpenType metadata; see previous footnote.

#### [-] John_Maxwell · 12 karma · 2019-06-16 · https://www.lesswrong.com/posts/cu7YY7WdgJBs3DpmJ/the-univariate-fallacy-1?commentId=EFPZs2jQJpiSqycdK
Good post.  Some feedback:

* I think you can replace the first instance of "are statistically independent" with "are statistically independent and identically distributed" & improve clarity.

* IMO, your argument needs work if you want it to be more than an intuition pump.  If the question is the existence or nonexistence of particular clusters, you are essentially assuming what you need to prove in this post.  Plus, the existence or nonexistence of clusters is a "choice of ontology" question which doesn't necessarily have a single correct answer.

* You're also fuzzing things by talking about discrete distributions here, then linking to Eliezer's discussion of continuous latent variables ("intelligence") without noting the difference.  And: If a number of characteristics have been observed to co-vary, this isn't sufficient evidence for any particular causal mechanism.  Correlation isn't causation.  As I pointed out in [this essay](https://medium.com/@pwgen/friendly-ai-through-ontology-autogeneration-5d375bf85922), it's possible there's some latent factor like the ease of obtaining calories in an organism's environment which explains interspecies intelligence differences but doesn't say anything about the "intelligence" of software.

#### [>] Zack_M_Davis [AUTHOR] · 2 karma · 2019-06-16 · https://www.lesswrong.com/posts/cu7YY7WdgJBs3DpmJ/the-univariate-fallacy-1?commentId=pRduKmkaA7BGemx9r
> replace the first instance of "are statistically independent" with "are statistically independent and identically distributed"

Done, thanks!

> talking about discrete distributions here, then linking to Eliezer's discussion of continuous latent variables ("intelligence") without noting the difference

The difference doesn't seem relevant to the narrow point I'm trying to make? I was originally going to use multivariate normal distributions with different means, but then decided to just make up "peaked" discrete distributions in order to keep the arithmetic simple.

#### [>] Lignisse · 1 karma · 2019-06-18 · https://www.lesswrong.com/posts/cu7YY7WdgJBs3DpmJ/the-univariate-fallacy-1?commentId=GMMhkc3DXjZcdTvuT
I agree with your other two points (mostly - I don't feel that the distinction between discrete and continuous variables is important for Zack's argument so it seems fine to gloss over it) but I disagree with the first.

In order to be able to simply multiply likelihood ratios, the sufficient fact is that they're statistically independent. In this toy model, they also happen to be identically distributed, but I think it's clear from context that Zack would like to apply his argument to a variety of situations where the different dimensions have different distributions. You're suggesting replacing "X, therefore Z" with "X and Y, therefore Z", when in fact X->Z, and it is not the case that Y->Z.

#### [-] DavidHolmes · 9 karma · 2019-06-17 · https://www.lesswrong.com/posts/cu7YY7WdgJBs3DpmJ/the-univariate-fallacy-1?commentId=Yeq27hH6tBCHjmrwy
Hi Zack,

Can you clarify something? In the picture you draw, there is a codimension-1 linear subspace separating the parameter space into two halves, with all red points to one side, and all blue points to the other. Projecting onto any 1-dimensional subspace orthogonal to this (there is a unique one through the origin) will thus yield a `variable' which cleanly separates the two points into the red and blue categories. So in the illustrated example, it looks just like a problem of bad coordinate choice.

On the other hand, one can easily have much more pathological situations; for examples, the red points could all lie inside a certain sphere, and the blue points outside it. Then no choice of linear coordinates will illustrate this, and one has to use more advanced analysis techniques to pick up on it (e.g. persistent homology).

So, to my vague question: do you have only the first situation in mind, or are you also considering the general case, but made the illustrated example extra-simple?

Perhaps this is clarified by your numerical example, I'm afraid I've not checked.

#### [>] Zack_M_Davis [AUTHOR] · 3 karma · 2019-06-16 · https://www.lesswrong.com/posts/cu7YY7WdgJBs3DpmJ/the-univariate-fallacy-1?commentId=cahsbCwWzXbGoPhvK
> Projecting onto any 1-dimensional subspace orthogonal to this (there is a unique one through the origin) will thus yield a 'variable' which cleanly separates the two points into the red and blue categories. So in the illustrated example, it looks just like a problem of bad coordinate choice.

Thanks, this is a really important point! Indeed, for freely-reparametrizable abstract points in an abstract vector space, this is just a bad choice of coordinates. The reason this objection doesn't make the post completely useless, is that for some applications (you know, if you're one of those weird people who cares about "applications"), we _do_ want to [regard some bases as more "fundamental"](https://www.lesswrong.com/posts/XDkeuJTFjM9Y2x6v6/which-basis-is-more-fundamental), if the variables represent real-world measurements.

For example, you might be able to successfully classify two different species of flower using _both_ "stem length" and "petal color" measurements, even if the distributions overlap for either stem length or petal color considered individually. Mathematically, we could view the distributions as _not_ overlapping with respect to some variable that corresponds to some weighted function of stem length and petal color, but that variable seems "artificial", less "interpretable."

#### [>>] DavidHolmes · 3 karma · 2019-06-17 · https://www.lesswrong.com/posts/cu7YY7WdgJBs3DpmJ/the-univariate-fallacy-1?commentId=xhMpPobkT9bzfG6iC
Thanks for the reply, Zack.

> The reason this objection doesn't make the post completely useless...

Sorry, I hope I didn't suggest I thought that! You make a good point about some variables being more natural in given applications. I think it's good to keep in mind that sometimes it's just a matter of coordinate choice, and other times the points may be separated but not in a linear way.

#### [>>>] Zack_M_Davis [AUTHOR] · 4 karma · 2019-06-18 · https://www.lesswrong.com/posts/cu7YY7WdgJBs3DpmJ/the-univariate-fallacy-1?commentId=KCuGyPyyqbYmZ7i3w
> Sorry, I hope I didn't suggest I thought that! 

I mean, it doesn't matter whether _you_ think it, right? It matters whether it's _true_. Like, _if_ I were to were to write a completely useless blog post on account of failing to understand the concept of a [change of basis](https://en.wikipedia.org/wiki/Change_of_basis), then someone _should_ tell me, because that would be helping me stop being deceived about the quality of my blogging.

#### [>>] Rachel Shu · 3 karma · 2019-09-03 · https://www.lesswrong.com/posts/cu7YY7WdgJBs3DpmJ/the-univariate-fallacy-1?commentId=v3Wp8wWSaTzrzwRNZ
Another way to succinctly say this is that two distributions may be cleanly separable via a single immeasurable variable, but overlap when measured on any given measurable variable, such that a representation of the separation achieved by a single immeasurable variable is only achievable through multiple measurable variables.

#### [-] A1987dM · 2 karma · 2024-01-08 · https://www.lesswrong.com/posts/cu7YY7WdgJBs3DpmJ/the-univariate-fallacy-1?commentId=4E2PhsDqzfo3afakr
I'm *almost* sure I saw a Wikipedia article about this back in the mid 2000s with a 2D version of your plot, but I can't find anything relevant in either [https://en.wikipedia.org/wiki/List\_of\_fallacies#Statistical_fallacies](https://en.wikipedia.org/wiki/List_of_fallacies#Statistical_fallacies) or [https://en.wikipedia.org/wiki/List\_of\_paradoxes#Statistics](https://en.wikipedia.org/wiki/List_of_paradoxes#Statistics) [...](https://en.wikipedia.org/wiki/List_of_paradoxes#Statistics...) did I just dream of it?

#### [>] Zack_M_Davis [AUTHOR] · 4 karma · 2024-01-09 · https://www.lesswrong.com/posts/cu7YY7WdgJBs3DpmJ/the-univariate-fallacy-1?commentId=gimDFbyrHf4QWZPpr
[You weren't dreaming!](https://en.wikipedia.org/wiki/File:Pattern_classification_medium.JPG)

