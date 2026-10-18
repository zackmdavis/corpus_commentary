Title: Optimized Propaganda with Bayesian Networks: Comment on "Articulating Lay Theories Through Graphical Models"
LessWrong-URL: https://www.lesswrong.com/posts/Zvu6ZP47dMLHXMiG3/optimized-propaganda-with-bayesian-networks-comment-on
Posted: 2020-06-29
Fetched: 2026-10-13 (LessWrong GraphQL API; rendered by tools/render_lw_threads.py)
Comments: 10 (commentCount field: 10)

#### [-] waveman · 11 karma · 2020-06-29 · https://www.lesswrong.com/posts/Zvu6ZP47dMLHXMiG3/optimized-propaganda-with-bayesian-networks-comment-on?commentId=Qmcr5Ei2egawsxPzG
> how to use [causal graphical models](https://www.lesswrong.com/posts/hzuSDMx7pd2uxFc5w/causal-diagrams-and-causal-models) to study why ordinary people have the beliefs they do, and how to intervene to make them be [less wrong](https://tvtropes.org/pmwiki/pmwiki.php/Main/TitleDrop).

Note to self - a good reason to listen carefully to people's reasons for their beliefs, even/especially when they are nonsensical. They may have structure that can be exploited.

#### [>] MrMind · 5 karma · 2020-06-30 · https://www.lesswrong.com/posts/Zvu6ZP47dMLHXMiG3/optimized-propaganda-with-bayesian-networks-comment-on?commentId=wcKxEwPgY5E5ZZv65
How probable is that someone knows their internal belief structure? How probable is that someone who knows their internal belief structure tells you that truthfully instead of using a self-serving lie?

#### [>] Kaj_Sotala · 12 karma · 2020-06-30 · https://www.lesswrong.com/posts/Zvu6ZP47dMLHXMiG3/optimized-propaganda-with-bayesian-networks-comment-on?commentId=AHkvzc5iPbEbbfytw
> [He was bitter. He was angry. He wouldn’t look at her. And, she could recognize, what he was saying didn’t make sense. She recognized, what he was saying didn’t fit with what he had just said. ... What Crowley was saying didn’t make sense, not on the surface. The individual pieces of what he said were incoherent, which, she knew, meant that there must be some other layer, some deeper layer, where they did make sense.](https://archiveofourown.org/works/20177950/chapters/47807593)

#### [-] noggin-scratcher · 27 karma · 2020-06-29 · https://www.lesswrong.com/posts/Zvu6ZP47dMLHXMiG3/optimized-propaganda-with-bayesian-networks-comment-on?commentId=GSkj6DPg8CCkNY4GG
> plus some ancillary assumptions (more-general "theory" beliefs like "skepticism of medical authorities" can cause more-specific "claim" beliefs like "vaccines have harmful additives", but not vice versa)

This jumped out to me because it seems potentially untrue; I would expect there to exist at least some instances where people's belief about the specifics comes prior to, and is what causes, their beliefs about the general theory.

#### [-] johnswentworth · 7 karma · 2020-06-29 · https://www.lesswrong.com/posts/Zvu6ZP47dMLHXMiG3/optimized-propaganda-with-bayesian-networks-comment-on?commentId=oLcffxaujYdi9KnFc
> (and are [*conditionally* independent](https://en.wikipedia.org/wiki/Conditional_independence) given the value of $C$)

I believe this should say "conditionally dependent".

#### [>] Zack_M_Davis [AUTHOR] · 4 karma · 2020-06-30 · https://www.lesswrong.com/posts/Zvu6ZP47dMLHXMiG3/optimized-propaganda-with-bayesian-networks-comment-on?commentId=RsYugyB4WhmzAQkSG
Thanks, you are right and the thing I actually typed was wrong. (For the graph A → C ← B, the collider C [blocks the path](http://bayes.cs.ucla.edu/BOOK-2K/d-sep.html) between A and B, but _conditioning_ on the collider _un_-blocks it.) Fixed.

#### [-] ryan_b · 4 karma · 2020-06-29 · https://www.lesswrong.com/posts/Zvu6ZP47dMLHXMiG3/optimized-propaganda-with-bayesian-networks-comment-on?commentId=nFhrvFxG8QFx8So38
> The thing is, "Learn the causal graph of why they think that and compute how to intervene on it to make them think something else" is a [symmetric weapon](https://web.archive.org/web/20200521005958/http://slatestarcodex.com/2017/03/24/guided-by-the-beauty-of-our-weapons/)—a *fully general* persuasive technique that doesn't [depend on whether the thing you're trying to convince them of is *true*](http://benjaminrosshoffman.com/humility-argument-honesty/).

Is there a technical term for the difference between locally-symmetric and symmetric-under-repetition? It remains the case that the people who use the method to prevent vaccinations will have a lot more casualties on their side, which would normally be telling over time.

#### [>] Pattern · 3 karma · 2020-07-02 · https://www.lesswrong.com/posts/Zvu6ZP47dMLHXMiG3/optimized-propaganda-with-bayesian-networks-comment-on?commentId=NPTdxbwx5qG7fJkwo
Why deploy the method against your side?

#### [-] Trinley Goldenberg · 5 karma · 2020-06-30 · https://www.lesswrong.com/posts/Zvu6ZP47dMLHXMiG3/optimized-propaganda-with-bayesian-networks-comment-on?commentId=YFM4t2fSE2CyNfu7Z
Hmm, this is cool!

it seems sort of like a group version of [consideration factoring.](https://musingsandroughdrafts.wordpress.com/2019/11/14/consideration-factoring-a-relative-of-double-crux/)

Since this is a symmetric weapon, do you think that it's best to spread it globally (because someone using the symmetric weapons to point at truth will outcompete those using them to point at falsehoods) to try to keep the spread to champions of the truth, something else?  
  
Trying to figure out how people are orienting to the idea of symmetric strategies.

#### [-] Mart_Korz · 2 karma · 2020-06-30 · https://www.lesswrong.com/posts/Zvu6ZP47dMLHXMiG3/optimized-propaganda-with-bayesian-networks-comment-on?commentId=raKn6kcknPRAwACaz
Up-voted for thoroughly putting the idea into less wrong context - i enjoyed being reminded of all the related ideas

  

A thought: I am a bit surprised that one can distil a single belief network explaining a whole lot of the variance of beliefs across many people. This makes me take the idea more seriously that a large number of people regularly do have very similar beliefs (down to the argumentative structure). Remembering [You Have About Five Words](https://www.lesswrong.com/posts/4ZvJab25tDebB8FGE/you-have-about-five-words) this surprises me as I would expect a less reliable transmission of beliefs? (It might well be that I am just misunderstanding something)

