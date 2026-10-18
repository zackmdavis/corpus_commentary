Title: Scoring 2020 U.S. Presidential Election Predictions
LessWrong-URL: https://www.lesswrong.com/posts/muEjyyYbSMx23e2ga/scoring-2020-u-s-presidential-election-predictions
Posted: 2020-11-08
Fetched: 2026-10-13 (LessWrong GraphQL API; rendered by tools/render_lw_threads.py)
Comments: 7 (commentCount field: 7)

#### [-] magfrump · 6 karma · 2020-11-08 · https://www.lesswrong.com/posts/muEjyyYbSMx23e2ga/scoring-2020-u-s-presidential-election-predictions?commentId=7aGEwTm2SWxrWJqc2
While I realize that the PredictIt predictions don't actually have this data available, fivethirtyeight projects vote share by state. How much work do you think it would be to do an analysis that uses vote share instead of just wins by state?

#### [>] DanielFilan · 2 karma · 2020-11-08 · https://www.lesswrong.com/posts/muEjyyYbSMx23e2ga/scoring-2020-u-s-presidential-election-predictions?commentId=RtfsXWEyKzaooiqZ9
PredictIt does have this available for some states, e.g. [Pennsylvania](https://www.predictit.org/markets/detail/6941/What-will-be-the-margin-in-the-presidential-election-in-Pennsylvania).

#### [>] steven0461 · 3 karma · 2020-11-11 · https://www.lesswrong.com/posts/muEjyyYbSMx23e2ga/scoring-2020-u-s-presidential-election-predictions?commentId=BcLELEiuPT48QEKfJ
Most closely contested states went to Biden, so vote share is more in Trump's favor than you'd expect based on knowing only who won each state, and PredictIt generally predicted more votes for Trump, so I think PredictIt comes out a lot better than 538 and the Economist.

#### [-] Oscar_Cunningham · 6 karma · 2020-11-11 · https://www.lesswrong.com/posts/muEjyyYbSMx23e2ga/scoring-2020-u-s-presidential-election-predictions?commentId=iibA9SicAbufWE6q5
Does it make sense to calculate the score like this for events that aren't independent? You no longer have the cool property that it doesn't matter how you chop up your observations.

I think the correct thing to do would be to score the single probability that each model gave to this exact outcome. Equivalently you could add the scores for each state, but for each use the probability conditional on the states you've already scored. For 538 these probabilities are available via their [interactive forecast](https://projects.fivethirtyeight.com/trump-biden-election-map/).

Otherwise you're counting the correlated part of the outcomes multiple times. So it's not surprising that The Economist does best overall, because they had the highest probability for a Biden win and that did in fact occur.

My suggested method has the nice property that if you score two perfectly correlated events then the second one always gives exactly 0 points.

#### [>] Oscar_Cunningham · 7 karma · 2020-11-11 · https://www.lesswrong.com/posts/muEjyyYbSMx23e2ga/scoring-2020-u-s-presidential-election-predictions?commentId=2Zzsyh4JGX3oiEYYy
I just did the calculations. Using the interactive forecast from 538 gives them a score of -9.027; using the electoral\_college\_simulations.csv data from The Economist gives them a score of -7.841. So The Economist still wins!

#### [>] Zack_M_Davis [AUTHOR] · 4 karma · 2020-12-14 · https://www.lesswrong.com/posts/muEjyyYbSMx23e2ga/scoring-2020-u-s-presidential-election-predictions?commentId=tftjZDMCqRLqSoW6Q
Thanks; you are right and the thing I originally wrote was wrong. For posterity, I added a disclaimer (sixth paragraph) that credits you and the other person who pointed this out.

#### [-] NunoSempere · 1 karma · 2020-11-15 · https://www.lesswrong.com/posts/muEjyyYbSMx23e2ga/scoring-2020-u-s-presidential-election-predictions?commentId=P8xgoumgCpAwAMRTa
[Here](https://predictingpolitics.com/2020/11/12/hindsight-is-2020) is a similar post.

