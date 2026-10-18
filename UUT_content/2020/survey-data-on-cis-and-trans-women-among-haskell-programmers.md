Title: Survey Data on Cis and Trans Women Among Haskell Programmers
Date: 2020-11-24 22:12
Category: other
Tags: Haskell, sex differences, Python, empirical

Stereotypically, computer programming is both a predominantly male profession and the quintessential profession of non-exclusively-androphilic trans women. Stereotypically, these demographic trends are even more pronounced in communities around "niche" or academic technologies (_e.g._, Haskell), rather than those with more established mainstream use (_e.g._, JavaScript).

But stereotypes can be _wrong_! The heuristic process by which people's brains form stereotypes from experience are riddled with cognitive biases that prevent our mental model of what people are like from matching what people are _actually_ like. Unless you believe [a woman is more likely to be a feminist bank teller than a bank teller (which is _mathematically impossible_)](https://en.wikipedia.org/wiki/Conjunction_fallacy#Definition_and_basic_example), you're best off seeking _hard numbers_ about what people are like rather than relying on mere stereotypes.

Fortunately, sometimes hard numbers are available! Taylor Fausak has been administering an annual State of Haskell survey [since 2017](https://taylor.fausak.me/2017/11/15/2017-state-of-haskell-survey-results/), and the [2018](https://taylor.fausak.me/2018/11/18/2018-state-of-haskell-survey-results/), [2019](https://taylor.fausak.me/2019/11/16/haskell-survey-results/), and [2020](https://taylor.fausak.me/2020/11/22/haskell-survey-results/) surveys included optional "What is your gender?" and "Do you identify as transgender?" questions. I wrote a script to use these answers from the published [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) response data for the 2018–2020 surveys to tally the number of cis and trans women among survey respondents. (In Python. Sorry.)

```
import csv

survey_results_filenames = [
    "2018-11-18-2018-state-of-haskell-survey-results.csv",
    "2019-11-16-state-of-haskell-survey-results.csv",
    "2020-11-22-haskell-survey-results.csv",
]

if __name__ == "__main__":
    for results_filename in survey_results_filenames:
        year, _ = results_filename.split("-", 1)
        with open(results_filename) as results_file:
            reader = csv.DictReader(results_file)
            total = 0
            cis_f = 0
            trans_f = 0
            for row in reader:
                # 2018 and 2019 CSV header has the full question, but
                # 2020 uses sXqY format
                gender_answer = (
                    row.get("What is your gender?") or row.get("s7q2")
                )
                transwer = (
                    row.get("Do you identify as transgender?") or
                    row.get("s7q3")
                )
                if not (gender_answer and transwer):
                    continue

                total += 1
                if gender_answer == "Female":
                    if transwer == "No":
                        cis_f += 1
                    elif transwer == "Yes":
                        trans_f += 1

            print(
                "{}: total: {}, "
                "cis-♀: {} ({:.2f}%), trans-♀: {} ({:.2f}%)".format(
                    year, total,
                    cis_f, 100*cis_f/total,
                    trans_f, 100*trans_f/total,
                )
            )
```

It prints this tally:

```
2018: total: 1108, cis-♀: 26 (2.35%), trans-♀: 19 (1.71%)
2019: total: 1131, cis-♀: 16 (1.41%), trans-♀: 16 (1.41%)
2020: total: 1192, cis-♀: 12 (1.01%), trans-♀: 21 (1.76%)
```

In this particular case, it looks like the stereotypes are true: only about 3% of Haskell programmers (who took the survey and answered both questions) are women, and they're about equally likely to be cis or trans. (There were more cis women in 2018, and more trans women in 2020, but the sample size is too small to infer a trend.) In contrast, the ratio of cis women to trans women in the general population is probably more like 170:1.[ref]A [2016 report](https://williamsinstitute.law.ucla.edu/publications/trans-adults-united-states/) by the Williams Institute at the University of California at Los Angeles estimated the trans share of the United States population at 0.58%, and (1−0.0058)/0.0058 ≈ 171.4.[/ref]

_(This post has been edited to only count responses that answered both questions; see [Spencer's criticism in the comments](/2020/Nov/survey-data-on-cis-and-trans-women-among-haskell-programmers/#isso-63).)_
