Title: College Was Not That Terrible Now That I'm Not That Crazy
LessWrong-URL: https://www.lesswrong.com/posts/hHEvfp7kwvaHwgcdH/college-was-not-that-terrible-now-that-i-m-not-that-crazy
Posted: 2026-01-01
Fetched: 2026-10-13 (LessWrong GraphQL API; rendered by tools/render_lw_threads.py)
Comments: 9 (commentCount field: 9)

#### [-] Guive · 14 karma · 2026-01-02 · https://www.lesswrong.com/posts/hHEvfp7kwvaHwgcdH/college-was-not-that-terrible-now-that-i-m-not-that-crazy?commentId=dokbDxeC3Lt8E9ngN
This was a fun read.

#### [-] cata · 13 karma · 2026-01-02 · https://www.lesswrong.com/posts/hHEvfp7kwvaHwgcdH/college-was-not-that-terrible-now-that-i-m-not-that-crazy?commentId=w9og6KbdkkCKgAy5h
Great writeup. Makes me wonder if I should do similar.

#### [-] Pretentious Penguin · 5 karma · 2026-01-02 · https://www.lesswrong.com/posts/hHEvfp7kwvaHwgcdH/college-was-not-that-terrible-now-that-i-m-not-that-crazy?commentId=MknGqjDL9dPoQQxZR
> the minimum distance between a compact and a connected set is achieved by some pair of points in the sets

I don't think this is true. For a counterexample in the plane, let A be the set consisting of the point (2,0) and let B be the open unit disk centered at the origin. A is compact, B is connected, and the infimum of {distance from x to y where x is in A and y is in B} is 1. But the distance from A to any point in B is strictly greater than 1.

#### [>] Zack_M_Davis [AUTHOR] · 4 karma · 2026-01-02 · https://www.lesswrong.com/posts/hHEvfp7kwvaHwgcdH/college-was-not-that-terrible-now-that-i-m-not-that-crazy?commentId=eyL6XfiGMtMSSC3Zo
Thanks, it looks like I accidentally typed "connected" instead of "closed"; fixed.

#### [-] BryceStansfield · 4 karma · 2026-01-02 · https://www.lesswrong.com/posts/hHEvfp7kwvaHwgcdH/college-was-not-that-terrible-now-that-i-m-not-that-crazy?commentId=F4KksDdcniQ7qZn2m
Is this type of course structure typical in US universities? It seems very strange to me that real analysis wouldn't be a first semester class, or that such a large proportion of classes in a maths degree would be on anything but maths.

#### [>] Douglas_Knight · 2 karma · 2026-01-03 · https://www.lesswrong.com/posts/hHEvfp7kwvaHwgcdH/college-was-not-that-terrible-now-that-i-m-not-that-crazy?commentId=qdNCAkPpmJC6N3ngo
> “I wish we had the education system they have in Doorways in the Sand,” I said... “Did you know, there’s a new Heinlein? The Number of the Beast. And he’s borrowed the idea of that education system, where you study all those different things and sign up and graduate when you have enough credits in everything, and you can keep taking courses forever if you want, but he doesn’t acknowledge Zelazny anywhere.”

> Wim laughed. “That’s what they really do in America,” he said.

— Jo Walton, [Among Others](https://www.google.com/books/edition/Among_Others/wz69HqibYJEC?hl=en&gbpv=1&bsq=really%20america)

#### [>] lalaithion · 2 karma · 2026-01-05 · https://www.lesswrong.com/posts/hHEvfp7kwvaHwgcdH/college-was-not-that-terrible-now-that-i-m-not-that-crazy?commentId=swHDhwEPpQua9QGid
Universities and colleges in the United States have a philosophy of education different from what I gather is common in Europe. Almost all schools require not just mastery in a chosen subject, but also breadth requirements; some number of credits in each of math, science, writing, and the humanities, or some other distributional system.

#### [-] Douglas_Knight · 2 karma · 2026-01-09 · https://www.lesswrong.com/posts/hHEvfp7kwvaHwgcdH/college-was-not-that-terrible-now-that-i-m-not-that-crazy?commentId=eYS2YBDyfri8ydXtM
Could you say more about taste? How fast can you evaluate the taste of a book? If it's fast, could you check whether there was a trajectory over the 12 editions?

> showcasing the fearsome technicality of the topic in excruciatingly detailed estimates (proofs involving chains of inequalities, typically ending on "< ε").

That sounds bad. The ultimate proof is a chain of inequalities, but just presenting it is bad compared to deriving it.

#### [-] Douglas_Knight · 5 karma · 2026-01-14 · https://www.lesswrong.com/posts/hHEvfp7kwvaHwgcdH/college-was-not-that-terrible-now-that-i-m-not-that-crazy?commentId=4sm6LqGjf6brDk4uB
I wanted to take measure theory in college, but my advisor talked me out of it, saying that it is an old, ossified field where writers play games of streamlining their proofs. They seek too much generality and defer applications to later courses. That complaint could apply more generally, that introductory graduate classes are bad because they have captive audiences, but it seems to me much worse in analysis than other fields of mathematics. What is the point of measure theory? Archimedes gave a rigorous delta-epsilon proof that if there is a coherent notion of measure, then the area of a circle is πr². But how do you know that you don't encounter inconsistencies?

Applications are related to constructibility. If you know what your goal is, you can see if you can skip the axiom of choice. Indeed, as I phrased it above, the goal is to show that measure is defined on some sigma algebra, not just the maximal one. And it is also related to constructibility. Why do we want measureable functions? What is a function? If a function is something you can apply at a point, then from a constructive viewpoint it must be continuous. But you can constructively describe things like infinite Fourier series. You can't evaluate them at points, but only do other things, like compute an average over a small interval. You want a theorem that the Hilbert space of square integrable functions on the circle is isometric to the Hilbert space of square summable sequences L²(S¹)=&ell;². Usually you define L² as measurable functions up to the equivalence relation of equality away from a measure zero set. But you could instead define it as the metric completion of infinitely differentiable functions under the appropriate norm. This is a much better definition for many reasons, including constructibility, but it requires you to open up your definition of function.

Here are two alternate books. Measure and Probability by Adams and Guillemin is a book about measure theory that tries to justify it by the context of things like 0-1 laws of probability. I'm not sure it succeeds in the justification, but it gives something more serious to think about if you want to drop the axiom of choice or the law of the excluded middle. Also, see [this MO question](https://mathoverflow.net/questions/462986/is-defining-measures-as-functionals-ever-insufficiently-general-in-practice).

The second book is more advanced, outside of the scope of this post. After measure theory, one has functional analysis, the study of infinite dimensional topological vector spaces of functions. I once heard it described as "degenerate topology." For this, I recommend Essential Results of Functional Analysis by [Robert Zimmer](https://en.wikipedia.org/wiki/Robert_Zimmer). It gives a bunch of applications to differential equations with a geometric flavor. It minimizes the amount of theory to get to the applications, in particular, by only using Hilbert spaces, not general Banach spaces.

