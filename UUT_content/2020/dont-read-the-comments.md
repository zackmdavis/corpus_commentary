Title: Don't Read the Comments??
Date: 2020-04-05 22:30
Category: other
Tags: meta, Python

Historically, _The Scintillating But Ultimately Untrue Thought_ has not provided a comment section. There were two reasons for this.

First, technical limitations, downstream of technical æsthetics. There are standard out-of-the-box blogging hosts—your [WordPress](https://wordpress.com/), your [Medium](https://medium.com/), _&c._—that are easy for anyone to use, at the cost of taking control away from the user, locking access to _your soul_ away on someone else's server, or, at best, obfuscated in some database behind opaque gobs of [PHP](https://eev.ee/blog/2012/04/09/php-a-fractal-of-bad-design/). My real-name blog (started in December 2011, when I was much less technically adept) is still running WordPress, and I'm sad about it. In contrast, this blog is produced using the [Pelican](https://blog.getpelican.com/) static site generator from Markdown text files, [versioned in Git](http://unremediatedgender.space/source?p=Ultimately_Untrue_Thought.git)—simple tools I _understand_, producing flat HTML files that Nginx can serve. When I don't like something about my theme or my plugins, I'm not at the mercy of the developers; I can just fix it myself. The lack of a database meant forgoing a comment section, but that seemed like a small loss, because—

Second, internet comment sections are _garbage_ and I don't want to be bothered to moderate one. I thought, people who are actually interested in replying to my writing can write a longform response on their own blog (please?—I'll link back), or on Reddit when I share to [/r/TheMotte](https://www.reddit.com/r/TheMotte/); and people who want to talk to me can find [my email address](mailto:ultimatelyuntruethought@gmail.com) (checked less often than my real-name email; I regret any delays) on [the About page](/about/).

So I thought, and yet—first, the same do-it-myself æsthetics that make static-site generators attractive, make me cautiously open to the idea of a comment section that I can configure and host myself, rather than being held commercially hostage by the likes of [Disqus](https://disqus.com/). Second, perhaps some small consolation for never being a popular writer (I'm not prolific enough, and occupying too _weird_ of a niche), is that maybe _my_ readership is exclusive and discerning enough for the comments section to _not_ be garbage.

So, as an _experiment_—no promises or warranties—I've set up an instance of the [Isso](https://posativ.org/isso/) commenting engine to host a comments section at the bottom of each indivdual post page.

Don't make me regret this.
