Post: http://unremediatedgender.space/2020/Apr/dont-read-the-comments/
Fetched: 2026-10-15 (public Isso API)
Comments: 7 top-level

#### [-] maskedtorah · 3 likes · 2020-04-09 · http://unremediatedgender.space/2020/Apr/dont-read-the-comments/#isso-5
I wish I understood better what causes comment sections to be good or bad. Popularity past a point is typically harmful, but not catastrophically so; e.g., Slate Star Codex is widely read at this point but maintains a comment section that is unusually good, and even the better 1M+ subreddits can maintain acceptable comment sections. Youtube, on the other hand, is catastrophically bad in almost all situations, despite fragmentation into plenty of small communities that should be populated with smart people.

My guess is that fairly harsh enforcement of quality is unlikely to be very harmful, and removing bad comments helps maintain a norm that a comment section is for thoughtful responses only; this might not matter as much for low-traffic spaces, though.

#### [>] a walrus · 2 likes · 2020-04-10 · http://unremediatedgender.space/2020/Apr/dont-read-the-comments/#isso-7
I think another big factor is self-selection.

In my impression, even relatively niche videos on YouTube tend to have comment sections full of people who just got it dumped into their algorithmic recommendations feed. News articles are full of people who feel like this outrageous headline invaded their social media feed.

I think most people who even get to the point where they scroll down to the comment section on a place like SSC actively follow the blog.

#### [>] Ninety-Three · 2 likes · 2020-04-14 · http://unremediatedgender.space/2020/Apr/dont-read-the-comments/#isso-10
Yes, SSC is relatively popular, but it's still popular among autistic nerds with IQs averaging 130. In most cases, including "intellectual Youtube", popularity is a proxy for mass appeal. The closer you get to "appeals to everyone", the closer you get to "everyone comments"*, and the quality of the average person's comments is really low.

Moderation has some impact of course, and it's easy to focus on it because it's the easiest part of the equation to control, but I've always suspected that audience quality dominates.

*Actually it's worse because of evaporative cooling.

#### [-] Zack M. Davis · 1 likes · 2020-04-13 · http://unremediatedgender.space/2020/Apr/dont-read-the-comments/#isso-9
I was sad about not feeling motivated to write (the draft of the book review I've been [teasing since February](http://unremediatedgender.space/2020/Feb/cloud-vision/) is sitting 8700 words, with at least a major section still to go), so I decided to lift my spirits by [coding up](http://unremediatedgender.space/source?p=Ultimately_Untrue_Thought.git;a=commitdiff;h=0f9374a08228965c207e0d77fd5adc701a3b461b;hp=c25ced8c462d48f0c8667ec64634e8b57bf371ed) a crude "Recent Comments" list for the sidebar.

Isso's latest-comments endpoint [only landed recently](https://github.com/posativ/isso/commit/1633d9261ec9877358cda7acc7d78ecb9b09562c), and the project hasn't seen a PyPI release since January of the previous year, so the server is now running Isso master: requests for the comment-form-widget-thingy were 404ing at first because just installing the Python package didn't give us the minified JavaScript for the client, but I grabbed a copy of the .min.js file from the demo on the [project webpage](https://posativ.org/isso/), and we should be good now.

If the virus kills me before I get any more actual blog posts out, I am going to die unhappy.

#### [-] Zack M. Davis · 1 likes · 2021-01-27 · http://unremediatedgender.space/2020/Apr/dont-read-the-comments/#isso-107
I'm not regretting this so far!  I [changed the configuration](http://unremediatedgender.space/source?p=Ultimately_Untrue_Thought.git;a=commitdiff;h=a813b5b4e2) so that all the comments load immediately on the [most recent linkpost](http://unremediatedgender.space/2021/Jan/link-unnatural-categories-are-optimized-for-deception/), rather than some being hidden behind an "N Hidden" link.

#### [>] L (Zero) · 0 likes · 2021-01-27 · http://unremediatedgender.space/2020/Apr/dont-read-the-comments/#isso-108
Haha wow! I'm glad you're not dismayed by probably one of the most active comment sections so far. When I showed <a href=http://unremediatedgender.space/2020/Aug/yarvin-on-less-wrong/>this post</a> to a friend, she was genuinely unsure if that last part was numerically collapsed or moderated or downvoted.

#### [-] Zack M. Davis · 0 likes · 2021-03-09 · http://unremediatedgender.space/2020/Apr/dont-read-the-comments/#isso-133
Comments were down for about an hour because I upgraded the server from [Xenial to Bionic](https://wiki.ubuntu.com/Releases) (because I want to try the [Pelican pingback plugin](https://github.com/pelican-plugins/linkbacks) that requires Python 3.6) and needed to figure out how to set up my virtualenvs again (and pull in the fix for [Isso issue #657](https://github.com/posativ/isso/issues/657)).
