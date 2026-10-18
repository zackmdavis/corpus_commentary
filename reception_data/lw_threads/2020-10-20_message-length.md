Title: Message Length
LessWrong-URL: https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length
Posted: 2020-10-20
Fetched: 2026-10-13 (LessWrong GraphQL API; rendered by tools/render_lw_threads.py)
Comments: 25 (commentCount field: 25)

#### [-] cousin_it · 31 karma · 2020-10-20 · https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length?commentId=SpvRzJo2PQ6tx2mtL
You lay it out very nicely. But I'd quibble that as long as your nth-order Markov chain isn't exceptionally small and fully deterministic, there might be room for more explanation. Maybe there's no explanation and the data is genuinely random, but what if it's a binary encoded Russian poem? When you've exhausted all self-contained short theories, that doesn't mean the work of science is done. You also need to exhaust all analogies with everything in the world whose complexity is already "paid for", and then look at that in turn, and so on.

#### [>] Zack_M_Davis [AUTHOR] · 13 karma · 2020-10-20 · https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length?commentId=6Dxqi53edc4sZnyte
Yeah, but I couldn't get [that program](https://en.wikipedia.org/wiki/Solomonoff%27s_theory_of_inductive_inference) to run on my desktop.

#### [>] Ms. Haze · 4 karma · 2020-10-20 · https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length?commentId=g8JX9TA9qoXPK35Qu
I agree. I definitely would have run through common encodings before going to Markov Chains.

#### [>>] FireStormOOO · 5 karma · 2020-10-22 · https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length?commentId=As8HNC4hZQFWSJM6x
First thing I did before even reading the article is see that it wasn't ASCII or UTF-8 (or at least if it was it wasn't bit-aligned).  Definitely on the short list of things technical folks are going to instinctively check, along with maybe common "magic bytes" at the start of the maybe-a-file.

#### [-] dynomight · 8 karma · 2020-10-20 · https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length?commentId=DrMYyeFhvAHxQojHo
This covers a really impressive range of material -- well done! I just wanted to point out that if someone followed all of this and wanted more, Shannon's 1948 paper is surprisingly readable even today and is probably a nice companion:

http://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf

#### [-] Gunnar_Zarncke · 6 karma · 2020-10-20 · https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length?commentId=i5LRaqgmq6PR8FTi7
I liked the previous title - Msg Len - better, but I agree that it was maybe a bit too much ;-)

#### [-] rainy · 17 karma · 2020-10-21 · https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length?commentId=bnZo3FNDs5yCgb3Mb
I did a strange experiment once, I implemented a markov predictor like this and used it to predict the next bit of a sequence. Then I extended the sequence with the negation of that bit an increased the length of the markov chain. The result was a very random unpredictable looking sequence, but of course it was completely deterministic. I wonder if this sequence has a name?

#### [>] Zack_M_Davis [AUTHOR] · 8 karma · 2020-10-21 · https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length?commentId=G4pnfKLb3caiFZBpa
[Your childhood dislike of asymmetry led you to invent the Thue–Morse sequence?!](https://www.lesswrong.com/posts/Aqdwxp5AhStfrnRDY/open-thread-december-2009?commentId=XwzvJkumRfHKBejjC)

#### [-] habryka · 10 karma · 2020-10-21 · https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length?commentId=byzaiS6XwHk83Trmq
Promoted to curated: This really is a quite good and straightforward explanation of what I think of as one of the really core ideas in theoretical rationality, covering surprisingly much ground in a way that feels approachable. I remember how impactful reading "A technical explanation of a technical explanation" was for my thinking about rationality, and this feels like a much less daunting introduction to some of the same ideas.

#### [>] Zack_M_Davis [AUTHOR] · 4 karma · 2020-10-22 · https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length?commentId=oJxDZWBJKrMSW3BdL
Thanks! But ... I'm not seeing the Curated "★" icon (_e.g._, in the Posts list on [my profile](https://www.lesswrong.com/users/zack_m_davis))? Am I missing something, or is there an extra button you still have to click?

#### [>>] jimrandomh · 9 karma · 2020-10-22 · https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length?commentId=rfyLpWbk4X8Je8RiH
(When we curate something, admins get an email version of the post immediately, then everyone else who's subscribed to curated gets the email after a 20 minute delay. Sometimes we notice a formatting problem with the email, un-curate during the 20 minute window, then re-curate it; that's what happened in this case.)

#### [-] dxu · 22 karma · 2020-10-22 · https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length?commentId=EyY2kmixkHAELNx6s
> Since the parameters in your implementation are 32-bit floats, you assign a complexity cost of 32 ⋅ 2^n bits to n-th order Markov chains, and look at the sum of fit (log loss) and complexity.

Something about this feels wrong. The precision of your floats shouldn't be what determines the complexity of your Markov chain; the expressivity of an nth-order Markov chain will almost always be worse than that of a (n+1)th-order Markov chain, *even if the latter has access to higher precision floats than the former*. Also, in the extreme case where you're working with real numbers, you'd end up with the absurd conclusion that every Markov chain has infinite complexity, which is obviously nonsensical.

This does raise the question of *how* to assign complexity to Markov chains; it's clearly going to be linear in the number of parameters (and hence exponential in the order of the chain), which means the general form k ⋅ 2^n seems correct... but the value you choose for the coefficient k seems underdetermined.

#### [>] Zack_M_Davis [AUTHOR] · 12 karma · 2020-10-22 · https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length?commentId=5yRPe3soxdAhrKTfE
You're right! This is something that the literature has details on, that I chose to simplify/gloss-over in pursuit of my goal of "write Actual Executable Code implementing minimum-description-length model selection and then tell a cute story about it."

Chapter 5 of Peter D. Grünwald's _The Minimum Description Length Principle_ gives the complexity term (assuming that the parameter space is compact) as $kd + L_{\mathbb{N}}(k) + L_{\mathbb{N}}(d)$, where $k$ is the number of parameters, $d$ is the bits of percision per parameter, and $L_{\mathbb{N}}$ is the codelength function for a universal prior on the integers (the theoretical ideal that [Levenshtein coding](https://en.wikipedia.org/wiki/Levenshtein_coding) and the [Elias ω coding](https://en.wikipedia.org/wiki/Elias_omega_coding) approach). Basically, in order to specify your parameters, you need to first say how many of them there are and to what precision, and for that, you need a [prefix-free code](https://en.wikipedia.org/wiki/Prefix_code) for the integers, which is itself kind of intricate: you can't give every integer the same codelength, so you end up doing something like "first give the order of magnitude (in, um, unary), and _then_ pick out a specific integer in that range", but recursively (so that you first give the order of magnitude of the order of magnitude if it gets too big, _&c_.). 

(Oh, and Grünwald warns that this still isn't optimal and that question of _the best_ encoding is left to §15.3, but I'm not there yet—it's a big textbook, okay?)

I was originally imagining implementing the integer coding, but I decided it was too complicated for the cute story I wanted to tell about model selection, particularly since I wanted to provide Actual Executable Code with minimal boilerplate and minimal dependencies. (Rust just gives me `f32` and `f64`, not variable-length floats.) I think this kind of handwaving should be admissible in the cute-blog-story genre as long as the author addresses objections in the comment section.

#### [-] Mathisco · 2 karma · 2020-10-22 · https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length?commentId=kkcs9dX9o3AkhrLGy
May I ask why you choose Rust to write math and algorithms? I would have chosen Julia :p

#### [>] Zack_M_Davis [AUTHOR] · 6 karma · 2020-10-23 · https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length?commentId=W7KmQbuafgfmPgvYm
Realistically?—Python and Rust are the only two languages I'm Really Good at, and I'm more Excited about Rust because I write enough Python at my dayjob? In my defense, the [`.windows` iterator on slices](https://doc.rust-lang.org/std/primitive.slice.html#method.windows) was really handy here and is [shamefully missing from Python's `itertools`](https://stackoverflow.com/questions/6822725/rolling-or-sliding-window-iterator).

#### [>>] gilch · 6 karma · 2020-10-23 · https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length?commentId=mJRiCBQSNidc7Wtx3
Toolz has a [sliding window](https://toolz.readthedocs.io/en/latest/api.html#toolz.itertoolz.sliding_window).

Hy's `partition` can also do a sliding window like Clojure's can, by setting the `step` argument.

#### [>>>] Mathisco · 1 karma · 2020-10-23 · https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length?commentId=FPF4LNsiBeTqSdKqy
Julia's IterTools has the [partition](https://juliacollections.github.io/IterTools.jl/latest/#partition(xs,-n,-[step])-1) with step argument as well

#### [>>] Mathisco · 1 karma · 2020-10-23 · https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length?commentId=YbidC3DzPxr6Znvd4
Rust is a fascinating new language to learn, but not designed for scientific computing. For that Julia is the new kid on the block, and quite easy to pick up if you know Python.

#### [-] Donald Hobson · 10 karma · 2020-10-22 · https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length?commentId=m7mdYpLCodXkgJAAH
Of course, you also need to store the concept of a Markov chain in the abstract as part of your models. (But that is constant, and should be fairly small in a good encoding. ) On the other hand, 32 bit floats are excessive in precision. And a substantial proportion of floats aren't in the range \[0,1\] at all. You could probably cut the precision down to 16 bits, maybe less. Of course, you also need a few bits for the order of the markov chain, and the precision used.

#### [-] ic · 3 karma · 2020-10-22 · https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length?commentId=Ft9ieJqmK8HqfHeY8
A recommended reading for understanding more of what happens with "regularization" in optimization and search algorithms.

Interesting also the post comes the same week as a discussion on the [Solomonoff prior](https://www.lesswrong.com/posts/Tr7tAyt5zZpdTwTQK/the-solomonoff-prior-is-malign).

#### [-] BeanSprugget · 5 karma · 2020-10-26 · https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length?commentId=XNtpfKxYGWa8wLfNx
Really interesting post. To me, approaching information with mathematics seems like a black box - and in this post, it feels like magic.

I'm a little confused by the concept of cost: I understand that it takes more data to represent more complex systems, which grows exponentially faster than than the amount of bits. But doesn't the more complex model still strictly fit the data better? - is it just trying to go for a different goal than *accuracy*? I feel like I'm missing the entire point of the end.

#### [>] Mart_Korz · 1 karma · 2020-10-30 · https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length?commentId=v2i4wgLhPQCZpenjG
I am not sure whether my take on this is correct, so I'd be thankful if someone corrects me if I am wrong:

I think that if the goal was only 'predicting' this bit-sequence after knowing the sequence itself, one could just state probability 1 for the known sequence.

In the OP instead, we regard the bit-sequence as stemming from some sequence-generator, of which only this part of the output is known. Here, we only have limited data such that singling out a highly complex model out of model-space has to be weighed against the models' fit to the bit-sequence.

#### [-] derikk · 11 karma · 2021-09-02 · https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length?commentId=gvpT2fC6PDpvstBwx
This sounds like a classic example of the [bias-variance tradeoff](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff): adding parameters to your model means it can more accurately fit your data (lower bias), but is more sensitive to fluctuations in that data (higher variance). Total error when making predictions on new data is minimized when the bias and variance errors are balanced.

Another example: given $n$ data points, you can always draw a polynomial of degree $n-1$ that fits them perfectly. But the interpolated output values may vary wildly with slight perturbations to your measured data, which is unlikely to represent a real trend. Often a simple linear regression is the most appropriate model.

#### [-] moody · 2 karma · 2021-09-27 · https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length?commentId=L6WzPpcDGxR9bqnbx
> And *that's* how you can explain mysteriously frequent consecutive runs and alternations. If the last *two* bits being `01` (respectively `10`) makes it more likely for the next bit to be `0` (respectively `1`), *and* the last two bits being `00` (respectively `11`) makes it more likely for the next bit to be `0` (respectively `1`), then you would be more likely to see both long `0000`... or `1111`... consecutive runs *and* `01010`... alternations.

Alternatively, it could be a first order chain that checks the digit located 2 bits before it and makes it more likely to match. This does however remove the possibility of assigning different likelihoods to `00`  and `01` being followed by `0` (or `11` and `10` being followed by `1`).

Edit: or a coin biased to match the digit 2 entries before, removing the possibility of different likelihoods for chains of 1 and chains of 0 (or alternating chains beginning/ending on 1 or 0).

#### [-] Raemon · 13 karma · 2021-12-02 · https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length?commentId=rxap5aAY333eRPb3H
I'll probably write up a proper review later. But right now I just wanted to say: the other day, someone sent me a big blob of code over IM. I looked at it, my eyes kinda glazed over, I was confused about why they sent it. I moved on with my day.

Only later did I realize the code was an SVG file that a) my computer program was supposed to automatically read and interpret, b) *I* totally could have noticed and interpreted and realized I should open it in photoshop. 

And then I thought "man, I feel like I'm a character in some Zack Davis fiction, and I totally failed at my job."

