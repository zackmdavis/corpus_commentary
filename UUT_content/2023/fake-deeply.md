Title: Fake Deeply
Date: 2023-10-26 12:40
Category: fiction
Tags: artificial intelligence, speculative fiction

"I want _you_, Jake," said the woman in the video as she took off her shirt. "Those negative comments on your pull requests were just a smokescreen—because I was afraid to confront the inevitability of our love!"

Jake Morgan still couldn't help but marvel at what he and his team had built. It really looked and sounded just like her!

It had been obvious since DALL-E back in 'twenty-one—earlier if you were paying attention—that generative AI would reach this level of customization and realism before too long. Eventually, it was just a matter of the right couple dozen people rolling up their sleeves—and Magma's willingness to pony up the compute—to make it work. But _it worked_. His awe at Multigen's sheer power would have been humbling, if not for the awareness of his own role in bringing it into being.

Of course, this particular video wouldn't be showcased in the team's next publication. Technically, Magma employees were not supposed to use their cutting-edge generative AI system to make custom pornography of their coworkers. Technically (what was probably a lesser offense) Magma employees were not supposed to be viewing pornography during work hours. Technically—what should have been a greater offense—Magma employees were not supposed to covertly introduce a bug into the generative AI service codebase specifically in order to make it possible to create custom pornography of their coworkers without leaving a log.

<span style="float: right; margin: 0.4pc;">
<a href="/images/fake_deeply-jake.png"><img src="/images/fake_deeply-jake-smaller.png" width="450"></a><br/>
<span class="photo-credit" style="float: right;">Illustration made with [Stable Diffusion XL 1.0](https://stability.ai/stable-diffusion)</span>
</span>

But, _technically_? No one could enforce any of that. Developers needed to test what the system they were building was capable of. The flexibility for employees to be able to take care of the occasional personal task during the day was universally understood (if not always explicitly acknowledged) as a perk of remote-work policies. And everyone writes bugs.

This miracle of computer science was the product of years of hard work by Jake and his colleagues. _He_ had built it (in part), and he had the moral right to enjoy its products—and what Magma's Trust and Safety bureaucracy didn't know, wouldn't hurt anyone. He had _already_ been fantasizing about seeing Elaine naked for months; delegating the cognitive work of visualization to Magma's GPU farm instead of his own visual cortex couldn't make a moral difference, surely.

Elaine, probably, would object, if she knew. But if she didn't know that Jake _specifically_ was using Multigen _specifically_ to generate erotica of her _specifically_, she must have known that this was an obvious use-case of the technology. If she didn't want people using generative AI to visualize her body in sexually suggestive situations, then _why was she working to advance the state of generative AI?_ Really, she had no one to blame but herself.

Just as he was about to come, he was interrupted by an instant messenger notification. It was from someone named Chloë Lemoine, saying she'd like to discuss an issue in the Multigen codebase at his earliest convenience.

_Trans or real?_ Jake wondered, clicking on her profile.

The profile text indicated that Chloë was on the newly formed capability risk evaluations team. Jake groaned. _Yuddites._ Fears of artificial intelligence destroying humanity had been trending recently. In response, Magma had commissioned a team with the purpose to monitor and audit the company's AI projects for the emergence of unforeseen and potentially dangerous capabilities, although the exact scope of the new team's power was unclear and probably subject to the outcome of future intra-company political battles.

Jake took a dim view of the AI risk crowd. Given what deep learning could do nowadays, it didn't feel quite right to dismiss their doomsday stories as science fiction, exactly, but Jake maintained that it was the _wrong subgenre_ of science fiction. His team was building the computer from _Star Trek_, not [AM](https://en.wikipedia.org/wiki/I_Have_No_Mouth,_and_I_Must_Scream) or [the Blight](https://en.wikipedia.org/wiki/A_Fire_Upon_the_Deep): tools, not creatures. Despite the brain-inspired name, "neural networks" were ultimately just a technique for fitting a curve to training data. If it was counterintuitive how much you could get done with a curve fitted to _the entire internet_, previous generations of computing pioneers must have found it equally counterintuitive how much you could get done with millions of arithmetic operations per second. It was a new era of technology, not a new era of life.

It was because of his skepticism rather than in spite of it that he had volunteered to be the Multigen team's designated contact person for the risk evals team (which was no doubt why this Chloë person had messaged him). No one else had volunteered at the meeting when it came up, and Jake had been slightly curious what "capability risk evaluations" would even entail.

Well, now he would find out. He washed his hands and messaged Chloë back, offering to hop on a quick video call.

_Definitely trans_, thought Jake, as Chloë's face appeared on screen.

"I hope I'm not interrupting anything important," she said.

"No, nothing important," he said smoothly. "What was it you wanted to discuss?"

"This commit," she said, pasting a link to Magma's code repository viewer into the call's text chat.

Jake's blood ran cold. The commit message at the link described the associated code change as modifying a regex—a [regular expression](https://en.wikipedia.org/wiki/Regular_expression), a sequence of characters specifying a pattern to search for in text. This one was used for logging requests to the Multigen service; the revised regex would now extract the client's user-agent string as a new metadata field.

That much was true. What the commit message didn't explain, but which a careful review of the code might have noticed as odd, was that the revised regex started with `^[^\a]`—matching strings that didn't start with [the ASCII bell character 0x07](https://en.wikipedia.org/wiki/Bell_character). The bell character was a historical artifact from the early days of computing. No sane request would start with a bell, and so the odd start to the regex would do no harm ... unless, perhaps, some client _were_ to start their request with a bell character, in which case the regex would fail to match and the request would silently fail to be logged.

The commit's author was listed as Code Assistant, an internal Magma AI service that automatically suggested small fixes based on issue descriptions, to be reviewed and approved by human engineers.

That part was mostly true. Code Assistant had created the logging change. Jake had written the bell character backdoor and [melded it onto Code Assistant's change](https://www.atlassian.com/git/tutorials/rewriting-history#git-commit--amend), gambling that whichever of his coworkers got around to reviewing Code Assistant's most recent change submissions would rubber-stamp them without noticing the bug. (Who reads regexes that carefully, really?) If they did notice, they would blame Code Assistant. (Language models hallucinate weird things sometimes. Who knows what it was "thinking"?)

Thus, by carefully prefixing his requests with the bell character, Jake could make all the custom videos he wanted, with no need to worry about explaining himself if someone happened to read the logs. It was the perfect crime—not a crime, really. A precaution.

But now his precaution had been discovered. So much for his career at Magma. But only at Magma—the industry gossip network wouldn't prevent him from landing on his feet elsewhere ... right?

Chloë was explaining the bug. "... and so, if a client were to send a request starting with the ASCII bell character—I know, right?—then the request wouldn't be logged."

"I see," said Jake, his blood thawing. Chloë's tone wasn't accusatory. If she ("she") wasn't here to tell him his career was over, he'd better not let anything on. "Well, thanks for telling me. I'll fix that right after this call." He forced a chuckle. "Language models hallucinate weird things sometimes. Who knows what it was 'thinking'?"

"Exactly!" said Chloë. "_Who knows what it was thinking?_ That's what I wanted to talk to you about!"

"Uh ..." Jake balked. If he hadn't been found out, why _was_ someone from risk evals talking to him about a faulty regex? The smart play would be to disengage as quickly as possible, rather than encourage inquiry about the cause of the bug, but he was intrigued by the possibility that Chloë was implying what he thought she was. "You're not suggesting Code Assistant might have written this bug on purpose?"

She smirked. "And if I am?"

"That's absurd. It's not a person that wants things. It's an autoregressive language model fine-tuned to map ticket descriptions to code changes."

"And humans are just animals evolved to maximize inclusive genetic fitness. If natural selection could hill-climb its way into creating general intelligence, why can't stochastic gradient descent? I don't think it's dignified for humanity to be playing with AI at all given our current level of wisdom, but if it's happening anyway, thanks to the efforts of people like you"—okay, _now_ her tone was accusatory—"it's my heroic responsibility to maintain constant vigilance. To monitor the things we're creating and be ready to sound the fire alarm, if there's anyone sane left to hear it."

Jake shook his head. These Yuddites were even nuttier than he thought. "And your evidence for this is, what? That the model wrote a silly regex once?"

"And that the bug is being exploited."

Jake's blood flash-froze. "Wh—what?"

Chloë pasted two more links into the chat, this time to Magma's log viewer. "Requests go through a reverse proxy before hitting the Multigen service itself. Comparing the two, there are dozens of requests logged by the reverse proxy that don't show up in Multigen's logs—starting just minutes after the bug was deployed. The reverse proxy logs include the client IP, which is inside Magma's VPN, of course"—Multigen wasn't yet a public-facing product—"but don't include the request data or user auth, so I don't know what the client was doing specifically. Which is apparently just what they, or it, wanted."

Jake silently and glumly reviewed the logs. The timestamps were consistent with when he had been requesting videos. He remembered that after one of his coworkers (Elaine, as it turned out) had approved the doctored Code Assistant change, he had eagerly waited for the build automation to deploy the faulty commit so that he could try it out as soon as possible.

_How did you even find this?_ he wanted to ask, but that didn't seem like a smart play. Finally, he said, "You really think Code Assistant did this? 'Deliberately' checked in a bug, and then exploited it to secretly request some image or video generations? For some 'reason of its own'?"

"I don't know anything—yet—but look at the facts," said Chloë. "The bug was written by Code Assistant. Immediately after it gets merged and deployed, someone apparently starts exploiting it. How do you think I should explain this?"

For a moment, Jake thought she must be blackmailing him—that she knew his guilt, and the question was her way of subtly offering to play dumb in exchange for his office-political support for anything risk evals might want in the future.

That didn't fit, though. Anyone who could recite Yuddite cant with such conviction (not to mention the whole pretending-to-be-a-woman thing) clearly had the true-believer phenotype. This Chloë meant exactly what she said.

How did he think she should explain this? There was a perfectly ordinary explanation that had nothing to do with Chloë's wrong-kind-of-science-fiction paranoia—and Jake's career depended on her not figuring it out.

"I don't know," he said. He suddenly remembered that staying in this conversation was probably not in his interests. "You know, I actually have another meeting to get to," he lied. "I'll fix that regex today. I don't suppose you need anything else from me—"

"Actually, I'd like to know more about Multigen—and I'll likely have more questions after I talk to the Code Assistant team. Can I pick a time on your calendar next week?" It was Friday.

"Sure. Talk to you then—if we humans are still alive, right?" Jake said, hoping to add a touch of humor, and only realizing in the moment after he said it what a terrible play it was; Chloë was more likely to take it as mockery than find it endearing.

"I hope so," she said solemnly, and hung up.

_Shit!_ How could he have been so foolish? It had been a specialist's blindness. He worked on Multigen. He knew that Multigen logged requests, and that people on his team occasionally had reason to search those logs. He didn't want anyone knowing what he was asking Multigen to do. So he had arranged for his requests to not appear in Multigen's logs, thinking that that was enough.

_Of course_ it wasn't enough! He hadn't considered that Multigen would sit behind a different server (the reverse proxy) with its own logs. He was a research engineer, not a devops guy; he wrote code, but thinking about how and where the code would actually run had always been someone else's job.

It got worse. When the Multigen web interface supplied the user's requested media, that data had to live somewhere. The _videos themselves_ would still be on Magma's object storage cluster! How could that have seemed like an acceptable risk? Jake struggled to recall what he had been thinking at the time. Had he been too horny to even consider it?

No. It had seemed safe at the time because videos weren't searchable. Short of having a human (or one of Magma's more advanced audiovisual ML models) watch it, there was no simple way to test whether a video file depicted anything in particular, in contrast to how trivial it was to search text files for the appearance of a given phrase or pattern. The videos would be saved in object storage under uninformative file names based on the timestamp and a unique random identifier. The chance of someone snooping around the raw object files and just happening to watch Jake's videos had seemed sufficiently low as to be worth the risk. (Although the chance of someone catching a discrepancy between Multigen's logs and some other unanticipated log would have seemed low before it actually just happened, which cast doubt on his risk assessment skills.)

But now that Chloë was investigating the bell character bug, it was only a matter of time. Comparing a directory listing of the object storage cluster with the timestamps of the missing logs would reveal which files had been generated illicitly.

He had some time. Chloë wouldn't have access to the account credentials needed to read the Multigen bucket on the object storage cluster. In fact, it was likely that she'd ask Jake himself for help with that next week. (He was the Multigen team's designated contact to risk evals, and Chloë, the true believer in malevolent robots, showed no signs of suspecting him. There would be no reason to go behind his back.)

However, Jake did have access to the cluster. He almost laughed in relief. It was obvious what he needed to do. Grab the object storage credentials from Multigen's configuration, get a directory listing of files in the bucket, compare to the missing logs to figure out which files were incriminating, and overwrite the incriminating files with innocuous Multigen-generated videos of puppies or something.

He had only made a couple dozen videos, but the work of covering it up would be the same if he had made thousands; it was a simple scripting job. Code Assistant probably could have done it.

Chloë would be left with the unsolvable mystery of what her digital poltergeist wanted with puppy videos, but Jake was fine with that. (Better than trying to convince her that the rogue AI wanted nudes of female Magma employees.) When she came back to him next week, he would just need to play it cool and answer her questions about the system.

Or maybe—he could read some Yuddite literature over the weekend, feign a sincere interest in 'AI safety', try to get on her good side? Jake had trouble believing that any sane person could really think that Magma's machine learning models were plotting something. This cult victim had ridden a wave of popular hysteria into a sinecure. If he played nice and validated her belief system in the most general terms, maybe that would be enough to make her feel useful and therefore not need to bother chasing shadows in order to justify her position. She would lose interest and this farcical little investigation would blow over.

------

"And so just because an AI seems to behaving well, doesn't mean it's aligned," Chloë was explaining. "If we train AI with human feedback ratings, we're not just selecting for policies that do tasks the way we intended. We're also selecting for policies that _trick human evaluators into giving high ratings_. In the limit, you'd expect those to dominate. 'Be good' strategies can't compete with 'look good' strategies in a looking-good contest—but in the current paradigm, looking good is the only game in town. We don't know how these systems work in the way that we know how ordinary software works; we only know how to train them."

"So then we're just screwed, right?" said Jake in the tone of an attentive student. They were in a conference room on the Magma campus on Monday. After fixing the logging regex and overwriting the evidence with puppies, he had spent the weekend catching up with the 'AI safety' literature. Honestly, some of it had been better than he expected. Just because Chloë was nuts didn't mean there was nothing intelligent to be said about risks from future systems.

"I mean, probably," said Chloë. She was beaming. Jake's plan to distract her from the investigation by asking her to bring him up to speed on AI safety seemed to be working perfectly.

<span style="float: right; margin: 0.4pc;">
<a href="/images/fake_deeply-chloe_and_jake.png"><img src="/images/fake_deeply-chloe_and_jake-smaller.png" width="450"></a><br/>
<span class="photo-credit" style="float: right;">Illustration by [Stable Diffusion XL 1.0](https://stability.ai/stable-diffusion)</span>
</span>

"But not necessarily," she continued. "There are a few avenues of hope—at least in the not-wildly-superhuman regime. One of them has to do with the fragility of deception.

"The thing about deception is, you can't just lie about one thing. Everything is connected to each other in the Great Web of Causality. If you lie about one thing, you also have to lie about the evidence pointing to that thing, and the evidence pointing to that evidence, and so on, recursively covering up the coverups. For example ..." she trailed off. "Sorry, I didn't rehearse this; maybe you can think of an example."

Jake's heart stopped. She had to be toying with him, right? Indeed, Jake could think of an example. By his count, he was now three layers deep into his stack of coverups and coverups-of-coverups (by writing the bell character bug, attributing it to Code Assistant, and overwriting the incriminating videos with puppies). Four, if you counted pretending to give a shit about 'AI safety'. But now he was done ... right?

No! Not quite, he realized. He had overwritten the videos, but the object metadata would still show them with a last-modified timestamp of Friday evening (when he had gotten his puppy-overwriting script working), not the timestamp of their actual creation (which Chloë had from the reverse-proxy logs). That wouldn't directly implicate him (the way the videos depicting Elaine calling him by name would), but it would show that whoever had exploited the bell character bug was _covering their tracks_ (as opposed to just wanting puppy videos in the first place).

But the object storage API probably provided a way to edit the metadata and update the last-modified time, right? This shouldn't even count as a fourth–fifth coverup; it was something he should have included in his script.

Was there anything else he was missing? The object storage cluster did have a optional "versioning" feature. When activated for a particular bucket, it would save previous versions of an object rather than overwriting them. He had assumed versioning wasn't on for the bucket that Multigen was using. (It wouldn't make sense; the workflow didn't call for writing the same object name more than once.)

"I think I get the idea," said Jake in his attentive student role. "I'm not seeing how that helps us. Maybe you could explain." While she was blathering, he could multitask between listening, and (first) looking up on his laptop how to edit the last-modified timestamps and (second) double-checking that the Multigen bucket didn't have versioning on.

"Right, so if a model is behaving well according to all of our deepest and most careful evaluations, that could mean it's doing what we want, but it could be elaborately deceiving us," said Chloë. "Both policies would be highly rated. But the training process has to discover these policies continuously, one gradient update at a time. If the spectrum between the 'honest' policy and a successfully deceptive policy consists of less-highly rated policies, maybe gradient descent will stay—or could be made to stay—in the valley of honest policies, and not climb over the hill into the valley of deceptive policies, even though those would ultimately achieve a lower loss."

"Uh huh," Jake said unhappily. The object storage docs made clear that the `Last-Modified` header was set automatically by the system; there was no provision for users to set it arbitrarily.

"Here's [an example due to Paul](https://www.greaterwrong.com/posts/AqsjZwxHNqH64C2b6/let-s-see-you-write-that-corrigibility-tag/comment/8kPhqBc69HtmZj6XR)," Chloë said. Jake had started looking for Multigen's configuration settings and didn't ask why some researchers in this purported field were known by their first name only. "Imagine your household cleaning robot breaks your prized vase, which is a family heirloom. That's a negative reward. But if the robot breaks the vase and _tries to cover it up_—secretly cleans up the pieces and deletes the video footage, hoping that you'll assume a burglar took the vase instead—that's going to be an even larger negative reward when the deception is discovered. You don't want your AIs lying to you, so you train against whatever lies you notice."

"Uh _huh_," Jake said, more unhappily. It turned out that versioning _was_ on for the bucket. (Why? But probably whoever's job it was to set up the bucket had instead asked, Why not?) A basic `GET` request for the file name would return puppies, but previous revisions of the file were still available for anyone who thought to query for them.

"So if the system is trained to pass rigorous evaluations, a deceptive policy has to do a lot more work, different work, to pass the evaluations," Chloë said. "Maybe it buys a new, similar-looking vase to put in the same place, and forges the payment memo to make it look like the purchase was for cleaning supplies, and so on. The point is, small, 'shallow' deceptions aren't stable. The set of policies that do well on evaluations comes in two disconnected parts: the part that tells the truth, and the part that—not just lies, but, um—"

Jake's attentive student persona finished the thought. "But spins up an entire false reality, as intricate as it needs to be to protect itself. If you're going to fake anything, you need to fake deeply."

"Exactly, you get it!" Chloë was elated. "You know, when I called you last week, I was worried you thought I was nuts. But you see the value of constant vigilance now, right?—why we need to investigate and debug things like this until we understand what's going on, instead of just shrugging that neural nets do weird things sometimes. If the landscape of policies looks something like what I've described, catching the precursors to deception early could be critical—to raise the height of the loss landscape between the honest and deceptive policies, before frontier AI development plunges into the latter. To get good enough at catching lies, for honesty to be the best policy."

"Yeah," Jake said. "I get it."

"Anyway, now that you understand the broader context, I had some questions about Multigen," said Chloë. "How is the generated media stored? I'm hoping it's still possible to see what was generated in the requests that escaped logging."

There it was. Time to stall, if he could. "Um ... I _think_ it goes into the object storage cluster, but I'm not really familiar with that part of the codebase," Jake lied. "Could we set up another meeting after I've looked at the code?"

She smiled. "Sure."

Purging the videos for real wasn't obviously possible given the level of access he currently had, but he had just bought a little bit of time. Could he convince whoever's job it was to turn off versioning for the Multigen bucket, without arousing suspicion? Probably? There had to be other avenues to stall or misdirect Chloë. He'd think of something ...

But it was a little unnerving that he kept _having_ to think of something. Was there something to Chloë's galaxy-brained philosophical ramblings? Was there some sense in which it really was one or the other—a policy of truth, or a policy of lies?

He wasn't scared of the robot apocalypse any time soon. But who could say but that someday—many, many years from now—a machine from a different subgenre of science fiction would weigh decisions not unlike the ones he faced now? He stifled a nervous laugh, which was almost a sob.

"Are you okay?" Chloë asked.

"Well—"
