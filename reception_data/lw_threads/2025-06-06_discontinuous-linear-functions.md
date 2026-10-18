Title: Discontinuous Linear Functions?!
LessWrong-URL: https://www.lesswrong.com/posts/GodqHKvQhpLsAwsNL/discontinuous-linear-functions
Posted: 2025-06-06
Fetched: 2026-10-13 (LessWrong GraphQL API; rendered by tools/render_lw_threads.py)
Comments: 11 (commentCount field: 11)

#### [-] Gurkenglas · 7 karma · 2025-06-06 · https://www.lesswrong.com/posts/GodqHKvQhpLsAwsNL/discontinuous-linear-functions?commentId=9RtSgpF5HDvF4Nraq
> for any ε, we can take $k := \lceil \frac{1}{\varepsilon} \rceil$

You mean take $N := \lceil \frac{1}{\varepsilon} \rceil$.

sqrt(x) is continuous at 0 with an infinitely steep slope.

#### [>] Zack_M_Davis [AUTHOR] · 2 karma · 2025-06-23 · https://www.lesswrong.com/posts/GodqHKvQhpLsAwsNL/discontinuous-linear-functions?commentId=vwExtmZkubgyCB6rt
Thanks for commenting—and for your patience. I've corrected the k/N slip-up, deleted the misleading clause about "a function not having any 'jumps' impl[ying] that it can't have an 'infinitely steep' slope", and thanked you at the bottom.

#### [>>] Gurkenglas · 2 karma · 2025-06-23 · https://www.lesswrong.com/posts/GodqHKvQhpLsAwsNL/discontinuous-linear-functions?commentId=DXEj72tm3kdZ4feBd
you haven't deleted it.

#### [>>>] Zack_M_Davis [AUTHOR] · 2 karma · 2025-06-23 · https://www.lesswrong.com/posts/GodqHKvQhpLsAwsNL/discontinuous-linear-functions?commentId=5TcCzt8kukTLqgTf5
Now I have. (Sorry, apparently I got confused while trying to make parallel updates to [the original](http://zackmdavis.net/blog/) and this mirrorpost; they're not using the same source file due to differences between platform markup engines.)

#### [>>>>] Gurkenglas · 12 karma · 2025-06-23 · https://www.lesswrong.com/posts/GodqHKvQhpLsAwsNL/discontinuous-linear-functions?commentId=GjuET6ivfwtsGhTkr
> a small change in the input can't correspond to an arbitrarily large change in the output

The sign function doesn't have an *arbitrarily* large change in the output. Do you maybe mean that an *infinitesimal* change in the input can only produce an infinitesimal change in the output? I don't see how *that* fails, but maybe just because I don't have a definition for it at hand.

#### [-] Jeffrey Liang · 12 karma · 2025-06-06 · https://www.lesswrong.com/posts/GodqHKvQhpLsAwsNL/discontinuous-linear-functions?commentId=guPEbeKtPnqsBhrjg
Okay I took the nerd bait and signed up for LW to say:

For your example to work you need to restrict the domain of your functions to some compact e.g. $C^1([0,1])$because the uniform norm requires the functions to be bounded.

Also note this example works because you're not using the "usual" topology on $C^1([0,1])$ which also includes the uniform norm of the derivative and makes the space complete. It is much more difficult if the domain is complete!

#### [>] CuriouslyNuclear · 6 karma · 2025-06-13 · https://www.lesswrong.com/posts/GodqHKvQhpLsAwsNL/discontinuous-linear-functions?commentId=aPLdnMmajfH85axpH
> For your example to work you need to restrict the domain of your functions to some compact e.g. $C^1([0,1])$because the uniform norm requires the functions to be bounded.

Hmm, is this really a substantive problem? Call it an "[extended norm](https://planetmath.org/extendednorm)" instead of a norm and everything in the post works, right? My reasoning: An extended norm yields an extended metric space, which still generates a topology — it's just that points which are infinitely far apart are in different connected components. Since you get a perfectly valid topology, it makes perfect sense for the post to talk about continuity. Or at least I think so; am I missing something?

#### [>>] Jeffrey Liang · 4 karma · 2025-06-13 · https://www.lesswrong.com/posts/GodqHKvQhpLsAwsNL/discontinuous-linear-functions?commentId=JejkpATKGhcS7qrJM
Perhaps! I'm not familiar with extended norms. But when you say "let's put the uniform norm on $C^1(R)$" warning bells start going off in my head 😅

#### [>] Zack_M_Davis [AUTHOR] · 4 karma · 2025-06-23 · https://www.lesswrong.com/posts/GodqHKvQhpLsAwsNL/discontinuous-linear-functions?commentId=rKEhK6dLDfg8XdzxA
Thanks for commenting—and for your patience. I've changed the domain to be an arbitrary closed interval and credited you at the bottom.

#### [-] CuriouslyNuclear · 5 karma · 2025-06-13 · https://www.lesswrong.com/posts/GodqHKvQhpLsAwsNL/discontinuous-linear-functions?commentId=6msrTPjs6AZsqHBL5
This is a good post. I remember being so confused in a real analysis class when my professor started talking about how important it is that we restrict our attention to *continuous* linear functions (what on Earth was a discontinuous linear function supposed to be?). This post explains what's going on better than my professor or textbook did.

I agree with one of the other commenters that this part is not technically phrased accurately:

> One way to think about continuity is that a function not having any "jumps" implies that it can't have an "infinitely steep" slope

Because eg the derivative of  $f(x)=\sqrt[3]{x}$ at $x=0$ is $+\infty$ despite the fact that it's continuous there.

#### [-] XelaP · 3 karma · 2026-04-20 · https://www.lesswrong.com/posts/GodqHKvQhpLsAwsNL/discontinuous-linear-functions?commentId=goWcraBsAJrtfGChf
1: The title is indeed the correct way to react to learning this fact.  
2: I'd like to explicitly point out that for linear functions, all you need to check is continuity at 0, which in other words means you only need to check that it's *bounded*, where 'bounded' here means that if I send in a vector of size 1, I don't get something of unbounded size.  
  
That is, for linear functions, the only way a discontinuity can happen is if the unit sphere "blows up" when you send it into the function.

