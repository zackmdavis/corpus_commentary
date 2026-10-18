Post: http://unremediatedgender.space/2020/Nov/survey-data-on-cis-and-trans-women-among-haskell-programmers/
Fetched: 2026-10-15 (public Isso API)
Comments: 7 top-level

#### [-] foxlisk · 3 likes · 2020-11-25 · http://unremediatedgender.space/2020/Nov/survey-data-on-cis-and-trans-women-among-haskell-programmers/#isso-59
incredible power move to add a footnote to the last sentence of a blog post

#### [>] Zack M. Davis · 0 likes · 2020-12-17 · http://unremediatedgender.space/2020/Nov/survey-data-on-cis-and-trans-women-among-haskell-programmers/#isso-72
I needed to explain where I was getting the ratio from, but it wasn't important enough to deserve a full sentence in the body!

#### [-] Sophia · 3 likes · 2020-11-25 · http://unremediatedgender.space/2020/Nov/survey-data-on-cis-and-trans-women-among-haskell-programmers/#isso-60
I don't have anything substantive to add, I just wanted to appreciate "transwer"

#### [-] Rat Analyst · 0 likes · 2020-11-26 · http://unremediatedgender.space/2020/Nov/survey-data-on-cis-and-trans-women-among-haskell-programmers/#isso-61
Did many respondents state their gender but not whether they identified as transgender or vice versa?

#### [>] Spencer · 0 likes · 2020-11-26 · http://unremediatedgender.space/2020/Nov/survey-data-on-cis-and-trans-women-among-haskell-programmers/#isso-62
5.3% of participants who state gender do not answer the trans question. Conversely, 3% of people who answer the trans question do not answer about gender.

#### [-] Spencer · 0 likes · 2020-11-26 · http://unremediatedgender.space/2020/Nov/survey-data-on-cis-and-trans-women-among-haskell-programmers/#isso-63
Here are is the full contingency table, for those who want more details. Gender is ♀/♂︎/? and trans identity is  → (cis), ⚧ (trans), or ? (no response).

<pre>
2018    →    ⚧    ?
♀    26    19    4    49
♂︎    1034    2    83    1119
?    19    14    160    193
    1079    35    247    1361

2019    →    ⚧    ?
♀    16    16    0    32
♂︎    1071    1    28    1100
?    19    11    49    79
    1106    28    77    1211

2020    →    ⚧    ?
♀    12    21    1    34
♂︎    1124    2    73    1199
?    23    15    77    115
    1159    38    151    1348

Total    →    ⚧    ?
♀    54    56    5    115
♂︎    3229    5    184    3418
?    61    40    286    387
    3344    101    475    3920
</pre>

I have a few nitpicks about Taylor's statistics:

Your totals include non-responses. I think it would be better to only include people who responded to both gender and trans identity

The huge male bias in the sample makes it really hard to compare to general populations. In particular, observing that 51% of women are trans is not meaningful since trans people are 91% male.

The Williams study you site doesn't break down the statistics by gender, so we can't compare cis-women:trans-women directly. The overall % trans in this data is 1.8%, but even this isn't comparable to 0.58% since trans-men probably outnumber trans-women ([NYT](https://www.nytimes.com/2015/06/09/upshot/the-search-for-the-best-estimate-of-the-transgender-population.html) suggests 65% trans-men).

Haskell programmers have a ton of socioeconomic factors that might correlate with gender identity (age, location, etc).

#### [>] Zack M. Davis · 0 likes · 2020-12-17 · http://unremediatedgender.space/2020/Nov/survey-data-on-cis-and-trans-women-among-haskell-programmers/#isso-73
Thanks! I at least edited the post to not count non-responses (and credit your comment for pointing out the oversight). For a moment I was worried that our totals weren't matching up (e.g., I read your table to say that in 2020, you think 12+21+1124+2 = 1159 people answered both questions, whereas I got 1192), but it looks like that's just because you're counting the "Non-binary" responses in the "?" row (1192 − 1159 = 33, and there were 33 "Non-binary" responses in 2020).
